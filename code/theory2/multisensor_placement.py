"""Package 1B - optimal sensor placement for the invariant multi-channel estimator.

Criterion: Var(P_hat) of the minimum-variance invariant estimator (GLS) and of
the offset-immune estimator.  For a scalar parameter D- and A-optimality
coincide (both minimise Var P_hat).  Because the noise and offset statistics do
not depend on position, Var^-1 = C' Q C (GLS) or C' Q_perp C (immune) is a
convex quadratic in the vector C of invariance constants, so its maximum over
the box [Cmin, Cmax]^k (every value is attained by continuity of C(x)) is at a
vertex: optimal sensors sit only at argmax C(x) or argmin C(x) of the uniform-
load response (per channel type) -- the extreme-point theorem.  The script
  (1) enumerates the vertex designs for all noise/offset settings,
  (2) verifies the theorem by brute force on a position grid,
  (3) solves the practical variant with distinct positions (min spacing 5 m),
  (4) gives a calibration-robust design for Cau May (A vs B).
Run: python3 code/theory2/multisensor_placement.py -> logs/multisensor_placement.log
"""
import csv
import itertools
import numpy as np
import multisensor_core as mc

log = mc.Logger("multisensor_placement.log")
PM = mc.prismatic_models()
CM = mc.caumay_models()
ALL = {**PM, **CM}
SIGS = (0.005, 0.01, 0.02)
EPSS = (0.02, 0.05, 0.1, 0.2, 0.5)
RHOS = (0.0, 0.5, 0.9, 1.0)
SIG_S, EPS_S = 1.0, 2.0
DMIN = 5.0


def pref(key):
    return mc.P_CM if key.startswith("CM") else mc.P_REF


def var_design(model, chans, sig, eps, rho, est="gls"):
    types = [t for t, _ in chans]
    C = [model.C(t, x) for t, x in chans]
    s_, e_ = mc.channel_defaults(types, sig, eps, SIG_S, EPS_S)
    S = mc.noise_cov(types, s_, e_, rho, mc.lrec(model))
    if est == "gls":
        return mc.gls(C, S)
    return mc.immune(C, S, types)


def extremes(model, typ):
    Cv = model.Cd if typ == "d" else model.Cs
    return [(typ, model.x[int(np.argmax(Cv))]), (typ, model.x[int(np.argmin(Cv))])]


def vertex_opt(model, k, tset, sig, eps, rho, est="gls"):
    cand = sum([extremes(model, t) for t in tset], [])
    best = (np.inf, None, None)
    for comb in itertools.combinations_with_replacement(range(len(cand)), k):
        ch = [cand[i] for i in comb]
        w, v = var_design(model, ch, sig, eps, rho, est)
        if v < best[0]:
            best = (v, ch, w)
    return best


def single_best(model, tset, sig, eps, rho):
    return vertex_opt(model, 1, tset, sig, eps, rho, "gls")


# --------------------------------------------------------- (1) vertex designs
log("=" * 78)
log("(1) Extreme-point designs. Var = Var(P_hat); std in % of P (250 kN prismatic, "
    "245.8 kN Cau May); 'ratio' = Var_k / Var_1 (single best sensor of the same types).")
log(f"    dx = {mc.DX} m, Lrec = L + {mc.ALLOW} m; strain channels: sig = {SIG_S} ue, "
    f"eps = {EPS_S} ue; offsets of different types independent.")
rows = []
for key, m in ALL.items():
    tsets = ["d"] if key.startswith("CM") else ["d", "s", "ds"]
    for tset in tsets:
        for sig in SIGS:
            for eps in EPSS:
                for rho in RHOS:
                    v1, ch1, _ = single_best(m, tset, sig, eps, rho)
                    for k in (1, 2, 3):
                        for est in ("gls", "immune"):
                            if est == "immune" and k == 1:
                                continue
                            v, ch, w = vertex_opt(m, k, tset, sig, eps, rho, est)
                            if ch is None:
                                continue
                            rows.append(dict(model=key, types=tset, sig=sig, eps=eps, rho=rho,
                                             k=k, est=est,
                                             design=" ".join(f"{t}@{x:.1f}" for t, x in ch),
                                             weights=" ".join(f"{wi:.5g}" for wi in w),
                                             std_pct=100 * np.sqrt(v) / pref(key),
                                             ratio=v / v1,
                                             single=" ".join(f"{t}@{x:.1f}" for t, x in ch1)))
with open(f"{mc.RES}/placement_vertex.csv", "w", newline="") as f:
    wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    wr.writeheader()
    wr.writerows(rows)
log(f"    {len(rows)} designs written to results/placement_vertex.csv")
for key in ALL:
    tset = "d"
    log(f"  {key} ({ALL[key].name}), deflection channels, sig = 0.01 mm:")
    for eps in (0.02, 0.1, 0.5):
        for rho in RHOS:
            sel = [r for r in rows if r["model"] == key and r["types"] == tset and
                   r["sig"] == 0.01 and r["eps"] == eps and r["rho"] == rho]
            txt = []
            for r in sel:
                txt.append(f"k={r['k']} {r['est'][:3]}: [{r['design']}] {r['std_pct']:.3g}% "
                           f"(x{r['ratio']:.3g})")
            log(f"    eps={eps:4.2f} rho={rho:3.1f} | " + " | ".join(txt))
for key in PM:
    log(f"  {key}: mixed deflection+strain (sig_d = 0.01 mm), best designs:")
    for eps in (0.1, 0.5):
        for rho in (0.0, 0.9):
            sel = [r for r in rows if r["model"] == key and r["types"] == "ds" and
                   r["sig"] == 0.01 and r["eps"] == eps and r["rho"] == rho and r["est"] == "gls"]
            log(f"    eps={eps:4.2f} rho={rho:3.1f} | " + " | ".join(
                f"k={r['k']}: [{r['design']}] {r['std_pct']:.3g}% (x{r['ratio']:.3g})" for r in sel))

# --------------------------------------------------------- (2)+(3) brute force


def combos(n, k, xg, dmin):
    """index combinations i<j<l of grid points with spacing >= dmin (dmin=0:
    with replacement)."""
    if k == 1:
        return np.arange(n)[:, None]
    out = []
    if k == 2:
        for i in range(n):
            j = np.arange(i if dmin == 0 else i + 1, n)
            j = j[xg[j] - xg[i] >= dmin - 1e-9]
            out.append(np.column_stack([np.full(len(j), i), j]))
        return np.vstack(out)
    for i in range(n):
        j0 = np.arange(i if dmin == 0 else i + 1, n)
        j0 = j0[xg[j0] - xg[i] >= dmin - 1e-9]
        for j in j0:
            l_ = np.arange(j if dmin == 0 else j + 1, n)
            l_ = l_[xg[l_] - xg[j] >= dmin - 1e-9]
            if len(l_):
                out.append(np.column_stack([np.full(len(l_), i), np.full(len(l_), j), l_]))
    return np.vstack(out)


def brute(model, k, sig, eps, rho, step, dmin, est="gls"):
    """Deflection channels only; exchangeable covariance S = a I + b 11'.
    GLS: Var^-1 = C'QC, Q = S^-1 = (I - b/(a+kb) 11')/a.
    immune: Var^-1 = (1/a) sum (C_j - Cbar)^2."""
    stride = int(round(step / mc.DX))
    xg, Cg = model.x[::stride], model.Cd[::stride]
    Lr = mc.lrec(model)
    a = sig**2 * mc.DX * (Lr - mc.DX / 2) + Lr**2 * eps**2 * (1 - rho)
    b = Lr**2 * eps**2 * rho
    idx = combos(len(xg), k, xg, dmin)
    Cc = Cg[idx]
    S1, S2 = Cc.sum(1), (Cc**2).sum(1)
    if est == "gls":
        J = (S2 - b / (a + k * b) * S1**2) / a
    else:
        J = (S2 - S1**2 / k) / a
    i = int(np.argmax(J))
    return xg[idx[i]], 1 / J[i]


log("=" * 78)
log("(2) Brute-force check of the extreme-point theorem (co-location allowed, grid "
    "0.5 m for k = 2, 1.0 m for k = 3), sig = 0.01 mm:")
chk = []
for key, m in ALL.items():
    for eps, rho in [(0.1, 0.0), (0.1, 0.5), (0.1, 0.9), (0.5, 1.0)]:
        for k in (2, 3):
            for est in ("gls", "immune"):
                xb, vb = brute(m, k, 0.01, eps, rho, 0.5 if k == 2 else 1.0, 0.0, est)
                vv, ch, _ = vertex_opt(m, k, "d", 0.01, eps, rho, est)
                chk.append(vb / vv)
                log(f"  {key:8s} eps={eps} rho={rho} k={k} {est:6s}: brute {np.round(xb,1).tolist()} "
                    f"Var {vb:.5e} | vertex [{' '.join(f'{x:.1f}' for _, x in ch)}] Var {vv:.5e} "
                    f"| ratio {vb/vv:.6f}")
log(f"  min ratio brute/vertex = {min(chk):.6f} (>= 1 up to grid resolution: theorem holds)")

log("=" * 78)
log(f"(3) Distinct positions, min spacing {DMIN} m (grid 0.5 m for k = 2; 1.0 m then "
    "0.1 m local refinement for k = 3), deflection channels, sig = 0.01 mm:")
rows3 = []


def refine(model, xs, sig, eps, rho, est, dmin):
    """Local refinement of a k = 3 design on the 0.1 m node grid (+-1.0 m)."""
    best = (var_design(model, [("d", x) for x in xs], sig, eps, rho, est)[1], xs)
    offs = np.arange(-1.0, 1.0001, 0.1)
    for d in itertools.product(offs, repeat=len(xs)):
        xn = np.clip(np.array(xs) + np.array(d), 0, model.L)
        xn = np.sort(xn)
        if np.min(np.diff(xn)) < dmin - 1e-9:
            continue
        v = var_design(model, [("d", x) for x in xn], sig, eps, rho, est)[1]
        if v < best[0]:
            best = (v, xn)
    return best[1], best[0]


for key, m in ALL.items():
    for eps in (0.02, 0.1, 0.5):
        for rho in RHOS:
            v1 = single_best(m, "d", 0.01, eps, rho)[0]
            for k in (2, 3):
                for est in ("gls", "immune"):
                    xb, vb = brute(m, k, 0.01, eps, rho, 0.5 if k == 2 else 1.0, DMIN, est)
                    if k == 3:
                        xb, vb = refine(m, list(xb), 0.01, eps, rho, est, DMIN)
                    rows3.append([key, eps, rho, k, est, " ".join(f"{x:.1f}" for x in xb),
                                  f"{100*np.sqrt(vb)/pref(key):.4g}", f"{vb/v1:.4g}"])
                    if eps in (0.1, 0.5):
                        log(f"  {key:8s} eps={eps:4.2f} rho={rho:3.1f} k={k} {est:6s}: x = "
                            f"{np.round(xb,1).tolist()} m, std {100*np.sqrt(vb)/pref(key):.4g}% "
                            f"(Var ratio to single best {vb/v1:.4g})")
with open(f"{mc.RES}/placement_distinct.csv", "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["model", "eps_mm", "rho", "k", "estimator", "positions_m", "std_pct",
                 "var_ratio_to_single_best"])
    wr.writerows(rows3)

# --------------------------------------------------------- (4) robust Cau May
log("=" * 78)
log("(4) Cau May: calibration-robust design (min over designs of max over A, B of "
    "Var/Var_opt,cal), distinct positions >= 5 m, deflection, sig = 0.01 mm, grid 1.0 m")
rows4 = []
for eps in (0.1, 0.5):
    for rho in (0.5, 0.9, 1.0):
        for k in (2, 3):
            for est in ("gls", "immune"):
                Js = {}
                for cal in ("A", "B"):
                    m = CM[f"CM-{cal}"]
                    stride = int(round(1.0 / mc.DX))
                    xg, Cg = m.x[::stride], m.Cd[::stride]
                    Lr = mc.lrec(m)
                    a = 0.01**2 * mc.DX * (Lr - mc.DX / 2) + Lr**2 * eps**2 * (1 - rho)
                    b = Lr**2 * eps**2 * rho
                    idx = combos(len(xg), k, xg, DMIN)
                    Cc = Cg[idx]
                    S1, S2 = Cc.sum(1), (Cc**2).sum(1)
                    J = (S2 - b / (a + k * b) * S1**2) / a if est == "gls" else (S2 - S1**2 / k) / a
                    Js[cal] = J
                rA = np.where(Js["A"] > 0, Js["A"].max() / np.maximum(Js["A"], 1e-300), np.inf)
                rB = np.where(Js["B"] > 0, Js["B"].max() / np.maximum(Js["B"], 1e-300), np.inf)
                worst = np.maximum(rA, rB)
                i = int(np.argmin(worst))
                iA, iB = int(np.argmax(Js["A"])), int(np.argmax(Js["B"]))
                rows4.append([eps, rho, k, est, " ".join(f"{x:.0f}" for x in xg[idx[i]]),
                              f"{worst[i]:.4f}", " ".join(f"{x:.0f}" for x in xg[idx[iA]]),
                              f"{rB[iA]:.4f}", " ".join(f"{x:.0f}" for x in xg[idx[iB]]),
                              f"{rA[iB]:.4f}"])
                log(f"  eps={eps} rho={rho} k={k} {est:6s}: robust x = {xg[idx[i]].tolist()} "
                    f"(worst Var ratio {worst[i]:.4f}); A-opt {xg[idx[iA]].tolist()} costs "
                    f"{rB[iA]:.4f} under B; B-opt {xg[idx[iB]].tolist()} costs {rA[iB]:.4f} under A")
with open(f"{mc.RES}/placement_caumay_robust.csv", "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["eps_mm", "rho", "k", "estimator", "robust_positions_m", "worst_var_ratio",
                 "A_opt_positions", "A_opt_ratio_under_B", "B_opt_positions",
                 "B_opt_ratio_under_A"])
    wr.writerows(rows4)
log("done")
