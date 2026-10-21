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
    eq = len(t.rows) == 1 and len(t.columns) == 3 and re.fullmatch(r"\([A-Z]?\.?\d+\)", t.cell(0, 2).text.strip() or "")
    jc = tblPr.find(qn("w:jc"))
    if jc is None:
        jc = OxmlElement("w:jc"); tblPr.append(jc)
    jc.set(qn("w:val"), "center")  # tables centred horizontally (V.1.1)
    if eq:
        borders(tblPr, {})
        set_widths(t, (0.1, 0.8, 0.1))
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
    # numeric columns right-aligned, text columns left-aligned (V.1.1)
    NUM = re.compile(r"^[\s\-−–+]*[\d.,]+[\d.,\s×⁻⁰-⁹eE()%–\-−a-dᵃᵇ]*$")
    body = t.rows[1:]
    for j in range(ncol):
        vals = [xtext(r._tr.findall(qn("w:tc"))[j]).strip() for r in body if len(r._tr.findall(qn("w:tc"))) > j]
        vals = [v for v in vals if v and v not in ("–", "-")]
        numeric = bool(vals) and sum(bool(NUM.match(v)) for v in vals) >= 0.7 * len(vals)
        for r in t.rows:
            tcs = r._tr.findall(qn("w:tc"))
            if len(tcs) > j:
                for p_ in tcs[j].iter(qn("w:p")):
                    ppr = p_.find(qn("w:pPr"))
                    if ppr is None:
                        ppr = OxmlElement("w:pPr"); p_.insert(0, ppr)
                    for old in ppr.findall(qn("w:jc")):
                        ppr.remove(old)
                    jc_ = OxmlElement("w:jc"); jc_.set(qn("w:val"), "right" if numeric else "left"); ppr.append(jc_)
    # header row repeats on page breaks; rows do not split
    trPr = t.rows[0]._tr.get_or_add_trPr()
    h = OxmlElement("w:tblHeader"); h.set(qn("w:val"), "true"); trPr.append(h)
    for row in t.rows:
        cs = OxmlElement("w:cantSplit"); row._tr.get_or_add_trPr().append(cs)
    for tc in t.rows[0]._tr.findall(qn("w:tc")):  # header bottom rule
        borders(tc.get_or_add_tcPr(), {"bottom": 6})
# upright (sty p) multi-letter subscripts such as "tot", "max": pandoc writes one
# math run per letter; merge neighbouring runs with identical properties so
# Word shows and edits them as one upright word
from lxml import etree
M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"
def _props(r):
    p = r.find(M + "rPr")
    return etree.tostring(p) if p is not None else b""
for parent in list(d.element.body.iter(M + "sub", M + "sup", M + "e", M + "oMath", M + "num", M + "den")):
    runs = [c for c in parent if c.tag == M + "r"]
    for a in runs:
        b = a.getnext()
        while b is not None and b.tag == M + "r" and a.getparent() is not None and _props(a) == _props(b) and b"sty" in _props(a):
            ta, tb = a.find(M + "t"), b.find(M + "t")
            if ta is None or tb is None or not (ta.text or "").isalpha() or not (tb.text or "").isalpha():
                break
            ta.text += tb.text
            nb = b.getnext(); parent.remove(b); b = nb
# multi-letter upright words in math (tot, ref, max, Var) also as normal text: LibreOffice's
# OMML import ignores sty p and would set them in italic in the PDF; Word shows them upright either way
for r in d.element.body.iter(M + "r"):
    pr, t_ = r.find(M + "rPr"), r.find(M + "t")
    if pr is None or t_ is None or pr.find(M + "sty") is None or pr.find(M + "nor") is not None:
        continue
    if (t_.text or "").isalpha():
        pr.append(OxmlElement("m:nor"))
# delimiters: drop the empty separator pandoc writes; LibreOffice then ignores endChr and
# closes "[" and "|" with ")" in the PDF (Word shows the same either way: one element, no separator)
for dp in list(d.element.body.iter(M + "dPr")):
    for sc in dp.findall(M + "sepChr"):
        if (sc.get(M + "val") or "") == "":
            dp.remove(sc)
# table titles stay with their table; figures stay with their captions
for par in d.paragraphs:
    if re.match(r"Table S?\d+\.", par.text.strip()):
        par.paragraph_format.keep_with_next = True
# page layout: symbol-table heading stays with its table; captions do not split across pages;
# short tables (and their footnotes) stay on one page
for par in d.paragraphs:
    s_ = par.text.strip()
    if s_.startswith("Principal symbols"):
        par.paragraph_format.keep_with_next = True
    if re.match(r"(Fig\.|Figure) S?\d+\.", s_) or re.match(r"Table S?\d+\.", s_):
        par.paragraph_format.keep_together = True
for t in d.tables:
    if len(t.rows) > 20:
        continue
    nxt = t._tbl.getnext()
    foot = nxt is not None and nxt.tag == qn("w:p") and xtext(nxt).strip()[:1] in ("ᵃ", "ᵇ", "*")
    rows = t.rows if foot else t.rows[:-1]
    for row in rows:
        for p_ in row._tr.iter(qn("w:p")):
            ppr = p_.find(qn("w:pPr"))
            if ppr is None:
                ppr = OxmlElement("w:pPr"); p_.insert(0, ppr)
            if ppr.find(qn("w:keepNext")) is None:
                ppr.insert(0, OxmlElement("w:keepNext"))
# lines broken by hand (address and signature blocks) are left-aligned, not stretched
for par in d.paragraphs:
    if par._p.findall(".//" + qn("w:br")) and par.alignment in (None, 3):
        par.paragraph_format.alignment = 0
# cover letter: single spacing so that it fits on one page (Quy tac VI.1)
if "--letter" in sys.argv:
    from docx.shared import Pt
    for par in d.paragraphs:
        pf = par.paragraph_format
        pf.line_spacing = 1.0
        pf.space_after = Pt(6)
        pf.space_before = Pt(0)
# reference list: left aligned with a hanging indent (justification stretches DOIs)
from docx.shared import Cm
inref = False
for par in d.paragraphs:
    if par.style is not None and par.style.name.startswith("Heading"):
        inref = par.text.strip() in ("References",)
        continue
    if inref and par.text.strip():
        pf = par.paragraph_format
        pf.alignment = 0; pf.left_indent = Cm(0.75); pf.first_line_indent = Cm(-0.75)
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
# operator-only scripts (A^+, xi^*) and lone bars as normal text: LibreOffice's OMML import
# otherwise reads them as operators without operands and prints an error glyph in the PDF
for r in d.element.body.iter(qn("m:r")):
    t = r.find(qn("m:t"))
    if t is None or t.text is None:
        continue
    par = r.getparent()
    lone_bar = t.text == "|"
    op_script = t.text in "+-\u2212*\u2217\u22c6" and len(t.text) == 1 and par.tag in (qn("m:sup"), qn("m:sub")) and len(par) == 1
    if lone_bar or op_script:
        old = r.find(qn("m:rPr"))
        if old is not None:
            r.remove(old)
        pr = OxmlElement("m:rPr"); pr.append(OxmlElement("m:nor")); r.insert(0, pr)
# overbars as U+00AF (LibreOffice draws U+203E as an acute accent); no line break between a number and its unit
for c in d.element.body.iter(qn("m:chr")):
    if c.get(qn("m:val")) == "\u203e":
        c.set(qn("m:val"), "\u00af")
UNIT = re.compile(r"(\d) (?=(%|mm|m|N|kN|t|Hz|s|µε|µrad|kN m|kN m/rad|m²/kN)(?![\w²]))")
for t in d.element.body.iter(qn("w:t")):
    if t.text and " " in t.text:
        t.text = UNIT.sub("\\1\u00a0", t.text)
d.save(path)
# docProps/app.xml from the pandoc template carries stale statistics (1 page, 83 words, Word 12.0);
# replace it with an empty properties part
import zipfile, shutil, tempfile
APP = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
       '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" '
       'xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"/>')
tmp = tempfile.mktemp(suffix=".docx")
with zipfile.ZipFile(path) as zi, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
    for it in zi.infolist():
        data = APP.encode() if it.filename == "docProps/app.xml" else zi.read(it.filename)
        zo.writestr(it, data)
shutil.move(tmp, path)
