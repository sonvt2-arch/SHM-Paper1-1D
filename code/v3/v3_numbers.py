"""Numbers that are new in manuscript v3 and not printed by an earlier log.

Run: python3 -I code/v3/v3_numbers.py  (writes code/v3/logs/v3_numbers.log)
Part A: offset bias, Eq. (19) of v3, for the Cau May constants over the admissible
        sets of package 1C (ident_freq.log lines 50-53) and for calibrations A, A', B
        (ident_static.log lines 13-15); P = 25.06 t, L_tot = 200 m.
Part B: NOR-BWIM beam model (code/norbwim/nb_beam.py): span shares of the moment
        influence line at the gauge, |C_eps(gauge)| / max |C_eps| along the girder.
Part C: r^2 of the global-shape fit for the documented single-truck crossings used
        in the invariance test (code/norbwim/results/events_field_qc.csv).
"""
import os
import sys
import numpy as np
import pandas as pd

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
out = []
p = lambda s="": out.append(s)  # noqa: E731

# ---------------- Part A
P = 25.06 * 9.80665          # kN
L = 200.0                     # m
EPS = [0.02, 0.05, 0.1, 0.2, 0.5]   # mm
cases = [
    ("N7 calib A (design EI, k_FE)", 3.610e-4),
    ("N7 calib A' (alpha 1.088, k_FE)", 3.350e-4),
    ("N7 calib B (alpha 0.716, k 1.2e8)", 4.047e-4),
    ("N7 joint set (static+f3) min C", 3.28e-4),
    ("N7 joint set (static+f3) max C", 3.84e-4),
    ("N7 static set max C", 4.95e-4),
    ("N8 calib A", 4.376e-5),
    ("N8 calib A'", 3.850e-5),
    ("N8 calib B", 1.147e-4),
    ("N8 joint set (static+f3) min C", 3.00e-5),
    ("N8 joint set (static+f3) max C", 9.39e-5),
    ("N8 static set max C", 1.98e-4),
]
p(f"PART A  offset bias eps0*L/(C*P) in %, P = {P:.2f} kN, L = {L} m")
p("case | C (m2/kN) | " + " | ".join(f"{e} mm" for e in EPS) + " | P_eps(0.1 mm) kN")
for name, C in cases:
    b = [e * 1e-3 * L / (C * P) * 100 for e in EPS]
    pe = 0.1e-3 * L / C
    p(f"{name} | {C:.3e} | " + " | ".join(f"{v:.1f}" for v in b) + f" | {pe:.1f}")

# ---------------- Part B
sys.path.insert(0, os.path.join(ROOT, "code", "norbwim"))
import nb_beam as nb  # noqa: E402
p()
p("PART B  NOR-BWIM beam model, haunch n = 2 (and n = 2.5, uniform)")
for hn, n in [(True, 2.0), (True, 2.5), (False, 2.0)]:
    m = nb.model(hn, n)
    x, il = nb.moment_il(m)
    edges = nb.EDGES
    tot = np.trapezoid(il, x)
    pos = np.trapezoid(np.clip(il, 0, None), x)
    shares = []
    for a, b in zip(edges[:-1], edges[1:]):
        k = (x >= a - 1e-9) & (x <= b + 1e-9)
        shares.append(np.trapezoid(il[k], x[k]) / tot * 100)
    xm, M, _ = nb.udl_moment(m)
    ce = np.abs(nb.strain_proxy(m, xm, M))
    cs = np.abs(nb.strain_proxy(m, nb.X_SENSOR, np.interp(nb.X_SENSOR, xm, M)))[0]
    p(f"haunch={hn} n={n}: net/positive area of M-IL at gauge = {tot/pos:.3f}; "
      f"span shares % = {np.round(shares, 1).tolist()}; "
      f"|C_eps(gauge)|/max|C_eps| = {cs/ce.max():.3f} (max at x = {xm[np.argmax(ce)]:.1f} m)")

# ---------------- Part C
e = pd.read_csv(os.path.join(ROOT, "code", "norbwim", "results", "events_field_qc.csv"))
used = ["R1", "R2", "R3", "R4", "R7", "R8", "R9", "R11", "R12", "R13", "R14",
        "R15", "R16", "R17", "R18"]
s = e[e.id.isin(used)]
p()
p(f"PART C  r2 of global-shape fit, documented single-truck lane-A crossings (n={len(s)}): "
  f"min {s.r2_fit.min():.3f}, median {s.r2_fit.median():.3f}, max {s.r2_fit.max():.3f}")
txt = "\n".join(out)
print(txt)
open(os.path.join(ROOT, "code", "v3", "logs", "v3_numbers.log"), "w").write(txt + "\n")
