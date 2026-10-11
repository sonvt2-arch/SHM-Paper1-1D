"""WP7b - mechanical checks of manuscript/v2 (word counts, highlights,
equation citations, placeholders).

Run:  python3 code/analysis/wp7b_checks.py [manuscript_dir]
      (default manuscript/v2; e.g. manuscript/schm for the SCHM version)
Counting rules: inline math $...$ counts as one word; display equations,
tables, headings, figure captions, appendices, declarations and references
are excluded from the main-text count (Introduction to end of Section 8).
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
V2 = os.path.join(ROOT, sys.argv[1]) if len(sys.argv) > 1 else \
    os.path.join(ROOT, "manuscript", "v2")
ms = open(os.path.join(V2, "manuscript.md"), encoding="utf-8").read()


def words(text):
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.S)
    text = re.sub(r"\$[^$]+\$", " MATH ", text)
    return len(text.split())


def section(text, start, end):
    i = text.index(start)
    j = text.index(end, i)
    return text[i + len(start):j]


abstract = section(ms, "## Abstract\n", "**Keywords:**")
print(f"Abstract: {words(abstract)} words (inline math = 1 word); "
      f"raw whitespace split {len(abstract.split())}")

main = section(ms, "## 1. Introduction", "## Appendix A.")
keep = []
for line in main.splitlines():
    s = line.strip()
    if not s or s.startswith("#") or s.startswith("|") or s.startswith("**Table") \
            or s.startswith("$$") or s == "---":
        continue
    keep.append(s)
print(f"Main text (Sections 1-8, prose only): {words(' '.join(keep))} words")

hl_path = os.path.join(V2, "highlights.md")
hl = [l[2:].strip() for l in open(hl_path, encoding="utf-8")
      if l.startswith("- ")] if os.path.exists(hl_path) else []
for h in hl:
    print(f"Highlight ({len(h)} chars): {h}")

kw = re.search(r"\*\*Keywords:\*\*(.*)", ms).group(1).split(";")
print(f"Keywords: {len(kw)}")

body = ms.split("## References")[0]
tags = re.findall(r"\\tag\{([^}]+)\}", body)
uncited = []
for t in tags:
    pat = r"Eqs?\.\s*\((?:[^)]*\b)?" + re.escape(t) + r"\)" + "|" + \
          r"Eqs\.\s*\(\d+\)[–-]\((\d+)\)"
    hits = [m for m in re.finditer(r"Eqs?\.\s*\(([^)]*)\)(?:\s*(?:–|and|,)\s*\(([^)]*)\))?", body)]
    found = False
    for m in hits:
        a, b = m.group(1), m.group(2)
        if a == t or b == t:
            found = True
        if a and b and a.isdigit() and b.isdigit() and t.isdigit() and int(a) <= int(t) <= int(b) \
                and "–" in m.group(0):
            found = True
    if not found:
        uncited.append(t)
print(f"Numbered equations: {len(tags)}; not cited by number: {uncited or 'none'}")

for f in sorted(os.listdir(V2)):
    if f.endswith(".md") and not f.startswith("_"):
        t = open(os.path.join(V2, f), encoding="utf-8").read()
        n = t.count("[NEED VALUE")
        if n:
            print(f"[NEED VALUE] in {f}: {n}")
for bad in ("CAN_TAC_GIA", "check exact", "fourteenfold", "near-blind in practice",
            "7–9 %", "\u2014"):
    if bad in ms:
        print(f"WARNING: '{bad}' still in manuscript")
