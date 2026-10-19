"""v4 re-analysis of the Smart Road Bridge NOR-BWIM field records (figshare 26880898).

Responds to the v3 editor reports (docs/editors_v3/): all channels, equivalence tests,
speed with truck as factor, measured cross-channel noise covariance, and out-of-sample
(leave-one-run-out) comparison of single-gauge, gauge-average, GLS and offset-immune
estimators. Inputs:
  results/events_field_qc.csv   (crossing integrals, from nb_field.py + nb_tests.py)
  cache/strains200.pkl, cache/allstrain.pkl  (raw records, via nb_io; read only)
Outputs: logs/v4.log, results/v4_*.csv, figures/v4_*.png/.pdf
Run:  python3 -I nb_v4.py          (about 1-2 min)

Nothing here changes nb_field / nb_tests results; their functions are reused unchanged.
"""
import os
import sys
import json
import numpy as np
import pandas as pd
from scipy import stats as sst
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import nb_io as nio      # noqa: E402
import nb_events as ev   # noqa: E402
import nb_field as nf    # noqa: E402  (import no longer touches logs/field.log)

RES = os.path.join(HERE, "results")
FIG = os.path.join(HERE, "figures")
LOGP = os.path.join(HERE, "logs", "v4.log")
LOG = None
NBOOT = 10000
RNG_SEED = 20261018
plt.rcParams.update({"font.size": 8, "axes.grid": True, "grid.alpha": .3,
                     "savefig.dpi": 300, "figure.dpi": 100})

CH2 = ["st40", "st36", "st34", "st31"]
CH1 = [f"ch{k}" for k in range(1, 13)]
AVG1 = nf.AVG1                          # ch4, ch5, ch12, ch11 (strong axle spikes)
NOSPIKE1 = ["ch1", "ch2", "ch8", "ch9"]  # no axle spikes (nb_field / 3_norbwim_analysis)


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    if LOG is not None:
        LOG.write(s + "\n")
        LOG.flush()


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name + ".png"), dpi=300)
    fig.savefig(os.path.join(FIG, name + ".pdf"))
    plt.close(fig)


# =========================================================== data
def load_events():
    F = pd.read_csv(os.path.join(RES, "events_field_qc.csv"))
    F["excluded"] = F["excluded"].fillna("")
    single = F[~F.trucks.str.contains(r"\+") & (F.excluded == "")]
    G = {"d1A": single[single.day == 1].reset_index(drop=True),
         "d2A": single[(single.day == 2) & (single.lane == "A")].reset_index(drop=True),
         "d2B": single[(single.day == 2) & (single.lane == "B")].reset_index(drop=True)}
    multi = F[F.trucks.str.contains(r"\+") & (F.excluded == "")].reset_index(drop=True)
    return F, G, multi


def Ix(df, c):
    """Integral in space, microstrain*m."""
    return (df[f"Idt_{c}"] * df.v1).values


def Cper(df, c):
    return Ix(df, c) / df.GVW.values


# =========================================================== statistics helpers
def boot_ci(x, fun, n=NBOOT, seed=0, alpha=0.05):
    rng = np.random.default_rng(seed)
    x = np.asarray(x)
    idx = rng.integers(0, len(x), size=(n, len(x)))
    b = np.array([fun(x[i]) for i in idx])
    return np.nanpercentile(b, 100 * alpha / 2), np.nanpercentile(b, 100 * (1 - alpha / 2))


def cv(x):
    return np.std(x, ddof=1) / abs(np.mean(x))


def cv_ci_param(x, alpha=0.05):
    """Normal-theory CI of CV via chi-square CI of the sd (mean treated as fixed)."""
    n = len(x)
    s, m = np.std(x, ddof=1), abs(np.mean(x))
    lo = s * np.sqrt((n - 1) / sst.chi2.ppf(1 - alpha / 2, n - 1)) / m
    hi = s * np.sqrt((n - 1) / sst.chi2.ppf(alpha / 2, n - 1)) / m
    return lo, hi


def welch_logratio(a, b):
    """Ratio mean(b)/mean(a) of same-sign samples via Welch t on log|.|.
    Returns ratio, 95% CI, 90% CI, TOST p for margins 5% and 10%, two-sided p (ratio=1)."""
    a, b = np.log(np.abs(a)), np.log(np.abs(b))
    d = b.mean() - a.mean()
    va, vb = a.var(ddof=1) / len(a), b.var(ddof=1) / len(b)
    se = np.sqrt(va + vb)
    df = (va + vb) ** 2 / (va ** 2 / (len(a) - 1) + vb ** 2 / (len(b) - 1))
    out = dict(ratio=np.exp(d), se_log=se, df=df,
               ci95_lo=np.exp(d - sst.t.ppf(.975, df) * se),
               ci95_hi=np.exp(d + sst.t.ppf(.975, df) * se),
               ci90_lo=np.exp(d - sst.t.ppf(.95, df) * se),
               ci90_hi=np.exp(d + sst.t.ppf(.95, df) * se),
               p_diff=2 * sst.t.sf(abs(d) / se, df))
    for m in (5, 10):
        lo, hi = np.log(1 - m / 100), np.log(1 + m / 100)
        p_lo = sst.t.sf((d - lo) / se, df)      # H0: d <= lo
        p_hi = sst.t.cdf((d - hi) / se, df)     # H0: d >= hi
        out[f"tost_p_{m}"] = max(p_lo, p_hi)
        out[f"equiv_{m}"] = bool(out[f"tost_p_{m}"] < 0.05)
    return out


def verdict(w):
    if w["equiv_5"]:
        return "equivalent within 5%"
    if w["equiv_10"]:
        return "equivalent within 10%"
    if w["p_diff"] < 0.05:
        return "DIFFERENT (95% CI excludes 1)"
    return "inconclusive (CI too wide)"


def chi2_noise(r, s):
    w = 1 / s ** 2
    mw = np.sum(w * r) / np.sum(w)
    chi = np.sum(((r - mw) / s) ** 2)
    return sst.chi2.sf(chi, len(r) - 1)


# =========================================================== task 1: invariance
def task1(G):
    log("\n" + "=" * 78 + "\nTASK 1. Per-channel constant C = int(eps dx)/GVW (microstrain*m/t)")
    log("Day-1 GVW: driver-reported per pass (Moghadam 2022 dissertation, hdl:10919/111390,"
        " Table 2.4); day-2 GVW: static weigh-station weights (same source, Table 2.1, "
        "Sec. 2.2.3). Day-1 runs R1-R4 = Truck 1, R7-R9 = Truck 2 (both 3-axle); day-2 "
        "lane A R11-R14 = Truck 3 (3-axle), R15-R18 = Truck 4 (5-axle).")
    log("Ratio CIs: Welch t on log|C| (empirical scatter, small n). TOST = 90% CI inside "
        "[1-m, 1+m]. chi2_p uses the noise sd from vehicle-free windows (nb_tests).")
    rows = []
    for g, chans, ta, tb in [("d1A", CH1 + ["avg"], "T1", "T2"),
                             ("d2A", CH2 + ["avg"], "T3", "T4"),
                             ("d2B", CH2 + ["avg"], "T3", "T4")]:
        df = G[g]
        for c in chans:
            r = Cper(df, c)
            s = (df[f"noise_sd_Idt_{c}"] * df.v1 / df.GVW).values
            assert np.all(r < 0), (g, c)
            n = len(r)
            m = r.mean()
            se = r.std(ddof=1) / np.sqrt(n)
            tq = sst.t.ppf(.975, n - 1)
            blo, bhi = boot_ci(r, cv, seed=RNG_SEED + len(rows))
            plo, phi = cv_ci_param(r)
            ma, mb = df.trucks.values == ta, df.trucks.values == tb
            w = welch_logratio(r[ma], r[mb])
            rows.append(dict(group=g, channel=c, n=n, C_mean=m, C_ci_lo=m - tq * se,
                             C_ci_hi=m + tq * se, CV=cv(r), CV_boot_lo=blo, CV_boot_hi=bhi,
                             CV_param_lo=plo, CV_param_hi=phi,
                             CV_noise=np.sqrt(np.mean(s ** 2)) / abs(m),
                             chi2_p=chi2_noise(r, s),
                             truckA=ta, truckB=tb, nA=ma.sum(), nB=mb.sum(),
                             C_A=r[ma].mean(), C_B=r[mb].mean(),
                             ratio_B_over_A=w["ratio"], ratio_ci95_lo=w["ci95_lo"],
                             ratio_ci95_hi=w["ci95_hi"], ratio_ci90_lo=w["ci90_lo"],
                             ratio_ci90_hi=w["ci90_hi"], p_diff=w["p_diff"],
                             tost_p_5=w["tost_p_5"], tost_p_10=w["tost_p_10"],
                             verdict=verdict(w)))
    T1 = pd.DataFrame(rows)
    T1["flag"] = np.where((T1.chi2_p < 0.05) | T1.verdict.str.startswith("DIFF"), "FAIL",
                          np.where(T1.verdict.str.startswith("equiv"), "pass", "weak"))
    T1.to_csv(os.path.join(RES, "v4_invariance.csv"), index=False)
    for g, title in [("d1A", "Day 1 lane A, T2/T1 (both 3-axle, driver-reported GVW)"),
                     ("d2A", "Day 2 lane A, T4(5-axle)/T3(3-axle), scale GVW"),
                     ("d2B", "Day 2 lane B (return trips, gauge-lag speeds), T4/T3")]:
        log(f"\n--- {title}")
        log(f"{'ch':5s} {'n':>2s} {'C':>6s} {'95%CI':>15s} {'CV%':>5s} {'CVboot95':>12s} "
            f"{'CVnoise':>7s} {'chi2p':>6s} {'ratio':>6s} {'95%CI':>13s} {'90%CI':>13s} "
            f"{'pTOST5':>6s} {'pTOST10':>7s}  verdict / flag")
        for _, r in T1[T1.group == g].iterrows():
            log(f"{r.channel:5s} {r.n:2d} {r.C_mean:6.2f} [{r.C_ci_lo:5.2f},{r.C_ci_hi:5.2f}] "
                f"{100*r.CV:5.1f} [{100*r.CV_boot_lo:4.1f},{100*r.CV_boot_hi:4.1f}] "
                f"{100*r.CV_noise:7.1f} {r.chi2_p:6.3f} {r.ratio_B_over_A:6.3f} "
                f"[{r.ratio_ci95_lo:.3f},{r.ratio_ci95_hi:.3f}] "
                f"[{r.ratio_ci90_lo:.3f},{r.ratio_ci90_hi:.3f}] {r.tost_p_5:6.3f} "
                f"{r.tost_p_10:7.3f}  {r.verdict} / {r.flag}")
    # pooled 3-axle (day 2 T3) vs 5-axle with equivalence statement: smallest margin
    for g in ("d1A", "d2A"):
        for _, r in T1[(T1.group == g) & (T1.channel == "avg")].iterrows():
            mmin = 100 * max(1 - r.ratio_ci90_lo, r.ratio_ci90_hi - 1)
            log(f"{g} avg: smallest symmetric margin excluded by TOST at 5% level = "
                f"+-{mmin:.1f}%")
    return T1


# =========================================================== task 2: speed
def ols(X, y):
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    res = y - X @ beta
    dof = len(y) - X.shape[1]
    s2 = res @ res / dof
    cov = s2 * np.linalg.inv(X.T @ X)
    return beta, np.sqrt(np.diag(cov)), dof


def task2(G):
    log("\n" + "=" * 78 + "\nTASK 2. Speed: C ~ v (pooled) and C ~ truck + v (OLS, empirical "
        "residual variance). Slope in % of mean C per 10 m/s; 95% CI; equivalence if the "
        "90% CI lies inside +-5 or +-10 %/10 m/s.")
    rows = []
    for g, chans, ta in [("d1A", CH1 + ["avg"], "T1"), ("d2A", CH2 + ["avg"], "T3")]:
        df = G[g]
        v = df.v1.values
        trk = (df.trucks.values != ta).astype(float)
        rpb = np.corrcoef(trk, v)[0, 1]
        vif = 1 / (1 - rpb ** 2)
        within = np.sum((v - np.array([v[trk == k].mean() for k in trk])) ** 2)
        total = np.sum((v - v.mean()) ** 2)
        log(f"\n{g}: corr(truck, speed) = {rpb:.3f}, VIF = {vif:.1f}; within-truck share of "
            f"speed variance = {100*within/total:.1f}%  (speeds "
            + ", ".join(f"{t}: {v[df.trucks.values == t].min():.1f}-"
                        f"{v[df.trucks.values == t].max():.1f}"
                        for t in sorted(set(df.trucks))) + " m/s)")
        for c in chans:
            y = Cper(df, c)
            mC = y.mean()
            for model in ("pooled", "truck+v"):
                X = np.column_stack([np.ones_like(v), v - v.mean()] +
                                    ([trk - trk.mean()] if model == "truck+v" else []))
                b, se, dof = ols(X, y)
                k = 1000 / mC
                sl, sls = b[1] * k, abs(se[1] * k)
                t95, t90 = sst.t.ppf(.975, dof), sst.t.ppf(.95, dof)
                row = dict(group=g, channel=c, model=model, slope_pct_10ms=sl,
                           slope_se=sls, ci95_lo=sl - t95 * sls, ci95_hi=sl + t95 * sls,
                           ci90_lo=sl - t90 * sls, ci90_hi=sl + t90 * sls, dof=dof,
                           p_slope=2 * sst.t.sf(abs(sl / sls), dof),
                           equiv_5=bool(abs(sl) + t90 * sls < 5),
                           equiv_10=bool(abs(sl) + t90 * sls < 10),
                           corr_truck_speed=rpb, VIF=vif)
                if model == "truck+v":
                    row["truck_effect_pct"] = 100 * b[2] / mC
                    row["truck_effect_se"] = abs(100 * se[2] / mC)
                rows.append(row)
    S = pd.DataFrame(rows)
    S.to_csv(os.path.join(RES, "v4_speed.csv"), index=False)
    for g in ("d1A", "d2A"):
        log(f"\n--- {g}")
        log(f"{'ch':5s} {'model':8s} {'slope':>7s} {'95% CI':>17s} {'p':>6s} eq5 eq10 "
            f"{'truck eff %':>12s}")
        for _, r in S[S.group == g].iterrows():
            te = (f"{r.truck_effect_pct:+6.1f}+-{r.truck_effect_se:4.1f}"
                  if r.model == "truck+v" else "")
            log(f"{r.channel:5s} {r.model:8s} {r.slope_pct_10ms:+7.1f} "
                f"[{r.ci95_lo:+6.1f},{r.ci95_hi:+6.1f}] {r.p_slope:6.3f} "
                f"{'Y' if r.equiv_5 else 'n':>3s} {'Y' if r.equiv_10 else 'n':>4s} {te:>12s}")
    return S


# =========================================================== task 3: noise covariance
def window_integrals(Yd, fs, chans, busy, Twin, step, nbase=8.0, buf=70.0, T=None):
    """Sliding-window integrals (microstrain*s) of quiet record segments of length Twin,
    same baseline as the crossings (linear through 8 s pre/post means; nb_events.integrate).
    A window is quiet if no detected vehicle onset lies within buf seconds of it."""
    n = len(Yd[chans[0]])
    T = (n - 1) / fs
    starts = np.arange(nbase + 1, T - Twin - nbase - 1, step)
    busy = np.asarray(busy)
    out, used = [], []
    for ta in starts:
        tb = ta + Twin
        if np.any((busy > ta - buf) & (busy < tb + buf)):
            continue
        i0 = int(np.floor((ta - nbase - 1) * fs))
        i1 = int(np.ceil((tb + nbase + 1) * fs)) + 1
        tt = np.arange(i0, i1) / fs
        out.append([ev.integrate(tt, Yd[c][i0:i1], ta, tb, nbase)[0] for c in chans])
        used.append(ta)
    return np.array(out), np.array(used)


def corr_summary(Z):
    R = np.corrcoef(Z.T)
    k = R.shape[0]
    off = R[np.triu_indices(k, 1)]
    lam = np.linalg.eigvalsh(R)[::-1]
    return R, off.mean(), off.min(), off.max(), lam[0] / k


def task3(raw, G):
    log("\n" + "=" * 78 + "\nTASK 3. Cross-channel covariance of the integrated noise "
        "(vehicle-free sliding windows, step 2 s, >=70 s from any detected vehicle).")
    NZ = {}
    rows = []
    for day, chans, gname in [(2, CH2, "d2A"), (1, CH1, "d1A")]:
        Yd, fs, busy, Ttot = raw[day]
        lens = sorted(set(int(round(t / 2) * 2) for t in G[gname].T_win))
        if day == 2:
            lens = sorted(set(lens) | set(int(round(t / 2) * 2) for t in G["d2B"].T_win))
        Tref = int(round(np.median(G[gname].T_win) / 2) * 2)
        lens = sorted(set(lens) | {Tref})
        NZ[day] = {}
        for Tw in lens:
            Z, st = window_integrals(Yd, fs, chans, busy, Tw, step=2.0)
            NZ[day][Tw] = Z
        Z = NZ[day][Tref]
        Zs, st = window_integrals(Yd, fs, chans, busy, Tref, step=float(Tref + 16))
        R, rbar, rmin, rmax, l1 = corr_summary(Z)
        Rn, rbarn, *_ , l1n = corr_summary(Zs)
        # bootstrap over non-overlapping windows for rho
        rng = np.random.default_rng(RNG_SEED + day)
        bs = []
        for _ in range(2000):
            i = rng.integers(0, len(Zs), len(Zs))
            _, rb, _, _, lb = corr_summary(Zs[i])
            bs.append((rb, lb))
        bs = np.array(bs)
        vbar = np.median(G[gname].v1)
        sd = Z.std(axis=0, ddof=1)
        log(f"\nDay {day}: record {Ttot:.0f} s, {len(busy)} detected vehicles; window T = "
            f"{Tref} s (median crossing window); {len(Z)} sliding windows (step 2 s), "
            f"{len(Zs)} non-overlapping")
        log("noise sd of integral (microstrain*s): " +
            ", ".join(f"{c}={s:.3f}" for c, s in zip(chans, sd)))
        log(f"  same in microstrain*m at median speed {vbar:.1f} m/s: " +
            ", ".join(f"{c}={s*vbar:.1f}" for c, s in zip(chans, sd)))
        log(f"mean off-diagonal r = {rbar:.3f} (range {rmin:.3f} to {rmax:.3f}); "
            f"first-eigenvalue fraction lambda1/k = {l1:.3f}")
        log(f"non-overlapping windows: mean r = {rbarn:.3f} [95% bootstrap "
            f"{np.percentile(bs[:,0],2.5):.3f}, {np.percentile(bs[:,0],97.5):.3f}], "
            f"lambda1/k = {l1n:.3f} [{np.percentile(bs[:,1],2.5):.3f}, "
            f"{np.percentile(bs[:,1],97.5):.3f}]")
        log("correlation matrix:")
        log("      " + " ".join(f"{c:>6s}" for c in chans))
        for c, rr in zip(chans, R):
            log(f"{c:5s} " + " ".join(f"{x:6.2f}" for x in rr))
        if day == 1:
            for sub, nm in [(AVG1, "wheel-path ch4,5,11,12"), (NOSPIKE1, "no-spike ch1,2,8,9"),
                            ([c for c in CH1 if c not in NOSPIKE1], "8 spike channels")]:
                ii = [chans.index(c) for c in sub]
                _, rb, rmn, rmx, lb = corr_summary(Z[:, ii])
                log(f"  subset {nm}: mean r = {rb:.3f} (range {rmn:.3f}-{rmx:.3f}), "
                    f"lambda1/k = {lb:.3f}")
        # equal-weight common-mode reduction: sd of mean of channels vs mean sd
        avg_sd = Z.mean(axis=1).std(ddof=1)
        log(f"sd of channel-mean integral = {avg_sd:.3f} vs mean channel sd "
            f"{sd.mean():.3f} (independent would give {np.sqrt(np.sum(sd**2))/len(sd):.3f})")
        for Tw in lens:
            Zt = NZ[day][Tw]
            _, rb, rmn, rmx, lb = corr_summary(Zt)
            rows.append(dict(day=day, T_win=Tw, n_windows=len(Zt), mean_r=rb, min_r=rmn,
                             max_r=rmx, lambda1_frac=lb,
                             **{f"sd_{c}": s for c, s in zip(chans, Zt.std(axis=0, ddof=1))}))
        pd.DataFrame(R, index=chans, columns=chans).to_csv(
            os.path.join(RES, f"v4_noise_corr_day{day}.csv"))
        NZ[day]["Tref"] = Tref
    N = pd.DataFrame(rows)
    N.to_csv(os.path.join(RES, "v4_noise_summary.csv"), index=False)
    log("\nper window length:")
    log(N[["day", "T_win", "n_windows", "mean_r", "min_r", "max_r", "lambda1_frac"]]
        .round(3).to_string())
    # cross-check with nb_field's 80 random windows (noise_sd_Idt in events table)
    for day, chans, g in [(2, CH2, "d2A"), (1, CH1, "d1A")]:
        df = G[g]
        r = []
        for _, e in df.iterrows():
            Tw = int(round(e.T_win / 2) * 2)
            sd = NZ[day][Tw].std(axis=0, ddof=1)
            r.append([sd[i] / e[f"noise_sd_Idt_{c}"] for i, c in enumerate(chans)])
        log(f"day {day}: sliding-window sd / nb_field random-window sd: median "
            f"{np.median(r):.3f} (range {np.min(r):.3f}-{np.max(r):.3f})")
    return NZ


# =========================================================== task 4: estimators
def weights(kind, C, S):
    k = len(C)
    if kind.startswith("single:"):
        w = np.zeros(k)
        j = int(kind.split(":")[1])
        w[j] = 1 / C[j]
        return w
    if kind == "average":
        return np.ones(k) / np.sum(C)
    if kind == "GLS":
        a = np.linalg.solve(S, C)
        return a / (C @ a)
    if kind == "GLS-diag":
        a = C / np.diag(S)
        return a / (C @ a)
    if kind in ("immune", "immune-eq"):
        A = np.column_stack([C, np.ones(k)])
        M = S if kind == "immune" else np.eye(k)
        Si_A = np.linalg.solve(M, A)
        return Si_A @ np.linalg.solve(A.T @ Si_A, np.array([1.0, 0.0]))
    raise ValueError(kind)


def run_estimators(df, chans, Sig_of, kinds, cal_mask_fn, label):
    """For each test run i: C from calibration runs (cal_mask_fn(i)), Sigma for the
    test-run window (from vehicle-free data, never from crossings), Ix of test run.
    Returns long DataFrame of errors."""
    I = np.column_stack([Ix(df, c) for c in chans])
    W = df.GVW.values
    rows = []
    for i in range(len(df)):
        cal = cal_mask_fn(i)
        if not cal.any():
            continue
        C = np.mean(I[cal] / W[cal, None], axis=0)
        S = Sig_of(df.iloc[i]) * df.v1.values[i] ** 2      # microstrain*m squared
        for kd in kinds:
            if kd == "mean-GVW":
                What, sdp = W[cal].mean(), np.nan
            elif kd == "GLS-resid":
                # Sigma from the scatter of the calibration crossings themselves
                # (residuals I - C W); needs more calibration runs than channels + 1
                if cal.sum() - 1 <= len(C):
                    continue
                Sr = np.cov((I[cal] - W[cal, None] * C).T)
                w = weights("GLS", C, Sr)
                What = w @ I[i]
                sdp = np.sqrt(w @ Sr @ w)
            else:
                w = weights(kd, C, S)
                What = w @ I[i]
                sdp = np.sqrt(w @ S @ w)
            rows.append(dict(scheme=label, estimator=kd, test=df.id.values[i],
                             truck=df.trucks.values[i], GVW=W[i], GVW_hat=What,
                             err_pct=100 * (What / W[i] - 1),
                             pred_sd_pct=100 * sdp / W[i],
                             w=json.dumps([round(float(x), 5) for x in w])
                             if kd != "mean-GVW" else ""))
    return pd.DataFrame(rows)


def summarise(E, seed):
    out = []
    for (sch, kd), g in E.groupby(["scheme", "estimator"], sort=False):
        e = g.err_pct.values
        mae = np.mean(np.abs(e))
        rms = np.sqrt(np.mean(e ** 2))
        mlo, mhi = boot_ci(e, lambda x: np.mean(np.abs(x)), seed=seed)
        rlo, rhi = boot_ci(e, lambda x: np.sqrt(np.mean(x ** 2)), seed=seed)
        out.append(dict(scheme=sch, estimator=kd, n=len(e), MAE=mae, MAE_lo=mlo,
                        MAE_hi=mhi, RMS=rms, RMS_lo=rlo, RMS_hi=rhi, bias=np.mean(e),
                        max_abs=np.max(np.abs(e)),
                        pred_sd_pct=np.sqrt(np.nanmean(g.pred_sd_pct ** 2))))
    return pd.DataFrame(out)


def paired_diff(E, sch, a, b, seed):
    ea = E[(E.scheme == sch) & (E.estimator == a)].set_index("test").err_pct
    eb = E[(E.scheme == sch) & (E.estimator == b)].set_index("test").err_pct
    ea, eb = ea.loc[eb.index].values, eb.values
    d = np.abs(ea) - np.abs(eb)
    lo, hi = boot_ci(d, np.mean, seed=seed)
    d2 = ea ** 2 - eb ** 2
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(ea), (NBOOT, len(ea)))
    drms = np.sqrt(np.mean(ea[idx] ** 2, 1)) - np.sqrt(np.mean(eb[idx] ** 2, 1))
    return d.mean(), lo, hi, (np.sqrt(np.mean(ea ** 2)) - np.sqrt(np.mean(eb ** 2)),
                              *np.percentile(drms, [2.5, 97.5]))


def task4(G, NZ):
    log("\n" + "=" * 78 + "\nTASK 4. Estimators, out-of-sample. C_j = mean(Ix_j/GVW) over "
        "calibration runs only; Sigma = covariance of vehicle-free integrals for the test "
        "run's window length (from quiet data, so it never contains the test run), scaled by "
        "v_test^2. Schemes: LOO = leave-one-run-out; LOTO = calibrate on one truck, test on "
        "the other; IN = in-sample (C from all runs incl. the test run) for comparison.")
    allE = []
    sets = [("d2A", 2, CH2, "day2 4ch"),
            ("d1A", 1, CH1, "day1 12ch"),
            ("d1A", 1, AVG1, "day1 wheel-path 4ch")]
    for g, day, chans, tag in sets:
        df = G[g]
        full = CH2 if day == 2 else CH1
        ii = [full.index(c) for c in chans]

        def Sig_of(e, day=day, ii=ii):
            Tw = int(round(e.T_win / 2) * 2)
            Z = NZ[day][Tw][:, ii]
            return np.cov(Z.T)
        kinds = ([f"single:{j}" for j in range(len(chans))] +
                 ["average", "GLS-diag", "GLS", "immune", "immune-eq", "GLS-resid",
                  "mean-GVW"])
        n = len(df)
        trucks = df.trucks.values
        for sch, fn in [("LOO", lambda i: np.arange(n) != i),
                        ("IN", lambda i: np.ones(n, bool)),
                        ("LOTO", lambda i: trucks != trucks[i])]:
            E = run_estimators(df, chans, Sig_of, kinds, fn, f"{tag} {sch}")
            E["estimator"] = E.estimator.apply(
                lambda k: f"single {chans[int(k.split(':')[1])]}" if k.startswith("single:")
                else k)
            allE.append(E)
    E = pd.concat(allE, ignore_index=True)
    # diagnostic: is the crossing-to-crossing scatter described by the quiet-data Sigma?
    log("\nDiagnostic: scatter of crossing residuals (I_j - C_j W, all runs) versus the "
        "vehicle-free noise covariance at each run's window and speed")
    diag_rows = []
    for g, day, chans, tag in sets:
        df = G[g]
        full = CH2 if day == 2 else CH1
        ii = [full.index(c) for c in chans]
        I = np.column_stack([Ix(df, c) for c in chans])
        W = df.GVW.values
        C = np.mean(I / W[:, None], axis=0)
        Rres = I - W[:, None] * C
        Sq = np.mean([np.cov(NZ[day][int(round(e.T_win / 2) * 2)][:, ii].T) * e.v1 ** 2
                      for _, e in df.iterrows()], axis=0)
        var_ratio = Rres.var(axis=0, ddof=1) / np.diag(Sq)
        Rc = np.corrcoef(Rres.T)
        Qc = Sq / np.sqrt(np.outer(np.diag(Sq), np.diag(Sq)))
        iu = np.triu_indices(len(chans), 1)
        log(f"{tag}: residual var / quiet var per channel: " +
            ", ".join(f"{c}={x:.2f}" for c, x in zip(chans, var_ratio)))
        log(f"   mean off-diag correlation: crossing residuals {Rc[iu].mean():.3f} "
            f"(range {Rc[iu].min():.2f} to {Rc[iu].max():.2f}) vs quiet noise "
            f"{Qc[iu].mean():.3f}")
        if len(chans) <= 4:
            log("   residual correlation matrix:")
            for c, rr in zip(chans, Rc):
                log(f"   {c:5s} " + " ".join(f"{x:6.2f}" for x in rr))
        # variance of the GLS(quiet) combination evaluated with the residual covariance
        Sr = np.cov(Rres.T)
        for kd in ["average", "GLS", "immune"]:
            w = weights(kd, C, Sq)
            log(f"   {kd:8s}: sd predicted by quiet Sigma {100*np.sqrt(w@Sq@w)/W.mean():5.1f}%"
                f", by crossing-residual covariance {100*np.sqrt(w@Sr@w)/W.mean():5.1f}%")
        diag_rows.append(dict(set=tag, mean_r_resid=Rc[iu].mean(), mean_r_quiet=Qc[iu].mean(),
                              **{f"varratio_{c}": x for c, x in zip(chans, var_ratio)}))
    pd.DataFrame(diag_rows).to_csv(os.path.join(RES, "v4_residual_vs_noise.csv"), index=False)
    E.to_csv(os.path.join(RES, "v4_estimator_errors.csv"), index=False)
    S = summarise(E, seed=RNG_SEED)
    S.to_csv(os.path.join(RES, "v4_estimators.csv"), index=False)
    for sch in S.scheme.unique():
        log(f"\n--- {sch}  (|error| % of GVW; 95% bootstrap CI over test runs)")
        log(f"{'estimator':14s} {'n':>2s} {'MAE':>6s} {'95% CI':>14s} {'RMS':>6s} "
            f"{'95% CI':>14s} {'bias':>6s} {'max':>6s} {'pred.sd':>7s}")
        for _, r in S[S.scheme == sch].iterrows():
            log(f"{r.estimator:14s} {r.n:2d} {r.MAE:6.1f} [{r.MAE_lo:5.1f},{r.MAE_hi:5.1f}] "
                f"{r.RMS:6.1f} [{r.RMS_lo:5.1f},{r.RMS_hi:5.1f}] {r.bias:+6.1f} "
                f"{r.max_abs:6.1f} {r.pred_sd_pct:7.1f}")
    # paired comparisons
    log("\nPaired bootstrap differences (LOO): mean(|e_a|-|e_b|) and RMS_a-RMS_b, 95% CI")
    pd_rows = []
    for tag, base in [("day2 4ch LOO", ["average", "single st36", "single st31"]),
                      ("day1 12ch LOO", ["average", "single ch11", "mean-GVW"]),
                      ("day1 wheel-path 4ch LOO", ["average", "single ch11", "mean-GVW"])]:
        for a in ["GLS", "immune"]:
            for b in base:
                d, lo, hi, (dr, rlo, rhi) = paired_diff(E, tag, a, b, RNG_SEED + 7)
                pd_rows.append(dict(scheme=tag, a=a, b=b, dMAE=d, dMAE_lo=lo, dMAE_hi=hi,
                                    dRMS=dr, dRMS_lo=rlo, dRMS_hi=rhi))
                log(f"{tag:24s} {a:7s} - {b:12s}: dMAE {d:+6.1f} [{lo:+6.1f},{hi:+6.1f}]  "
                    f"dRMS {dr:+6.1f} [{rlo:+6.1f},{rhi:+6.1f}]")
    pd.DataFrame(pd_rows).to_csv(os.path.join(RES, "v4_estimator_paired.csv"), index=False)
    # weights used (LOO, mean over folds)
    log("\nMean LOO weights (normalised so that sum |w_j C_j| reported as share):")
    for tag in ["day2 4ch LOO", "day1 wheel-path 4ch LOO", "day1 12ch LOO"]:
        for kd in ["GLS", "immune"]:
            ws = np.array([json.loads(s) for s in
                           E[(E.scheme == tag) & (E.estimator == kd)].w])
            log(f"  {tag:24s} {kd:7s} mean w = " + ", ".join(f"{x:+.4f}" for x in
                                                             ws.mean(0)))
    # per-run LOO errors day 2
    log("\nDay-2 LOO errors per run (%):")
    sub = E[E.scheme == "day2 4ch LOO"].pivot(index="test", columns="estimator",
                                               values="err_pct")
    log(sub.round(1).to_string())
    log("\nDay-1 LOO errors per run (%), 12-ch and wheel-path sets:")
    for tag in ["day1 12ch LOO", "day1 wheel-path 4ch LOO"]:
        sub = E[E.scheme == tag].pivot(index="test", columns="estimator", values="err_pct")
        log(tag)
        log(sub[[c for c in ["average", "GLS", "GLS-diag", "immune", "immune-eq",
                             "GLS-resid", "mean-GVW"] if c in sub.columns]]
            .round(1).to_string())
    return E, S


# =========================================================== task 5: lane, superposition
def task5(G, multi, NZ):
    log("\n" + "=" * 78 + "\nTASK 5. Lane effect (day 2, same trucks) and two-truck events")
    rows = []
    for c in CH2 + ["avg"]:
        a, b = Cper(G["d2A"], c), Cper(G["d2B"], c)
        w = welch_logratio(a, b)
        rng = np.random.default_rng(RNG_SEED + 11)
        bs = [np.mean(b[rng.integers(0, len(b), len(b))]) /
              np.mean(a[rng.integers(0, len(a), len(a))]) for _ in range(NBOOT)]
        rows.append(dict(channel=c, C_laneA=a.mean(), C_laneB=b.mean(),
                         B_over_A=b.mean() / a.mean(), ci95_lo=w["ci95_lo"],
                         ci95_hi=w["ci95_hi"], boot_lo=np.percentile(bs, 2.5),
                         boot_hi=np.percentile(bs, 97.5), p_diff=w["p_diff"],
                         CV_laneB=cv(b)))
    L = pd.DataFrame(rows)
    L.to_csv(os.path.join(RES, "v4_lane.csv"), index=False)
    log("C_B/C_A, 95% CI from Welch t on log|C| and from bootstrap of runs:")
    log(L.round(3).to_string())
    # superposition
    dA = G["d2A"]
    rows = []
    for _, e in multi[multi.lane == "A"].iterrows():
        Tw = int(round(e.T_win / 2) * 2)
        Z = NZ[2][Tw]
        for c in CH2 + ["avg"]:
            r = Cper(dA, c)
            Cm, Cse = r.mean(), r.std(ddof=1) / np.sqrt(len(r))
            pred = Cm * e.sum_W_over_v
            meas = e[f"Idt_{c}"]
            nsd = (Z.mean(axis=1) if c == "avg" else Z[:, CH2.index(c)]).std(ddof=1)
            q = meas / pred
            qsd = abs(q) * np.hypot(nsd / meas, Cse / Cm)
            rows.append(dict(event=e.id, channel=c, meas=meas, noise_sd=nsd, pred=pred,
                             ratio=q, ratio_sd=qsd, ci95_lo=q - 1.96 * qsd,
                             ci95_hi=q + 1.96 * qsd))
        # GLS total weight estimate with C, Sigma from the 8 single runs
        Iv = np.array([e[f"Idt_{c}"] for c in CH2])
        C = np.array([Cper(dA, c).mean() for c in CH2])
        S = np.cov(Z.T)
        w = weights("GLS", C, S)
        sumWv = w @ Iv                       # estimate of sum W_k/v_k
        vbar = e.GVW / e.sum_W_over_v
        rows.append(dict(event=e.id, channel="GLS", meas=sumWv, pred=e.sum_W_over_v,
                         ratio=sumWv / e.sum_W_over_v,
                         ratio_sd=np.sqrt(w @ S @ w) / e.sum_W_over_v,
                         ci95_lo=(sumWv - 1.96 * np.sqrt(w @ S @ w)) / e.sum_W_over_v,
                         ci95_hi=(sumWv + 1.96 * np.sqrt(w @ S @ w)) / e.sum_W_over_v,
                         noise_sd=np.nan))
        log(f"{e.id}: GLS estimate of total GVW = {sumWv*vbar:.1f} t (true {e.GVW:.1f} t, "
            f"{100*(sumWv*vbar/e.GVW-1):+.1f}%; noise-only 95% CI "
            f"[{(sumWv-1.96*np.sqrt(w@S@w))*vbar:.1f}, {(sumWv+1.96*np.sqrt(w@S@w))*vbar:.1f}] t)")
    SP = pd.DataFrame(rows)
    SP.to_csv(os.path.join(RES, "v4_superposition.csv"), index=False)
    log("measured / predicted (sum of single-truck constants), CI includes noise of the "
        "event integral and the SE of C (n = 8):")
    log(SP.round(3).to_string())
    for c in ["avg", "GLS"]:
        s = SP[SP.channel == c]
        wts = 1 / s.ratio_sd ** 2
        pm = np.sum(wts * s.ratio) / np.sum(wts)
        psd = 1 / np.sqrt(np.sum(wts))
        log(f"pooled M1+M2 ({c}): {pm:.3f} [{pm-1.96*psd:.3f}, {pm+1.96*psd:.3f}] "
            "(note: C uncertainty is shared between the two events, so this CI is slightly "
            "too narrow)")
    return L, SP


# =========================================================== figures
def figures(T1, S, E, SM, NZ, G):
    # invariance
    fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.2), gridspec_kw={"width_ratios": [13, 5]})
    for a, g in zip(axs, ["d1A", "d2A"]):
        sub = T1[T1.group == g]
        x = np.arange(len(sub))
        col = ["C3" if f == "FAIL" else ("C0" if f == "pass" else "C1") for f in sub.flag]
        a.errorbar(x, sub.ratio_B_over_A,
                   yerr=[sub.ratio_B_over_A - sub.ratio_ci95_lo,
                         sub.ratio_ci95_hi - sub.ratio_B_over_A], fmt="none", ecolor="0.4",
                   capsize=2)
        a.scatter(x, sub.ratio_B_over_A, c=col, s=14, zorder=3)
        for m, ls in [(0.05, "--"), (0.10, ":")]:
            a.axhspan(1 - m, 1 + m, color="0.85" if m == .05 else "0.93", zorder=0)
        a.axhline(1, color="k", lw=.6)
        a.set_xticks(x)
        a.set_xticklabels(sub.channel, rotation=90, fontsize=7)
        a.set_title("(a) Day 1: C(T2)/C(T1), both 3-axle" if g == "d1A" else
                    "(b) Day 2: C(5-axle)/C(3-axle)", fontsize=8, loc="left")
        a.set_ylabel("ratio of constants (95% CI)")
        a.set_ylim(0.4, 1.6)
    save(fig, "v4_invariance")
    # noise correlation
    fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.3), gridspec_kw={"width_ratios": [3, 2]})
    for a, day, chans in [(axs[0], 1, CH1), (axs[1], 2, CH2)]:
        R = np.corrcoef(NZ[day][NZ[day]["Tref"]].T)
        im = a.imshow(R, vmin=-1, vmax=1, cmap="RdBu_r")
        a.set_xticks(range(len(chans)))
        a.set_yticks(range(len(chans)))
        a.set_xticklabels(chans, rotation=90, fontsize=7)
        a.set_yticklabels(chans, fontsize=7)
        a.grid(False)
        a.set_title(f"Day {day}: correlation of vehicle-free integrals, "
                    f"T = {NZ[day]['Tref']} s", fontsize=7)
        if day == 2:
            for i in range(4):
                for j in range(4):
                    a.text(j, i, f"{R[i,j]:.2f}", ha="center", va="center", fontsize=7)
    fig.colorbar(im, ax=axs, shrink=0.8)
    fig.savefig(os.path.join(FIG, "v4_noise_corr.png"), dpi=300)
    fig.savefig(os.path.join(FIG, "v4_noise_corr.pdf"))
    plt.close(fig)
    # estimators (fixed x positions per estimator so schemes line up)
    fig, axs = plt.subplots(1, 3, figsize=(7.2, 3.2), sharey=False)
    for a, tag in zip(axs, ["day2 4ch", "day1 wheel-path 4ch", "day1 12ch"]):
        order = list(SM[SM.scheme == f"{tag} LOO"].estimator)
        if tag == "day1 12ch":
            order = [e for e in order if not e.startswith("single") or
                     e in ("single ch11", "single ch5")]
        pos = {e: k for k, e in enumerate(order)}
        for sch, mk, off in [("IN", "s", -0.2), ("LOO", "o", 0.0), ("LOTO", "^", 0.2)]:
            sub = SM[(SM.scheme == f"{tag} {sch}") & SM.estimator.isin(order)]
            x = np.array([pos[e] for e in sub.estimator]) + off
            a.errorbar(x, sub.MAE, yerr=[sub.MAE - sub.MAE_lo, sub.MAE_hi - sub.MAE],
                       fmt=mk, ms=3, capsize=1.5, label=sch)
        a.set_xticks(range(len(order)))
        a.set_xticklabels([e.replace("single ", "").replace("immune", "zero-sum") for e in order], rotation=90,
                          fontsize=6.5)
        a.set_title({"day2 4ch": "(a) Day 2, 4 gauges", "day1 wheel-path 4ch": "(b) Day 1, 4 wheel-path gauges",
                     "day1 12ch": "(c) Day 1, 12 gauges (2 singles shown)"}[tag], fontsize=8, loc="left")
        a.set_ylabel("MAE of GVW (%)")
        a.legend(fontsize=6)
    save(fig, "v4_estimators")
    # speed
    fig, axs = plt.subplots(1, 3, figsize=(7.2, 2.6))
    for a, (g, c) in zip(axs, [("d1A", "avg"), ("d1A", "ch1"), ("d2A", "avg")]):
        df = G[g]
        y = Cper(df, c)
        for tk, col in {"T1": "C0", "T2": "C1", "T3": "C2", "T4": "C3"}.items():
            m = df.trucks.values == tk
            if m.any():
                a.plot(df.v1.values[m], y[m], "o", color=col, ms=4, label=tk)
        r = S[(S.group == g) & (S.channel == c) & (S.model == "truck+v")].iloc[0]
        a.set_title(f"{'Day 1' if g == 'd1A' else 'Day 2'} {c}: slope|truck "
                    f"{r.slope_pct_10ms:+.0f} [{r.ci95_lo:+.0f},{r.ci95_hi:+.0f}] %/10 m/s",
                    fontsize=6.5)
        a.set_xlabel("speed (m/s)")
        a.set_ylabel(r"$C$ ($\mu\varepsilon$ m/t)")
        a.legend(fontsize=6)
    save(fig, "v4_speed")


# =========================================================== main
def load_raw(F):
    raw = {}
    for day, loader, chans, fs, ref in [(2, nio.load_strains200, CH2, 200, "st40"),
                                        (1, nio.load_allstrain, CH1, 100, "ch4")]:
        df = loader()
        Y = {c: nio.GAIN * df[c].values for c in chans}
        busy = nf.detect_all(Y[ref], fs)          # same detector as nb_field
        step = fs // 20
        Yd = {c: Y[c][::step] for c in chans}     # 20 Hz, as nb_field.noise_integrals
        raw[day] = (Yd, 20, busy, len(df) / fs)
        del df, Y
    return raw


def main():
    os.makedirs(RES, exist_ok=True)
    os.makedirs(FIG, exist_ok=True)
    F, G, multi = load_events()
    log("nb_v4.py: NOR-BWIM v4 re-analysis. Runs used: "
        + "; ".join(f"{g}: {', '.join(G[g].id)}" for g in G)
        + f"; multi: {', '.join(multi.id)}")
    T1 = task1(G)
    S = task2(G)
    raw = load_raw(F)
    NZ = task3(raw, G)
    E, SM = task4(G, NZ)
    task5(G, multi, NZ)
    figures(T1, S, E, SM, NZ, G)
    log("\nwritten results/v4_*.csv, figures/v4_*.png/.pdf")


if __name__ == "__main__":
    LOG = open(LOGP, "w")
    main()
