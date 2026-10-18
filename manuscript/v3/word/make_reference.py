"""Build the pandoc reference document: Times New Roman 12 pt, 1.5 line
spacing, black headings, page numbers in the footer."""
import sys, subprocess
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
out = sys.argv[1]
subprocess.run(["pandoc", "-o", out, "--print-default-data-file", "reference.docx"], check=True)
d = Document(out)
for st in d.styles:
    if st.type != 1:  # paragraph and character styles only
        continue
    try:
        st.font.name = "Times New Roman"
        rpr = st.element.get_or_add_rPr()
        rf = rpr.find(qn("w:rFonts"))
        if rf is None:
            rf = OxmlElement("w:rFonts"); rpr.append(rf)
        for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
            rf.set(qn(a), "Times New Roman")
        for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
            if rf.get(qn(a)) is not None:
                del rf.attrib[qn(a)]
    except Exception:
        pass
sizes = {"Title": 16, "Heading 1": 14, "Heading 2": 12, "Heading 3": 12}
WANT = ("Normal", "Body Text", "First Paragraph", "Compact", "Title", "Heading 1",
        "Heading 2", "Heading 3", "Abstract", "Bibliography", "Author", "Date")
for st in list(d.styles):
    name = st.name
    if st.type != 1 or name not in WANT:
        continue
    st.font.size = Pt(sizes.get(name, 10 if name == "Compact" else 12))
    if name.startswith("Heading") or name == "Title":
        st.font.color.rgb = RGBColor(0, 0, 0)
        c = st.element.rPr.find(qn("w:color"))
        if c is not None and c.get(qn("w:themeColor")) is not None:
            del c.attrib[qn("w:themeColor")]
        st.font.bold = True
        st.font.italic = name == "Heading 3"
    pf = st.paragraph_format
    pf.line_spacing = 1.0 if name == "Compact" else 1.5
    if name in ("Body Text", "First Paragraph"):
        pf.space_after = Pt(6)
# figure placeholder style
try:
    ph = d.styles["Figure placeholder"]
except KeyError:
    ph = d.styles.add_style("Figure placeholder", 1)
ph.base_style = d.styles["Normal"]
ph.font.italic = True
ph.paragraph_format.alignment = 1
sec = d.sections[0]
sec.page_height, sec.page_width = Cm(29.7), Cm(21.0)
for m in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
    setattr(sec, m, Cm(2.5))
p = sec.footer.paragraphs[0] if sec.footer.paragraphs else sec.footer.add_paragraph()
p.alignment = 1
ppr = p._p.get_or_add_pPr()
ppr.append(OxmlElement("w:suppressLineNumbers"))
r = p.add_run()
for tag, txt in (("begin", None), (None, " PAGE "), ("end", None)):
    if tag:
        e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), tag)
    else:
        e = OxmlElement("w:instrText"); e.set(qn("xml:space"), "preserve"); e.text = txt
    r._r.append(e)
d.save(out)
