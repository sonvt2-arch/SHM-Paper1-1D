"""Prepare manuscript.md for pandoc: replace the 'Figure Captions' section by a
'Figures' section that embeds the figure files that exist in ../figures and
puts a captioned placeholder for each author-supplied figure."""
import os, re, sys
src, dst = sys.argv[1], sys.argv[2]
FIG = os.path.abspath(os.path.join(os.path.dirname(src), "figures"))
FILES = {2: "Fig2_obs_map_3span.png", 3: "Fig3_channels_prismatic.png", 4: "Fig4_multichannel_gain.png", 6: "Fig6_norbwim_crossings.png",
         7: "Fig7_norbwim_invariance.png", 8: "Fig8_caumay_channels.png", 9: "Fig9_caumay_identifiability.png"}
s = open(src, encoding="utf-8").read()
head, caps = s.split("## Figure Captions", 1)
out = ["## Figures\n"]
for m in re.finditer(r"\*\*Fig\. (\d+)\.\*\*(.*)", caps):
    n, cap = int(m.group(1)), m.group(2).strip()
    f = FILES.get(n)
    if f and os.path.exists(os.path.join(FIG, f)):
        out.append(f"![]({os.path.join(FIG, f)}){{width=16cm}}\n")
    else:
        out.append(f"::: {{custom-style=\"Figure placeholder\"}}\n[Figure {n} to be inserted: "
                   f"source file supplied by the authors]\n:::\n")
    out.append(f"**Fig. {n}.** {cap}\n")
open(dst, "w", encoding="utf-8").write(head + "\n".join(out))
