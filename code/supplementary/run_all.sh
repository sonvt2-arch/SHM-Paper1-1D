#!/usr/bin/env bash
# Run every supplementary script and write its console output to logs/.
#
#   bash code/supplementary/run_all.sh                 # s01-s05 (about 3 min)
#   bash code/supplementary/run_all.sh --with-analysis # also the code/analysis scripts
#
# --with-analysis re-runs the three-span and Cau May scripts of code/analysis.
# Those scripts write their own outputs inside the repository
# (code/analysis/logs, code/analysis/results, code/analysis/data, figures/);
# their logs are then copied to logs/analysis/.
# Scripts are run with `python3 -I` (isolated mode); each script puts its own
# directory on sys.path, so the shared module beam_theory.py is found.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
PY="${PYTHON:-python3}"
mkdir -p "$HERE/logs"

for s in beam_theory s01_symbolic_two_span s02_quadrature_table3 s03_load_identification \
         s04_monte_carlo s05_moving_force; do
    echo ">>> $s"
    "$PY" -I -u "$HERE/$s.py" > "$HERE/logs/$s.log" 2>&1
done

if [[ "${1:-}" == "--with-analysis" ]]; then
    mkdir -p "$HERE/logs/analysis"
    cd "$ROOT"
    for s in cm_multispan cm_3span_theory verify_3span; do
        echo ">>> code/analysis/$s.py"
        "$PY" -I "code/analysis/$s.py" > "$HERE/logs/analysis/$s.log" 2>&1
    done
    for s in wp3_run wp4_dynamic_records wp7b_peps; do
        echo ">>> code/analysis/$s.py"
        "$PY" -I "code/analysis/$s.py" > /dev/null 2>&1
    done
    cp code/analysis/logs/wp3_run.log code/analysis/logs/wp4.log \
       code/analysis/logs/wp7b_peps.log "$HERE/logs/analysis/"
fi
echo "done; logs in $HERE/logs"
