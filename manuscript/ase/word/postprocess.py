"""Post-process the pandoc output: data tables get top, header and bottom
rules only (no vertical rules); equation tables get no borders; continuous
line numbers are switched on."""
import re, sys
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
path = sys.argv[1]
lines = len(sys.argv) > 2 and sys.argv[2] == "--line-numbers"
d = Document(path)


def borders(el, spec):
    b = el.find(qn("w:tblBorders")) if el.tag == qn("w:tblPr") else el.find(qn("w:tcBorders"))
    if b is not None:
        el.remove(b)
    b = OxmlElement("w:tblBorders" if el.tag == qn("w:tblPr") else "w:tcBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        if el.tag == qn("w:tcPr") and side in ("insideH", "insideV"):
            continue
        e = OxmlElement(f"w:{side}")
        v = spec.get(side)
        e.set(qn("w:val"), "single" if v else "nil")
        if v:
            e.set(qn("w:sz"), str(v)); e.set(qn("w:space"), "0"); e.set(qn("w:color"), "000000")
        b.append(e)
    el.append(b)


TEXT_W = 9070  # twips, 16 cm


def xtext(el):
    return "".join(x.text or "" for x in el.iter() if x.tag in (qn("w:t"), qn("m:t")))


def set_widths(t, fracs):
    grid = t._tbl.tblGrid
    for gc, f in zip(grid.findall(qn("w:gridCol")), fracs):
        gc.set(qn("w:w"), str(int(TEXT_W * f)))
    for row in t.rows:
        for tc, f in zip(row._tr.findall(qn("w:tc")), fracs):
            pr = tc.get_or_add_tcPr()
            w = pr.find(qn("w:tcW"))
            if w is None:
                w = OxmlElement("w:tcW"); pr.insert(0, w)
            w.set(qn("w:type"), "dxa"); w.set(qn("w:w"), str(int(TEXT_W * f)))


for t in d.tables:
    tblPr = t._tbl.tblPr
    eq = len(t.rows) == 1 and len(t.columns) == 2 and re.fullmatch(r"\([A-Z]?\.?\d+\)", t.cell(0, 1).text.strip() or "")
    if eq:
        borders(tblPr, {})
        set_widths(t, (0.88, 0.12))
        for tc in t.rows[0]._tr.findall(qn("w:tc")):
            v = OxmlElement("w:vAlign"); v.set(qn("w:val"), "center")
            tc.get_or_add_tcPr().append(v)
        continue
    # column widths proportional to content (capped), so long headers do not squeeze numbers
    ncol = len(t._tbl.tblGrid.findall(qn("w:gridCol")))
    wts = [4.0] * ncol
    for row in t.rows:
        for j, tc in enumerate(row._tr.findall(qn("w:tc"))[:ncol]):
            txt = xtext(tc)
            longest = max((len(w) for w in txt.split()), default=0)
            wts[j] = max(wts[j], longest + 1.5, 0.6 * min(len(txt), 30))
    set_widths(t, [w / sum(wts) for w in wts])
    borders(tblPr, {"top": 8, "bottom": 8})
    for tc in t.rows[0]._tr.findall(qn("w:tc")):  # header bottom rule
        borders(tc.get_or_add_tcPr(), {"bottom": 6})
# tight lists outside tables: body size instead of the 10 pt table style
for par in d.paragraphs:
    if par.style is not None and par.style.name == "Compact":
        par.style = d.styles["Body Text"]
if lines:
    for s in d.sections:
        ln = OxmlElement("w:lnNumType")
        ln.set(qn("w:countBy"), "1"); ln.set(qn("w:restart"), "continuous"); ln.set(qn("w:distance"), "283")
        pg = s._sectPr.find(qn("w:pgSz"))
        (pg.addnext(ln) if pg is not None else s._sectPr.append(ln))
d.save(path)
