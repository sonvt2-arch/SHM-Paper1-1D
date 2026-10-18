# Changes from v3 to v4: editor concerns and actions

Sources: `docs/editors_v3/00_TONG_HOP_V3.md` and `editor1_EIC.md` … `editor4_field.md`. Field numbers come from `docs/pkg1/v4_norbwim_reanalysis.md` and `code/norbwim/logs/v4.log`. No new experiments were done (authors' decision). References are numbered as in v4.

## Summary of structural changes

- Title, abstract, contributions and conclusions reframed: the influence-area identity and GLS/zero-sum estimation are stated as classical; novelty is claimed only for the blind-locus catalogue, the indicators, the placement rule, the identifiability law and the evidence-based field assessment.
- §4 rewritten from the v4 re-analysis (all channels, 95 % CIs, equivalence tests, out-of-sample estimator comparison, measured noise covariance).
- §2.4 keeps the theory and adds the empirical caveat and the condition under which offset immunity helps.
- §3 shortened to a validation section; specimen figure and Appendix D moved to the supplement. §5.3 (frequency interpretation) moved to the supplement.
- Main text 7,430 words (prose, Sections 1–8; v3: 7,461 by the same rule, but v3 also had a 247-word abstract, 9 tables and Appendix D). Abstract to end of appendices including tables: about 10,200 words (v3 about 13,200 including references).
- References 57 → 54 (six removed, three added).

## Editor 1 (Editor-in-Chief)

| # | Concern | Action in v4 |
|---|---|---|
| 1 | Novelty overstated; "theorem" classical; GLS textbook; convex placement standard; compare with [31], [39], [44], [35, 36] | "Theorem" renamed "classical influence-area identity" with antecedents [23, 38] (§1 para. 4, §2.1). GLS and zero-sum weights called standard (§1, §2.4). Contributions list (§1) claims only (i)–(v). §1 para. 3–4 now positions the paper against [31] sparse-sensing placement, [39] influence-line-free weighing, [44] Kalman-filter placement, [35, 36] integrated influence lines, [34] Yan et al. and [15] Yu et al. A separate comparison table was not added, to save length. |
| 2 | Structural-scale evidence does not cover the claims | Title changed to a design-criteria paper with laboratory verification and a field **assessment**. Abstract and conclusions state what the field data cannot show (weight discrimination, blind loci, deflection pair). Offset-immune estimator now tested on field data (§4.3), with a negative result. §7 limitations list what remains untested. |
| 3 | Weak field statistics | 95 % CIs, TOST equivalence margins (±10 %, ±11.8 %, ±26.7 %), "consistent with, inconclusive" wording (§4.2, Table 3). "Speed-independent" removed. Day-1 SLM 6.5–7.0 % dropped from abstract and text; replaced by out-of-sample MAE with the constant-predictor baseline (Table 4). |
| 4 | Too long | §3 condensed; §5.3 and Cramér–Rao detail reduced; Appendix D and lab figure to supplement; Table 7 (v3) merged/condensed into Table 8; main + appendices ≈ 10,200 words. |
| 5 | Practical significance | §6 last paragraph and §7 state what was demonstrated (per-crossing errors 5–12 % on these records, not discriminating weights) and what a screening use would still need. A numeric screening specification was not added (no source). |
| 6 | Overlap, COI, data DOI | Still `[NEED VALUE]` (open items B4, B5, B8); cover letter asks to attach the *Structures* papers. |
| 7 | Figures 3, 4, 8, 9; Figs 1, 5 missing | Fig. 3 diacritics; Fig. 4 legends (mathtext ρ, no overlap); Fig. 8 title; Fig. 9 symbol $r_{87}$, panel labels, single tolerance band, PDF. Fig. 1 still author-supplied; old Fig. 5 to supplement (S15). |
| 8 | Validity envelope | New paragraph at the end of §2.1 linking each assumption to the section that tests it. Placement claim restricted to the stated noise model (§2.4). |

## Editor 2 (BWIM)

| # | Concern | Action |
|---|---|---|
| 1 | Theorem is the classical influence-area identity | As editor 1 #1; title no longer says "theorem". |
| 2 | GLS/zero-sum textbook; common-mode assumption untested; ρ = 1 headline numbers | Estimator called standard. ρ measured from vehicle-free windows (0.92 day 2, 0.42 day 1) and GLS/immune applied out of sample (§4.3, Table 4): worse than the average on day 2 (20.4 vs 11.9 %). Mechanism given (crossing-error correlation 0.63). ρ = 1 value (0.071 %) removed; ρ = 0.9 value kept as an upper bound with the caveat (§5.3). Placement restricted to the noise model; zero-sum within one channel type stated (§2.4). |
| 3 | Selective NOR-BWIM reporting; weights; speed; superposition; selection; baseline comparison | All 12 day-1 channels reported (Table 3 summary, full table in supplement; Fig. 6). Driver-reported weights stated; constant predictor (2.0–2.2 %) reported. Speed: confound on day 1, unresolved slope on day 2. Superposition: "consistent but low in both events". Selection: the wheel-path gauges are defined by axle spikes (§4.1); exclusions identical throughout. Comparison with [41–43] accuracy: `[NEED VALUE]` (open item A4). |
| 4 | Multiple presence, transverse position, speed measurement, screening | Multiple presence and wander stated as unquantified (§6, §7). [15] cited for NOR transverse-position estimation. Speed-measurement row added to Table 8 and §6. Screening statement tempered (§6 last paragraph). Poisson headway estimate not added (no traffic data). |
| 5 | Cầu Mây long and predictive | §5 shortened; frequency argument to supplement; strain-channel design given with the $cM_q/EI$ caveat (§5.3). |
| 6 | Weak laboratory | §3 shortened to a validation section; untested blind configuration stated. |
| 7 | Editorial completeness | Placeholders listed in open items B. |
| 8 | Minor: observability term; Eq. 14 channel types; structure-aware weights; ±12 m; abstract Cầu Mây detail; figures | "Identifiability" used in keywords and §2.5; Eq. (14) channel-type note added; structure-aware weights moved to App. B/supplement; ±12 m model inference removed; abstract keeps one Cầu Mây result plus the offset bias; Fig. 6/7 replaced. |
| refs | Yan 2022; Lobo Aguilar & Christenson 2018; Yu, Cai & Deng 2018 | All three verified (Crossref and journal page) and added as [34], [30], [15]. |

## Editor 3 (mechanics)

| # | Concern | Action |
|---|---|---|
| 1 | Day-1 weights driver-reported; no discriminating power | "Weighed" removed for day 1; constant predictor reported beside every estimator (Table 4); abstract leads with this limitation. |
| 2 | N8 upper bound 0.82 from normalisation | Both normalisations reported (§5.2, Table 5): 0.14–0.42 with $\alpha EI$, 0.12–0.82 with design $EI$; priors α ∈ [0.9, 1.3] give 0.14–0.27 / 0.12–0.30; absolute $C_8$ range (factor 6.6) given; abstract and conclusions use 0.14–0.42. Pier-geometry bracket not used (geometry is a placeholder in the log). |
| 3 | $N_w$ = 2.5 at SS mid-span; thresholds not equivalent | Corrected in §2.3, App. B, Table A.1 caption, Fig. 3 caption, conclusion 2. Thresholds defined explicitly as 8 % (deflection) and 20 % (strain) of the SS value. Renormalisation offered as open item A2. |
| 4a | 2.7× vs 3.2× | Replaced by one statistic: day-1 constants from −1.49 (ch8) to −5.85 (ch11) µε m/t, factor 3.9, non-overlapping 95 % CIs; lane argument with standard errors (3.24 ± 0.56 vs 1.82 ± 0.10, about 2.5 SE). |
| 4b | "Half the integral" is ≈ 170 % | "Span 2 contributes about 170 % of the net integral" (§4.4). |
| 5a | 24.8 % vs 23 % | Record lengths stated: 24.8 % for 220 m (placement study), 22.5 % for 200 m (Table 7). |
| 5b | 10⁻⁴ vs 5 × 10⁻⁶ | Δx = 0.1 m and $L_\mathrm{tot}$ = 220 m stated; ratio ≈ 5 × 10⁻⁶ (§2.4). |
| 5c | 152 vs 155 m | 152 m kept and named as the minimax design within 0.9 % of each calibration-specific optimum. |
| 5d | α⁻¹ in Eq. (15) | Eq. (15) now carries $1/\alpha$; $C_0$, $C_\infty$ at α = 1. |
| 6 | Cramér–Rao evaluation point; singular Fisher at B | Evaluation point (calibration A, κ, α*), noise levels and assumed rotation σ stated; singularity at B and the tiltmeter value there (0.04) given (§5.3). |
| 7 | Strain placement must use $cM_q/EI$ | §2.4, §5.3, §7 step 5, conclusion 3. |
| 8 | Novelty framing; ratio test power | As editor 1 #1; §4.2 says the axle-configuration test checks linearity and processing, not the identity. |
| 9 | Laboratory ratios with different denominators | Both ratios defined explicitly in §3. |
| 10 | Figures; Fig. 9 legend; placeholders; "real root" | Fig. 9 single band; "positive root" in §2.2; redundant phrase removed. |
| 11 | Frequency interpretation in abstract/conclusions | Joint set removed from abstract, conclusions and Table 5; one conditional sentence in §5.2; detail in supplement. |

## Editor 4 (field)

| # | Concern | Action |
|---|---|---|
| 1 | Offset-immune estimator not tested on held data | Done (§4.3, Table 4, Fig. 7, Fig. S1): noise correlation matrices, ρ, GLS and immune out of sample. Editor's in-sample 15.6 % was a noise-model prediction; observed error is 21.0 % RMS in sample, 23.6 % out of sample. Presented as a finding and a design caution (§2.4, §4.3, §7 step 6). |
| 2 | Selective day-1 channels | All 12 reported; selection rule (axle spikes) stated before results; confound discussed; possible causes listed without explaining them away. |
| 3 | Low power; lane-B invariance fails | TOST margins; single-gauge rows in Table 4; lane-B failure flagged (§4.2, Table 3). |
| 4 | Weights, gain, gauge geometry | Day-1 weights stated as driver-reported; geometry corrected to longitudinal stations about 2 m apart, "within 6 m along the girder" (no longer "one cross-section"); "which the 1D model does not reproduce" sense kept with the lane argument and its SE. Gauge calibration factors stated as unpublished (§4.5). |
| 5 | Cầu Mây datum, SE, τ dependence, abstract bias | Datum `[NEED VALUE]` (§5.1); 1.9–2.0 % described as systematic transverse spread; τ = 3 % and 4 % sets reported (design rigidity excluded at τ = 3 %); abstract bias uses the static set (16–25 %). |
| 6 | Residual offset not tied to a sensor | 0.23 mm re-described as drift before re-zeroing, not ε₀ (§6). Named-technique ε₀ values not added (no sources in the repository). |
| 7 | Speed constant over 605 m | Stated as not measured; speed-measurement row in Table 8. |
| 8 | Reproducibility: README, log side effect, data DOI | `code/supplementary/README.md` updated to the v4 scripts and logs; `nb_field.py` log fix done in the re-analysis package; DOI still open. |
| 9 | GPS wording; truck-to-truck SLM; SNR; GUM | "speeds computed by the dataset authors' processing script"; day-1 test described as truck to truck; GUM limitation stated once (§6); laboratory 0.07 % noise row removed from Table 8. |

## Rule checks

- AI-disclosure paragraph and the "Computational Implementation" paragraph copied verbatim from v3.
- No em dashes; `python3 code/analysis/wp7b_checks.py manuscript/v4` run (see traceability.md).
- No git commit made.
