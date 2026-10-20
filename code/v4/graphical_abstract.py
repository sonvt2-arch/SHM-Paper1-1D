"""Graphical abstract for the ASE submission (13.3 x 5 in), assembled from main-text
Fig. 1, Fig. 2 panel (a) and Fig. 7 panel (a). No new data or numbers: Figs. 1 and 2
are cropped from the figure files in manuscript/ase/figures, and Fig. 7 panel (a) is
re-plotted from code/theory2/logs/ident_static_scan.npz, the file written by
code/theory2/ident_static.py together with Fig. 7, with the same plotting commands.
Run after gc/schm/ident_static figures are current:  python3 code/v4/graphical_abstract.py
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
F = os.path.join(ROOT, "manuscript", "ase", "figures")
sys.path.insert(0, os.path.join(ROOT, "code", "theory2"))
from ident_static import K_FE  # noqa: E402  (constant only; no computation on import)

plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Inter", "DejaVu Sans"],
                     "font.size": 10, "axes.titlesize": 10})


def trim(img, thr=0.97, pad=6):
    """Crop white margins of an RGB(A) image array with values in [0, 1]."""
    rgb = img[..., :3]
    ink = (rgb < thr).any(axis=2)
    rows, cols = np.where(ink.any(axis=1))[0], np.where(ink.any(axis=0))[0]
    r0, r1 = max(rows[0] - pad, 0), min(rows[-1] + pad + 1, img.shape[0])
    c0, c1 = max(cols[0] - pad, 0), min(cols[-1] + pad + 1, img.shape[1])
    return img[r0:r1, c0:c1]


def left_panel(img, lo=0.45, hi=0.60, thr=0.97):
    """Left panel of a two-panel figure: cut in the middle of the widest blank column run
    between lo and hi of the image width."""
    blank = ~(img[..., :3] < thr).any(axis=2).any(axis=0)
    a, b = int(lo * img.shape[1]), int(hi * img.shape[1])
    best, run, start = (0, a), 0, a
    for j in range(a, b):
        if blank[j]:
            if run == 0:
                start = j
            run += 1
            if run > best[0]:
                best = (run, start)
        else:
            run = 0
    cut = best[1] + best[0] // 2
    return img[:, :cut]


fig1 = trim(mpimg.imread(os.path.join(F, "Fig1_beams.png")))
fig2a = trim(left_panel(mpimg.imread(os.path.join(F, "Fig2_obs_map_3span.png"))))

fig = plt.figure(figsize=(13.3, 5.0))
gs = fig.add_gridspec(1, 3, width_ratios=[1.32, 1.0, 0.92], left=0.006, right=0.992,
                      bottom=0.11, top=0.70, wspace=0.25)
a1 = fig.add_subplot(gs[0])
a1.imshow(fig1)
a1.axis("off")
a2 = fig.add_subplot(gs[1])
a2.imshow(fig2a)
a2.axis("off")

# Fig. 7 panel (a), same commands as code/theory2/ident_static.py
d = np.load(os.path.join(ROOT, "code", "theory2", "logs", "ident_static_scan.npz"))
KAPPA, tau_rec = d["kappa"], float(d["tau_rec"])
names = [k[:-5] for k in d.files if k.endswith("__rho")]
ax = fig.add_subplot(gs[2])
for name in names:
    ax.semilogx(KAPPA, d[f"{name}__rho"], color="k" if name == "Lv44" else "0.65",
                lw=1.6 if name == "Lv44" else 0.8)
ax.axhline(1.0, color="k", lw=0.5)
ax.axhspan(np.exp(-2 * tau_rec), np.exp(2 * tau_rec), color="#2a9d8f", alpha=0.15, lw=0,
           label=f"admissible band |ln $r_{{87}}$| $\\leq$ 2$\\tau$, $\\tau$ = {100*tau_rec:.1f} %")
ax.plot([], [], color="0.65", lw=0.8, label="model-form variants")
ax.axvline(K_FE, color="#d0563b", ls=":", lw=1.2); ax.text(K_FE, 1.13, " A", color="#d0563b")
ax.axvline(1.199e8 / 0.716, color="#3b6fb6", ls=":", lw=1.2); ax.text(1.68e8, 1.13, " B", color="#3b6fb6")
ax.set_ylabel("$r_{87}$ = (meas/pred)$_{N8}$ / (meas/pred)$_{N7}$")
ax.set_xlabel("$\\kappa = k/\\alpha$ (kN m/rad)")
ax.set_ylim(0.98, 1.16)
ax.legend(fontsize=8.5, loc="lower right")
ax.set_title("misfit ratio of Mây Bridge gauges N8 and N7", loc="left")

heads = ["Continuous girder: influence lines change sign,\nso the record integral can vanish",
         "Closed-form blind loci and near-blind bands\nguide channel placement",
         "In-service box girder: pier stiffness\ncontrols the side-span constant"]
for a, t in zip((a1, a2, ax), heads):
    bb = gs[[a1, a2, ax].index(a)].get_position(fig)
    fig.text((bb.x0 + bb.x1) / 2, 0.80, t, ha="center", va="center", fontsize=14,
             fontweight="semibold", color="#1f3a5f")
fig.suptitle("Blind loci and sensor layout for influence-area bridge weigh-in-motion on continuous girders",
             fontsize=16, fontweight="bold", y=0.975)
out = os.path.join(F, "GraphicalAbstract.png")
fig.savefig(out, dpi=300, bbox_inches="tight", pad_inches=0.08)
print("saved", out)
