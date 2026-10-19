"""Fig. S1: measured and analytical single-load influence line of the laboratory beam (Table S1)."""
import os, re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(__file__)
SUP = os.path.join(HERE, "..", "..", "manuscript", "v4", "supplementary_material.md")
OUT = os.path.join(HERE, "..", "..", "manuscript", "v4", "figures", "supplementary", "FigS1_lab_influence_line.png")
plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm", "font.size": 10})

txt = open(SUP, encoding="utf-8").read()
block = txt[txt.index("**Table S1.**"):]
x, ana, mea = [], [], []
for line in block.splitlines()[3:]:
    if not line.startswith("|"):
        if x:
            break
        continue
    c = [s.strip() for s in line.strip("|").split("|")]
    if c[1] and re.match(r"[−\-]?\d", c[1]):
        x.append(float(c[0]) / 1000)
        ana.append(float(c[1].replace("−", "-")))
        mea.append(float(c[2].replace("−", "-")))

fig, ax = plt.subplots(figsize=(6.0, 3.0))
ax.axhline(0, color="0.6", lw=0.6)
ax.axvline(2.5, color="0.6", lw=0.6, ls=":")
ax.plot(x, ana, "k-", lw=1.2, label="analytical")
ax.plot(x, mea, "o", ms=4, mfc="white", mec="C3", label="measured")
ax.set_xlabel("load position $x$ (m)")
ax.set_ylabel("mid-span deflection of span 1 (mm)")
ax.set_xlim(0, 5)
ax.legend(frameon=False)
ax.text(1.6, -0.8, "span 1", ha="center")
ax.text(3.75, 2.4, "span 2", ha="center")
fig.tight_layout()
os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT, dpi=300)
print("saved", OUT, len(x), "points")
