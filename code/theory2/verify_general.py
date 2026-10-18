"""Package 1A verification: closed forms of gc_theory.py (all channels) against the FE
of gc_fe.py (element routine of cm_multispan.py), by two FE routes:
  (udl) response under a uniform unit load (consistent nodal loads, exact end forces);
  (il)  exact integral of the FE influence line of the channel (Simpson per element,
        exact because the line is cubic in the load position in a prismatic element),
plus (conv) complete-crossing convoy records integrated exactly, and the haunched /
spring-supported Cau May FE (flex elements) against an independent force-method
solution with adaptive quadrature (gc_force_method.py).

Error measure: all channels are compared through their normalised indicators
  N_w = 192 EI C_w/L^4, N_th = 24 EI C_th/L^3, N_M = 8 C_M/L^2, N_V = 2 C_V/L,
  N_R = R/(q0 L_trib)
which are O(1) (= 1 for the simply supported reference), so the printed error is the
absolute error of N (= error relative to the simply supported reference value); this
handles exact zeros (blind configurations). Tolerance 1e-8.

Run:  python code/theory2/verify_general.py | tee code/theory2/logs/verify_general.log
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gc_theory as th                         # noqa: E402
from gc_fe import Girder, convoy_integral      # noqa: E402
from gc_force_method import ForceMethod3       # noqa: E402
import gc_bridge as br                         # noqa: E402

TOL = 1e-8
n_checks = 0
fails = []
maxerr = {}


def check(group, label, cf, num):
    global n_checks
    n_checks += 1
    err = abs(num - cf)
    ok = err <= TOL
    maxerr[group] = max(maxerr.get(group, 0.0), err)
    if not ok:
        fails.append(f"{group}: {label}")
    print(f"  {label:58s} closed={cf: .12f} FE={num: .12f} err={err:.1e} "
          f"{'OK' if ok else 'FAIL'}")


def norms(L, EI):
    return dict(w=192 * EI / L**4, theta=24 * EI / L**3, M=8 / L**2, V=2 / L)


def run_structure(group, spl, positions, ne=24):
    """spl: list (L, EI, ml, mr); positions: list of (span j, xi)."""
    spans = [s[0] for s in spl]
    x0 = np.concatenate([[0.0], np.cumsum(spans)])
    EIs = [s[1] for s in spl]
    edges = x0
    EIf = lambda x: EIs[min(int(np.searchsorted(edges, x, side="right") - 1), len(spl) - 1)]
    xs = [x0[j] + xi * spans[j] for j, xi in positions]
    g = Girder(spans, EI=EIf, ne_per_span=ne, extra_nodes=tuple(xs))
    for (j, xi), xm in zip(positions, xs):
        L, EI, ml, mr = spl[j]
        cf = th.at(spl, j, xi)
        nz = norms(L, EI)
        side = "right" if xi == 0 else "left"
        fe = g.channels_udl(xm, side=side)
        for ch in ("w", "theta", "M", "V"):
            check(group, f"span{j+1} xi={xi:.6g} {ch:5s} (udl)", cf[ch] * nz[ch], fe[ch] * nz[ch])
        for ch in ("theta", "M", "V"):
            Iil = g.il_integral(xm, ch, side=side)
            check(group, f"span{j+1} xi={xi:.6g} {ch:5s} (il)", cf[ch] * nz[ch], Iil * nz[ch])
    Rcf = th.reactions(spl)
    trib = np.array([spans[0] / 2] + [(spans[i - 1] + spans[i]) / 2 for i in range(1, len(spans))]
                    + [spans[-1] / 2])
    Rfe = g.channels_udl(xs[0])["R"]
    for i in range(len(Rcf)):
        check(group, f"reaction R{i} (udl)", Rcf[i] / trib[i], Rfe[i] / trib[i])
        Iil = g.il_integral(xs[0], "R", sup_index=i)
        check(group, f"reaction R{i} (il)", Rcf[i] / trib[i], Iil / trib[i])
    return g


print("=" * 110)
print("A. Two-span beam, all channels, closed form vs FE (udl and influence-line routes)")
print("=" * 110)
for rho_L, rho_EI in [(1.0, 1.0), (0.5, 1.0), (1.3, 1.0), (1.45743, 1.0), (2.0, 1.0),
                      (1.6, 2.14), (1.0, 3.0), (2.5, 1.0)]:
    print(f" rho_L={rho_L} rho_EI={rho_EI}  mu={th.mu_two(rho_L, rho_EI):.10f}")
    run_structure("A two-span", th.two_span(rho_L, rho_EI),
                  [(0, 0.0), (0, 0.25), (0, 0.5), (0, 0.75), (1, 0.4), (1, 0.8)])

print("=" * 110)
print("B. Symmetric three-span beam, all channels")
print("=" * 110)
for beta, rho in [(1.0, 1.0), (90 / 55, 1.0), (1.2, 2.0), (1.8, 0.7), (np.sqrt(1.5), 0.5),
                  (2.0, 1.0)]:
    print(f" beta={beta:.6f} rho={rho}  mu={th.mu_three(beta, rho):.10f}")
    run_structure("B three-span", th.three_span_sym(beta, rho),
                  [(0, 0.0), (0, 0.4), (0, 0.5), (0, 0.8), (1, 0.0), (1, 0.25), (1, 0.5)])

print("=" * 110)
print("C. Asymmetric four-span (three-moment equation) and asymmetric three-span")
print("=" * 110)
for spans, EIs in [([30, 45, 50, 35], [1.0, 1.4, 1.6, 1.1]), ([40, 70, 25], [1, 2.5, 0.8])]:
    print(f" spans={spans} EI={EIs}")
    run_structure("C n-span", th.three_moment(spans, EIs),
                  [(0, 0.3), (1, 0.5), (2, 0.65), (len(spans) - 1, 0.5)], ne=30)

print("=" * 110)
print("D. Zeros of the uniform-load moment diagram (strain blind points), xi = s/L")
print("=" * 110)
for lab, spl in [("2-span rho_L=1", th.two_span(1.0)), ("2-span rho_L=1.3", th.two_span(1.3)),
                 ("2-span rho_L=0.7, rho_EI=2", th.two_span(0.7, 2.0)),
                 ("3-span beta=1", th.three_span_sym(1.0)),
                 ("3-span beta=90/55", th.three_span_sym(90 / 55)),
                 ("3-span beta=1.4, rho=1.8", th.three_span_sym(1.4, 1.8)),
                 ("4-span", th.three_moment([30, 45, 50, 35], [1.0, 1.4, 1.6, 1.1]))]:
    spans = [s[0] for s in spl]
    x0 = np.concatenate([[0.0], np.cumsum(spans)])
    EIs = [s[1] for s in spl]
    EIf = lambda x: EIs[min(int(np.searchsorted(x0, x, side="right") - 1), len(spl) - 1)]
    g = Girder(spans, EI=EIf, ne_per_span=37)          # zeros generally not at nodes
    zfe = g.moment_zeros()
    zcf = []
    for j, (L, EI, ml, mr) in enumerate(spl):
        zcf += [x0[j] + z * L for z in th.moment_zeros(ml, mr)]
    print(f" {lab}: {len(zcf)} closed-form zeros, {len(zfe)} FE zeros")
    if len(zcf) != len(zfe):
        fails.append(f"D count {lab}")
    for zc, zf in zip(zcf, zfe):
        j = int(np.searchsorted(x0, zc) - 1)
        check("D moment zeros", f"{lab}: zero in span {j+1} (xi)", (zc - x0[j]) / spans[j],
              (zf - x0[j]) / spans[j])

print("=" * 110)
print("E. Closed-form blind configurations of non-deflection channels (FE indicator = 0)")
print("=" * 110)
R = th.roots_summary()
for k_, v in R.items():
    print(f"  {k_:40s} = {v:.9f}")
cases = [
    ("2-span end reaction R_A, rho_L=(1+sqrt13)/2", th.two_span(R["2span_endR_blind_rhoL"]), "R0", None),
    ("2-span end rotation, rho_L=golden ratio", th.two_span(R["2span_endrot_blind_rhoL"]), "theta", (0, 0.0)),
    ("2-span rotation at B, rho_L=1, rho_EI=3", th.two_span(1.0, 3.0), "theta", (0, 1.0)),
    ("3-span rotation at B, beta=sqrt(3/2), rho=0.5", th.three_span_sym(R["3span_Brot_blind_beta"], 0.5), "theta", (0, 1.0)),
    ("3-span rotation at B, beta=sqrt(3/2), rho=3", th.three_span_sym(R["3span_Brot_blind_beta"], 3.0), "theta", (0, 1.0)),
    ("3-span end rotation, beta=2cos(pi/9)", th.three_span_sym(R["3span_endrot_blind_beta"]), "theta", (0, 0.0)),
    ("3-span end reaction, beta^3-6beta-3=0", th.three_span_sym(R["3span_endR_blind_beta"]), "R0", None),
    ("3-span mid-main moment, beta^3+2beta^2-2=0", th.three_span_sym(R["3span_midmain_strain_blind_beta"]), "M", (1, 0.5)),
    ("3-span mid-main shear (symmetry), beta=1.6", th.three_span_sym(1.6, 1.3), "V", (1, 0.5)),
    ("3-span mid-main rotation (symmetry), beta=1.6", th.three_span_sym(1.6, 1.3), "theta", (1, 0.5)),
]
for lab, spl, ch, pos in cases:
    spans = [s[0] for s in spl]
    x0 = np.concatenate([[0.0], np.cumsum(spans)])
    EIs = [s[1] for s in spl]
    EIf = lambda x: EIs[min(int(np.searchsorted(x0, x, side="right") - 1), len(spl) - 1)]
    if ch == "R0":
        g = Girder(spans, EI=EIf, ne_per_span=20)
        check("E blind configs", lab + " N_R", 0.0, g.channels_udl(0.0, side="right")["R"][0] / (spans[0] / 2))
        continue
    j, xi = pos
    xm = x0[j] + xi * spans[j]
    g = Girder(spans, EI=EIf, ne_per_span=20, extra_nodes=(xm,))
    L, EI = spans[j], EIs[j]
    val = g.channels_udl(xm, side="right" if xi == 0 else "left")[ch] * norms(L, EI)[ch]
    check("E blind configs", lab + f" N_{ch}", 0.0, val)
spl = th.three_span_sym(1.0)
g = Girder([1, 1, 1], ne_per_span=20)
check("E blind configs", "3-span beta=1: mid-main N_M = 0.2 (band edge)", 0.2,
      g.channels_udl(1.5)["M"] * 8)

print("=" * 110)
print("F. Theorem: complete-crossing convoy integral = P_tot * C_r (exact quadrature);")
print("   piecewise-prismatic girders, incl. elastic rotational springs at the piers")
print("=" * 110)
P = np.array([50.0, 100.0, 100.0, 50.0, 100.0, 100.0])      # two 3-axle trucks
a = np.array([0.0, 3.6, 4.95, 10.95, 14.55, 15.9])          # offsets (m)
for lab, spans, EIs, k in [("2-span 30+39 m, EI2/EI1=1.5", [30.0, 39.0], [1.0, 1.5], 0.0),
                           ("3-span 30+48+30 m, pier springs k = 60 EI_s/L_s", [30.0, 48.0, 30.0], [1.0, 1.8, 1.0], 2.0),
                           ("3-span 30+48+30 m, fixed piers", [30.0, 48.0, 30.0], [1.0, 1.8, 1.0], np.inf)]:
    x0 = np.concatenate([[0.0], np.cumsum(spans)])
    EIf = lambda x, EIs=EIs, x0=x0: EIs[min(int(np.searchsorted(x0, x, side="right") - 1), len(EIs) - 1)]
    h = 0.15
    g = Girder(spans, EI=EIf, ne_per_span=0, h_max=h, k_rot=k)
    assert np.allclose(np.diff(g.x), h)
    print(f" {lab}")
    for xm, ch, si in [(12.0, "w", None), (12.0, "theta", None), (12.0, "M", None),
                       (12.0, "V", None), (x0[1], "M", None), (0.0, "R", 0), (0.0, "R", 1)]:
        side = "right" if xm == 0 else "left"
        I, rec = convoy_integral(g, xm, ch, P, a, side=side, sup_index=si)
        F, qe = g.udl_load(1.0)
        if ch == "R":
            Cr = g.channels_udl(x0[1])["R"][si]
        else:
            Cr = g.channels_udl(xm, side=side)[ch]
        scale = abs(P.sum() * Cr) if abs(Cr) > 0 else 1.0
        err = abs(I - P.sum() * Cr) / scale
        global_ok = err <= TOL
        n_checks += 1  # noqa
        maxerr["F theorem"] = max(maxerr.get("F theorem", 0), err)
        if not global_ok:
            fails.append(f"F {lab} {ch}")
        # truncated record (stop when the leader leaves the girder): shows the error
        ne = g.n - 1
        It = np.sum(h / 6 * (rec[:ne, 0] + 4 * rec[:ne, 1] + rec[:ne, 2]))
        print(f"  x_m={xm:6.2f} {ch:5s}{'' if si is None else si}  int={I: .10e}  P_tot*C_r={P.sum()*Cr: .10e}"
              f"  relerr={err:.1e} {'OK' if global_ok else 'FAIL'}   truncated-at-L error {abs(It/(P.sum()*Cr)-1)*100:6.2f} %")

print("=" * 110)
print("G. Cau May haunched girder (flex elements, h = 0.5 m) vs independent force method")
print("   (quadrature); indicators normalised by the prismatic references of each span")
print("=" * 110)
for name, c in br.cases().items():
    g = Girder(br.SPANS, EI=c["EI"], ne_per_span=0, h_max=0.5, kind="flex", ngauss=8,
               k_rot=c["k"], extra_nodes=tuple(br.GAUGES.values()) + (25.0, 70.0))
    fm = ForceMethod3(br.SPANS, c["EI"], k=c["k"], breaks=br.BREAKS)
    print(f" {name}")
    for xm in (22.0, 25.0, 27.5, 70.0, 100.0):
        L = 55.0 if xm < 55 else 90.0
        o = g.channels_udl(xm)
        check("G haunch FE vs force method", f"x={xm:5.1f} N_M", 8 * fm.M(xm) / L**2, 8 * o["M"] / L**2)
        check("G haunch FE vs force method", f"x={xm:5.1f} N_V", 2 * fm.V(xm) / L, 2 * o["V"] / L)
        check("G haunch FE vs force method", f"x={xm:5.1f} N_th (EI_mid)", 24 * br.EI_MID * fm.theta(xm) / L**3,
              24 * br.EI_MID * o["theta"] / L**3)
    for side, xs in (("left", 55.0), ("right", 55.0)):
        o = g.channels_udl(xs, side=side)
        L = 55.0 if side == "left" else 90.0
        Mfm = fm.ends[0][1] if side == "left" else fm.ends[1][0]
        check("G haunch FE vs force method", f"pier T6 girder moment ({side}) N_M", 8 * Mfm / L**2, 8 * o["M"] / L**2)
    Rfe = g.channels_udl(100.0)["R"]
    Rfm = fm.reactions()
    for i, tr in enumerate((27.5, 72.5, 72.5, 27.5)):
        check("G haunch FE vs force method", f"reaction R{i} N_R", Rfm[i] / tr, Rfe[i] / tr)
    zf, zm = g.moment_zeros(), fm.zeros()
    if len(zf) != len(zm):
        fails.append(f"G zero count {name}")
    for a_, b_ in zip(zm, zf):
        L = 55.0 if (a_ < 55 or a_ > 145) else 90.0
        check("G haunch FE vs force method", f"moment zero at {a_:8.4f} m (in span lengths)", a_ / L, b_ / L)

print("=" * 110)
print(f"SUMMARY: {n_checks} checks, tolerance {TOL:.0e}, failures: {len(fails)}")
for k_, v in maxerr.items():
    print(f"  max error  {k_:32s} {v:.1e}")
for f in fails:
    print("  FAIL:", f)
print("ALL PASS" if not fails else "SOME CHECKS FAILED")
