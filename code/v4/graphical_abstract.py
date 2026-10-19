"""Graphical abstract for the ASE submission, assembled from main-text Figs. 1, 2
and 7 (no new data or numbers)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(HERE, "..", "..", "manuscript", "ase", "figures")
panels = [("Fig1_beams.png", "Continuous girder: influence lines change sign,\nso the record integral can vanish"),
          ("Fig2_obs_map_3span.png", "Closed-form blind loci and near-blind bands\nguide channel placement"),
          ("Fig7_caumay_identifiability.png", "In-service box girder: pier stiffness\ncontrols the side-span constant")]
fig, axs = plt.subplots(1, 3, figsize=(13.3, 5.0), gridspec_kw={"width_ratios": [1.0, 1.25, 0.8]})
for a, (f, t) in zip(axs, panels):
    a.imshow(mpimg.imread(os.path.join(F, f)))
    a.axis("off")
fig.tight_layout(rect=(0, 0, 1, 0.80))
for a, (f, t) in zip(axs, panels):
    bb = a.get_position()
    fig.text((bb.x0 + bb.x1) / 2, 0.86, t, ha="center", va="center", fontsize=12, fontfamily="serif")
fig.suptitle("Observability and sensor layout for influence-area load monitoring of continuous girder bridges",
             fontsize=13, fontweight="bold", fontfamily="serif")
out = os.path.join(F, "GraphicalAbstract.png")
fig.savefig(out, dpi=300)
print("saved", out)
