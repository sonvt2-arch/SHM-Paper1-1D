# Figure and table plan (manuscript v4)

Main text: 9 figures (8 embedded, Fig. 1 author-supplied), 8 tables. Appendix: Table A.1. Supplementary: Figs. S1–S15 and the former Appendix D. Files are in `manuscript/v4/figures/` (main) and `manuscript/v4/figures/supplementary/`. The Word build (`word/prep_md.py`) embeds the main figures that exist and inserts a captioned placeholder for Fig. 1.

All re-plots in v4 changed labels, legends, panel titles or output format only. The scripts were rerun and their logs, CSV and NPZ outputs were checked unchanged with `git status` (`ident_static.log`, `ident_static_scan.npz`, `v4.log`, `v4_*.csv`, all `theory2/results`).

## Main figures

| No. | Content | File | Source script | v4 action |
|---|---|---|---|---|
| Fig. 1 | Notation: (a) two-span; (b) symmetric three-span | – | old JCSHM Fig. 1 (a); (b) new | **Author to supply** |
| Fig. 2 | Three-span deflection observability map | `Fig2_obs_map_3span.{png,pdf}` | `code/analysis/schm_figures.py` (via v3) | unchanged |
| Fig. 3 | $N_w$, $N_\theta$, $N_M$, $N_V$ along prismatic girders | `Fig3_channels_prismatic.{png,pdf}` | `code/theory2/gc_figures.py` | re-plotted: panel (b) title "Cầu Mây" with diacritics; caption now states $N_w$ = 2.5 at a simply supported mid-span |
| Fig. 4 | Multi-channel gain, offset level, immune pair | `Fig4_multichannel_gain.{png,pdf}` | `code/theory2/multisensor_figures.py` | re-plotted: legends use $\rho$ (mathtext) instead of "rho="; legends of (b) and (c) moved below the axes so they no longer overlap the curves; legend of (a) moved to the empty lower left; figure height 2.6 → 3.6 in |
| Fig. 5 | NOR-BWIM crossings (was Fig. 6) | `Fig5_norbwim_crossings.{png,pdf}` | `code/norbwim/nb_fig1.py` | unchanged |
| Fig. 6 | Per-gauge truck ratio with 95 % CI, all channels (replaces v3 Fig. 7) | `Fig6_norbwim_invariance.{png,pdf}` | `code/norbwim/nb_v4.py` | new in main text; panel labels (a), (b) added |
| Fig. 7 | Estimator MAE, IN/LOO/LOTO (new) | `Fig7_norbwim_estimators.{png,pdf}` | `code/norbwim/nb_v4.py` | new; panel titles changed to "(a) Day 2, 4 gauges" etc. |
| Fig. 8 | Cầu Mây deflection and strain indicators | `Fig8_caumay_channels.{png,pdf}` | `code/theory2/gc_figures.py` | re-plotted: panel (a) title "(a) deflection channel, $N_w$" (was "indicator of manuscript Eq. 13") |
| Fig. 9 | Cầu Mây identifiability | `Fig9_caumay_identifiability.{png,pdf}` | `code/theory2/ident_static.py` | re-plotted: misfit ratio renamed $r_{87}$ (was $\rho$, which clashed with the common-mode fraction and $\rho_L$); panel labels (a), (b); the duplicate "τ = 5 %" band removed, only the $\pm 2\tau$ band with τ = 5.3 % kept; "$R_m$" → "$R$"; PDF output added |

The v3 laboratory figure (old Fig. 5, author-supplied) moves to the supplement as Fig. S15.

## Supplementary figures

| No. | File in `figures/supplementary/` | Source |
|---|---|---|
| S1 | `FigS1_norbwim_noise_correlation.png` | `code/norbwim/figures/v4_noise_corr` (nb_v4.py) |
| S2 | `FigS2_norbwim_speed.png` | `code/norbwim/figures/v4_speed` (nb_v4.py) |
| S3 | `FigS3_norbwim_beam_observability.png` | `code/norbwim/figures/fig6_observability_model` |
| S4 | `FigS4_veb_synthetic.png` | `code/norbwim/figures/fig7_fe_veb` |
| S5 | `FigS5_strain_map_2span.png` | `code/theory2/figures/fig_gc_strain_map_2span` |
| S6 | `FigS6_strain_map_3span.png` | `code/theory2/figures/fig_gc_strain_map_3span` (annotation now "Cầu Mây") |
| S7 | `FigS7_Cx_extremes.png` | `code/theory2/figures/ms_fig1_Cx_extremes` |
| S8 | `FigS8_multichannel_montecarlo.png` | `code/theory2/figures/ms_fig3_montecarlo` (panel (b) title now "Cầu Mây") |
| S9 | `FigS9_structure_aware_weights.png` | `code/theory2/figures/ms_fig4_structure_aware` |
| S10 | `FigS10_caumay_freq_vs_kappa.png` | `code/theory2/figures/ident_freq_vs_kappa` |
| S11 | `FigS11_caumay_alpha_k_map.png` | `code/theory2/figures/ident_alpha_k_map` |
| S12 | `FigS12_mobius_closedform.png` | `code/theory2/figures/ident_theory_closedform` |
| S13 | `FigS13_giecuc_phuongdo_baseline.png` | `manuscript/schm/figures/Fig8_baseline_sensitivity` |
| S14 | `FigS14_giecuc_phuongdo_lowpass.png` | `manuscript/schm/figures/Fig9_lowpass_residual` |
| S15 | laboratory specimen and single-load influence line | **author to supply** (old JCSHM Figs. 3–4) |

Removed from the v4 supplement: v3 S1 (SLM, superseded by the out-of-sample estimator comparison), v3 S2 (speed, superseded by S2 from nb_v4.py), v3 S3 (lane and superposition from `nb_tests.py`, whose values differ from the v4 reanalysis), v3 S14 (SCHM v2 indicator values), v3 S17–S18 (field-plan figures with Vietnamese labels). The field-plan figures are not used in v4; if the authors want them back, `code/fieldplan/fieldplan_compute.py` lines 412–480 must be relabelled in English and rerun (open item C3).

## Tables

| No. | Content | Source |
|---|---|---|
| Table 1 | Blind loci by channel | as v3 (GCR T1, T2; VG group E) |
| Table 2 | Laboratory identified loads | as v3 |
| Table 3 | Field constants and invariance, representative rows; full 23-row table in the supplement | `code/norbwim/logs/v4.log` TASK 1; `results/v4_invariance.csv` |
| Table 4 | Out-of-sample estimator comparison | `v4.log` TASK 4; `results/v4_estimators.csv`, `v4_estimator_errors.csv` |
| Table 5 | Cầu Mây deflection indicators (A′ column removed; αEI column added) | `ident_static.log`; `ident_freq.log` |
| Table 6 | Predicted discriminating measurements (frequency-ratio row moved to the supplement) | `code/fieldplan/results/fieldplan_compute.log` |
| Table 7 | Offset bias at Cầu Mây over the static admissible set | `code/v3/logs/v3_numbers.log` Part A |
| Table 8 | Indicative sensitivity budget (speed measurement row added) | values from Sections 3–6 |
| Table A.1 | Three-span $\xi^*$ and $N_w$ | as v3 |

Moved to the supplement: Appendix D (Table D.1, laboratory data); the joint (static + frequency) admissible set and its column in Table 4 of v3.

Word build: no vertical rules; units in headings; equations numbered (1)–(16) right-aligned; line numbers on.
