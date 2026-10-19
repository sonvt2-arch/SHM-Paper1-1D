"""Fig. 1: example field crossings with integration window and beam-model shape."""
import os
import sys
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import nb_io as nio      # noqa: E402
import nb_events as ev   # noqa: E402
import nb_field as nf    # noqa: E402

plt.rcParams.update({"font.size": 8, "axes.grid": True, "grid.alpha": .3})
F = pd.read_csv(os.path.join(HERE, "results", "events_field.csv"))
s2 = nio.load_strains200()
a1 = nio.load_allstrain()
fig, axs = plt.subplots(3, 1, figsize=(7.2, 7.5))
for lt, a, (eid, df, fs, chans) in zip("abc", axs, [("R17", s2, 200, nf.CH2), ("R11", s2, 200, nf.CH2),
                                         ("R1", a1, 100, ["ch4", "ch5", "ch11", "ch1"])]):
    e = F[F.id == eid].iloc[0]
    t = np.arange(len(df)) / fs
    m = (t > e.ta - 15) & (t < e.tb + 15)
    tt = t[m] - e.t_entry
    for c in chans:
        y = nio.GAIN * df[c].values[m]
        _, yb = ev.integrate(t[m], y, e.ta, e.tb, 8.0)
        a.plot(tt, yb, lw=0.4, alpha=0.6)
        a.plot(tt, ev.lowpass(yb, fs, 0.5), lw=1.0,
               label=f"{c}: " + r"$\int\varepsilon dx$=" + f"{e['Idt_' + c] * e.v1:.0f}")
    trk = e.trucks
    ax0 = nf.axles(trk)
    w = nf.TRUCKS[trk]["axw"] or [1.0] * len(ax0)
    sh = ev.shape(t[m], e.t_entry, e.v1, ax0, w, e.direction)
    ref = ev.lowpass(nio.GAIN * df[chans[0]].values[m], fs, 0.5)
    _, refb = ev.integrate(t[m], nio.GAIN * df[chans[0]].values[m], e.ta, e.tb, 8.0)
    k = np.dot(sh, ev.lowpass(refb, fs, 0.5)) / np.dot(sh, sh)
    a.plot(tt, k * sh, "k--", lw=1, label=f"beam-model shape (scaled to {chans[0]})")
    a.axvspan(e.ta - e.t_entry, e.tb - e.t_entry, color="0.9", zorder=-1)
    a.axvline(0, color="k", lw=0.5)
    a.axvline(e.t_exit - e.t_entry, color="k", lw=0.5)
    a.set_title(f"({lt}) {nf.TRUCKS[trk]['n']}-axle truck, v = {e.v1:.1f} m/s, "
                f"day {e.day}", fontsize=8)
    a.set_ylabel(r"strain ($\mu\varepsilon$)")
    a.legend(fontsize=7, ncol=2, loc="lower left")
axs[-1].set_xlabel("time from first-axle entry (s)")
fig.tight_layout()
for x in ("png", "pdf"):
    fig.savefig(os.path.join(HERE, "figures", f"fig1_example_crossings.{x}"), dpi=300)
