"""Package 1B - Monte Carlo verification (fixed seeds, 1e5 realisations per case).

Every realisation draws a random axle configuration (1-6 axles, loads
U(20,120) kN, spacings U(1,4) m, random entry delay inside the record
allowance), synthesises the full sampled record of every channel
  z_j(x_i) = sum_a P_a eta_j(x_i - s_a) + eps0_j + sig_j zeta_ij,
integrates it with the trapezoid rule and applies the estimators.  Offsets are
drawn from N(0, Sigma_eps) with a common-mode fraction rho within a channel
type.  eta_j is evaluated by cubic Hermite interpolation of the FE nodal
deflections and rotations (exact for prismatic elements).

Cases
  A  three-span 30+60+30 m: d@60 (Cmax), d@98.5 (Cmin < 0), d@15
  B  Cau May calibration A: d@100 (Cmax), d@155 (Cmin < 0), d@178 (gauge N8)
  C  two-span 30+30 m, mixed: d@12.6, s@12.6, s@30 (pier)
  D  two-span 30+30 m, single channel d@12.6, structure-aware weights (T4), S = 20 m,
     exact and misspecified structure (span-2 EI x1.2)
  plus a deterministic common-mode drift added to A and B (immunity test).
Run: python3 code/theory2/multisensor_mc.py -> logs/multisensor_mc.log
"""
import csv
import time
import numpy as np
import multisensor_core as mc

log = mc.Logger("multisensor_mc.log")
NREAL = int(__import__("os").environ.get("NREAL", 100_000))
BATCH = 1000
SEED = 20261018


class Channel:
    def __init__(self, model, typ, xm):
        self.typ, self.xm = typ, xm
        j = int(np.argmin(abs(model.x - xm)))
        if typ == "d":
            F = np.zeros(2 * len(model.x))
            F[2 * j] = 1.0
            u, sc = model._full_solve(F), 1e3
        else:
            u, sc = model._full_solve(model._curv_vec(j)), -mc.C_FIBRE * 1e6
        w, th = sc * u[0::2], sc * u[1::2]
        h = np.diff(model.x)
        assert np.allclose(h, mc.DX, atol=1e-9)
        ne = len(w) - 1
        pad = 10
        self.coef = np.zeros((4, ne + 2 * pad))           # element coefficients, padded
        self.coef[0, pad:pad + ne] = w[:-1]
        self.coef[1, pad:pad + ne] = mc.DX * th[:-1]
        self.coef[2, pad:pad + ne] = w[1:]
        self.coef[3, pad:pad + ne] = mc.DX * th[1:]
        self.pad, self.ne = pad, ne
        self.C = model.C(typ, xm)

    def record(self, s, P, N):
        """y(x_i), i = 0..N-1, for axles at entry shifts s (B x A) with loads P."""
        B, A = s.shape
        y = np.zeros((B, N))
        i = np.arange(N)
        for a in range(A):
            q = np.floor(s[:, a] / mc.DX).astype(int)
            t = 1.0 - (s[:, a] / mc.DX - q)                # local coordinate in (0, 1]
            e = i[None, :] - q[:, None] - 1
            e = np.clip(e, -self.pad, self.ne + self.pad - 1) + self.pad
            e[(i[None, :] - q[:, None] - 1 < 0) | (i[None, :] - q[:, None] - 1 >= self.ne)] = 0
            tt = t[:, None]
            H = (1 - 3 * tt**2 + 2 * tt**3, tt - 2 * tt**2 + tt**3,
                 3 * tt**2 - 2 * tt**3, tt**3 - tt**2)
            val = sum(H[k] * self.coef[k][e] for k in range(4))
            y += P[:, a:a + 1] * val
        return y


def configs(rng, B, allow):
    nax = rng.integers(1, 7, B)
    A = 6
    P = rng.uniform(20, 120, (B, A)) * (np.arange(A)[None, :] < nax[:, None])
    sp = rng.uniform(1.0, 4.0, (B, A)) * (np.arange(A)[None, :] < nax[:, None])
    sp[:, 0] = 0.0
    a = np.cumsum(sp, axis=1)
    amax = a.max(axis=1)
    d = rng.uniform(0, 1, B) * (allow - amax)
    s = d[:, None] + a
    s[P == 0] = 0.0
    return s, P, nax


def run_case(name, model, chans, sig, eps, rho, estimators, drift=None, seed=0):
    """estimators: dict name -> weight vector over channels (P_hat = w' I)."""
    rng = np.random.default_rng(SEED + seed)
    Lr = mc.lrec(model)
    N = int(round(Lr / mc.DX)) + 1
    wt = mc.trap_weights(N)
    types = [c.typ for c in chans]
    k = len(chans)
    Seps = np.outer(eps, eps) * (rho * np.array([[1.0 if a == b else 0.0 for b in types]
                                                for a in types]) + (1 - rho) * np.eye(k))
    Le = np.linalg.cholesky(Seps + 1e-15 * np.eye(k))
    xr = np.arange(N) * mc.DX
    out = {e: [] for e in estimators}
    clean = {e: [] for e in estimators}
    nax_all, P_all = [], []
    t0 = time.time()
    for b0 in range(0, NREAL, BATCH):
        s, P, nax = configs(rng, BATCH, mc.ALLOW)
        Ptot = P.sum(1)
        I = np.zeros((BATCH, k))
        I0 = np.zeros((BATCH, k))
        off = rng.standard_normal((BATCH, k)) @ Le.T
        for j, c in enumerate(chans):
            y = c.record(s, P, N)
            I0[:, j] = y @ wt
            z = y + off[:, j:j + 1] + sig[j] * rng.standard_normal((BATCH, N))
            if drift is not None and c.typ == "d":
                z = z + drift(xr)[None, :]
            I[:, j] = z @ wt
        for e, w in estimators.items():
            out[e].append(I @ w - Ptot)
            clean[e].append(I0 @ w / Ptot - 1)
        nax_all.append(nax)
        P_all.append(Ptot)
    log(f"  [{name}] {NREAL} realisations in {time.time()-t0:.0f} s, N = {N} samples/channel")
    res = {e: np.concatenate(v) for e, v in out.items()}
    res_clean = {e: np.concatenate(v) for e, v in clean.items()}
    return res, res_clean, np.concatenate(nax_all), np.concatenate(P_all)


def summarise(name, model, chans, sig, eps, rho, estimators, res, clean, nax, Ptot,
              rows, theory=None):
    types = [c.typ for c in chans]
    S = mc.noise_cov(types, sig, eps, rho, mc.lrec(model))
    for e, w in estimators.items():
        vt = w @ S @ w if theory is None else theory[e]
        err = res[e]
        sd = err.std(ddof=1)
        se_mean = sd / np.sqrt(len(err))
        se_sd = sd / np.sqrt(2 * (len(err) - 1))
        z_mean = err.mean() / se_mean
        byn = [(n, err[nax == n].mean(), err[nax == n].std(ddof=1)) for n in range(1, 7)]
        sd_n = np.array([b[2] for b in byn])
        log(f"  [{name}] {e:22s} w = {np.round(w, 6).tolist()}  w'C = {w @ np.array([c.C for c in chans]):.6f}")
        log(f"      mean error {err.mean():+.4f} kN (z = {z_mean:+.2f}); std {sd:.4f} kN, "
            f"theory {np.sqrt(vt):.4f} kN, ratio {sd/np.sqrt(vt):.4f} (+-{se_sd/np.sqrt(vt):.4f})")
        log(f"      noise-free invariance: max |P_hat/P - 1| = {np.max(abs(clean[e])):.2e}; "
            f"by axle count std = {np.round(sd_n, 4).tolist()} kN, "
            f"means = {np.round([b[1] for b in byn], 4).tolist()} kN")
        rows.append([name, e, len(err), f"{err.mean():.5g}", f"{z_mean:.3f}", f"{sd:.6g}",
                     f"{np.sqrt(vt):.6g}", f"{sd/np.sqrt(vt):.5f}", f"{np.max(abs(clean[e])):.3e}",
                     ";".join(f"{v:.5g}" for v in sd_n)])


rows = []
np_save = {}
sigd, epsd, rho = 0.01, 0.1, 0.9
PM = mc.prismatic_models()
CMm = mc.caumay_models()


def drift(x):
    L = x[-1]
    return 0.5 + 0.5 * x / L + 0.2 * np.sin(3 * np.pi * x / L)


for case, model, spec in [("A", PM["3S-b2.0"], [("d", 60.0), ("d", 98.5), ("d", 15.0)]),
                          ("B", CMm["CM-A"], [("d", 100.0), ("d", 155.0), ("d", 178.0)])]:
    log("=" * 78)
    chans = [Channel(model, t, x) for t, x in spec]
    C = np.array([c.C for c in chans])
    sig, eps = [sigd] * 3, [epsd] * 3
    S = mc.noise_cov(["d"] * 3, sig, eps, rho, mc.lrec(model))
    w1 = np.array([1 / C[0], 0, 0])
    wg = mc.gls(C, S)[0]
    wi = mc.immune(C, S, ["d"] * 3)[0]
    est = {"single (Cmax)": w1, "GLS-3": wg, "immune-3": wi}
    log(f"Case {case}: {model.name}, channels {spec}, C = {np.round(C, 6).tolist()}, "
        f"sig = {sigd} mm, eps = {epsd} mm, rho = {rho}")
    res, cl, nax, Pt = run_case(case, model, chans, sig, eps, rho, est, seed=ord(case))
    summarise(case, model, chans, sig, eps, rho, est, res, cl, nax, Pt, rows)
    for e in est:
        np_save[f"{case}_{e}"] = res[e].astype(np.float32)
    np_save[f"{case}_nax"] = nax.astype(np.int8)
    np_save[f"{case}_P"] = Pt.astype(np.float32)
    # deterministic common-mode drift on top (immunity test)
    log(f"  [{case}+drift] common drift d(x) = 0.5 + 0.5 x/Lrec + 0.2 sin(3 pi x/Lrec) mm on "
        f"every deflection channel; predicted bias w' (sum_i wt_i d_i) 1:")
    Lr = mc.lrec(model)
    N = int(round(Lr / mc.DX)) + 1
    Dint = mc.trap_weights(N) @ drift(np.arange(N) * mc.DX)
    resd, cld, naxd, Ptd = run_case(case + "+drift", model, chans, sig, eps, rho, est,
                                    drift=drift, seed=ord(case) + 100)
    for e, w in est.items():
        bias_pred = Dint * w.sum()
        log(f"      {e:22s} mean error {resd[e].mean():+9.4f} kN (predicted {bias_pred:+9.4f}), "
            f"std {resd[e].std(ddof=1):.4f} kN")
        rows.append([case + "+drift", e, NREAL, f"{resd[e].mean():.5g}", f"pred {bias_pred:.5g}",
                     f"{resd[e].std(ddof=1):.6g}", "", "", "", ""])

# ---------------------------------------------------------------- case C mixed
log("=" * 78)
model = PM["2S-eq"]
spec = [("d", 12.6), ("s", 12.6), ("s", 30.0)]
chans = [Channel(model, t, x) for t, x in spec]
C = np.array([c.C for c in chans])
types = [c.typ for c in chans]
sig, eps = mc.channel_defaults(types, sigd, epsd, 1.0, 2.0)
S = mc.noise_cov(types, sig, eps, rho, mc.lrec(model))
vs = [S[j, j] / C[j]**2 for j in range(3)]
jb = int(np.argmin(vs))
w1 = np.zeros(3)
w1[jb] = 1 / C[jb]
est = {f"single ({spec[jb][0]}@{spec[jb][1]})": w1, "GLS-3": mc.gls(C, S)[0],
       "immune (strain pair)": mc.immune(C, S, types)[0]}
log(f"Case C: {model.name}, channels {spec}, C = {np.round(C, 6).tolist()}, sig = {sig}, "
    f"eps = {eps}, rho (strain common mode) = {rho}")
res, cl, nax, Pt = run_case("C", model, chans, sig, eps, rho, est, seed=ord("C"))
summarise("C", model, chans, sig, eps, rho, est, res, cl, nax, Pt, rows)

# ---------------------------------------------------------------- case D
log("=" * 78)
log("Case D: structure-aware invariant weights, 2S-eq d@12.6, S = 20 m (= record allowance)")
model = PM["2S-eq"]
ch = Channel(model, "d", 12.6)
Lr = mc.lrec(model)
N = int(round(Lr / mc.DX)) + 1
eta_nodes = model.il_defl(12.6)
ne_ = len(eta_nodes)
ns = int(round(mc.ALLOW / mc.DX)) + 1
A = np.zeros((ns, N))
for kk in range(ns):
    A[kk, kk:kk + ne_] = eta_nodes
sig1, eps1 = 0.01, 0.1
W = sig1**2 * np.eye(N) + eps1**2 * np.ones((N, N))
WiAt = np.linalg.solve(W, A.T)
g_opt = WiAt @ np.linalg.solve(A @ WiAt, np.ones(ns))
Ac = np.vstack([A, np.ones(N)])
g_imm = Ac.T @ np.linalg.solve(Ac @ Ac.T, np.concatenate([np.ones(ns), [0.0]]))
g_uni = mc.trap_weights(N) / ch.C
wts = {"uniform": g_uni, "struct-aware GLS": g_opt, "struct-aware immune": g_imm}
theory = {e: sig1**2 * np.sum(g**2) + eps1**2 * np.sum(g)**2 for e, g in wts.items()}
EI2 = lambda s_: mc.EI_PRISM * (1.2 if s_ > 30.0 else 1.0)
m_mis = mc.Model("two-span, span-2 EI x1.2", (30.0, 30.0), EIfun=EI2)
for tag, truth in [("D", model), ("D-misspecified", m_mis)]:
    chT = Channel(truth, "d", 12.6)
    rng = np.random.default_rng(SEED + 7 + len(tag))
    errs = {e: [] for e in wts}
    rel = {e: [] for e in wts}
    naxs = []
    t0 = time.time()
    for b0 in range(0, NREAL, BATCH):
        s, P, nax = configs(rng, BATCH, mc.ALLOW)
        Ptot = P.sum(1)
        y = chT.record(s, P, N)
        z = y + eps1 * rng.standard_normal((BATCH, 1)) + sig1 * rng.standard_normal((BATCH, N))
        for e, g in wts.items():
            # SLM-style scale: divide by the estimator's response to a unit load
            # on the TRUE structure, averaged over entry shifts (scale is calibrated)
            errs[e].append(z @ g - Ptot)
            rel[e].append((y @ g) / Ptot)
        naxs.append(nax)
    nax = np.concatenate(naxs)
    log(f"  [{tag}] {NREAL} realisations in {time.time()-t0:.0f} s; truth: {truth.name}")
    for e in wts:
        err = np.concatenate(errs[e])
        r = np.concatenate(rel[e])
        sd = err.std(ddof=1)
        if tag == "D":
            log(f"      {e:22s} mean error {err.mean():+.4f} kN (z = {err.mean()/(sd/np.sqrt(NREAL)):+.2f}), "
                f"std {sd:.4f} kN, theory {np.sqrt(theory[e]):.4f} kN, ratio {sd/np.sqrt(theory[e]):.4f}; "
                f"noise-free max|P_hat/P-1| = {np.max(abs(r-1)):.2e}")
            rows.append([tag, e, NREAL, f"{err.mean():.5g}", "", f"{sd:.6g}",
                         f"{np.sqrt(theory[e]):.6g}", f"{sd/np.sqrt(theory[e]):.5f}",
                         f"{np.max(abs(r-1)):.3e}", ""])
            np_save[f"D_{e}"] = err.astype(np.float32)
        else:
            rs = r / r.mean()          # scale error removed (SLM calibrates it)
            byn = [rs[nax == n].mean() - 1 for n in range(1, 7)]
            log(f"      {e:22s} noise-free P_hat/P after scale calibration: range "
                f"[{rs.min()-1:+.4f}, {rs.max()-1:+.4f}], std {rs.std():.4f}; mean by axle count "
                f"{np.round(byn, 4).tolist()}; total std incl. noise/offset {sd:.3f} kN")
            rows.append([tag, e, NREAL, "", "", f"{sd:.6g}", "", "",
                         f"range {rs.min()-1:.4f}..{rs.max()-1:.4f}", f"cfg std {rs.std():.5f}"])
    np_save[f"{tag}_nax"] = nax.astype(np.int8)

with open(f"{mc.RES}/mc_summary.csv", "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["case", "estimator", "n", "mean_err_kN", "z_mean_or_pred", "std_kN",
                 "std_theory_kN", "ratio", "noise_free_max_rel_or_range", "std_by_axle_count"])
    wr.writerows(rows)
np.savez_compressed(f"{mc.RES}/mc_errors.npz", **np_save)
log("done")
