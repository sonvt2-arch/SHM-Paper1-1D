"""Compare the numeric tokens of two manuscript versions.

Run:  python3 code/v4/num_diff.py OLD.md NEW.md

Numbers are extracted from the whole file (prose, tables, math). Before
extraction, LaTeX subscripts (C_8, r_{87}) and cross-reference numbers
(Table n, Tables n, Fig(s). n, Eq(s). (n), Section(s) n.n, Appendix) are
removed and counted separately, because they are labels, not data.
The report lists (1) distinct values present in one file only (true losses
or additions), (2) multiset count changes, split by location (table rows vs
prose), and (3) cross-reference label counts.
"""
import re
import sys
from collections import Counter

NUM = re.compile(r"(?<![A-Za-z])\d+(?:[.,]\d+)?")
SUB = re.compile(r"_\{[^}]*\}|_[A-Za-z0-9]")
XREF = re.compile(r"\b(?:Tables?|Figs?\.|Eqs?\.|Sections?|Appendix|Appendices)\s*\(?[\dA-Z][\d.]*\)?"
                  r"(?:\s*(?:and|–|-|,)\s*\(?\d[\d.]*\)?)*")


def load(path):
    text = open(path, encoding="utf-8").read()
    xrefs = Counter(m.group(0) for m in XREF.finditer(text))
    clean = XREF.sub(" ", text)
    clean = SUB.sub(" ", clean)
    prose, table = Counter(), Counter()
    for line in clean.splitlines():
        target = table if line.lstrip().startswith("|") else prose
        target.update(NUM.findall(line))
    return prose, table, xrefs


def main(old, new):
    op, ot, ox = load(old)
    np_, nt, nx = load(new)
    oall, nall = op + ot, np_ + nt
    lost = sorted(set(oall) - set(nall), key=lambda v: float(v.replace(",", ".")))
    added = sorted(set(nall) - set(oall), key=lambda v: float(v.replace(",", ".")))
    print(f"Distinct numeric values: old {len(oall)}, new {len(nall)}")
    print("Values in OLD only (disappeared entirely):", lost or "none")
    print("Values in NEW only (appeared entirely):", added or "none")
    print("\nMultiset changes (value: old prose/table -> new prose/table):")
    for v in sorted(set(oall) | set(nall), key=lambda v: float(v.replace(",", "."))):
        a = (op[v], ot[v]); b = (np_[v], nt[v])
        if a != b:
            tag = ""
            if sum(a) == sum(b):
                tag = "moved prose<->table, total unchanged"
            elif sum(b) < sum(a):
                tag = f"total -{sum(a) - sum(b)}"
            else:
                tag = f"total +{sum(b) - sum(a)}"
            print(f"  {v}: {a[0]}/{a[1]} -> {b[0]}/{b[1]}  ({tag})")
    print(f"\nTotal tokens: old {sum(oall.values())}, new {sum(nall.values())}")
    print("\nCross-reference labels whose count changed:")
    for k in sorted(set(ox) | set(nx)):
        if ox[k] != nx[k]:
            print(f"  {k!r}: {ox[k]} -> {nx[k]}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
