"""Closed-form invariance constant C_m for three-span continuous beams (WP2).

Derivation (SymPy, from first principles):
  * each span i is a simply supported Euler-Bernoulli beam with uniform load q_i,
    rigidity EI_i (piecewise constant) and end moments M_left, M_right
    (sagging positive, w downward positive, M = -EI w'');
  * the two redundant support moments M_B, M_C follow from slope continuity at
    the interior supports (this reproduces the three-moment equation);
  * C_m = w_q(x_m)/q0 (Maxwell-Betti corollary, Eq. (10) of the manuscript).

Run:  python code/analysis/cm_3span_theory.py
Prints the symbolic results and writes the observability map
(figures/fig_obs_map_3span.png, code/analysis/data/obs_map_3span*.csv).
"""
import os
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

# --------------------------------------------------------------------------
# 1. Generic span solution and three-span compatibility
# --------------------------------------------------------------------------
s, L, EI, q, Ml, Mr = sp.symbols("s L EI q M_l M_r", real=True)


def span_deflection():
    """w(s) on 0<=s<=L for UDL q and end moments Ml (s=0), Mr (s=L)."""
    w = sp.Function("w")
    c = sp.symbols("c0:4")
    wexpr = q * s**4 / (24 * EI) + c[0] + c[1] * s + c[2] * s**2 + c[3] * s**3
    eqs = [wexpr.subs(s, 0), wexpr.subs(s, L),
           (-EI * sp.diff(wexpr, s, 2)).subs(s, 0) - Ml,
           (-EI * sp.diff(wexpr, s, 2)).subs(s, L) - Mr]
    sol = sp.solve(eqs, c, dict=True)[0]
    return sp.simplify(wexpr.subs(sol))


W = span_deflection()
dW = sp.diff(W, s)

L1, L2, L3, E1, E2, E3, q1, q2, q3 = sp.symbols(
    "L1 L2 L3 EI1 EI2 EI3 q1 q2 q3", positive=True)
MB, MC = sp.symbols("M_B M_C", real=True)


def w_span(i, Mleft, Mright):
    Ls, Es, qs = [(L1, E1, q1), (L2, E2, q2), (L3, E3, q3)][i]
    return W.subs({L: Ls, EI: Es, q: qs, Ml: Mleft, Mr: Mright})


w1 = w_span(0, 0, MB)
w2 = w_span(1, MB, MC)
w3 = w_span(2, MC, 0)
# slope continuity at B (end of span 1 = start of span 2) and at C
eqB = sp.diff(w1, s).subs(s, L1) - sp.diff(w2, s).subs(s, 0)
eqC = sp.diff(w2, s).subs(s, L2) - sp.diff(w3, s).subs(s, 0)
SOL = sp.solve([eqB, eqC], [MB, MC], dict=True)[0]
MB_gen = sp.simplify(SOL[MB])
MC_gen = sp.simplify(SOL[MC])

# general (asymmetric) C_m, sensor in span 1 at s = xi*L1, all spans loaded q0
xi, eta, beta, rho, q0 = sp.symbols("xi eta beta rho q0", positive=True)
a1, a3 = sp.symbols("alpha1 alpha3", positive=True)   # L1/L2, L3/L2


def Cm_general_span(i, var):
    """Symbolic C_m for a sensor in span i (0,1,2) at s = var*L_i, uniform q0."""
    Mb, Mc = MB_gen, MC_gen
    w = [w_span(0, 0, Mb), w_span(1, Mb, Mc), w_span(2, Mc, 0)][i]
    Li = [L1, L2, L3][i]
    expr = w.subs(s, var * Li).subs({q1: q0, q2: q0, q3: q0}) / q0
    return sp.simplify(expr)


# --------------------------------------------------------------------------
# 2. Symmetric three-span beam: L1 = L3 = Ls, L2 = beta*Ls, EI2 = rho*EI1
# --------------------------------------------------------------------------
Ls, EIs = sp.symbols("L_s EI_s", positive=True)
SYM = {L1: Ls, L3: Ls, L2: beta * Ls, E1: EIs, E3: EIs, E2: rho * EIs}

C_side = sp.simplify(Cm_general_span(0, xi).subs(SYM))
C_main = sp.simplify(Cm_general_span(1, eta).subs(SYM))
N_side = sp.factor(sp.simplify(192 * EIs * C_side / Ls**4))            # /Ls^4/(192EIs)
N_main = sp.factor(sp.simplify(192 * rho * EIs * C_main / (beta * Ls)**4))  # /Lm^4/(192EIm)

MB_sym = sp.simplify(MB_gen.subs(SYM).subs({q1: q0, q2: q0, q3: q0}))
mu = sp.simplify(-8 * MB_sym / (q0 * Ls**2))            # same definition as two-span
nu = sp.simplify(-12 * MB_sym / (q0 * (beta * Ls)**2))
mu_s, nu_s = sp.symbols("mu nu", positive=True)
F_side = 8 * (xi * (1 - 2 * xi**2 + xi**3) - mu_s / 2 * xi * (1 - xi**2))
G_main = 8 * (eta * (1 - 2 * eta**2 + eta**3) - nu_s * eta * (1 - eta))

# span-wise contributions (load only span j) for a side-span sensor
def side_contrib(j, var=xi):
    loads = {q1: 0, q2: 0, q3: 0}
    loads[[q1, q2, q3][j]] = q0
    w = w_span(0, 0, MB_gen).subs(s, var * L1).subs(loads) / q0
    return sp.factor(sp.simplify(192 * EIs * w.subs(SYM) / Ls**4))


def main_contrib(j, var=eta):
    loads = {q1: 0, q2: 0, q3: 0}
    loads[[q1, q2, q3][j]] = q0
    w = w_span(1, MB_gen, MC_gen).subs(s, var * L2).subs(loads) / q0
    return sp.factor(sp.simplify(192 * rho * EIs * w.subs(SYM) / (beta * Ls)**4))


# --------------------------------------------------------------------------
# 3. Numeric helpers (lambdified closed forms)
# --------------------------------------------------------------------------
f_side = sp.lambdify((xi, beta, rho), N_side, "numpy")
f_main = sp.lambdify((eta, beta, rho), N_main, "numpy")
N_gen = sp.simplify(192 * E1 * Cm_general_span(0, xi) / L1**4)
f_gen = sp.lambdify((xi, L1, L2, L3, E1, E2, E3), N_gen, "numpy")


def side_norm(xi_, beta_, rho_=1.0):
    return float(f_side(xi_, beta_, rho_))


def main_norm(eta_, beta_, rho_=1.0):
    return float(f_main(eta_, beta_, rho_))


def general_norm(xi_, spans, EIs_=(1.0, 1.0, 1.0)):
    return float(f_gen(xi_, *spans, *EIs_))


def blind_beta_mid(rho_=1):
    """Real positive root of 6 beta^3 - 15 beta - 4 rho = 0 (mid side-span)."""
    b = sp.symbols("b", positive=True)
    return sp.solve(sp.Eq(6 * b**3 - 15 * b - 4 * rho_, 0), b)


def xi_opt(beta_, rho_=1.0):
    """Sensor position maximising the side-span C_m (root of the cubic in (0,1))."""
    m = float(mu.subs({beta: beta_, rho: rho_}))
    r = np.roots([8.0, -(12.0 - 3.0 * m), 0.0, 2.0 - m])
    r = [x.real for x in r if abs(x.imag) < 1e-12 and 0 < x.real < 1]
    best = max(r, key=lambda x: side_norm(x, beta_, rho_))
    return best, side_norm(best, beta_, rho_)


# --------------------------------------------------------------------------
# 4. Observability maps
# --------------------------------------------------------------------------
def make_maps():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    os.makedirs(os.path.join(HERE, "data"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "figures"), exist_ok=True)

    # (a) symmetric, uniform EI: beta x xi (side-span sensor)
    B = np.linspace(0.5, 2.5, 201)
    X = np.linspace(0.01, 0.99, 99)
    BB, XX = np.meshgrid(B, X)
    Z = f_side(XX, BB, 1.0)
    with open(os.path.join(HERE, "data", "obs_map_3span.csv"), "w") as fh:
        fh.write("# symmetric three-span, uniform EI, side-span sensor; "
                 "value = 192 EI_s C_m / L_s^4 (closed form)\n")
        fh.write("beta,xi,Cm_norm\n")
        for i in range(XX.shape[0]):
            for j in range(XX.shape[1]):
                fh.write(f"{BB[i, j]:.4f},{XX[i, j]:.4f},{Z[i, j]:.10f}\n")

    # (b) asymmetric, uniform EI: L1/L2 x L3/L2, sensor at mid span 1
    A1 = np.linspace(0.3, 1.2, 181)
    A3 = np.linspace(0.3, 1.2, 181)
    AA1, AA3 = np.meshgrid(A1, A3)
    Z2 = f_gen(0.5, AA1, 1.0, AA3, 1.0, 1.0, 1.0)
    with open(os.path.join(HERE, "data", "obs_map_3span_asym.csv"), "w") as fh:
        fh.write("# asymmetric three-span, uniform EI, sensor at mid span 1; "
                 "value = 192 EI C_m / L1^4 (closed form)\n")
        fh.write("L1_over_L2,L3_over_L2,Cm_norm\n")
        for i in range(AA1.shape[0]):
            for j in range(AA1.shape[1]):
                fh.write(f"{AA1[i, j]:.4f},{AA3[i, j]:.4f},{Z2[i, j]:.10f}\n")

    fig, ax = plt.subplots(1, 2, figsize=(11, 4.4), constrained_layout=True)
    lev = np.linspace(-1.5, 1.5, 31)
    cs = ax[0].contourf(BB, XX, np.clip(Z, -1.5, 1.5), levels=lev, cmap="RdBu")
    ax[0].contour(BB, XX, Z, levels=[0.0], colors="k", linewidths=2)
    ax[0].contourf(BB, XX, np.abs(Z), levels=[0, 0.2], colors="none",
                   hatches=["////"])
    xo = np.array([xi_opt(b) for b in B])
    ok = xo[:, 1] > 0                                 # optimum only where C_m > 0
    ax[0].plot(B[ok], xo[ok, 0], "k--", lw=1, label=r"$\xi^*(\beta)$")
    for nm, b in [("Cau May 55+90+55", 90 / 55), ("Thai Binh 42+63+42", 63 / 42)]:
        ax[0].plot(b, 0.5, "ko", ms=5)
        ax[0].annotate(nm, (b, 0.5), (0.62, 0.80) if b > 1.6 else (0.62, 0.68),
                       fontsize=8, arrowprops=dict(arrowstyle="-", lw=0.6))
    ax[0].set_xlabel(r"$\beta = L_m/L_s$")
    ax[0].set_ylabel(r"side-span sensor position $\xi = x/L_s$")
    ax[0].set_title("(a) symmetric, uniform EI", fontsize=10)
    ax[0].legend(loc="lower left", fontsize=8)
    fig.colorbar(cs, ax=ax[0], label=r"$192EI_sC_m/L_s^4$")

    cs2 = ax[1].contourf(AA1, AA3, np.clip(Z2, -1.5, 1.5), levels=lev, cmap="RdBu")
    ax[1].contour(AA1, AA3, Z2, levels=[0.0], colors="k", linewidths=2)
    ax[1].contourf(AA1, AA3, np.abs(Z2), levels=[0, 0.2], colors="none",
                   hatches=["////"])
    ax[1].plot(A1, A1, "k:", lw=0.8)
    ax[1].set_xlabel(r"$L_1/L_2$ (instrumented side span)")
    ax[1].set_ylabel(r"$L_3/L_2$ (far side span)")
    ax[1].set_title(r"(b) asymmetric, uniform EI, sensor at mid span 1", fontsize=10)
    fig.colorbar(cs2, ax=ax[1], label=r"$192EI_1C_m/L_1^4$")
    out = os.path.join(ROOT, "figures", "fig_obs_map_3span.png")
    fig.savefig(out, dpi=200)
    return out


if __name__ == "__main__":
    sp.init_printing(use_unicode=False)
    print("Three-moment check (general):")
    print("  M_B =", MB_gen)
    print("\nSymmetric beam, uniform load q0:")
    print("  M_B = M_C =", sp.factor(MB_sym))
    print("  mu  = -8 M_B/(q0 Ls^2)  =", sp.factor(mu))
    print("  nu  = -12 M_B/(q0 Lm^2) =", sp.factor(nu))
    print("  192 EI_s C_m/Ls^4 (side) =", N_side)
    print("    equals F_side(xi,mu)? ", sp.simplify(N_side - F_side.subs(mu_s, mu)) == 0)
    print("  192 EI_m C_m/Lm^4 (main) =", N_main)
    print("    equals G_main(eta,nu)?", sp.simplify(N_main - G_main.subs(nu_s, nu)) == 0)

    # blind loci
    mu_c = sp.factor(sp.solve(sp.Eq(F_side, 0), mu_s)[0])
    nu_c = sp.factor(sp.solve(sp.Eq(G_main, 0), nu_s)[0])
    print("\nBlind locus, side sensor: mu_crit(xi) =", mu_c)
    print("  rho_crit(beta, xi) =", sp.factor(sp.solve(sp.Eq(mu, mu_c), rho)[0]))
    print("  mid-span: rho_crit(beta) =", sp.factor(sp.solve(sp.Eq(mu, mu_c.subs(xi, sp.Rational(1, 2))), rho)[0]))
    print("Blind locus, main sensor: nu_crit(eta) =", nu_c)
    print("  rho_crit(beta, eta) =", sp.factor(sp.solve(sp.Eq(nu, nu_c), rho)[0]))

    b = sp.symbols("b", positive=True)
    cub = 6 * b**3 - 15 * b - 4
    roots = sp.solve(cub, b)
    print("\nMid side-span, uniform EI: 6 b^3 - 15 b - 4 = 0")
    print("  discriminant =", sp.discriminant(cub, b), "(>0: three real roots, casus irreducibilis)")
    for r in roots:
        print("  root:", sp.nsimplify(r), "=", sp.N(r, 15))
    beta_trig = sp.sqrt(sp.Rational(10, 3)) * sp.cos(sp.acos(sp.Rational(2, 5) * sp.sqrt(sp.Rational(6, 5))) / 3)
    beta_crit_mid = beta_trig
    print("  trigonometric form sqrt(10/3) cos( acos( (2/5) sqrt(6/5) )/3 ) =", sp.N(beta_trig, 15))
    cubm = 3 * b**3 + 10 * b**2 - 12
    rm = [r for r in sp.Poly(cubm, b).nroots(n=15) if r.is_real and r > 0]
    print("Mid main-span, uniform EI: 3 b^3 + 10 b^2 - 12 = 0  -> beta_crit =", rm)

    print("Whole side span blind (mu = 2, i.e. mu_crit(xi->0)): beta^3 - 3 beta - rho = 0;"
          " rho=1 -> beta = 2 cos(pi/9) =", sp.N(2 * sp.cos(sp.pi / 9), 15),
          " check:", sp.N((2 * sp.cos(sp.pi / 9))**3 - 3 * 2 * sp.cos(sp.pi / 9) - 1, 5))
    nb = [r for r in sp.Poly(30 * b**3 - 69 * b - 16, b).nroots(n=15) if r.is_real and r > 0]
    print("Near-blind edge |N|=0.2, mid side, uniform EI: mu = 23/15 <=> 30 b^3 - 69 b - 16 = 0 ->", nb)
    for nm, bb in [("Cau May", sp.Rational(90, 55)), ("Thai Binh", sp.Rational(63, 42))]:
        print(f"  {nm}: beta={float(bb):.6f}  rho_crit(mid side)={float(3*bb*(2*bb**2-5)/4):.6f}"
              f"  neg/pos(mid side, uniform)={float(6*bb**3/(15*bb+4)):.6f}")
    print("\nOptimal side-span sensor: d/dxi F = 0  <=>",
          sp.factor(sp.expand(2 * sp.diff(F_side, xi) / 8)), "= 0")
    for bb in [1.0, 1.2, 1.4, 1.5, 90 / 55, 1.6, 1.7]:
        xo, vo = xi_opt(bb)
        print(f"  beta={bb:.5f}: mu={float(mu.subs({beta: bb, rho: 1})):.8f}  "
              f"xi*={xo:.8f}  Cm_norm(xi*)={vo:.8f}  Cm_norm(0.5)={side_norm(0.5, bb):.8f}")

    print("\nSpan-wise contributions, side sensor (normalised by Ls^4/192EIs):")
    for j in range(3):
        print(f"  span {j+1}:", side_contrib(j))
    print("Span-wise contributions, main sensor (normalised by Lm^4/192EIm):")
    for j in range(3):
        print(f"  span {j+1}:", main_contrib(j))
    from scipy.optimize import brentq
    print("\nAsymmetric, uniform EI, mid span-1 sensor: blind L1/L2 for given L3/L2")
    for a3_ in [0.3, 0.5, 0.6, 0.8, 1.0, 1.2]:
        r = brentq(lambda a: general_norm(0.5, (a, 1.0, a3_)), 0.3, 1.2, xtol=1e-14)
        print(f"  L3/L2={a3_:.2f}: L1/L2_crit={r:.6f}  (L2/L1={1/r:.6f})")
    print("\nFigure:", make_maps())
