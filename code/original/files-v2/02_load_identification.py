"""
02_load_identification.py
=========================
Reproduces Tables 2, 4 and 5 of the revised paper:

  * the exact, trapezoidal and Simpson values of the deflection integral,
  * the total loads identified by BPM and SLM for the three configurations,
  * the quadrature convergence study,
  * the calibration line I_y = C_m P,
  * the zero-offset sensitivity, dP/P = eps0 * L_tot / I_y.

Run:  python3 02_load_identification.py
"""

import numpy as np
import beam_theory as bt

line = lambda t: print(('\n== %s ' % t).ljust(74, '='))
G = bt.G


# --------------------------------------------------------------------------
line("Deflection integrals (Table 2)")
# --------------------------------------------------------------------------
exact = bt.C_M * bt.P0
grid = np.linspace(0, 2 * bt.L_SPAN, 21)             # dx = 250 mm
y_exact = bt.eta(grid, bt.P0)

rows = [
    ("Exact, Eq. (11): P0 l^4 / 192EI",              exact),
    ("Analytical influence line, trapezoidal rule",  bt.integral_trapz(y_exact, grid)),
    ("Analytical influence line, Simpson rule",      bt.integral_simpson(y_exact, grid)),
    ("Measured, trapezoidal rule",                   bt.integral_trapz(bt.Y_SINGLE, bt.X_1)),
    ("Measured, Simpson rule",                       bt.integral_simpson(bt.Y_SINGLE, bt.X_1)),
]
for name, v in rows:
    print("%-46s %10.2f mm^2   %+7.3f %%" % (name, v, 100 * (v - exact) / exact))
print("\nNOTE: the value 2488.69 quoted in the old draft as 'analytical' is the")
print("      TRAPEZOIDAL approximation, not the exact closed-form value.")


# --------------------------------------------------------------------------
line("Identified total loads (Table 4)")
# --------------------------------------------------------------------------
I_ref = bt.integral_trapz(bt.Y_SINGLE, bt.X_1)

print("%-8s %-16s %10s %12s %12s %10s"
      % ("case", "method", "Iy (mm^2)", "load (N)", "load (g)", "dev.(%)"))
results = {}
for case in ("two", "three"):
    xg, yg, W = bt.CASES[case]
    Iy = bt.integral_trapz(yg, xg)
    results[case] = Iy
    print("%-8s %-16s %10s %12.3f %12.1f %10s"
          % (case, "LWM (weighing)", "-", W, W / G * 1000, "-"))
    for name, val in (("BPM, Eq. (12)", bt.bpm(Iy)),
                      ("SLM, Eq. (15)", bt.slm(Iy, I_ref))):
        print("%-8s %-16s %10.2f %12.3f %12.1f %+10.2f"
              % ("", name, Iy, val, val / G * 1000, 100 * (val - W) / W))

ratio = bt.bpm(results["two"]) / bt.slm(results["two"], I_ref)
print("\nBPM/SLM ratio, two loads   = %.5f" % ratio)
print("BPM/SLM ratio, three loads = %.5f"
      % (bt.bpm(results["three"]) / bt.slm(results["three"], I_ref)))
print("measured reference integral / exact = %.5f" % (I_ref / exact))
print("-> the entire BPM/SLM difference is the calibration error of the")
print("   reference crossing: this is common-mode cancellation, observed directly.")

# what BPM would give if the quadrature bias were removed first
q_bias = bt.integral_trapz(y_exact, grid) / exact
print("\nquadrature bias factor = %.5f (%.3f %%)" % (q_bias, 100 * (q_bias - 1)))
for case in ("two", "three"):
    _, _, W = bt.CASES[case]
    corrected = bt.bpm(results[case] / q_bias)
    print("  %-6s BPM corrected for quadrature: %+.2f %% (uncorrected %+.2f %%)"
          % (case, 100 * (corrected - W) / W,
             100 * (bt.bpm(results[case]) - W) / W))


# --------------------------------------------------------------------------
line("Quadrature convergence on the exact influence line")
# --------------------------------------------------------------------------
print("%6s %10s %12s %10s %12s %10s"
      % ("n/span", "dx (mm)", "trapezoid", "bias %", "Simpson", "bias %"))
for n in (2, 4, 5, 10, 20, 25, 50):
    xs = np.linspace(0, 2 * bt.L_SPAN, 2 * n + 1)
    ys = bt.eta(xs, bt.P0)
    tr, si = bt.integral_trapz(ys, xs), bt.integral_simpson(ys, xs)
    print("%6d %10.1f %12.3f %+10.3f %12.3f %+10.4f"
          % (n, bt.L_SPAN / n, tr, 100 * (tr - exact) / exact,
             si, 100 * (si - exact) / exact))


# --------------------------------------------------------------------------
line("Calibration line  I_y = C_m P  (Fig. 6)")
# --------------------------------------------------------------------------
Ps = np.array([bt.P0, bt.W_TWO, bt.W_THREE])
Is = np.array([I_ref, results["two"], results["three"]])
slope = np.sum(Ps * Is) / np.sum(Ps * Ps)            # regression through origin
r2 = 1 - np.sum((Is - slope * Ps) ** 2) / np.sum((Is - Is.mean()) ** 2)
print("fitted slope   = %.4f mm^2/N" % slope)
print("theoretical    = %.4f mm^2/N  (fit is %+.2f %% above theory)"
      % (bt.C_M, 100 * (slope / bt.C_M - 1)))
print("R^2            = %.6f" % r2)


# --------------------------------------------------------------------------
line("Zero-offset sensitivity (Table 5) --  dP/P = eps0 * L_tot / I_y")
# --------------------------------------------------------------------------
print("%-8s %10s %10s %s" % ("case", "Iy (mm^2)", "Ltot (mm)",
                             "   ".join("eps=%.3f" % e
                                        for e in (0.005, 0.01, 0.02, 0.05, 0.10))))
for case in ("single", "two", "three"):
    xg, yg, _ = bt.CASES[case]
    Iy = bt.integral_trapz(yg, xg)
    Ltot = xg[-1]
    cells = "  ".join("%+8.2f%%" % (100 * e * Ltot / Iy)
                      for e in (0.005, 0.01, 0.02, 0.05, 0.10))
    print("%-8s %10.1f %10.0f  %s" % (case, Iy, Ltot, cells))
print("\n-> the bias is inversely proportional to the load: the method becomes")
print("   MORE accurate for heavier vehicles, which suits overload screening.")
