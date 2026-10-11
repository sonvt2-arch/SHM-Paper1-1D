# Figure and table plan (SCHM version)

Main text: 10 figures, 10 tables. Appendices: 4 tables. Supplementary: Figure S1. Figure and table numbers are unchanged from v2. Old figure numbers refer to the JCSHM manuscript (`CSHM-D-26-00881`, Word file `JCSHM_Submission.docx`), which is not in the repository.

SCHM rules (see `schm_requirements.md`): figures embedded in the Word file at submission, one source file per figure after acceptance, bitmaps ≥ 300 dpi, vector formats accepted; tables without vertical rules, units in column headings.

Figures produced in this version: `python3 code/analysis/schm_figures.py` (plotting only; it calls the existing analysis functions and reads the CSV files they write). Output in `manuscript/schm/figures/`: PNG at 600 dpi and vector PDF, 7.0 in (178 mm) wide. Every value printed on a figure is listed in `figures/schm_figures_values.txt`.

## Figures

| No. | Content | File / source | Status |
|---|---|---|---|
| Fig. 1 | (a) two-span notation; (b) symmetric three-span notation | old Fig. 1 (docx) for (a); (b) new | **Author to supply**: schematic; panel (b) with $L_s$, $L_m = \beta L_s$, sensor at $\xi L_s$ must be drawn |
| Fig. 2 | Two-span observability map: (a) over $\rho_L$, $\rho_{EI}$; (b) against sensor position | old Fig. 10 (docx) | **Author to supply** (old docx figure; not in the repository; no repository script draws it) |
| Fig. 3 | Three-span observability map: (a) symmetric, $\beta$–$\xi$; (b) asymmetric | `figures/Fig3_obs_map_3span.{png,pdf}`; data `code/analysis/data/obs_map_3span*.csv` (from `cm_3span_theory.py`), $\xi^*$ from `cm_3span_theory.xi_opt` | **Done.** Thái Bình marker removed; "Cầu Mây" spelled with diacritics; open-circle marker at $\beta = 90/55$, $\xi = 0.5$ |
| Fig. 4 | Laboratory specimen: elevation and instrumentation; photograph | old Fig. 3 (docx) | **Author to supply** (drawing and photograph; check that no label says "Department") |
| Fig. 5 | Influence line under the single 40.64 N load: analytical, FE, measured; residual panel | old Fig. 4 (docx) | **Author to supply** (could be redrawn from Appendix C and Eq. (A.2), but no repository script plots it and the FE curve is not in the repository) |
| Fig. 6 | Measured integral against total load, theoretical slope | old Fig. 6 (docx) | **Author to supply** |
| Fig. 7 | Cầu Mây: (a) $EI(x)/EI_\mathrm{mid}$; (b) influence line at N8 (0.4L); (c) influence line at N7; calibrations A and B, pinned and fixed piers | `figures/Fig7_caumay_EI_influence_lines.{png,pdf}`; `wp3_run.bridge_models()` + `wp3_run.calibrate()` (Cầu Mây variants), `wp3_fe.Bridge.Cm` | **Done.** Calibration B lines added; areas shaded for A and B; Thái Bình panels removed; $N_m$, $R_m$ boxes equal Table 5. Text now cites "Figs. 7b and 7c" |
| Fig. 8 | Baseline sensitivity of the event integral, seven complete crossings | `figures/Fig8_baseline_sensitivity.{png,pdf}`; `data/bridges/{gie-cuc-1,phuong-do}/wp4_events_baseline.csv` (from `wp4_dynamic_records.py`) | **Done.** Legend in words (tare only, cubic, high-pass 0.1/0.5 Hz); bridge names on the axis |
| Fig. 9 | 2 Hz low-pass and dynamic residual | `figures/Fig9_lowpass_residual.{png,pdf}`; `wp4_dynamic_records.detect_events/analyse_record` and `wp4_lowpass.csv` | **Done.** Axis labels added; one record per span (first complete crossing, processed channel). `schm_figures.py` restores `logs/wp4.log`, which importing the WP4 module would otherwise truncate |
| Fig. 10 | Dynamic error of the quasi-static estimator against $T_\mathrm{cr}/T_1$ | old Fig. 11 (docx) | **Author to supply** (the moving-load script of Section 6.5 is not in the repository) |
| Fig. S1 (supplementary) | $N_m$ and $R_m$ of the three Cầu Mây gauge positions for calibrations A and B, with pinned … fixed bounds | `figures/FigS1_caumay_indicators.{png,pdf}`; same models; bounds from `results/wp3_Cm_summary.csv` (`norm_min`, `norm_max`) | **Done.** Same numbers as Table 5, so it is placed in the supplementary material rather than the main text |

Considered and not produced: a $P_\varepsilon$ figure. Table 8 already gives all eight values, and a plot of $P_\varepsilon$ against $\varepsilon_0$ would add only a straight line per gauge. Old figures not used: Figs. 2 (workflow), 5 (invariance illustration), 7 (zero-offset bias), 8 (Monte Carlo histogram), 9 (parametric study). If the editor asks for a graphical abstract, Fig. 7b or old Fig. 2 are candidates.

## Tables

| No. | Content | Source | Status |
|---|---|---|---|
| Table 1 | Two-span closed form against FE | old Table 1 | Unchanged |
| Table 2 | Three-span $\xi^*$ and indicator | `docs/wp2_three_span_theory.md` §3; `code/analysis/logs/verify_3span.log` B | Unchanged |
| Table 3 | Single-load integral, quadrature | old Table 3 | Unchanged |
| Table 4 | Identified loads against weighing | old Table 5 | Unchanged |
| Table 5 | Cầu Mây indicators, calibrations A and B, $R_m$, bounds | `code/analysis/results/wp3_Cm_table.csv`, `wp3_Cm_summary.csv`; `wp3_run.log` | Unchanged; values re-confirmed by `schm_figures_values.txt` |
| Table 6 | Cầu Mây static consistency, models A and B | `wp3_loadtest_summary.csv`; `wp3_run.log` | Unchanged |
| Table 7 | Zero-offset bias, laboratory | old Table 6 | Unchanged |
| Table 8 | $P_\varepsilon$ and bias at the Cầu Mây gauges | `code/analysis/logs/wp7b_peps.log` Part A | Unchanged |
| Table 9 | Dynamic error envelope | old Table 9 | Unchanged |
| Table 10 | Uncertainty budget | `wp7b_peps.log` Part D | Unchanged |
| Tables A.1, B.1, C.1 | Appendices | as in v2 | Unchanged |

When building the Word file: no vertical rules (SCHM), units in column headings (Tables 3, 4, 6–8 already comply), embed Figs. 1–10 near their first citation.
