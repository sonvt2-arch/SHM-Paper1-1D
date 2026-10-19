#!/usr/bin/env bash
# Build the ASE Word/PDF files from the Markdown sources.
#   bash manuscript/ase/word/build_docx.sh [--pdf]
set -euo pipefail
W="$(cd "$(dirname "$0")" && pwd)"; S="$(dirname "$W")"; B="$W/build"
mkdir -p "$B"
python3 "$W/make_reference.py" "$B/reference.docx"
python3 "$W/prep_md.py" "$S/manuscript.md" "$B/manuscript_build.md"
pandoc "$B/manuscript_build.md" -f markdown+tex_math_dollars-implicit_figures \
  --reference-doc="$B/reference.docx" --lua-filter="$W/eqnum.lua" \
  --resource-path="$S" -o "$W/Manuscript_ASE.docx"
python3 "$W/postprocess.py" "$W/Manuscript_ASE.docx" --line-numbers
python3 - "$S/supplementary_material.md" "$S/figures/supplementary" "$B/supplementary_build.md" <<'PY'
import sys, re, glob, os
src, fig, out = sys.argv[1:]
t = open(src, encoding="utf-8").read()
files = {int(re.findall(r"FigS(\d+)_", f)[0]): f for f in glob.glob(os.path.join(fig, "FigS*.png"))}
t = re.sub(r"^\*\*Fig\. S(\d+)\.\*\*", lambda m: (f"![]({files[int(m.group(1))]}){{width=15.5cm}}\n\n" if int(m.group(1)) in files else "") + m.group(0), t, flags=re.M)
open(out, "w", encoding="utf-8").write(t)
PY
pandoc "$B/supplementary_build.md" -f markdown+tex_math_dollars-implicit_figures \
  --reference-doc="$B/reference.docx" -o "$W/Supplementary_Material_ASE.docx"
python3 "$W/postprocess.py" "$W/Supplementary_Material_ASE.docx"
if [[ -f "$S/cover_letter_ASE.md" ]]; then
  pandoc "$S/cover_letter_ASE.md" -f markdown+hard_line_breaks --reference-doc="$B/reference.docx" \
    -o "$W/Cover_Letter_ASE.docx"
  python3 "$W/postprocess.py" "$W/Cover_Letter_ASE.docx"
fi
if [[ "${1:-}" == "--pdf" ]]; then
  for f in "$W"/*.docx; do soffice --headless --convert-to pdf --outdir "$W" "$f" >/dev/null 2>&1 || true; done
fi
echo "Built in $W"
