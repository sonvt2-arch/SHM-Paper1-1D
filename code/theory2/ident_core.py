"""Package 1C - shared core for the identifiability study of Cau May.

Re-assembles the WP3 Euler-Bernoulli model (same mesh, same EI(x) law, same
spring placement as code/analysis/wp3_fe.Bridge) so that the girder
stiffness K_g, the pier-spring pattern K_p and a consistent mass matrix M are
available separately:   K(alpha, k) = alpha*K_g + k*K_p.
Existing modules are imported, never modified.  Units kN, m, t, s.
"""
import os
import sys
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import splu, eigsh

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "code", "analysis"))
from wp3_fe import Bridge, haunch_EI                    # noqa: E402
import wp3_run as W                                     # noqa: E402

LOGD = os.path.join(HERE, "logs")
FIGD = os.path.join(HERE, "figures")
os.makedirs(LOGD, exist_ok=True)
os.makedirs(FIGD, exist_ok=True)

g = W.g
E = W.E_C45
SPANS = (55.0, 90.0, 55.0)
CM = dict(I_mid=5.482, I_pier=59.612, h_mid=2.40, h_pier=5.40,
          A_mid=7.233, A_pier=14.437, A_onpier=29.945, A_endpier=16.127)
X_N8, X_N7 = 178.0, 100.0          # installed gauges (wp3_run.PRIMARY)
X_N8MID = 172.5
EI_MID = E * CM["I_mid"]


class Logger:
    def __init__(self, name):
        self.path = os.path.join(LOGD, name)
        self.lines = []

    def __call__(self, *a):
        s = " ".join(str(v) for v in a)
        print(s)
        self.lines.append(s)

    def save(self):
        with open(self.path, "w") as f:
            f.write("\n".join(self.lines) + "\n")


def EI_law(Lv=44.0, n_override=None):
    EI, h, n = haunch_EI(SPANS, E, CM["I_mid"], CM["I_pier"], CM["h_mid"],
                         CM["h_pier"], Lv)
    if n_override is not None:
        n = n_override
        EI = lambda x, h=h, n=n: E * CM["I_mid"] * (h(x) / CM["h_mid"]) ** n
    return EI, h, n


# ------------------------------------------------------------- mass model
MASS_CASES = {
    # rho_c [t/m3], asphalt thickness [m], barrier+kerb per side [t/m],
    # include pier/end diaphragms, A(h) law
    "low":  dict(rho=2.40, t_as=0.05, barrier=0.30, diaph=False, Alaw="power"),
    "base": dict(rho=2.50, t_as=0.07, barrier=0.50, diaph=True, Alaw="linear"),
    "high": dict(rho=2.55, t_as=0.10, barrier=1.00, diaph=True, Alaw="linear"),
}
RHO_AS = 2.25        # t/m3 bituminous wearing surface (AASHTO LRFD Tab. 3.5.1-1)
W_CARR = 11.0        # m, 12.0 m deck minus 2 x 0.5 m kerbs (INVENTORY sec.1)
L_DIAPH_PIER = 3.0   # m, [NEED VALUE] assumed diaphragm length over T6/T7
L_DIAPH_END = 2.0    # m, [NEED VALUE] assumed end-diaphragm length at T5/T8


def area_law(h, law):
    hm, hp, Am, Ap = CM["h_mid"], CM["h_pier"], CM["A_mid"], CM["A_pier"]
    if law == "linear":
        return Am + (Ap - Am) * (h - hm) / (hp - hm)
    p = np.log(Ap / Am) / np.log(hp / hm)
    return Am * (h / hm) ** p


def mass_fn(case="base", Lv=44.0):
    c = MASS_CASES[case]
    _, h, _ = EI_law(Lv)
    sup = np.concatenate([[0.0], np.cumsum(SPANS)])
    sdl = RHO_AS * c["t_as"] * W_CARR + 2 * c["barrier"]

    def m(x):
        x = np.asarray(x, float)
        A = area_law(h(x), c["Alaw"])
        if c["diaph"]:
            dp = np.minimum(abs(x - sup[1]), abs(x - sup[2]))
            de = np.minimum(abs(x - sup[0]), abs(x - sup[3]))
            A = np.where(dp < L_DIAPH_PIER / 2, CM["A_onpier"], A)
            A = np.where(de < L_DIAPH_END / 2, CM["A_endpier"], A)
        return c["rho"] * A + sdl
    return m, sdl


# ------------------------------------------------------------- FE model
class Model:
    """Same discretisation as wp3_fe.Bridge (ne elements per metre)."""

    def __init__(self, EI, mass=None, ne=10, spans=SPANS):
        self.spans = np.asarray(spans, float)
        self.sup = np.concatenate([[0.0], np.cumsum(self.spans)])
        xs = [0.0]
        for a, b in zip(self.sup[:-1], self.sup[1:]):
            n = int(round((b - a) * ne))
            xs += list(np.linspace(a, b, n + 1)[1:])
        self.x = x = np.array(xs)
        n = len(x)
        self.n = n
        h = np.diff(x)
        xm = 0.5 * (x[:-1] + x[1:])
        EIe = EI(xm) * np.ones(n - 1)
        me = mass(xm) * np.ones(n - 1) if mass is not None else np.zeros(n - 1)
        rK, cK, vK, vM = [], [], [], []
        for e in range(n - 1):
            he = h[e]
            k = EIe[e] / he ** 3 * np.array(
                [[12, 6 * he, -12, 6 * he], [6 * he, 4 * he * he, -6 * he, 2 * he * he],
                 [-12, -6 * he, 12, -6 * he], [6 * he, 2 * he * he, -6 * he, 4 * he * he]])
            mm = me[e] * he / 420 * np.array(
                [[156, 22 * he, 54, -13 * he], [22 * he, 4 * he * he, 13 * he, -3 * he * he],
                 [54, 13 * he, 156, -22 * he], [-13 * he, -3 * he * he, -22 * he, 4 * he * he]])
            idx = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
            for a in range(4):
                for b_ in range(4):
                    rK.append(idx[a]); cK.append(idx[b_])
                    vK.append(k[a, b_]); vM.append(mm[a, b_])
        N = 2 * n
        Kg = sp.csc_matrix((vK, (rK, cK)), shape=(N, N))
        Mf = sp.csc_matrix((vM, (rK, cK)), shape=(N, N))
        self.node = [int(np.argmin(abs(x - s))) for s in self.sup]
        fixed = [2 * i for i in self.node]
        self.free = np.setdiff1d(np.arange(N), fixed)
        self.rot_dof = [2 * i + 1 for i in self.node]          # all 4 supports
        pd = [2 * i + 1 for i in self.node[1:3]]                # inner piers
        Kp = sp.csc_matrix((np.ones(2), (pd, pd)), shape=(N, N))
        f = self.free
        self.Kg = Kg[f][:, f].tocsc()
        self.Kp = Kp[f][:, f].tocsc()
        self.M = Mf[f][:, f].tocsc()
        self.mass_total = float(np.sum(me * h))
        self._lu = {}
        self.N = N

    # ---- loads
    def point_load(self, xp, P=1.0):
        F = np.zeros(self.N)
        e = int(np.clip(np.searchsorted(self.x, xp) - 1, 0, self.n - 2))
        h = self.x[e + 1] - self.x[e]
        s = (xp - self.x[e]) / h
        Nn = [1 - 3 * s**2 + 2 * s**3, h * (s - 2 * s**2 + s**3),
              3 * s**2 - 2 * s**3, h * (-s**2 + s**3)]
        F[[2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]] += P * np.array(Nn)
        return F[self.free]

    def uniform_load(self, q=1.0):
        F = np.zeros(self.N)
        for e in range(self.n - 1):
            h = self.x[e + 1] - self.x[e]
            F[[2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]] += q * np.array(
                [h / 2, h * h / 12, h / 2, -h * h / 12])
        return F[self.free]

    def axle_load(self, xs, P):
        return sum(self.point_load(xa, p) for xa, p in zip(xs, P))

    # ---- solves
    def lu(self, k, alpha=1.0):
        key = (float(k), float(alpha))
        if key not in self._lu:
            if len(self._lu) > 8:
                self._lu.clear()
            self._lu[key] = splu((alpha * self.Kg + k * self.Kp).tocsc())
        return self._lu[key]

    def solve(self, F, k, alpha=1.0):
        return self.lu(k, alpha).solve(F)

    def full(self, uf):
        u = np.zeros(self.N)
        u[self.free] = uf
        return u

    def defl_at(self, u_full, xm):
        """Deflection at xm from a full dof vector (Hermite interpolation)."""
        e = int(np.clip(np.searchsorted(self.x, xm) - 1, 0, self.n - 2))
        h = self.x[e + 1] - self.x[e]
        s = (xm - self.x[e]) / h
        Nn = np.array([1 - 3 * s**2 + 2 * s**3, h * (s - 2 * s**2 + s**3),
                       3 * s**2 - 2 * s**3, h * (-s**2 + s**3)])
        return float(Nn @ u_full[[2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]])

    def Cm(self, xm, k, alpha=1.0):
        """C_m = deflection at xm under unit uniform load (Eq. 3)."""
        u = self.full(self.solve(self.uniform_load(), k, alpha))
        return self.defl_at(u, xm)

    def Cm_parts(self, xm, k, alpha=1.0):
        """C_m, A+, A- from the influence line (Maxwell-Betti)."""
        u = self.full(self.solve(self.point_load(xm), k, alpha))
        eta = u[0::2]
        c = np.trapezoid(eta, self.x)
        pos = np.trapezoid(np.clip(eta, 0, None), self.x)
        neg = np.trapezoid(np.clip(eta, None, 0), self.x)
        return c, pos, neg, eta, u

    def modes(self, k, alpha=1.0, nm=6):
        K = (alpha * self.Kg + k * self.Kp).tocsc()
        lam, V = eigsh(K, k=nm, M=self.M, sigma=0.0, which="LM")
        o = np.argsort(lam)
        lam, V = lam[o], V[:, o]
        return np.sqrt(lam) / (2 * np.pi), V


# ---------------------------------------------------- test loads (static)
def schemes():
    s = W.cm_schemes()
    return {k: dict(x=v["x"], P=v["P"] * g) for k, v in s.items()}


MEAS_ALL = {"N8": np.array(W.MEAS["CM_III_N8"]["all"]),
            "N7": np.array(W.MEAS["CM_IV_N7"]["all"])}
MEAS_MEAN = {k: v.mean() for k, v in MEAS_ALL.items()}
FE_REPORT = {"N8": W.MEAS["CM_III_N8"]["fe"], "N7": W.MEAS["CM_IV_N7"]["fe"]}


def static_pred(model, k, alpha=1.0, sch=None):
    """Predicted gauge deflections [mm] for scheme III (N8) and IV (N7)."""
    sch = sch or schemes()
    out = {}
    for gk, (xm, key) in {"N8": (X_N8, "CM_III_N8"), "N7": (X_N7, "CM_IV_N7")}.items():
        u = model.full(model.solve(model.axle_load(sch[key]["x"], sch[key]["P"]), k, alpha))
        out[gk] = model.defl_at(u, xm) * 1000
    return out


def norm_index(Cm, L, EIref=EI_MID):
    return 192 * EIref * Cm / L ** 4


def classify_mode(model, v, k):
    """Return ('S'|'A', dominant span) for a vertical mode vector."""
    u = model.full(v)
    w = u[0::2]
    x = model.x
    L = model.sup[-1]
    wl = np.interp(L - x, x, w)
    sym = np.linalg.norm(w - wl) < np.linalg.norm(w + wl)
    amp = [np.max(abs(w[(x >= a) & (x <= b)])) for a, b in zip(model.sup[:-1], model.sup[1:])]
    return ("S" if sym else "A"), int(np.argmax(amp)), w, amp
