#!/usr/bin/env bash
# Run every supplementary script and write its console output to logs/.
#
#   bash code/supplementary/run_all.sh                 # s01-s05 (about 3 min)
#   bash code/supplementary/run_all.sh --with-analysis # also the code/analysis scripts
#   bash code/supplementary/run_all.sh --all           # also every remaining analysis (about 20 min)
#
# --all runs, each from its own folder, the scripts of code/theory2 (closed forms,
# FE checks, multi-channel placement and Monte Carlo, identifiability),
# code/norbwim (public field records; needs data/public/norbwim_figshare26880898),
# code/v3, code/fieldplan and the figure scripts of code/v4. Each script writes
# its own log in its folder (logs/ or results/).
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
         s04_monte_carlo s05_moving_force s06_threshold_sensitivity; do
    echo ">>> $s"
    "$PY" -I -u "$HERE/$s.py" > "$HERE/logs/$s.log" 2>&1
done

if [[ " $* " == *" --with-analysis "* ]]; then
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
if [[ " $* " == *" --all "* ]]; then
    run_in() { local d="$1"; shift; for s in "$@"; do
        echo ">>> code/$d/$s.py"; (cd "$ROOT/code/$d" && "$PY" -u "$s.py" > /dev/null); done; }
    run_in theory2 gc_theory gc_fe gc_force_method verify_general gc_results gc_figures \
        multisensor_theory multisensor_placement multisensor_mc multisensor_figures \
        ident_theory ident_static ident_freq ident_fisher
    run_in norbwim nb_field nb_v4 nb_tests nb_beam nb_fig1 nb_fe_veb
    run_in v3 v3_numbers
    run_in fieldplan fieldplan_compute
    run_in v4 fig1_beams figS1_lab_il
fi
echo "done; logs in $HERE/logs"
