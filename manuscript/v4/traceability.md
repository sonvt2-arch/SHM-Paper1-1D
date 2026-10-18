# Traceability of numeric values in `manuscript/v4/manuscript.md`

Every number in the v4 manuscript is listed with its source. Numbers carried unchanged from v3 point to `manuscript/v3/traceability.md` (**V3-T**), which in turn names the original log. New or changed numbers are listed in full. No number was produced from memory; values that the repository does not hold are `[NEED VALUE]` in the manuscript.

## Source abbreviations

| Code | File |
|---|---|
| NV4 | `code/norbwim/logs/v4.log` and `code/norbwim/results/v4_*.csv` (script `nb_v4.py`, deterministic; described in `docs/pkg1/v4_norbwim_reanalysis.md`) |
| NBT | `code/norbwim/logs/tests.log`; `code/norbwim/results/test_*.csv` |
| 3B | `docs/pkg1/3_norbwim_analysis.md` |
| IS, IF, IFI, IT | `code/theory2/logs/ident_static.log`, `ident_freq.log`, `ident_fisher.log`, `ident_theory.log` |
| MST, MSP, MSMC | `code/theory2/logs/multisensor_theory.log`, `multisensor_placement.log`, `multisensor_mc.log`; `docs/pkg1/1B_multisensor.md` |
| GCR, VG | `code/theory2/logs/gc_results.log`, `verify_general.log`; `docs/pkg1/1A_general_channels.md` |
| V3N | `code/v3/logs/v3_numbers.log` |
| FP | `code/fieldplan/results/fieldplan_compute.log`, `results/A_caumay_*.csv` |
| CR | Crossref / journal landing page, checked 2026-10-18 |
| DER | arithmetic on sourced values, shown |

## Abstract

| Value | Source |
|---|---|
| within 1.2 % | V3-T Table 2 (BPM +1.10 %, +1.19 %) |
| 2.0–2.2 % | NV4 TASK 4: mean-GVW LOO MAE 2.0 (day 2), 2.2 (day 1) |
| 0.98 (95 % CI 0.70–1.37) | NV4 TASK 1, d2A avg ratio 0.978 [0.697, 1.374] |
| 20.4 % against 11.9 % | NV4 day2 4ch LOO: GLS 20.4, average 11.9 |
| 0.63; 0.92 | NV4 TASK 4 diagnostic: crossing residuals mean r 0.630; TASK 3 day 2 non-overlapping mean r 0.921 |
| 55 + 90 + 55 m | V3-T |
| 0.14 and 0.42 | IS, τ = 5.27 % Lv44: N8a [0.144, 0.422] |
| 0.1 mm; 25 t; 16–25 % | V3N Part A: N7 static set max C 16.4 %; joint/static min C 24.8 % (25.06 t) |

## Section 1

As V3-T §1. New: [15] Yu, Cai and Deng (CR 10.1080/15732479.2017.1401095: SIE 14 (8) 1108–1122, issue 2018); [30] Lobo Aguilar and Christenson (CR 10.15517/mym.v8i1.34551; journal landing page: Vol. 8 (2018), citation_date 2018; pp. 11–22); [34] Yan et al. (CR 10.1016/j.ymssp.2022.109133: MSSP 177 (2022) 109133; title only, full text not read). [31] Agüero-Barrantes et al. year 2021 confirmed on the journal landing page (Vol. 11 (2021)).

## Section 2

| Value | Location | Source |
|---|---|---|
| 59 % | §2.1 | V3-T (VG group F) |
| Eqs. (4)–(9), 1.4574, 0.4215, 1.7006, 1.8794, bands 1.385–1.525 and 1.621–1.775, 981 checks, 8.1 × 10⁻¹¹ | §2.2 | V3-T §2 |
| 0.75L, 0.276, 0.177, $\mu<4$, 0.676–0.812, 0.19–0.32 | §2.2 | V3-T §2 |
| Table 1 | §2.2 | V3-T §2 |
| $N_w$ = 2.5 at a simply supported mid-span; 1 at mid-span of two equal spans | §2.3, App. A/B, Fig. 3 caption | DER from Eq. (5): $8F(0.5, 0) = 8 \times 0.3125 = 2.5$; $8F(0.5, 1) = 8 \times 0.125 = 1$; editor 3 report, concern 3 |
| 8 % and 20 % | §2.3 | DER 0.2/2.5 = 0.08; 0.2/1 = 0.20 |
| 4/7; 0.667, 0.571 | §2.3 | V3-T §2 |
| 1.65–2.0 | §2.4 | MST (1.647 … 2.000) |
| about 5 × 10⁻⁶ | §2.4 | DER $\sigma^2\Delta x/(\varepsilon_0^2L) = (0.01^2 \times 0.1)/(0.1^2 \times 220) = 4.5\times10^{-6}$ with $\Delta x$ = 0.1 m and $L_\mathrm{rec}$ = 220 m from 1B §1 (baseline settings). Replaces v3 "about 10⁻⁴" (editor 3, concern 5b). Consistent with MST l. 31–33 for a 60 m record: (0.064/18.236)² = 1.2 × 10⁻⁵ |
| 96 cases; 10⁵; 0.6 % | §2.4 | V3-T §2 |
| Eq. (15) with $\alpha^{-1}$ | §2.5 | IT (homogeneity of degree −1, $S_\alpha + S_k = -1$); editor 3 concern 5d |
| 4.4 × 10⁻⁷; 0.287 → 1.037; 0.755 → 0.500 | §2.5 | V3-T §2 |

## Section 3

As V3-T §3 (25 mm, 2.03 mm, 16 530 mm⁴, 200 GPa, 2500 mm, 61.54 mm²/N, 0.005 mm, 250 mm, 40.64 N, 0.030/0.55 mm, 0.0126 mm, 0.44 %, 0.500 %, Table 2, 1.0049, 1.010/1.016/1.017, 3644 mm).

## Section 4

| Value | Source |
|---|---|
| 605 m, spans, 3.8/9.5 m, 158.5 m | V3-T §4 |
| stations about 2 m apart; day-1 station pairs and the four no-spike gauges; within 6 m | 3B l. 24–25 (st40–st31 distance 6.02 ± 0.09 m; four stations 2 m apart) |
| 12 channels 100 Hz; four channels 200 Hz | V3-T §4 |
| 21.2–22.8 t (runs used) | V3-T §4 (22.82 … 21.17 t, rounded) |
| 26.8 t, 25.9 t | V3-T §4 |
| MAE 2.0 % (day 2), 2.2 % (day 1) | NV4 LOO mean-GVW rows |
| 1–2 %, 5 s, exclusions | V3-T §4 |
| 70 s | NV4 TASK 3 header |
| eight gauges CV 5.8–13.5 %, χ² p 0.13–0.71 | NV4 d1A rows ch3–ch7, ch10–ch12 |
| ch11 0.996, 90 % CI 0.904–1.098 | NV4 d1A ch11 |
| 0.955 (0.863–1.057); ±11.8 % | NV4 d1A avg; "smallest symmetric margin … ±11.8 %" |
| 22–26 % lower | NV4 ratios 0.740–0.783 (DER 1 − ratio) |
| 2.9–5.1 | NV4 residual var / quiet var: ch8 2.93 … ch9 5.05 |
| Table 3 (all entries) | NV4 TASK 1 tables d1A, d2A, d2B |
| 0.98 (0.70–1.37); ±26.7 %; about 27 % | NV4 d2A avg; margin ±26.7 % |
| lane-B χ² p 0.016–0.027; CV 31–40 % | NV4 d2B st36, st31, avg; CV 30.8–39.7 % |
| speeds 10.4–12.8, 19.1–19.8 m/s; r 0.98 | NV4 TASK 2 d1A |
| 13–28 m/s; +6 % (−23 to +35 %) | NV4 TASK 2 d2A avg truck+v +6.3 [−22.7, +35.4]; speed ranges 13.2–28.1 m/s |
| 1227, 3405 windows | NV4 TASK 3 |
| 0.92 (0.83–0.96); 13.7–32.8 µε m; 0.42 (0.26–0.54) | NV4 TASK 3 |
| Table 5 (all entries) | NV4 TASK 4 LOO and LOTO blocks; predicted sd column "pred.sd"; day-1 wheel-path worst single = ch4 12.1 |
| +8.5 points (+2.3 to +15.1) | `docs/pkg1/v4_norbwim_reanalysis.md` §4 paired bootstrap; `results/v4_estimator_paired.csv` |
| 12.7 % vs 19.8 % | NV4 day2 LOO pred.sd GLS 12.7, average 19.8 |
| average 5.3, GLS 5.8, best single 4.8 | NV4 day1 12ch LOO |
| 0.63; 0.30–0.37; 0.90 | NV4 TASK 4 diagnostic day2 (residual r 0.630; st40–st36 0.30, st40–st34 0.37; quiet 0.895) |
| 21.0 % and 14.6 % | NV4 TASK 4 diagnostic day2 |
| +0.16 on st40, −0.35 on st36 | `docs/pkg1/v4_norbwim_reanalysis.md` §4 |
| 10.4 % vs 28.4 % | NV4 day2 GLS-resid IN RMS 10.4, LOO RMS 28.4 |
| 0.79 (0.59–1.00); st36 0.64 (0.47–0.81) | NV4 `v4_lane.csv` (avg 0.794 [0.590, 1.000]; st36 0.640 [0.469, 0.807]) |
| 0.92, 0.92; pooled 0.92 (0.77–1.06); GLS 0.82 (0.73–0.91) | NV4 `v4_superposition.csv`; reanalysis §5 (0.921, 0.915; 0.918 [0.772, 1.064]; GLS pooled 0.818 [0.729, 0.907]) |
| −1.49 (ch8), −5.85 (ch11); 3.9; CIs do not overlap | NV4 d1A C values and 95 % CIs; DER 5.85/1.49 = 3.93. Replaces v3 "up to 2.7 times" (relative to ch4) and "about 3.2" (editor 3 concern 4a) |
| 0.978–1.003 | V3-T §4 (test_f_model.csv) |
| 3.24 ± 0.56; 1.82 ± 0.10; about 2.5 standard errors | NBT `test_f_gauge_ratios.csv` (3.2387, se 0.5593; 1.8191, se 0.0963); DER (3.24 − 1.82)/√(0.56² + 0.10²) = 2.5 |
| $r^2$ 0.79–0.94; 121.6, 190.8 m; 35 m; 0.69; 0.56–0.93; 0.51 | V3-T §4 (V3N Parts B, C) |
| about 170 %; −26 %, −66 % | V3N Part B span shares [−26.0, 171.5, −65.5, 23.4, −3.5] %. Replaces v3 "about half" (editor 3 concern 4b) |
| 10–27 % | NV4 TOST margins (±10 % for ch11 … ±26.7 % for d2A avg) |

## Section 5

| Value | Source |
|---|---|
| bridge data, 25.06 t, 5.55/15.42 mm, model and variants | V3-T §5 |
| A: +2.4/+12.3 %; B: α 0.716, k 1.2 × 10⁸, −2.8/+2.9 % | IS l. 13, 15 |
| 1.126, 1.058, 1.68 × 10⁸, 1.091; 1.039–1.092; 4–9 %; 28 % | V3-T §5 |
| 1.9–2.0 % spread of six readings (3 lines × 2 transverse cases) | IS l. 2 (rel. SEM 1.90 %, 2.04 %); now described as systematic transverse spread (editor 4 concern 5) |
| 1.75 %; τ = 5.3 % | IS l. 46–47 (model-form 1.75 %; τ = 5.27 %) |
| κ ≥ 1.8 × 10⁷; α 0.51–1.15 | IS τ = 5.27 % Lv44 (κ [1.78e7, 1e12]; α [0.513, 1.153]) |
| τ = 3 %: κ 1.0–3.0 × 10⁸, α 0.64–0.80 | IS τ = 3.00 % Lv44 |
| τ = 4 %: κ 4.2 × 10⁷–2.0 × 10⁹, α 0.54–0.98 | IS τ = 4.00 % Lv44 |
| 0.14–0.42 (αEI); 0.12–0.82 (design); α ≈ 0.5 | IS τ = 5.27 % Lv44 (N8a [0.144, 0.422]; N8d [0.124, 0.822]); IS κ = 10¹² row α* 0.517 |
| prior α ∈ [0.9, 1.3]: 0.14–0.27 / 0.12–0.30 | IF "τ = 5.27 % static + prior alpha" (alpha-ref [0.144, 0.267]; design-ref [0.124, 0.297]) |
| C8 3.0 × 10⁻⁵–2.0 × 10⁻⁴; factor 6.6; C7 3.3–5.0 × 10⁻⁴ | IF τ = 5.27 % static only (C8 [3.00e-05, 1.98e-04]; C7 [3.28e-04, 4.95e-04]); DER 1.98/0.300 = 6.6 |
| k_g 4.36 × 10⁷; 14.0; 0.59; 0.63; B_m 0.51, 0.12; 6.5 vs 1.5 | V3-T §5 |
| Table 7 | V3-T §5 (A′ column removed); αEI column from IS N8a |
| 0.341 | IS l. 6 (κ = 1.679e8: N8 index αEI 0.341) |
| 3.43–3.64 Hz | IF (N6 3.43 … N7 3.64) |
| 26.0–33.3 m; 0.048; 0.163–0.212; 0.65–1; 5–10 m; ≥ 0.39; one fifth; 0.47–0.61 | V3-T §5 (1A §3) |
| 4–10 m; (100, 152) m; 0.9 % | V3-T §5 (MSP) |
| 220 m (200 m + 20 m) | 1B §1 baseline settings ($L_\mathrm{rec} = L + 20$ m) |
| 24.8 %; 10.6 % at ρ = 0.9 | MST T3 Cầu Mây A (24.80; 10.57) |
| 22.5 % (200 m) | V3N Part A (N7 calib A, 0.1 mm: 22.5 %) |
| 167 µrad | IFI κ = 2.748e7 row (rotT7 = 167.3 µrad) |
| CRB at A: κ 2.75 × 10⁷, α* 1.07; σ 2.64 %, rotation 3 % assumed; 0.87 → 0.18; 0.24 | IFI header (static 2.64 %, rotation 3.0 % [NEED VALUE] in log, i.e. assumed) and κ = 2.748e7 block (sd ln C8 0.865; +rot T7 0.177; +f1+f3 0.237) |
| singular at B; 0.04 with tiltmeter | IFI κ = 1.679e8 block (FIM singular; +rot T7 0.040) |
| Table 8 | V3-T §5 (FP); frequency-ratio row moved to the supplement |
| factor 2.3 | DER 0.284/0.121 |

## Section 6

| Value | Source |
|---|---|
| ≤ 1 % at ≥ 8; > 15 % below 2.5 | V3-T §6 (S05) |
| 200 m; 25.06 t | V3-T §6 |
| 0.23 mm | V3-T §6 (WP4); now described as drift before re-zeroing (editor 4 concern 6) |
| Table 9 (all entries) | V3N Part A rows "N7 static set max C", "N7 joint set min C" (= static min), "N8 static set max C", "N8 joint set min C" (= static min, IF C8 3.00e-05) |
| 16–25 %; 41–271 % | V3N Part A |
| 0.79; 2.05 mm, 13 %; 0.92 | NV4 lane; V3-T §6; NV4 superposition |
| 12.4 s | V3-T §6 |
| Table 10 | rows above; "6.6-fold" DER as in §5 |
| 5–12 % | NV4 LOO MAE of average/GLS (day 1 ≈ 5 %, day 2 11.9 %) |
| 0.6–0.7 % | Table 2 |

## Sections 7–8 and appendices

As above and V3-T. Appendix D (laboratory data) moved unchanged to the Supplementary Material (source: V3-T, SCHM Table C.1).

## Word counts

`python3 code/analysis/wp7b_checks.py manuscript/v4`: abstract 251 words; main text (Sections 1–8, prose only) about 7,430 words; 16 numbered equations, all cited. Abstract to end of Appendix C including tables and nomenclature: about 10,200 words (same counting rule, inline math = 1 word).

## Readability revision (v4.1): numbers moved between prose and tables

The readability pass (see `readability_changes.md`) changed no value. Tables were renumbered: new Table 4 (noise and crossing residuals) and new Table 6 (admissible set against τ) were inserted, so v4 Tables 4, 5, 6, 7, 8 are now Tables 5, 7, 8, 9, 10. Sources of every value are unchanged and are listed above under their section. Values that moved:

| Value | Was in | Now in | Source (unchanged) |
|---|---|---|---|
| ch11 90 % CI 0.904–1.098 | §4.2 prose | Table 3, ch11 row, Equivalence column (TOST uses the 90 % CI; caption says so) | NV4 d1A ch11 |
| CV 5.8–13.5 %, χ² p 0.13–0.71 (eight gauges) | §4.2 prose | Table 3, new row "eight gauges consistent with the noise" | NV4 d1A rows ch3–ch7, ch10–ch12 |
| residual/noise variance 2.9–5.1 | §4.2 prose | Table 3, row ch1, ch2, ch8, ch9 | NV4 residual var / quiet var |
| lane-B χ² p 0.016–0.027, CV 31–40 % | §4.2 prose | Table 3, new row "lane B, range over channels" | NV4 d2B |
| 0.955 (0.863–1.057); 0.996 | §4.2 prose | Table 3 only (already there) | NV4 d1A |
| speed slope +6 % per 10 m/s (−23 to +35 %) | §4.2 prose | Table 10 only (already there) | NV4 TASK 2 |
| 1227, 3405 windows; 0.92 (0.83–0.96); 0.42 (0.26–0.54); 13.7–32.8 µε m | §4.3 prose | Table 4 (0.92 and 0.42 also kept in prose) | NV4 TASK 3 |
| 0.63; 0.30–0.37; 0.90 | §4.3 prose | Table 4 (0.63 and 0.90 also kept in prose) | NV4 TASK 4 diagnostic |
| +0.16 on st40, −0.35 on st36 | §4.3 prose | Table 4 | reanalysis §4 |
| 21.0 % and 14.6 % | §4.3 prose | Table 4 | NV4 TASK 4 diagnostic |
| 10.4 % vs 28.4 % | §4.3 prose | Table 4 | NV4 GLS-resid IN/LOO RMS |
| 20.3 %; 12.7 % vs 19.8 %; day 1 5.3/5.8/4.8 % | §4.3 prose | Table 5 only (already there) | NV4 TASK 4 |
| −1.49, −5.85 µε m/t | §4.4 prose | Table 3 only (already there) | NV4 d1A |
| κ ≥ 1.8 × 10⁷ (also kept in prose), α 0.51–1.15; τ = 3 %: κ 1.0–3.0 × 10⁸, α 0.64–0.80; τ = 4 %: κ 4.2 × 10⁷–2.0 × 10⁹, α 0.54–0.98 | §5.2 prose | Table 6 | IS |
| N8 0.14–0.42 (αEI; also kept in prose), 0.12–0.82 (design), α ≈ 0.5; prior α ∈ [0.9, 1.3]: 0.14–0.27 / 0.12–0.30 | §5.2 prose | Table 6 | IS; IF |
| C8 3.0 × 10⁻⁵–2.0 × 10⁻⁴ | §5.2 prose | Table 6 | IF |
| B_m 0.51 (N8), 0.12 (N7) | §5.2 prose | Table 7, new column $B_m$ | V3-T §5 |
| 0.341 (B, αEI normalisation) | §5.2 prose | Table 7, column B, N8 row | IS l. 6 |
| 0.476 | §5.2 prose | Table 7 only (already there) | V3-T §5 |
| Abstract: 1.2 %, 2.0–2.2 %, 0.98 (0.70–1.37), 0.63, 0.92, 55 + 90 + 55 m, 0.14–0.42, 0.1 mm, 25 t, 16–25 % | Abstract | removed from the abstract only; each value remains in the body (1.2 % as Table 2's +1.10/+1.19 %) | as listed under Abstract |
| Abstract: factor 6.6 | §5.2, Table 10 | also in the abstract | IF, DER 1.98/0.300 |

`code/v4/num_diff.py manuscript/v4/manuscript_pre_readability.md manuscript/v4/manuscript.md` confirms that no distinct numeric value disappeared and none appeared.
