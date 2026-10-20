# Scripts and console output

This archive holds the scripts, console logs and derived data behind the article *Blind loci and sensor layout for influence-area bridge weigh-in-motion on continuous girders* and its Supplementary Material. Table and figure numbers below are those of the article ("Fig. 3", "Table 2") and of the Supplementary Material ("Fig. S4", "Table S8").

Paths are relative to the repository root (the `code/` folder of this archive). Logs and CSV files are the committed outputs of the scripts; every script is deterministic, so rerunning it regenerates them unchanged. Directory contents:

| Directory | Contents |
|---|---|
| `code/supplementary` | shared module `beam_theory.py`, laboratory and two-span scripts `s01`–`s05`, `run_all.sh`, `requirements.txt`, logs |
| `code/theory2` | closed forms and finite element checks for general channels, multi-channel placement and Monte Carlo, identifiability of the in-service girder |
| `code/norbwim` | processing of the public NOR-BWIM field records |
| `code/analysis` | three-span theory, Mây Bridge model, dynamic records |
| `code/fieldplan` | predicted discriminating measurements at the Mây Bridge |
| `code/v3` | offset-bias and beam-model numbers (`v3_numbers.py`) |
| `code/v4` | figure scripts (Fig. 1, Fig. S8) and a numerical differentiation helper |

## How to run

```bash
pip install -r code/supplementary/requirements.txt
bash code/supplementary/run_all.sh                  # s01-s05, about 3 min, logs -> code/supplementary/logs/
bash code/supplementary/run_all.sh --with-analysis  # also re-runs the code/analysis scripts (writes inside code/analysis and figures/)
bash code/supplementary/run_all.sh --all            # also every remaining analysis (theory2, norbwim, v3, fieldplan, v4), about 20 min
```

`--all` runs each script from its own folder, and each writes its own log in its folder (`logs/` or `results/`). The `code/norbwim` scripts need the public NOR-BWIM records (https://doi.org/10.7294/26880898.v1) in `data/public/norbwim_figshare26880898`; the raw records are not redistributed. The `theory2` and `norbwim` scripts import sibling modules, so run them from their own folder without `-I` isolation if you call them one by one (`python3 <script>.py`). The `s01`–`s05` scripts can be run as `python3 -I code/supplementary/<script>.py`. Units are N and mm unless a script states otherwise (`s05` works in SI). All random numbers come from fixed seeds (`s04`: 20260817).

## Article: figures

| Article | Content | Script | Output / log |
|---|---|---|---|
| Fig. 1 | Two- and three-span beams, notation | `code/v4/fig1_beams.py` | `Fig1_beams` |
| Fig. 2 | Deflection observability of three-span beams | `code/analysis/schm_figures.py` (data: `code/analysis/cm_3span_theory.py`) | `code/analysis/data/obs_map_3span*.csv`, `code/analysis/logs/cm_3span_theory.log` |
| Fig. 3 | Indicators along prismatic girders | `code/theory2/gc_figures.py` | `code/theory2/figures/fig_gc_channels_prismatic.*` |
| Fig. 4 | NOR-BWIM strain records of three crossings | `code/norbwim/nb_fig1.py` | `code/norbwim/figures/fig1_example_crossings.*` |
| Fig. 5 | Truck ratio per gauge, 95 % CIs | `code/norbwim/nb_v4.py` | `code/norbwim/figures/v4_invariance.*`, `results/v4_invariance.csv`, `logs/v4.log` |
| Fig. 6 | Mây Bridge indicators, prismatic and haunched | `code/theory2/gc_figures.py` | `code/theory2/figures/fig_gc_caumay_channels.*`, `results/gc_T4_caumay.csv` |
| Fig. 7 | Identifiability of the pier stiffness | `code/theory2/ident_static.py` | `code/theory2/figures/ident_static_kappa_scan.*`, `logs/ident_static.log`, `logs/ident_static_scan.npz` |

## Article: tables

| Article | Content | Script | Log / results |
|---|---|---|---|
| Table 1 | Blind loci of response channels | `code/theory2/gc_theory.py`, `gc_fe.py`, `gc_force_method.py`, `verify_general.py`, `gc_results.py` | `code/theory2/logs/verify_general.log`, `gc_results.log`, `results/gc_T1_two_span.csv`, `gc_T2_three_span.csv`, `gc_T3_near_pier.csv`, `gc_T4_caumay.csv` |
| Table 2 | Out-of-sample MAE of the gross weight (single gauge, average, GLS, mean weight) | `code/norbwim/nb_v4.py` | `code/norbwim/logs/v4.log` (estimator comparison), `results/v4_estimators.csv`, `v4_estimator_errors.csv`, `v4_estimator_paired.csv` |
| Table 3 | Deflection indicator and cancellation ratio of the installed Mây Bridge gauges | `code/theory2/ident_static.py`, `ident_freq.py` | `code/theory2/logs/ident_static.log`, `ident_freq.log` |
| Table 4 | Predicted discriminating measurements at the Mây Bridge | `code/fieldplan/fieldplan_compute.py` | `code/fieldplan/results/fieldplan_compute.log`, `A_caumay_*.csv` |

Other numbers quoted in the article text come from the logs named in the sections below: crossing integrals, speeds and noise windows (Section 4.1) from `code/norbwim/nb_field.py` (`logs/field.log`, `results/events_field.csv`, `events_field_qc.csv`); gauge ratios and beam-model shares (Section 4.2) from `code/norbwim/nb_tests.py`, `nb_beam.py` (`logs/tests.log`, `results/test_*.csv`); Cramér–Rao bounds (Section 5.3) from `code/theory2/ident_fisher.py` (`logs/ident_fisher.log`); the Mây Bridge model (Section 5.1) from `code/analysis/wp3_run.py` (`logs/wp3_run.log`).

## Supplementary Material: figures

| Supplementary | Content | Script | Output / log |
|---|---|---|---|
| Fig. S1 | Strain indicator map, two-span beam | `code/theory2/gc_figures.py` | `code/theory2/figures/fig_gc_strain_map_2span.*` |
| Fig. S2 | Strain indicator map, symmetric three-span beam | `code/theory2/gc_figures.py` | `code/theory2/figures/fig_gc_strain_map_3span.*` |
| Fig. S3 | Structure-aware weighting functions | `code/theory2/multisensor_figures.py` (data: `multisensor_theory.py`) | `code/theory2/figures/ms_fig4_structure_aware.*`, `results/T4_structure_aware.csv`, `T4_weights.npz` |
| Fig. S4 | Multi-channel gain, offset level, immune pair | `code/theory2/multisensor_figures.py` (placement: `multisensor_placement.py`) | `code/theory2/figures/ms_fig2_placement_gain.*`, `results/T2_Ok.csv`, `T3_immune.csv`, `placement_*.csv` |
| Fig. S5 | Uniform-load response along six girders | `code/theory2/multisensor_figures.py` | `code/theory2/figures/ms_fig1_Cx_extremes.*`, `logs/multisensor_figures.log` |
| Fig. S6 | Monte Carlo verification of the multi-channel estimators | `code/theory2/multisensor_mc.py` | `code/theory2/figures/ms_fig3_montecarlo.*`, `logs/multisensor_mc.log`, `results/mc_summary.csv`, `mc_errors.npz` |
| Fig. S7 | Möbius law, closed form against FE | `code/theory2/ident_theory.py` | `code/theory2/figures/ident_theory_closedform.*`, `logs/ident_theory.log` |
| Fig. S8 | Laboratory influence line | `code/v4/figS1_lab_il.py` | reads `code/v4/lab_single_load_influence_line.csv` (Table S5); writes `code/v4/figures/FigS8_lab_influence_line.png` |
| Fig. S9 | Integral constant against speed | `code/norbwim/nb_v4.py` | `code/norbwim/figures/v4_speed.*`, `results/v4_speed.csv` |
| Fig. S10 | Estimator MAE, in sample, leave-one-run-out, leave-one-truck-out | `code/norbwim/nb_v4.py` | `code/norbwim/figures/v4_estimators.*`, `results/v4_estimators.csv` |
| Fig. S11 | Noise correlation between gauges | `code/norbwim/nb_v4.py` | `code/norbwim/figures/v4_noise_corr.*`, `results/v4_noise_corr_day1.csv`, `v4_noise_corr_day2.csv` |
| Fig. S12 | Five-span beam model, haunch laws | `code/norbwim/nb_tests.py`, `nb_beam.py` | `code/norbwim/figures/fig6_observability_model.*`, `logs/tests.log` |
| Fig. S13 | Synthetic strain records of the dataset authors | `code/norbwim/nb_fe_veb.py` | `code/norbwim/figures/fig7_fe_veb.*`, `logs/fe_veb.log`, `results/fe_veb_*.csv` |
| Fig. S14 | Mây Bridge frequencies against pier stiffness | `code/theory2/ident_freq.py` | `code/theory2/figures/ident_freq_vs_kappa.*`, `logs/ident_freq.log`, `logs/ident_freq_curves.npz` |
| Fig. S15 | Static misfit over rigidity factor and pier stiffness | `code/theory2/ident_freq.py` | `code/theory2/figures/ident_alpha_k_map.*`, `logs/ident_freq.log` |
| Fig. S16 | Baseline sensitivity, two simply supported bridges | `code/analysis/schm_figures.py` (event data: `wp4_dynamic_records.py`) | `code/analysis/logs/wp4.log` |
| Fig. S17 | Low-pass filtered deflection records | `code/analysis/schm_figures.py` (event data: `wp4_dynamic_records.py`) | `code/analysis/logs/wp4.log` |

## Supplementary Material: tables

| Supplementary | Content | Script | Log / results |
|---|---|---|---|
| Table S1 | Nomenclature | – | – |
| Table S2 | Symmetric three-span beam: optimal position and deflection indicator | `code/analysis/cm_3span_theory.py`, `verify_3span.py` | `code/analysis/logs/cm_3span_theory.log`, `verify_3span.log` (copies in `code/supplementary/logs/analysis/`) |
| Table S3 | Near-blind bands against the indicator threshold | `code/supplementary/s06_threshold_sensitivity.py` | `code/supplementary/logs/s06_threshold_sensitivity.log` |
| Table S4 | Laboratory: identified total loads | `code/supplementary/s03_load_identification.py` | `code/supplementary/logs/s03_load_identification.log` |
| Table S5 | Laboratory: measured and analytical deflections | `code/supplementary/beam_theory.py`, `s02_quadrature_table3.py` | `code/supplementary/logs/beam_theory.log`, `s02_quadrature_table3.log` |
| Table S6 | Integral constant and its scatter over the runs | `code/norbwim/nb_v4.py` | `code/norbwim/logs/v4.log`, `results/v4_invariance.csv` |
| Table S7 | Ratio of the integral constants of two trucks, TOST | `code/norbwim/nb_v4.py`, `nb_tests.py` | `code/norbwim/logs/v4.log`, `tests.log`, `results/test_f_gauge_ratios.csv` |
| Table S8 | Out-of-sample MAE of the gross weight, all estimators | `code/norbwim/nb_v4.py` | `code/norbwim/logs/v4.log`, `results/v4_estimators.csv`, `v4_estimator_errors.csv` |
| Table S9 | Correlation between gauges of the integrated strain | `code/norbwim/nb_v4.py` | `code/norbwim/logs/v4.log`, `results/v4_noise_corr_day1.csv`, `v4_noise_corr_day2.csv`, `v4_noise_summary.csv`, `v4_residual_vs_noise.csv` |
| Table S10 | Per-crossing standard deviation under two covariance models | `code/norbwim/nb_v4.py` | `code/norbwim/logs/v4.log`, `results/v4_estimator_paired.csv` |
| Table S11 | Weighed 3-axle test trucks | `code/analysis/wp9_truckweight_check.py` | `code/analysis/logs/wp9_truckweight_check.log` |
| Table S12 | Mây Bridge acceptance test | `code/analysis/wp3_run.py` | `code/analysis/logs/wp3_run.log`, `results/wp3_loadtest_table.csv`, `wp3_loadtest_summary.csv` |
| Table S13 | Admissible set of the Mây Bridge model against the tolerance | `code/theory2/ident_static.py` | `code/theory2/logs/ident_static.log`, `ident_static_scan.npz` |
| Table S14 | Vertical natural frequencies of the main-bridge spans | `code/theory2/ident_freq.py` | `code/theory2/logs/ident_freq.log` |
| Table S15 | Deflection indicator, cancellation ratio and boundary sensitivity of the Mây Bridge gauges | `code/theory2/ident_static.py`, `ident_freq.py`, `gc_results.py` | `code/theory2/logs/ident_static.log`, `ident_freq.log`, `gc_results.log` |
| Table S16 | Axle positions of the static test load (Mây Bridge) | `code/analysis/wp3_run.py` (`cm_schemes`) | positions as coded from the test plan |
| Table S17 | Bias of a single-channel estimate caused by a residual offset | `code/v3/v3_numbers.py` | `code/v3/logs/v3_numbers.log` |
| Table S18 | Indicative sensitivity budget | – (values taken from the sections of the article and the logs above) | – |

## Supplementary Material: sections

| Section | Content | Script / log |
|---|---|---|
| S2 | Closed forms for two- and three-span beams | `code/supplementary/s01_symbolic_two_span.py` (`logs/s01_symbolic_two_span.log`), `code/analysis/cm_3span_theory.py`, `verify_3span.py` |
| S3 | General channels, FE verification, weighting functions | `code/theory2/gc_*.py`, `verify_general.py`, `multisensor_theory.py` |
| S4 | Multi-channel estimation and placement | `code/theory2/multisensor_core.py`, `multisensor_placement.py`, `multisensor_mc.py` |
| S5 | Identifiability, sensitivities, Möbius law | `code/theory2/ident_core.py`, `ident_theory.py`, `ident_fisher.py` |
| S6 | Laboratory test | `code/supplementary/s01`–`s05` (see the table below) |
| S7 | Public field records | `code/norbwim/` |
| S8 | Mây Bridge | `code/analysis/wp3_*.py`, `code/theory2/ident_*.py`, `code/fieldplan/` |
| S9 | Dynamics and baseline handling | `code/analysis/wp4_dynamic_records.py` (`logs/wp4.log`), `code/supplementary/s05_moving_force.py` |
| S10 | Error budget and design checklist | `code/v3/v3_numbers.py`, `code/analysis/wp7b_peps.py` (`logs/wp7b_peps.log`) |
| S11 | Scripts, console output and derived data | this file |

## Laboratory and two-span scripts in `code/supplementary`

| Script | Reproduces | Log |
|---|---|---|
| `beam_theory.py` | Shared module: specimen constants, influence line, closed form, laboratory records (Table S5), quadrature rule, BPM/SLM identification, prismatic Hermite FE (stiffness, consistent mass, moving point load). Run alone, it prints I, EI, P0 and C_m. | `logs/beam_theory.log` |
| `s01_symbolic_two_span.py` | Section S2: influence line derived twice (force method; double integration plus Maxwell), continuity, 64EI, C_m = l⁴/192EI, closed form against two FE routes, ρ_L = (3+√33)/6 and ξ* = (1+√33)/16, near-blind band, R_m = 4/7, O_m = 2√44765/1279 and its monotonicity. | `logs/s01_symbolic_two_span.log` |
| `s02_quadrature_table3.py` | Quadrature comparison (2501.19, 2488.68, 2501.85, 2513.43), 20/21/23 intervals with Simpson and a 3/8 end panel, trapezoid O(Δx²) convergence, quadrature bias at 300 and 375 mm spacing. | `logs/s02_quadrature_table3.log` |
| `s03_load_identification.py` | Table S4 (BPM/SLM), the +1.61 % correction, measured/analytical ratios, the fitted line (slope 62.229, R² = 0.99998), three-load order, offset residual and its 58 %/42 % split. | `logs/s03_load_identification.log` |
| `s04_monte_carlo.py` | Monte Carlo of the single-gauge model with gain, zero offset and additive noise (200 000 realisations, seed 20260817). | `logs/s04_monte_carlo.log` |
| `s05_moving_force.py` | Dynamic study: FE with 40 Hermite elements per span, Rayleigh damping 2 % at modes 1 and 3, Newmark average acceleration, constant force crossing at speed v, E_dyn against C_mP over 47 speeds and a 300-speed dense sweep; f₁ = 11.942 Hz, time-step and mesh convergence, truncation and window-extension checks, multi-axle spread. Writes `logs/s05_sweep47.csv` and `logs/s05_sweep_dense.csv`. | `logs/s05_moving_force.log` |
| `run_all.sh`, `requirements.txt` | Driver and dependencies (tested versions listed). | |

## Scripts in `code/analysis` (three-span theory, Mây Bridge, dynamic records)

Run them from the repository root, or use `run_all.sh --with-analysis`. Their logs are in `code/analysis/logs/` and in `code/supplementary/logs/analysis/`.

| Script | Reproduces | Log |
|---|---|---|
| `cm_multispan.py` | Multi-span FE for C_m with variable EI(x) (exact non-prismatic flexibility element, influence-line and uniform-load routes) | `cm_multispan.log` |
| `cm_3span_theory.py` | Three-span closed forms (symbolic): critical ratios, band edge, asymmetric blind ratios; data for Fig. 2 (`data/obs_map_3span*.csv`) | `cm_3span_theory.log` |
| `verify_3span.py` | Closed forms against FE (60 comparisons), span-wise contributions, haunched FE convergence | `verify_3span.log` |
| `wp3_sections.py`, `wp3_fe.py`, `wp3_run.py` | Mây Bridge section properties, variable-EI FE, calibrations A and B, acceptance-test comparison (Table S12) | `wp3_run.log` |
| `wp9_truckweight_check.py` | Effect of the weighed test-truck mass (Table S11) | `wp9_truckweight_check.log` |
| `wp4_dynamic_records.py` | Event detection, baselines, high- and low-pass filtering of the simply supported records (Figs. S16–S17) | `wp4.log` |
| `wp7b_peps.py`, `wp7b_checks.py` | Offset-bias and k-sensitivity statements, near-blind band edges, root-sum-square budget | `wp7b_peps.log`, `wp7b_peps_2506.log` |
| `schm_figures.py` | Plots of Fig. 2 and Figs. S16–S17 | not re-run |

## Data in this archive

- `data/bridges/cau-may/`: Mây Bridge acceptance test (June 2020): static deflections at N7 and N8 (Table S12), weighed trucks (Table S11) and measured span frequencies (read by `code/theory2/ident_freq.py`).
- `code/v4/lab_single_load_influence_line.csv`: laboratory single-load influence line (Table S5).

## What is not here

- The laboratory raw records (each deflection is the mean of three cycles; only the means in Table S5 exist in the repository).
- The Abaqus model of the laboratory beam. The Hermite FE in `beam_theory.py` stands in for it; cubic elements are nodally exact, so both give the same nodal influence line.
- The raw NOR-BWIM records (available from the dataset DOI above; place them in `data/public/norbwim_figshare26880898/`) and the raw dynamic records of the Gie Cục I and Phương Độ bridges (Figs. S16 and S17).
