"""Tests (a)-(f) on the crossing integrals of the Smart Road Bridge field records.
Input: results/events_field.csv (from nb_field.py). Run: python3 -I nb_tests.py
"""
import os
import sys
import json
import numpy as np
import pandas as pd
from scipy.stats import chi2
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import nb_beam as bm   # noqa: E402

RES = os.path.join(HERE, "results")
FIG = os.path.join(HERE, "figures")
os.makedirs(FIG, exist_ok=True)
LOG = open(os.path.join(HERE, "logs", "tests.log"), "w")
plt.rcParams.update({"font.size": 8, "axes.grid": True, "grid.alpha": .3,
                     "savefig.dpi": 300, "figure.dpi": 100})


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")
    LOG.flush()


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name + ".png"), dpi=300)
    fig.savefig(os.path.join(FIG, name + ".pdf"))
    plt.close(fig)


F = pd.read_csv(os.path.join(RES, "events_field.csv"))
CH2 = ["st40", "st36", "st34", "st31", "avg"]
CH1 = [f"ch{k}" for k in range(1, 13)] + ["avg"]
GAP = 6.019   # st40-st31 distance (m) from nb_field log

# ------------------------------------------------------------ speed QC (lane B)
F["v_lag"] = np.where(F.lag_40_31.abs() > 0.05, GAP / F.lag_40_31.abs(), np.nan)
F["v1"] = F.v_used.apply(lambda s: json.loads(s)[0])
F["v_fit_corr"] = F.v_fit / 1.139
F["speed_flag"] = (np.abs(F.v1 - F.v_fit_corr) / F.v1 > 0.2)
# exclusions (documented in the report)
EXCL = {"R5": "Truck 2 (R10) enters 43 s later; low global-shape fit r2=0.60",
        "R6": "Truck 1 crossed 15.7 s earlier (both on bridge)",
        "R10": "Truck 1 (R5) still on bridge at entry; r2=0.55",
        "X1": "extra pass, weight not documented", "X1r": "extra pass",
        "X2": "extra pass", "X2r": "extra pass"}
for i, r in F.iterrows():
    if r.speed_flag and r.id not in EXCL:
        EXCL[r.id] = (f"speed inconsistent: used {r.v1:.1f} m/s vs corrected low-pass "
                      f"fit {r.v_fit_corr:.1f} m/s")
F["excluded"] = F.id.map(lambda k: EXCL.get(k, ""))
log("Exclusions:")
for k, v in EXCL.items():
    log(f"  {k}: {v}")
log(F[["id", "lane", "v1", "v_src", "v_lag", "v_fit_corr", "v_script"]].round(2)
    .to_string())


def ratios(df, c):
    r = df[f"Idt_{c}"] * df.v1 / df.GVW
    s = df[f"noise_sd_Idt_{c}"] * df.v1 / df.GVW
    return r.values, s.values


def stats(r, s):
    w = 1 / s ** 2
    mw = np.sum(w * r) / np.sum(w)
    chi = np.sum(((r - mw) / s) ** 2)
    n = len(r)
    return dict(n=n, mean=np.mean(r), sd=np.std(r, ddof=1),
                cv=np.std(r, ddof=1) / abs(np.mean(r)),
                cv_noise=np.sqrt(np.mean(s ** 2)) / abs(np.mean(r)),
                wmean=mw, wmean_se=np.sqrt(1 / np.sum(w)),
                chi2=chi, p=chi2.sf(chi, n - 1))


single = F[~F.trucks.str.contains(r"\+") & (F.excluded == "")]
G = {
    "day1_laneA_T1T2": (single[(single.day == 1)], CH1),
    "day2_laneA_T3T4": (single[(single.day == 2) & (single.lane == "A")], CH2),
    "day2_laneB_T3T4": (single[(single.day == 2) & (single.lane == "B")], CH2),
}

# ------------------------------------------------------------ per-run table
rows = []
for gname, (df, chans) in G.items():
    for c in chans:
        r, s = ratios(df, c)
        for (_, e), ri, si in zip(df.iterrows(), r, s):
            rows.append(dict(group=gname, channel=c, id=e.id, truck=e.trucks,
                             axles=5 if e.trucks == "T4" else 3, GVW=e.GVW, v=e.v1,
                             Idx=e[f"Idt_{c}"] * e.v1, Idx_noise_sd=e[f"noise_sd_Idt_{c}"] * e.v1,
                             Idx_per_t=ri, Idx_per_t_sd=si))
RUN = pd.DataFrame(rows)
RUN.to_csv(os.path.join(RES, "integrals_per_run.csv"), index=False)

# ------------------------------------------------------------ (a) invariance
inv = []
for gname, (df, chans) in G.items():
    for c in chans:
        r, s = ratios(df, c)
        st = stats(r, s)
        st.update(group=gname, channel=c)
        if gname == "day2_laneA_T3T4":       # 3-axle vs 5-axle
            m3 = df.trucks.values == "T3"
            a, b = stats(r[m3], s[m3]), stats(r[~m3], s[~m3])
            st.update(T3_mean=a["wmean"], T3_se=a["wmean_se"], T4_mean=b["wmean"],
                      T4_se=b["wmean_se"], T4_over_T3=b["wmean"] / a["wmean"],
                      T4_over_T3_se=abs(b["wmean"] / a["wmean"]) * np.hypot(
                          b["wmean_se"] / b["wmean"], a["wmean_se"] / a["wmean"]))
        if gname == "day1_laneA_T1T2":
            m1 = df.trucks.values == "T1"
            a, b = stats(r[m1], s[m1]), stats(r[~m1], s[~m1])
            st.update(T1_mean=a["wmean"], T1_se=a["wmean_se"], T2_mean=b["wmean"],
                      T2_se=b["wmean_se"], T2_over_T1=b["wmean"] / a["wmean"])
        inv.append(st)
INV = pd.DataFrame(inv)
INV.to_csv(os.path.join(RES, "test_a_invariance.csv"), index=False)
log("\n(a) invariance of Idx/GVW (microstrain*m/t)")
log(INV.round(3).to_string())

# cross-day check on the same gauge st40 (= ch4 on day 1)
d1 = G["day1_laneA_T1T2"][0]
d2 = G["day2_laneA_T3T4"][0]
r1, s1 = ratios(d1, "ch4")
r2, s2 = ratios(d2, "st40")
allr = np.concatenate([r1, r2])
alls = np.concatenate([s1, s2])
st = stats(allr, alls)
log(f"\nst40 pooled day1(T1,T2)+day2 laneA(T3,T4): n={st['n']} mean={st['mean']:.3f} "
    f"CV={st['cv']:.3f} (noise-expected {st['cv_noise']:.3f}) chi2 p={st['p']:.3f}")
s1d, s2d = stats(r1, s1), stats(r2, s2)
log(f"  day1 ch4 wmean {s1d['wmean']:.3f}+-{s1d['wmean_se']:.3f};  day2 st40 wmean "
    f"{s2d['wmean']:.3f}+-{s2d['wmean_se']:.3f}")
POOL = dict(n=st["n"], mean=st["mean"], cv=st["cv"], cv_noise=st["cv_noise"], p=st["p"],
            day1=s1d["wmean"], day1_se=s1d["wmean_se"], day2=s2d["wmean"],
            day2_se=s2d["wmean_se"])

# ------------------------------------------------------------ (b) SLM
slm = []
for gname, (df, chans) in list(G.items()) + [("st40_both_days", (None, ["st40"]))]:
    for c in chans:
        if gname == "st40_both_days":
            dd = pd.concat([d1.assign(_c="ch4"), d2.assign(_c="st40")])
            I = np.array([e[f"Idt_{e._c}"] * e.v1 for _, e in dd.iterrows()])
        else:
            dd = df
            I = (dd[f"Idt_{c}"] * dd.v1).values
        W = dd.GVW.values
        ids = dd.id.values
        trk = dd.trucks.values
        for i in range(len(dd)):
            for j in range(len(dd)):
                if i == j:
                    continue
                Wp = W[i] * I[j] / I[i]
                slm.append(dict(group=gname, channel=c, ref=ids[i], ref_truck=trk[i],
                                test=ids[j], test_truck=trk[j], GVW=W[j], GVW_pred=Wp,
                                err_pct=100 * (Wp / W[j] - 1),
                                cross_truck=trk[i] != trk[j]))
SLM = pd.DataFrame(slm)
SLM.to_csv(os.path.join(RES, "test_b_slm_pairs.csv"), index=False)
summ = SLM.groupby(["group", "channel", "cross_truck"]).err_pct.agg(
    n="size", MAE=lambda x: np.mean(np.abs(x)), RMSE=lambda x: np.sqrt(np.mean(x ** 2)),
    median_abs=lambda x: np.median(np.abs(x)), max_abs=lambda x: np.max(np.abs(x))
).reset_index()
summ.to_csv(os.path.join(RES, "test_b_slm_summary.csv"), index=False)
log("\n(b) SLM single-reference errors (%)")
log(summ.round(2).to_string())

# calibration with all runs of one truck -> other truck
cal = []
for gname, a, b in [("day2_laneA_T3T4", "T3", "T4"), ("day2_laneA_T3T4", "T4", "T3"),
                    ("day1_laneA_T1T2", "T1", "T2"), ("day1_laneA_T1T2", "T2", "T1")]:
    df, chans = G[gname]
    for c in chans:
        r, s = ratios(df, c)
        m = df.trucks.values == a
        cref = np.mean(r[m])
        Ipred = (df[f"Idt_{c}"] * df.v1).values[~m] / cref
        e = 100 * (Ipred / df.GVW.values[~m] - 1)
        for idv, ee, wp, wt in zip(df.id.values[~m], e, Ipred, df.GVW.values[~m]):
            cal.append(dict(group=gname, channel=c, calib=a, test=idv, GVW=wt,
                            GVW_pred=wp, err_pct=ee))
# cross-day: calibrate on day 1 ch4 (T1,T2) -> predict day-2 lane-A st40 (T3,T4)
cref = np.mean(r1)
for (_, e), rr in zip(d2.iterrows(), r2):
    cal.append(dict(group="crossday_st40", channel="st40", calib="day1 T1+T2",
                    test=e.id, GVW=e.GVW, GVW_pred=rr * e.GVW / cref,
                    err_pct=100 * (rr / cref - 1)))
CAL = pd.DataFrame(cal)
CAL.to_csv(os.path.join(RES, "test_b_slm_truck_calibration.csv"), index=False)
cs = CAL.groupby(["group", "channel", "calib"]).err_pct.agg(
    n="size", mean="mean", MAE=lambda x: np.mean(np.abs(x)),
    RMSE=lambda x: np.sqrt(np.mean(x ** 2))).reset_index()
cs.to_csv(os.path.join(RES, "test_b_slm_truck_calibration_summary.csv"), index=False)
log("\n(b2) SLM calibrated on all runs of one truck, applied to the other (%)")
log(cs.round(2).to_string())

# ------------------------------------------------------------ (c) speed
spd = []
for gname in ["day1_laneA_T1T2", "day2_laneA_T3T4"]:
    df, chans = G[gname]
    for c in chans:
        r, s = ratios(df, c)
        v = df.v1.values
        A = np.vstack([np.ones_like(v), v - v.mean()]).T
        w = 1 / s ** 2
        Aw = A * np.sqrt(w)[:, None]
        coef, *_ = np.linalg.lstsq(Aw, r * np.sqrt(w), rcond=None)
        cov = np.linalg.inv(Aw.T @ Aw)
        spd.append(dict(group=gname, channel=c, mean=coef[0],
                        slope_pct_per_10ms=1000 * coef[1] / coef[0],
                        slope_se_pct_per_10ms=1000 * np.sqrt(cov[1, 1]) / abs(coef[0]),
                        v_min=v.min(), v_max=v.max()))
SPD = pd.DataFrame(spd)
SPD.to_csv(os.path.join(RES, "test_c_speed.csv"), index=False)
log("\n(c) speed: weighted regression of Idx/GVW on v")
log(SPD.round(2).to_string())

# ------------------------------------------------------------ (d) lane
lane = []
for c in CH2:
    ra, sa = ratios(G["day2_laneA_T3T4"][0], c)
    rb, sb = ratios(G["day2_laneB_T3T4"][0], c)
    A, B = stats(ra, sa), stats(rb, sb)
    q = B["wmean"] / A["wmean"]
    lane.append(dict(channel=c, laneA=A["wmean"], laneA_se=A["wmean_se"], nA=A["n"],
                     laneB=B["wmean"], laneB_se=B["wmean_se"], nB=B["n"], B_over_A=q,
                     B_over_A_se=abs(q) * np.hypot(A["wmean_se"] / A["wmean"],
                                                    B["wmean_se"] / B["wmean"]),
                     cv_laneB=B["cv"], cv_noise_laneB=B["cv_noise"], p_laneB=B["p"]))
LANE = pd.DataFrame(lane)
LANE.to_csv(os.path.join(RES, "test_d_lane.csv"), index=False)
log("\n(d) lane effect (day 2, same trucks): C_B / C_A")
log(LANE.round(3).to_string())

# ------------------------------------------------------------ (e) superposition
sup = []
multi = F[F.trucks.str.contains(r"\+")]
for _, e in multi.iterrows():
    gl = "day2_laneA_T3T4" if e.lane == "A" else "day2_laneB_T3T4"
    for c in CH2:
        r, s = ratios(G[gl][0], c)
        st = stats(r, s)
        pred = st["wmean"] * e.sum_W_over_v          # microstrain*s
        meas = e[f"Idt_{c}"]
        sd = e[f"noise_sd_Idt_{c}"]
        sdp = st["wmean_se"] * e.sum_W_over_v
        # SLM-type total GVW of the pair, using the lane constant
        vbar = e.GVW / e.sum_W_over_v                 # weight-harmonic mean speed
        W_hat = meas * vbar / st["wmean"]
        sup.append(dict(event=e.id, lane=e.lane, channel=c, v=e.v_used,
                        Idt_meas=meas, Idt_meas_sd=sd, Idt_pred_sum=pred, Idt_pred_sd=sdp,
                        meas_over_pred=meas / pred,
                        meas_over_pred_sd=abs(meas / pred) * np.hypot(sd / meas, sdp / pred),
                        GVW_true=e.GVW, GVW_hat=W_hat, err_pct=100 * (W_hat / e.GVW - 1)))
SUP = pd.DataFrame(sup)
SUP.to_csv(os.path.join(RES, "test_e_superposition.csv"), index=False)
log("\n(e) multiple-truck events: measured vs sum of single-truck predictions")
log(SUP.round(3).to_string())

# ------------------------------------------------------------ (f) observability
obs_rows = []
models = {"uniform EI": bm.model(False, 2.0), "haunch n=2": bm.model(True, 2.0),
          "haunch n=2.5": bm.model(True, 2.5)}
fig, ax = plt.subplots(3, 1, figsize=(7.2, 7.6), sharex=True)
for k, (name, m) in enumerate(models.items()):
    xm, M, _ = bm.udl_moment(m)
    eps = bm.strain_proxy(m, xm, M)
    z = bm.zero_moment_points(xm, M)
    Ms = np.interp(bm.X_SENSOR, xm, M)
    es = np.interp(bm.X_SENSOR, xm, eps)
    gx = bm.X_SENSOR + np.array([-3, -1, 1, 3.0])      # 4 gauges 2 m apart, centred
    gr = np.interp(gx, xm, eps) / es
    x_il, il = bm.moment_il(m)
    obs_rows.append(dict(model=name, M_q_sensor=Ms, int_IL=np.trapezoid(il, x_il),
                         theorem_rel_err=np.trapezoid(il, x_il) / Ms - 1,
                         zeros=json.dumps([round(float(v), 1) for v in z]),
                         zeros_span2=json.dumps([round(float(v), 1) for v in z
                                                 if 86.5 < v < 230.5]),
                         gauge_ratio_min=gr.min(), gauge_ratio_max=gr.max()))
    ax[0].plot(xm, M / Ms, lw=1, label=name)
    ax[1].plot(xm, eps / es, lw=1, label=name)
    if name == "haunch n=2":
        for v in z:
            for a in ax:
                a.axvline(v, color="0.6", lw=0.5, ls=":")
OBS = pd.DataFrame(obs_rows)
OBS.to_csv(os.path.join(RES, "test_f_model.csv"), index=False)
log("\n(f) beam model")
log(OBS.to_string())

# observability map: GVW standard error for a single crossing (W = 25 t) for a sensor
# at x on the top slab, scaled by the measured mid-span constant and measured noise
m = models["haunch n=2"]
xm, M, _ = bm.udl_moment(m)
eps = bm.strain_proxy(m, xm, M)
es = np.interp(bm.X_SENSOR, xm, eps)
noise = {}
for lab, df, c, cconst in [("day 1 (st40=ch4)", d1, "ch4", s1d["wmean"]),
                           ("day 2 (st40)", d2, "st40", s2d["wmean"])]:
    sdx = np.median(df[f"noise_sd_Idt_{c}"] * df.v1)
    noise[lab] = sdx
    C = cconst * eps / es
    rel = 100 * sdx / (np.abs(C) * 25.0)
    ax[2].semilogy(xm, rel, lw=1, label=f"{lab}: noise sd {sdx:.1f} microstrain m")
    for thr in (5, 10):
        bad = xm[rel > thr]
        log(f"  {lab}: |sigma_W/W| > {thr}% over {np.sum(np.diff(xm)[:len(rel)-1][rel[:-1] > thr]):.1f} m "
            f"of {bm.LTOT} m")
    obs_rows.append(dict(model=lab, noise_sd_Idx=sdx, C_mid=cconst,
                         rel_err_at_sensor_pct=100 * sdx / (abs(cconst) * 25)))
for a in ax:
    for e in bm.EDGES:
        a.axvline(e, color="k", lw=0.6)
    a.axvline(bm.X_SENSOR, color="r", lw=1)
ax[0].set_ylabel(r"$M_q(x)/M_q(x_s)$")
ax[1].set_ylabel(r"$C_\varepsilon(x)/C_\varepsilon(x_s)$ (top fibre)")
ax[2].set_ylabel(r"$\sigma_W/W$ (%) for W = 25 t")
ax[2].set_xlabel("x along bridge (m); red = gauges (mid-span 2), dotted = zero-moment points")
ax[2].axhline(5, color="0.5", lw=0.5)
ax[2].axhline(10, color="0.5", lw=0.5)
ax[2].set_ylim(0.5, 1000)
ax[0].legend(fontsize=7)
ax[2].legend(fontsize=7)
save(fig, "fig6_observability_model")
pd.DataFrame(obs_rows).to_csv(os.path.join(RES, "test_f_model.csv"), index=False)

# measured ratios between gauges (model-free shape check)
gr = []
for gname, ref in [("day2_laneA_T3T4", "st40"), ("day2_laneB_T3T4", "st40"),
                   ("day1_laneA_T1T2", "ch4")]:
    df, chans = G[gname]
    for c in chans:
        q = df[f"Idt_{c}"].values / df[f"Idt_{ref}"].values
        gr.append(dict(group=gname, channel=c, ref=ref, ratio_mean=np.mean(q),
                       ratio_sd=np.std(q, ddof=1), ratio_se=np.std(q, ddof=1) / np.sqrt(len(q)),
                       n=len(q), model_ratio_beam="1.000 (same section, top slab)"))
GR = pd.DataFrame(gr)
GR.to_csv(os.path.join(RES, "test_f_gauge_ratios.csv"), index=False)
log("\n(f) measured integral ratios between gauges")
log(GR.round(3).to_string())

# ------------------------------------------------------------ figures
# Fig 2: invariance
fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.0))
for a, (gname, c, title) in zip(axs, [("day1_laneA_T1T2", "ch4", "Day 1, gauge st40 (=ch4)"),
                                      ("day2_laneA_T3T4", "st40", "Day 2, gauge st40, lane A")]):
    df = G[gname][0]
    r, s = ratios(df, c)
    cols = {"T1": "C0", "T2": "C1", "T3": "C2", "T4": "C3"}
    for k, (_, e) in enumerate(df.iterrows()):
        a.errorbar(k, r[k], yerr=s[k], fmt="o", color=cols[e.trucks], ms=4, capsize=2)
    st = stats(r, s)
    a.axhline(st["wmean"], color="k", lw=0.8)
    a.set_xticks(range(len(df)))
    a.set_xticklabels([f"{e.id}\n{e.trucks}\n{e.v1:.0f} m/s" for _, e in df.iterrows()],
                      fontsize=6)
    a.set_title(f"{title}\nCV={100*st['cv']:.1f}% (noise-expected {100*st['cv_noise']:.1f}%)",
                fontsize=8)
    a.set_ylabel(r"$\int\varepsilon\,dx$ / GVW  ($\mu\varepsilon\cdot$m/t)")
save(fig, "fig2_invariance")

# Fig 3: SLM errors
fig, ax = plt.subplots(figsize=(4.5, 3.4))
lim = [15, 32]
for gname, mk, c in [("day1_laneA_T1T2", "o", "ch4"), ("day2_laneA_T3T4", "s", "st40"),
                     ("day2_laneA_T3T4", "^", "avg")]:
    sub = SLM[(SLM.group == gname) & (SLM.channel == c)]
    ax.plot(sub.GVW + np.random.default_rng(0).uniform(-.15, .15, len(sub)), sub.GVW_pred,
            mk, ms=3, alpha=.6, label=f"{gname} {c}")
ax.plot(lim, lim, "k", lw=.8)
ax.set_xlabel("GVW, weigh station (t)")
ax.set_ylabel("GVW predicted by SLM (t)")
ax.legend(fontsize=6)
ax.set_ylim(0, 70)
save(fig, "fig3_slm")

# Fig 4: speed
fig, axs = plt.subplots(1, 2, figsize=(7.2, 2.8))
for a, (gname, c) in zip(axs, [("day1_laneA_T1T2", "avg"), ("day2_laneA_T3T4", "avg")]):
    df = G[gname][0]
    r, s = ratios(df, c)
    for tk, col in {"T1": "C0", "T2": "C1", "T3": "C2", "T4": "C3"}.items():
        mm = df.trucks.values == tk
        if mm.any():
            a.errorbar(df.v1.values[mm], r[mm], yerr=s[mm], fmt="o", color=col, ms=4,
                       capsize=2, label=tk)
    a.set_xlabel("speed (m/s)")
    a.set_ylabel(r"$\int\varepsilon dx$/GVW, gauge average")
    a.set_title(gname, fontsize=8)
    a.legend(fontsize=7)
save(fig, "fig4_speed")

# Fig 5: lane and superposition
fig, axs = plt.subplots(1, 2, figsize=(7.2, 2.8))
a = axs[0]
xx = np.arange(len(CH2))
a.bar(xx - 0.2, LANE.laneA, 0.4, yerr=LANE.laneA_se, label="lane A (gauge lane)")
a.bar(xx + 0.2, LANE.laneB, 0.4, yerr=LANE.laneB_se, label="lane B (other lane)")
a.set_xticks(xx)
a.set_xticklabels(CH2)
a.set_ylabel(r"$C$ ($\mu\varepsilon\cdot$m/t)")
a.legend(fontsize=7)
a = axs[1]
for k, (ev, g) in enumerate(SUP[SUP.channel == "avg"].groupby("event")):
    a.errorbar(k, g.meas_over_pred.values[0], yerr=g.meas_over_pred_sd.values[0], fmt="o")
a.axhline(1, color="k", lw=.8)
a.set_xticks(range(len(SUP.event.unique())))
a.set_xticklabels(sorted(SUP.event.unique()))
a.set_ylabel("measured / sum of single-truck (gauge avg)")
save(fig, "fig5_lane_superposition")

log("\nPOOL", json.dumps({k: float(v) for k, v in POOL.items()}))
log("noise", json.dumps({k: float(v) for k, v in noise.items()}))
F.to_csv(os.path.join(RES, "events_field_qc.csv"), index=False)
