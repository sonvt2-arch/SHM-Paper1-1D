"""Package 1B - optimal invariant multi-channel estimation: shared core.

Structural models, invariance constants C(x) for every candidate position,
influence lines, the integral-noise covariance and the estimators.

Units: kN, m for the structure.  Deflection channels in mm, strain channels in
microstrain.  A channel integral I_j = int z_j dx is in mm*m (deflection) or
ue*m (strain); C_j in mm*m/kN or ue*m/kN; the load P in kN.

Models
  prismatic beams  : code/analysis/cm_multispan.py (Hermite FE, uniform EI)
  Cau May 55+90+55 : code/analysis/wp3_fe.py (haunched EI(x), L_v = 44 m,
                     rotational springs at the monolithic inner piers), with the
                     two calibrations of manuscript Section 4.2 (values from
                     code/analysis/logs/wp3_run.log):
                       A: design EI, k = 2.748e7 kN m/rad
                       B: alpha = 0.716, k = 1.199e8 kN m/rad
Existing files are imported, never modified.
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "code", "analysis"))
import cm_multispan as cms                          # noqa: E402
from wp3_fe import Bridge, haunch_EI                # noqa: E402

LOGS = os.path.join(HERE, "logs")
RES = os.path.join(HERE, "results")
FIGS = os.path.join(HERE, "figures")
for d in (LOGS, RES, FIGS):
    os.makedirs(d, exist_ok=True)

DX = 0.1            # sampling interval along the bridge (m)
ALLOW = 20.0        # record allowance for the convoy length (m): L_rec = L_beam + ALLOW
EI_PRISM = 1.0e7    # kN m^2, prismatic reference girder (10 mm under 250 kN, 30 m span)
C_FIBRE = 0.6       # m, neutral axis to bottom fibre (strain channels)
P_REF = 250.0       # kN, reference vehicle for relative errors (prismatic beams)
P_CM = 245.8        # kN, mean weighed Cau May test truck (manuscript Table 8)

E_C45 = 36.057e6    # kN/m^2 (manuscript Section 4.1)
CM_GEOM = dict(spans=(55.0, 90.0, 55.0), I_mid=5.482, I_pier=59.612, h_mid=2.40,
               h_pier=5.40, Lv=44.0)
CM_CAL = {"A": dict(alpha=1.0, k=2.748e7), "B": dict(alpha=0.716, k=1.199e8)}


class Model:
    """Beam with nodal grid x (spacing DX), deflection constant Cd(x) and,
    for prismatic beams, bottom-fibre strain constant Cs(x)."""

    def __init__(self, name, spans, kind="prism", cal=None, EIfun=None):
        self.name, self.spans, self.kind = name, tuple(spans), kind
        self.EIfun = EIfun if EIfun is not None else (lambda s: EI_PRISM)
        self.L = float(sum(spans))
        self.supports = np.concatenate([[0.0], np.cumsum(spans)])
        if kind == "prism":
            self._x, self._K, self._free, Fe = self._prism_fe()
            F = np.zeros(2 * len(self._x))
            for e in range(len(self._x) - 1):
                F[2 * e:2 * e + 4] += Fe[e]
            u = cms._solve(self._K, self._free, F)
            self.x = self._x
            self.Cd = 1e3 * u[0::2]                       # mm*m/kN
            self._uq = u
            self.Cs = np.array([self._curv_dot(j, u) for j in range(len(self.x))])
            self.Cs = -C_FIBRE * 1e6 * self.Cs            # ue*m/kN (sagging +)
        else:
            c = CM_CAL[cal]
            g = CM_GEOM
            EI, h, n = haunch_EI(g["spans"], E_C45, g["I_mid"], g["I_pier"],
                                 g["h_mid"], g["h_pier"], g["Lv"])
            self.EI_mid = E_C45 * g["I_mid"] * c["alpha"]
            self.br = Bridge(g["spans"], lambda xx: c["alpha"] * EI(xx), c["k"])
            self.x = self.br.x
            self.Cd = 1e3 * self.br.uniform(1.0)          # mm*m/kN
            self.Cs = None

    # ---- prismatic FE helpers (cm_multispan) --------------------------------
    def _prism_fe(self):
        # build mesh with element size DX in every span
        xs = [0.0]
        for L in self.spans:
            n = int(round(L / DX))
            xs += list(np.linspace(xs[-1], xs[-1] + L, n + 1)[1:])
        x = np.array(xs)
        n = len(x)
        import scipy.sparse as sps
        rows, cols, vals = [], [], []
        Fe = np.zeros((n - 1, 4))
        for e in range(n - 1):
            k, Fe[e] = cms.element(x[e], x[e + 1], self.EIfun)
            idx = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
            rows += idx * 4
            cols += [i for i in idx for _ in range(4)]
            vals += list(k.T.ravel())
        K = sps.csr_matrix((vals, (rows, cols)), shape=(2 * n, 2 * n))
        fixed = [2 * int(np.argmin(abs(x - s))) for s in self.supports]
        free = np.setdiff1d(np.arange(2 * n), fixed)
        return x, K, free, Fe

    def _curv_vec(self, j):
        """Nodal vector b with b.u = w''(x_j) (Hermite, element ending at node j)."""
        e = j - 1 if j > 0 else 0
        h = self._x[e + 1] - self._x[e]
        s = 1.0 if j > 0 else 0.0
        coef = np.array([(-6 + 12 * s) / h**2, (-4 + 6 * s) / h,
                         (6 - 12 * s) / h**2, (-2 + 6 * s) / h])
        b = np.zeros(2 * len(self._x))
        b[2 * e:2 * e + 4] = coef
        return b

    def _curv_dot(self, j, u):
        return self._curv_vec(j) @ u

    # ---- influence lines -----------------------------------------------------
    def il_defl(self, xm):
        """Deflection influence line at xm, mm/kN, on self.x."""
        j = int(np.argmin(abs(self.x - xm)))
        if self.kind == "prism":
            F = np.zeros(2 * len(self.x))
            F[2 * j] = 1.0
            return 1e3 * cms._solve(self._K, self._free, F)[0::2]
        return 1e3 * self.br.influence_line(self.x[j])

    def il_strain(self, xm):
        """Bottom-fibre strain influence line at xm, ue/kN (Maxwell-Betti dual)."""
        j = int(np.argmin(abs(self.x - xm)))
        u = cms._solve(self._K, self._free, self._curv_vec(j))
        return -C_FIBRE * 1e6 * u[0::2]

    def _full_solve(self, F):
        if self.kind == "prism":
            return cms._solve(self._K, self._free, F)
        u = np.zeros(2 * self.br.n)
        u[self.br.free] = self.br.lu.solve(F[self.br.free])
        return u

    def il_hermite(self, typ, xm):
        """Callable eta(xq) (mm/kN or ue/kN), cubic Hermite interpolation of the
        nodal deflections AND rotations (exact for prismatic elements); 0 outside."""
        j = int(np.argmin(abs(self.x - xm)))
        if typ == "d":
            F = np.zeros(2 * len(self.x))
            F[2 * j] = 1.0
            u, sc = self._full_solve(F), 1e3
        else:
            u, sc = self._full_solve(self._curv_vec(j)), -C_FIBRE * 1e6
        w, th, x = sc * u[0::2], sc * u[1::2], self.x
        L = self.L

        def f(xq):
            xq = np.asarray(xq, float)
            out = np.zeros_like(xq)
            m = (xq >= 0) & (xq <= L)
            xx = xq[m]
            e = np.clip(np.searchsorted(x, xx) - 1, 0, len(x) - 2)
            h = x[e + 1] - x[e]
            s = (xx - x[e]) / h
            out[m] = (w[e] * (1 - 3 * s**2 + 2 * s**3) + th[e] * h * (s - 2 * s**2 + s**3)
                      + w[e + 1] * (3 * s**2 - 2 * s**3) + th[e + 1] * h * (s**3 - s**2))
            return out
        return f

    def C(self, typ, xm):
        j = int(np.argmin(abs(self.x - xm)))
        return (self.Cd if typ == "d" else self.Cs)[j]

    def il(self, typ, xm):
        return self.il_defl(xm) if typ == "d" else self.il_strain(xm)


def prismatic_models():
    return {"2S-eq": Model("two-span 30+30 m", (30.0, 30.0)),
            "2S-r2": Model("two-span 30+60 m", (30.0, 60.0)),
            "3S-b1.4": Model("three-span 30+42+30 m", (30.0, 42.0, 30.0)),
            "3S-b2.0": Model("three-span 30+60+30 m", (30.0, 60.0, 30.0))}


def caumay_models():
    return {"CM-A": Model("Cầu Mây 55+90+55 m, calibration A", CM_GEOM["spans"], "cm", "A"),
            "CM-B": Model("Cầu Mây 55+90+55 m, calibration B", CM_GEOM["spans"], "cm", "B")}


# ---------------------------------------------------------------- noise model
def trap_weights(n, dx=DX):
    w = np.full(n, dx)
    w[0] = w[-1] = dx / 2
    return w


def lrec(model, allow=ALLOW):
    return model.L + allow


def noise_cov(types, sig, eps, rho, Lrec, dx=DX):
    """Covariance of the channel integrals I_j (trapezoid rule, N samples).
    types: list of 'd'/'s'; sig, eps: per-channel white-noise std per sample and
    offset std; rho: common-mode fraction of the offset among channels of the
    same type (offsets of different types independent).
      Sigma = diag(sig^2) * dx*(Lrec - dx/2) + Lrec^2 * D (rho*T + (1-rho) I) D."""
    types = list(types)
    k = len(types)
    sig, eps = np.asarray(sig, float), np.asarray(eps, float)
    T = np.array([[1.0 if types[a] == types[b] else 0.0 for b in range(k)]
                  for a in range(k)])
    R = rho * T + (1 - rho) * np.eye(k)
    return np.diag(sig**2) * dx * (Lrec - dx / 2) + Lrec**2 * np.outer(eps, eps) * R


def gls(C, S):
    """Minimum-variance invariant linear estimator: w = S^-1 C / (C' S^-1 C)."""
    C = np.asarray(C, float)
    a = np.linalg.solve(S, C)
    J = C @ a
    return a / J, 1.0 / J


def immune(C, S, types):
    """Offset-immune estimator: min w'Sw s.t. w'C = 1 and sum_{j in type} w_j = 0
    for every channel type present at least twice (common-mode offset cancels)."""
    C = np.asarray(C, float)
    types = list(types)
    cols = [C]
    for t in sorted(set(types)):
        idx = [i for i, tt in enumerate(types) if tt == t]
        if len(idx) >= 2:
            cols.append(np.array([1.0 if tt == t else 0.0 for tt in types]))
    M = np.column_stack(cols)
    if M.shape[1] > len(C) or np.linalg.matrix_rank(M) < M.shape[1]:
        return None, np.inf
    SiM = np.linalg.solve(S, M)
    F = M.T @ SiM
    Fi = np.linalg.inv(F)
    w = SiM @ Fi[:, 0]
    return w, Fi[0, 0]


def channel_defaults(types, sig_d=0.01, eps_d=0.1, sig_s=1.0, eps_s=2.0):
    sig = [sig_d if t == "d" else sig_s for t in types]
    eps = [eps_d if t == "d" else eps_s for t in types]
    return sig, eps


def matched_filter_var(ils, sig, eps, rho, types, dx=DX):
    """Variance of the (non-invariant) matched filter for one axle at a known
    position: P_hat = s' Cov^-1 z / s' Cov^-1 s with s_j = eta_j sampled, Cov =
    white noise + random offsets (Woodbury).  eps = 0 gives the white-noise MF."""
    k = len(ils)
    sig, eps = np.asarray(sig, float), np.asarray(eps, float)
    N = len(ils[0])
    a = np.array([np.sum(s**2) for s in ils]) / sig**2           # s'D^-1 s per channel
    u = np.array([np.sum(s) for s in ils]) / sig**2              # U'D^-1 s
    info = a.sum()
    if np.any(eps > 0):
        types = list(types)
        T = np.array([[1.0 if types[i] == types[j] else 0.0 for j in range(k)]
                      for i in range(k)])
        Se = np.outer(eps, eps) * (rho * T + (1 - rho) * np.eye(k))
        Se = Se + 1e-12 * np.eye(k) * np.max(np.diag(Se))
        Mmat = np.linalg.inv(Se) + np.diag(N / sig**2)
        info -= u @ np.linalg.solve(Mmat, u)
    return 1.0 / info


def O_k(C, ils, sig, Lrec, dx=DX):
    """Multi-channel price of invariance under white noise (no offsets):
    O_k = sqrt(Var_MF / Var_GLS) = sqrt( sum C_j^2/(sig_j^2 Lrec) /
                                          sum int eta_j^2 / sig_j^2 )."""
    C, sig = np.asarray(C, float), np.asarray(sig, float)
    num = np.sum(C**2 / sig**2) / Lrec
    den = np.sum([np.sum(s**2) * dx / sg**2 for s, sg in zip(ils, sig)])
    return np.sqrt(num / den)


class Logger:
    def __init__(self, name):
        self.f = open(os.path.join(LOGS, name), "w")

    def __call__(self, *a):
        s = " ".join(str(v) for v in a)
        print(s)
        self.f.write(s + "\n")
        self.f.flush()
