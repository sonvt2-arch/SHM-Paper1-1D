# Figure and table plan

Main text: 10 figures, 9 tables. Appendices: 4 tables. Old figure numbers refer to the JCSHM manuscript (`CSHM-D-26-00881`, Word file `JCSHM_Submission.docx`).

## Figures

| New no. | Caption (short) | Source file / script | Status |
|---|---|---|---|
| Fig. 1 | (a) two-span beam notation; (b) symmetric three-span beam notation | old Fig. 1 (docx) for (a); panel (b) new | **Needs redraw**: add panel (b) with $L_s$, $L_m = \beta L_s$, sensor at $\xi L_s$ |
| Fig. 2 | Two-span observability map: (a) over $\rho_L$, $\rho_{EI}$ with blind locus and near-blind band; (b) versus sensor position | old Fig. 10 (docx) | Old figure from docx; renumber only |
| Fig. 3 | Three-span observability map: (a) symmetric, over $\beta$ and $\xi$; (b) asymmetric | `figures/fig_obs_map_3span.png` (`code/analysis/cm_3span_theory.py`) | **Needs redraw**: remove the "Thai Binh 42+63+42" marker (Thái Bình is not analysed); keep Cầu Mây marker; spell "Cầu Mây" |
| Fig. 4 | Laboratory specimen: elevation/instrumentation; view of rig | old Fig. 3 (docx) | Old figure from docx; change "Department" if it appears in a label |
| Fig. 5 | Influence line under single 40.64 N load: analytical, FE, measured; residual panel | old Fig. 4 (docx) | Old figure from docx |
| Fig. 6 | Calibration line: integral vs total load | old Fig. 6 (docx) | Old figure from docx |
| Fig. 7 | Cầu Mây: (a) $EI(x)/EI_\mathrm{mid}$; (b) influence lines at N8 (0.4L) and N7 for pinned, $k_\mathrm{FE}$, fixed | left panel of `figures/wp3_EI_profiles.png` + panels 1–2 of `figures/wp3_influence_lines.png` (`code/analysis/wp3_run.py`) | **Needs redraw**: drop Thái Bình panels (right panel of EI profile; panels 3–5 of influence lines); combine into one two-row figure |
| Fig. 8 | Baseline sensitivity of event integrals, field records | `figures/wp4_integral_sensitivity.png` (`code/analysis/wp4_dynamic_records.py`) | Exists; suggest relabelling legend codes (a_raw → "tare", c1_poly3 → "cubic", c2/c3 → "high-pass 0.1/0.5 Hz", pre_only → "pre level") and axis tick labels (Gie Cuc / Phuong Do) |
| Fig. 9 | Low-pass 2 Hz and dynamic residual, field records | `figures/wp4_lowpass.png` | Exists; add axis labels (time s, deflection mm); consider showing 2–3 records only to save space |
| Fig. 10 | Dynamic error of quasi-static estimator vs $T_\mathrm{cr}/T_1$ | old Fig. 11 (docx) | Old figure from docx |

Not used (available): `figures/wp3_Cm_normalised_bar.png` (content given in Table 5; includes Thái Bình), `figures/wp4_baseline_methods.png`, `figures/wp4_consistency.png`, `figures/wp4_records_events.png`, `figures/wp4_pd_n1_lobe.png`; old Figs. 2 (workflow), 5 (analytical invariance illustration), 7 (zero-offset bias), 8 (Monte Carlo histogram), 9 (parametric study). Old Fig. 9 content is covered by Fig. 2 and Table A.1; if an editor asks for a graphical abstract, old Fig. 2 or a simplified Fig. 7b are candidates.

## Tables

| New no. | Content | Source | Status |
|---|---|---|---|
| Table 1 | Two-span closed form vs FE | old Table 1 | Reused unchanged (column $\rho_{EI}$ removed, all = 1) |
| Table 2 | Three-span $\xi^*$, indicator at $\xi^*$ and at 1/2 | `docs/wp2_three_span_theory.md` §3; `code/analysis/logs/verify_3span.log` sec. B | New |
| Table 3 | Single-load integral, quadrature | old Table 3 (FE trapezoidal row removed as identical to analytical) | Reused, condensed |
| Table 4 | Identified loads vs weighing | old Table 5 (gram column dropped) | Reused, condensed |
| Table 5 | Cầu Mây observability indicators | `code/analysis/results/wp3_Cm_summary.csv`; `wp3_run.log` | New (Cầu Mây rows only) |
| Table 6 | Cầu Mây static consistency | `code/analysis/results/wp3_loadtest_summary.csv`; `wp3_run.log` | New (Cầu Mây rows only) |
| Table 7 | Zero-offset bias | old Table 6 | Reused unchanged |
| Table 8 | Dynamic error envelope | old Table 9 | Reused unchanged |
| Table 9 | Uncertainty budget | old Table 11 | Reused; Type A rows relabelled "A (bound)" |
| Table A.1 | Two-span constant vs span ratio | old Table 8 (1.457 written as 1.45743, value 0) | Moved to appendix |
| Table B.1 | Monte Carlo | old Table 7 | Moved to appendix |
| Table C.1 | Laboratory deflections | old Tables 2 and 4 merged (FE column dropped, identical to analytical) | Moved to appendix |

Dropped: old Table 10 (indicative crossing-time ratios; summarised in one sentence in Section 6.5), old Table 12 (signed decomposition; key values in Section 2.2 text), old Table 13 (positioning vs BWIM; summarised in Section 7.1 prose).
