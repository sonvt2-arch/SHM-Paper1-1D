"""Prepare manuscript.md for pandoc: replace the 'Figure captions' section by a
'Figures' section that embeds ../figures/Fig<n>_*.png above each caption."""
import glob, os, re, sys
src, dst = sys.argv[1], sys.argv[2]
FIG = os.path.abspath(os.path.join(os.path.dirname(src), "figures"))
FILES = {int(re.findall(r"Fig(\d+)_", os.path.basename(f))[0]): f for f in glob.glob(os.path.join(FIG, "Fig*.png"))}
s = open(src, encoding="utf-8").read()
head, caps = re.split(r"(?mi)^## Figure captions\s*$", s, maxsplit=1)
out = ["## Figures\n"]
for m in re.finditer(r"\*\*Fig(?:ure|\.) (\d+)\.\*\*(.*)", caps):
    n, cap = int(m.group(1)), m.group(2).strip()
    out.append(f"![]({FILES[n]}){{width=16cm}}\n")
    out.append(f"**Figure {n}.** {cap}\n")
open(dst, "w", encoding="utf-8").write(head + "\n".join(out))
