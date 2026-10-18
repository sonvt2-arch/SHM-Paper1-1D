"""Package 1B - theory checks and tables (no Monte Carlo).

T1  single-sensor reduction: GLS with k = 1 equals P = I/C, variance
    (sig^2 dx (Lrec - dx/2) + eps^2 Lrec^2)/C^2; manuscript O_m reproduced.
T2  multi-channel price of invariance O_k (white noise) for example layouts.
T3  offset-immune estimator (sum w_j = 0 within a channel type): weights,
    noise cost and gain against the single best sensor and against GLS.
T4  structure-aware invariant weights: when eta is KNOWN, non-uniform weights
    g with (g * eta)(s) = 1 for all entry shifts s in [0, S] exist; minimum-
    variance element, its offset-immune variant, the Cauchy-Schwarz lower bound
    S^2/||Phi||^2 and the off-grid invariance defect.  Uniform weighting is the
    only weight invariant for every influence line (structure-agnostic).
Run: python3 code/theory2/multisensor_theory.py  -> logs/multisensor_theory.log
"""
import csv
import numpy as np
import multisensor_core as mc

log = mc.Logger("multisensor_theory.log")
PM = mc.prismatic_models()
CM = mc.caumay_models()
ALL = {**PM, **CM}

# ------------------------------------------------------------------- T1
log("=" * 78)
log("T1  single-sensor reduction and the manuscript's O_m")
m = PM["2S-eq"]
Lr = mc.lrec(m)
c = m.C("d", 15.0)
for sig, eps in [(0.01, 0.0), (0.01, 0.1), (0.02, 0.5)]:
    S = mc.noise_cov(["d"], [sig], [eps], 0.0, Lr)
    w, v = mc.gls([c], S)
    vt = (sig**2 * mc.DX * (Lr - mc.DX / 2) + eps**2 * Lr**2) / c**2
    log(f"  2S-eq mid-span, sig={sig}, eps={eps}: w = {w[0]:.6f} (1/C = {1/c:.6f}); "
        f"Var GLS = {v:.6e}, closed form = {vt:.6e} kN^2")
eta = m.il_defl(15.0)
log(f"  O_m (Eq. 15, L_tot = 60 m) = {mc.O_k([c], [eta], [1.0], 60.0):.4f} "
    f"(manuscript 2*sqrt(44765)/1279 = {2*np.sqrt(44765)/1279:.4f})")
log(f"  MF white-noise variance / uniform variance, Lrec = 60 m: "
    f"{mc.matched_filter_var([eta], [1.0], [0.0], 0.0, ['d']) / (mc.DX*(60-mc.DX/2)/c**2):.4f}"
    " (= O_m^2 up to the trapezoid end weights)")

# ------------------------------------------------------------------- T2
log("=" * 78)
log("T2  multi-channel price of invariance O_k (white noise, Lrec = beam length, "
    "single axle; equal sig per type: sig_d = 0.01 mm, sig_s = 1 ue)")
rows = []
layouts = {
    "2S-eq": [[("d", 15.0)], [("d", 12.6)], [("d", 12.6), ("d", 47.4)],
              [("d", 12.6), ("d", 30.0)], [("s", 30.0)], [("d", 12.6), ("s", 30.0)],
              [("d", 12.6), ("s", 12.6), ("s", 30.0)]],
    "3S-b2.0": [[("d", 60.0)], [("d", 98.5)], [("d", 60.0), ("d", 98.5)],
                [("d", 60.0), ("d", 21.5), ("d", 98.5)]],
    "CM-A": [[("d", 100.0)], [("d", 178.0)], [("d", 100.0), ("d", 155.0)],
             [("d", 100.0), ("d", 178.0)]],
    "CM-B": [[("d", 100.0)], [("d", 178.0)], [("d", 100.0), ("d", 148.9)]],
}
for key, lays in layouts.items():
    mm = ALL[key]
    for lay in lays:
        types = [t for t, _ in lay]
        C = [mm.C(t, x) for t, x in lay]
        ils = [mm.il(t, x) for t, x in lay]
        sig = [0.01 if t == "d" else 1.0 for t in types]
        Ok = mc.O_k(C, ils, sig, mm.L)
        Oj = [mc.O_k([cc], [ii], [1.0], mm.L) for cc, ii in zip(C, ils)]
        lab = "+".join(f"{t}@{x:g}" for t, x in lay)
        log(f"  {key:8s} {lab:28s} C = {np.round(C, 5).tolist()}  O_j = "
            f"{np.round(Oj, 4).tolist()}  O_k = {Ok:.4f}")
        rows.append([key, lab, ";".join(f"{v:.6g}" for v in C),
                     ";".join(f"{v:.4f}" for v in Oj), f"{Ok:.4f}"])
with open(f"{mc.RES}/T2_Ok.csv", "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["model", "layout", "C_j", "O_j", "O_k"])
    wr.writerows(rows)
log("  O_k^2 is the C^2/sig^2-weighted mean of the O_j^2: combining channels never")
log("  raises efficiency relative to the multi-channel matched filter, it lowers variance.")

# offsets in the MF benchmark: the MF can estimate a constant offset jointly
log("  Matched filter with random offsets (one axle, known position), 2S-eq d@12.6, "
    "sig = 0.01 mm, Lrec = 80 m:")
mm = PM["2S-eq"]
Lr = mc.lrec(mm)
ilr = np.interp(np.arange(0, Lr + 1e-9, mc.DX), mm.x, mm.il_defl(12.6), right=0.0)
cc = mm.C("d", 12.6)
for eps in (0.0, 0.02, 0.1, 0.5):
    vmf = mc.matched_filter_var([ilr], [0.01], [eps], 0.0, ["d"])
    vu = mc.gls([cc], mc.noise_cov(["d"], [0.01], [eps], 0.0, Lr))[1]
    log(f"    eps = {eps:4.2f} mm: std MF = {np.sqrt(vmf):8.3f} kN, std integral = "
        f"{np.sqrt(vu):8.3f} kN, ratio (O incl. offset) = {np.sqrt(vmf/vu):.4f}")

# ------------------------------------------------------------------- T3
log("=" * 78)
log("T3  offset-immune estimator: w'C = 1, sum w_j = 0 (deflection channels)")
log("    two channels: w = (1, -1)/(C1 - C2); Var = (s1^2 + s2^2) sig_I^2/(C1-C2)^2 "
    "+ independent-offset part")
rows = []
for key, mm in ALL.items():
    Lr = mc.lrec(mm)
    imax, imin = int(np.argmax(mm.Cd)), int(np.argmin(mm.Cd))
    cmax, cmin = mm.Cd[imax], mm.Cd[imin]
    P = mc.P_CM if key.startswith("CM") else mc.P_REF
    for sig in (0.005, 0.01, 0.02):
        for eps in (0.02, 0.1, 0.5):
            for rho in (0.9, 1.0):
                S1 = mc.noise_cov(["d"], [sig], [eps], rho, Lr)
                v1 = mc.gls([cmax], S1)[1]
                S2 = mc.noise_cov(["d", "d"], [sig] * 2, [eps] * 2, rho, Lr)
                wi, vi = mc.immune([cmax, cmin], S2, ["d", "d"])
                wg, vg = mc.gls([cmax, cmin], S2)
                vr = mc.immune([cmax, 0.0], S2, ["d", "d"])[1]   # reference at a support
                rows.append([key, sig, eps, rho, f"{mm.x[imax]:.1f}", f"{mm.x[imin]:.1f}",
                             f"{cmax:.6g}", f"{cmin:.6g}",
                             f"{100*np.sqrt(v1)/P:.4f}", f"{100*np.sqrt(vg)/P:.4f}",
                             f"{100*np.sqrt(vi)/P:.4f}", f"{100*np.sqrt(vr)/P:.4f}",
                             f"{wi[0]:.6g}", f"{wi[1]:.6g}"])
with open(f"{mc.RES}/T3_immune.csv", "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["model", "sig_mm", "eps_mm", "rho", "x_Cmax", "x_Cmin", "Cmax", "Cmin",
                 "std_single_pct", "std_GLS2_pct", "std_immune2_pct",
                 "std_immune_ref_support_pct", "w1_immune", "w2_immune"])
    wr.writerows(rows)
for r in rows:
    if r[1] == 0.01 and r[2] in (0.1, 0.5):
        log(f"  {r[0]:8s} sig={r[1]} eps={r[2]} rho={r[3]}: Cmax {r[6]} @ {r[4]} m, "
            f"Cmin {r[7]} @ {r[5]} m | std % single {r[8]}, GLS-2 {r[9]}, immune-2 "
            f"{r[10]}, immune with support reference {r[11]}")
log("  Noise-only cost of immunity (rho = 1, eps irrelevant), two channels at Cmax, Cmin:")
for key, mm in ALL.items():
    cmax, cmin = mm.Cd.max(), mm.Cd.min()
    f_imm = 2 * cmax**2 / (cmax - cmin)**2
    log(f"    {key:8s} Var(immune)/Var(single, white noise only) = 2 Cmax^2/(Cmax-Cmin)^2 "
        f"= {f_imm:.4f}  (Cmin/Cmax = {cmin/cmax:+.4f})")

# ------------------------------------------------------------------- T4
log("=" * 78)
log("T4  structure-aware invariant weights (eta known), single deflection channel,")
log("    2S-eq at x = 12.6 m; constraint (g*eta)(s) = 1 on the sample grid s in [0, S]")
mm = PM["2S-eq"]
xm = 12.6
eta = mm.il_defl(xm)                      # on [0, 60], spacing DX
fh = mm.il_hermite("d", xm)               # exact cubic between nodes
C0 = np.trapezoid(eta, mm.x)
ne = len(eta)
# misspecified "true" structures for the robustness test
EI2 = lambda s: mc.EI_PRISM * (1.2 if s > 30.0 else 1.0)
m_EI = mc.Model("two-span, span-2 EI x1.2", (30.0, 30.0), EIfun=EI2)
truths = {"exact": fh, "sensor +0.5 m": mm.il_hermite("d", xm + 0.5),
          "span-2 EI x1.2": m_EI.il_hermite("d", xm)}
rows, gsave = [], {}
sig, eps = 0.01, 0.1
rng = np.random.default_rng(11)
for S in (0.0, 2.0, 5.0, 10.0, 20.0, 40.0, 80.0, 160.0):
    T = mm.L + S
    N = int(round(T / mc.DX)) + 1
    ns = int(round(S / mc.DX)) + 1
    A = np.zeros((ns, N))
    for k in range(ns):
        A[k, k:k + ne] = eta
    # (a) min ||g||^2 (white noise)
    g = A.T @ np.linalg.solve(A @ A.T, np.ones(ns))
    # (b) with offsets: W = sig^2 I + eps^2 11'
    W = sig**2 * np.eye(N) + eps**2 * np.ones((N, N))
    WiAt = np.linalg.solve(W, A.T)
    gb = WiAt @ np.linalg.solve(A @ WiAt, np.ones(ns))
    # (c) offset-immune single channel: add 1'g = 0
    Ac = np.vstack([A, np.ones(N)])
    rhs = np.concatenate([np.ones(ns), [0.0]])
    gc = Ac.T @ np.linalg.solve(Ac @ Ac.T, rhs)
    okc = np.max(abs(Ac @ gc - rhs)) < 1e-6
    wu = mc.trap_weights(N) / C0
    vu_w = np.sum(wu**2)
    va_w = np.sum(g**2)
    vu_t = sig**2 * np.sum(wu**2) + eps**2 * np.sum(wu)**2
    vb_t = sig**2 * np.sum(gb**2) + eps**2 * np.sum(gb)**2
    vc_t = sig**2 * np.sum(gc**2) if okc else np.inf
    # Cauchy-Schwarz bound: sum_s h(s) = g'Phi = ns  =>  ||g||^2 >= ns^2/||Phi||^2
    Phi = A.sum(axis=0)
    lb = ns**2 / np.sum(Phi**2)
    vmf = 1.0 / np.sum(eta**2)
    # invariance defect at random OFF-GRID entry shifts, exact (Hermite) eta
    xs = np.arange(N) * mc.DX
    sh = rng.uniform(0, S, 400) if S > 0 else rng.uniform(0, mc.DX, 50)
    dfx = {}
    for nm, ft in truths.items():
        hg = np.array([g @ ft(xs - s_) for s_ in sh])
        hc = np.array([gc @ ft(xs - s_) for s_ in sh])
        hu = np.array([wu @ ft(xs - s_) for s_ in sh])
        dfx[nm] = [(hg.max() - hg.min()) / hg.mean(), (hc.max() - hc.min()) / hc.mean(),
                   (hu.max() - hu.min()) / hu.mean()]
    gsave[S] = (xs, g, gc, wu)
    rows.append([S, T, va_w / vu_w, lb / vu_w, vmf / vu_w, vb_t / vu_t, vc_t / vu_t,
                 np.sum(gc**2) / vu_w] + [v for nm in truths for v in dfx[nm]])
    log(f"  S = {S:5.1f} m (T = {T:5.1f}): white noise: Var_opt/Var_unif = {va_w/vu_w:.4f}, "
        f"CS bound = {lb/vu_w:.4f}, MF = {vmf/vu_w:.4f}, immune(1'g=0)/unif = "
        f"{np.sum(gc**2)/vu_w:.4f} | sig = {sig}, eps = {eps} mm: opt/unif = {vb_t/vu_t:.2e}, "
        f"immune/unif = {vc_t/vu_t:.2e}")
    log("      invariance defect (max-min)/mean of h(s), off-grid shifts [opt, immune, uniform]: "
        + "; ".join(f"{nm}: " + ", ".join(f"{v:.2e}" for v in dfx[nm]) for nm in truths))
hdr = ["S_m", "T_m", "var_opt_over_unif_white", "CS_lower_bound", "var_MF_over_unif",
       "var_opt_over_unif_eps0.1", "var_immune_over_unif_eps0.1", "var_immune_over_unif_white"]
for nm in truths:
    hdr += [f"defect_opt_{nm}", f"defect_immune_{nm}", f"defect_unif_{nm}"]
with open(f"{mc.RES}/T4_structure_aware.csv", "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(hdr)
    wr.writerows([[f"{v:.6g}" for v in r] for r in rows])
np.savez(f"{mc.RES}/T4_weights.npz", **{f"S{int(S)}_{k}": v for S, t in gsave.items()
                                        for k, v in zip(("x", "g", "gc", "wu"), t)})
log("  Reading: with eta known exactly, non-uniform invariant weights exist and can be")
log("  made offset-immune; the uniform weight is the only one whose invariance survives")
log("  any error in eta (defect 0), which is what SLM relies on.")
