/*
 * docx_helpers.js
 * ===============
 * Small helper layer over docx-js used by 07_build_docx.js:
 *   rt()        inline mark-up parser (*italic*, **bold**, _sub_, ^sup^)
 *   P/H1/H2/H3  paragraph and heading builders
 *   eq()        inserts an equation PNG with a right-aligned number
 *   fig()       inserts a figure PNG with its caption
 *   tbl()       three-line (booktabs-style) table
 */

const fs = require('fs');
const d = require('docx');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, ImageRun,
        Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType, ExternalHyperlink,
        PageBreak, Footer, Header, PageNumber, TabStopType, convertInchesToTwip } = d;

const sizeOf = (p) => { const b = fs.readFileSync(p); // PNG header
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) }; };

const FIG = 'figs/', EQ = 'eqs/';
const BODYPX = 600;                       // usable width in docx "pixels"

function eq(name, num, scale = 1/6.25) {
  const { w, h } = sizeOf(EQ + name + '.png');
  let W = w * scale, H = h * scale;
  if (W > 470) { H = H * 470 / W; W = 470; }
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [8100, 1260],
    borders: noBorders(),
    rows: [ new TableRow({ children: [
      new TableCell({ width: { size: 8100, type: WidthType.DXA }, margins:{top:60,bottom:60},
        children: [ new Paragraph({ alignment: AlignmentType.CENTER, children: [
          new ImageRun({ type: 'png', data: fs.readFileSync(EQ + name + '.png'),
                         transformation: { width: Math.round(W), height: Math.round(H) } })] })] }),
      new TableCell({ width: { size: 1260, type: WidthType.DXA }, verticalAlign: 'center',
        children: [ new Paragraph({ alignment: AlignmentType.RIGHT,
          children: [ new TextRun({ text: '(' + num + ')', font: 'Times New Roman', size: 22 }) ] })] })
    ]})]
  });
}

function noBorders() {
  const n = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
  return { top: n, bottom: n, left: n, right: n, insideHorizontal: n, insideVertical: n };
}

function fig(name, capNum, capText, widthPx) {
  const { w, h } = sizeOf(FIG + name + '.png');
  const W = widthPx || BODYPX, H = Math.round(h * W / w);
  return [
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200, after: 80 },
      children: [ new ImageRun({ type: 'png', data: fs.readFileSync(FIG + name + '.png'),
        transformation: { width: W, height: H } }) ] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240 },
      children: rt('Fig. ' + capNum + ' – ' + capText, { size: 18, extra: { bold: true, italics: true } }) })
  ];
}

// ---- inline rich text mini-parser: *italic*, **bold**, _sub_, ^sup^ ----
function rt(s, opts = {}) {
  const base = { font: 'Times New Roman', size: opts.size || 22 };
  const out = []; let buf = ''; let i = 0;
  const push = (t, extra) => { if (t) out.push(new TextRun(Object.assign({}, base, opts.extra||{}, extra, { text: t })));};
  while (i < s.length) {
    if (s.startsWith('**', i)) { const j = s.indexOf('**', i+2); if (j>0){ push(buf); buf=''; push(s.slice(i+2,j), {bold:true}); i=j+2; continue; } }
    if (s[i] === '*') { const j = s.indexOf('*', i+1); if (j>0){ push(buf); buf=''; push(s.slice(i+1,j), {italics:true}); i=j+1; continue; } }
    if (s[i] === '_') { const j = s.indexOf('_', i+1); if (j>0){ push(buf); buf=''; push(s.slice(i+1,j), {subScript:true, italics:true}); i=j+1; continue; } }
    if (s[i] === '^') { const j = s.indexOf('^', i+1); if (j>0){ push(buf); buf=''; push(s.slice(i+1,j), {superScript:true}); i=j+1; continue; } }
    buf += s[i]; i++;
  }
  push(buf);
  return out;
}

const P = (s, o = {}) => new Paragraph({
  alignment: o.align || AlignmentType.JUSTIFIED,
  spacing: { after: o.after === undefined ? 120 : o.after, before: o.before || 0, line: o.line || 260 },
  indent: o.indent === false ? undefined : { firstLine: o.firstLine === undefined ? 340 : o.firstLine },
  children: rt(s, o)
});

const H1 = (n, s) => new Paragraph({ spacing: { before: 320, after: 140 },
  children: [ new TextRun({ text: n + '  ' + s, font: 'Times New Roman', size: 26, bold: true }) ] });
const H2 = (n, s) => new Paragraph({ spacing: { before: 240, after: 120 },
  children: [ new TextRun({ text: n + '  ' + s, font: 'Times New Roman', size: 23, bold: true, italics: true }) ] });
const H3 = (n, s) => new Paragraph({ spacing: { before: 200, after: 100 },
  children: [ new TextRun({ text: n + '  ' + s, font: 'Times New Roman', size: 22, bold: true }) ] });

const BUL = (s) => new Paragraph({ alignment: AlignmentType.JUSTIFIED, bullet: { level: 0 },
  spacing: { after: 80, line: 260 }, children: rt(s) });

function tableCap(n, txt) {
  return new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 220, after: 100 },
    children: rt('Table ' + n + ' – ' + txt, { size: 18, extra: { bold: true, italics: true } }) });
}

function tbl(header, rows, widths, opts = {}) {
  const total = widths.reduce((a, b) => a + b, 0);
  const th = { style: BorderStyle.SINGLE, size: 6, color: '000000' };
  const nb = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
  const mk = (txt, i, o) => new TableCell({
    width: { size: widths[i], type: WidthType.DXA },
    margins: { top: 40, bottom: 40, left: 70, right: 70 },
    shading: o.shade ? { type: ShadingType.CLEAR, fill: o.shade, color: 'auto' } : undefined,
    borders: { top: o.top || nb, bottom: o.bottom || nb, left: nb, right: nb },
    verticalAlign: 'center',
    children: String(txt).split('\n').map(t => new Paragraph({
      alignment: o.align || (opts.alignAll ? opts.alignAll : (i === 0 ? AlignmentType.LEFT : AlignmentType.CENTER)),
      spacing: { after: 0, line: 230 },
      children: rt(t, { size: opts.fs || 17, extra: o.bold ? { bold: true } : {} }) }))
  });
  const rowsOut = [];
  header.forEach((hr, k) => rowsOut.push(new TableRow({ tableHeader: true,
    children: hr.map((t, i) => mk(t, i, { bold: true, shade: 'F2F2F2',
      top: k === 0 ? th : nb, bottom: k === header.length - 1 ? th : nb })) })));
  rows.forEach((r, k) => rowsOut.push(new TableRow({
    children: r.map((t, i) => mk(t, i, { bottom: k === rows.length - 1 ? th : nb })) })));
  return new Table({ width: { size: total, type: WidthType.DXA }, columnWidths: widths,
    borders: noBorders(), rows: rowsOut, alignment: AlignmentType.CENTER });
}

module.exports = { d, Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, ImageRun,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType, PageBreak, Footer, Header,
  PageNumber, eq, fig, P, H1, H2, H3, BUL, tbl, tableCap, rt, noBorders, convertInchesToTwip };
