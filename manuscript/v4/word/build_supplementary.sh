#!/usr/bin/env bash
# Build Supplementary_Material_v4.docx (and .pdf with --pdf) from ../supplementary_material.md,
# embedding Figs. S1-S14 above their captions.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/../supplementary_material.md"
FIG="$HERE/../figures/supplementary"
mkdir -p "$HERE/build"
python3 - "$SRC" "$FIG" "$HERE/build/supplementary_build.md" <<'PY'
import sys, re, glob, os
src, fig, out = sys.argv[1:]
t = open(src, encoding="utf-8").read()
files = {int(re.findall(r"FigS(\d+)_", f)[0]): f for f in glob.glob(os.path.join(fig, "FigS*.png"))}
def rep(m):
    n = int(m.group(1))
    img = f"![]({files[n]}){{width=15.5cm}}\n\n" if n in files else ""
    return img + m.group(0)
t = re.sub(r"^\*\*Fig\. S(\d+)\.\*\*", rep, t, flags=re.M)
open(out, "w", encoding="utf-8").write(t)
PY
REF="$HERE/build/reference.docx"
ARGS=(--from markdown+tex_math_dollars --to docx -o "$HERE/Supplementary_Material_v4.docx")
[ -f "$REF" ] && ARGS+=(--reference-doc "$REF")
pandoc "$HERE/build/supplementary_build.md" "${ARGS[@]}"
if [ "${1:-}" = "--pdf" ]; then
  (cd "$HERE" && soffice --headless --convert-to pdf Supplementary_Material_v4.docx >/dev/null 2>&1 || true)
fi
echo "Built: $HERE/Supplementary_Material_v4.docx"
