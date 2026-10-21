"""Fig. 1: notation sketch of the two-span and symmetric three-span beams."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle

OUT = os.environ.get("FIG1_OUT",
                     os.path.join(os.path.dirname(__file__), "..", "..", "manuscript", "v4", "figures"))
LABELS = os.environ.get("FIG1_LABELS", "1") != "0"   # panel letters off for the graphical abstract
plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Inter", "DejaVu Sans"],
                     "font.size": 10})


def pin(ax, x, y=0.0, s=0.12):
    ax.add_patch(Polygon([[x, y], [x - s, y - 1.6 * s], [x + s, y - 1.6 * s]],
                         closed=True, fc="white", ec="k", lw=1.0))
    ax.plot([x - 1.6 * s, x + 1.6 * s], [y - 1.6 * s] * 2, "k", lw=1.0)


def roller(ax, x, y=0.0, s=0.12):
    ax.add_patch(Polygon([[x, y], [x - s, y - 1.3 * s], [x + s, y - 1.3 * s]],
                         closed=True, fc="white", ec="k", lw=1.0))
    for dx in (-0.6 * s, 0.6 * s):
        ax.add_patch(Circle((x + dx, y - 1.6 * s), 0.28 * s, fc="white", ec="k", lw=0.8))
    ax.plot([x - 1.6 * s, x + 1.6 * s], [y - 2.0 * s] * 2, "k", lw=1.0)


def dim(ax, x0, x1, y, label, dy=0.06):
    ax.annotate("", xy=(x0, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle="<->", lw=0.8, shrinkA=0, shrinkB=0))
    for x in (x0, x1):
        ax.plot([x, x], [y - dy, y + dy], "k", lw=0.6)
    ax.text(0.5 * (x0 + x1), y - 0.13, label, ha="center", va="top")


def sensor(ax, x, label):
    ax.plot(x, 0.0, marker="v", ms=8, mfc="k", mec="k", zorder=5)
    ax.text(x, 0.16, label, ha="center", va="bottom")


fig, axs = plt.subplots(2, 1, figsize=(6.8, 3.6))

# (a) two-span beam
ax = axs[0]
L1, L2 = 3.0, 4.2
ax.plot([0, L1 + L2], [0, 0], "k", lw=2.2)
pin(ax, 0); roller(ax, L1); roller(ax, L1 + L2)
xs = 0.42 * L1
sensor(ax, xs, "sensor")
ax.text(0.72 * L1, 0.13, r"$EI_1$", ha="center", va="bottom")
ax.text(L1 + 0.5 * L2, 0.13, r"$EI_2 = \gamma EI_1$", ha="center", va="bottom")
dim(ax, 0, xs, -0.42, r"$\xi L_1$")
dim(ax, 0, L1, -0.78, r"$L_1$ (instrumented)")
dim(ax, L1, L1 + L2, -0.78, r"$L_2 = \lambda L_1$")
if LABELS:
    ax.text(-0.45, 0.25, "(a)", fontsize=11)

# (b) symmetric three-span beam
ax = axs[1]
Ls, Lm = 2.2, 3.6
x = [0, Ls, Ls + Lm, 2 * Ls + Lm]
ax.plot([x[0], x[-1]], [0, 0], "k", lw=2.2)
pin(ax, x[0]); roller(ax, x[1]); roller(ax, x[2]); roller(ax, x[3])
xs = 0.42 * Ls
sensor(ax, xs, "sensor")
ax.text(0.75 * Ls, 0.13, r"$EI_\mathrm{side}$", ha="center", va="bottom")
ax.text(x[1] + 0.5 * Lm, 0.13, r"$EI_\mathrm{main} = \gamma EI_\mathrm{side}$", ha="center", va="bottom")
ax.text(x[2] + 0.5 * Ls, 0.13, r"$EI_\mathrm{side}$", ha="center", va="bottom")
dim(ax, 0, xs, -0.42, r"$\xi L_\mathrm{side}$")
dim(ax, x[0], x[1], -0.78, r"$L_\mathrm{side}$")
dim(ax, x[1], x[2], -0.78, r"$L_\mathrm{main} = \beta L_\mathrm{side}$")
dim(ax, x[2], x[3], -0.78, r"$L_\mathrm{side}$")
if LABELS:
    ax.text(-0.45, 0.25, "(b)", fontsize=11)

for ax in axs:
    ax.set_xlim(-0.6, 8.2)
    ax.set_ylim(-1.15, 0.55)
    ax.set_aspect("equal")
    ax.axis("off")

fig.tight_layout(h_pad=0.4)
for ext in ("pdf", "png"):
    os.makedirs(OUT, exist_ok=True)
    fig.savefig(os.path.join(OUT, f"Fig1_beams.{ext}"), dpi=300, bbox_inches="tight")
print("saved Fig1_beams")
