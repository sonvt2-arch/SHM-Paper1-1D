"""Convert a markdown manuscript with numbered [n] citations and an Elsevier-style
numbered reference list into Sage Harvard (author-year) style.

usage: python3 harvard.py in.md out.md
Narrative citations ("Ojio and Yamada [23]") become "Ojio and Yamada (2002)".
Prints a report of anything it could not parse.
"""
import re, sys
from collections import defaultdict

src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8").read()
head, refs_block = re.split(r"(?m)^## References\s*$", t, maxsplit=1)
m = re.search(r"(?m)^(## |---)", refs_block)
refs_txt, tail = (refs_block[:m.start()], refs_block[m.start():]) if m else (refs_block, "")

INIT = r"(?:[A-ZÀ-Ž][a-z]?\.(?:[\-\s]?[A-ZÀ-Ž][a-z]?\.)*)"
FIX = {"in Genoa. Italy, ": "in Genoa, Italy. "}
CORP = {"EN 1991-2:2003": "CEN", "AASHTO": "AASHTO"}
refs = {}
for line in refs_txt.strip().splitlines():
    mm = re.match(r"\[(\d+)\]\s+(.*)", line.strip())
    if not mm:
        continue
    n, body = int(mm.group(1)), mm.group(2)
    parts = [p.strip() for p in body.split(", ")]
    authors, i, eds = [], 0, False
    while i < len(parts):
        p = parts[i]
        if p == "et al.":
            authors.append(("et al.", "")); i += 1; continue
        a = re.match(rf"^({INIT})\s+(.+?)(\s*\(Eds\.\))?$", p)
        if a and len(a.group(2).split()) <= 3:
            authors.append((a.group(2), a.group(1))); eds = eds or bool(a.group(3)); i += 1
        else:
            break
    rest = ", ".join(parts[i:])
    if not authors:
        key = body.split(",")[0]
        authors = [(CORP.get(key, key), "")]
        rest = body
        if key in CORP:
            rest = body
    yrs = re.findall(r"\((\d{4})\)|, (\d{4})[.,]", rest)
    year = next((a or b for a, b in reversed(yrs)), "n.d.")
    refs[n] = dict(authors=authors, eds=eds, rest=rest, year=year, raw=body)

def cite_name(r):
    a = [s for s, _ in r["authors"] if s != "et al."]
    etal = any(s == "et al." for s, _ in r["authors"])
    if len(a) == 1 and not etal:
        return a[0]
    if len(a) == 2 and not etal:
        return f"{a[0]} and {a[1]}"
    return f"{a[0]} et al."

# disambiguate identical name+year
groups = defaultdict(list)
for n in sorted(refs):
    groups[(cite_name(refs[n]), refs[n]["year"])].append(n)
for (nm, y), ns in groups.items():
    if len(ns) > 1:
        for k, n in enumerate(ns):
            refs[n]["year"] = y + "abcdefgh"[k]

def expand(s):
    out = []
    for p in s.split(","):
        p = p.strip()
        if re.match(r"^\d+\s*[–-]\s*\d+$", p):
            a, b = map(int, re.split(r"\s*[–-]\s*", p)); out += list(range(a, b + 1))
        else:
            out.append(int(p))
    return out

missing = set()
def repl(mt):
    ns = expand(mt.group(1))
    for n in ns:
        if n not in refs:
            missing.add(n)
    pre = head_txt[max(0, mt.start() - 80):mt.start()]
    if len(ns) == 1 and ns[0] in refs:
        nm = cite_name(refs[ns[0]])
        if pre.rstrip().endswith(nm):
            return f"({refs[ns[0]]['year']})"
    items = [f"{cite_name(refs[n])}, {refs[n]['year']}" for n in ns if n in refs]
    return "(" + "; ".join(items) + ")"

head_txt = head
new_head = re.sub(r"\[(\d+(?:\s*[–,-]\s*\d+)*)\]", repl, head)
new_head = re.sub(r" \(([^()]*)\) \(", r" (\1; ", new_head)  # merge "(A) (B)" rarely produced

def fmt_ref(r):
    names = []
    for s, ini in r["authors"]:
        if s == "et al.":
            names.append("et al."); continue
        names.append(f"{s} {ini.replace('.', '').replace(' ', '').replace('-', '')}".strip())
    if len(names) > 1 and names[-1] != "et al.":
        au = ", ".join(names[:-1]) + " and " + names[-1]
    else:
        au = ", ".join(names).replace(", et al.", " et al.")
    if r["eds"]:
        au += " (eds)"
    rest = r["rest"]
    y0 = r["year"][:4]
    if re.search(rf"\s\({y0}\)(?=\s|$)", rest):
        rest = re.sub(rf"\s\({y0}\)(?=\s|$)", "", rest)
    else:
        rest = re.sub(r", \d{4}([.,])", r"\1", rest)
    rest = re.sub(r"(\d+) \((\S+)\) ", r"\1(\2): ", rest)
    rest = re.sub(r" (\d+) (\d[\d–]*)\. (https|DOI)", r" \1: \2. \3", rest)
    rest = re.sub(r" (\d+) (\d[\d–]*)\.?$", r" \1: \2.", rest)
    rest = re.sub(r"https://doi\.org/(\S+)", r"DOI: \1.", rest).rstrip(".") + "."
    if r["authors"] and r["authors"][0][1] == "" and r["rest"] == r["raw"]:
        return f"{au} ({r['year']}) {rest[len(au)+2:] if rest.startswith(au) else rest}"
    bits = rest.split(", ")
    k = 1
    while k < len(bits) - 1 and (bits[k][:1].islower() or bits[k][:1].isdigit() and not re.search(r"\d+[(:]", bits[k])):
        k += 1
    title, venue = ", ".join(bits[:k]), ", ".join(bits[k:])
    out = f"{au} ({r['year']}) {title.rstrip('.')}. {venue}"
    for a, b in FIX.items():
        out = out.replace(a, b)
    return out

lst = sorted(refs.values(), key=lambda r: (cite_name(r).lower().replace("ž", "z"), r["year"]))
ref_out = "\n\n".join(fmt_ref(r) for r in lst)
open(dst, "w", encoding="utf-8").write(new_head + "## References\n\n" + ref_out + "\n\n" + tail)
print("refs", len(refs), "missing", sorted(missing))
