# Traceability of numeric values in `manuscript/v3/manuscript.md`

Every number in the v3 manuscript is listed with its source. Numbers carried unchanged from SCHM v2 point to `manuscript/schm/traceability.md` (abbreviated **SCHM-T**), which in turn names the original log. Rounding to at most four significant figures was applied to closed-form constants; the exact value is in the source.

## Source abbreviations

| Code | File |
|---|---|
| GCR | `code/theory2/logs/gc_results.log` (package 1A, tables T1–T4) |
| VG | `code/theory2/logs/verify_general.log` (981 checks, summary l. 1049–1057) |
| 1A | `docs/pkg1/1A_general_channels.md` |
| MST | `code/theory2/logs/multisensor_theory.log`; `code/theory2/results/T2_Ok.csv`, `T3_immune.csv`, `T4_structure_aware.csv` |
| MSP | `code/theory2/logs/multisensor_placement.log`; `results/placement_distinct.csv`, `placement_caumay_robust.csv` |
| MSMC | `code/theory2/logs/multisensor_mc.log`; `results/mc_summary.csv` |
| 1B | `docs/pkg1/1B_multisensor.md` (quotes the three logs above) |
| IT | `code/theory2/logs/ident_theory.log` |
| IS | `code/theory2/logs/ident_static.log` |
| IF | `code/theory2/logs/ident_freq.log` |
| IFI | `code/theory2/logs/ident_fisher.log` |
| 1C | `docs/pkg1/1C_identifiability.md` (quotes IT, IS, IF, IFI) |
| NBT | `code/norbwim/logs/tests.log`; `code/norbwim/results/test_*.csv`, `events_field_qc.csv` |
| NBV | `code/norbwim/logs/fe_veb.log` |
| 3B | `docs/pkg1/3_norbwim_analysis.md` (metadata from the dissertation [51] and dataset files) |
| FP | `code/fieldplan/results/fieldplan_compute.log` |
| V3N | `code/v3/logs/v3_numbers.log` (new script `code/v3/v3_numbers.py`, run with `python3 -I`) |
| S02–S05 | `code/supplementary/logs/s02_quadrature_table3.log` … `s05_moving_force.log` |
| CMI | `data/bridges/cau-may/INVENTORY.md` |
| CR | Crossref / DataCite API record, checked 2026-10-18 |
| DER | arithmetic on sourced values, shown |

## Title page, abstract, keywords

| Value | Source |
|---|---|
| $(3+\sqrt{33})/6$ | SCHM-T (OLD Eq. 11c); VG group A |
| ratio 0.999 ± 0.140 | NBT (a) row `day2_laneA_T3T4 avg`, `T4_over_T3` 0.9991, se 0.1397 |
| 6.5–7.0 % | NBT (b) `day1_laneA_T1T2 avg` MAE 6.51 (other truck), 7.00 (same truck) |
| 2 m; up to 2.7 times | 3B §2 (about 2 m pitch); NBT (f) gauge ratios, max 2.706 (ch11/ch4) |
| 55 + 90 + 55 m | CMI §1 |
| 0.12 and 0.82 | IS l. 40 (N8d [0.124, 0.822]) |
| 0.1 mm, 25 t, 21–25 % | V3N Part A, N7 joint set 21.2 / 24.8 % at 0.1 mm (truck 25.06 t) |

## Section 1

| Value | Source |
|---|---|
| 2012, four trucks [1] | SCHM-T §1 |
| seven-span, within 5 % [29,30] | SCHM-T (CR Helmi 2014; Lydon 2016) |
| Ojio–Yamada primary source, ICWIM3 Orlando 2002, pp. 209–218 | TRID record 723286 (trid.trb.org/view/723286) and Connecticut State Library reference list (web search 2026-10-18) |
| [35] sparse sensing, single-span, number and location of sensors | CR 10.15517/mym.v11i0.46400 (abstract) |
| [42] continuous multi-girder, lane influence lines | CR 10.1007/s11709-020-0653-0 (title) |
| [43–45] long-span box girders | CR records of the three DOIs (titles) |
| five-span [41] | SCHM-T §1 |
| 55 + 90 + 55 m | CMI |

## Section 2

| Value | Location | Source |
|---|---|---|
| 59 % (rotation, truncation) | §2.1, App. B | VG group F; 1A §4 |
| 10 % (moment, truncation) | App. B | VG group F; 1A §4 |
| Eq. (4) both forms | §2.2 | SCHM Eqs. (5), (8); 1A §2.1 |
| 1.4574, 0.4215 | Eq. (7) | SCHM-T (1.45743, 0.42154) |
| 1.7006 | Eq. (8) | SCHM-T (1.700594; V3 sec. B) |
| 1.8794 | §2.2, Table 1 | SCHM-T (1.879385) |
| 1.385–1.525; 1.621–1.775 | §2.2, §7 | SCHM-T (P7 Part E: 1.385061–1.524695; 1.621399–1.775021) |
| 981 checks; 8.1 × 10⁻¹¹ | §2.2 | VG l. 1049–1052 |
| 0.75L | §2.2 | GCR T1 ($\rho_L$ = 1, $\xi_0$ = 0.7500) |
| 0.276, 0.177 | §2.2 | GCR T2 ($\eta_0$ 0.2764 at β = 1; 0.1767 at β = 1.636) |
| $\mu<4$ | §2.2 | 1A §2.2 |
| 0.676 < ξ < 0.812; 0.19–0.32 | §2.2 | GCR T1 band [0.6760, 0.8116]; DER 1 − 0.8116 = 0.188, 1 − 0.6760 = 0.324 |
| $\lvert N_M\rvert = \mu$ at the support | §2.2 | 1A §2.4 |
| Table 1: 1.6180, 2.3028, 2.6691, $\sqrt{3/2}$, end/pier rotation, shear, mid-main always blind | Table 1 | 1A §2.2 table; GCR T1 rows ρ_L 1.61803, 2.30278; T2 rows; VG group E |
| $2R_A/(q_0L_1) = \xi_0$ | §2.2 | 1A §2.2 identity 1 |
| 4/7 | §2.3 | SCHM-T (DER 1.000/1.750) |
| $R_\varepsilon$ 0.667, $R_w$ 0.571 | §2.3 | GCR "Cancellation ratio" block (0.6667, 0.5714) |
| uniform weight only translation-invariant for every structure | §2.4, App. B | 1B §2 Theorem 1 and the correction in §2 |
| 1.5–6.6 times smaller variance | §2.4 | MST / T4_structure_aware.csv: Var opt/unif 0.6779 (S = 160 m) and 0.1513 (S = 2 m); DER 1/0.6779 = 1.48, 1/0.1513 = 6.61 |
| −1.1 % to +2.0 % | §2.4 | MSMC case D, misspecified structure: −1.12 % to +1.99 % (1B §5) |
| 1.65–2.0 | §2.4 | MST T3: factors 1.647 … 2.000 (1B §3) |
| about 10⁻⁴; σ = 0.01 mm; ε0 = 0.1 mm | §2.4 | 1B §3 (MST) |
| 96 cases | §2.4 | MSP (1B §4: min ratio 1.000000 over 96 cases) |
| 10⁵ configurations; within 0.6 % | §2.4 | MSMC (1B §5) |
| Eq. (15); Eq. (16) | §2.5 | 1C §2.2, §2.3; IT |
| 4.4 × 10⁻⁷ | §2.5 | IT (1C §2.3) |
| 0.287 → 1.037; 0.755 → 0.500 | §2.5 | IT (1C §2.3: N_side(0.4) 0.287 → 1.037; N_main 0.7546 → 0.500) |

## Section 3 (laboratory)

| Value | Source |
|---|---|
| 25 mm, 2.03 mm, $I$ = 16 530 mm⁴ (16 529.8), 200 GPa, 2500 mm | SCHM-T §3 (OLD l. 950–960); rounding |
| 61.54 mm²/N (61.541); 8 × 10⁻⁴ | SCHM-T §3 |
| 0.005 mm; 250 mm; three cycles | SCHM-T §3 |
| 40.64 N; 2145/4684 g; 2550/5100/5100 g; 250, 500 mm | SCHM-T §3 |
| rms 0.030 vs 0.55 mm | SCHM-T (P7 Part C: 0.0298, 0.5529 mm) |
| 0.0126 mm, 0.44 % | S03 l. 17–20 (SCHM-T reproduction block) |
| −0.500 %, +0.027 %, −0.92 %, −0.44 % | S02 l. 12–14; SCHM Table 3 |
| Table 2 (66.99, 67.73, 67.40, 125.08, 126.57, 125.95 N; +1.10, +0.61, +1.19, +0.70 %) | SCHM Table 4; S03 |
| 1.0049 | SCHM-T (1.00489 = 2513.43/2501.19) |
| 1.010, 1.016, 1.017 | SCHM-T (P7 Part C) |
| 2500 mm and 3644 mm | SCHM §7.2 (DER 2500 × 1.45743 = 3644) |

## Section 4 (NOR-BWIM)

| Value | Source |
|---|---|
| CC0; dataset citation | CR (DataCite 10.7294/26880898.v1: creators Moghadam, Sarlo; Virginia Tech; 2024; CC0) |
| 86.5 + 3 × 144 + 86.5 = 605 m; 3.8 / 9.5 m | 3B §2 ([51] §2.2.1) |
| 158.5 m | 3B §3 item 2 |
| 21.17–22.82 t, 100 Hz, 12 channels | 3B §2 run list (used runs R1–R4, R7–R9: 22.82, 22.51, 22.45, 22.18, 22.10, 21.17, 21.61 t); sampling 3B §2 |
| 26.8 t, 25.9 t; 200 Hz; four channels | 3B §2 ([51] Table 2.1, §2.2.3) |
| within 1–2 % of GPS speeds | 3B §2 and NBT speed table (v_used vs v_script) |
| 5 s; 80 vehicle-free records | 3B §3 items 3–4 |
| three runs excluded, four passes | NBT "Exclusions" (R5, R6, R10; X1, X1r, X2, X2r) |
| CV 5.8–13.5 % (wheel-path ch4, ch5, ch11, ch12: 13.5, 7.0, 5.8, 10.3 %); 5.6 % (avg) | NBT (a) rows ch4, ch5, ch11, ch12, avg |
| χ² p 0.14–0.60 | NBT (a): 0.157, 0.169, 0.595, 0.144 |
| −2.18 ± 0.09, −2.12 ± 0.25 µε m/t | NBT "st40 pooled" line (−2.179 ± 0.092; −2.124 ± 0.251) |
| 0.999 ± 0.140; 1.010 ± 0.115 | NBT (a) day 2 avg and st36 |
| Table 3: 6.1 %, 14.4 %, 20.2 % | NBT (a) cv_noise avg day 1 0.0608; day 2 cv 0.1437, cv_noise 0.2021 |
| 7.0 %, 6.5 % | NBT (b) |
| 5.1 %; 17.1 % | NBT (b2) day2 avg calib T3 MAE 5.06; calib T4 17.12 |
| 17.8 % | NBT (b) day2 avg MAE 17.77 |
| 3–4 times | 3B §4(b); DER 18.80/5.48 = 3.4 (test_f_model.csv) |
| −3.6 ± 5.8 %; +5.2 ± 13.0 % per 10 m/s | NBT (c) avg rows (−3.60 ± 5.83; 5.15 ± 12.95) |
| 0.93 ± 0.11, 0.92 ± 0.11; 52.7 t; 48.8 t, 48.5 t; −7.3 %, −7.9 % | NBT (e) M1, M2 avg rows (0.927 ± 0.106; 0.921 ± 0.109; 48.83, 48.55 t; −7.35, −7.88 %) |
| 0.81 ± 0.09; 0.66–1.02 | NBT (d) (0.812 ± 0.086; st36 0.659 … st40 1.015) |
| 0.68–2.71; 1.82 ± 0.10; 2.41 ± 0.10; 0.978–1.003 | NBT (f) gauge ratios (ch8 0.681 … ch11 2.706; lane B st36 1.819 ± 0.096, st31 2.413 ± 0.098); model test_f_model.csv haunch n = 2: 0.978–1.003 |
| about 3.2 vs 1.8 | NBT (f) st36/st40 lane A 3.239, lane B 1.819 |
| $r^2$ 0.79–0.94 | V3N Part C (min 0.791, max 0.940, n = 15) |
| 121.6 and 190.8 m; about 35 m | NBT (f) beam model zeros_span2; DER 158.5 − 121.6 = 36.9, 190.8 − 158.5 = 32.3 |
| 0.69; 0.56–0.93 | V3N Part B (0.692 n = 2; 0.926 n = 2.5; 0.560 uniform) |
| net/positive 0.51 | V3N Part B (0.513) |
| −26 %, −66 %, +23 % | V3N Part B span shares [−26.0, 171.5, −65.5, 23.4, −3.5] % |
| 0.1–0.3 µε below 0.2 Hz; 50–130 µε m | 3B §5 item 1 |
| 5.5 and 18.8 µε m | NBT test_f_model.csv noise_sd_Idx (5.477; 18.803) |
| 10 %, 35 % | NBT test_f_model.csv rel_err_at_sensor_pct (10.05; 35.42) |
| ±12 m | 3B §4(f) |
| factors 2–3 | NBT (f) |

## Section 5 (Cầu Mây)

| Value | Source |
|---|---|
| DT389, Kinh Mon, Hai Duong; β = 1.636; 2.40/5.40 m; 5.482, 59.61 m⁴; 36 057 MPa | CMI; SCHM-T §4 |
| June 2020; four / six trucks; 5 + 10 + 10 t; 25.06 t | SCHM-T §4 and authors' answers (SCHM-T update 2026-10-18) |
| 5.55 mm, 15.42 mm | SCHM-T §4; 1C S7 (5.5533 / 15.4250) |
| $L_v$ = 44 m (40, 45); $n$ = 2.943 (2.5, 3.2); ±1.5 m rigid zone | 1C §3 S3–S5; IS l. 39–44 |
| A: α = 1, k = 2.75 × 10⁷; misfit +2.4/+12.3 % | IS l. 13 |
| A′: α = 1.088; −4.6/+5.0 % | IS l. 14 |
| B: α = 0.716, k = 1.2 × 10⁸; −2.8/+2.9 % | IS l. 15 |
| 1.126 at 10⁷; 1.058 at 1.68 × 10⁸; 1.091 | 1C §4.1 table (IS) |
| 1.039–1.092; 4–9 % | 1C §4.1 variants (1.0391 … 1.0916) |
| 28 % | DER 1 − 0.716 |
| 1.9–2.0 %; 1.75 %; 5.3 % | 1C §3 S7, S8; F1 (τ = 5.27 %) |
| κ ≥ 1.8 × 10⁷; N8 0.12–0.82; R 0.13–1.00; N7 0.19–0.29 | IS l. 40 |
| α ≈ 0.5–0.7 | 1C §4.1 |
| prior: 0.12–0.30 | IF l. 51 (N8d [0.124, 0.297]) |
| $k_g$ = 4.36 × 10⁷; 14.0; 0.59; 0.63 | IT l. 28–36 |
| $B_m$ 0.51, 0.12 | IT (S_kappa +0.5115, −0.1150) |
| 6.5; 1.5 | 1C §4.3 shape factor (6.49; 1.51) |
| Table 4, prismatic column 0.287 (0.14), 0.163 (0.08), 0.755 (0.70) | GCR T4 prismatic (N_w 0.2870, R_w 0.144; mid side 0.163, 0.08; N7 0.755, 0.70); 1A §3 table |
| Table 4, A / A′ / B | IS l. 13–15 (A′ N8 mid 0.089; R of A′ N8 0.172, N7 0.581) |
| Table 4, static and joint sets | IS l. 40; IF l. 50, 53 |
| Table 4, bounds 0.023 … 0.446; −0.066 … 0.375; 0.263 … 0.145 | 1C §4.4 (IS); SCHM Table 5 with the N7 order corrected |
| 0.341 | IS (1C summary item 7) |
| 3.43, 3.64, 3.63 Hz | 1C §3 D1 |
| 24.4–29.7 t/m; 1.0–1.2 | 1C §3 M7, D2 |
| 1.19–2.48 Hz; α ≥ 1.91 | IF (1C §4.2) |
| 2.89 Hz; 3.28 Hz | IF (2.888; 3.28) |
| κ 1.8 × 10⁷–1.1 × 10⁸; α 0.80–1.15; N8 0.12–0.39; N7 0.19–0.22 | IF l. 53 |
| 3.0–3.1 Hz | 1C §3 D1 (3.03–3.11) |
| 3.3–3.8 × 10⁻⁴ m²/kN | IF l. 53 (C7 3.28–3.84 × 10⁻⁴) |
| 26.0–33.3 m; 0.048; 0.163–0.212; 0.65–1; 5–10 m; ≥ 0.39; one fifth; 0.47–0.61 | 1A §3 (GCR T4) |
| 4–10 m; (100, 152) m; 0.9 % | 1B §4 (MSP: worst ratio 1.0090) |
| 24.8 %, 10.6 %, 0.071 % | MST T3 Cầu Mây A (24.80; 10.57; 0.0712) |
| 167 µrad | IFI (1C §4.3) |
| 0.87 → 0.18; 0.24 | IFI (0.865, 0.177, 0.237) |
| Table 5: 0.121 / 0.284; −58 / −29 µrad; 0.006 / 0.17; 1.78, 2.30 / 1.59, 1.75 | FP "discriminating A vs B" block; DER 2.35/381.32 = 0.006, 81.59/477.96 = 0.171; f-ratios DER from FP frequencies (2.505/1.407, 3.239/1.407; 2.594/1.631, 2.846/1.631) |
| 171.3 m | FP (S1 position) |
| factor 2.3 | DER 0.284/0.121 = 2.35 |
| 18.6 s, 26 at 40 km/h | FP T_cr block (18.6 s, 26.1) |

## Section 6

| Value | Source |
|---|---|
| 0.07 % | SCHM Appendix B / S04 (random noise σ_a = 0.0025 mm) |
| 1 % at ≥ 8; < 4.2 % at ≥ 4; > 15 % below 2.5 | S05 (SCHM-T reproduction block) |
| 10–28 m/s | NBT (c) v_min/v_max |
| Table 6 (all entries); 87–271 %; 21–25 % | V3N Part A |
| 200 m; 25.06 t | SCHM-T (P7 Part A) |
| up to 0.23 mm | SCHM-T (WP4 l. 9, l. 45: 0.17–0.23 mm, Phuong Do N2) |
| 0.81; 0.66–1.02 | NBT (d) |
| 2.05 mm; about 13 % | SCHM §4.4 (2.05 mm); DER 2.05/15.42 = 0.133 |
| 7–8 % | NBT (e) (−7.35, −7.88 %) |
| 12.4 s at 60 km/h | FP T_cr block |
| Table 7: 6.5-fold; 10 %/35 %; −3.6 ± 5.8 %; ≤ 1 %; 0.81; 2.05 mm; 0.92–0.93; 1.010 → 1.017; 0.07 % | as in the rows above |
| 0.6–0.7 % | Table 2 (0.61, 0.70 %) |

## Section 7–8 and appendices

| Value | Source |
|---|---|
| bands 1.385–1.525, 1.621–1.775 | as §2.2 |
| five reference crossings | SCHM §6.3 recommendation (Eq. 20 there) |
| App. A: 1.50–2.00; −0.125 to −4.00 | SCHM-T (OLD Table 12) |
| App. A: 4/5; 1.3; cubic; 30β³ − 69β − 16; 10β³ − 27β − 8; 0.9647; ν; 0.587–0.592 | SCHM-T §2 (WP2; V3); editor 3 note for the upper-edge cubic |
| Table A.1 | SCHM Table 2 (WP2 §3; V3 sec. B), rounded to 4 s.f. |
| App. B: 2.8 × 10⁻⁹; 5.4 × 10⁻¹⁰ | VG l. 1055–1056 |
| App. C: 5 × 10⁻⁶; 10⁵–10¹² | IT l. 29 (4.6 × 10⁻⁶) |
| Table D.1 | SCHM Table C.1 (unchanged) |

## Word counts

`python3 code/analysis/wp7b_checks.py manuscript/v3`: abstract 247 words; main text (Sections 1–8, prose only) 7461 words; 16 numbered equations, all cited; 5 `[NEED VALUE]` in manuscript.md.
