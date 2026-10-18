# Supplementary scripts: SCHM submission

Scripts and console logs for the manuscript

> *Total-load observability of continuous girder bridges from a single deflection channel: closed-form blind configurations, laboratory verification and sensor placement on an in-service box girder* (`manuscript/schm/manuscript.md`).

These are the supplementary scripts that the manuscript's "Computational Implementation", "Data Availability" and "Supplementary Materials" sections refer to. The two-span and laboratory scripts (`s01`–`s05`) were rebuilt from the authors' early package `code/original/files-v2/`; the later JCSHM package was not available. The three-span and Cầu Mây analyses live in `code/analysis/`. They are listed below rather than copied. Every manuscript number checked, and whether it reproduces, is listed in [`REPRODUCTION_REPORT.md`](REPRODUCTION_REPORT.md).

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
