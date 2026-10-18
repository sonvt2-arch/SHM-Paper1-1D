"""s02_quadrature_table3.py - deflection integral and quadrature (Table 3, Section 6.1).

Reproduces (SCHM manuscript):
  Table 3   : exact P0 l^4/(192EI) = 2501.19 mm^2; analytical influence line by
              the trapezoidal rule 2488.68 (-0.500 %) and Simpson 2501.85
              (+0.027 %) at dx = 250 mm; measured record, trapezoid 2513.43 (+0.49 %).
  Section 3.2: 20/21/23 intervals; Simpson with the 3/8 end panel on the
              two- and three-load records.
  Section 2.4: trapezoid converges as dx^2, Simpson nearly exact.
  Section 6.1: quadrature bias -0.5000 % for all three configurations (spacings
              multiples of dx); at a spacing of 300 mm -0.110 %, at 375 mm
              +0.249 %; SLM residual 0.4-0.75 %.

Run:  python3 -I code/supplementary/s02_quadrature_table3.py
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import beam_theory as bt  # noqa: E402


def head(t):
    print(("\n== %s " % t).ljust(78, "="))


exact = bt.C_M * bt.P0
head("Table 3: deflection integral, single load (40.64 N), dx = 250 mm")
grid = np.arange(0, 2 * bt.L_SPAN + 1, bt.DX)
y_an = bt.eta(grid, bt.P0)
rows = [("Exact, P0 l^4/(192EI)", exact, "2501.19", "n/a"),
        ("Analytical IL, trapezoidal rule", bt.integral_trapz(y_an, grid), "2488.68", "-0.500 %"),
        ("Analytical IL, Simpson rule", bt.integral_simpson(y_an, grid), "2501.85", "+0.027 %"),
        ("Measured, trapezoidal rule", bt.integral_trapz(bt.Y_SINGLE, bt.X_1), "2513.43", "+0.49 %"),
        ("Measured, Simpson rule (not in Table 3)", bt.integral_simpson(bt.Y_SINGLE, bt.X_1), "-", "-")]
print("  %-42s %12s %10s   %s" % ("quantity", "mm^2", "diff", "manuscript"))
for name, v, ms, md in rows:
    print("  %-42s %12.4f %+9.3f %%   %s (%s)" % (name, v, 100 * (v - exact) / exact, ms, md))
print("  tabulated analytical column (Table C.1), trapezoid: %.4f mm^2"
      % bt.integral_trapz(bt.Y_ANALYTICAL, bt.X_1))

head("Number of intervals and Simpson with 3/8 end panel (Section 3.2)")
for case in ("single", "two", "three"):
    xg, yg, W = bt.CASES[case]
    n = len(xg) - 1
    yan = bt.record(case, xg)
    Iex = bt.C_M * W
    print("  %-6s n = %2d  measured: trap %9.2f  Simpson%s %9.2f | analytical: trap %+.4f %%  "
          "Simpson %+.4f %%"
          % (case, n, bt.integral_trapz(yg, xg), "+3/8" if n % 2 else "    ",
             bt.integral_simpson(yg, xg),
             100 * (bt.integral_trapz(yan, xg) / Iex - 1),
             100 * (bt.integral_simpson(yan, xg) / Iex - 1)))
print("  (manuscript: 20, 21 and 23 intervals; analytical-record trapezoid bias -0.5000 % for all)")

head("Quadrature convergence on the exact influence line")
print("  %7s %9s %12s %10s %12s %11s" % ("n/span", "dx (mm)", "trapezoid", "bias %", "Simpson",
                                         "bias %"))
for n in (4, 5, 10, 20, 25, 50, 100):
    xs = np.linspace(0, 2 * bt.L_SPAN, 2 * n + 1)
    ys = bt.eta(xs, bt.P0)
    tr, si = bt.integral_trapz(ys, xs), bt.integral_simpson(ys, xs)
    print("  %7d %9.1f %12.3f %+10.4f %12.3f %+11.5f"
          % (n, bt.L_SPAN / n, tr, 100 * (tr / exact - 1), si, 100 * (si / exact - 1)))
print("  trapezoid bias x (n/10)^2 is constant -> O(dx^2) (Section 2.4)")

head("Section 6.1: quadrature bias when the spacing is not a multiple of dx")


def group_bias(spacing, case="two"):
    """Trapezoid bias of the analytical record of a load group on the 250 mm grid
    (leading load at the grid points), with the second load at `spacing`."""
    g = bt.GROUPS[case]
    a = [0.0, spacing] if case == "two" else g["a"]
    amax = max(a)
    xg = np.arange(0, 2 * bt.L_SPAN + amax + bt.DX, bt.DX)   # record to cover the crossing
    y = bt.record(case, xg, a=a)
    W = bt.group_weight(case)
    return 100 * (bt.integral_trapz(y, xg) / (bt.C_M * W) - 1)


b0 = 100 * (bt.integral_trapz(y_an, grid) / exact - 1)
for sp_ in (250.0, 300.0, 375.0, 500.0):
    b = group_bias(sp_)
    print("  two-load group, spacing %5.0f mm: bias %+.3f %%; SLM residual (e_q,t - e_q,0) = %+.3f pp"
          % (sp_, b, b - b0))
print("  (manuscript: 300 mm -0.110 %, 375 mm +0.249 %, residual 0.4-0.75 %)")
print("  three-load group as tested: bias %+.4f %%" % group_bias(None, "three"))


def shifted_copy_bias(delta):
    """Trapezoid bias of ONE influence-line copy whose entry lies delta mm after a grid point."""
    xg = np.arange(-bt.DX, 2 * bt.L_SPAN + 2 * bt.DX + 1, bt.DX)
    return 100 * (bt.integral_trapz(bt.eta(xg - delta, 1.0), xg) / bt.C_M - 1)


print("  single shifted copy, grid offset 50 mm (spacing 300): %+.4f %%; 125 mm (spacing 375): %+.4f %%"
      % (shifted_copy_bias(50.0), shifted_copy_bias(125.0)))
print("  NOTE: neither interpretation reproduces -0.110 %; +0.249 % is close to the single")
print("  shifted copy at 125 mm (+0.250 %).  Other load orders/groups tried in")
print("  REPRODUCTION_REPORT.md also fail.  The manuscript values remain unreproduced.")
