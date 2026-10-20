"""Package 3 - field-test design: influence lines, predicted integrals, signal
levels and offset bias for (A) Mây Bridge main bridge 55+90+55 m and (B) a generic
2-3 span continuous overpass.

Stiffness assembly and solves use code/analysis/cm_multispan.py (imported, not
modified).  Rotational springs at the monolithic inner piers are added to the
stiffness matrix returned by cm_multispan.beam_fe.  The haunch law, Ec, I_mid,
I_pier, n, Lv and the calibrations (k_FE, alpha) are those of
code/analysis/wp3_run.py / logs/wp3_run.log (Lv = 44 m base case).

Run:  python3 code/fieldplan/fieldplan_compute.py
Outputs: code/fieldplan/results/*.csv, code/fieldplan/figures/*.png,
         code/fieldplan/results/fieldplan_compute.log
Units: kN, m, t (1 t = 9.81 kN).  Deflection positive downward.
"""
import os
import sys
import csv
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla
import scipy.linalg as sla
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "code", "analysis"))
import cm_multispan as cms                                  # noqa: E402

RES = os.path.join(HERE, "results")
FIG = os.path.join(HERE, "figures")
os.makedirs(RES, exist_ok=True)
os.makedirs(FIG, exist_ok=True)
LOG = open(os.path.join(RES, "fieldplan_compute.log"), "w", encoding="utf-8")


def log(*a):
    s = " ".join(str(v) for v in a)
    print(s)
    LOG.write(s + "\n")


g = 9.81

# ----------------------------------------------------------------- trucks
# Axle loads are ILLUSTRATIVE splits of the gross mass; the real values come
# from the per-axle weighbridge tickets on the test day.
TRUCKS = {
    # T1 = same type as the 2020 acceptance trucks (report Fig. 2.1): 5+10+10 t
    "T1 (3-axle, 25 t)": dict(P=np.array([5.0, 10.0, 10.0]), a=np.array([0.0, 3.60, 4.95])),
    # T2 = 4-axle (spacings 1.80+3.00+1.35 m) loaded to ~25 t: same total, other axles
    "T2 (4-axle, 25 t)": dict(P=np.array([5.5, 5.5, 7.0, 7.0]), a=np.array([0.0, 1.80, 4.80, 6.15])),
    # T3 = same 4-axle truck fully loaded, ~30 t: different total
    "T3 (4-axle, 30 t)": dict(P=np.array([6.0, 6.0, 9.0, 9.0]), a=np.array([0.0, 1.80, 4.80, 6.15])),
    # T4 = optional light 2-axle truck, ~12 t, wheelbase 4.5 m (to show P_eps scaling)
    "T4 (2-axle, 12 t, optional)": dict(P=np.array([4.0, 8.0]), a=np.array([0.0, 4.50])),
}
OFFSETS = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50]           # mm


# ----------------------------------------------------------------- model
class Model:
    """Continuous beam from cm_multispan.beam_fe + optional rotational springs."""

    def __init__(self, spans, EI, k_rot=0.0, ne_per_span=500, extra=()):
        self.spans = np.asarray(spans, float)
        self.sup = np.concatenate([[0.0], np.cumsum(self.spans)])
        x, K, free, Fe = cms.beam_fe(list(spans), ne_per_span=ne_per_span, EI=EI,
                                     extra_nodes=tuple(extra), return_load=True)
        n = len(x)
        self.x, self.Fe, self.EI = x, Fe, EI
        self.pier_nodes = [int(np.argmin(abs(x - s))) for s in self.sup[1:-1]]
        if k_rot > 0:
            r = [2 * i + 1 for i in self.pier_nodes]
            K = K + sps.csr_matrix((np.full(len(r), k_rot), (r, r)), shape=K.shape)
        self.K, self.free, self.n = K, free, n
        Kff = K[free][:, free].tocsc()
        d = 1.0 / np.sqrt(Kff.diagonal())
        self._d = d
        self._lu = spla.splu((sps.diags(d) @ Kff @ sps.diags(d)).tocsc())

    def solve(self, F):
        F = np.atleast_2d(F.T).T if F.ndim == 1 else F
        u = np.zeros((2 * self.n, F.shape[1]))
        u[self.free] = self._d[:, None] * self._lu.solve(self._d[:, None] * F[self.free])
        return u

    def node(self, xm):
        return int(np.argmin(abs(self.x - xm)))

    def il_defl(self, xm):
        F = np.zeros(2 * self.n); F[2 * self.node(xm)] = 1.0
        return self.solve(F)[0::2, 0]

    def il_rot(self, xm):
        """Rotation influence line at xm (Maxwell: deflection under unit moment)."""
        F = np.zeros(2 * self.n); F[2 * self.node(xm) + 1] = 1.0
        return self.solve(F)[0::2, 0]

    def uniform(self):
        F = np.zeros(2 * self.n)
        for e in range(self.n - 1):
            F[2 * e:2 * e + 4] += self.Fe[e]
        return self.solve(F)[:, 0]

    def moment_at(self, u, xs):
        """Sagging moment at node xs from the element to its left (exact for
        prismatic Hermite elements with nodal loads).  u: (2n, m) array."""
        i = self.node(xs)
        e = max(i - 1, 0)
        h = self.x[e + 1] - self.x[e]
        B = np.array([6.0, 2 * h, -6.0, 4 * h]) / h ** 2          # w'' at element end
        EIe = self.EI(0.5 * (self.x[e] + self.x[e + 1]))
        return -EIe * (B @ u[2 * e:2 * e + 4])

    def il_moment(self, xs):
        """Moment influence line at xs: unit load at every node (one factorization)."""
        F = np.zeros((2 * self.n, self.n))
        F[2 * np.arange(self.n), np.arange(self.n)] = 1.0
        u = self.solve(F)
        return self.moment_at(u, xs)

    def moment_uniform(self, xs):
        return float(self.moment_at(self.uniform()[:, None], xs)[0])


def crossing(x, eta, truck, v=None, dx=0.05):
    """Quasi-static record y(s) for the front axle at s, and its integral."""
    P = truck["P"] * g
    a = truck["a"]
    s = np.arange(x[0] - 5.0, x[-1] + a.max() + 5.0, dx)
    y = np.zeros_like(s)
    for Pi, ai in zip(P, a):
        y += Pi * np.interp(s - ai, x, eta, left=0.0, right=0.0)
    return s, y, np.trapezoid(y, s)


def peak(y):
    i = np.argmax(abs(y))
    return y[i], y.max(), y.min()


def area_parts(x, eta):
    return (np.trapezoid(eta, x), np.trapezoid(np.clip(eta, 0, None), x),
            np.trapezoid(np.clip(eta, None, 0), x))


# ======================================================================
# (A) MÂY BRIDGE 55+90+55
# ======================================================================
E = 36.057e6
I_MID, I_PIER, H_MID, H_PIER, LV = 5.482, 59.612, 2.40, 5.40, 44.0
N_EXP = np.log(I_PIER / I_MID) / np.log(H_PIER / H_MID)
SP = [55.0, 90.0, 55.0]
P1, P2 = 55.0, 145.0
A_MID, A_PIER = 7.233, 14.437                 # m2, LRFR p.5
ZC_MID, ZC_PIER = 1.572, 3.053                # soffit to centroid, LRFR p.5
RHO = 2.55                                    # t/m3 (25 kN/m3) [assumption]
M_SDL = 3.0                                   # t/m superimposed dead load [assumption, not given in the test report]


def h_cm(x):
    d = np.minimum(abs(x - P1), abs(x - P2))
    return np.where(d < LV, H_MID + (H_PIER - H_MID) * (1 - d / LV) ** 2, H_MID)


def EI_cm(alpha=1.0):
    return lambda x: alpha * E * I_MID * (h_cm(x) / H_MID) ** N_EXP


def zc_cm(x):
    return ZC_MID + (h_cm(x) - H_MID) * (ZC_PIER - ZC_MID) / (H_PIER - H_MID)


CAL = {   # wp3_run.log, Lv = 44 m
    "A (design EI, k_FE)": dict(alpha=1.0, k=2.748e7),
    "A' (alpha=1.088, k_FE)": dict(alpha=1.088, k=2.748e7),
    "B (alpha=0.716, k=1.2e8)": dict(alpha=0.716, k=1.199e8),
}
CAL_MAIN = ["A (design EI, k_FE)", "B (alpha=0.716, k=1.2e8)"]

# candidate sensor abscissae (x from end support T5)
X_N7MID, X_N8_04, X_N8MID = 100.0, 178.0, 172.5


def mass_matrix(x, mfun):
    n = len(x)
    rows, cols, vals = [], [], []
    for e in range(n - 1):
        h = x[e + 1] - x[e]
        m = mfun(0.5 * (x[e] + x[e + 1]))
        Me = m * h / 420 * np.array([[156, 22 * h, 54, -13 * h], [22 * h, 4 * h * h, 13 * h, -3 * h * h],
                                     [54, 13 * h, 156, -22 * h], [-13 * h, -3 * h * h, -22 * h, 4 * h * h]])
        idx = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
        rows += idx * 4
        cols += [i for i in idx for _ in range(4)]
        vals += list(Me.T.ravel())
    return sps.csr_matrix((vals, (rows, cols)), shape=(2 * n, 2 * n))


def freqs(model, mfun, nmode=4):
    M = mass_matrix(model.x, mfun)
    f = model.free
    Kd = model.K[f][:, f].toarray()
    Md = M[f][:, f].toarray()
    w2, V = sla.eigh(Kd, Md, subset_by_index=[0, nmode - 1])
    return np.sqrt(w2) / (2 * np.pi), V


def m_cm(x):
    A = A_MID + (h_cm(x) - H_MID) * (A_PIER - A_MID) / (H_PIER - H_MID)
    return RHO * A + M_SDL


log("=" * 78)
log("(A) Mây Bridge 55+90+55 m: n = %.3f, Lv = %.0f m, Ec = %.0f MPa" % (N_EXP, LV, E / 1e3))
models = {}
for name, c in CAL.items():
    models[name] = Model(SP, EI_cm(c["alpha"]), c["k"], ne_per_span=550,
                         extra=(X_N7MID, X_N8_04, X_N8MID))

# ---- C_m profile = uniform-load deflection (Eq. 3) and characteristic points
prof = {}
for name, m in models.items():
    w = m.uniform()[0::2]
    prof[name] = w
    x = m.x
    ms = (x > P1) & (x < P2)
    ss = x > P2
    i_main = np.argmax(np.where(ms, w, -np.inf))
    i_side = np.argmax(np.where(ss, w, -np.inf))
    # contraflexure of the uniform-load moment in N8 (sagging->hogging)
    Mq = np.array([m.moment_uniform(xx) for xx in x[ss][::5]])
    xs8 = x[ss][::5]
    zc = [0.5 * (xs8[j] + xs8[j + 1]) for j in range(len(Mq) - 1) if Mq[j] * Mq[j + 1] < 0]
    Mq7 = np.array([m.moment_uniform(xx) for xx in x[ms][::5]])
    xs7 = x[ms][::5]
    zc7 = [0.5 * (xs7[j] + xs7[j + 1]) for j in range(len(Mq7) - 1) if Mq7[j] * Mq7[j + 1] < 0]
    models[name].xstar_main = x[i_main]
    models[name].xstar_side = x[i_side]
    models[name].zero_M_N8 = zc
    models[name].zero_M_N7 = zc7
    log(f"[{name}] main-span optimum x* = {x[i_main]:.1f} m (xi = {(x[i_main]-P1)/90:.3f}), "
        f"C_m = {w[i_main]:.3e} m2/kN; side-span N8 optimum x = {x[i_side]:.1f} m "
        f"(xi from T8 = {(200-x[i_side])/55:.3f}), C_m = {w[i_side]:.3e}; "
        f"M_q = 0 in N8 at x = {[round(v,1) for v in zc]} (dist. from T7 {[round(v-P2,1) for v in zc]}); "
        f"in N7 at {[round(v,1) for v in zc7]}")

# choose sensor set (calibration A defines the optimum; the B shift is reported)
mA = models[CAL_MAIN[0]]
XS_SIDE = round(float(mA.xstar_side), 1)
XS_ZERO = round(float(mA.zero_M_N8[0]), 1)
SENS = [
    ("D1 N7 mid-span (xi* main span)", "defl", X_N7MID),
    ("D2 N8 mid-span (near-blind)", "defl", X_N8MID),
    ("D3 N8 0.4L (2020 position)", "defl", X_N8_04),
    (f"D4 N8 optimum x={XS_SIDE:g} m", "defl", XS_SIDE),
    ("D5 N6 0.4L (mirror of D3)", "defl", 22.0),
    (f"S1 bottom fiber, M_q=0 in N8 (x={XS_ZERO:g} m)", "strain", XS_ZERO),
    ("S2 bottom fiber mid-N7", "strain", X_N7MID),
    ("R1 girder rotation over pier T7", "rot", P2),
    ("R2 girder rotation over pier T6", "rot", P1),
]
# re-build with sensor nodes present
for name, c in CAL.items():
    models[name] = Model(SP, EI_cm(c["alpha"]), c["k"], ne_per_span=550,
                         extra=tuple(s[2] for s in SENS))

rows = []
ils = {}
for name, m in models.items():
    for lab, kind, xs in SENS:
        if kind == "defl":
            eta = m.il_defl(xs); unit = "mm"; scale = 1e3
            C = area_parts(m.x, eta)
        elif kind == "rot":
            eta = m.il_rot(xs); unit = "urad"; scale = 1e6
            C = area_parts(m.x, eta)
        else:
            Mil = m.il_moment(xs)
            fac = zc_cm(xs) / m.EI(xs)           # bottom-fiber strain per kN m
            eta = fac * Mil; unit = "ue"; scale = 1e6
            C = area_parts(m.x, eta)
            Cchk = fac * m.moment_uniform(xs)
            log(f"[check strain C] {name} {lab}: IL area {C[0]:.4e} vs uniform {Cchk:.4e}")
        ils[(name, lab)] = (m.x.copy(), eta, kind, unit, scale)
        R = C[0] / C[1] if C[1] > 0 else np.nan
        Nm = ""
        if kind == "defl":
            Lref = 90.0 if P1 < xs < P2 else 55.0
            Nm = 192 * E * I_MID * C[0] / Lref ** 4
        rec = dict(cal=name, sensor=lab, kind=kind, x=xs, C=C[0], Apos=C[1], Aneg=C[2], R=R, N=Nm)
        for tn, tr in TRUCKS.items():
            s, y, Iy = crossing(m.x, eta, tr)
            pk, ymax, ymin = peak(y * scale)
            rec[f"peak[{tn}]"] = pk
            rec[f"max[{tn}]"] = ymax
            rec[f"min[{tn}]"] = ymin
            rec[f"I[{tn}]"] = Iy * scale
        rows.append(rec)

with open(os.path.join(RES, "A_caumay_sensors.csv"), "w", newline="") as f:
    wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    wr.writeheader()
    wr.writerows(rows)

log("\n--- (A) sensor constants and predicted signals (peak = extreme of quasi-static record) ---")
log("units: defl C [m2/kN], record [mm], integral [mm*m]; strain C [m/kN *ue/1e6], record [ue], integral [ue*m]; rot record [urad]")
for r in rows:
    if r["cal"] == "A' (alpha=1.088, k_FE)":
        continue
    log(f"{r['cal'][:2]:2s} {r['sensor']:38s} C={r['C']:+.3e} R={r['R']:+.2f} "
        + (f"N={r['N']:+.3f} " if r['N'] != "" else "        ")
        + " | ".join(f"{tn[:2]} pk {r[f'peak[{tn}]']:+7.2f} [{r[f'min[{tn}]']:+.2f},{r[f'max[{tn}]']:+.2f}] I {r[f'I[{tn}]']:+8.2f}"
                     for tn in list(TRUCKS)[:3]))

# ---- identification quantities A vs B
log("\n--- (A) discriminating A vs B (pier stiffness / EI) ---")
for name in CAL:
    r = {x["sensor"]: x for x in rows if x["cal"] == name}
    d1, d2, d3 = (r[SENS[i][0]]["C"] for i in (0, 1, 2))
    log(f"[{name}] C(D2)/C(D1) = {d2/d1:.3f}; C(D3)/C(D1) = {d3/d1:.3f}; "
        f"R1 peak T1 = {r[SENS[7][0]]['peak[' + list(TRUCKS)[0] + ']']:+.1f} urad; "
        f"S1 integral T1 = {r[SENS[5][0]]['I[' + list(TRUCKS)[0] + ']']:+.2f} ue*m, "
        f"S1 peak T1 = {r[SENS[5][0]]['max[' + list(TRUCKS)[0] + ']']:+.2f}/{r[SENS[5][0]]['min[' + list(TRUCKS)[0] + ']']:+.2f} ue")

# k sweep around A for the ratio D3/D1 and the T7 rotation
log("\nk-sweep (design EI): k [kNm/rad] -> C(D3)/C(D1), C(D2)/C(D1), peak rot T7 (T1) [urad], f1,f2,f3 [Hz]")
ksweep = []
for k in [1e7, 2.748e7, 5e7, 1.199e8, 3e8, 1e9]:
    for alpha in (1.0, 0.716):
        m = Model(SP, EI_cm(alpha), k, ne_per_span=550, extra=tuple(s[2] for s in SENS))
        c1 = area_parts(m.x, m.il_defl(X_N7MID))[0]
        c2 = area_parts(m.x, m.il_defl(X_N8MID))[0]
        c3 = area_parts(m.x, m.il_defl(X_N8_04))[0]
        s, y, _ = crossing(m.x, m.il_rot(P2), TRUCKS[list(TRUCKS)[0]])
        mf = Model(SP, EI_cm(alpha), k, ne_per_span=60)
        f, _ = freqs(mf, m_cm, 3)
        ksweep.append((k, alpha, c3 / c1, c2 / c1, peak(y * 1e6)[0], *f))
        log(f"k={k:9.3e} alpha={alpha:5.3f}: D3/D1={c3/c1:.3f} D2/D1={c2/c1:.3f} "
            f"rotT7={peak(y*1e6)[0]:+6.1f} urad  f = {f[0]:.3f}, {f[1]:.3f}, {f[2]:.3f} Hz")
with open(os.path.join(RES, "A_caumay_k_sweep.csv"), "w", newline="") as fh:
    wr = csv.writer(fh)
    wr.writerow(["k_kNm_rad", "alpha", "C_D3_over_C_D1", "C_D2_over_C_D1", "rotT7_peak_T1_urad", "f1", "f2", "f3"])
    wr.writerows(ksweep)

log("\nfrequencies of the calibrations (mass: rho=2.55 t/m3 x A(h) + %.1f t/m SDL [assumption]):" % M_SDL)
fr = {}
for name, c in CAL.items():
    mf = Model(SP, EI_cm(c["alpha"]), c["k"], ne_per_span=60)
    f, V = freqs(mf, m_cm, 4)
    fr[name] = f
    log(f"[{name}] f1..f4 = " + ", ".join(f"{v:.3f}" for v in f) + " Hz; T1 = %.3f s" % (1 / f[0]))
log("measured (report, truck-excited, 'vertical' at mid-span): N6 3.43, N7 3.64, N8 3.63 Hz"
    " -> not the fundamental of this model; ambient test must resolve modes 1-4")

# dynamic validity
log("\nT_cr/T_1 for the main unit (L_tot = 200 m + wheelbase), calibration A f1:")
f1A = fr[CAL_MAIN[0]][0]
dyn = []
for v in [5, 10, 20, 30, 40, 60]:
    Tcr = (200 + 6.15) / (v / 3.6)
    dyn.append((v, Tcr, Tcr * f1A, 0.05 * v / 3.6 * 1000 / 100))
    log(f"v = {v:3d} km/h: T_cr = {Tcr:6.1f} s, T_cr/T1 = {Tcr*f1A:6.1f}; dx at 100 Hz = {v/3.6/100*100:.1f} cm")

# ---- offset bias table (Eq. 19)
bias_rows = []
for name in CAL_MAIN:
    for lab, kind, xs in SENS[:5]:
        C = [r for r in rows if r["cal"] == name and r["sensor"] == lab][0]["C"]
        for tn, tr in TRUCKS.items():
            P = tr["P"].sum() * g
            Lt = 200.0 + tr["a"].max()
            for e0 in OFFSETS:
                bias_rows.append(dict(cal=name, sensor=lab, truck=tn, P_kN=P, eps0_mm=e0,
                                      Peps_kN=e0 * 1e-3 * Lt / C,
                                      bias_pct=100 * e0 * 1e-3 * Lt / (C * P)))
with open(os.path.join(RES, "A_caumay_offset_bias.csv"), "w", newline="") as fh:
    wr = csv.DictWriter(fh, fieldnames=list(bias_rows[0].keys()))
    wr.writeheader()
    wr.writerows(bias_rows)
log("\n--- (A) offset bias (Eq. 19), truck T1 25 t, % ---")
log("sensor / cal | " + " ".join(f"{e:5.2f}mm" for e in OFFSETS))
for name in CAL_MAIN:
    for lab, _, _ in SENS[:5]:
        b = [r["bias_pct"] for r in bias_rows if r["cal"] == name and r["sensor"] == lab
             and r["truck"] == list(TRUCKS)[0]]
        log(f"{name[:2]} {lab:34s} | " + " ".join(f"{v:7.1f}" for v in b))
log("(T3 30 t: multiply by 25/30; T4 12 t: by 25/12)")

# check against manuscript Table 8 (0.05 mm, 25.06 t, L=200)
for name in CAL_MAIN:
    for lab, xs in (("N7", X_N7MID), ("N8 0.4L", X_N8_04)):
        C = area_parts(models[name].x, models[name].il_defl(xs))[0]
        log(f"[check Table 8] {name[:2]} {lab}: C_m = {C:.3e} m2/kN, bias(0.05 mm, 245.8 kN, 200 m) = "
            f"{100*0.05e-3*200/(C*245.8):.0f} %")

# ---- figures (A)
cols = {"A (design EI, k_FE)": "#1f5fa8", "A' (alpha=1.088, k_FE)": "#7aa6d6",
        "B (alpha=0.716, k=1.2e8)": "#c0392b"}
fig, ax = plt.subplots(4, 1, figsize=(10, 12.5), gridspec_kw=dict(height_ratios=[0.8, 1.2, 1.4, 1.4]))
# (a) elevation / layout
a0 = ax[0]
xx = np.linspace(0, 200, 801)
a0.fill_between(xx, 0, -h_cm(xx), color="#d9d9d9")
a0.plot(xx, -h_cm(xx), "k", lw=0.8)
a0.plot([0, 200], [0, 0], "k", lw=1.2)
for xp, lab in [(0, "T5 (bearing)"), (55, "T6 (monolithic)"), (145, "T7 (monolithic)"), (200, "T8 (bearing)")]:
    a0.plot([xp, xp], [-h_cm(np.array(xp)) if xp in (55, 145) else -2.4, -9], "k", lw=3 if xp in (55, 145) else 1.5)
    a0.text(xp, -10.3, lab, ha="center", fontsize=8)
a0.axhline(-7.5, color="#5dade2", lw=1, ls="--")
a0.text(100, -8.6, "water level (illustrative)", ha="center", fontsize=7, color="#2e86c1")
mk = {"defl": ("v", "#1f5fa8"), "strain": ("s", "#27ae60"), "rot": ("o", "#c0392b")}
for lab, kind, xs in SENS:
    sym, c = mk[kind]
    a0.plot(xs, 0.6, sym, color=c, ms=8)
    a0.text(xs, 1.3, lab.split()[0], ha="center", fontsize=8, color=c)
a0.set_ylim(-11, 2.4); a0.set_xlim(-5, 205)
a0.set_title("(a) Sensor layout (girder elevation exaggerated): D = deflection (HLS in box girder + non-contact reference), "
             "S = strain, R = tilt", fontsize=9)
a0.set_yticks([]); a0.set_xlabel("x from centerline of bearing T5 (m)")
# (b) C_m profile
for name, w in prof.items():
    ax[1].plot(models[name].x, w * 1e3 * 245.8, color=cols[name], lw=1.6,
               label=f"{name}")
ax[1].axhline(0, color="k", lw=0.6)
for lab, kind, xs in SENS[:5]:
    ax[1].axvline(xs, color="0.6", lw=0.6, ls=":")
    ax[1].text(xs, ax[1].get_ylim()[1] if False else 0, lab.split()[0], fontsize=7, rotation=90, va="bottom")
ax[1].set_ylabel("I_y = C_m P (mm*m)\nwith P = 25.06 t")
ax[1].set_title("(b) Predicted deflection integral at each sensor point = C_m(x)*P (Eq. 3: deflection under unit uniform load)", fontsize=9)
ax[1].legend(fontsize=8); ax[1].set_xlim(-5, 205)
# (c) deflection influence lines
for name in CAL_MAIN:
    for lab, ls in ((SENS[0][0], "-"), (SENS[1][0], "--"), (SENS[2][0], "-."), (SENS[3][0], ":")):
        x_, eta, kind, unit, sc = ils[(name, lab)]
        ax[2].plot(x_, eta * 1e3 * 100, ls, color=cols[name], lw=1.3,
                   label=f"{name[:2]} {lab}")
ax[2].axhline(0, color="k", lw=0.6)
ax[2].set_ylabel("eta (mm / 100 kN)"); ax[2].set_xlim(-5, 205)
ax[2].set_title("(c) Deflection influence lines at points D1-D4 (A: blue, B: red)", fontsize=9)
ax[2].legend(fontsize=7, ncol=2)
# (d) strain and rotation ILs
a3 = ax[3]
a3b = a3.twinx()
for name in CAL_MAIN:
    x_, eta, kind, unit, sc = ils[(name, SENS[5][0])]
    a3.plot(x_, eta * 1e6 * 100, "-", color=cols[name], lw=1.3, label=f"{name[:2]} S1 (ue/100 kN)")
    x_, eta, kind, unit, sc = ils[(name, SENS[6][0])]
    a3.plot(x_, eta * 1e6 * 100, "--", color=cols[name], lw=1.0, label=f"{name[:2]} S2 (ue/100 kN)")
    x_, eta, kind, unit, sc = ils[(name, SENS[7][0])]
    a3b.plot(x_, eta * 1e6 * 100, ":", color=cols[name], lw=1.6, label=f"{name[:2]} R1 T7 (urad/100 kN)")
a3.axhline(0, color="k", lw=0.6)
a3.set_ylabel("strain (ue / 100 kN)"); a3b.set_ylabel("rotation (urad / 100 kN)")
a3.set_xlabel("unit-load position x (m)"); a3.set_xlim(-5, 205)
h1, l1 = a3.get_legend_handles_labels(); h2, l2 = a3b.get_legend_handles_labels()
a3.legend(h1 + h2, l1 + l2, fontsize=7, ncol=3)
a3.set_title("(d) Strain influence lines (S1 at M_q=0 point, S2 at mid-N7) and rotation over pier T7", fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fA1_caumay_layout_IL.png"), dpi=200)
plt.close(fig)

# predicted crossing records
fig, ax = plt.subplots(2, 2, figsize=(10, 7))
for j, (lab, unit, sc) in enumerate([(SENS[0][0], "mm", 1e3), (SENS[2][0], "mm", 1e3),
                                     (SENS[5][0], "ue", 1e6), (SENS[7][0], "urad", 1e6)]):
    a = ax.flat[j]
    for name in CAL_MAIN:
        x_, eta, kind, unit_, sc_ = ils[(name, lab)]
        for tn, ls in zip(list(TRUCKS)[:3], ("-", "--", ":")):
            s, y, Iy = crossing(x_, eta, TRUCKS[tn])
            a.plot(s, y * sc, ls, color=cols[name], lw=1.1,
                   label=f"{name[:2]} {tn.split()[0]}  I={Iy*sc:.1f}")
    a.axhline(0, color="k", lw=0.5)
    a.set_title(lab, fontsize=9); a.set_ylabel(unit)
    a.set_xlabel("front axle position (m)")
    a.legend(fontsize=6.5)
fig.suptitle("Predicted quasi-static records (single moving truck, no dynamics); I = integral over space", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fA2_caumay_predicted_records.png"), dpi=200)
plt.close(fig)

# bias vs offset
fig, ax = plt.subplots(figsize=(7.5, 4.8))
e = np.logspace(-2, np.log10(0.5), 60)
for name in CAL_MAIN:
    for lab, ls in ((SENS[0][0], "-"), (SENS[1][0], "--"), (SENS[2][0], "-."), (SENS[3][0], ":")):
        C = [r for r in rows if r["cal"] == name and r["sensor"] == lab][0]["C"]
        P = TRUCKS[list(TRUCKS)[0]]["P"].sum() * g
        ax.loglog(e, 100 * e * 1e-3 * 205 / (abs(C) * P), ls, color=cols[name], label=f"{name[:2]} {lab}")
ax.axhline(5, color="k", lw=0.6); ax.axhline(2, color="k", lw=0.6, ls=":")
ax.text(0.011, 5.4, "5 %", fontsize=8); ax.text(0.011, 2.15, "2 %", fontsize=8)
ax.set_xlabel("residual zero offset after load-zero eps0 (mm)")
ax.set_ylabel("load error |dP/P| (%) - truck T1 25 t")
ax.set_title("Eq. (19): expected accuracy vs. offset level, L_tot = 205 m", fontsize=9)
ax.legend(fontsize=7); ax.grid(True, which="both", lw=0.3)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fA3_caumay_bias_vs_offset.png"), dpi=200)
plt.close(fig)

# ======================================================================
# (B) GENERIC 2-3 SPAN CONTINUOUS OVERPASS (prismatic, bearings)
# ======================================================================
log("\n" + "=" * 78)
log("(B) generic overpass, prismatic, on bearings (pinned supports)")
# closed form, Eq. (8): mid side and xi* vs beta
log("Eq.(8) 3 spans uniform EI: beta -> N(mid side), xi*, N(xi*), N(mid main) [FE]")
selrows = []
for beta in [1.0, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]:
    mu = 2 * beta ** 3 / (3 * beta) if False else 2 * (1 + beta ** 3) / (2 + 3 * beta)
    F = lambda xi: xi * (1 - 2 * xi ** 2 + xi ** 3) - mu / 2 * xi * (1 - xi ** 2)
    xi = np.linspace(0.01, 0.99, 9801)
    Nmid = 8 * F(0.5)
    Ns = 8 * F(xi)
    ist = np.argmax(Ns)
    spans = [1.0, beta, 1.0]
    cmain, _, _ = cms.Cm(spans, 1 + beta / 2, ne_per_span=200)
    Nmain = 192 * cmain / beta ** 4
    selrows.append((beta, Nmid, xi[ist], Ns[ist], Nmain))
    log(f"beta={beta:4.2f}: N(mid side)={Nmid:+.3f}  xi*={xi[ist]:.3f} N(xi*)={Ns[ist]:+.3f}  N(mid main)={Nmain:+.3f}")
log("2 spans uniform EI, mid-span sensor: rho_L -> N")
for rho in [1.0, 1.2, 1.3, 1.4, 1.45743, 1.5]:
    mu = (1 + rho ** 3) / (1 + rho)
    log(f"rho_L={rho:.3f}: N(mid) = {8*(0.5*(1-0.5+0.0625) - mu/2*0.5*0.75):+.3f}")
with open(os.path.join(RES, "B_selection_beta.csv"), "w", newline="") as fh:
    wr = csv.writer(fh)
    wr.writerow(["beta", "N_mid_side", "xi_star", "N_xi_star", "N_mid_main"])
    wr.writerows(selrows)

# example: 25 + 40 + 25 m, EI assumed
SPB = [24.0, 40.0, 24.0]   # beta = 1.667 (near-blind band of Eq. 9)
EIB = 6.0e7         # kN m2  [ASSUMPTION: PC box/slab h ~ 1.8-2.0 m; replace with design value]
MB = 18.0           # t/m    [ASSUMPTION]
betaB = SPB[1] / SPB[0]
LtB = sum(SPB)
muB = 2 * (1 + betaB ** 3) / (2 + 3 * betaB)
xiB = np.linspace(0.01, 0.99, 9801)
FB = xiB * (1 - 2 * xiB ** 2 + xiB ** 3) - muB / 2 * xiB * (1 - xiB ** 2)
xiB_star = xiB[np.argmax(FB)]
log(f"example beta = {betaB:.4f}: Eq.(8) N(mid side) = {8*np.interp(0.5, xiB, FB):+.3f}, xi* = {xiB_star:.3f}, N(xi*) = {8*FB.max():+.3f}")
XB3 = round(LtB - SPB[0] * xiB_star, 1)
SENSB = [("D1 mid-span of main span", "defl", SPB[0] + SPB[1] / 2),
         ("D2 mid-span of right side span (near-blind)", "defl", LtB - SPB[0] / 2),
         (f"D3 right side span xi* (x={XB3:.1f} m)", "defl", XB3),
         ("D4 mid-span of left side span (mirror of D2)", "defl", SPB[0] / 2)]
mB = Model(SPB, lambda x: EIB, 0.0, ne_per_span=400, extra=tuple(s[2] for s in SENSB))
wq = mB.uniform()[0::2]
Mq = np.array([mB.moment_uniform(v) for v in mB.x[mB.x > SPB[0] + SPB[1]][::4]])
xz = mB.x[mB.x > SPB[0] + SPB[1]][::4]
zeroB = [0.5 * (xz[j] + xz[j + 1]) for j in range(len(Mq) - 1) if Mq[j] * Mq[j + 1] < 0]
log(f"{SPB}: M_q = 0 in right side span at x = {[round(float(v),2) for v in zeroB]} "
    f"({[round(float(v)-SPB[0]-SPB[1],2) for v in zeroB]} m from pier)")
ZC_B = 1.1          # m, soffit to centroid [ASSUMPTION]
SENSB += [(f"S1 bottom fiber at M_q=0 (x={zeroB[0]:.1f} m)", "strain", round(zeroB[0], 1)),
          ("S2 bottom fiber at mid-span of main span", "strain", SPB[0] + SPB[1] / 2)]
mB = Model(SPB, lambda x: EIB, 0.0, ne_per_span=400, extra=tuple(s[2] for s in SENSB))
fB, _ = freqs(Model(SPB, lambda x: EIB, 0.0, ne_per_span=40), lambda x: MB, 3)
log(f"f1..f3 (EI={EIB:.1e}, m={MB} t/m, assumed) = {fB[0]:.2f}, {fB[1]:.2f}, {fB[2]:.2f} Hz")
for v in [5, 10, 20, 30, 40]:
    Tcr = (LtB + 6.15) / (v / 3.6)
    log(f"v={v} km/h: T_cr={Tcr:.1f} s, T_cr/T1={Tcr*fB[0]:.1f}")
rowsB = []
ilsB = {}
for lab, kind, xs in SENSB:
    if kind == "defl":
        eta = mB.il_defl(xs); sc = 1e3; Lref = SPB[1] if SPB[0] < xs < SPB[0] + SPB[1] else SPB[0]
        C = area_parts(mB.x, eta); Nm = 192 * EIB * C[0] / Lref ** 4
    else:
        eta = ZC_B / EIB * mB.il_moment(xs); sc = 1e6
        C = area_parts(mB.x, eta); Nm = ""
    ilsB[lab] = (eta, sc)
    rec = dict(sensor=lab, kind=kind, x=xs, C=C[0], Apos=C[1], Aneg=C[2],
               R=C[0] / C[1], N=Nm)
    for tn, tr in TRUCKS.items():
        s, y, Iy = crossing(mB.x, eta, tr)
        pk, ymax, ymin = peak(y * sc)
        rec[f"peak[{tn}]"] = pk; rec[f"max[{tn}]"] = ymax; rec[f"min[{tn}]"] = ymin
        rec[f"I[{tn}]"] = Iy * sc
        if kind == "defl":
            for e0 in (0.01, 0.02, 0.05):
                rec[f"bias{e0}[{tn}]"] = 100 * e0 * 1e-3 * (LtB + tr["a"].max()) / (abs(C[0]) * tr["P"].sum() * g)
    rowsB.append(rec)
keys = sorted({k for r in rowsB for k in r}, key=lambda k: list(rowsB[0]).index(k) if k in rowsB[0] else 999)
with open(os.path.join(RES, "B_generic_sensors.csv"), "w", newline="") as fh:
    wr = csv.DictWriter(fh, fieldnames=keys)
    wr.writeheader(); wr.writerows(rowsB)
log(f"\n--- (B) {SPB} m sensors, EI = 6.0e7 kNm2 (assumed) ---")
for r in rowsB:
    s = f"{r['sensor']:40s} C={r['C']:+.3e} R={r['R']:+.2f} " + (f"N={r['N']:+.3f} " if r['N'] != "" else "")
    s += " | ".join(f"{tn[:2]} pk {r[f'peak[{tn}]']:+6.2f} I {r[f'I[{tn}]']:+7.2f}" for tn in list(TRUCKS)[:3])
    if r["kind"] == "defl":
        s += " | bias T1 0.01/0.02/0.05 mm: " + "/".join(f"{r[f'bias{e}[' + list(TRUCKS)[0] + ']']:.1f}%" for e in (0.01, 0.02, 0.05))
    log(s)

wq = mB.uniform()[0::2]
fig, ax = plt.subplots(3, 1, figsize=(9, 9.5), gridspec_kw=dict(height_ratios=[0.6, 1.2, 1.2]))
a0 = ax[0]
a0.plot([0, LtB], [0, 0], "k", lw=4)
for xp in np.concatenate([[0.0], np.cumsum(SPB)]):
    a0.plot([xp], [-0.25], "^", color="k", ms=10)
for lab, kind, xs in SENSB:
    sym, c = mk[kind]
    a0.plot(xs, 0.45, sym, color=c, ms=8)
    a0.text(xs, 0.8, lab.split()[0], ha="center", fontsize=8, color=c)
    if kind == "defl":
        a0.plot([xs, xs], [-0.1, -1.0], color=c, lw=0.8)
        a0.plot(xs, -1.05, "s", color="0.4", ms=5)
a0.text(LtB / 2, -1.6, "LVDT/dial gauge on fixed frame under girder (accessed from ground)", ha="center", fontsize=8)
a0.set_ylim(-2, 1.3); a0.set_yticks([]); a0.set_xlim(-3, LtB + 3)
a0.set_title(f"(a) Example overpass {SPB[0]:g}+{SPB[1]:g}+{SPB[2]:g} m (beta = {betaB:.3f}), prismatic, on bearings: sensor layout", fontsize=9)
ax[1].plot(mB.x, wq * 1e3 * 245.8, "k", lw=1.6)
ax[1].axhline(0, color="k", lw=0.5)
for lab, kind, xs in SENSB[:4]:
    ax[1].axvline(xs, color="0.6", ls=":", lw=0.7)
ax[1].set_ylabel("I_y = C_m P (mm*m), P = 25.06 t")
ax[1].set_title("(b) Predicted integral along the bridge (EI = 6.0e7 kN m2 assumed)", fontsize=9)
for lab, kind, xs in SENSB:
    eta, sc = ilsB[lab]
    if kind == "defl":
        ax[2].plot(mB.x, eta * 1e3 * 100, label=lab)
ax2b = ax[2].twinx()
for lab, kind, xs in SENSB:
    eta, sc = ilsB[lab]
    if kind == "strain":
        ax2b.plot(mB.x, eta * 1e6 * 100, "--", label=lab)
ax[2].axhline(0, color="k", lw=0.5)
ax[2].set_ylabel("deflection (mm/100 kN)"); ax2b.set_ylabel("strain (ue/100 kN)")
ax[2].set_xlabel("x (m)")
h1, l1 = ax[2].get_legend_handles_labels(); h2, l2 = ax2b.get_legend_handles_labels()
ax[2].legend(h1 + h2, l1 + l2, fontsize=7)
ax[2].set_title("(c) Influence lines", fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fB1_generic_overpass.png"), dpi=200)
plt.close(fig)
log("\nfigures written to", FIG)
LOG.close()
