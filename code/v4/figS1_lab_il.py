"""Fig. S8: measured and analytical single-load influence line of the laboratory beam
(data of Supplementary Table S5, stored in lab_single_load_influence_line.csv)."""
import csv, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "lab_single_load_influence_line.csv")
OUT = os.path.join(HERE, "figures", "FigS8_lab_influence_line.png")
plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Inter", "DejaVu Sans"],
                     "font.size": 10})

x, ana, mea = [], [], []
with open(DATA, newline="") as f:
    for r in csv.DictReader(f):
        x.append(float(r["x_mm"]) / 1000)
        ana.append(float(r["analytical_mm"]))
        mea.append(float(r["measured_mm"]))

fig, ax = plt.subplots(figsize=(6.0, 3.0))
ax.axhline(0, color="0.6", lw=0.6)
ax.axvline(2.5, color="0.6", lw=0.6, ls=":")
ax.plot(x, ana, "k-", lw=1.2, label="analytical")
ax.plot(x, mea, "o", ms=4, mfc="white", mec="C3", label="measured")
ax.set_xlabel("load position $x$ (m)")
ax.set_ylabel("mid-span deflection of span 1 (mm)")
ax.set_xlim(0, 5)
ax.legend(frameon=False, loc="upper right")
ax.text(1.6, -0.8, "span 1", ha="center")
ax.text(3.3, 2.4, "span 2", ha="center")
fig.tight_layout()
os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT, dpi=300)
print("saved", OUT, len(x), "points")
