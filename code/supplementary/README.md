# Supplementary scripts: manuscript v4 (SCHM)

Scripts and console logs for the manuscript

> *Blind loci and design criteria for integral load-monitoring channels on continuous girder bridges, with laboratory verification and an assessment on public field records* (`manuscript/v4/manuscript.md`).

This README is the entry point for the supplementary package of manuscript v4. The scripts are listed where they live; nothing is duplicated. Every number in the manuscript is traced to a log or CSV in `manuscript/v4/traceability.md`. Older material (the two-span and laboratory scripts `s01`–`s05` and the `code/analysis/` scripts) keeps its original, SCHM-v2 equation and table numbers; the second half of this README describes it.

## Manuscript v4: where each result comes from

Run each script from its own folder with `python3 <script>.py` (the `theory2` and `norbwim` scripts import sibling modules, so do not use `-I` for them). All are deterministic; rerunning them regenerates the committed logs and CSV files unchanged.

| v4 location | Script | Log / results |
|---|---|---|
| §2.2, Table 1, App. A–B (blind loci of all channels, strain ring, 981 FE checks) | `code/theory2/gc_theory.py`, `gc_fe.py`, `gc_force_method.py`, `verify_general.py`, `gc_results.py` | `code/theory2/logs/verify_general.log`, `gc_results.log`, `results/gc_T*.csv` |
| Figs. 3, 8; Figs. S5–S6 | `code/theory2/gc_figures.py` | `code/theory2/figures/fig_gc_*` |
| §2.4, Fig. 4, Figs. S7–S9 (GLS, zero-sum weights, placement, Monte Carlo, structure-aware weights); §5.3 placement at Cầu Mây | `code/theory2/multisensor_core.py`, `multisensor_theory.py`, `multisensor_placement.py`, `multisensor_mc.py`, `multisensor_figures.py` | `code/theory2/logs/multisensor_*.log`, `results/T*.csv`, `placement_*.csv`, `mc_summary.csv` |
| §2.5, App. C (Möbius law, adjoint sensitivities, Eq. 16) | `code/theory2/ident_theory.py` | `code/theory2/logs/ident_theory.log` |
| §5.2, Table 5, Fig. 9 (static admissible sets against τ, model-form variants) | `code/theory2/ident_static.py` | `code/theory2/logs/ident_static.log`, `ident_static_scan.npz` |
| §5.2 priors, supplement frequency interpretation, Figs. S10–S11 | `code/theory2/ident_freq.py` | `code/theory2/logs/ident_freq.log` |
| §5.3 Cramér–Rao bounds (evaluation points A and B) | `code/theory2/ident_fisher.py` | `code/theory2/logs/ident_fisher.log` |
| §4.1 crossing integrals, speeds, noise windows | `code/norbwim/nb_io.py`, `nb_events.py`, `nb_field.py` (reads `data/public/...`) | `code/norbwim/logs/field.log`, `results/events_field.csv`, `events_field_qc.csv` |
| §4.2–4.4, Tables 3–4, Figs. 6–7, Figs. S1–S2 (all channels, 95 % CIs, TOST, speed, noise covariance, out-of-sample estimators, lane, superposition) | `code/norbwim/nb_v4.py` (about 35 s) | `code/norbwim/logs/v4.log`, `results/v4_*.csv`; narrative in `docs/pkg1/v4_norbwim_reanalysis.md` |
| §4.4 gauge ratios with standard errors; Fig. 5; Figs. S3–S4 | `code/norbwim/nb_tests.py`, `nb_beam.py`, `nb_fig1.py`, `nb_fe_veb.py` | `code/norbwim/logs/tests.log`, `fe_veb.log`, `results/test_*.csv` |
| §4.4 beam-model span shares and $r^2$; Table 7 (offset bias over the static set) | `code/v3/v3_numbers.py` | `code/v3/logs/v3_numbers.log` |
| Table 6 (predicted discriminating measurements) | `code/fieldplan/fieldplan_compute.py` | `code/fieldplan/results/fieldplan_compute.log` (figure labels in this script are still Vietnamese; its figures are not used in v4) |
| §3, Table 2, supplementary laboratory material | `code/supplementary/s01`–`s05` (below) | `code/supplementary/logs/` |
| Word counts and placeholder check | `code/analysis/wp7b_checks.py manuscript/v4` | console |

Figure files for the manuscript are copied into `manuscript/v4/figures/`; `manuscript/v4/figure_table_plan.md` maps each to its script. The Word and PDF files are built with `bash manuscript/v4/word/build_docx.sh --pdf`.

## Legacy material (SCHM-v2 numbering)

The following sections describe the scripts written for the SCHM v2 manuscript (`manuscript/schm/manuscript.md`). Their equation, table and section numbers refer to that version.

## How to run

```bash
pip install -r code/supplementary/requirements.txt
bash code/supplementary/run_all.sh                  # s01-s05, about 3 min, logs -> code/supplementary/logs/
bash code/supplementary/run_all.sh --with-analysis  # also re-runs the code/analysis scripts (writes inside code/analysis and figures/)
```

Each script can also be run on its own with `python3 -I code/supplementary/<script>.py`. Isolated mode works because each script puts its own directory on `sys.path`. Units are N and mm unless a script states otherwise (`s05` works in SI). All random numbers come from a fixed seed (`s04`: 20260817).

## Scripts in this folder

| Script | Reproduces (SCHM manuscript) | Log |
|---|---|---|
| `beam_theory.py` | Shared module: specimen constants (Section 3.1), influence line Eq. (A.2), closed form Eqs. (4)–(5), Table C.1 records, quadrature Eq. (12) (Simpson with a 3/8 end panel), BPM/SLM Eq. (11), prismatic Hermite FE (stiffness, consistent mass, moving point load). Run alone, it prints I, EI, P0 and C_m. | `logs/beam_theory.log` |
| `s01_symbolic_two_span.py` | Appendix A: Eq. (A.1), Eq. (A.2) derived twice (force method; double integration plus Maxwell), continuity, 64EI, 2.875/71.9 %/0.480l/72.1 %, span-wise decomposition, Table A.1. Sections 2.1–2.2: C_m = l⁴/192EI, Eqs. (4)–(5) from first principles, Table 1 (closed form against two FE routes of Eq. (3)), Eq. (6), Eq. (7) ρ_L = (3+√33)/6 and ξ* = (1+√33)/16, 1.039895, the ρ_L = 1.6 and 1.45 statements, near-blind band, 3644 mm. Section 2.4: R_m = 4/7, O_m = 2√44765/1279 and its monotonicity. | `logs/s01_symbolic_two_span.log` |
| `s02_quadrature_table3.py` | Table 3 (2501.19, 2488.68, 2501.85, 2513.43); 20/21/23 intervals and Simpson with a 3/8 end panel (Section 3.2); trapezoid O(Δx²) convergence; Section 6.1 quadrature bias at 300 and 375 mm spacing (not reproduced, see report). | `logs/s02_quadrature_table3.log` |
| `s03_load_identification.py` | Table 4 (BPM/SLM), 1.00489, the +1.61 % correction, measured/analytical ratios 1.010/1.016/1.017, Fig. 6 line (slope 62.229, R² = 0.99998, +1.12 %), three-load order (rms 0.030 against 0.55 mm), largest residual (Section 3.2), Table 7, the offset residual (1.2596 − 1.9893) and 58 %/42 % (Section 6.1), 60 % (Section 6.3). | `logs/s03_load_identification.log` |
| `s04_monte_carlo.py` | Appendix B / Table B.1 (Eq. (16) model with gain, zero offset and additive noise; 200 000 realisations; seed 20260817); Section 6.3 (0.07 %, 2.11 → 3.09 %, factor 1.47, BPM 2.12 %); the "three-load agrees within 0.1 pp" claim. | `logs/s04_monte_carlo.log` |
| `s05_moving_force.py` | Section 6.5 / Fig. 10 / Table 9 / Eq. (21): FE (40 Hermite elements per span, consistent mass), Rayleigh damping 2 % at modes 1 and 3, Newmark average acceleration, a constant force crossing at speed v, E_dyn of v∫y dt against C_mP over 47 speeds (T_cr/T₁ = 0.6–120) plus a 300-speed dense sweep. Also checks f₁ = 11.942 Hz (FE and analytical), time-step and mesh convergence, the truncation, window-extension and damping statements, and the multi-axle spread. Also writes `logs/s05_sweep47.csv` and `logs/s05_sweep_dense.csv` (data behind Fig. 10). | `logs/s05_moving_force.log` |
| `run_all.sh`, `requirements.txt` | Driver and dependencies (versions tested listed). | |

## Scripts in `code/analysis/` (three-span theory, Cầu Mây, field records)

These are not duplicated here. Run them from the repository root, or use `run_all.sh --with-analysis`. Their logs, regenerated on 2026-10-18 in a clean copy of the repository and identical to the committed logs in `code/analysis/logs/` (except an absolute path in one line), are in `logs/analysis/`.

| Script | Reproduces | Log |
|---|---|---|
| `code/analysis/cm_multispan.py` | Multi-span FE for C_m with EI(x) (exact non-prismatic flexibility element, influence-line and uniform-load routes, Eq. (3)) | `logs/analysis/cm_multispan.log` |
| `code/analysis/cm_3span_theory.py` | Section 2.3 and Appendix D, symbolic: Eq. (8), μ = 4/5, Eq. (9) β_crit = 1.700594, 2cos(π/9) = 1.879385, band edge 1.621399 (30β³ − 69β − 16 = 0), Eq. (10), 0.964706, Table 2, the asymmetric blind ratios 0.589774 … 0.461410; data for Fig. 3 (`code/analysis/data/obs_map_3span*.csv`) | `logs/analysis/cm_3span_theory.log` |
| `code/analysis/verify_3span.py` | Closed forms against FE: 60 comparisons, max 7.5 × 10⁻¹²; asymmetric cases ≤ 9.2 × 10⁻¹²; Table 2 FE slope ≤ 3.6 × 10⁻⁷; span-wise contributions 1.870395 / −1.902566 / 0.195395, 0.754630, 0.30; haunched FE convergence | `logs/analysis/verify_3span.log` |
| `code/analysis/wp3_sections.py`, `wp3_fe.py`, `wp3_run.py` | Section 4: section properties and polygon check, variable-EI FE, calibrations A and B, Table 5, Table 6, Fig. 7 data (`code/analysis/results/wp3_*.csv`) | `logs/analysis/wp3_run.log` |
| `code/analysis/wp4_dynamic_records.py` | Section 5: event detection, baselines, high-/low-pass filtering, Figs. 8–9 data (`data/bridges/*/wp4_*.csv`) | `logs/analysis/wp4.log` |
| `code/analysis/wp7b_peps.py` | Section 6.2 Table 8 (P_ε and bias), the α = 1.088 and k-sensitivity statements of Section 4.3, near-blind band edges, Table 10 root-sum-square | `logs/analysis/wp7b_peps.log` |
| `code/analysis/schm_figures.py` | Figs. 3, 7, 8, 9, S1 of the SCHM manuscript (values to `manuscript/schm/figures/schm_figures_values.txt`) | not re-run here |

## Early author package (`code/original/files-v2/`)

`logs/files-v2/` holds the console output of `beam_theory.py` and scripts 01–06 of that package, run unchanged on 2026-10-18 (Python 3.13, NumPy 2.5.3, SciPy 1.18.1, SymPy 1.14). Script 06 fails because `pdflatex` is absent, and script 05 skips the photograph panel. The package predates the SCHM text: its equation and table numbers differ, it states the three-load spacing in reverse order, and it has no moving-load study. `REPRODUCTION_REPORT.md` maps its output onto the SCHM numbers.

## What is not here

- The laboratory raw records (each deflection is the mean of three cycles; only the means in Table C.1 exist in the repository).
- The Abaqus model of Section 3.1. The Hermite FE in `beam_theory.py` stands in for it; cubic elements are nodally exact, so both give the same nodal influence line.
- The Cầu Mây and field data files are in `data/bridges/`. The availability conditions are in the manuscript's Data Availability section.
