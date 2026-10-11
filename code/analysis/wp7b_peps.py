"""WP7b - numbers added in manuscript v2 (manuscript/v2/manuscript.md).

Run:  python3 code/analysis/wp7b_peps.py   (writes code/analysis/logs/wp7b_peps.log)

Part A  Offset-equivalent load P_eps = eps0 * L_tot / C_m and the load bias
        P_eps / P for the Cau May gauges, for BOTH calibrations of WP3
        (kFE: design EI, pier spring fitted to the report FE;
         kMeas: joint (alpha, k) fit to the measured deflections).
        C_m is read from code/analysis/results/wp3_Cm_table.csv (base model
        varEI_Lv44). L_tot = 200 m (main bridge 55 + 90 + 55 m).
Part B  Sensitivity of C_m to the pier spring k at k_FE (FE model of WP3,
        design EI, Lv = 44 m), and the indicators at (alpha = 1.088, k_FE),
        i.e. calibration A after the EI scaling that matches the measurements.
Part C  Laboratory linearity: measured / analytical deflection integral per
        configuration (trapezoidal rule, dx = 250 mm, Appendix C data).
Part D  Table 9 combined with one rule (root-sum-square of all standard
        uncertainties) for every column.
"""
import os
import sys
import csv
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
LOG = os.path.join(HERE, "logs", "wp7b_peps.log")
out = []


def pr(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)


g = 9.81  # m/s2, as in the laboratory load values (4.143 kg -> 40.64 N)

# ------------------------------------------------------------------ Part A
pr("=== Part A: offset-equivalent load P_eps = eps0*L_tot/C_m (Cau May, base model varEI_Lv44) ===")
L_tot = 200.0                     # m, 55 + 90 + 55
truck_kN = 25.0 * g               # nominal test truck 5 + 10 + 10 t
rows = list(csv.DictReader(open(os.path.join(HERE, "results", "wp3_Cm_table.csv"))))
sel = {}
for r in rows:
    if r["bridge"] == "CM" and r["model"] == "varEI_Lv44" and r["pier"] in ("kFE", "kMeas") \
            and r["sensor"] in ("CM N8 0.4L (22 m from T8)", "CM N7 mid-span"):
        sel[(r["pier"], r["sensor"])] = r
pr(f"L_tot = {L_tot} m; 25 t truck = {truck_kN:.2f} kN; wheelbase 4.95 m would add "
   f"{100*4.95/L_tot:.1f} % to L_tot (not included)")
for (cal, sen), r in sorted(sel.items()):
    Cm = float(r["Cm_m2_per_kN"])           # m2/kN
    line = f"{cal:5s} {sen:28s} C_m = {Cm:.4e} m2/kN  N_m = {float(r['norm_192EICm_L4']):.3f}  " \
           f"neg/pos = {float(r['neg_over_pos']):.3f}"
    for e0_mm in (0.02, 0.05):
        Peps = e0_mm * 1e-3 * L_tot / Cm  # kN
        line += f" | eps0={e0_mm} mm: P_eps = {Peps:6.1f} kN, bias(25 t) = {100*Peps/truck_kN:5.1f} %"
    pr(line)
for cal in ("kFE", "kMeas"):
    c8 = float(sel[(cal, "CM N8 0.4L (22 m from T8)")]["Cm_m2_per_kN"])
    c7 = float(sel[(cal, "CM N7 mid-span")]["Cm_m2_per_kN"])
    pr(f"{cal}: C_m(N7)/C_m(N8) = {c7/c8:.2f}")

# ------------------------------------------------------------------ Part B
pr("\n=== Part B: C_m sensitivity to the pier spring k (design EI, Lv = 44 m) ===")
from wp3_fe import Bridge, haunch_EI      # noqa: E402
E = 36.057e6
spans = (55.0, 90.0, 55.0)
EI, _, _ = haunch_EI(spans, E, 5.482, 59.612, 2.40, 5.40, 44.0)
EIref = E * 5.482
kFE = 2.748e7
sens = {"N8 0.4L": (178.0, 55.0), "N7 mid": (100.0, 90.0)}


def indic(alpha, k):
    b = Bridge(spans, lambda x: alpha * EI(x), k)
    res = {}
    for lab, (xm, L) in sens.items():
        c, pos, neg, _ = b.Cm(xm)
        res[lab] = (c, 192 * EIref * c / L ** 4, neg / pos)
    return res


base = indic(1.0, kFE)
for lab in sens:
    c, n, npr = base[lab]
    pr(f"k_FE = {kFE:.3e}: {lab}: C_m = {c:.4e}, N_m = {n:.3f}, neg/pos = {npr:.3f}")
for f in (0.5, 2.0):
    r = indic(1.0, f * kFE)
    for lab in sens:
        pr(f"k = {f:g} k_FE: {lab}: N_m = {r[lab][1]:.3f}, neg/pos = {r[lab][2]:.3f}, "
           f"C_m/C_m(k_FE) = {r[lab][0]/base[lab][0]:.3f}")
h = 0.01
rp, rm = indic(1.0, kFE * np.exp(h)), indic(1.0, kFE * np.exp(-h))
for lab in sens:
    d = (np.log(rp[lab][0]) - np.log(rm[lab][0])) / (2 * h)
    pr(f"d ln C_m / d ln k at k_FE: {lab}: {d:+.3f}")
r = indic(1.088, kFE)
for lab in sens:
    pr(f"alpha = 1.088, k = k_FE: {lab}: N_m (design EI_ref) = {r[lab][1]:.3f}, neg/pos = {r[lab][2]:.3f}")
r = indic(0.716, 1.199e8)
for lab in sens:
    pr(f"check kMeas (alpha 0.716, k 1.199e8): {lab}: N_m = {r[lab][1]:.3f}, neg/pos = {r[lab][2]:.3f}")

# ------------------------------------------------------------------ Part C
pr("\n=== Part C: laboratory linearity (Appendix C, trapezoidal rule, dx = 250 mm) ===")
l, EIlab, dx = 2500.0, 200e3 * 16529.8, 250.0


def eta(x):
    """Eq. (A.2), sensor at l/2, unit load, mm/N."""
    x = np.asarray(x, float)
    y = np.where(x <= l / 2, x * (9 * l**2 - 13 * x**2) / 192,
                 np.where(x <= l, (x - l) * (4 * l**2 - 29 * l * x + 19 * x**2) / 192,
                          (2 * l - x) * (3 * l**2 - 4 * l * x + x**2) / 64))
    return np.where((x < 0) | (x > 2 * l), 0.0, y) / EIlab


single = [0, .8844, 1.6975, 2.3525, 2.7738, 2.8827, 2.6363, 2.1100, 1.4213, .6838, 0,
          -.5069, -.8556, -1.0600, -1.1438, -1.1200, -1.0013, -.8175, -.5816, -.3019, 0]
two = [0, .4625, 1.8813, 3.1413, 4.0988, 4.6350, 4.6238, 4.0688, 3.1375, 1.9600, .7715,
       -.2689, -1.0063, -1.4988, -1.7813, -1.8600, -1.7738, -1.5525, -1.2213, -.8125, -.3325, 0]
three = [0, .5525, 1.0450, 2.5413, 4.8700, 6.7588, 7.9350, 8.2775, 7.6825, 6.2800, 4.3725,
         2.2975, .3021, -1.2588, -2.3650, -3.0363, -3.3300, -3.2663, -2.9450, -2.4125,
         -1.7088, -1.0713, -.3650, 0]
# load trains: (mass g, offset behind the leading load, mm)
cases = {"single": (single, [(4143, 0)]),
         "two": (two, [(2145, 0), (4684, 250)]),
         "three": (three, [(2550, 0), (5100, 500), (5100, 750)])}
for name, (rec, train) in cases.items():
    x = np.arange(len(rec)) * dx
    P = sum(m for m, _ in train) * 1e-3 * g
    ana = sum(m * 1e-3 * g * eta(x - a) for m, a in train)
    Im, Ia = np.trapezoid(rec, x), np.trapezoid(ana, x)
    rms = np.sqrt(np.mean((np.array(rec) - ana) ** 2))
    pr(f"{name:6s} P = {P:7.3f} N  I_meas = {Im:8.2f}  I_analytical(trap) = {Ia:8.2f}  "
       f"ratio = {Im/Ia:.4f}  rms(meas-analytical) = {rms:.4f} mm")
pr("(three-load order: 2550 g leading, 5100 g at +500 mm, 5100 g at +750 mm; "
   "rms for the alternative reading 250/500 mm:")
x = np.arange(len(three)) * dx
alt = sum(m * 1e-3 * g * eta(x - a) for m, a in [(2550, 0), (5100, 250), (5100, 750)])
pr(f"  rms = {np.sqrt(np.mean((np.array(three) - alt) ** 2)):.4f} mm)")
pr(f"two-load record: {len(two)-1} intervals (odd -> Simpson needs a 3/8 end panel); "
   f"three-load: {len(three)-1}; single: {len(single)-1}")

# ------------------------------------------------------------------ Part D
pr("\n=== Part D: Table 9 combined by root-sum-square in every column ===")
# (low, high) standard uncertainties in %; '<x' bounds entered as x at both ends;
# dynamic '< 1 %' entered as 0 (low) to 1 (high); quadrature bias corrected (Simpson).
cols = {
    "Laboratory (SLM)": dict(P0=(0.1, 0.1), eps0=(0.4, 1.0), noise=(0.1, 0.1), ref=(0.1, 0.1)),
    "Field (SLM)": dict(P0=(0.5, 1.0), eps0=(2, 10), v=(1, 3), dyn=(0, 1), noise=(0.1, 0.3), ref=(0.1, 0.3)),
    "Field (BPM)": dict(EI=(5, 15), l=(0.4, 2), gain=(1, 2), eps0=(2, 10), v=(1, 3), dyn=(0, 1),
                        noise=(0.1, 0.3)),
}
for name, c in cols.items():
    lo = np.sqrt(sum(v[0] ** 2 for v in c.values()))
    hi = np.sqrt(sum(v[1] ** 2 for v in c.values()))
    lin_lo, lin_hi = sum(v[0] for v in c.values()), sum(v[1] for v in c.values())
    pr(f"{name:18s} RSS {lo:5.2f} - {hi:5.2f} %   (linear sum would give {lin_lo:.2f} - {lin_hi:.2f} %)")

# ------------------------------------------------------------------ Part E
pr("\n=== Part E: edges of the near-blind band |N_m| < 0.2, mid-span sensor, uniform EI ===")
# 8F(1/2, mu) = 2.5 - 1.5 mu = +/-0.2  ->  mu = 23/15 (N = +0.2) or mu = 1.8 (N = -0.2)
for mu in (23 / 15, 1.8):
    # two spans: mu = (1 + rho^3)/(1 + rho) = 1 - rho + rho^2
    rho = (1 + np.sqrt(1 + 4 * (mu - 1))) / 2
    # symmetric three spans: mu = 2(1 + b^3)/(2 + 3b)  ->  2b^3 - 3 mu b + 2 - 2 mu = 0
    rts = np.roots([2.0, 0.0, -3 * mu, 2 - 2 * mu])
    b = max(r.real for r in rts if abs(r.imag) < 1e-12)
    pr(f"N_m = {2.5-1.5*mu:+.1f}: two-span rho_L = {rho:.6f}; three-span beta = {b:.6f}")
pr("three-span beta = 2: mu = 2.25, N_m(mid side span) = "
   f"{2.5-1.5*2*(1+8)/(2+6):.3f}")

os.makedirs(os.path.dirname(LOG), exist_ok=True)
with open(LOG, "w") as f:
    f.write("\n".join(out) + "\n")
