"""Package 1A - numbers for docs/pkg1/1A_general_channels.md.

Tables T1-T3: closed forms (gc_theory.py), prismatic beams.
Table  T4  : Cau May haunched girder, FE (gc_fe.py, flex elements, h = 0.5 m) for the
             WP3 model variants (gc_bridge.py): strain blind points / bands versus the
             deflection indicators of the installed gauges.
Writes code/theory2/results/gc_*.csv and prints everything (log).

Run:  python code/theory2/gc_results.py | tee code/theory2/logs/gc_results.log
"""
import os
import sys
import csv
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gc_theory as th                 # noqa: E402
from gc_fe import Girder               # noqa: E402
import gc_bridge as br                 # noqa: E402

RES = os.path.join(HERE, "results")
os.makedirs(RES, exist_ok=True)


def wcsv(name, header, rows):
    with open(os.path.join(RES, name), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)


def f(v, n=4):
    return "-" if v is None else f"{v:.{n}f}"


# ------------------------------------------------------------------ T1 two-span
print("=" * 100)
print("T1. Two-span beam (closed form). Span 1 instrumented, xi from the end support A.")
print("    N_M = 8M_q/(q0 L1^2); strain zero xi0 = 1 - mu/4; band |N_M| < 0.2.")
print("=" * 100)
hdr = ["rho_L", "rho_EI", "mu", "xi0_span1", "dist_from_B_span1_L1", "zero_span2_from_C_L2",
       "band_span1_lo", "band_span1_hi", "NM_mid1", "NM_at_B", "NR_A", "NR_C", "Nth_A",
       "Nth_B", "xi_V0", "Nw_mid1"]
rows = []
for rL, rE in [(0.5, 1), (0.8, 1), (1.0, 1), (1.2, 1), (1.45743, 1), ((1 + 5**.5) / 2, 1),
               (2.0, 1), ((1 + 13**.5) / 2, 1), (1.0, 0.5), (1.0, 2.0), (1.6, 2.14)]:
    mu = th.mu_two(rL, rE)
    spl = th.two_span(rL, rE)
    z1 = th.moment_zeros(0, mu)
    z2 = th.moment_zeros(mu / rL**2, 0)        # local xi from B in span 2
    be = th.band_edges(0, mu)
    # band around the interior zero: the pair of edges bracketing xi0
    lo = max([b for b in be if z1 and b < z1[-1]], default=None)
    hi = min([b for b in be if z1 and b > z1[-1]], default=None)
    R = th.reactions(spl)
    row = [rL, rE, mu, z1[-1] if z1 else None, mu / 4, (1 - z2[0]) if z2 else None,
           lo, hi, th.N_M(0.5, 0, mu), -mu, 2 * R[0] / 1.0, 2 * R[2] / rL,
           th.N_th(0.0, 0, mu), th.N_th(1.0, 0, mu), (4 - mu) / 8, th.N_w(0.5, 0, mu)]
    rows.append(row)
    print(" rho_L={:.5f} rho_EI={:<4} mu={:.6f} xi0={} (B-dist {:.4f} L1) span-2 zero {} L2 from C;"
          " band [{}, {}]; N_M(mid)={:.4f}, N_M(B)={:.4f}; N_R(A)={:.4f} N_R(C)={:.4f};"
          " N_th(A)={:.4f} N_th(B)={:.4f}; V=0 at xi={:.4f}; N_w(mid)={:.4f}".format(
              rL, rE, mu, f(row[3]), mu / 4, f(row[5]), f(lo), f(hi), row[8], row[9], row[10],
              row[11], row[12], row[13], row[14], row[15]))
wcsv("gc_T1_two_span.csv", hdr, rows)

# ------------------------------------------------------------------ T2 three-span
print("=" * 100)
print("T2. Symmetric three-span beam, uniform EI (closed form). Side: xi from abutment;")
print("    main: eta from the pier; main normalisation by L_m.")
print("=" * 100)
hdr = ["beta", "mu", "m_main", "xi0_side", "band_side_lo", "band_side_hi", "eta0_main",
       "band_main_lo", "band_main_hi", "NM_mid_side", "NM_mid_main", "NM_pier_side",
       "NM_pier_main", "Nth_end", "Nth_B_side", "NR_end", "Nw_mid_side", "Nw_mid_main"]
rows = []
for beta in [1.0, 1.2, np.sqrt(1.5), 1.4, 1.5, 90 / 55, 1.700594, 1.8, 2 * np.cos(np.pi / 9),
             2.0, 2.5]:
    mu = th.mu_three(beta)
    m = mu / beta**2
    zs = th.moment_zeros(0, mu)
    zm = th.moment_zeros(m, m)
    bs = th.band_edges(0, mu)
    bm = th.band_edges(m, m)
    lo_s = max([b for b in bs if zs and b < zs[-1]], default=None)
    hi_s = min([b for b in bs if zs and b > zs[-1]], default=None)
    lo_m = max([b for b in bm if zm and b < zm[0]], default=0.0 if zm else None)
    hi_m = min([b for b in bm if zm and b > zm[0]], default=None)
    R = th.reactions(th.three_span_sym(beta))
    row = [beta, mu, m, zs[-1] if zs else None, lo_s, hi_s, zm[0] if zm else None, lo_m, hi_m,
           th.N_M(0.5, 0, mu), th.N_M(0.5, m, m), -mu, -m, th.N_th(0, 0, mu), th.N_th(1, 0, mu),
           2 * R[0], th.N_w(0.5, 0, mu), th.N_w(0.5, m, m)]
    rows.append(row)
    print(" beta={:.6f} mu={:.5f} m={:.5f} | side zero xi0={} band [{}, {}] | main zero eta0={} "
          "band [{}, {}] | N_M mid side {:.4f}, mid main {:.4f}, pier {:.4f}/{:.4f} | N_th end "
          "{:.4f}, at B {:.4f} | N_R end {:.4f} | N_w mid side {:.4f}, mid main {:.4f}".format(
              beta, mu, m, f(row[3]), f(lo_s), f(hi_s), f(row[6]), f(lo_m), f(hi_m), row[9],
              row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17]))
wcsv("gc_T2_three_span.csv", hdr, rows)

# ------------------------------------------------------------------ T3 near pier
print("=" * 100)
print("T3. Strain indicator N_M at a distance d from the interior support (prismatic)")
print("=" * 100)
ds = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
hdr = ["case"] + [f"d={d:.2f}L" for d in ds]
rows = []
mu2 = th.mu_two(1.0)
for lab, ml, mr, side in [("2-span equal, span 1", 0, mu2, "r"),
                          ("3-span equal, side span", 0, th.mu_three(1.0), "r"),
                          ("3-span equal, main span", th.mu_three(1.0), th.mu_three(1.0), "l"),
                          ("3-span beta=1.636, side span", 0, th.mu_three(90 / 55), "r"),
                          ("3-span beta=1.636, main span", th.mu_three(90 / 55) / (90 / 55)**2,
                           th.mu_three(90 / 55) / (90 / 55)**2, "l")]:
    vals = [th.N_M(1 - d if side == "r" else d, ml, mr) for d in ds]
    rows.append([lab] + vals)
    print(f" {lab:32s} " + " ".join(f"{v:7.3f}" for v in vals))
wcsv("gc_T3_near_pier.csv", hdr, rows)

# cancellation ratio of the strain channel, prismatic (FE influence line)
print("\n Cancellation ratio R_eps = C/A+ of the strain (moment) influence line, prismatic:")
for lab, spans, xm in [("2-span equal, mid span 1", [1.0, 1.0], 0.5),
                       ("2-span equal, xi = 0.4", [1.0, 1.0], 0.4),
                       ("3-span equal, mid side", [1.0, 1.0, 1.0], 0.5),
                       ("3-span equal, mid main", [1.0, 1.0, 1.0], 1.5),
                       ("3-span beta=1.636, 0.4 side", [1.0, 90 / 55, 1.0], 0.4),
                       ("3-span beta=1.636, mid side", [1.0, 90 / 55, 1.0], 0.5),
                       ("3-span beta=1.636, mid main", [1.0, 90 / 55, 1.0], 1 + 45 / 55)]:
    g = Girder(spans, ne_per_span=60, extra_nodes=(xm,))
    Ap, C = g.il_pos_area(xm, "M")
    Apw, Cw = g.il_pos_area(xm, "w")
    print(f"  {lab:30s} R_eps = {C/Ap:7.4f}   (deflection R_w = {Cw/Apw:7.4f})")

# ------------------------------------------------------------------ T4 Cau May
print("=" * 100)
print("T4. Cau May 55+90+55 m: uniform-load moment zeros (strain blind points), strain")
print("    indicators and deflection indicators at the gauges. FE flex elements h = 0.5 m.")
print("    N_M = 8M_q/(q0 L^2) (no reference stiffness); N_w = 192 EI_mid C_w/L^4;")
print("    N_eps,abs = N_M (EI_mid/EI(x)) (c(x)/c_mid), assumption c ~ h (bottom fibre).")
print("=" * 100)
h = br.depth()
n_exp = br.exponent()
print(f" I ~ h^n with n = {n_exp:.4f}")
gx = tuple(br.GAUGES.values())
rows = []
for name, c in br.cases().items():
    g = Girder(br.SPANS, EI=c["EI"], ne_per_span=0, h_max=0.5, kind="flex", ngauss=8,
               k_rot=c["k"], extra_nodes=gx)
    zs = g.moment_zeros()
    X, M, V, u = g.moment_diagram(nsub=1)
    Lx = np.where((X < 55) | (X > 145), 55.0, 90.0)
    NM = 8 * M / Lx**2
    haunched = name.startswith("haunched")
    # strain sensitivity of the section relative to the mid-span section:
    # (c/EI)(x) / (c/EI)_mid, assumption c ~ h for the haunched girder, c const if prismatic
    sens = (lambda xx: (br.EI_MID * c["alpha"] / c["EI"](xx)) * (h(xx) / br.H_MID)) if haunched \
        else (lambda xx: 1.0)
    # blind band |N_M| < 0.2 in the left half (symmetry)
    blind = np.abs(NM) < 0.2
    edges = []
    for i in range(1, len(X)):
        if blind[i] != blind[i - 1] and X[i] <= 100.0 + 1e-9:
            edges.append(0.5 * (X[i] + X[i - 1]))
    print(f"\n {name}")
    print(f"   moment zeros (m from T5): " + ", ".join(f"{z:.3f}" for z in zs))
    zl = zs[zs < 100]
    print(f"   side-span zero: {zl[0]:.3f} m from abutment = {zl[0]/55:.4f} L_s "
          f"({55-zl[0]:.3f} m from pier); main-span zero {zl[1]-55:.3f} m from pier = "
          f"{(zl[1]-55)/90:.4f} L_m")
    print(f"   |N_M| < 0.2 band edges in x <= 100 m (0.5 m grid): "
          + ", ".join(f"{e:.2f}" for e in edges))
    for gl, xm in br.GAUGES.items():
        L = 55.0 if xm > 145 or xm < 55 else 90.0
        o = g.channels_udl(xm)
        NMg = 8 * o["M"] / L**2
        Nwg = 192 * br.EI_MID * o["w"] / L**4
        ratio = sens(xm)
        Ap, Cm = g.il_pos_area(xm, "M", nsub=4)
        Apw, Cw = g.il_pos_area(xm, "w", nsub=4)
        print(f"   {gl:24s} N_M={NMg: .4f}  R_eps={Cm/Ap: .3f} | N_w={Nwg: .4f} R_w={Cw/Apw: .3f} "
              f"| N_eps,abs={NMg*ratio: .4f}")
        rows.append([name, gl, xm, NMg, Cm / Ap, Nwg, Cw / Apw, NMg * ratio])
    for side in ("left", "right"):
        o = g.channels_udl(55.0, side=side)
        L = 55.0 if side == "left" else 90.0
        ratio = sens(55.0)
        print(f"   pier T6 face ({side:5s}) N_M={8*o['M']/L**2: .4f}  N_eps,abs={8*o['M']/L**2*ratio: .4f}"
              f"  (strain at pier relative to mid-span section: x{ratio:.3f})")
    for d in (5.0, 10.0, 15.0, 20.0):
        for xm, lab in ((55 - d, "side"), (55 + d, "main")):
            gg = Girder(br.SPANS, EI=c["EI"], ne_per_span=0, h_max=0.5, kind="flex", ngauss=8,
                        k_rot=c["k"])
            L = 55.0 if lab == "side" else 90.0
            o = gg.channels_udl(xm)
            ratio = sens(xm)
            rows.append([name, f"{d:.0f} m from T6 ({lab})", xm, 8 * o["M"] / L**2, None,
                         192 * br.EI_MID * o["w"] / L**4, None, 8 * o["M"] / L**2 * ratio])
    print("   N_M at d m from pier T6:  " + "  ".join(
        f"d={r[2] if False else r[1].split(' m')[0]}m {r[1].split('(')[1][:-1]}: {r[3]: .3f}"
        for r in rows[-8:]))
wcsv("gc_T4_caumay.csv", ["case", "location", "x_m", "N_M", "R_eps", "N_w_EImid", "R_w",
                          "N_eps_abs_c_prop_h"], rows)
print("\nDone; CSV files in code/theory2/results/")
