"""Prepare supplementary_material.md for pandoc, as prep_md.py does for the
article: centred title block, each Fig. S<n> placed after the first paragraph
that cites it (centred), caption directly below; caption section removed."""
import glob, os, re, sys
src, figdir, dst = sys.argv[1:]
FILES = {int(re.findall(r"FigS(\d+)_", os.path.basename(f))[0]): f for f in glob.glob(os.path.join(figdir, "FigS*.png"))}
s = open(src, encoding="utf-8").read()
head, caps = re.split(r"(?m)^## Supplementary figure captions\s*$", s, maxsplit=1)
CAP = {int(m.group(1)): m.group(2).strip() for m in re.finditer(r"\*\*Fig\. S(\d+)\.\*\*(.*)", caps)}
title, rest = re.split(r"(?m)^(?=## S1\.)", head, maxsplit=1)
lines = title.strip().split("\n", 1)
intro = lines[1].strip().split("\n\n")
tb = [b for b in intro if b.startswith("**") or re.match(r"^[A-Z][\w-]+ [\w-]+(, [A-Z][\w-]+ [\w-]+)*$", b)]
other = [b for b in intro if b not in tb]
title = ("::: {custom-style=\"Title\"}\n" + lines[0].lstrip("# ").strip() + "\n:::\n\n::: {custom-style=\"Title block\"}\n"
         + "\n\n".join(tb) + "\n:::\n\n" + "\n\n".join(other) + "\n\n")
blocks = rest.split("\n\n")
placed, out = set(), []
for b in blocks:
    out.append(b)
    if b.lstrip().startswith(("#", "|", "$$", "**Table")):
        continue
    for m in re.finditer(r"Figs?\.\s*((?:S\d+[a-z]?(?:\s*(?:,|and|–|-)\s*)?)+)", b):
        for x in re.findall(r"S(\d+)", m.group(1)):
            n = int(x)
            if n in CAP and n not in placed:
                placed.add(n)
                style = "Caption centred" if len(CAP[n]) < 90 else "Caption justified"
                out.append(f"::: {{custom-style=\"Figure\"}}\n![]({FILES[n]}){{width=14cm}}\n:::")
                out.append(f"::: {{custom-style=\"{style}\"}}\n**Figure S{n}.** {CAP[n]}\n:::")
missing = sorted(set(CAP) - placed)
assert not missing, f"supplementary figures never cited: {missing}"
open(dst, "w", encoding="utf-8").write(title + "\n\n".join(out))
