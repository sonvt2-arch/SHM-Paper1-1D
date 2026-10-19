"""Prepare manuscript.md for pandoc (Quy tac viet chung V.1, V.1.1):
- every figure is placed in its own centred paragraph right after the first
  body paragraph that cites it, with its caption directly below (one-line
  captions centred, longer captions justified);
- the 'Figure captions' section is removed;
- the title block (everything before '## Abstract') is wrapped in a centred style."""
import glob, os, re, sys
src, dst = sys.argv[1], sys.argv[2]
FIG = os.path.abspath(os.path.join(os.path.dirname(src), "figures"))
FILES = {int(re.findall(r"Fig(\d+)_", os.path.basename(f))[0]): f for f in glob.glob(os.path.join(FIG, "Fig*.png"))}
s = open(src, encoding="utf-8").read()
head, caps = re.split(r"(?mi)^## Figure captions\s*$", s, maxsplit=1)
CAP = {int(m.group(1)): m.group(2).strip() for m in re.finditer(r"\*\*Fig(?:ure|\.) (\d+)\.\*\*(.*)", caps)}
# centred title block
title, rest = re.split(r"(?m)^## Abstract\s*$", head, maxsplit=1)
tl = title.strip().split("\n", 1)
tb = re.sub(r"(?m)^---\s*$", "", tl[1]).strip()
title = "::: {custom-style=\"Title\"}\n" + tl[0].lstrip("# ").strip() + "\n:::\n\n::: {custom-style=\"Title block\"}\n" + tb + "\n:::\n\n"
blocks = rest.split("\n\n")
body_end = next(i for i, b in enumerate(blocks) if b.startswith("## Acknowledgements"))
placed = set()
out = []
def cites(b):
    ns = []
    for m in re.finditer(r"Figs?\.\s*((?:\d+[a-z]?(?:\s*(?:,|and|–|-)\s*)?)+)", b):
        for x in re.findall(r"\d+", m.group(1)):
            ns.append(int(x))
    return ns
for i, b in enumerate(blocks):
    out.append(b if b.strip() != "---" else "")
    if i >= body_end or b.lstrip().startswith(("#", "|", "$$", "**Table", "**Fig")):
        continue
    for n in cites(b):
        if n in CAP and n not in placed:
            placed.add(n)
            style = "Caption centred" if len(CAP[n]) < 90 else "Caption justified"
            out.append(f"::: {{custom-style=\"Figure\"}}\n![]({FILES[n]}){{width=14cm}}\n:::")
            out.append(f"::: {{custom-style=\"{style}\"}}\n**Figure {n}.** {CAP[n]}\n:::")
missing = sorted(set(CAP) - placed)
assert not missing, f"figures never cited in body: {missing}"
open(dst, "w", encoding="utf-8").write(title + "## Abstract\n" + "\n\n".join(out))
