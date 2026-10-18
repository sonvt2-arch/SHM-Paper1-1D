#!/usr/bin/env bash
# Build the v4 Word files from the Markdown sources.
#   bash manuscript/v4/word/build_docx.sh [--pdf]
# Needs pandoc (>= 3.1), python3 with python-docx; --pdf also needs LibreOffice.
set -euo pipefail
W="$(cd "$(dirname "$0")" && pwd)"; S="$(dirname "$W")"; B="$W/build"
mkdir -p "$B"
python3 "$W/make_reference.py" "$B/reference.docx"
python3 "$W/prep_md.py" "$S/manuscript.md" "$B/manuscript_build.md"
pandoc "$B/manuscript_build.md" -f markdown+tex_math_dollars-implicit_figures \
  --reference-doc="$B/reference.docx" --lua-filter="$W/eqnum.lua" \
  --resource-path="$S" -o "$W/Manuscript_v4.docx"
python3 "$W/postprocess.py" "$W/Manuscript_v4.docx" --line-numbers
pandoc "$S/cover_letter_SCHM.md" -f markdown+hard_line_breaks --reference-doc="$B/reference.docx" \
  -o "$W/Cover_Letter_v4.docx"
python3 "$W/postprocess.py" "$W/Cover_Letter_v4.docx"
if [[ "${1:-}" == "--pdf" ]]; then
  SOFFICE=$(ls /root/.claude/skills/synced/*/docx/scripts/office/soffice.py 2>/dev/null | head -1 || true)
  for f in Manuscript_v4 Cover_Letter_v4; do
    if [[ -n "$SOFFICE" ]]; then python3 "$SOFFICE" --headless --convert-to pdf --outdir "$B" "$W/$f.docx"
    else soffice --headless --convert-to pdf --outdir "$B" "$W/$f.docx"; fi
  done
fi
echo "Built: $W/Manuscript_v4.docx, $W/Cover_Letter_v4.docx"
