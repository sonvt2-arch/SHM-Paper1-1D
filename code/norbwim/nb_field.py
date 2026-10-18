"""Smart Road Bridge field records (NOR-BWIM, figshare 26880898): event isolation,
speed, direction, baseline removal and crossing integrals of strain.

Run:  python3 -I nb_field.py      (writes results/events_field.csv, logs/field.log)
"""
import os
import sys
import json
import numpy as np
import pandas as pd
from scipy.ndimage import median_filter
from scipy.signal import find_peaks

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import nb_io as nio      # noqa: E402
import nb_events as ev   # noqa: E402
import nb_beam as bm     # noqa: E402

# The log file is opened only when this file is run as a script (see __main__ below), so
# importing nb_field from another script no longer truncates logs/field.log.
LOG = None


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    if LOG is not None:
        LOG.write(s + "\n")
        LOG.flush()


# ---------------------------------------------------------------- truck metadata
# Dissertation (Moghadam 2022, hdl:10919/111390) Table 2.1 and Sec. 2.2.3.
# Axle spacings AS (m) measured with tape; GVW from off-road weigh station.
TRUCKS = {
    # Truck 3: 3-axle hired truck, GVW 26.8 t; front 7.2 t, rear tandem 19.6 t (text)
    "T3": dict(n=3, AS=[4.78, 1.32], GVW=26.8, axw=[7.2, 9.8, 9.8]),
    # Truck 4: 5-axle, GVW 25.9 t; front 5.2, middle tandem 11.0, rear tandem 9.7 t
    "T4": dict(n=5, AS=[6.17, 1.32, 10.62, 1.24], GVW=25.9,
               axw=[5.2, 5.5, 5.5, 4.85, 4.85]),
    # Trucks 1, 2: 3-axle construction trucks; per-run GVW from Table 2.4
    "T1": dict(n=3, AS=[4.24, 1.37], GVW=None, axw=None),
    "T2": dict(n=3, AS=[4.19, 1.35], GVW=None, axw=None),
}
# Table 2.4 "Actual weight (ton)" for Runs 1-10 (Trucks 1 and 2)
GVW_T24 = {1: 22.82, 2: 22.51, 3: 22.45, 4: 22.18, 5: 22.30,
           6: 22.86, 7: 22.10, 8: 21.17, 9: 21.61, 10: 22.00}
# Speeds hard-coded in mainSmartRoadBridgeNORBWIM.mlx (Tests 1-8 = GPS-based for
# Trucks 3/4; Evaluations 1-10 = estimated for Trucks 1/2), m/s
V_SCRIPT = {"R15": 23.07, "R16": 22.94, "R17": 13.8, "R18": 13.29,
            "R11": 27.91, "R12": 28.16, "R13": 17.1, "R14": 16.56,
            "R1": 10.48, "R2": 12.11, "R3": 11.28, "R4": 12.19, "R5": 12.12,
            "R6": 19.9, "R7": 19.96, "R8": 19.66, "R9": 19.9, "R10": 18.99}


def axles(tk):
    return np.concatenate([[0.0], np.cumsum(TRUCKS[tk]["AS"])])


# ---------------------------------------------------------------- event list
# Day 2 = 2020-09-30, Strains200Hz.dat (200 Hz; st40, st36, st34, st31).
# Index = sample index in Strains200Hz.dat at which the automatic detector fired.
# Mapping of script Tests 1-8 (DataWed.csv rows + 299458) to detected events; Test k
# of the script = Truck 4 (k=1..4) and Truck 3 (k=5..8) = Runs 15-18 and 11-14.
D2 = [
    # id, idx, vehicles [(truck, label)], lane class, note
    ("R15", 314280, ["T4"], "A", "script Test 1"),
    ("R15r", 334540, ["T4"], "B", "return trip after Test 1 (same truck)"),
    ("R16", 373960, ["T4"], "A", "script Test 2"),
    ("R16r", 393560, ["T4"], "B", "return"),
    ("R17", 434720, ["T4"], "A", "script Test 3"),
    ("R17r", 458540, ["T4"], "B", "return"),
    ("R18", 487300, ["T4"], "A", "script Test 4"),
    ("R18r", 510380, ["T4"], "B", "return"),
    ("R11", 610720, ["T3"], "A", "script Test 5"),
    ("R11r", 628920, ["T3"], "B", "return"),
    ("X1r", 661700, ["T3?"], "B", "extra pass, not in script/tables"),
    ("X1", 679840, ["T3?"], "A", "extra pass, not in script/tables"),
    ("R12", 714820, ["T3"], "A", "script Test 6"),
    ("R12r", 733200, ["T3"], "B", "return"),
    ("X2r", 768220, ["T3?"], "B", "extra pass, not in script/tables"),
    ("X2", 787060, ["T3?"], "B", "extra pass, not in script/tables"),
    ("R13", 814660, ["T3"], "A", "script Test 7"),
    ("R13r", 834940, ["T3"], "B", "return"),
    ("R14", 859620, ["T3"], "A", "script Test 8"),
    ("R14r", 881780, ["T3"], "B", "return"),
    ("M1", 934640, ["T4", "T3"], "A", "multiple-truck run 1 (Table 2.3), in line ~10 m"),
    ("M1r", 955880, ["T4", "T3"], "B", "return of both trucks, ~11 s apart"),
    ("M2", 981000, ["T4", "T3"], "A", "multiple-truck run 2 (Table 2.3)"),
    ("M2r", 1001260, ["T4", "T3"], "B", "return of both trucks, ~12 s apart"),
]
# Day 1 = 2020-09-10, AllStrainData_construction trucks.dat (100 Hz, 12 channels;
# ch4 == B.csv Column5 == st40). Indices located from the script's B.csv windows.
D1 = [
    ("R1", 44950, ["T1"], "A", "Eva 1 (Ricky 9:07)"),
    ("R2", 208540, ["T1"], "A", "Eva 2"),
    ("R3", 560110, ["T1"], "A", "Eva 3"),
    ("R4", 787580, ["T1"], "A", "Eva 4"),
    ("R5", 1003280, ["T1"], "A", "Eva 5; Truck 2 (R10) follows 43 s later"),
    ("R6", 163160, ["T2"], "A", "Eva 6; Truck 1 crossed 15.7 s earlier (161590)"),
    ("R7", 344590, ["T2"], "A", "Eva 7"),
    ("R8", 593530, ["T2"], "A", "Eva 8"),
    ("R9", 809790, ["T2"], "A", "Eva 9"),
    ("R10", 1007590, ["T2"], "A", "Eva 10"),
]

CH2 = ["st40", "st36", "st34", "st31"]
CH1 = [f"ch{k}" for k in range(1, 13)]
# day-1 channels with the strongest axle spikes (inferred wheel-path gauges, one per
# longitudinal station): used for the day-1 channel average "avg"
AVG1 = ["ch4", "ch5", "ch12", "ch11"]


SECOND = {"M1r": 958060, "M2r": 1003680}


def idx2(eid):
    return SECOND.get(eid)


def xlag(a, b, fs, maxlag=0.6):
    """Lag (s) of b relative to a from the cross-correlation of the high-passed signals
    (positive: b later)."""
    ha = a - median_filter(a, int(0.3 * fs))
    hb = b - median_filter(b, int(0.3 * fs))
    n = int(maxlag * fs)
    c = [np.dot(ha[n:-n], np.roll(hb, -k)[n:-n]) for k in range(-n, n + 1)]
    k = int(np.argmax(np.abs(c)) - n) if False else int(np.argmax(c) - n)
    # parabolic refinement
    j = k + n
    if 0 < j < len(c) - 1:
        d = 0.5 * (c[j - 1] - c[j + 1]) / (c[j - 1] - 2 * c[j] + c[j + 1])
    else:
        d = 0.0
    return (k + d) / fs


def spikes(y, fs, h_min=0.6):
    hp = y - median_filter(y, int(0.3 * fs))
    sd = np.median(np.abs(hp)) / 0.6745
    p, _ = find_peaks(hp, height=max(6 * sd, h_min), distance=max(3, int(0.03 * fs)))
    return p, hp


def spike_speed(Y, fs, i0, nax_list, AS_list):
    """Speed and first-axle times from local axle spikes. For each channel with exactly
    sum(nax) spikes, v = wheelbase/(t_last - t_first) of the first vehicle and the
    pattern residual is checked. Returns (v, t_first per vehicle [s, global], rms, nch)."""
    ntot = sum(nax_list)
    vs, tf, rr = [], [], []
    for y in Y:
        p, _ = spikes(y, fs)
        if len(p) != ntot:
            continue
        tp = (i0 + p) / fs
        k = 0
        firsts = []
        vv = []
        for nax, AS in zip(nax_list, AS_list):
            tt = tp[k:k + nax]
            wb = np.sum(AS)
            v = wb / (tt[-1] - tt[0])
            pred = tt[0] + np.concatenate([[0], np.cumsum(AS)]) / v
            rr.append(np.sqrt(np.mean((pred - tt) ** 2)))
            vv.append(v)
            firsts.append(tt[0])
            k += nax
        vs.append(vv)
        tf.append(firsts)
    if not vs:
        return None
    vs = np.array(vs)
    tf = np.array(tf)
    return np.median(vs, axis=0), tf[0], float(np.max(rr)), len(vs)


def analyse(day, events, df, chans, fs, tcol="Time"):
    rows = []
    t_all = np.arange(len(df)) / fs
    Ymat = {c: nio.GAIN * df[c].values for c in chans}
    ref = chans[0] if day == 2 else "ch4"
    for eid, idx, veh, lane, note in events:
        trk = [v.rstrip("?") for v in veh]
        nax = [TRUCKS[t]["n"] for t in trk]
        AS = [TRUCKS[t]["AS"] for t in trk]
        # --- spikes (search 2 s before to 16 s after detection index)
        i0 = idx - 2 * fs
        i1 = idx + 12 * fs
        sp_ch = [c for c in chans if c not in ("ch1", "ch2", "ch8", "ch9")]
        res = None
        if len(trk) == 1 or lane == "A":
            res = spike_speed([Ymat[c][i0:i1] for c in sp_ch], fs, i0, nax, AS)
        v_sp = None
        if res is not None and res[2] < 0.03:
            v_sp, tfirst, rms, nch = res
            v_sp = list(np.atleast_1d(v_sp))
            if len(v_sp) < len(trk):          # in-line multiple: same speed
                v_sp = v_sp * len(trk)
        # --- low-pass global response for direction (and fallback speed/time)
        j0 = idx - 60 * fs
        j1 = idx + 70 * fs
        tt = t_all[j0:j1:max(1, fs // 20)]
        yl = ev.lowpass(Ymat[ref][j0:j1], fs)[::max(1, fs // 20)]
        yl = yl - np.median(yl[: 20 * 20])
        ax0 = axles(trk[0])
        w0 = TRUCKS[trk[0]]["axw"] or [1.0] * len(ax0)
        tm = tt[np.argmin(ev.lowpass(Ymat[ref][j0:j1], fs, 0.2)[::max(1, fs // 20)])]
        fit = {}
        for direction in (+1, -1):
            f = ev.fit_event(tt, yl, ax0, w0, t_mid_guess=tm) if direction == 1 else None
            fit = f
            break
        # separate residuals for the two directions at the best speed
        dres = {}
        for direction in (+1, -1):
            best = None
            for v in np.arange(8.0, 32.01, 0.25):
                xs = bm.X_SENSOR if direction > 0 else bm.LTOT - bm.X_SENSOR
                for dt in np.arange(-3, 3.01, 0.1):
                    te = tm - (xs + 0.5 * ax0[-1]) / v + dt
                    s = ev.shape(tt, te, v, ax0, w0, direction)
                    A = np.vstack([s, np.ones_like(s), tt - tt.mean()]).T
                    c, *_ = np.linalg.lstsq(A, yl, rcond=None)
                    r = np.sum((A @ c - yl) ** 2)
                    if best is None or r < best[0]:
                        best = (r, v, te)
            dres[direction] = best
        lag = None
        if day == 2:
            lag = xlag(Ymat["st40"][i0:i1], Ymat["st31"][i0:i1], fs)
            direction = -1 if lag > 0 else +1        # st40 first -> lane A -> dir -1
            lane = "A" if direction == -1 else "B"
        else:
            direction = -1                          # ch3/ch4 first in all day-1 runs
        v_fit = dres[direction][1]
        te_fit = dres[direction][2]
        r2 = 1 - dres[direction][0] / np.sum((yl - yl.mean()) ** 2)
        xs = bm.X_SENSOR if direction > 0 else bm.LTOT - bm.X_SENSOR
        rows.append(dict(id=eid, day=day, idx=idx,
                         time=str(df[tcol].iloc[idx]), trucks="+".join(veh), lane=lane,
                         note=note, direction=direction, v_fit=v_fit, te_fit=te_fit,
                         r2_fit=r2, res_dir_ratio=dres[-direction][0] / dres[direction][0],
                         lag_40_31=lag, lag2=(xlag(Ymat["st40"][idx2(eid) - 2 * fs:idx2(eid) + 12 * fs],
                                                   Ymat["st31"][idx2(eid) - 2 * fs:idx2(eid) + 12 * fs], fs)
                                              if day == 2 and idx2(eid) else None),
                         v_spike=json.dumps(None if v_sp is None else
                                            [round(float(x), 3) for x in v_sp]),
                         t_first=json.dumps(None if v_sp is None else
                                            [round(float(x), 3) for x in tfirst]),
                         v_script=V_SCRIPT.get(eid, np.nan), xsens=xs))
        log(f"{eid:5s} {veh} lane={lane} dir={direction:+d} (res ratio "
            f"{rows[-1]['res_dir_ratio']:.2f}) v_fit={v_fit:.2f} r2={r2:.3f} "
            f"v_spike={rows[-1]['v_spike']} v_script={rows[-1]['v_script']}")
    return pd.DataFrame(rows), Ymat, t_all


def finalize(day, R, Ymat, t_all, fs, chans, pad=5.0, nbase=8.0, bias=None, gap=None):
    """Speeds/timing per vehicle, window, integral per channel."""
    out = []
    for _, r in R.iterrows():
        trk = [v.rstrip("?") for v in r.trucks.split("+")]
        vsp = json.loads(r.v_spike)
        tf = json.loads(r.t_first)
        if vsp is not None:
            v = vsp
            tref = tf
            vsrc = "spikes"
        else:
            # fallback: low-pass fit speed corrected by the fit/spike bias of lane-A runs
            if gap is not None and r.lag_40_31 is not None and abs(r.lag_40_31) > 0.05:
                v = [gap / abs(r.lag_40_31)]
                vsrc = "gauge lag"
                if len(trk) == 2:
                    v.append(gap / abs(r.lag2))
            else:
                v = [r.v_fit / bias] * len(trk)
                vsrc = "fit/bias"
            # first-axle time at the sensor from the low-pass fit centre (window only)
            tref = [r.idx / fs + 2.5]
            if len(trk) == 2:
                tref.append(idx2(r.id) / fs + 2.5)
        entries, exits = [], []
        for k, t in enumerate(trk):
            wb = axles(t)[-1]
            entries.append(tref[k] - r.xsens / v[k])
            exits.append(tref[k] + (bm.LTOT - r.xsens + wb) / v[k])
        ta = min(entries) - pad
        tb = max(exits) + pad
        d = r.to_dict()
        d.update(v_used=json.dumps([round(float(x), 3) for x in v]), v_src=vsrc,
                 t_entry=min(entries), t_exit=max(exits), ta=ta, tb=tb, T_win=tb - ta)
        GV = []
        for k, t in enumerate(trk):
            if TRUCKS[t]["GVW"] is not None:
                GV.append(TRUCKS[t]["GVW"])
            else:
                GV.append(GVW_T24[int(r.id[1:])] if r.id[1:].isdigit() else np.nan)
        d["GVW"] = float(np.sum(GV))
        d["sum_W_over_v"] = float(np.sum(np.array(GV) / np.array(v)))
        d["v1"] = float(v[0])
        m = (t_all >= ta - nbase - 1) & (t_all <= tb + nbase + 1)
        tt = t_all[m]
        for c in chans:
            I, _ = ev.integrate(tt, Ymat[c][m], ta, tb, nbase)
            d[f"Idt_{c}"] = I
            d[f"Idx_{c}"] = I * v[0] if len(trk) == 1 else np.nan
        out.append(d)
    return pd.DataFrame(out)


def noise_integrals(Ymat, t_all, fs, chans, busy, Twin, n=60, nbase=8.0, seed=1):
    """Integrals of quiet records (no detected vehicle within +-70 s) of length Twin."""
    rng = np.random.default_rng(seed)
    T = t_all[-1]
    res = {c: [] for c in chans}
    tries = 0
    while len(res[chans[0]]) < n and tries < 20000:
        tries += 1
        ta = rng.uniform(nbase + 1, T - Twin - nbase - 1)
        tb = ta + Twin
        if any((b > ta - 70) and (b < tb + 70) for b in busy):
            continue
        m = (t_all >= ta - nbase - 1) & (t_all <= tb + nbase + 1)
        for c in chans:
            I, _ = ev.integrate(t_all[m], Ymat[c][m], ta, tb, nbase)
            res[c].append(I)
    return {c: np.array(v) for c, v in res.items()}


def detect_all(y, fs, thr=0.8):
    """Times (s) of all vehicle events (any lane) for the noise-window exclusion."""
    from scipy.ndimage import uniform_filter1d
    step = fs // 10
    yd = y[::step]
    base = median_filter(yd, size=601)
    e = uniform_filter1d((np.abs(yd - base) > thr).astype(float), 30) > 0
    on = np.where(np.diff(e.astype(int)) == 1)[0]
    return on * step / fs


def main():
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    s2 = nio.load_strains200()
    R2, Y2, t2 = analyse(2, D2, s2, CH2, 200)
    Y2["avg"] = np.mean([Y2[c] for c in CH2], axis=0)
    a1 = nio.load_allstrain()
    R1, Y1, t1 = analyse(1, D1, a1, CH1, 100)
    Y1["avg"] = np.mean([Y1[c] for c in AVG1], axis=0)
    R = pd.concat([R2, R1])
    ok = R[(R.lane == "A") & R.v_spike.ne("null")]
    vs = ok.v_spike.apply(lambda s: json.loads(s)[0])
    bias = float(np.median(ok.v_fit / vs))
    bias_sd = float(np.std(ok.v_fit / vs))
    log(f"low-pass fit speed / spike speed (lane A, n={len(ok)}): median {bias:.3f}, "
        f"sd {bias_sd:.3f}")
    okA = R2[(R2.lane == "A") & R2.v_spike.ne("null")]
    gaps = okA.v_spike.apply(lambda s: json.loads(s)[0]) * okA.lag_40_31
    gap = float(np.median(gaps))
    log(f"st40-st31 distance from lane-A spike speed x lag: median {gap:.3f} m, "
        f"sd {np.std(gaps):.3f} m (n={len(gaps)})")
    F2 = finalize(2, R2, Y2, t2, 200, CH2 + ["avg"], bias=bias, gap=gap)
    F1 = finalize(1, R1, Y1, t1, 100, CH1 + ["avg"], bias=bias)
    F = pd.concat([F2, F1], ignore_index=True)
    # contamination: any other detected vehicle inside the window
    for day, Ymat, tA, fs, ref in [(2, Y2, t2, 200, "st40"), (1, Y1, t1, 100, "ch4")]:
        allev = detect_all(Ymat[ref], fs)
        sub = F[F.day == day]
        for i, r in sub.iterrows():
            inside = [t for t in allev if r.ta + 1 < t < r.tb - 1]
            # own detections lie within +-25 s of the reference index
            tidx = r.idx / fs
            foreign = [round(t - tidx, 1) for t in inside if abs(t - tidx) > 20]
            F.loc[i, "foreign_events_s"] = json.dumps(foreign)
        busy = list(allev)
        chans = (CH2 if day == 2 else CH1) + ["avg"]
        step = fs // 20
        Yd = {c: Ymat[c][::step] for c in chans}
        td = tA[::step]
        cache = {}
        for i in F.index[F.day == day]:
            Tw = round(float(F.loc[i, "T_win"]) / 2) * 2
            if Tw not in cache:
                cache[Tw] = noise_integrals(Yd, td, 20, chans, busy, Tw, n=80)
            for c in chans:
                F.loc[i, f"noise_sd_Idt_{c}"] = cache[Tw][c].std()
        for Tw, nz in sorted(cache.items()):
            log(f"day {day} noise sd of integral (microstrain*s), T={Tw}s: " +
                ", ".join(f"{c}={nz[c].std():.3f}" for c in chans))
    F.to_csv(os.path.join(HERE, "results", "events_field.csv"), index=False)
    log("written results/events_field.csv", len(F))
    cols = ["id", "trucks", "lane", "direction", "v_used", "v_src", "v_script", "GVW",
            "T_win", "foreign_events_s"]
    log(F[cols + ["Idx_st40", "Idx_ch4"]].to_string())


if __name__ == "__main__":
    LOG = open(os.path.join(HERE, "logs", "field.log"), "w")
    main()
