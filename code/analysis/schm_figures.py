"""SCHM submission figures (publication quality, PNG >= 300 dpi + vector PDF).

Plotting only. Every plotted number comes from the existing analysis code or
from the files it writes; no computational logic is changed here:
  * Fig. 3  three-span observability map: code/analysis/data/obs_map_3span*.csv
            (written by cm_3span_theory.make_maps) and cm_3span_theory.xi_opt /
            side_norm / general_norm for the optimum line and the blind roots.
  * Fig. 7  Cau May EI profile and influence lines: wp3_run.bridge_models() and
            wp3_run.calibrate() (Cau May variants only), wp3_fe.Bridge.Cm().
  * Fig. S1 C_m indicators N_m and R_m for calibrations A and B: same models.
  * Fig. 8  baseline sensitivity of the event integral: data/bridges/*/
            wp4_events_baseline.csv (written by wp4_dynamic_records.py).
  * Fig. 9  2 Hz low-pass and dynamic residual: wp4_dynamic_records.detect_events
            and analyse_record, and data/bridges/*/wp4_lowpass.csv.

Run from the repository root:  python3 code/analysis/schm_figures.py
Output: manuscript/schm/figures/*.png (600 dpi) and *.pdf, plus
manuscript/schm/figures/schm_figures_values.txt (every value annotated on a figure).
"""
import os
import shutil
import sys

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import logging  # noqa: E402

logging.getLogger("fontTools").setLevel(logging.WARNING)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "manuscript", "schm", "figures")
sys.path.insert(0, HERE)
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "font.size": 8, "axes.labelsize": 8, "axes.titlesize": 8, "legend.fontsize": 7,
    "xtick.labelsize": 7, "ytick.labelsize": 7, "axes.linewidth": 0.6,
    "pdf.fonttype": 42, "ps.fonttype": 42, "savefig.bbox": "tight",
    "savefig.pad_inches": 0.02, "font.family": "DejaVu Sans",
})
W2 = 7.0      # double-column width (in)
DISP = {"Gie Cuc I": "Gie Cục I", "Phuong Do": "Phương Độ"}   # names as printed in figures
VALUES = []   # (figure, quantity, value) for traceability


def note(fig, what, val):
    VALUES.append(f"{fig}\t{what}\t{val}")


def save(fig, name):
    for ext, kw in (("png", dict(dpi=600)), ("pdf", {})):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), **kw)
    plt.close(fig)
    print("wrote", name)


# ---------------------------------------------------------------- Fig. 3
def fig3_obs_map():
    import cm_3span_theory as c3
    a = np.loadtxt(os.path.join(HERE, "data", "obs_map_3span.csv"), delimiter=",",
                   skiprows=2)
    B = np.unique(a[:, 0]); X = np.unique(a[:, 1])
    Z = np.full((X.size, B.size), np.nan)
    Z[np.searchsorted(X, a[:, 1]), np.searchsorted(B, a[:, 0])] = a[:, 2]
    BB, XX = np.meshgrid(B, X)
    b2 = np.loadtxt(os.path.join(HERE, "data", "obs_map_3span_asym.csv"), delimiter=",",
                    skiprows=2)
    A1 = np.unique(b2[:, 0]); A3 = np.unique(b2[:, 1])
    Z2 = np.full((A3.size, A1.size), np.nan)
    Z2[np.searchsorted(A3, b2[:, 1]), np.searchsorted(A1, b2[:, 0])] = b2[:, 2]
    AA1, AA3 = np.meshgrid(A1, A3)

    fig, ax = plt.subplots(1, 2, figsize=(W2, 2.9), constrained_layout=True)
    lev = np.linspace(-1.5, 1.5, 31)
    cs = ax[0].contourf(BB, XX, np.clip(Z, -1.5, 1.5), levels=lev, cmap="RdBu")
    ax[0].contour(BB, XX, Z, levels=[0.0], colors="k", linewidths=1.6)
    ax[0].contourf(BB, XX, np.abs(Z), levels=[0, 0.2], colors="none", hatches=["////"])
    ax[0].contour(BB, XX, np.abs(Z), levels=[0.2], colors="k", linewidths=0.5)
    xo = np.array([c3.xi_opt(b) for b in B])
    ok = xo[:, 1] > 0
    ax[0].plot(B[ok], xo[ok, 0], "k--", lw=1.0, label=r"optimum $\xi^*(\beta)$")
    bcm = 90 / 55
    ax[0].plot(bcm, 0.5, "o", mfc="w", mec="k", ms=5, zorder=5)
    ax[0].annotate("Mây Bridge\n55 + 90 + 55 m", (bcm, 0.5), (0.58, 0.66), fontsize=7,
                   va="center", arrowprops=dict(arrowstyle="-", lw=0.6))
    note("Fig3", "Cau May marker beta = 90/55, xi = 0.5; N_side", f"{bcm:.6f}, {c3.side_norm(0.5, bcm):.6f}")
    ax[0].set_xlabel(r"span ratio $\beta = L_\mathrm{main}/L_\mathrm{side}$")
    ax[0].set_ylabel(r"side-span sensor position $\xi = x/L_\mathrm{side}$")
    ax[0].set_title("(a) symmetric beam, uniform $EI$", loc="left")
    ax[0].legend(loc="lower left", frameon=True, framealpha=0.9)
    cb = fig.colorbar(cs, ax=ax[0], ticks=[-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
    cb.set_label(r"$N_w = 192EI_\mathrm{side}C_m/L_\mathrm{side}^4$")

    cs2 = ax[1].contourf(AA1, AA3, np.clip(Z2, -1.5, 1.5), levels=lev, cmap="RdBu")
    ax[1].contour(AA1, AA3, Z2, levels=[0.0], colors="k", linewidths=1.6)
    ax[1].contourf(AA1, AA3, np.abs(Z2), levels=[0, 0.2], colors="none", hatches=["////"])
    ax[1].contour(AA1, AA3, np.abs(Z2), levels=[0.2], colors="k", linewidths=0.5)
    ax[1].plot(A1, A1, "k:", lw=0.8, label="symmetric layouts")
    ax[1].set_xlabel(r"$L_1/L_2$ (instrumented side span)")
    ax[1].set_ylabel(r"$L_3/L_2$ (far side span)")
    ax[1].set_title("(b) asymmetric beam, sensor at mid span 1", loc="left")
    ax[1].legend(loc="upper left", frameon=True, framealpha=0.9)
    cb2 = fig.colorbar(cs2, ax=ax[1], ticks=[-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
    cb2.set_label(r"$192EI_1C_m/L_1^4$")
    save(fig, "Fig3_obs_map_3span")


# ---------------------------------------------------------------- Cau May models
def caumay_models():
    import wp3_run as w
    models = {k: v for k, v in w.bridge_models().items() if k[0] == "CM"}
    models = w.calibrate(models, lambda *a: None)
    return w, models


def fig7_caumay(w, models):
    base = w.BASE["CM"]
    mA = models[("CM", base, "kFE")]
    mB = models[("CM", base, "kMeas")]
    mP = models[("CM", base, "pinned")]
    mF = models[("CM", base, "fixed")]
    EIr = w.E_C45 * mA["I_mid"]            # EI_ref = design mid-span section
    note("Fig7", "k_FE (kN m/rad); calibration B alpha, k", f"{mA['k']:.4e}; {mB['alpha']:.4f}, {mB['k']:.4e}")

    fig = plt.figure(figsize=(W2, 6.4), constrained_layout=True)
    gs = fig.add_gridspec(3, 1, height_ratios=[0.6, 1, 1])
    ax0 = fig.add_subplot(gs[0])
    b = mP["b"]
    ax0.plot(b.x, mP["EI"](b.x) / EIr, "k", lw=1.0)
    for sx in b.sup:
        ax0.axvline(sx, color="0.6", lw=0.6)
    ax0.set_ylabel(r"$EI(x)/EI_\mathrm{mid}$")
    ax0.set_title(f"(a) assumed stiffness profile, design $EI$ ($n$ = {mP['n']:.3f}, "
                  f"$L_v$ = {mP['Lv']:g} m)", loc="left")
    ax0.set_xlim(b.sup[0], b.sup[-1])
    ax0.set_xticklabels([])
    note("Fig7a", "n, Lv, max EI/EI_mid", f"{mP['n']:.4f}, {mP['Lv']}, {(mP['EI'](b.x)/EIr).max():.4f}")

    for k_, (lab, xm, key, _n) in enumerate([w.CM_SENS[0], w.CM_SENS[2]]):
        ax = fig.add_subplot(gs[k_ + 1])
        name = "N8, 0.4L of side span" if k_ == 0 else "N7, mid centre span"
        i, L = mA["b"].span_of(xm)
        txt = []
        for m, col, cname, ls in ((mA, "#1f4e9c", "A", "-"), (mB, "#c0392b", "B", "-")):
            c, pos, neg, eta = m["b"].Cm(xm)
            e = eta * EIr / L ** 3
            ax.fill_between(m["b"].x, 0, e, where=e >= 0, color=col, alpha=0.18, lw=0)
            ax.fill_between(m["b"].x, 0, e, where=e < 0, color=col, alpha=0.38, lw=0)
            ax.plot(m["b"].x, e, color=col, lw=1.1, ls=ls, label=f"calibration {cname}")
            N = 192 * EIr * c / L ** 4
            txt.append(f"{cname}: $N_m$ = {N:.3f}, $R_m$ = {c / pos:.2f}")
            note(f"Fig7 {name}", f"cal {cname}: C_m (m2/kN), N_m, R_m",
                 f"{c:.5e}, {N:.4f}, {c / pos:.4f}")
        for m, ls, col, sname in ((mP, ":", "0.3", "pinned piers"), (mF, "--", "0.3", "fixed piers")):
            c, pos, neg, eta = m["b"].Cm(xm)
            ax.plot(m["b"].x, eta * EIr / L ** 3, color=col, lw=0.8, ls=ls, label=sname)
            note(f"Fig7 {name}", f"{sname}: N_m", f"{192 * EIr * c / L ** 4:.4f}")
        for sx in mA["b"].sup:
            ax.axvline(sx, color="0.6", lw=0.6)
        ax.axvline(xm, color="#2a9d8f", lw=0.9, ls="-.")
        ax.axhline(0, color="k", lw=0.5)
        ax.set_xlim(mA["b"].sup[0], mA["b"].sup[-1])
        ax.set_ylabel(r"$\eta_m\,EI_\mathrm{mid}/L^3$")
        ax.set_title(f"({'b' if k_ == 0 else 'c'}) influence line at {name}", loc="left")
        ax.text(0.01 if k_ == 0 else 0.99, 0.95, "\n".join(txt), transform=ax.transAxes,
                ha="left" if k_ == 0 else "right", va="top",
                fontsize=7, bbox=dict(fc="w", ec="0.7", lw=0.5))
        if k_ == 0:
            ax.legend(loc="lower left", ncol=2, frameon=True, framealpha=0.9)
            ax.set_xticklabels([])
        else:
            ax.set_xlabel("x along the continuous unit from end support T5 (m); dash-dot line: gauge")
    save(fig, "Fig7_caumay_EI_influence_lines")


def figS1_indicators(w, models):
    base = w.BASE["CM"]
    labs = ["N8, 0.4L\n(installed)", "N8, mid side span\n(alternative)", "N7, mid centre\n(installed)"]
    rows = []
    for (lab, xm, key, _n) in w.CM_SENS:
        r = {}
        for cal, sup in (("A", "kFE"), ("B", "kMeas"), ("pinned", "pinned"), ("fixed", "fixed")):
            m = models[("CM", base, sup)]
            EIr = w.E_C45 * m["I_mid"]
            c, pos, neg, eta = m["b"].Cm(xm)
            i, L = m["b"].span_of(xm)
            r[cal] = (192 * EIr * c / L ** 4, c / pos)
        rows.append(r)
    y = np.arange(3)
    fig, ax = plt.subplots(1, 2, figsize=(W2, 2.5), constrained_layout=True, sharey=True)
    h = 0.36
    for j, (idx, xl) in enumerate(((0, r"$N_m = 192EI_\mathrm{mid}C_m/L^4$"),
                                   (1, r"$R_m = C_m/A^+$"))):
        for k_, (cal, col) in enumerate((("A", "#1f4e9c"), ("B", "#c0392b"))):
            v = np.array([r[cal][idx] for r in rows])
            ax[j].barh(y + (k_ - 0.5) * h, v, h, color=col, label=f"calibration {cal}")
            for yy, vv in zip(y + (k_ - 0.5) * h, v):
                ax[j].text(vv + 0.01, yy, f"{vv:.3f}" if idx == 0 else f"{vv:.2f}",
                           va="center", fontsize=6.5)
            for nm, vv in zip(labs, v):
                note("FigS1", f"{nm.replace(chr(10), ' ')} cal {cal} {'N_m' if idx == 0 else 'R_m'}", f"{vv:.4f}")
        if idx == 0:
            # bounds as in Table 5: pinned ... fixed piers, design EI, all L_v variants
            # (norm_min / norm_max written by wp3_run.py to results/wp3_Cm_summary.csv)
            import csv
            summ = {r["sensor"]: r for r in csv.DictReader(
                open(os.path.join(HERE, "results", "wp3_Cm_summary.csv")))}
            lo = np.array([float(summ[s[0]]["norm_min"]) for s in w.CM_SENS])
            hi = np.array([float(summ[s[0]]["norm_max"]) for s in w.CM_SENS])
            ax[j].errorbar((lo + hi) / 2, y, xerr=(hi - lo) / 2, fmt="none", ecolor="k",
                           capsize=2.5, lw=0.7, label="pinned … fixed bound")
            for nm, a_, b_ in zip(labs, lo, hi):
                note("FigS1", f"{nm.replace(chr(10), ' ')} pinned..fixed bound N_m", f"{a_:.4f} … {b_:.4f}")
            ax[j].axvline(0.2, color="0.4", ls="--", lw=0.8)
            ax[j].text(0.205, -0.42, r"$|N_m| = 0.2$ (prismatic threshold)", fontsize=6.5,
                       color="0.3", va="bottom")
        ax[j].axvline(0, color="k", lw=0.5)
        ax[j].set_xlabel(xl)
    ax[0].set_yticks(y)
    ax[0].set_yticklabels(labs)
    ax[0].set_ylim(2.55, -0.62)
    ax[0].set_xlim(-0.1, 0.62)
    ax[1].set_xlim(0, 0.95)
    hh, ll = ax[0].get_legend_handles_labels()
    fig.legend(hh, ll, loc="lower center", bbox_to_anchor=(0.5, -0.08), ncol=3, frameon=False)
    save(fig, "FigS1_caumay_indicators")


# ---------------------------------------------------------------- Fig. 8
def fig8_baseline():
    import pandas as pd
    frames = []
    for br, short in (("gie-cuc-1", "Gie Cuc I"), ("phuong-do", "Phuong Do")):
        d = pd.read_csv(os.path.join(ROOT, "data", "bridges", br, "wp4_events_baseline.csv"))
        d["name"] = short
        frames.append(d)
    d = pd.concat(frames)
    d = d[d.major & d.I_b_linear.notna() & ~d.trunc_start & ~d.trunc_end]
    # one bar group per crossing: the raw channel (the processed channel gives the same
    # deviations except at Phuong Do N1, where both channels are shown)
    sel = []
    for _, r in d.iterrows():
        if r.channel == "raw" or (r["name"] == "Phuong Do" and r.span == "N1"):
            sel.append(r)
    meths = [("dev_pct_a_raw", "tare only", "#7f7f7f"),
             ("dev_pct_c1_poly3", "cubic (quiet samples)", "#2a9d8f"),
             ("dev_pct_c2_hp0.1Hz", "high-pass 0.1 Hz", "#e9a03b"),
             ("dev_pct_c3_hp0.5Hz", "high-pass 0.5 Hz", "#c0392b")]
    fig, ax = plt.subplots(figsize=(W2, 2.6), constrained_layout=True)
    x = np.arange(len(sel))
    wd = 0.19
    for k_, (col, lab, c) in enumerate(meths):
        v = np.array([r[col] for r in sel], float)
        ax.bar(x + (k_ - 1.5) * wd, v, wd, color=c, label=lab)
        for r, vv in zip(sel, v):
            note("Fig8", f"{r['name']} {r.span} {r.channel} e{r.event} {lab} (%)", f"{vv}")
    ticks = [f"{DISP[r['name']]}\n{r.span}, crossing {r.event}" +
             (f"\n({'raw' if r.channel == 'raw' else 'processed'})"
              if r["name"] == "Phuong Do" and r.span == "N1" else "") for r in sel]
    ax.set_xticks(x)
    ax.set_xticklabels(ticks, fontsize=6.5)
    ax.axhline(0, color="k", lw=0.5)
    ax.set_ylabel("deviation of event integral from\nlinear pre/post baseline (%)")
    ax.set_ylim(-115, 20)
    ax.grid(axis="y", alpha=0.3, lw=0.4)
    ax.legend(ncol=4, loc="lower center", bbox_to_anchor=(0.5, 1.0), frameon=False)
    save(fig, "Fig8_baseline_sensitivity")


# ---------------------------------------------------------------- Fig. 9
def fig9_lowpass():
    import pandas as pd
    log = os.path.join(ROOT, "code", "analysis", "logs", "wp4.log")
    bak = log + ".schm_bak"
    shutil.copy2(log, bak)              # importing wp4 truncates its log; restore after
    try:
        import wp4_dynamic_records as w4
        w4.log.disabled = True
        rec = []
        for br, cfg in w4.BRIDGES.items():
            lp = pd.read_csv(os.path.join(ROOT, "data", "bridges", br, "wp4_lowpass.csv"))
            for span, f in cfg["files"].items():
                d = pd.read_csv(os.path.join(ROOT, "data", "bridges", br, f))
                t = d["time_ms"].values / 1000.0
                det = w4.detect_events(t, -d[cfg["cols"][1]].values.astype(float))
                y = d[cfg["cols"][1]].values.astype(float)
                rows, _, info = w4.analyse_record(br, span, "proc", t, y, det)
                major = [r for r in rows if r["major"]]
                if not major:
                    continue
                r0 = major[0]
                e = [x for x in info["ev"] if x["n"] == r0["event"]][0]
                lr = lp[(lp.span == span) & (lp.channel == "proc") & (lp.event == r0["event"])
                        & (lp.fc_Hz == 2.0)].iloc[0]
                rec.append((br, span, t, -y, e, info, lr))
    finally:
        for h in list(logging.getLogger().handlers):
            h.close()
        shutil.move(bak, log)
    n = len(rec)
    fig, axs = plt.subplots(n, 2, figsize=(W2, 1.25 * n + 0.4), constrained_layout=True,
                            gridspec_kw=dict(width_ratios=[1.25, 1]))
    for k_, (br, span, t, s, e, info, lr) in enumerate(rec):
        ref = e["base_b"] if not np.isnan(e["base_b"]).all() else e["base_a"]
        sl = info["s_lp"][2.0]
        m = (t >= e["ta"] - 1) & (t <= e["tb"] + 1)
        nm = ("Gie Cuc I " if br == "gie-cuc-1" else "Phuong Do ") + span
        axs[k_, 0].plot(t[m], (s - ref)[m], color="0.45", lw=0.6, label="unfiltered")
        axs[k_, 0].plot(t[m], (sl - ref)[m], color="#c0392b", lw=1.0, label="low-pass 2 Hz")
        axs[k_, 0].text(0.01, 0.92, DISP[nm[:-len(span) - 1]] + " " + span,
                        transform=axs[k_, 0].transAxes, va="top", fontsize=7)
        axs[k_, 1].plot(t[m], (s - sl)[m], color="#1f4e9c", lw=0.6)
        axs[k_, 1].axhline(0, color="k", lw=0.4)
        rr = (s - sl)[m]
        lo_, hi_ = np.nanmin(rr), np.nanmax(rr)
        axs[k_, 1].set_ylim(lo_ - 0.05 * (hi_ - lo_), hi_ + 0.40 * (hi_ - lo_))  # headroom for the label
        axs[k_, 1].text(0.01, 0.92, f"$I_\\mathrm{{LP}}/I$ = {lr.ratio_LP_over_unfiltered}; "
                        f"net/abs = {lr.cancellation_net_over_abs}",
                        transform=axs[k_, 1].transAxes, va="top", fontsize=6.5)
        note("Fig9", f"{nm} proc e{e['n']}: I_LP/I, net/abs", f"{lr.ratio_LP_over_unfiltered}, {lr.cancellation_net_over_abs}")
        for a in axs[k_]:
            a.grid(alpha=0.3, lw=0.4)
            if k_ < n - 1:
                a.set_xticklabels([])
        axs[k_, 0].set_ylabel("s (mm)")
    axs[0, 0].legend(loc="upper right", frameon=False, fontsize=6.5)
    axs[0, 0].set_title("(a) deflection relative to linear pre/post baseline", loc="left")
    axs[0, 1].set_title("(b) dynamic residual, unfiltered − low-pass", loc="left")
    axs[-1, 0].set_xlabel("time (s)")
    axs[-1, 1].set_xlabel("time (s)")
    save(fig, "Fig9_lowpass_residual")


if __name__ == "__main__":
    fig3_obs_map()
    w, models = caumay_models()
    fig7_caumay(w, models)
    figS1_indicators(w, models)
    fig8_baseline()
    fig9_lowpass()
    with open(os.path.join(OUT, "schm_figures_values.txt"), "w", encoding="utf-8") as fh:
        fh.write("figure\tquantity\tvalue\n" + "\n".join(VALUES) + "\n")
    print("values ->", os.path.join(OUT, "schm_figures_values.txt"))
