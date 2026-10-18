# Figure and table plan (manuscript v3)

Main text: 9 figures (7 embedded, 2 author-supplied), 7 tables. Appendices: Tables A.1 and D.1. Supplementary: Figs. S1–S18. All chosen files are copied into `manuscript/v3/figures/` (main) and `manuscript/v3/figures/supplementary/` under their final names; the Word build (`word/prep_md.py`) embeds the main figures that exist and inserts a captioned placeholder for the others.

## Main figures

| No. | Content | File in `v3/figures/` | Source | Status / action |
|---|---|---|---|---|
| Fig. 1 | Notation: (a) two-span; (b) symmetric three-span | – | old JCSHM Fig. 1 (docx) for (a); (b) new | **Author to supply** (as in SCHM v2, open item 8) |
| Fig. 2 | Three-span deflection observability map, symmetric and asymmetric | `Fig2_obs_map_3span.{png,pdf}` | `manuscript/schm/figures/Fig3_obs_map_3span` (`code/analysis/schm_figures.py`) | Ready |
| Fig. 3 | $N_w$, $N_\theta$, $N_M$, $N_V$ along an equal two-span and a $\beta$ = 1.636 three-span beam | `Fig3_channels_prismatic.{png,pdf}` | `code/theory2/figures/fig_gc_channels_prismatic` (`gc_figures.py`) | Ready. Cosmetic: panel (b) title writes "Cau May" without diacritics; re-plot with "Cầu Mây" before submission |
| Fig. 4 | Multi-channel gain, offset level, immune pair | `Fig4_multichannel_gain.{png,pdf}` | `code/theory2/figures/ms_fig2_placement_gain` (`multisensor_figures.py`) | Ready. Cosmetic: legend uses "rho" in text; abbreviations 2S-eq, 3S-b2.0, CM-A/B explained in caption |
| Fig. 5 | Laboratory specimen and single-load influence line | – | old JCSHM Figs. 3 and 4 (docx) | **Author to supply**; can be merged into one two-panel figure |
| Fig. 6 | NOR-BWIM crossings with integration windows | `Fig6_norbwim_crossings.{png,pdf}` | `code/norbwim/figures/fig1_example_crossings` (`nb_fig1.py`) | Ready |
| Fig. 7 | Invariance at the gauge common to both days | `Fig7_norbwim_invariance.{png,pdf}` | `code/norbwim/figures/fig2_invariance` (`nb_tests.py`) | Ready |
| Fig. 8 | Cầu Mây deflection and strain indicators along the girder | `Fig8_caumay_channels.{png,pdf}` | `code/theory2/figures/fig_gc_caumay_channels` (`gc_figures.py`) | **Relabel needed**: panel (a) title reads "indicator of manuscript Eq. 13"; in v3 the deflection indicator is Eq. (10). Re-plot with title "(a) deflection channel, $N_w$" |
| Fig. 9 | Cầu Mây identifiability: ratio misfit and indicators against $\kappa$ | `Fig9_caumay_identifiability.png` | `code/theory2/figures/ident_static_kappa_scan.png` (`ident_static.py`) | PNG only; produce a PDF/vector version and add panel labels (a), (b) |

## Supplementary figures

| No. | File in `v3/figures/supplementary/` | Source |
|---|---|---|
| S1 | `FigS1_norbwim_slm.png` | `code/norbwim/figures/fig3_slm` |
| S2 | `FigS2_norbwim_speed.png` | `code/norbwim/figures/fig4_speed` |
| S3 | `FigS3_norbwim_lane_superposition.png` | `code/norbwim/figures/fig5_lane_superposition` |
| S4 | `FigS4_norbwim_beam_observability.png` | `code/norbwim/figures/fig6_observability_model` |
| S5 | `FigS5_veb_synthetic.png` | `code/norbwim/figures/fig7_fe_veb` (synthetic records of another bridge by the dataset authors) |
| S6 | `FigS6_strain_map_2span.png` | `code/theory2/figures/fig_gc_strain_map_2span` |
| S7 | `FigS7_strain_map_3span.png` | `code/theory2/figures/fig_gc_strain_map_3span` |
| S8 | `FigS8_Cx_extremes.png` | `code/theory2/figures/ms_fig1_Cx_extremes` (placement at extremes) |
| S9 | `FigS9_multichannel_montecarlo.png` | `code/theory2/figures/ms_fig3_montecarlo` |
| S10 | `FigS10_structure_aware_weights.png` | `code/theory2/figures/ms_fig4_structure_aware` |
| S11 | `FigS11_caumay_freq_vs_kappa.png` | `code/theory2/figures/ident_freq_vs_kappa` |
| S12 | `FigS12_caumay_alpha_k_map.png` | `code/theory2/figures/ident_alpha_k_map` |
| S13 | `FigS13_mobius_closedform.png` | `code/theory2/figures/ident_theory_closedform` |
| S14 | `FigS14_caumay_indicators.png` | `manuscript/schm/figures/FigS1_caumay_indicators` (SCHM v2 values; bound order of N7 printed as min…max) |
| S15 | `FigS15_giecuc_phuongdo_baseline.png` | `manuscript/schm/figures/Fig8_baseline_sensitivity` (old Section 5) |
| S16 | `FigS16_giecuc_phuongdo_lowpass.png` | `manuscript/schm/figures/Fig9_lowpass_residual` (old Section 5) |
| S17 | `FigS17_caumay_fieldplan_layout_VI.png` | `code/fieldplan/figures/fA1_caumay_layout_IL`: **labels in Vietnamese without diacritics; must be re-plotted in English** |
| S18 | `FigS18_caumay_predicted_records_VI.png` | `code/fieldplan/figures/fA2_caumay_predicted_records`: **same: re-plot in English** |

Not used: `fA3_caumay_bias_vs_offset` (Vietnamese labels; content given by Table 6), `fB1_generic_overpass` (field plan option B, not discussed in v3), SCHM Fig. 7 (influence lines of A/B; superseded by Fig. 8 and Table 4).

## Tables

| No. | Content | Source |
|---|---|---|
| Table 1 | Blind loci by channel | `docs/pkg1/1A_general_channels.md` §2.2; `code/theory2/logs/gc_results.log` T1, T2; `verify_general.log` group E |
| Table 2 | Laboratory identified loads | SCHM Table 4 (old JCSHM Table 5); `code/supplementary/logs/s03_load_identification.log` |
| Table 3 | NOR-BWIM tests | `code/norbwim/logs/tests.log`; `code/norbwim/results/test_*.csv` |
| Table 4 | Cầu Mây indicators (was SCHM Table 5; N7 bound order fixed to 0.263 … 0.145) | `code/theory2/logs/ident_static.log` l. 13–15, 40; `ident_freq.log` l. 50–53; `gc_results.log` T3/T4 (prismatic $R$); `code/analysis/logs/wp3_run.log` (bounds) |
| Table 5 | Predicted discriminating measurements | `code/fieldplan/results/fieldplan_compute.log` |
| Table 6 | Offset bias at Cầu Mây, ε0 = 0.02–0.5 mm | `code/v3/logs/v3_numbers.log` Part A |
| Table 7 | Indicative sensitivity budget (replaces SCHM Table 10; no root-sum-square, no GUM label) | values from Sections 3–6 (see traceability) |
| Table A.1 | Three-span $\xi^*$ and $N_w$ (was SCHM Table 2, rounded to 4 s.f.) | `code/analysis/logs/verify_3span.log` B; `docs/wp2_three_span_theory.md` §3 |
| Table D.1 | Laboratory data (was SCHM Table C.1, unchanged) | old JCSHM appendix |

Removed from the main text: SCHM Table 1 (closed form vs FE to 11 digits; replaced by one sentence with the 981-check maximum), Table 3 (quadrature; one sentence kept), Table 6 (static consistency; misfits now in §5.1 text), Table 7 (laboratory offset; supplement), Table 9 (dynamic envelope; bounds kept in §6.1), Table 10 (GUM-labelled budget; replaced by Table 7), Table A.1 (two-span list; supplement), Table B.1 (Monte Carlo; supplement).

Word build: no vertical rules; units in headings; equations numbered (1)–(16) right-aligned; line numbers on.
