# Reproduction report: SCHM manuscript against the supplementary scripts

Date: 2026-10-18. Manuscript: `manuscript/schm/manuscript.md` (not edited). Environment: Python 3.13.16, NumPy 2.5.3, SciPy 1.18.1, SymPy 1.14.0, matplotlib 3.11.2, pandas 3.0.5. All scripts were run with `python3 -I`; console logs are in `logs/`.

**Match** means equal after rounding to the digits printed in the manuscript. **Mismatch** means a difference larger than that rounding. **Not reproduced** means no script in the repository produces the number and the method is too loosely specified to rebuild it without guessing. No parameter was tuned to force a match. Where the manuscript leaves a modelling choice open (mesh, number of steps, speed spacing in `s05`), the choice made is stated, and its effect is shown in the log.

## 1. Summary of mismatches

| # | Manuscript statement | Script value | Assessment |
|---|---|---|---|
| M1 | Section 6.1: trapezoidal bias "at a spacing of 300 mm −0.110 %, at 375 mm +0.249 %" (from OLD l. 1243) | Two-load group with its spacing changed: −0.171 % / +0.014 %. A single influence-line copy shifted by 50 / 125 mm: −0.020 % / +0.250 %. Other interpretations tried (heavier load leading, the three-load group with one spacing changed, records truncated at 2l + a): none gives −0.110 % (closest −0.116 %, three-load group [0, 300, 550] mm). | **Not reproduced.** +0.249 % is consistent with the single shifted copy at 125 mm (+0.250 %), but −0.110 % matches no interpretation. The conclusion that the residual does not cancel when spacings are not multiples of Δx stands: the two-load residuals are +0.33 and +0.51 pp. The stated range "0.4–0.75 %" depends on the unreproduced pair. (`s02`) |
| M2 | Section 3.2 / recommendation 9: Simpson quadrature is "nearly exact"; for the 21- and 23-interval records it needs the 3/8 end panel | Analytical two-load record: Simpson+3/8 bias −0.92 % (trapezoid −0.50 %); three-load: −0.44 %. The influence line has slope discontinuities at entry (x = 0) and exit (x = 2l) of every axle. For trailing axles these kinks fall inside a Simpson panel, and Simpson then loses its accuracy. | **New finding, not a number mismatch.** "Nearly exact" holds only when every axle's entry and exit coincide with panel boundaries (the single-load record). The text recommends Simpson for multi-axle records without this caveat. (`s02`) |
| M3 | Appendix B: "the three-load case agrees within 0.1 percentage point" | Std. dev. for zero offset: 0.37 % (three loads) against 0.64 % (two loads), a 0.26 pp difference; p5 differs by 0.52 pp. Gain p95 +0.12 pp; random p5 +0.14 pp; bias always +0.08–0.09 pp. | **Mismatch.** True for the bias and for the gain-only std. dev.; false for the zero-offset scenario. That case is expected to differ, because the offset term εL/I_y scales as 1/I_y. (`s04`) |
| M4 | Section 3.2: largest deviation 0.0125 mm, 0.43 % of the maximum deflection | 0.0126 mm (x = 2000 mm: 1.4213 − 1.4087), 0.44 %. The value 0.0125 occurs at x = 2250 mm. | **Mismatch (last digit).** (`s03`) |
| M5 | Table 9 envelope for T_cr/T₁ ≥ 3, 4, 6, 10, 15, 20: 8.6, 3.8, 1.7, 0.32, 0.15, 0.08 % | 47 log-spaced speeds: 7.55, 3.04, 1.29, 0.51, 0.18, 0.11 %. Dense 300-speed sweep: 8.64, 4.09, 1.77, 0.59, 0.23, 0.13 %. The ≥ 2 (17.64 %) and ≥ 8 (0.99 %) entries match. | **Partial mismatch.** The envelope depends on how the speeds were sampled, which the manuscript does not give. The dense sweep matches the manuscript at ≥ 3 and ≥ 6 within 0.1 pp, but is 1.6–1.8 times larger at ≥ 10, 15 and 20 (the smooth regime, where E ∝ (T₁/T_cr)² and sampling does not matter). Even E evaluated exactly at T_cr/T₁ = 10, 15, 20 (−0.34, −0.18, −0.11 %) exceeds the printed envelope, so the manuscript's tail cannot be an envelope of this model. The damping choice (modes 1&3 or 1&2, mass- or stiffness-proportional) changes the tail by less than 0.02 pp. (`s05`) |
| M6 | Eq. (21): T_cr/T₁ ≥ 4 ⇒ \|E_dyn\| < 4 % | Max \|E\| = 4.09 % (dense sweep) and 4.12 % (fine scan, at T_cr/T₁ = 4.48) | **Mismatch, marginal.** "< 4 %" should read "≲ 4 %" (or the threshold should be ≥ 4.5). ≥ 8 ⇒ ≲ 1 % is confirmed (0.99 %). (`s05`) |
| M7 | Section 6.5: exit deflection "39 % of the static peak at T_cr/T₁ = 1.5" | 34.5 % (upward, i.e. opposite sign to the static peak) | **Mismatch.** Same mechanism, smaller value. (`s05`) |
| M8 | Section 6.5: "Extending the window by four fundamental periods roughly halves the error" | The error falls to 0.72 / 0.77 / 0.80 of its value at T_cr/T₁ = 1.5 / 3 / 8 | **Mismatch.** A 20–28 % reduction, not a halving. (`s05`) |
| M9 | Section 6.5: damping 0.5–5 % "changes it monotonically, and less damping gives less error" | E is monotonic in ζ at T_cr/T₁ = 3, 5, 8. \|E\| increases with ζ at 3 and 8, but not at 5, where E changes sign (+0.38 % at 0.5 %, +0.02 % at 1 %, −0.55 % at 2 %). | **Mostly consistent.** "Less damping, less error" is not universal. (`s05`) |
| M10 | Section 6.5: multi-axle spread 0.33 % at T_cr/T₁ = 11.9 and 1.95 % at 3.0 | 0.23 % at 11.94 (v = 5 m/s) and 2.31 % at 2.99 (v = 20 m/s), for 1 axle and for 2 or 3 equal axles at 0.5/1.0/1.5 m | **Same order, not exact.** The axle configurations are not specified in the manuscript; this set is an assumption. (`s05`) |

The other numbers checked match (Sections 2–4 below). Rounding note: the measured integrals 2513.4250 and 7788.9250 mm² are exact four-decimal sums. Binary floating point prints them as 2513.42 and 7788.92; exact decimal arithmetic, rounded half up, gives the manuscript's 2513.43 and 7788.93 (`s03` prints both).

## 2. Two-span theory (s01; `logs/s01_symbolic_two_span.log`)

| Manuscript | Location | Script | Status |
|---|---|---|---|
| R_A, R_B, R_C, Eq. (A.1); 13P/32, 11P/16, −3P/32 | App. A | force method, symbolic | match |
| M_B = −Px(l² − x²)/(4l²) | App. A | symbolic | match |
| Eq. (A.2), all three branches | App. A | two independent routes (force method in the load position; double integration under a load at l/2 with the six listed conditions, plus Maxwell): difference 0 | match |
| Continuous and twice differentiable at l/2 and l; third branch 64EI, not 192EI | App. A | jumps of η, η′, η″ = 0; ratio 3 | match |
| −1.1255 mm at x = 3750 mm; Table C.1 analytical column | App. C | −1.1255; max difference 5.4 × 10⁻⁵ mm (rounding) | match |
| 2.875Pl³/(192EI); 71.9 %; x = 0.480l; 72.1 % | App. A | 23/8; 71.875 %; 0.4804; 72.06 % | match |
| C_m = l⁴/(192EI) (integral of η, and w_q(l/2)/q₀) | 2.1, 2.2 | symbolic | match |
| Eq. (4) with μ of Eq. (5), from slope continuity | 2.2 | derived from the three-moment equation; difference 0; μ = −8M_B/(q₀L₁²) | match |
| Table 1, all seven closed-form values | 2.2 | 1.00000000, 1.37500000, 0.41500000, 0.00000000, −2.00000000, 1.03989535, 0.60480000 | match |
| Table 1 "Difference" column (1 × 10⁻¹¹ … 9 × 10⁻¹¹) | 2.2 | FE (40 Hermite elements per span, both Eq. (3) routes): 3 × 10⁻¹² to 5.6 × 10⁻¹⁰ | match in kind (round-off). The exact digits depend on mesh and BLAS and cannot be reproduced; the optimal-sensor row is 5 × 10⁻¹⁰ here against 9 × 10⁻¹¹ printed. |
| μ_crit = 2(1 + ξ − ξ²)/(1 + ξ); ρ_EI,crit formula; 5/3 | Eq. (6) | symbolic | match |
| 3ρ² − 3ρ − 2 = 0; ρ_L,crit = (3 + √33)/6 = 1.45743 | Eq. (7) | symbolic; 1.45743 | match |
| 8ξ² − ξ − 1 = 0; ξ* = (1 + √33)/16 = 0.42154; factor 1.039895 | Eq. (7), 2.2 | dF/dξ = (ξ − 1)(8ξ² − ξ − 1)/2; 0.42154; 1.03989535 | match |
| Falls to 10 % of its maximum at 0.9L₁ | 2.2 | 9.7 % | match |
| ρ_L = 2: \|N\| = 2.0 | 2.2 | −2.000000 | match |
| ∂μ/∂ρ_EI ∝ ρ_L(1 − ρ_L²); ∂μ/∂ρ_L numerator ρ_EI(3ρ_L² − 1) + 2ρ_L³; μ = 0.750, 1, 3 | 2.2, App. A | symbolic | match |
| ρ_L = 1.6: −0.78 (ρ_EI = 0.5), +0.33 (ρ_EI = 4), zero at 2.14 | 2.2 | −0.7829, +0.3314, 2.1440 | match |
| ρ_L = 1.45: 0.021 at mid-span; 0.233 at ξ = 0.266 | 2.2 | 0.0213; 0.2331 (ξ = 0.266 is the optimum) | match |
| Near-blind band 1.385 < ρ_L < 1.525 | 2.2, 7.1 | 1.385061 – 1.524695 | match |
| Blind rig 2500 mm and 3644 mm | 7.2 | 3643.6 mm | match |
| Table A.1 (nine values) | App. A | identical | match |
| C⁺ 1.50–2.00, C⁻ −0.125 to −4.00; 1.750 / −0.750; at 0.42L₁: 1.732 / −0.692, net 1.000 → 1.040 | App. A | identical | match |
| R_m = 4/7 | 2.4 | 4/7 | match |
| O_m = 2√44765/1279 = 0.331 | Eq. (15) | symbolic identity; 0.3308 | match |
| O_m decreases monotonically as the sensor moves away from the outer support | 2.4 | 0.399 (ξ = 0.05) → 0.063 (ξ = 0.95), strictly decreasing | match |
| Strain blind point at 0.75L | 2.1 | 3/4 | match |
| Span-to-depth 100; shear 8 × 10⁻⁴ of bending | 3.1 | 100; order-of-magnitude estimate 8.8 × 10⁻⁴ (simply supported, central load, web shear area) | consistent in order; the exact basis of 8 × 10⁻⁴ is not documented |

## 3. Laboratory (s02, s03; `logs/s02_*.log`, `logs/s03_*.log`)

| Manuscript | Location | Script | Status |
|---|---|---|---|
| I = 16 529.8 mm⁴; EI = 3.3060 × 10⁹ N mm²; C_m = 61.541 mm²/N; 40.64 N | 3.1 | 16 529.76; 3.30595 × 10⁹; 61.5407; 40.6428 | match |
| 66.99 N, 125.08 N | Table 4 | 66.9925, 125.0775 | match |
| Three-load order: rms 0.030 mm against 0.55 mm for the reverse spacing | 3.1 | 0.0298 / 0.5529 mm | match. files-v2 states the reverse order (250 then 500 mm); the SCHM order is the one that fits. The two-load order (not stated) fits with the 2145 g load leading (0.017 against 0.286 mm). |
| Records 5000/5250/5750 mm; 20/21/23 intervals | 3.1, 3.2 | identical | match |
| Table 3: 2501.19; 2488.68 (−0.500 %); 2501.85 (+0.027 %); 2513.43 (+0.49 %) | Table 3 | 2501.1871; 2488.6811 (−0.500 %); 2501.8541 (+0.027 %); 2513.4250 (+0.489 %) | match |
| Largest deviation 0.0125 mm, 0.43 %, 2.5 × resolution | 3.2 | 0.0126 mm, 0.44 %, 2.53 × | **mismatch, last digit (M4)** |
| Residuals predominantly positive | 3.2 | 15 of 18 interior points have measured − theory > 0 | match (raw sign) |
| Table 4: I_y 4168.15 / 7788.93; BPM 67.73 (+1.10 %) / 126.57 (+1.19 %); SLM 67.40 (+0.61 %) / 125.95 (+0.70 %) | Table 4 | 4168.1500 / 7788.9250; 67.7300 (+1.101 %) / 126.5655 (+1.190 %); 67.4002 (+0.609 %) / 125.9492 (+0.697 %) | match |
| BPM/SLM = 1.00489 for both = 2513.43/2501.19 | 3.3 | 1.00489, 1.00489, 1.00489 | match |
| Quadrature-corrected BPM +1.10 → +1.61 % | 3.3 | +1.61 % (three loads: +1.70 %) | match |
| Measured/analytical 1.010, 1.016, 1.017 | 3.3, 7.2 | 1.0099, 1.0161, 1.0170 | match |
| I_y = 62.229P, R² = 0.99998, +1.12 % | 3.3, Fig. 6 | 62.2289, R² 0.999981 (centred SST), +1.12 % | match. With the uncentred R² for regression through the origin, R² = 0.9999967. |
| Table 7 (nine entries) | 6.2 | identical | match |
| (1.2596 − 1.9893) mm⁻¹; 58 % of the BPM term, 42 % reduction | 6.1 | 1.2596, 1.9893; 0.579 | match |
| Quadrature bias −0.5000 % for all three configurations | 6.1 | −0.5000 % (analytical records) | match |
| Spacing 300 mm: −0.110 %; 375 mm: +0.249 %; residual 0.4–0.75 % | 6.1 | see M1 | **not reproduced** |
| Simpson "nearly exact"; 3/8 end panel for 21 and 23 intervals | 2.4, 3.2 | see M2 | **caveat** |
| Trapezoid converges as Δx² | 2.4 | bias × (n/10)² constant (−0.500, −0.125, −0.020 …) | match |
| Reference integral 60 % of the two-load one | 6.3 | 0.603 | match |

## 4. Monte Carlo (s04; `logs/s04_monte_carlo.log`)

The model is Eq. (16) applied to the measured records. Gain and offset are drawn once per crossing and noise per sample; 200 000 realisations; seed 20260817; the same random stream as files-v2 `03_monte_carlo.py`.

| Manuscript | Script | Status |
|---|---|---|
| Table B.1, all 12 rows × 4 columns (bias, std. dev., p5, p95) | identical to 0.01 in all 48 entries | match |
| Three-load case within 0.1 pp | see M3 | **mismatch** |
| Random noise sd 0.07 % | 0.07 % | match |
| SLM sd 2.11 % (averaged) → 3.09 % (single); factor 1.47; BPM 2.12 % | 2.11, 3.09, 1.466, 2.12 | match |

files-v2 `03_monte_carlo.py` (run unchanged) already implements the gain + offset + noise model of Eq. (16). It printed MAE rather than the standard deviation, but its percentiles equal Table B.1. Its extra "legacy 5 % multiplicative" scenario is not in the manuscript; `s04` keeps it, labelled, only so that the random stream (and hence the Section 6.3 re-draw) is unchanged.

## 5. Moving force (s05; `logs/s05_moving_force.log`, `logs/s05_sweep47.csv`, `logs/s05_sweep_dense.csv`)

Model: Euler–Bernoulli, 40 Hermite elements per span, consistent mass m = 7850 × 186.52 × 10⁻⁶ = 1.464 kg/m, Rayleigh damping 2 % at modes 1 and 3, Newmark average acceleration, 4000 steps per crossing, constant force applied through the Hermite shape functions of the current element, window from entry to exit (T_cr = 2l/v), E = v∫y dt/(C_mP) − 1. The manuscript states all of this except the mesh, the step count and the speed spacing (taken log-uniform).

| Manuscript | Script | Status |
|---|---|---|
| 1.464 kg/m | 1.46415 kg/m | match |
| f₁ = 11.942 Hz, agrees with the analytical value (π/l)²√(EI/m)/2π to four figures | FE 11.9425 Hz = analytical 11.9425 Hz (with A rounded to 186.5 mm²: 11.9430 Hz) | match. The unrounded tube area (186.52 mm²) reproduces 11.942; this is the section's real value, not a fitted one. |
| Refining from 1000 to 16 000 steps changes the error by 0.002 pp | 0.0021 pp at T_cr/T₁ = 3; ≤ 0.0013 pp at 1.5, 8, 30, 120 | match |
| 47 speeds, T_cr/T₁ 0.6–120 | 47 log-spaced speeds | reproduced (spacing assumed) |
| Table 9: 17.6 / 8.6 / 3.8 / 1.7 / 1.00 / 0.32 / 0.15 / 0.08 | 47 pts: 17.64 / 7.55 / 3.04 / 1.29 / 0.99 / 0.51 / 0.18 / 0.11; dense: 17.64 / 8.64 / 4.09 / 1.77 / 0.99 / 0.59 / 0.23 / 0.13 | **partial (M5)**: ≥ 2 and ≥ 8 match |
| Eq. (21): ≥ 8 ⇒ ≲ 1 %; ≥ 4 ⇒ < 4 % | 0.99 %; 4.09–4.12 % | first part matches; **second marginally fails (M6)** |
| Abstract and Section 8: "about 1 % at a crossing time of eight fundamental periods" | max \|E\| for T_cr/T₁ ≥ 8: 0.99 % (at 8.5); E(8.0) = −0.47 % | match |
| Error exceeds 15 % and changes sign below ≈ 2.5 | \|E\| > 15 % up to T_cr/T₁ = 2.52; sign changes at 1.06, 1.97, 2.04 | match |
| Truncation: 39 % of the static peak at exit (T_cr/T₁ = 1.5) | 34.5 % | **mismatch (M7)** |
| Extending the window by 4T₁ roughly halves the error | factor 0.72–0.80 | **mismatch (M8)** |
| Damping 0.5–5 %: monotonic; less damping, less error | see M9 | mostly consistent |
| Multi-axle spread 0.33 % at 11.9, 1.95 % at 3.0 | 0.23 % / 2.31 % (assumed configurations) | same order (M10) |
| 10–30 m spans at 50–80 km/h give T_cr/T₁ of 7 to 20 | not computed: "plausible frequencies" from the old Table 10, no model | not reproducible by design (orientation only) |

## 6. Three-span theory and Cầu Mây (code/analysis; `logs/analysis/`)

`cm_multispan.py`, `cm_3span_theory.py`, `verify_3span.py`, `wp3_run.py`, `wp4_dynamic_records.py` and `wp7b_peps.py` were re-run in a clean copy of the repository. Their output is identical to the committed logs. Spot checks against the manuscript:

| Manuscript | Log value | Status |
|---|---|---|
| β_crit = 1.700594; 2cos(π/9) = 1.879385; 1.621399 (30β³ − 69β − 16); 0.964706 | 1.700593981702; 1.879385241572; 1.62139880522; 0.964705646960 | match |
| μ = 4/5 and 1.3 times the two-span value; Table 2 (six rows); FE slope ≤ 3.6 × 10⁻⁷ | identical; max \|slope\| 3.6 × 10⁻⁷ | match |
| 60 comparisons, max 7.5 × 10⁻¹²; asymmetric ≤ 9.2 × 10⁻¹² | 7.5 × 10⁻¹²; 9.2 × 10⁻¹² | match |
| Blind L₁/L₂ 0.589774 … 0.461410 | identical | match |
| 0.163, 0.921, 1.870395 / 0.195395 / −1.902566, 0.754630, 0.30 | 0.163223, 0.92099, identical, 0.30059 | match |
| Near-blind edge 1.775; β = 2: 0.875 | 1.775021; −0.875 | match |
| Calibration A: k_FE 2.7 × 10⁷ (2.5–3.6 × 10⁷), misfit −4.2/+3.7 %; α = 1.088 (−4.6/+5.0 %); calibration B α = 0.716, k = 1.2 × 10⁸ (−2.8/+2.9 %) | identical (wp3_run.log l. 1–3) | match |
| Polygon check −0.3/−0.5 % (A), −5.8/−2.6 % (I); 1.1 × 10⁻⁴ | 7.215/7.233, 14.360/14.437, 5.164/5.482, 58.085/59.612; 1.07 × 10⁻⁴ | match |
| Table 8 (C_m, P_ε, bias) | identical (wp7b_peps Part A; 11.3 % printed as 11 %) | match |
| k sensitivity 0.124/0.248, 0.191/0.224, +0.51/−0.12; α = 1.088: 0.160, 83 % | identical (Part B) | match |
| Table 10 combined 0.4–1.0 / 2.3–10.5 / 5.6–18.5 % | 0.44–1.01 / 2.30–10.54 / 5.58–18.52 % | match |

Tables 5 and 6 and the Section 5 values are traced to these logs and CSVs in `manuscript/schm/traceability.md`; that file was not re-audited line by line here.

## 7. files-v2 output mapped to the SCHM manuscript (`logs/files-v2/`)

| files-v2 item | SCHM item | Status |
|---|---|---|
| 01: reactions, Eq. (6) branches, 64EI, C_m | Eq. (A.1), (A.2), C_m | match |
| 02 "Table 2" | Table 3 | match (prints 2513.42; see the rounding note) |
| 02 "Table 4" | Table 4 | match (prints 7788.92) |
| 02 quadrature-corrected BPM | Section 3.3 | match |
| 02 calibration line | Fig. 6 | match |
| 02 "Table 5" zero offset | Table 7 | match |
| 03 Monte Carlo | Table B.1, Section 6.3 | match. Same model; the standard deviation is added in `s04`. |
| 04 Maxwell–Betti ratio 1.00000002 | Table 1 (FE to 11 figures) | files-v2 integrates with Simpson on the nodal values (2 × 10⁻⁸). The exact Hermite integral in `s01` gives about 10⁻¹¹. |
| 04 span ratio, critical 1.4574, sensor position, optimum 0.42 (+4.0 %) | Table A.1, Eq. (7), Table 1 | match |
| 05 figures (11 PNG) | old draft figure set (not the SCHM figures) | ran; photograph panel skipped |
| 06 equation images | none | fails: `pdflatex` not installed |
| (none) | Section 6.5 moving force | **absent from files-v2**; rebuilt in `s05` |
| beam_theory "spacings 250 and 500 mm" for the three-load group | Section 3.1 order 500 then 250 | files-v2 wording is wrong; corrected in `s0x` (integrals unaffected) |
