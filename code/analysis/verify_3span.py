"""WP2 verification: three-span closed forms (cm_3span_theory.py) against the FE of
cm_multispan.py, and the haunched-girder FE against an independent force-method
(flexibility) solution with adaptive quadrature.

Run:  python code/analysis/verify_3span.py | tee code/analysis/logs/verify_3span.log
"""
import os
import sys
import numpy as np
import sympy as sp
from scipy.integrate import quad

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cm_multispan as fe                      # noqa: E402
import cm_3span_theory as th                   # noqa: E402

TOL = 1e-8
fails = []


def check(label, cf, num, scale=None):
    """Relative error |num-cf|/|cf|; for an exact zero use absolute error."""
    ref = abs(cf) if scale is None else scale
    err = abs(num - cf) / ref if ref > 0 else abs(num - cf)
    ok = err <= TOL
    if not ok:
        fails.append(label)
    kind = "rel" if ref > 0 else "abs"
    print(f"  {label:46s} closed={cf: .12f}  FE={num: .12f}  {kind}err={err:.1e} "
          f"{'OK' if ok else 'FAIL'}")
    return err


def fe_norm(spans, xm, Lref, EIref, EIs=None, route="udl", load_spans=None, ne=12):
    kw = dict(ne_per_span=ne)
    if EIs is not None:
        kw["EI"] = fe.piecewise_EI(spans, EIs)
    if route == "udl":
        c = fe.Cm_udl(spans, xm, load_spans=load_spans, **kw)
    else:
        c = fe.Cm(spans, xm, quad="hermite", **kw)[0]
    return 192 * EIref * c / Lref**4


print("=" * 100)
print("A. Symmetric three-span, closed form vs FE (both FE routes: w_q(x_m)/q0 and "
      "exact integral of influence line)")
print("=" * 100)
Ls = 1.0
for beta, rho in [(1.0, 1.0), (1.5, 1.0), (90 / 55, 1.0), (1.2, 2.0), (1.8, 0.7), (0.8, 1.5)]:
    spans = [Ls, beta * Ls, Ls]
    EIs = [1.0, rho, 1.0]
    print(f" beta={beta:.5f} rho={rho}")
    for xi in [0.25, 0.5, 0.7]:
        cf = th.side_norm(xi, beta, rho)
        check(f"side xi={xi} (udl)", cf, fe_norm(spans, xi * Ls, Ls, 1.0, EIs))
        check(f"side xi={xi} (IL integral)", cf, fe_norm(spans, xi * Ls, Ls, 1.0, EIs, "il"))
    for eta in [0.3, 0.5]:
        cf = th.main_norm(eta, beta, rho)
        check(f"main eta={eta} (udl)", cf,
              fe_norm(spans, Ls + eta * beta * Ls, beta * Ls, rho, EIs))
        check(f"main eta={eta} (IL integral)", cf,
              fe_norm(spans, Ls + eta * beta * Ls, beta * Ls, rho, EIs, "il"))

print("\n Dimensional bridges (uniform EI = 1, metres; 12 elements/span: prismatic Hermite"
      " elements are nodally exact, finer meshes only add round-off):")
for name, spans in [("Cau May 55+90+55", [55, 90, 55]), ("Thai Binh 42+63+42", [42, 63, 42])]:
    b = spans[1] / spans[0]
    check(f"{name} mid side", th.side_norm(0.5, b), fe_norm(spans, spans[0] / 2, spans[0], 1.0))
    check(f"{name} mid main", th.main_norm(0.5, b),
          fe_norm(spans, spans[0] + spans[1] / 2, spans[1], 1.0))

print("\n" + "=" * 100)
print("B. Blind configurations and optimal sensor position")
print("=" * 100)
bc = float(sp.N(th.sp.sqrt(sp.Rational(10, 3)) *
                sp.cos(sp.acos(sp.Rational(2, 5) * sp.sqrt(sp.Rational(6, 5))) / 3), 20))
print(f" beta_crit (mid side, uniform EI) = sqrt(10/3) cos(acos((2/5)sqrt(6/5))/3) = {bc:.15f}")
print(f"   cubic residual 6b^3-15b-4 = {6*bc**3-15*bc-4:.2e}")
check("FE at beta_crit, mid side (exact zero)", 0.0, fe_norm([1, bc, 1], 0.5, 1, 1.0))
for beta in [1.2, 1.7]:
    rc = 3 * beta * (2 * beta**2 - 5) / 4
    if rc > 0:
        check(f"FE at rho_crit={rc:.6f}, beta={beta}", 0.0,
              fe_norm([1, beta, 1], 0.5, 1, 1.0, [1, rc, 1]))
    else:
        print(f"  beta={beta}: rho_crit={rc:.6f} <= 0 -> no blind stiffness ratio")
bw = 2 * np.cos(np.pi / 9)
print(f" side-span blind locus ends (no positive C_m on the whole side span) when mu>=2: beta^3-3beta-1=0 -> beta = 2cos(pi/9) = {bw:.15f}")
check("FE at beta=2cos(pi/9), xi=0.05 (should be < 0)", th.side_norm(0.05, bw),
      fe_norm([1, bw, 1], 0.05, 1, 1.0))
bm = [r for r in np.roots([3, 10, 0, -12]) if abs(r.imag) < 1e-14 and r.real > 0][0].real
print(f" beta_crit (mid main, uniform EI): 3b^3+10b^2-12=0 -> {bm:.15f}")
check("FE at beta_crit, mid main (exact zero)", 0.0, fe_norm([1, bm, 1], 1 + 0.5 * bm, bm, 1.0))

print("\n xi* (side span, uniform EI): root of 8xi^3-(12-3mu)xi^2+(2-mu)=0")
print(f"  {'beta':>8s} {'mu':>12s} {'xi*':>12s} {'Cm(xi*)':>12s} {'Cm(0.5)':>12s} "
      f"{'FE(xi*)':>14s} {'FE slope':>10s}")
for beta in [1.0, 1.2, 1.4, 1.5, 90 / 55, 1.7]:
    xo, vo = th.xi_opt(beta)
    m = 2 * (beta**3 + 1) / (3 * beta + 2)
    f0 = fe_norm([1, beta, 1], xo, 1, 1.0)
    d = 1e-4
    slope = (fe_norm([1, beta, 1], xo + d, 1, 1.0) - fe_norm([1, beta, 1], xo - d, 1, 1.0)) / (2 * d)
    print(f"  {beta:8.5f} {m:12.8f} {xo:12.8f} {vo:12.8f} {th.side_norm(0.5, beta):12.8f} "
          f"{f0:14.10f} {slope:10.1e}")
    if abs(f0 - vo) / abs(vo) > TOL:
        fails.append(f"xi* beta={beta}")

print("\n" + "=" * 100)
print("C. Span-wise contributions (load on one span only) and negative/positive fraction")
print("=" * 100)
xs_, b_, r_ = th.xi, th.beta, th.rho
contrib_side = [sp.lambdify((xs_, b_, r_), th.side_contrib(j)) for j in range(3)]
contrib_main = [sp.lambdify((th.eta, b_, r_), th.main_contrib(j)) for j in range(3)]
print(f"  {'case':34s} {'C1':>10s} {'C2':>10s} {'C3':>10s} {'sum':>10s} {'neg/pos':>9s}")
for name, beta, rho, where, pos in [
        ("two-span-like beta=1 side", 1.0, 1.0, "side", 0.5),
        ("Thai Binh side (beta=1.5)", 1.5, 1.0, "side", 0.5),
        ("Cau May side (beta=1.636)", 90 / 55, 1.0, "side", 0.5),
        ("Thai Binh main (beta=1.5)", 1.5, 1.0, "main", 0.5),
        ("Cau May main (beta=1.636)", 90 / 55, 1.0, "main", 0.5)]:
    spans, EIs = [1, beta, 1], [1, rho, 1]
    cs, fes = [], []
    for j in range(3):
        if where == "side":
            cf = float(contrib_side[j](pos, beta, rho))
            num = fe_norm(spans, pos, 1, 1.0, EIs, load_spans=[j])
        else:
            cf = float(contrib_main[j](pos, beta, rho))
            num = fe_norm(spans, 1 + pos * beta, beta, rho, EIs, load_spans=[j])
        cs.append(cf)
        fes.append(num)
        if abs(num - cf) / abs(cf) > TOL:
            fails.append(f"contrib {name} span {j+1}")
    cs = np.array(cs)
    negpos = cs[cs < 0].sum() / cs[cs > 0].sum()
    print(f"  {name:34s} {cs[0]:10.6f} {cs[1]:10.6f} {cs[2]:10.6f} {cs.sum():10.6f} {negpos:9.5f}"
          f"   max FE rel.err {max(abs(np.array(fes)-cs)/abs(cs)):.1e}")
# closed form of the fraction, mid side span, uniform EI
b = sp.symbols("beta", positive=True)
C = [sp.simplify(th.side_contrib(j).subs({th.xi: sp.Rational(1, 2), th.rho: 1}).subs(th.beta, b))
     for j in range(3)]
print("  mid side-span, uniform EI: C1, C2, C3 =", [sp.factor(c) for c in C])
print("  neg/pos = -C2/(C1+C3) =", sp.factor(sp.simplify(-C[1] / (C[0] + C[2]))))
# sign constancy of the influence line inside each span (justifies span-wise split)
for name, spans, xm in [("Cau May side", [55, 90, 55], 27.5), ("Cau May main", [55, 90, 55], 100.0)]:
    x, w, _ = fe.influence_line(spans, xm, ne_per_span=200)
    edges = np.cumsum([0] + spans)
    sg = []
    for j in range(3):
        mask = (x > edges[j] + 1e-9) & (x < edges[j + 1] - 1e-9)
        sg.append("+" if np.all(w[mask] > 0) else "-" if np.all(w[mask] < 0) else "mixed")
    print(f"  influence-line sign per span, {name}: {sg}")

print("\n" + "=" * 100)
print("D. Asymmetric three spans: general closed form vs FE")
print("=" * 100)
for spans, EIs, xi in [([0.6, 1, 0.8], [1, 1, 1], 0.5), ([0.5, 1, 0.7], [1, 1.4, 0.9], 0.4),
                       ([1.1, 1, 0.4], [1, 0.8, 1.2], 0.6), ([42, 63, 50], [1, 1, 1], 0.5)]:
    cf = th.general_norm(xi, spans, EIs)
    check(f"spans={spans} EI={EIs} xi={xi}", cf,
          fe_norm(spans, xi * spans[0], spans[0], EIs[0], EIs))

print("\n" + "=" * 100)
print("E. Haunched box girder (variable EI): FE convergence vs force method")
print("=" * 100)


def force_method(spans, xm, EI, brk=()):
    """Flexibility method on the released structure (hinges at interior supports)."""
    edges = np.concatenate([[0.0], np.cumsum(spans)])
    L1, L2, L3 = spans

    def loc(x):
        j = min(int(np.searchsorted(edges, x, side="right") - 1), 2)
        return j, x - edges[j], spans[j]

    def M0(x):
        j, s, L = loc(x)
        return 0.5 * s * (L - s)

    def mB(x):
        j, s, L = loc(x)
        return s / L if j == 0 else (1 - s / L if j == 1 else 0.0)

    def mC(x):
        j, s, L = loc(x)
        return s / L if j == 1 else (1 - s / L if j == 2 else 0.0)

    jm, am, Lm_ = loc(xm)

    def mbar(x):
        j, s, L = loc(x)
        if j != jm:
            return 0.0
        return s * (L - am) / L if s <= am else am * (L - s) / L

    pts = sorted(set(list(edges) + [xm] + list(brk)))

    def I(f):
        return sum(quad(lambda x: f(x) / EI(x), a, c, epsabs=0, epsrel=1e-13, limit=200)[0]
                   for a, c in zip(pts[:-1], pts[1:]))
    d = np.array([[I(lambda x: mB(x) ** 2), I(lambda x: mB(x) * mC(x))],
                  [I(lambda x: mB(x) * mC(x)), I(lambda x: mC(x) ** 2)]])
    r = -np.array([I(lambda x: mB(x) * M0(x)), I(lambda x: mC(x) * M0(x))])
    X = np.linalg.solve(d, r)
    return I(lambda x: (M0(x) + X[0] * mB(x) + X[1] * mC(x)) * mbar(x))


def haunch_brk(spans, lc_side):
    e = np.cumsum([0] + spans)
    lc = 0.5 * spans[1] if lc_side is None else lc_side
    return [e[1] - min(lc, spans[0]), e[2] + min(lc, spans[2])]


spans = [55, 90, 55]
HN = fe.haunch_nodes(spans)
for n in (2.0, 3.0):
    EIf = fe.haunch_EI(spans, 2.4, 5.4, n)
    for lab, xm, Lr in [("mid side", 27.5, 55), ("mid main", 100.0, 90)]:
        ref = 192 * force_method(spans, xm, EIf, haunch_brk(spans, None)) / Lr**4
        print(f"  Cau May n={n} {lab}: force method (adaptive quad) {ref:.12f}")
        for kind, ng, nes in [("flex", 8, (5, 10, 20, 40)), ("hermite", 4, (50, 100, 200))]:
            out = [192 * fe.Cm_udl(spans, xm, ne_per_span=ne, EI=EIf, kind=kind, ngauss=ng,
                                   extra_nodes=(xm,) + HN) / Lr**4 for ne in nes]
            errs = [abs(v - ref) / abs(ref) for v in out]
            print(f"    {kind:7s} ne/span={nes}: " +
                  "  ".join(f"{v:.12f} (rel {e:.1e})" for v, e in zip(out, errs)))
            if kind == "flex" and errs[2] > TOL:
                fails.append(f"haunch flex FE n={n} {lab}")
print("  -> flex element at 20 elements/span is used for all haunched results below.")
print("  (piecewise-constant EI check of the FE stiffness routine, ngauss=4, rho=1.7):")
check("  side xi=0.5, beta=1.5, rho=1.7, ngauss=4", th.side_norm(0.5, 1.5, 1.7),
      192 * fe.Cm_udl([1, 1.5, 1], 0.5, ne_per_span=60,
                      EI=fe.piecewise_EI([1, 1.5, 1], [1, 1.7, 1]), ngauss=4))

print("\n" + "=" * 100)
print("F. Haunched results (EI normalised at h_mid; ASSUMPTIONS: I ~ h^n, constant E,")
print("   parabolic soffit with vertex at main mid-span; side-span haunch length Lc_side;")
print("   no constant-depth pier segment; flex FE, 20 el./span, 8-point Gauss)")
print("=" * 100)


def side_scan(spans, EIf, nodes, ne=20):
    """Max over sensor positions in span 1 (coarse grid then golden refinement)."""
    from scipy.optimize import minimize_scalar
    f = lambda x: -fe.Cm_udl(spans, x * spans[0], ne_per_span=ne, EI=EIf, kind="flex",
                             ngauss=8, extra_nodes=(x * spans[0],) + nodes)
    g = np.linspace(0.1, 0.9, 17)
    v = [f(x) for x in g]
    k = int(np.argmin(v))
    r = minimize_scalar(f, bounds=(g[max(k - 1, 0)], g[min(k + 1, 16)]), method="bounded",
                        options=dict(xatol=1e-4))
    return r.x, -192 * r.fun / spans[0] ** 4


def negpos_fe(spans, xm, EIf, nodes, ne=20):
    c = [fe.Cm_udl(spans, xm, load_spans=[j], ne_per_span=ne, EI=EIf, kind="flex", ngauss=8,
                   extra_nodes=(xm,) + nodes) for j in range(3)]
    c = np.array(c)
    return c[c < 0].sum() / c[c > 0].sum()


def haunch_table(name, spans, ratios, lc_list, hm=1.0):
    print(f"\n  {name} {spans}: uniform EI mid side = {th.side_norm(0.5, spans[1]/spans[0]):.4f},"
          f" mid main = {th.main_norm(0.5, spans[1]/spans[0]):.4f}")
    print(f"  {'h_pier/h_mid':>12s} {'n':>4s} {'Lc_side':>8s} {'side xi=.5':>11s} {'shift':>8s}"
          f" {'neg/pos':>8s} {'xi*':>7s} {'Cm(xi*)':>8s} {'main':>8s} {'neg/pos':>8s}")
    rows = []
    for r in ratios:
        for n in (2.0, 2.5, 3.0):
            for lc in lc_list:
                EIf = fe.haunch_EI(spans, hm, r * hm, n, lc)
                nd = fe.haunch_nodes(spans, lc)
                kw = dict(ne_per_span=20, EI=EIf, kind="flex", ngauss=8)
                s = 192 * fe.Cm_udl(spans, spans[0] / 2, extra_nodes=(spans[0] / 2,) + nd,
                                    **kw) / spans[0]**4
                xmm = spans[0] + spans[1] / 2
                m = 192 * fe.Cm_udl(spans, xmm, extra_nodes=(xmm,) + nd, **kw) / spans[1]**4
                nps = negpos_fe(spans, spans[0] / 2, EIf, nd)
                npm = negpos_fe(spans, xmm, EIf, nd)
                xo, vo = side_scan(spans, EIf, nd)
                lcv = lc if lc is not None else 0.5 * spans[1]
                shift = s - th.side_norm(0.5, spans[1] / spans[0])
                print(f"  {r:12.3f} {n:4.1f} {lcv:8.1f} {s:11.4f} {shift:8.4f} {nps:8.4f}"
                      f" {xo:7.3f} {vo:8.4f} {m:8.4f} {npm:8.4f}")
                rows.append((r, n, lcv, s, shift, nps, xo, vo, m, npm))
    return rows


rows_cm = haunch_table("Cau May (h 2.4 m mid-span, 5.4 m pier)", [55, 90, 55],
                       [5.4 / 2.4], [None, 55.0, 30.0], hm=2.4)
rows_tb = haunch_table("Thai Binh (depths NOT available: parametrised by h_pier/h_mid)",
                       [42, 63, 42], [1.0, 1.5, 2.0, 2.25, 2.5, 3.0], [None])

os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"), exist_ok=True)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "haunch_3span.csv"), "w") as fh:
    fh.write("bridge,h_ratio,n,Lc_side_m,side_mid,shift_vs_uniform,side_negpos,xi_star,"
             "Cm_xi_star,main_mid,main_negpos\n")
    for nm, rows in [("CauMay", rows_cm), ("ThaiBinh", rows_tb)]:
        for r in rows:
            fh.write(nm + "," + ",".join(f"{v:.6f}" for v in r) + "\n")

print("\n" + "=" * 100)
print(f"SUMMARY: tolerance {TOL:g}; failures: {len(fails)}" + (f" -> {fails}" if fails else ""))
