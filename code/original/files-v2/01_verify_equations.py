"""
01_verify_equations.py
======================
Independent verification, symbolic (SymPy) and numeric (NumPy), of every
equation in the manuscript.  This is the script that located the errors
listed in Annex A.1 of the revised paper.

Run:  python3 01_verify_equations.py
"""

import numpy as np
import sympy as sp

import beam_theory as bt

P, l, x, s, EI = sp.symbols('P l x s EI', positive=True)
line = lambda t='': print(('\n== %s ' % t).ljust(74, '=') if t else '')


# --------------------------------------------------------------------------
line("Eq. (1) and (2) - support reactions")
# --------------------------------------------------------------------------
RA_AB = P * (x**3 - 5*l**2*x + 4*l**3) / (4*l**3)
RB_AB = P * (-x**3 + 3*l**2*x) / (2*l**3)
RC_AB = P * (x**3 - l**2*x) / (4*l**3)

print("equilibrium  sum(R) - P = ", sp.simplify(RA_AB + RB_AB + RC_AB - P))
sub = {x: l/2}
print("at x = l/2 :  R_A = %s,  R_B = %s,  R_C = %s"
      % (sp.nsimplify(RA_AB.subs(sub)/P), sp.nsimplify(RB_AB.subs(sub)/P),
         sp.nsimplify(RC_AB.subs(sub)/P)))
print("expected   :  13P/32, 11P/16, -3P/32  (simple interior support)")
print("NOTE: these values are NOT those of a beam with a rotation-restrained")
print("      support at B, which is how the original draft described it.")

# span BC obtained from span AB by the symmetry substitution x -> 2l - x
RA_BC = P * (-x**3 + 6*l*x**2 - 11*l**2*x + 6*l**3) / (4*l**3)
RB_BC = P * (x**3 - 6*l*x**2 + 9*l**2*x - 2*l**3) / (2*l**3)
RC_BC = P * (-x**3 + 6*l*x**2 - 7*l**2*x + 2*l**3) / (4*l**3)
print("symmetry check R_C^BC - R_A^AB(2l-x) =",
      sp.expand(RC_BC - RA_AB.subs(x, 2*l - x)))
print("symmetry check R_A^BC - R_C^AB(2l-x) =",
      sp.expand(RA_BC - RC_AB.subs(x, 2*l - x)))
print("symmetry check R_B^BC - R_B^AB(2l-x) =",
      sp.expand(RB_BC - RB_AB.subs(x, 2*l - x)))


# --------------------------------------------------------------------------
line("Eq. (5) - full deflection field, and its consistency with Eq. (6)")
# --------------------------------------------------------------------------
y5_a = P/(24*EI*l**3) * (7*l**4*s*x - 4*l**3*s**3 - 12*l**3*s*x**2
                         + 5*l**2*s**3*x + 5*l**2*s*x**3 - s**3*x**3)
y5_b = P/(24*EI*l**3) * (7*l**4*s*x - 4*l**3*x**3 - 12*l**3*s**2*x
                         + 5*l**2*s**3*x + 5*l**2*s*x**3 - s**3*x**3)
y5_c = P/(24*EI*l**3) * (6*l**5*s - 11*l**4*s*x - 6*l**3*s**3 + 6*l**3*s*x**2
                         + 11*l**2*s**3*x - l**2*s*x**3 - 6*l*s**3*x**2
                         + s**3*x**3)
print("Maxwell reciprocity, branch(a) with s<->x  minus branch(b) :",
      sp.expand(y5_a.subs({s: x, x: s}, simultaneous=True) - y5_b))

# Eq. (6): specialise Eq. (5) to s = l/2
y6_1 = P * (9*l**2*x - 13*x**3) / (192*EI)
y6_2 = P * (-4*l**3 + 33*l**2*x - 48*l*x**2 + 19*x**3) / (192*EI)
y6_3 = P * (6*l**3 - 11*l**2*x + 6*l*x**2 - x**3) / (64*EI)
print("Eq.(5b) at s=l/2 minus Eq.(6) branch 1 :", sp.simplify(y5_b.subs(s, l/2) - y6_1))
print("Eq.(5a) at s=l/2 minus Eq.(6) branch 2 :", sp.simplify(y5_a.subs(s, l/2) - y6_2))
print("Eq.(5c) at s=l/2 minus Eq.(6) branch 3 :", sp.simplify(y5_c.subs(s, l/2) - y6_3))
print("-> the third branch requires the denominator 64*EI")

print("continuity at x = l/2 :", sp.simplify(y6_1.subs(x, l/2) - y6_2.subs(x, l/2)))
print("value at x = l        :", sp.simplify(y6_2.subs(x, l)), sp.simplify(y6_3.subs(x, l)))
print("value at x = 2l       :", sp.simplify(y6_3.subs(x, 2*l)))
print("slope continuity at l :",
      sp.simplify(sp.diff(y6_2, x).subs(x, l) - sp.diff(y6_3, x).subs(x, l)))


# --------------------------------------------------------------------------
line("ERROR FOUND - factorised form printed as Eq. (15)/(16) of the old draft")
# --------------------------------------------------------------------------
f2_old = P * (x - l) * (4*l**2 - 29*l*x + 19*x**2) / (192*EI)
f3_old = P * (2*l - x) * (3*l**2 - 4*l*x + x**2) / (192*EI)   # as printed
print("branch 2 (correct)          :", sp.simplify(f2_old - y6_2))
print("branch 3 as printed, y6/f3  :", sp.simplify(y6_3 / f3_old))
print("-> the printed third branch is a factor of 3 too small "
      "(192*EI should read 64*EI)")

# numeric confirmation against Table 1
xv = 3750.0
print("at x = 3750 mm : correct = %+.4f mm  (Table 1 gives -1.1255 mm)"
      % bt.eta(xv, bt.P0))
wrong = bt.P0 * (6*bt.L_SPAN**3 - 11*bt.L_SPAN**2*xv + 6*bt.L_SPAN*xv**2
                 - xv**3) / (192*bt.EI)
print("                 as printed = %+.4f mm" % wrong)


# --------------------------------------------------------------------------
line("Eq. (11) - closed-form invariance constant")
# --------------------------------------------------------------------------
C_sym = (sp.integrate(y6_1, (x, 0, l/2))
         + sp.integrate(y6_2, (x, l/2, l))
         + sp.integrate(y6_3, (x, l, 2*l)))
print("C_m * P =", sp.simplify(C_sym), "   (expected P*l**4/(192*EI))")


# --------------------------------------------------------------------------
line("Eq. (6) against the tabulated values of Table 1")
# --------------------------------------------------------------------------
y_calc = bt.eta(bt.X_1, bt.P0)
print("max |Eq.(6) - reported analytical| = %.2e mm"
      % np.max(np.abs(y_calc - bt.Y_ANALYTICAL)))


# --------------------------------------------------------------------------
line("Unit check on the load values reported in the old draft")
# --------------------------------------------------------------------------
for g_mass, printed_N in [(6829.0, 66992.5), (12750.0, 125077.5)]:
    print("%8.1f g  ->  %8.3f N     old draft printed %10.1f N  (x %.0f)"
          % (g_mass, g_mass / 1000 * bt.G, printed_N,
             printed_N / (g_mass / 1000 * bt.G)))
print("-> every force value in the old draft was overstated by a factor of 1000")
