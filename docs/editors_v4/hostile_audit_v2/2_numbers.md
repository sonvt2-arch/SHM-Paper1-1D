# Hostile audit v2, role 2_numbers: numerical values against logs and data

Scope: every number in `manuscript/ase/manuscript.md`, `supplementary_material.md` and `cover_letter_ASE.md`, checked against the logs listed in `code/supplementary/README.md`, the data in `data/bridges/cau-may/`, and recomputed independently where possible. Read-only: no repository file was changed. The recomputations ran on copies in the session scratchpad.

Independent recomputations:
- the Table S13 sets and their max/min ratios, recomputed at full precision from `code/theory2/logs/ident_static_scan.npz` with the `admissible()` logic of `ident_static.py` and the α prior of `ident_freq.py`;
- B_m from the adjoint formula on the base model;
- the Cramér–Rao bounds to five decimals;
- the Table S3 bands, by root finding on the closed forms;
- the laboratory ratios, the Table S17 biases, and the Table S11/S12 means and spreads.

## Recently changed items: verdicts

| Item | Source | Recomputed | Verdict |
|---|---|---|---|
| C8 max/min 1.5 / 3.4 / 6.6 / 2.4 | npz | 1.539 / 3.389 / 6.606 / 2.384 | correct |
| C7 max/min 1.1 / 1.4 / 1.5 / 1.1 (new column) | npz, `ident_freq.log` l.51 | 1.127 / 1.372 / 1.510 / 1.112 | correct |
| "6.6 against 1.5", "2.4 against 1.1" (Abstract, Sec. 1, 5.2, 7, S8, cover letter) | as above | as above | correct and stated the same way everywhere |
| "1.5 against 1.1 and 3.4 against 1.4" (Sec. 5.2) | as above | as above | correct |
| Table 3 prior row: N_w 0.124–0.297 / 0.190–0.211, R 0.13–0.34 / 0.56–0.66, α 0.90–1.15 | `ident_freq.log` l.51 | same | correct |
| Table S13 prior row: κ 1.8–6.7×10⁷, C8 3.0×10⁻⁵–7.2×10⁻⁵ (7.154), C7 3.3–3.6×10⁻⁴ | `ident_freq.log`, npz | same | correct |
| Table S3, all nine cells | `s06_threshold_sensitivity.log`; own root finding | all match to the third decimal | correct |
| Table S16, all 15 axle positions, loads and distances from T8 | `wp3_run.py` `cm_schemes()`/`cm_truck()`, `wp3_run.log` l.84–85 | match | correct |
| B_m 0.51 / 0.12 | `ident_theory.log` (+0.5115 / −0.1150); adjoint rerun: 0.51149 / 0.115001 | 0.51 / 0.12 (N7 rounds up, just barely) | correct |
| 90 % CI 0.76–1.27, ±26.7 %, "about 27 %" | `v4.log` l.35, 45: [0.756, 1.267] | – | correct |
| 1.010 / 1.016 / 1.017 | `s03_load_identification.log`: 1.0099 / 1.0161 / 1.0170; from Table S5: 2513.43/2488.68, 4168.15/4102.1, 7788.93/7659.0 | 1.00995 / 1.0161 / 1.0170. SLM deviations 1.0161/1.0099 = +0.61 % and 1.0170/1.0099 = +0.70 % match Table S4 | correct |

## Blocking

**B1. Table S13, row τ = 4 %, column C8: upper end misrounded.**
- Location: Supplementary S8, Table S13, row "τ = 4 %", column "C8 (m²/kN)". The row reads "5.5 × 10⁻⁵–1.9 × 10⁻⁴".
- Problem: the full-precision maximum is 1.8493 × 10⁻⁴ (npz). The log prints it as `1.85e-04` (`ident_static.log`, row "tau=4.00% Lv44"), which led to rounding twice. To two significant figures the value is 1.8 × 10⁻⁴. A reader who divides the printed ends gets 1.9/0.55 = 3.45, which does not match the stated max/min of 3.4.
- Fix: "5.5 × 10⁻⁵–1.8 × 10⁻⁴". The ratio 3.4 stays.

**B2. C7 upper end over the τ = 5.3 % admissible set misrounded, in two tables.**
- Location: Table S13, row "τ = 5.3 %", column C7, which reads "3.3–5.0 × 10⁻⁴". The same value appears in Table S17, row "N7, mid main span", column C, which reads "3.3–5.0 × 10⁻⁴".
- Problem: the full-precision maximum is 4.947 × 10⁻⁴ (npz). The log prints `4.95e-04` (`ident_static.log`, row "tau=5.27% Lv44"; `v3_numbers.log`, "N7 static set max C | 4.950e-04"), so the value was again rounded twice. To two significant figures it is 4.9 × 10⁻⁴. Neither the bias percentages in Table S17 (16–25 %, etc.) nor the max/min of 1.5 change.
- Fix: "3.3–4.9 × 10⁻⁴" in both tables.

These two items are classed as blocking only because the audit rules count a wrong printed number as blocking. Each is a last-digit rounding fix, and no ratio, conclusion or cross-reference depends on it.

## Should-fix

**S1. Main text, Sec. 5.3, paragraph 3: the variance penalty of the robust pair is understated for the estimator the paragraph uses.**
- Quote: "the pair at 100 m and 152 m from T5 is within 0.9 % in variance of the calibration-specific optimum under both A and B. … the standard deviation of the load falls from 24.8 % with N7 alone to 10.6 % with the pair and the zero-sum estimator".
- Source: `multisensor_placement.log`, section (4), l.402–403. At ρ = 0.9 the worst variance ratio is 1.0090 for GLS but 1.0099 for the zero-sum ("immune") pair. At ρ = 1 it is 1.0099 for both. Since the sentence that follows quotes the zero-sum estimator, the bound should be 1.0 %.
- Fix: "within 1 % in variance".

**S2. Table S17, row N8, column δ0 = 0.2 mm: the upper end "543 %" is one unit off.**
- Problem: `v3_numbers.log` computes it from a C8 already rounded to 3.000 × 10⁻⁵, giving 542.5, which was then rounded up. With the full-precision minimum C8 = 3.0010 × 10⁻⁵ (npz) the bias is 0.04/(3.0010 × 10⁻⁵ × 245.75) = 542.4 %.
- Fix: "82–542 %". Better still, compute `v3_numbers.py` from the unrounded set limits. The other cells of the row (54, 136, 271, 1356) are unaffected.

**S3. `code/supplementary/README.md`, row for Table S13: incomplete source.**
- The row names only `ident_static.py` / `ident_static.log`. The row "τ = 5.3 %, prior α ∈ [0.9, 1.3]", including the newly added 1.1 and the values 7.2 × 10⁻⁵ and 3.6 × 10⁻⁴, exists only in `code/theory2/logs/ident_freq.log` (l.45 and 51). `ident_static.log` contains no prior row. A referee who follows the README cannot find these numbers.
- Fix: add `ident_freq.py` / `logs/ident_freq.log` to the Table S13 row, as the README already does for Table 3.

## Minor

**M1. Table 3 and Table S15: "–: not computed" is not accurate.**
- The rows "Haunched, pinned piers" and "Haunched, fixed piers" show "–" for R, captioned "not computed". `gc_results.log` (T4, "haunched, pinned" and "haunched, fixed", L_v = 44 m) does compute them: R_w = 0.022 (N8 at 0.4L), −0.039 (N8 at mid side span), 0.508 (N7) with pinned piers, and 1.000 for all with fixed piers.
- Fix: enter the L_v = 44 m values, or change the note to "not tabulated over the haunch variants".

**M2. `code/v3/logs/v3_numbers.log`, PART A: row labels do not match Table S17.**
- The rows that supply the minimum constants in Table S17 are labeled "N7 joint set (static+f3) min C" and "N8 joint set (static+f3) min C", but Table S17 claims ranges over the static set. The values coincide (3.280 × 10⁻⁴ and 3.000 × 10⁻⁵ are also the static-set minima in `ident_freq.log` l.50), so no number is wrong. The labels just make the source hard to trace.
- Fix: relabel the rows, or add a static-set minimum row.

**M3. Supplementary S3, last paragraph: the factor range is incomplete.**
- Quote: "their white-noise variance is lower by a factor of 1.5–6.6".
- Source: `multisensor_theory.log`, T4, gives Var_opt/Var_unif = 0.1513 (S = 2 m, factor 6.6) to 0.6779 (S = 160 m, factor 1.5). At S = 0 the ratio is 0.1232, a factor of 8.1. The stated range therefore leaves out the zero-shift case, and the text does not say so.
- Fix: write "for entry-shift ranges of 2–160 m", or "1.5–8.1".

**M4. Cover letter, paragraph 6: the table count needs clarifying.**
- Quote: "with 7 figures and 5 tables".
- The main text has four numbered tables (Tables 1–4). The fifth is the unnumbered "Principal symbols" table, which is how `submission_checklist.md` counts it.
- Fix: "7 figures, 4 tables and a table of symbols", or keep "5" if the word-equivalent count requires it.

**M5. `code/supplementary/README.md`: the s06 script is missing from part of the README.**
- The directory table ("laboratory and two-span scripts `s01`–`s05`"), the run comment ("# s01-s05") and the table "Laboratory and two-span scripts in `code/supplementary`" all omit `s06_threshold_sensitivity.py`, which `run_all.sh` (l.27) runs and Table S3 relies on.
- Fix: add s06 in those places.

**M6. Shipped logs and data contain "[NEED VALUE]" placeholders.**
- `ident_fisher.log` l.1 ("rotation 3.0 % [NEED VALUE]"), `ident_static.log`, last section ("pier geometry [NEED VALUE]"), and `data/bridges/cau-may/cau-may_truck_and_dynamic.csv` ("individual truck weights NOT reported [NEED VALUE]"). The last contradicts `cau-may_10_trucks_weighed.csv`, which gives exactly those weights (Table S11).
- The text correctly calls the 3 % an assumption. The placeholders still look unfinished in a public archive.
- Fix: replace them with "assumed" wording, and correct the CSV comment.

## Verified without finding (selection)

**Sections 2 and 3; Tables 1 and S2–S5**
- λ = 1.4574, β = 1.7006, 1.8794, 1.6180, 2.3028, 2.6691, ζ0 = 0.276 / 0.177, 0.9647. Bands 1.385–1.525, 1.621–1.775 and 0.676–0.812 (0.19–0.32).
- 981 checks, 8.1 × 10⁻¹¹, 2.8 × 10⁻⁹, 5.4 × 10⁻¹⁰; truncation errors of 59 % and 10 %.
- R_ε = 0.667 against R_w = 0.571. N_w 0.287 → 1.037 and 0.755 → 0.500.
- Table S2 (all cells); the six asymmetric ratios; the span contributions 1.50–2.00 and −0.125 to −4.00.
- Laboratory: C_m = 61.54; 0.0126 mm = 0.44 %; RMS residuals 0.030 and 0.55 mm.
- Table S4 (all cells): BPM-to-SLM ratio 1.0049; trapezoid error −0.500 %.

**Section 4; Tables 2 and S6–S10 (`v4.log`, `tests.log`, `field.log`)**
- Every cell of Tables 2 and S6–S10.
- Ratio 0.98 (0.70–1.37); 22–26 % (0.740–0.783); lane 0.79 (0.59–1.00); 0.92 (0.77–1.06); GLS 0.82 (0.73–0.91); st36 0.64 (0.47–0.81).
- Gauge ratios 3.24 ± 0.56 against 1.82 ± 0.10 (2.50 SE apart); ch11/ch8 3.9 (−5.85/−1.49); beam model 0.978–1.003.
- Paired difference +8.5 (+2.3 to +15.1); 0.63 against 0.90; 8.5 against 23.4 (RMS 10.4 / 28.4); predicted SDs 16.2 / 32.5 / 19.8 / 19.4 / 12.7 / 13.3 / 16.1; weights +0.16 / −0.35.
- Speeds and confounding: 1.4 % / 4.6 % (recomputed over the 15 runs used); 1.139, SD 0.124; corr 0.98; +6 % per 10 m/s (−23 to +35); noise 13.7–32.8 µε m.
- Beam model and run data: r² 0.79–0.94; zeros at 121.6 and 190.8 m; strain-constant ratio 0.69 (0.56–0.93); R 0.51; span shares 170 / −26 / −66 %; GVW 21.2–22.8 t; 10 000 bootstrap resamples (`nb_v4.py` NBOOT).

**Section 5; Tables 3, 4 and S11–S15**
- Calibrations: misfits +2.4/+12.3 % (A) and −2.8/+2.9 % (B); κ_B = 1.68 × 10⁸; α 0.716 (28 % below design); k 2.75 × 10⁷ and 1.2 × 10⁸; r87 1.058, 1.039–1.092, 1.126, 1.091.
- Tolerance: SD 4.7–5.0 %, SEM 1.9–2.0 %, 1.75 %, 2.64 %, τ = 5.27 %; the measured means 5.55 / 15.43 mm and the 2.05 mm spread (13 %) recomputed from Table S12; 25.06 t from Table S11 (matches the CSV); Table S14 matches the CSV.
- Möbius law and sensitivities: k_g = 4.36 × 10⁷; κ/k_g = 0.63; 14.0 and 0.59; 5 × 10⁻⁶; 4.4 × 10⁻⁷; 6.5 against 1.5.
- Cramér–Rao bounds: 0.87 (0.86503), 0.18 (0.17727), 0.24 (0.23680), 0.04; α* = 1.07; 167 µrad.
- Indicators: N_M 0.048 and 0.163–0.212; zeros at 26.0–33.3 m; R_ε 0.65–1.00; |N_M| ≥ 0.39; gain about 0.26–0.34 and 0.207 (recomputed from h^−1.943); N_F 0.47–0.61.
- Placement: 4–10 m; 24.8 / 10.6 / 22.5 %.
- Table 4 (0.121, 0.284, ratio 2.34 → 2.3; −58 / −29; 0.006 / 0.17; 171.3 m).
- Every other cell of Tables 3, S13, S15 and S17. Placement and white-noise figures: 96 cases, 0.6 % (1.0062), 1.65–2.0, about 5 × 10⁻⁶ and 5 × 10⁻⁵ (4.5 × 10⁻⁶ and 4.5 × 10⁻⁵).

**Section S9 and cover letter**
- S9: f₁ = 11.942 Hz; ≤ 1 % for t_cr/T₁ ≥ 8 (0.99 %); > 15 % below 2.5 (2.52); 0.23 mm; 12.4 s.
- Cover letter: every number matches the main text.

**Built PDFs:** `Manuscript_ASE.pdf` and `Supplementary_Material_ASE.pdf` contain the current statements, including the new C7 column.

## Count per class

- Blocking: 2 (B1, B2; both are last-digit rounding errors in table entries)
- Should-fix: 3 (S1–S3)
- Minor: 6 (M1–M6)
