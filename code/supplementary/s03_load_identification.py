"""s03_load_identification.py - laboratory load identification (Sections 3.2-3.3, 6.1-6.2).

Reproduces (SCHM manuscript):
  Section 3.1: 40.64 N, 66.99 N, 125.08 N; three-load order (rms residual 0.030 mm
               against 0.55 mm for the reverse spacing).
  Section 3.2: largest |measured - analytical| = 0.0125 mm, 0.43 % of the peak,
               2.5 x LVDT resolution; residuals predominantly positive.
  Table 4    : I_y = 4168.15 / 7788.93 mm^2; BPM 67.73 / 126.57 N (+1.10 / +1.19 %);
               SLM 67.40 / 125.95 N (+0.61 / +0.70 %); BPM/SLM = 1.00489 =
               2513.43/2501.19; quadrature-corrected BPM +1.61 %.
  Section 3.3: measured/analytical integral 1.010, 1.016, 1.017.
  Fig. 6     : regression through the origin I_y = 62.229 P, R^2 = 0.99998,
               +1.12 % above 61.541 mm^2/N.
  Table 7    : zero-offset bias eps0 L_tot / I_y.
  Section 6.1: offset residual eps0 (1.2596 - 1.9893) mm^-1, 58 % / 42 %.
  Section 6.3: reference integral is 60 % of the two-load one.

Run:  python3 -I code/supplementary/s03_load_identification.py
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import beam_theory as bt  # noqa: E402


def head(t):
    print(("\n== %s " % t).ljust(78, "="))


def exact_trapz(y, x):
    """Trapezoidal rule in exact decimal arithmetic on the 4-decimal data of Table C.1,
    rounded half up to 0.01 mm^2 (binary floating point turns 2513.4250 into 2513.42)."""
    from decimal import Decimal, ROUND_HALF_UP
    yd = [Decimal(repr(float(v))) for v in y]
    h = Decimal(repr(float(x[1] - x[0])))
    tot = h * (sum(yd) - (yd[0] + yd[-1]) / 2)
    return tot, tot.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


head("Loads (Section 3.1)")
print("  P0      = %.4f N  (40.64)" % bt.P0)
print("  W_two   = %.4f N  (66.99)" % bt.W_TWO)
print("  W_three = %.4f N  (125.08)" % bt.W_THREE)

head("Section 3.1: order of the three-load group (fit of Eq. (1) to the record)")
for label, m, a in (("2550 g leading, +500, +250 (manuscript)", [2550, 5100, 5100], [0, 500, 750]),
                    ("2550 g leading, +250, +500 (files-v2)", [2550, 5100, 5100], [0, 250, 750]),
                    ("5100 g leading, +250, +500 (mirror)", [5100, 5100, 2550], [0, 250, 750])):
    yp = bt.record("three", bt.X_3, a=a, m=m)
    print("  %-42s rms residual %.4f mm" % (label, np.sqrt(np.mean((bt.Y_THREE - yp) ** 2))))
print("  (manuscript: 0.030 mm for the stated order, 0.55 mm for the reverse spacing)")
for label, m in (("2145 g leading", [2145, 4684]), ("4684 g leading", [4684, 2145])):
    yp = bt.record("two", bt.X_2, m=m)
    print("  two loads, %-31s rms residual %.4f mm" % (label, np.sqrt(np.mean((bt.Y_TWO - yp) ** 2))))
print("  (order of the two-load group is not stated in the manuscript)")

head("Section 3.2: measured vs analytical influence line, single load")
y_an = bt.eta(bt.X_1, bt.P0)
res = bt.Y_SINGLE - y_an
k = int(np.argmax(np.abs(res)))
print("  max |measured - Eq.(A.2)| = %.4f mm at x = %.0f mm  (0.0125 mm)" % (abs(res[k]), bt.X_1[k]))
print("  vs tabulated analytical column: %.4f mm" % np.max(np.abs(bt.Y_SINGLE - bt.Y_ANALYTICAL)))
print("  relative to max deflection %.4f mm: %.2f %%  (0.43 %%)" % (y_an.max(), 100 * abs(res[k]) / y_an.max()))
print("  / LVDT resolution 0.005 mm = %.2f  (two and a half times)" % (abs(res[k]) / bt.RESOLUTION))
inner = res[1:-1]
inner = inner[np.abs(bt.X_1[1:-1] - bt.L_SPAN) > 1]
print("  sign of residual (measured - theory) x |eta| at the 18 interior non-support points:")
sgn = np.sign(res * np.sign(y_an))
print("    magnitude above theory: %d, below: %d  (manuscript: 'predominantly positive')"
      % (int(np.sum(sgn[1:-1] > 0)), int(np.sum(sgn[1:-1] < 0))))
print("    raw residual > 0: %d, < 0: %d" % (int(np.sum(res > 1e-9)), int(np.sum(res < -1e-9))))

head("Table 4: identified total loads (trapezoidal rule, dx = 250 mm)")
I_ref = bt.integral_trapz(bt.Y_SINGLE, bt.X_1)
exact = bt.C_M * bt.P0
I = {}
print("  %-7s %-9s %12s %12s %9s" % ("case", "method", "I_y (mm^2)", "load (N)", "dev."))
for case, ms in (("two", "4168.15 | 67.73 +1.10 % | 67.40 +0.61 %"),
                 ("three", "7788.93 | 126.57 +1.19 % | 125.95 +0.70 %")):
    xg, yg, W = bt.CASES[case]
    Iy = bt.integral_trapz(yg, xg)
    I[case] = Iy
    print("  %-7s %-9s %12s %12.4f %9s" % (case, "weighing", "n/a", W, "n/a"))
    for name, val in (("BPM", bt.bpm(Iy)), ("SLM", bt.slm(Iy, I_ref))):
        print("  %-7s %-9s %12.4f %12.4f %+8.3f %%" % ("", name, Iy, val, 100 * (val / W - 1)))
    print("          manuscript: %s" % ms)
for case in ("single", "two", "three"):
    xg, yg, _ = bt.CASES[case]
    ex, rd = exact_trapz(yg, xg)
    print("  exact decimal I_y, %-6s = %s mm^2 -> %s (round half up)" % (case, ex, rd))
print("  (manuscript: 2513.43, 4168.15, 7788.93)")
for case in ("two", "three"):
    print("  BPM/SLM, %-5s = %.5f" % (case, bt.bpm(I[case]) / bt.slm(I[case], I_ref)))
print("  I_ref / exact  = %.5f  (1.00489 = 2513.43/2501.19)" % (I_ref / exact))

grid = np.arange(0, 2 * bt.L_SPAN + 1, bt.DX)
q = bt.integral_trapz(bt.eta(grid, bt.P0), grid) / exact
for case in ("two", "three"):
    W = bt.CASES[case][2]
    print("  %-5s BPM corrected for the quadrature bias (/%.5f): %+.2f %% (uncorrected %+.2f %%)"
          % (case, q, 100 * (bt.bpm(I[case] / q) / W - 1), 100 * (bt.bpm(I[case]) / W - 1)))
print("  (manuscript, two loads: +1.10 % -> +1.61 %)")

head("Section 3.3: measured / analytical integral (both trapezoidal, same grid)")
for case in ("single", "two", "three"):
    xg, yg, W = bt.CASES[case]
    ia = bt.integral_trapz(bt.record(case, xg), xg)
    print("  %-6s %.4f" % (case, bt.integral_trapz(yg, xg) / ia))
print("  (manuscript: 1.010, 1.016, 1.017)")

head("Fig. 6: calibration line through the origin")
Ps = np.array([bt.P0, bt.W_TWO, bt.W_THREE])
Is = np.array([I_ref, I["two"], I["three"]])
slope = np.sum(Ps * Is) / np.sum(Ps * Ps)
r2_c = 1 - np.sum((Is - slope * Ps) ** 2) / np.sum((Is - Is.mean()) ** 2)
r2_u = 1 - np.sum((Is - slope * Ps) ** 2) / np.sum(Is ** 2)
print("  slope = %.4f mm^2/N (62.229); theory %.4f (61.541); +%.2f %% (1.12 %%)"
      % (slope, bt.C_M, 100 * (slope / bt.C_M - 1)))
print("  R^2 (centred total sum of squares)   = %.6f  (0.99998)" % r2_c)
print("  R^2 (uncentred, regression thru 0)   = %.7f" % r2_u)

head("Table 7: zero-offset bias eps0 L_tot / I_y")
print("  %-7s %9s %8s %9s %9s %9s" % ("case", "I_y", "L_tot", "0.005", "0.02", "0.05 mm"))
for case in ("single", "two", "three"):
    xg, yg, W = bt.CASES[case]
    Iy = bt.integral_trapz(yg, xg)
    Lt = xg[-1]
    print("  %-7s %9.1f %8.0f %+8.2f%% %+8.2f%% %+8.2f%%"
          % (case, Iy, Lt, *(100 * e * Lt / Iy for e in (0.005, 0.02, 0.05))))
print("  (Table 7: +0.99/+3.98/+9.95; +0.63/+2.52/+6.30; +0.37/+1.48/+3.69 %)")

head("Section 6.1: offset residual of SLM, two-load case")
s_t = bt.X_2[-1] / I["two"]
s_0 = bt.X_1[-1] / I_ref
print("  L_t/I_t = %.4f, L_0/I_0 = %.4f mm^-1  (1.2596, 1.9893)" % (s_t, s_0))
print("  |residual| / BPM term = %.3f -> %.0f %% of the BPM term, %.0f %% reduction  (58 %%, 42 %%)"
      % (abs(s_t - s_0) / s_t, 100 * abs(s_t - s_0) / s_t, 100 * (1 - abs(s_t - s_0) / s_t)))

head("Section 6.3: size of the reference integral")
print("  I_ref / I_two = %.3f  (manuscript: 60 %%)" % (I_ref / I["two"]))
