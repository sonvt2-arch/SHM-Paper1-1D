"""WP4: field dynamic deflection records (Gie Cuc I, Phuong Do) - events, baseline drift,
quasi-static integral.  Run from the repo root:  python3 code/analysis/wp4_dynamic_records.py

Sign convention: records are deflection y (mm, downward negative).  Everything below is
done on s = -y (downward positive), so the integral of a crossing is positive.
Truck weight, speed, lane and girder for these runs are NOT known [NEED VALUE]; nothing here
uses them except in the clearly flagged "illustrative reference" columns.
"""
import logging
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfiltfilt
from scipy.integrate import cumulative_trapezoid

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FS = 200.0
DT = 1.0 / FS
T_REC = 15.0

os.makedirs(os.path.join(ROOT, "code/analysis/logs"), exist_ok=True)
os.makedirs(os.path.join(ROOT, "figures"), exist_ok=True)
logging.basicConfig(level=logging.INFO, format="%(message)s", handlers=[
    logging.FileHandler(os.path.join(ROOT, "code/analysis/logs/wp4.log"), mode="w"),
    logging.StreamHandler()])
log = logging.getLogger("wp4")

# ---------------------------------------------------------------- inputs (from INVENTORY.md)
BRIDGES = {
    "gie-cuc-1": dict(
        L=25.7, L_calc=25.0, I=0.32909, E=31.5e6, wheelbase=3.37 + 1.35, wb1=3.37, wb2=1.35, P_nom_t=27.5,
        f1={"N1": 5.573, "N2": 5.871, "N3": 6.012}, IM={"N1": 1.152, "N2": 1.114, "N3": 1.122},
        files={"N1": "dynamic_deflection_N1_midspan_200Hz.csv",
               "N2": "dynamic_deflection_N2_midspan_200Hz.csv",
               "N3": "dynamic_deflection_N3_midspan_200Hz.csv"},
        cols=("Vong0_mm_raw", "Vong_mm_processed")),
    "phuong-do": dict(
        L=17.5, L_calc=17.5, I=0.08324, E=29.939483e6, wheelbase=3.9 + 1.36, wb1=3.9, wb2=1.36, P_nom_t=24.0,
        f1={"N1": 5.184, "N2": 5.552}, IM={"N1": 1.126, "N2": 1.095},
        files={"N1": "vong_dong_N1_midspan_deflection_timehistory.csv",
               "N2": "vong_dong_N2_midspan_deflection_timehistory.csv"},
        cols=("Vong0_mm", "Vong_mm")),
}
G = 9.80665


def sos_filter(y, fc, kind, order=4):
    sos = butter(order, fc, btype=kind, fs=FS, output="sos")
    return sosfiltfilt(sos, y)


def movavg(x, w):
    k = np.ones(w) / w
    return np.convolve(np.pad(x, (w // 2, w - 1 - w // 2), mode="edge"), k, mode="valid")


def integ(x, t0, t1, t):
    m = (t >= t0) & (t <= t1)
    return float(np.trapezoid(x[m], t[m]))


# ---------------------------------------------------------------- event detection
def detect_events(t, s):
    sm = movavg(s, 41)  # 0.2 s
    hist, edges = np.histogram(sm, bins=np.arange(sm.min() - 0.05, sm.max() + 0.15, 0.1))
    b0 = 0.5 * (edges[np.argmax(hist)] + edges[np.argmax(hist) + 1])
    dev = sm - b0
    thr = max(0.1 * np.max(np.abs(dev)), 0.15)
    on = np.abs(dev) > thr
    idx = np.flatnonzero(on)
    ev = []
    if idx.size:
        starts = [idx[0]]
        ends = []
        gap = int(0.6 * FS)
        for a, b in zip(idx[:-1], idx[1:]):
            if b - a > gap:
                ends.append(a)
                starts.append(b)
        ends.append(idx[-1])
        for i0, i1 in zip(starts, ends):
            if (i1 - i0) * DT >= 0.5:
                ev.append((i0, i1))
    return sm, b0, thr, ev


def quiet_mask(t, ev, pad=0.3):
    q = np.ones(t.size, bool)
    for i0, i1 in ev:
        q[max(0, i0 - int(pad * FS)):i1 + int(pad * FS) + 1] = False
    return q


def level(t, s, q, ta, tb, minn=40):
    m = q & (t >= ta) & (t <= tb)
    if m.sum() < minn:
        return np.nan, np.nan
    return float(np.median(s[m])), float(t[m].mean())


def eta_mid(x, L):
    """Mid-span deflection influence line of a simply supported prismatic beam, peak-normalised."""
    u = np.clip(x / L, 0.0, 1.0)
    u = np.minimum(u, 1.0 - u)
    out = 3 * u - 4 * u ** 3
    out[(x < 0) | (x > L)] = 0.0
    return out


def truck_model(t, v, t0, A, L, axles):
    """axles: list of (weight fraction, distance behind front axle in m)."""
    return A * sum(w * eta_mid(v * (t - t0) - d, L) for w, d in axles)


def fit_speed(t, d, L, axles, tw0, tw1, t_guess):
    from scipy.optimize import least_squares
    m = (t >= tw0) & (t <= tw1)
    tt, dd = t[m], d[m]
    best = None
    for v0 in (6.0, 10.0, 14.0, 18.0, 24.0):
        x0 = [v0, t_guess, max(dd.max(), 0.1)]
        try:
            r = least_squares(lambda p: truck_model(tt, p[0], p[1], p[2], L, axles) - dd, x0,
                              bounds=([2.0, t_guess - 1.5, 0.01], [40.0, t_guess + 1.5, 100.0]))
        except Exception:
            continue
        if best is None or r.cost < best.cost:
            best = r
    if best is None:
        return np.nan, np.nan, np.nan, np.nan
    rms = float(np.sqrt(np.mean(best.fun ** 2)))
    return best.x[0], best.x[1], best.x[2], rms / max(dd.max(), 1e-9)


def analyse_record(bridge, span, chan, t, y, det=None):
    s = -y
    cfg = BRIDGES[bridge]
    sm, b0, thr, ev = det if det is not None else detect_events(t, s)
    q = quiet_mask(t, ev)
    tare = float(np.median(s[: int(0.5 * FS)]))
    # whole-record polynomial baseline from quiet samples (deg 3) and HP filters
    p = np.polyfit(t[q], s[q], 3) if q.sum() > 200 else None
    s_hp01 = sos_filter(s, 0.1, "highpass", 2)
    s_hp05 = sos_filter(s, 0.5, "highpass", 2)
    s_lp = {fc: sos_filter(s, fc, "lowpass", 4) for fc in (1.0, 2.0, 3.0)}
    # block scatter of quiet levels (0.5 s blocks) -> empirical eps0 scale
    # pooled scatter of 0.5 s block medians about each inter-event quiet segment's own mean
    # (so that a pre/post step is NOT counted as scatter)
    blocks = []
    nb = int(0.5 * FS)
    ends_i = [i1 for _, i1 in ev]
    for k in range(0, t.size - nb + 1, nb):
        mm = q[k:k + nb]
        if mm.all():
            blocks.append((sum(e < k for e in ends_i), np.median(s[k:k + nb])))
    res_ = []
    for gk in set(b[0] for b in blocks):
        v_ = np.array([b[1] for b in blocks if b[0] == gk])
        if len(v_) > 1:
            res_ += list(v_ - v_.mean())
    eps_q = float(np.sqrt(np.sum(np.square(res_)) / max(len(res_) - 1, 1))) if len(res_) > 3 else np.nan
    slope = float(np.polyfit(t[q], s[q], 1)[0]) if q.sum() > 200 else np.nan
    peaks = [np.max(np.abs(sm[i0:i1 + 1] - b0)) for i0, i1 in ev]
    pmax = max(peaks) if peaks else 0
    wts = (0.2, 0.4, 0.4)  # axle load fractions of the static-test truck (5.5/11/11 t, 4.8/9.6/9.6 t)
    axles = [(wts[0], 0.0), (wts[1], cfg["wb1"]),
             (wts[2], cfg["wb1"] + cfg["wb2"])]
    rows, lp_rows, store = [], [], []
    for n, (i0, i1) in enumerate(ev, 1):
        t0, t1 = t[i0], t[i1]
        ta, tb = max(t[0], t0 - 0.3), min(t[-1], t1 + 0.3)
        trunc_s, trunc_e = i0 <= int(0.3 * FS), i1 >= t.size - 1 - int(0.3 * FS)
        pre, tpre = level(t, s, q, t0 - 2.5, t0 - 0.3)
        post, tpost = level(t, s, q, t1 + 0.3, t1 + 2.5)
        have_b = not (np.isnan(pre) or np.isnan(post))
        if have_b:
            base_b = pre + (post - pre) * (t - tpre) / (tpost - tpre)
        else:
            base_b = np.full(t.size, np.nan)
        base_a = np.full(t.size, tare)
        base_c = np.polyval(p, t) if p is not None else np.full(t.size, np.nan)
        ref = base_b if have_b else base_a
        # downward main lobe relative to reference baseline
        d = movavg(s - ref, 21)
        seg = slice(i0, i1 + 1)
        ipk = i0 + int(np.argmax(d[seg]))
        pk = d[ipk]
        major = peaks[n - 1] >= 0.25 * pmax
        # T10: contiguous region around the peak with d >= 10 % of the peak
        j0 = ipk
        while j0 > 0 and d[j0] >= 0.1 * pk:
            j0 -= 1
        j1 = ipk
        while j1 < t.size - 1 and d[j1] >= 0.1 * pk:
            j1 += 1
        T10 = (t[j1] - t[j0])
        T10_ok = (j0 > 0) and (j1 < t.size - 1) and major
        # half-height width
        h0 = ipk
        while h0 > 0 and d[h0] >= 0.5 * pk:
            h0 -= 1
        h1 = ipk
        while h1 < t.size - 1 and d[h1] >= 0.5 * pk:
            h1 += 1
        T50 = t[h1] - t[h0]
        T10 = max(T10, DT)
        vA = 0.933 * cfg["L"] / T10 * 3.6 if T10_ok else np.nan   # point-load IL, 10 % level
        vB = 0.653 * cfg["L"] / max(T50, DT) * 3.6                  # point-load IL, half height
        # model fit to low-pass (2 Hz) downward lobe
        dlp = s_lp[2.0] - ref
        vf = vfp = np.nan
        fit_rms = np.nan
        tf0 = np.nan
        Af = np.nan
        if T10_ok and major and not (trunc_s or trunc_e):
            tw0, tw1 = t[j0] - 0.3, t[j1] + 0.3
            vf_, tf0, Af, fit_rms = fit_speed(t, dlp, cfg["L"], axles, tw0, tw1, t[j0])
            vf = vf_ * 3.6
            vfp_, _, _, _ = fit_speed(t, dlp, cfg["L"], [(1.0, 0.0)], tw0, tw1, t[j0])
            vfp = vfp_ * 3.6
        I = {}
        I["a_raw"] = integ(s - base_a, ta, tb, t)
        I["b_linear"] = integ(s - base_b, ta, tb, t) if have_b else np.nan
        I["c1_poly3"] = integ(s - base_c, ta, tb, t)
        I["c2_hp0.1Hz"] = integ(s_hp01, ta, tb, t)
        I["c3_hp0.5Hz"] = integ(s_hp05, ta, tb, t)
        I["pre_only"] = integ(s - pre, ta, tb, t) if not np.isnan(pre) else np.nan
        Iref = I["b_linear"] if have_b else np.nan
        Twin = tb - ta
        r = dict(bridge=bridge, span=span, channel=chan, event=n, major=major,
                 trunc_start=trunc_s, trunc_end=trunc_e, t_start_s=round(t0, 3), t_end_s=round(t1, 3),
                 peak_down_mm=round(pk, 3), t_peak_s=round(t[ipk], 3),
                 peak_up_mm=round(float(np.max(-(s - ref)[seg])), 3),
                 T10_s=round(T10, 3), T50_s=round(T50, 3), T10_complete=T10_ok,
                 v_kmh_IL10=round(vA, 1) if T10_ok else np.nan,
                 v_kmh_IL50=round(vB, 1) if T10_ok else np.nan,
                 v_kmh_fit_3axle=round(vf, 1), v_kmh_fit_pointload=round(vfp, 1),
                 fit_rms_over_peak=round(fit_rms, 3), A_fit_mm=round(Af, 3) if Af == Af else np.nan,
                 pre_level_mm=round(pre, 3), post_level_mm=round(post, 3),
                 eps0_prepost_mm=round(post - pre, 3) if have_b else np.nan,
                 window_s=round(Twin, 3))
        for k, v in I.items():
            r["I_" + k] = round(v, 3)
        if have_b:
            for k in I:
                if k != "b_linear":
                    r["dev_pct_" + k] = round(100 * (I[k] - Iref) / Iref, 1)
            eps_eff = (I["a_raw"] - Iref) / Twin
            r["eps0_eff_mm"] = round(eps_eff, 3)
            r["bias_paper_Trec15_pct"] = round(100 * abs(eps_eff) * T_REC / abs(Iref), 1)
            r["eps0_quiet_scatter_mm"] = round(eps_q, 3)
            r["bias_quietscatter_Trec15_pct"] = round(100 * eps_q * T_REC / abs(Iref), 1)
        r["quiet_slope_mm_per_s"] = round(slope, 4)
        rows.append(r)
        # low-pass block
        for fc, sl in s_lp.items():
            Ilp = integ(sl - ref, ta, tb, t)
            Iun = integ(s - ref, ta, tb, t)
            res = (s - sl)
            lp_rows.append(dict(bridge=bridge, span=span, channel=chan, event=n, major=major,
                                baseline="b_linear" if have_b else "a_tare(only)", fc_Hz=fc,
                                fc_over_f1=round(fc / cfg["f1"][span], 2),
                                I_unfiltered=round(Iun, 3), I_lowpass=round(Ilp, 3),
                                ratio_LP_over_unfiltered=round(Ilp / Iun, 4),
                                I_dynamic_residual=round(integ(res, ta, tb, t), 3),
                                I_abs_residual=round(integ(np.abs(res), ta, tb, t), 3),
                                cancellation_net_over_abs=round(abs(integ(res, ta, tb, t)) /
                                                                 integ(np.abs(res), ta, tb, t), 3),
                                peak_unfilt_mm=round(float(np.max((s - ref)[seg])), 3),
                                peak_lowpass_mm=round(float(np.max((sl - ref)[seg])), 3),
                                peak_ratio=round(float(np.max((s - ref)[seg]) / np.max((sl - ref)[seg])), 3),
                                IM_reported=cfg["IM"][span]))
        store.append(dict(n=n, i0=i0, i1=i1, ta=ta, tb=tb, base_a=base_a, base_b=base_b, base_c=base_c,
                          pre=(tpre, pre), post=(tpost, post), major=major, T10=(t[j0], t[j1])))
    info = dict(b0=b0, thr=thr, tare=tare, eps_q=eps_q, slope=slope, q=q, s_hp01=s_hp01,
                s_hp05=s_hp05, s_lp=s_lp, ev=store, sm=sm)
    return rows, lp_rows, info


def main():
    all_rows, all_lp, infos, data = [], [], {}, {}
    for br, cfg in BRIDGES.items():
        for span, f in cfg["files"].items():
            d = pd.read_csv(os.path.join(ROOT, "data/bridges", br, f))
            t = d["time_ms"].values / 1000.0
            det = detect_events(t, -d[cfg["cols"][1]].values.astype(float))  # events defined on 'Vong' (proc)
            for chan, col in zip(("raw", "proc"), cfg["cols"]):
                y = d[col].values.astype(float)
                data[(br, span, chan)] = (t, y)
                rows, lp, info = analyse_record(br, span, chan, t, y, det)
                all_rows += rows
                all_lp += lp
                infos[(br, span, chan)] = info
                log.info(f"[{br} {span} {chan}] samples={t.size} ymin={y.min():.3f} ymax={y.max():.3f} "
                         f"mode_baseline(s)={info['b0']:.3f} thr={info['thr']:.3f} tare0={info['tare']:.3f} "
                         f"quiet_block_scatter={info['eps_q']:.3f} mm quiet_slope={info['slope']:.4f} mm/s "
                         f"events={len(rows)}")
    ev = pd.DataFrame(all_rows)
    lp = pd.DataFrame(all_lp)
    pd.set_option("display.width", 250, "display.max_columns", 60)
    for br in BRIDGES:
        ev[ev.bridge == br].drop(columns="bridge").to_csv(
            os.path.join(ROOT, "data/bridges", br, "wp4_events_baseline.csv"), index=False)
        lp[lp.bridge == br].drop(columns="bridge").to_csv(
            os.path.join(ROOT, "data/bridges", br, "wp4_lowpass.csv"), index=False)
    log.info("\n=== EVENTS / SPEED ===")
    log.info(ev[["bridge", "span", "channel", "event", "major", "trunc_start", "trunc_end", "t_start_s", "t_end_s",
                 "peak_down_mm", "peak_up_mm", "T10_s", "T50_s", "T10_complete", "v_kmh_IL10", "v_kmh_IL50", "v_kmh_fit_3axle", "v_kmh_fit_pointload", "fit_rms_over_peak"]].to_string())
    log.info("\n=== BASELINE ===")
    bc = [c for c in ev.columns if c.startswith(("I_", "dev_", "eps0", "bias", "pre_", "post_"))]
    log.info(ev[["bridge", "span", "channel", "event", "major"] + bc].to_string())
    log.info("\n=== LOW-PASS (fc=2 Hz) ===")
    log.info(lp[lp.fc_Hz == 2.0].drop(columns=["bridge"]).to_string())
    log.info("\n=== LOW-PASS fc sweep, major events, ratio ===")
    log.info(lp[lp.major].pivot_table(index=["bridge", "span", "channel", "event"], columns="fc_Hz",
                                     values="ratio_LP_over_unfiltered").to_string())

    # ---------------------------------------------------------- channel relation and whole-record totals
    log.info("\n=== Vong (processed) vs Vong0 (raw): least-squares  Vong = k*Vong0 + c, over the major-event window "
             "(PD N1 excluded after the 7.2 s step) ===")
    scl, tot = [], []
    for br, cfg in BRIDGES.items():
        for span in cfg["files"]:
            t, yr = data[(br, span, "raw")]
            _, yp = data[(br, span, "proc")]
            m = np.ones(t.size, bool)
            if br == "phuong-do" and span == "N1":
                m = t < 7.15
            k, c = np.polyfit(yr[m], yp[m], 1)
            r = np.corrcoef(yr[m], yp[m])[0, 1]
            scl.append(dict(bridge=br, span=span, k=round(k, 3), c_mm=round(c, 3), corr=round(r, 4),
                            rng_raw_mm=round(np.ptp(yr), 2), rng_proc_mm=round(np.ptp(yp), 2)))
            for chan in ("raw", "proc"):
                t, y = data[(br, span, chan)]
                s_ = -y
                inf = infos[(br, span, chan)]
                tare = inf["tare"]
                q = inf["q"]
                pc = np.polyfit(t[q], s_[q], 3)
                I_t = float(np.trapezoid(s_ - tare, t))
                I_p = float(np.trapezoid(s_ - np.polyval(pc, t), t))
                tot.append(dict(bridge=br, span=span, channel=chan, T_record_s=T_REC,
                                I_whole_record_tare_mm_s=round(I_t, 2), I_whole_record_poly3_mm_s=round(I_p, 2),
                                diff_pct=round(100 * (I_t - I_p) / I_p, 1) if abs(I_p) > 1e-9 else np.nan,
                                eps0_equiv_mm=round((I_t - I_p) / T_REC, 3)))
    scl = pd.DataFrame(scl)
    tot = pd.DataFrame(tot)
    log.info(scl.to_string())
    log.info("\n=== Whole 15 s record integral: tare-only vs quiet-sample poly3 baseline ===")
    log.info(tot.to_string())
    for br in BRIDGES:
        scl[scl.bridge == br].to_csv(os.path.join(ROOT, "data/bridges", br, "wp4_channel_scale.csv"), index=False)
        tot[tot.bridge == br].to_csv(os.path.join(ROOT, "data/bridges", br, "wp4_record_totals.csv"), index=False)

    # ---------------------------------------------------------- consistency (task 4)
    cons = []
    for _, r in ev[(ev.major) & (~ev.trunc_start) & (~ev.trunc_end) & ev.T10_complete & ev.v_kmh_fit_3axle.notna()].iterrows():
        cfg = BRIDGES[r.bridge]
        Iref = r.I_b_linear
        if np.isnan(Iref):
            continue
        EI = cfg["E"] * cfg["I"]
        Cm = 5 * cfg["L_calc"] ** 4 / (384 * EI)  # m^2/kN (m per kN/m)
        Pnom = cfg["P_nom_t"] * G  # kN
        PCm_mm_m = Pnom * Cm * 1e3  # mm*m
        for vname, v in (("v_fit", r.v_kmh_fit_3axle / 3.6), ("v_nom30", 30 / 3.6),
                         ("v_nom35", 35 / 3.6), ("v_nom40", 40 / 3.6)):
            cons.append(dict(bridge=r.bridge, span=r.span, channel=r.channel, event=r.event, speed_source=vname,
                             v_ms=round(v, 2), I_b_mm_s=Iref, v_times_I_mm_m=round(v * Iref, 2),
                             ref_P_Cm_mm_m_if_static_truck_full_share=round(PCm_mm_m, 1),
                             implied_share_if_static_truck=round(v * Iref / PCm_mm_m, 3)))
    cons = pd.DataFrame(cons)
    for br in BRIDGES:
        cons[cons.bridge == br].drop(columns="bridge").to_csv(
            os.path.join(ROOT, "data/bridges", br, "wp4_consistency.csv"), index=False)
    log.info("\n=== CONSISTENCY v*I (complete major events, baseline b) ===")
    log.info(cons.to_string())
    summ = []
    for (br, ch, vs), g in cons.groupby(["bridge", "channel", "speed_source"]):
        # all events and largest-event-per-span
        big = ev.set_index(["bridge", "span", "channel", "event"])
        gg = g.copy()
        gg["peak"] = [big.loc[(br, a, ch, e), "peak_down_mm"] for a, e in zip(gg.span, gg.event)]
        top = gg.loc[gg.groupby("span")["peak"].idxmax()]
        for lab, x in (("all complete major events", gg), ("largest event per span", top)):
            v = x.v_times_I_mm_m.values
            summ.append(dict(bridge=br, channel=ch, speed_source=vs, set=lab, n=len(v), mean=v.mean(),
                             sd=v.std(ddof=1) if len(v) > 1 else np.nan,
                             cv_pct=100 * v.std(ddof=1) / v.mean() if len(v) > 1 else np.nan,
                             min=v.min(), max=v.max()))
    summ = pd.DataFrame(summ).round(2)
    for br in BRIDGES:
        summ[summ.bridge == br].to_csv(os.path.join(ROOT, "data/bridges", br, "wp4_consistency_summary.csv"),
                                       index=False)
    log.info("\n=== CONSISTENCY SUMMARY ===")
    log.info(summ.to_string())

    # ---------------------------------------------------------- figures
    make_figures(data, infos, ev, lp, cons)
    pd_lobe(data, infos)


def make_figures(data, infos, ev, lp, cons):
    keys = list(data.keys())
    spans = [(b, s) for b in BRIDGES for s in BRIDGES[b]["files"]]
    # fig 1: records with events
    fig, axs = plt.subplots(len(spans), 1, figsize=(12, 2.6 * len(spans)), sharex=True)
    for ax, (b, s) in zip(axs, spans):
        for chan, c, lab in (("raw", "tab:blue", "Vong0 (raw)"), ("proc", "tab:orange", "Vong (processed)")):
            t, y = data[(b, s, chan)]
            ax.plot(t, y, lw=0.7, color=c, label=lab)
        inf = infos[(b, s, "proc")]
        for e in inf["ev"]:
            ax.axvspan(data[(b, s, "proc")][0][e["i0"]], data[(b, s, "proc")][0][e["i1"]],
                       color="0.85" if not e["major"] else "tab:green", alpha=0.25)
        ax.set_ylabel("y (mm)")
        ax.set_title(f"{b} {s} (shaded: detected events on 'proc', green = major)", fontsize=9, loc="left")
        ax.grid(alpha=0.3)
    axs[0].legend(ncol=2, fontsize=8)
    axs[-1].set_xlabel("time (s)")
    fig.tight_layout()
    fig.savefig(os.path.join(ROOT, "figures/wp4_records_events.png"), dpi=130)
    plt.close(fig)

    # fig 2: baselines per major event (raw channel and proc, first complete event each) - grid
    sel = ev[ev.major]
    n = len(sel)
    cols = 3
    fig, axs = plt.subplots(int(np.ceil(n / cols)), cols, figsize=(15, 2.9 * int(np.ceil(n / cols))))
    axs = np.atleast_1d(axs).ravel()
    for ax, (_, r) in zip(axs, sel.iterrows()):
        t, y = data[(r.bridge, r.span, r.channel)]
        s = -y
        e = [x for x in infos[(r.bridge, r.span, r.channel)]["ev"] if x["n"] == r.event][0]
        m = (t >= e["ta"] - 1) & (t <= e["tb"] + 1)
        ax.plot(t[m], s[m], "k", lw=0.8, label="s=-y")
        ax.plot(t[m], e["base_a"][m], "tab:red", lw=1, label="(a) tare")
        if not np.isnan(e["base_b"]).all():
            ax.plot(t[m], e["base_b"][m], "tab:blue", lw=1.2, label="(b) linear pre/post")
        ax.plot(t[m], e["base_c"][m], "tab:green", lw=1, ls="--", label="(c1) poly3")
        ax.plot(t[m], infos[(r.bridge, r.span, r.channel)]["s_hp01"][m], color="tab:purple", lw=0.7, alpha=0.7,
                label="(c2) HP 0.1 Hz signal")
        ax.set_title(f"{r.bridge} {r.span} {r.channel} ev{r.event}  dev(a)={r.get('dev_pct_a_raw', np.nan)}%",
                     fontsize=8)
        ax.grid(alpha=0.3)
    axs[0].legend(fontsize=6)
    for ax in axs[n:]:
        ax.axis("off")
    fig.supxlabel("time (s)")
    fig.supylabel("downward deflection s (mm)")
    fig.tight_layout()
    fig.savefig(os.path.join(ROOT, "figures/wp4_baseline_methods.png"), dpi=120)
    plt.close(fig)

    # fig 3: integral deviation bars
    sel = ev[ev.major & ev.I_b_linear.notna()].copy()
    meths = ["a_raw", "c1_poly3", "c2_hp0.1Hz", "c3_hp0.5Hz", "pre_only"]
    fig, ax = plt.subplots(figsize=(13, 4.5))
    w = 0.16
    x = np.arange(len(sel))
    for k, mth in enumerate(meths):
        ax.bar(x + (k - 2) * w, sel["dev_pct_" + mth].values, w, label=mth)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{r.bridge[:3]} {r.span}\n{r.channel} e{r.event}" for _, r in sel.iterrows()],
                       fontsize=7)
    ax.set_ylabel("integral deviation vs (b) linear pre/post (%)")
    ax.axhline(0, color="k", lw=0.5)
    ax.legend(fontsize=7, ncol=3)
    ax.set_ylim(-150, 150)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(ROOT, "figures/wp4_integral_sensitivity.png"), dpi=130)
    plt.close(fig)

    # fig 4: low-pass
    sel = ev[ev.major].drop_duplicates(["bridge", "span", "channel"])
    sel = sel[sel.channel == "proc"]
    fig, axs = plt.subplots(len(sel), 2, figsize=(13, 2.7 * len(sel)))
    for k, (_, r) in enumerate(sel.iterrows()):
        t, y = data[(r.bridge, r.span, r.channel)]
        inf = infos[(r.bridge, r.span, r.channel)]
        e = [x for x in inf["ev"] if x["n"] == r.event][0]
        ref = e["base_b"] if not np.isnan(e["base_b"]).all() else e["base_a"]
        s = -y
        sl = inf["s_lp"][2.0]
        m = (t >= e["ta"] - 1) & (t <= e["tb"] + 1)
        axs[k, 0].plot(t[m], (s - ref)[m], "k", lw=0.8, label="unfiltered (baseline b)")
        axs[k, 0].plot(t[m], (sl - ref)[m], "tab:red", lw=1.2, label="low-pass 2 Hz")
        axs[k, 0].set_title(f"{r.bridge} {r.span} proc ev{r.event}", fontsize=8)
        axs[k, 1].plot(t[m], (s - sl)[m], "tab:blue", lw=0.8)
        axs[k, 1].axhline(0, color="k", lw=0.4)
        lr = lp[(lp.bridge == r.bridge) & (lp.span == r.span) & (lp.channel == "proc") & (lp.event == r.event) &
                (lp.fc_Hz == 2.0)].iloc[0]
        axs[k, 1].set_title(f"dynamic residual: net/abs integral = {lr.cancellation_net_over_abs}, "
                            f"I_LP/I = {lr.ratio_LP_over_unfiltered}", fontsize=8)
        for a in axs[k]:
            a.grid(alpha=0.3)
    axs[0, 0].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(ROOT, "figures/wp4_lowpass.png"), dpi=120)
    plt.close(fig)

    # fig 5: consistency
    c = cons[cons.speed_source == "v_fit"]
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))
    for ax, br in zip(axs, BRIDGES):
        for chan, mk in (("raw", "o"), ("proc", "s")):
            g = c[(c.bridge == br) & (c.channel == chan)]
            ax.scatter([f"{r.span}-e{r.event}" for _, r in g.iterrows()], g.v_times_I_mm_m, marker=mk, s=45,
                       label=chan)
        ref = c[c.bridge == br].ref_P_Cm_mm_m_if_static_truck_full_share
        if len(ref):
            ax.axhline(ref.iloc[0], color="k", ls=":", label="P*C_m, static-test truck, 100% share (illustrative)")
        ax.set_title(f"{br}: v*I per complete event (v from duration)", fontsize=9)
        ax.set_ylabel("v * integral (mm*m)")
        ax.grid(alpha=0.3)
        ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(ROOT, "figures/wp4_consistency.png"), dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------- task 5: Phuong Do N1 lobe
def pd_lobe(data, infos):
    log.info("\n=== TASK 5: Phuong Do N1 positive lobe ===")
    t, raw = data[("phuong-do", "N1", "raw")]
    _, proc = data[("phuong-do", "N1", "proc")]
    corr = proc - raw
    dstep = np.diff(proc)
    k = int(np.argmax(np.abs(dstep)))
    log.info(f"Largest single-sample step in Vong (processed): {dstep[k]:.3f} mm between t={t[k]:.3f}s and "
             f"{t[k+1]:.3f}s (values {proc[k]:.3f} -> {proc[k+1]:.3f}); next largest |step| = "
             f"{np.sort(np.abs(dstep))[-2]:.3f} mm")
    log.info(f"Vong0: pre level {np.median(raw[:200]):.3f}, post level (last 3 s) {np.median(raw[-600:]):.3f}; "
             f"Vong post level {np.median(proc[-600:]):.3f}")
    log.info(f"Vong0 max {raw.max():.3f} at {t[np.argmax(raw)]:.3f}s; Vong max {proc.max():.3f} at "
             f"{t[np.argmax(proc)]:.3f}s; Vong0 min {raw.min():.3f}; Vong min {proc.min():.3f}")
    # lobe under several baselines (deflection y, upward positive part)
    inf = infos[("phuong-do", "N1", "raw")]
    e = [x for x in inf["ev"] if x["major"]][0]
    ta, tb = e["ta"], e["tb"]
    m = (t >= ta) & (t <= tb)
    rows = []
    ipk_dn = int(np.argmin(raw))
    t_step = float(t[ipk_dn + np.argmax(raw[ipk_dn:] >= 0.5 * (np.median(raw[-600:]) + np.median(raw[:200])))])
    step_base = np.where(t < t_step, np.median(raw[:200]), np.median(raw[-600:]))
    log.info(f"Vong0 first reaches the mid-level of the pre/post step after its minimum at t_step = {t_step:.3f} s; "
             f"plateau values: raw[5.75-6.0 s] median = {np.median(raw[(t>=5.75)&(t<=6.0)]):.3f}, "
             f"raw[7.25-7.5 s] median = {np.median(raw[(t>=7.25)&(t<=7.5)]):.3f}")
    cases = {
        "Vong0, step baseline at t_step (pre->post)": raw - step_base,
        "Vong0, tare (no correction)": raw - np.median(raw[:100]),
        "Vong0, linear pre/post (b)": raw + e["base_b"],  # base_b is in s-units: y - (-base) -> raw + base_b
        "Vong0, poly3 (c1)": raw + e["base_c"],
        "Vong0, HP 0.1 Hz": -inf["s_hp01"],
        "Vong (processed, as delivered)": proc - np.median(proc[:100]),
    }
    for lab, yy in cases.items():
        up = yy[m].max()
        lobe = np.clip(yy[m], 0, None)
        down = np.clip(yy[m], None, 0)
        rows.append(dict(case=lab, max_up_mm=round(up, 3), t_up_s=round(t[m][np.argmax(yy[m])], 3),
                         min_down_mm=round(yy[m].min(), 3),
                         ratio_up_over_down=round(up / abs(yy[m].min()), 3),
                         int_pos_mm_s=round(float(np.trapezoid(lobe, t[m])), 3),
                         int_neg_mm_s=round(float(np.trapezoid(down, t[m])), 3),
                         int_net_mm_s=round(float(np.trapezoid(yy[m], t[m])), 3)))
    # timing: downward lobe T10 vs time of positive lobe
    t10 = e["T10"]
    log.info(f"Downward lobe (10% level) from {t10[0]:.3f} to {t10[1]:.3f} s (T10={t10[1]-t10[0]:.3f}); event window "
             f"{ta:.2f}-{tb:.2f}")
    tab = pd.DataFrame(rows)
    tab.to_csv(os.path.join(ROOT, "data/bridges/phuong-do/wp4_n1_lobe.csv"), index=False)
    log.info(tab.to_string())

    # ---- raw acceleration DAT0034 = N2 only
    a = pd.read_csv(os.path.join(ROOT, "data/bridges/phuong-do/N2_DAT0034_raw_accel_ch2-4.csv"))
    ta_ = a["time_ms"].values / 1000.0
    acc = a["ch2_vertical_colC_mm_s2"].values.astype(float)
    accD = a["ch2_colD_unlabelled"].values.astype(float)
    log.info(f"\nDAT0034 ch2 vertical: mean={acc.mean():.2e}, std={acc.std():.4f}, |max|={np.abs(acc).max():.3f}, "
             f"distinct values={len(np.unique(acc))}, quantum~{np.min(np.diff(np.unique(acc))):.4f} (units as labelled: mm/s^2)")
    t2, raw2 = data[("phuong-do", "N2", "raw")]
    _, proc2 = data[("phuong-do", "N2", "proc")]
    # reference acceleration from Vong0 (N2): second derivative of 8 Hz low-passed displacement (mm -> mm/s^2)
    ref_disp = sos_filter(raw2, 8.0, "lowpass", 4)
    ref_acc = np.gradient(np.gradient(ref_disp, DT), DT)
    out = []
    fig, axs = plt.subplots(4, 1, figsize=(12, 11))
    for fcut in (0.3, 0.5, 1.0):
        accz = acc - acc.mean()
        v = cumulative_trapezoid(accz, dx=DT, initial=0)
        v = sos_filter(v, fcut, "highpass", 2)
        x = cumulative_trapezoid(v, dx=DT, initial=0)
        x = sos_filter(x, fcut, "highpass", 2)
        xr = sos_filter(raw2, fcut, "highpass", 2)
        kfit = float(np.dot(x, xr) / np.dot(x, x))
        cc = float(np.corrcoef(x, xr)[0, 1])
        out.append(dict(hp_Hz=fcut, rms_x_from_acc_mm=round(float(np.std(x)), 5), rms_Vong0_hp_mm=round(float(np.std(xr)), 4),
                        scale_fit=round(kfit, 1), corr=round(cc, 3)))
        if fcut == 0.5:
            axs[1].plot(t2, xr, "k", lw=0.8, label=f"Vong0 N2 HP {fcut} Hz")
            axs[1].plot(t2, x * kfit, "tab:red", lw=0.8, label=f"double-integrated DAT0034 x fit {kfit:.0f} (corr {cc:.2f})")
            axs[1].legend(fontsize=7)
            axs[1].set_ylabel("mm")
    log.info("Double integration of DAT0034 ch2 vs HP-filtered Vong0 N2:\n" + pd.DataFrame(out).to_string())
    # spectral content: fraction of accel energy below 2 Hz vs reference acceleration
    from numpy.fft import rfft, rfftfreq
    f = rfftfreq(acc.size, DT)
    Pa = np.abs(rfft(acc - acc.mean())) ** 2
    Pr = np.abs(rfft(ref_acc - ref_acc.mean())) ** 2
    log.info(f"Energy fraction below 2 Hz: DAT0034 ch2 = {Pa[f < 2].sum()/Pa.sum():.3f}; "
             f"second derivative of Vong0 N2 = {Pr[f < 2].sum()/Pr.sum():.3f}")
    # rms of reference acc in 0-2 Hz band vs measured acc in same band
    band = lambda z: sos_filter(z, 2.0, "lowpass", 4)
    log.info(f"RMS acc 0-2 Hz: DAT0034 = {np.std(band(acc)):.4f}; from Vong0 N2 (mm/s^2) = {np.std(band(ref_acc)):.3f}; "
             f"ratio = {np.std(band(ref_acc))/np.std(band(acc)):.1f}")
    pd.DataFrame(out).to_csv(os.path.join(ROOT, "data/bridges/phuong-do/wp4_n2_accel_reintegration.csv"), index=False)
    # figure
    axs[0].plot(ta_, acc, "k", lw=0.5, label="DAT0034 ch2 (as labelled mm/s^2)")
    axs[0].plot(t2, band(ref_acc), "tab:blue", lw=0.8, label="d2/dt2 of Vong0 N2, 0-2 Hz")
    axs[0].legend(fontsize=7)
    axs[0].set_ylabel("acc")
    t1_, r1 = data[("phuong-do", "N1", "raw")]
    t1p, r1p = data[("phuong-do", "N1", "proc")]
    axs[2].plot(t1_, r1, label="N1 Vong0 (raw)", lw=0.9)
    axs[2].plot(t1p, r1p, label="N1 Vong (processed)", lw=0.9)
    axs[2].plot(t1_, -e["base_b"], "k--", lw=0.8, label="linear pre/post baseline")
    axs[2].axvline(t[k], color="r", ls=":", label="step in Vong")
    axs[2].legend(fontsize=7)
    axs[2].set_ylabel("y (mm)")
    axs[3].plot(t1_, r1 + e["base_b"], label="N1 Vong0 - linear baseline", lw=0.9)
    axs[3].plot(t1_, r1 + e["base_c"], label="N1 Vong0 - poly3", lw=0.9)
    axs[3].plot(t1_, -inf["s_hp01"], label="N1 Vong0 HP 0.1 Hz", lw=0.9)
    axs[3].axhline(0, color="k", lw=0.4)
    axs[3].legend(fontsize=7)
    axs[3].set_ylabel("y (mm)")
    axs[3].set_xlabel("time (s)")
    for a_ in axs:
        a_.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(ROOT, "figures/wp4_pd_n1_lobe.png"), dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    main()
