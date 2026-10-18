"""s01_symbolic_two_span.py - symbolic verification of the two-span solution.

Reproduces / checks (SCHM manuscript):
  Appendix A : reactions Eq. (A.1), support moment, influence line Eq. (A.2)
               derived twice (force method for the load position; double
               integration of the deflected shape under a load at l/2 plus
               Maxwell), continuity, 64EI in branch 3, 2.875, 71.9 %, 0.480l,
               72.1 %, span-wise decomposition, Table A.1.
  Section 2.1: C_m = integral of eta = l^4/(192 EI), Eq. (2)-(3); strain blind
               point 0.75L.
  Section 2.2: closed form Eqs. (4)-(5) derived from first principles, Table 1
               (closed form vs FE, two FE routes of Eq. (3)), blind condition
               Eq. (6), exact roots Eq. (7): rho_L = (3+sqrt33)/6, xi* =
               (1+sqrt33)/16, 1.039895, 10 % at 0.9L1, rho_L = 1.6 and 1.45
               statements, near-blind band 1.385 < rho_L < 1.525, rig 3644 mm.
  Section 2.4: R_m = 4/7, O_m = 2 sqrt(44765)/1279 = 0.331, monotonicity of O_m.

Run:  python3 -I code/supplementary/s01_symbolic_two_span.py
"""
import os
import sys

import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize_scalar

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import beam_theory as bt  # noqa: E402

P, l, x, s, EI, q = sp.symbols("P l x s EI q", positive=True)
xi, mu, rL, rE = sp.symbols("xi mu rho_L rho_EI", positive=True)
L1, E1 = sp.symbols("L_1 EI_1", positive=True)


def head(t):
    print(("\n== %s " % t).ljust(78, "="))


def show(label, expr, expect=None, simplify=True):
    e = sp.simplify(expr) if simplify else expr
    tail = "" if expect is None else "   (manuscript: %s)" % expect
    print("  %-52s %s%s" % (label, e, tail))
    return e


# ---------------------------------------------------------------------------
head("A.1  Reactions for a load P at 0 <= x <= l  (Eq. A.1)")
# ---------------------------------------------------------------------------
# force method: simply supported beam A-C (length 2l), redundant R_B at x = l
def ss_unit(p, a, Lb, p_left_of_load):
    """Deflection (down +, times EI) at p of a simply supported beam of length Lb
    under a unit load at a.  The ordering of p and a is passed explicitly."""
    if not p_left_of_load:
        p, a = Lb - p, Lb - a                     # mirror
    b = Lb - a
    return b * p * (Lb ** 2 - b ** 2 - p ** 2) / (6 * Lb)


d_B_B = ss_unit(l, l, 2 * l, True)
RB = sp.simplify(P * ss_unit(l, x, 2 * l, False) / d_B_B)          # load at x <= l
RA = sp.simplify(P * (2 * l - x) / (2 * l) - RB / 2)
RC = sp.simplify(P - RA - RB)
show("R_A - P(x^3-5l^2x+4l^3)/(4l^3)", RA - P * (x ** 3 - 5 * l ** 2 * x + 4 * l ** 3) / (4 * l ** 3), "0")
show("R_B - P(-x^3+3l^2x)/(2l^3)", RB - P * (-x ** 3 + 3 * l ** 2 * x) / (2 * l ** 3), "0")
show("R_C - P(x^3-l^2x)/(4l^3)", RC - P * (x ** 3 - l ** 2 * x) / (4 * l ** 3), "0")
show("R_A, R_B, R_C at x = l/2 (/P)", sp.Tuple(*(r.subs(x, l / 2) / P for r in (RA, RB, RC))),
     "13/32, 11/16, -3/32")
MB = sp.simplify(RA * l - P * (l - x))
show("M_B + P x (l^2-x^2)/(4l^2)", MB + P * x * (l ** 2 - x ** 2) / (4 * l ** 2), "0")

# ---------------------------------------------------------------------------
head("A.2  Influence line at s = l/2, route 1: force method in the load position")
# ---------------------------------------------------------------------------
eta1 = x * (9 * l ** 2 - 13 * x ** 2) / (192 * EI)
eta2 = (x - l) * (4 * l ** 2 - 29 * l * x + 19 * x ** 2) / (192 * EI)
eta3 = (2 * l - x) * (3 * l ** 2 - 4 * l * x + x ** 2) / (64 * EI)
m = l / 2
d_m_B = ss_unit(m, l, 2 * l, True)                 # unit load at B, deflection at m
# (branch, m left of load?, B left of load?, Eq. (A.2) branch)
for name, m_left, B_left, eta_ms in (("branch 1, 0<=x<=l/2", False, False, eta1),
                                     ("branch 2, l/2<x<=l", True, False, eta2),
                                     ("branch 3, l<x<=2l", True, True, eta3)):
    rb = ss_unit(l, x, 2 * l, B_left) / d_B_B
    eta_fm = (ss_unit(m, x, 2 * l, m_left) - rb * d_m_B) / EI
    show("force method - Eq. (A.2), " + name, sp.factor(eta_fm - eta_ms), "0")

# ---------------------------------------------------------------------------
head("A.2  route 2: double integration, load at l/2, Maxwell eta_m(x) = w_m(x)")
# ---------------------------------------------------------------------------
c = sp.symbols("c1:7")
RA_, RB_ = sp.Rational(13, 32), sp.Rational(11, 16)     # Eq. (A.1) at x = l/2
Ms = (RA_ * x, RA_ * x - (x - l / 2), RA_ * x - (x - l / 2) + RB_ * (x - l))
# downward-positive deflection v, sagging-positive M: EI v'' = -M
v = [sp.integrate(sp.integrate(-Mk / EI, x), x) + c[2 * k] * x + c[2 * k + 1]
     for k, Mk in enumerate(Ms)]
# the six displacement conditions of Appendix A
conds = [v[0].subs(x, 0),
         (v[0] - v[1]).subs(x, l / 2), sp.diff(v[0] - v[1], x).subs(x, l / 2),
         v[1].subs(x, l), v[2].subs(x, l), v[2].subs(x, 2 * l)]
sol = sp.solve(conds, c, dict=True)[0]
v = [sp.simplify(vk.subs(sol)) for vk in v]
for k, ref in enumerate((eta1, eta2, eta3)):
    show("double integration - Eq. (A.2), branch %d" % (k + 1), v[k] - ref, "0")
show("slope continuity at x = l (not imposed; checks R_B)", sp.diff(v[1] - v[2], x).subs(x, l), "0")

head("A.2  continuity, twice differentiable, 64EI")
for k, (a_, b_, pt) in enumerate(((eta1, eta2, l / 2), (eta2, eta3, l))):
    show("eta, eta', eta'' jumps at %s" % pt,
         sp.Tuple(*(sp.simplify(sp.diff(a_ - b_, x, j).subs(x, pt)) for j in range(3))), "0, 0, 0")
show("eta at x = 0, l, 2l", sp.Tuple(eta1.subs(x, 0), eta2.subs(x, l), eta3.subs(x, 2 * l)))
f3_192 = (2 * l - x) * (3 * l ** 2 - 4 * l * x + x ** 2) / (192 * EI)
show("branch 3 with 64EI / branch 3 with 192EI", eta3 / f3_192, "factor 3 (64EI, not 192EI)")
print("  numeric: eta(3750 mm) * 40.64 N = %+.4f mm  (Table C.1 analytical: -1.1255)"
      % bt.eta(3750.0, bt.P0))
dev = np.max(np.abs(bt.eta(bt.X_1, bt.P0) - bt.Y_ANALYTICAL))
print("  max |Eq.(A.2) - Table C.1 analytical column| = %.1e mm (4-decimal rounding)" % dev)

head("A.2  mid-span values (Appendix A)")
e_mid = sp.simplify(eta1.subs(x, l / 2) * 192 * EI / l ** 3)
show("eta(l/2) * 192EI/l^3", e_mid, "2.875")
ss = l ** 3 / (48 * EI)
show("eta(l/2) / (Pl^3/48EI)", sp.N(eta1.subs(x, l / 2) / ss, 6), "71.9 %")
xs_ = sp.solve(sp.diff(eta1, x), x)[0]
show("argmax_x eta / l", sp.N(xs_ / l, 6), "0.480")
show("max eta / (Pl^3/48EI)", sp.N(eta1.subs(x, xs_) / ss, 6), "72.1 %")

# ---------------------------------------------------------------------------
head("Eq. (2)-(3): C_m, A+, A-, R_m (equal spans, mid-span)")
# ---------------------------------------------------------------------------
Cm_sym = sp.integrate(eta1, (x, 0, l / 2)) + sp.integrate(eta2, (x, l / 2, l)) \
    + sp.integrate(eta3, (x, l, 2 * l))
show("C_m (integral of Eq. A.2)", Cm_sym, "l**4/(192*EI)")
Ap = sp.integrate(eta1, (x, 0, l / 2)) + sp.integrate(eta2, (x, l / 2, l))
Am = sp.integrate(eta3, (x, l, 2 * l))
show("A+ * 192EI/l^4", Ap * 192 * EI / l ** 4, "1.750")
show("A- * 192EI/l^4", Am * 192 * EI / l ** 4, "-0.750")
show("R_m = C_m/A+", Cm_sym / Ap, "4/7")
print("  numeric C_m = %.4f mm^2/N (Section 3.1: 61.541); P0 C_m = %.2f mm^2 (Table 3: 2501.19)"
      % (bt.C_M, bt.C_M * bt.P0))
# uniform-load route of Eq. (3): two-span beam, uniform q, deflection at l/2
xx = sp.symbols("xx", positive=True)
wq = q * xx * (l ** 3 - 2 * l * xx ** 2 + xx ** 3) / (24 * EI) \
    - (q * l ** 2 / 8) * xx * (l ** 2 - xx ** 2) / (6 * EI * l)
show("w_q(l/2)/q  (Eq. 3, M_B = -q l^2/8)", wq.subs(xx, l / 2) / q, "l**4/(192*EI)")
# strain blind point
Mq = 3 * q * l * xx / 8 - q * xx ** 2 / 2
show("zero of M_q in span 1 (strain blind point)/l", sp.solve(Mq, xx)[0] / l, "0.75")

# ---------------------------------------------------------------------------
head("Eqs. (4)-(5): two-span closed form from first principles")
# ---------------------------------------------------------------------------
L2, E2 = rL * L1, rE * E1
MB_q = -q * (L1 ** 3 / E1 + L2 ** 3 / E2) / (8 * (L1 / E1 + L2 / E2))   # three-moment eq.
xm = xi * L1
w_ss = q * xm * (L1 ** 3 - 2 * L1 * xm ** 2 + xm ** 3) / (24 * E1)
w_M = MB_q * xm * (L1 ** 2 - xm ** 2) / (6 * E1 * L1)     # hogging M_B lifts span 1
Cm_gen = sp.simplify((w_ss + w_M) / q)
mu5 = (1 + rL ** 3 / rE) / (1 + rL / rE)
F4 = xi * (1 - 2 * xi ** 2 + xi ** 3) - mu / 2 * xi * (1 - xi ** 2)
show("C_m - L1^4/(24EI1) F(xi, mu(Eq.5))", Cm_gen - L1 ** 4 / (24 * E1) * F4.subs(mu, mu5), "0")
show("mu = -8 M_B/(q L1^2) - Eq. (5)", -8 * MB_q / (q * L1 ** 2) - mu5, "0")
show("rho_L = rho_EI = 1, xi = 1/2: C_m", Cm_gen.subs({rL: 1, rE: 1, xi: sp.Rational(1, 2)}),
     "L1^4/(192 EI1)")
dmu_dE = sp.factor(sp.diff(mu5, rE))
show("d mu / d rho_EI", dmu_dE, "proportional to rho_L(1-rho_L^2)")
dmu_dL = sp.factor(sp.diff(mu5, rL))
show("d mu / d rho_L", dmu_dL, "numerator rho_EI(3rho_L^2-1)+2rho_L^3")
show("mu(rho_L = 1/2, 1, 2), rho_EI = 1",
     sp.Tuple(*(mu5.subs({rE: 1, rL: v_}) for v_ in (sp.Rational(1, 2), 1, 2))), "0.750, 1, 3")

head("Eq. (6)-(7): blind condition and optimum")
mu_c = sp.factor(sp.solve(F4, mu)[0])
show("mu_crit(xi)", mu_c, "2(1+xi-xi^2)/(1+xi)")
show("mu_crit(1/2)", mu_c.subs(xi, sp.Rational(1, 2)), "5/3")
rEc = sp.solve(sp.Eq(mu5, mu), rE)[0]
show("rho_EI,crit - rho_L(rho_L^2-mu)/(mu-1)", rEc - rL * (rL ** 2 - mu) / (mu - 1), "0")
blind = sp.factor(sp.numer(sp.cancel(sp.together(mu5.subs(rE, 1) - sp.Rational(5, 3)))))
show("blind condition, uniform stiffness, mid-span", blind, "3rho^2-3rho-2 = 0", simplify=False)
rc = [r for r in sp.solve(blind, rL) if r.is_positive][0]
show("rho_L,crit", rc, "(3+sqrt(33))/6")
print("  rho_L,crit = %.5f   (manuscript: 1.45743); rig: 2500 mm x rho = %.1f mm (manuscript: 3644)"
      % (float(rc), 2500 * float(rc)))
dF = sp.factor(sp.diff(F4.subs(mu, 1), xi))
show("dF/dxi at mu = 1 (factored)", dF, "contains 8xi^2-xi-1", simplify=False)
xs_opt = [r for r in sp.solve(8 * xi ** 2 - xi - 1, xi) if r.is_positive][0]
show("xi*", xs_opt, "(1+sqrt(33))/16")
Nopt = 8 * F4.subs({mu: 1, xi: xs_opt})
print("  xi* = %.5f (0.42154); N(xi*) = %.8f (Table 1: 1.03989535); ratio to mid-span %.6f (1.039895)"
      % (float(xs_opt), float(Nopt), float(Nopt)))
print("  N(0.9)/N(xi*) = %.4f   (manuscript: 'falls to 10 %% of its maximum at 0.9L1')"
      % (bt.Nm_two_span(1.0, 0.9) / float(Nopt)))

head("Section 2.2 statements (numeric, Eq. 4)")
N = bt.Nm_two_span
print("  rho_L = 2: N = %.6f        (manuscript: -2.0, |N| twice the equal-span value)" % N(2.0))
print("  rho_L = 1.6: N(rho_EI = 0.5) = %+.4f, N(rho_EI = 4) = %+.4f   (manuscript: -0.78, +0.33)"
      % (N(1.6, 0.5, 0.5), N(1.6, 0.5, 4.0)))
z = brentq(lambda r: N(1.6, 0.5, r), 0.5, 4.0)
print("  rho_L = 1.6: zero crossing at rho_EI = %.4f   (manuscript: 2.14)" % z)
print("  rho_L = 1.45, xi = 0.5: N = %.4f   (manuscript: 0.021)" % N(1.45, 0.5))
r = minimize_scalar(lambda t: -N(1.45, t), bounds=(0.05, 0.95), method="bounded")
print("  rho_L = 1.45, xi = 0.266: N = %.4f (manuscript: 0.233); optimum there xi = %.3f, N = %.4f"
      % (N(1.45, 0.266), r.x, -r.fun))
lo = brentq(lambda t: N(t) - 0.2, 1.0, 1.457)
hi = brentq(lambda t: N(t) + 0.2, 1.458, 2.0)
print("  near-blind band |N| < 0.2: %.6f < rho_L < %.6f   (manuscript: 1.385 < rho_L < 1.525)" % (lo, hi))

head("Table 1: closed form Eq. (4) against FE evaluation of Eq. (3)")
print("  %-22s %8s %8s %13s %13s %13s %9s %9s" % ("case", "rho_L", "xi", "closed", "FE udl",
                                                  "FE IL-int", "d(udl)", "d(IL)"))
rows = [("Equal spans", 1.0, 0.5, "1.00000000"), ("Short adjacent span", 0.5, 0.5, "1.37500000"),
        ("Long adjacent span", 1.3, 0.5, "0.41500000"),
        ("Blind configuration", float(rc), 0.5, "0.00000000"), ("Beyond blind", 2.0, 0.5, "-2.00000000"),
        ("Optimal sensor", 1.0, float(xs_opt), "1.03989535"), ("Sensor near support", 1.0, 0.7, "0.60480000")]
for name, rho, x_, ms in rows:
    cf = N(rho, x_)
    b = bt.Beam([1.0, rho], ne=[40, int(round(40 * rho))], ei=1.0, extra=[x_])
    fu = 192 * b.Cm_udl(x_)
    fi = 192 * b.Cm_il(x_)
    print("  %-22s %8.5f %8.5f %13.8f %13.8f %13.8f %9.1e %9.1e  (ms %s)"
          % (name, rho, x_, cf, fu, fi, abs(fu - cf), abs(fi - cf), ms))
print("  note: 'Blind configuration' uses the exact root; the manuscript lists 1.45743.")
print("  FE differences are round-off (Hermite elements are nodally exact); their exact")
print("  size depends on mesh and BLAS and is not expected to equal the printed 1e-11.")

head("Table A.1: 192EI1 C_m/L1^4, mid-span sensor, uniform stiffness")
for rho, ms in ((0.5, 1.375), (0.7, 1.315), (0.8, 1.240), (1.0, 1.000), (1.2, 0.640), (1.3, 0.415),
                (1.4, 0.160), (float(rc), 0.0), (1.6, -0.440)):
    print("  L2/L1 = %-8.5f  N = %+.4f   (Table A.1: %+.3f)" % (rho, N(rho), ms))

head("Appendix A: span-wise decomposition (units L1^4/(192 EI1), uniform stiffness)")


def contrib(rho, x_):
    """(C+ from loading span 1 only, C- from loading span 2 only)."""
    lam = 1.0 / (1.0 + rho)               # L1/(L1+L2) with EI equal
    ss = x_ * (1 - 2 * x_ ** 2 + x_ ** 3) / 24.0
    mom = x_ * (1 - x_ ** 2) / 6.0
    mb1 = -lam / 8.0                       # M_B/(q L1^2), span 1 loaded
    mb2 = -rho ** 3 * lam / 8.0            # span 2 loaded
    return 192 * (ss + mb1 * mom), 192 * (mb2 * mom)


cp = [contrib(r_, 0.5) for r_ in np.linspace(0.5, 2.0, 151)]
print("  rho_L 0.5..2.0: C+ in [%.3f, %.3f] (1.50-2.00); C- in [%.3f, %.3f] (-0.125 to -4.00)"
      % (min(c_[0] for c_ in cp), max(c_[0] for c_ in cp), max(c_[1] for c_ in cp),
         min(c_[1] for c_ in cp)))
print("  equal spans, xi = 0.50: C+ = %.3f, C- = %.3f, net = %.3f (1.750, -0.750, 1.000)"
      % (*contrib(1, 0.5), sum(contrib(1, 0.5))))
print("  equal spans, xi = 0.42: C+ = %.3f, C- = %.3f, net = %.3f (1.732, -0.692, 1.040)"
      % (*contrib(1, 0.42), sum(contrib(1, 0.42))))

# ---------------------------------------------------------------------------
head("Eq. (15): O_m for the equal two-span beam, mid-span sensor")
# ---------------------------------------------------------------------------
I2 = sp.integrate(eta1 ** 2, (x, 0, l / 2)) + sp.integrate(eta2 ** 2, (x, l / 2, l)) \
    + sp.integrate(eta3 ** 2, (x, l, 2 * l))
Om = sp.nsimplify(sp.simplify(Cm_sym / sp.sqrt(2 * l * I2)))
show("O_m (L_tot = 2l, single axle)", Om, "2*sqrt(44765)/1279")
show("O_m - 2 sqrt(44765)/1279", Om - 2 * sp.sqrt(44765) / 1279, "0")
print("  O_m = %.4f (manuscript: 0.331)" % float(Om))


def Om_num(x_, ne=80):
    b = bt.Beam([1.0, 1.0], ne=ne, ei=1.0, extra=[x_])
    u = b.solve(b.point_load(x_, 1.0))     # eta_m(x) = w_m(x) by Maxwell
    tot2, tot = 0.0, 0.0
    sg = np.linspace(0, 1, 21)
    for e in range(b.ne):
        Le = b.x[e + 1] - b.x[e]
        Nn = np.array([bt.hermite(t * Le, Le) for t in sg])
        wv = Nn @ u[2 * e:2 * e + 4]
        from scipy.integrate import simpson
        tot2 += simpson(wv ** 2, x=sg * Le)
        tot += simpson(wv, x=sg * Le)
    return abs(tot) / np.sqrt(2.0 * tot2)


print("  numeric check at xi = 0.5: %.6f" % Om_num(0.5))
xi_list = np.round(np.arange(0.05, 0.96, 0.05), 2)
om = [Om_num(v_) for v_ in xi_list]
print("  xi:  " + " ".join("%5.2f" % v_ for v_ in xi_list))
print("  O_m: " + " ".join("%5.3f" % v_ for v_ in om))
print("  O_m monotonically decreasing in xi: %s   (manuscript: decreases monotonically"
      % bool(np.all(np.diff(om) < 0)))
print("  as the sensor moves away from the outer support)")

head("Section 3.1: shear deformation (order-of-magnitude check, not in files-v2)")
G_mod = bt.E_STEEL / (2 * 1.3)
A_web = 2 * (bt.B_OUT - bt.T_WALL) * bt.T_WALL
ratio = 12 * bt.EI / (G_mod * A_web * bt.L_SPAN ** 2)
print("  span/depth = %.0f (manuscript: 100)" % (bt.L_SPAN / bt.B_OUT))
print("  simply supported span, central load, web shear area: delta_s/delta_b = %.1e" % ratio)
print("  (manuscript: 8e-4; the basis of the printed value is not documented, same order)")
