# Associate Editor assessment: field monitoring, measurement uncertainty, data quality, statistics, reproducibility

**Manuscript:** "Blind loci and design criteria for integral load-monitoring channels on continuous girder bridges, with laboratory verification and an assessment on public field records" (SCHM submission, v4)

**Material assessed:** `manuscript/v4/manuscript.md`, `supplementary_material.md`, `cover_letter_SCHM.md`, the figures in `manuscript/v4/figures/`, and the script package `code/{supplementary,analysis,theory2,norbwim,v4}` with its logs. Data: `data/bridges/`, and the public NOR-BWIM raw files under `data/public/` (git-ignored, but present on disk, so the field pipeline could be rebuilt from the raw files).

---

## 1. Decision

**Send to reviewers. Expected outcome: major revision.** There is a real risk of rejection if the reviewers judge the field part insufficient for the claims in the title.

The theory (closed-form blind loci, the indicators, the Möbius law) is verified computationally to round-off. The computational package is unusually good: every v4 script I ran regenerated its committed log byte for byte, and that includes the full NOR-BWIM pipeline rebuilt from the raw public files with the cache deleted. The authors also report their negative field results honestly. That transparency, and the fact that the main contribution is a set of design criteria rather than a field claim, are why I am not returning the paper. My concerns are about the evidence. None of the three empirical parts tests the paper's central claims:

- No experiment has a gauge at or near a blind locus.
- No deflection channel was measured under moving load.
- No zero-sum pair was measured.
- The public records have reference weights within 3.4 % of each other (25.9 and 26.8 t), so the mean weight beats every estimator.

The laboratory test is static, has two configurations and no stated uncertainty. The Cầu Mây analysis rests on two static numbers fitted with two parameters. Several measurement-uncertainty statements are wrong or unquantified:

- The Cầu Mây scatter called a "standard deviation" is a standard error of the mean.
- The speed used to convert time integrals to space integrals has an unreported 14 % systematic disagreement between two estimators, with a 12 % spread.
- The lane-B constants use a different speed method from lane A.

The package also omits the scripts behind Tables 6 and 7. All of this can be fixed without new data, except the absence of a direct field test of the criteria. The authors must either supply that test (the Cầu Mây moving-load test they have already designed) or narrow the title, abstract and cover letter to "theory with a feasibility check". The reviewers should be told explicitly to judge this point.

## 2. Scores (1–10)

| Criterion | Score | One-line justification |
|---|---|---|
| Strength of field evidence | 3 | One public dataset: n = 7–8 runs per day, 4 trucks, nearly constant weights, peak strains of only 1.5–4 µε. Two static readings at Cầu Mây. No field test of a blind locus, a deflection channel or a zero-sum pair. |
| Statistical treatment | 6 | CIs, TOST, out-of-sample validation and paired bootstrap are reported, which is good. But n = 7–8 percentile bootstrap, no multiplicity control over 12 gauges, a post-hoc "best gauge" in the main table, and χ² non-rejection read as consistency. |
| Uncertainty / error budget | 4 | Table 8 is explicitly not a budget. δ₀ is assumed, never measured. Speed uncertainty is not propagated. Lab BPM deviations are given without an uncertainty on EI. The Cầu Mây σ is mislabelled and built heuristically. |
| Reproducibility | 8 | Every script run reproduced its committed logs, CSVs and NPZ files exactly (apart from timing, path and label lines), including the field pipeline rebuilt from the raw files. Deducted for: Tables 6 and 7 and the §4.2 beam numbers come from scripts outside the package; `run_all.sh` does not drive the v4 analyses; README pointers to `docs/` and legacy numbering. |
| Data availability | 6 | NOR-BWIM is public (CC0). The lab means are tabulated, but the raw cycles do not exist. The Cầu Mây readings, trucks and frequencies are tabulated, but the truck positions are "given as drawings … not tabulated", so the static model cannot be rebuilt from the published data. |

## 3. Reproducibility report

### 3.1 What I ran

Everything ran in a scratch copy (`/tmp/claude-0/-home-user-SHM-Paper1-1D/e0d84659-e833-593b-82ad-e0ad845000cf/scratchpad/ed4/`), with `data/public` linked read-only. Environment: Python 3.13.16, NumPy 2.5.3, SciPy 1.18.1, SymPy 1.14.0, matplotlib 3.11.2, pandas 3.0.5, the same as the stated test environment. No repository file was modified.

| Run | Time | Result |
|---|---|---|
| `bash code/supplementary/run_all.sh --with-analysis` (beam_theory, s01–s05, cm_multispan, cm_3span_theory, verify_3span, wp3_run, wp4_dynamic_records, wp7b_peps) | 4 min 26 s | Every log is identical to the committed one, except: the `s05` run-time line (99 s → 131 s); one absolute figure path in `cm_3span_theory.log`; a trailing blank line in two logs. `s05_sweep47.csv` and `s05_sweep_dense.csv` are identical. |
| `code/norbwim`: `nb_field.py` → `nb_v4.py` → `nb_tests.py` → `nb_fe_veb.py`, after **deleting `cache/*.pkl`** so that everything was rebuilt from the raw figshare files (`DataWed.csv`, `Strains200Hz.dat`, `B.csv`, `AllStrainData…dat`) | 8.5 min | `field.log`, `v4.log`, `tests.log`, `fe_veb.log` and all 26 CSVs in `results/` are **byte-identical** to the committed versions. |
| `code/theory2`: `gc_results`, `verify_general`, `multisensor_theory`, `multisensor_placement`, `ident_theory`, `ident_static`, `ident_freq`, `ident_fisher` | ~6 min | All logs and `ident_static_scan.npz` are identical. One exception: `multisensor_placement.log` differs only in labels ("Cau May" against "Cầu Mây") and an absolute path in a warning. The script was evidently edited after the log was committed; all numbers are unchanged. |
| `code/theory2/multisensor_mc.py` (10⁵ realisations × 7 cases) | 13 min | Identical apart from run-time and label lines (§3.4). |
| Not run | – | `code/v4/*.py` (figure and numerical-difference helpers); `gc_figures.py`, `multisensor_figures.py`, `nb_fig1.py`, `schm_figures.py` (figures only). |

**Scripts outside the submitted package.** Several numbers come from scripts that are not in the submitted package (`supplementary/`, `analysis/`, `theory2/`, `norbwim/`, `v4/`):

- Table 7, the §4.2 span shares and r², and Table S3 notes: `code/v3/v3_numbers.py` and its log.
- Table 6: `code/fieldplan/fieldplan_compute.py`. Its log and labels are in Vietnamese.

I traced these numbers in the repository (below), but a referee given only the package could not. The package README also points to `docs/pkg1/...` and to `manuscript/v4/traceability.md`, and its second half describes "SCHM-v2" equation and table numbers. The Supplementary Material (S1) says `run_all.sh` "reruns … the identifiability analysis …, the processing of the public field records". It does not: `run_all.sh` runs only `s01`–`s05` and the legacy `code/analysis` scripts. The v4 `theory2` and `norbwim` analyses have to be started by hand, one folder at a time.

### 3.2 Traced numbers (35)

"Match" means equal after rounding to the printed digits.

| # | Manuscript value (location) | Source | Source value | Status |
|---|---|---|---|---|
| 1 | $C_m$ = 61.54 mm²/N (§3) | `supplementary/logs/beam_theory.log` | 61.5407 | match |
| 2 | Single-load IL residual 0.0126 mm, 0.44 % (§3) | `s03_load_identification.log` | 0.0126 mm, 0.44 % | match |
| 3 | Trapezoid underestimates by 0.500 % (§3) | `s02_quadrature_table3.log` | −0.5000 % | match |
| 4 | Table 2: BPM 67.73 (+1.10 %), SLM 67.40 (+0.61 %); 126.57 (+1.19 %), 125.95 (+0.70 %) | `s03` | 67.7300 / +1.101; 67.4002 / +0.609; 126.5655 / +1.190; 125.9492 / +0.697 | match |
| 5 | BPM/SLM = 1.0049; ratios 1.010 / 1.016 / 1.017 (§3) | `s03` | 1.00489; 1.0099 / 1.0161 / 1.0170 | match |
| 6 | Three-load order: rms 0.030 against 0.55 mm (§3) | `s03` | 0.0298 / 0.5529 | match |
| 7 | 981 FE checks, max 8.1 × 10⁻¹¹; convoy 2.8 × 10⁻⁹; force method 5.4 × 10⁻¹⁰ (App. B) | `theory2/logs/verify_general.log` | 981, 0 failures; 8.1e-11; 2.8e-09; 5.4e-10 | match |
| 8 | Truncation changes rotation integral by up to 59 % (§2.1, App. B) | `verify_general.log` l. 888 | 59.40 % | match |
| 9 | Main-span strain zero 0.276 at β = 1 (Table 1) | `verify_general.log` l. 840 | 0.276393 | match |
| 10 | Prismatic side-span indicator 0.287 (pinned) → 1.037 (fixed); main 0.755 → 0.500 (§2.5) | `ident_theory.log` | 0.2870 / 1.0368; 0.754630 / 0.500 | match |
| 11 | Day 1: 8 of 12 gauges pass χ²; CV 5.8–13.5 %, p = 0.13–0.71 (§4.2, S3) | `norbwim/logs/v4.log` Task 1 | ch3–7, 10–12 p = 0.130–0.708; CV 5.8–13.5 | match |
| 12 | ch11 ratio 0.996 (0.874–1.136), 90 % CI 0.904–1.098 (Table S3) | `v4.log` | identical | match |
| 13 | Non-spike gauges 22–26 % lower (ratios 0.740–0.783) | `v4.log` | ch8 0.740 … ch2 0.783 | match |
| 14 | Day-2 ratio 0.978 (0.697–1.374); equivalence only within ±26.7 %; day 1 ±11.8 % | `v4.log` | identical | match |
| 15 | Speed/truck correlation 0.98 on day 1 (§4.2) | `v4.log` Task 2 | 0.982 | match |
| 16 | Lane B/A 0.79 (0.59–1.00); st36 0.64 (0.47–0.81) | `v4.log` Task 5 | 0.794 (0.590–1.000); 0.640 (0.469–0.807) | match |
| 17 | Two-truck runs 0.92, pooled CI 0.77–1.06 | `v4.log` | 0.918 (0.772–1.064) | match (the log notes this CI is slightly too narrow; the paper does not) |
| 18 | Table 3, all 16 cells (MAE and bootstrap CI, LOO) | `v4.log` "day2 4ch LOO", "day1 12ch LOO" | identical (e.g. GLS 20.4 (12.3–28.8), average 11.9 (6.0–18.6), immune-eq 13.0 (7.1–19.0)) | match |
| 19 | Mean-weight MAE 2.0 % on day 2 | own recomputation from GVW 26.8/25.9 t, LOO | 1.92 % / 1.98 % | match |
| 20 | Paired GLS − average +8.5 pp (+2.3 to +15.1) | `v4.log` | +8.5 [+2.3, +15.1] | match |
| 21 | Residual correlation 0.63 against 0.90 (vehicle-free) | `v4.log` Task 4 / Task 3 | 0.630 against 0.895 (0.899 at T = 42 s) | match |
| 22 | Table S6 LOTO column (day 2) and day-1 wheel-path column | `v4.log` | identical | match |
| 23 | Table S5: GLS SD predicted from vehicle-free Σ 12.7 % | `v4.log` | 12.8 % in the diagnostic block; 12.7 in the "max pred.sd" column of the LOO table | minor inconsistency (two definitions) |
| 24 | GLS with residual Σ: "10.4 % in sample, 28.4 % out of sample" (S3) | `v4.log` | MAE 8.5 / 23.4; **RMS** 10.4 / 28.4 | **metric mislabelled**: these are RMS values, whereas Table 3 and Fig. 7 use MAE (Fig. 7 plots 23.4) |
| 25 | ch11/ch8 = 3.9; beam-model ratios 0.978–1.003; st36/st40 3.24 ± 0.56 against 1.82 ± 0.10 | `v4.log` C values; `results/test_f_*.csv` | 5.85/1.49 = 3.93; 0.978–1.003; 3.239 ± 0.559; 1.819 ± 0.096 | match |
| 26 | Moment zeros about 35 m from the gauges; span shares 170 / −26 / −66 %; r² 0.79–0.94 | `test_f_model.csv`; `code/v3/logs/v3_numbers.log` (outside the package) | zeros 121.6 / 190.8 m against gauge 158.5 m; 171.5 / −26.0 / −65.5; 0.791–0.940 | match |
| 27 | Cầu Mây means 5.55 / 15.42 mm; trucks mean 25.06 t | `data/bridges/cau-may/*.csv` | 5.553 / 15.425; 25.057 | match |
| 28 | Calibration A misfits +2.4 / +12.3 %; B −2.8 / +2.9 %, α = 0.716; r₈₇ min 1.058; variants 1.039–1.092 | `theory2/logs/ident_static.log` | identical; variant range 1.0391–1.0916 | match |
| 29 | "Six readings … standard deviation of 1.9–2.0 % about their mean" (§5.2) | `ident_static.log` l. 2 | "rel. **SEM** 1.90 % / 2.04 %"; sd 0.259 and 0.769 mm = **4.7 % and 5.0 %** | **mismatch in meaning** (SEM reported as SD) |
| 30 | σ = 2.64 %, τ = 5.3 %; κ ≥ 1.8 × 10⁷; α 0.51–1.15; N8 0.124–0.822; N7 0.190–0.286 | `ident_static.log` | 2.64; 5.27; 1.78e7; 0.513–1.153; 0.124–0.822; 0.190–0.286 | match |
| 31 | C₈ 3.0 × 10⁻⁵–2.0 × 10⁻⁴ (factor 6.6); C₇ 3.3–5.0 × 10⁻⁴ | `ident_static.log`; own extraction from `ident_static_scan.npz` | 3.00e-5–1.98e-4; C₇/α 3.28e-4–4.90e-4 | match |
| 32 | C∞/C₀ = 14.0 (N8), 0.59 (N7); k_g = 4.36 × 10⁷; κ/k_g = 0.63; B_m 0.51 / 0.12 | `ident_theory.log` | 13.991; 0.592; 4.3585e7; 0.630; 0.5115 / 0.1150 | match |
| 33 | CRB on ln C₈: 0.87 → 0.18 (tilt), 0.24 (frequencies), 0.04 at B; ratio 6.5 against 1.5 | `ident_fisher.log` | 0.865; 0.177; 0.237; 0.040; 6.49 / 1.509 | numbers match. **But** the 0.24 row is labelled "+f1+f3 (if f1 measured)", while the paper says "identified first and third vertical frequencies" and f1 was not measured (Table S10). |
| 34 | Table 7 (e.g. N7 16–25 % and N8 41–271 % at 0.1 mm) | `code/v3/logs/v3_numbers.log` (outside the package); my hand check, 0.1 mm × 200 m / (3.61 × 10⁻⁴ × 245.75 kN) = 22.5 % | 16.4–24.8; 41.1–271.3 | match |
| 35 | Table 6: integral ratio 0.121 / 0.284; rotation −58 / −29 µrad; strain ratio 0.006 / 0.17 | `code/fieldplan/results/fieldplan_compute.log` (outside the package) | 0.121 / 0.284; −58.1 / −29.0; 2.35/381.32 = 0.0062, 81.59/477.96 = 0.171 | match |
| 36 | §5.3: σ_P 24.8 % (N7) → 10.6 % (pair) at ρ = 0.9 | `theory2/logs/multisensor_placement.log` l. 62–64 | 24.8 %; immune pair 10.6 % | match |
| 37 | Day-2 speed slope +6 % per 10 m/s (−23 to +35) | `v4.log` Task 2 | +6.3 [−22.7, +35.4] | match |

**Summary:** 37 items, covering more than 100 individual numbers. Every number agrees with its log after rounding. There are three problems of labelling or meaning: #24 (RMS presented next to MAE), #29 (SEM called SD) and #33 (f1 described as identified although it was not measured). There is one rounding inconsistency (#23). Items #26, #34 and #35 can only be traced through scripts that are not in the submitted package.

### 3.3 Observations from the logs that the manuscript does not report

- **Speed.** `norbwim/logs/field.log` reports "low-pass fit speed / spike speed (lane A, n = 22): median 1.139, sd 0.124". The space integral is the time integral times the speed measured at the gauges. A 14 % systematic and 12 % random disagreement between two speed estimators is therefore of the same order as every effect the paper tries to resolve. The manuscript mentions only the 1–2 % agreement with the dataset authors' script, which uses the same axle spikes.
- **Lane B speed method.** All lane-B speeds come from "gauge lag" (`events_field.csv`, column `v_src`), not from axle spikes. The lane ratio of 0.79 therefore mixes two speed estimators.
- **Day-2 noise model.** The vehicle-free noise over-predicts the crossing scatter: residual variance / quiet variance is 0.51–0.64 for three of the four gauges. The χ² p-values of 0.48–0.83 are then uninformative, because the noise model is inflated.

### 3.4 Monte Carlo script

I ran `multisensor_mc.py` in full (794 s). `multisensor_mc.log` is identical to the committed log apart from the run-time lines and the "Cau May"/"Cầu Mây" label. `mc_summary.csv`, `mc_errors.npz` and all other 13 files in `theory2/results/` are byte-identical. Checks against the paper: the std/theory ratios lie within 0.997–1.006, consistent with the "within 0.6 %" claim in §2.4.

One line deserves attention. The structure-aware GLS and immune estimators show a mean error of +0.0020 kN with **z = +16.75**. This is a statistically significant bias. It is small (5 % of their SD) but contradicts "unbiased" unless it is explained, for example as discretisation.

**Overall reproducibility:** every script in the v4 trail that I ran (beam_theory, s01–s05, six `code/analysis` scripts, nine `theory2` scripts, four `norbwim` scripts) regenerated its committed logs, CSVs and NPZ files exactly. The only differences are run-time lines, absolute paths, blank lines and one stale label. That includes the NOR-BWIM pipeline rebuilt from raw public files.

---

## 4. The five most serious problems, ranked

### 1. The empirical evidence does not test the paper's claims, and the title and cover letter oversell it

The criteria concern blind and near-blind loci, deflection channels, the placement rule and the zero-sum pair. The evidence offered:

- **Laboratory.** Static loading, equal spans, two configurations, no blind configuration.
- **NOR-BWIM.** The records include only strain gauges near mid-span 2, about 35 m from any zero.
  - The reference weights are 25.9 and 26.8 t (day 2) and driver-reported (day 1). The mean-weight predictor (2.0 %) beats every estimator.
  - The signal is small. Peak strains are about 1.5–4 µε (Fig. 5) on a 605 m integration path whose far-field contributions are ±0.3 µε. A baseline error of 0.05 µε over 605 m equals 30 µε m, which is 20–50 % of the integrals in the Fig. 5 legend.
  - Run-to-run spread for one truck is large (st40: −21.6 against −50.5 µε m in R15 and R16, `events_field.csv`).
- **Cầu Mây.** Two static numbers and no moving load.

The "assessment on public field records" is therefore a study of a noisy dataset that cannot discriminate weights. It is not a verification of the criteria.

**Fix: needs new data.** Run the moving-load test already designed for Cầu Mây (Table 6), with:

- at least two clearly different vehicle weights (for example 15 t and 30 t);
- repeated runs (n ≥ 10 per vehicle and lane);
- a deflection pair at the N7 position and at the predicted minimum;
- one strain gauge at or near a predicted zero-moment point;
- a pier tiltmeter.

Report whether the predicted ratios in Table 6 are observed. Without new data, retitle the paper and rewrite the abstract and cover letter as a theoretical contribution with a feasibility check on public records. Delete "verification" for the field part, and move most of §4 to the Supplementary Material.

### 2. Speed and integration-domain uncertainty are not quantified, and the lane comparison is confounded

The conversion $\int\varepsilon\,dx = v\int\varepsilon\,dt$ over a 605 m crossing uses one speed measured from axle spikes over about 6 m at a single station. The authors' own alternative estimator (low-pass fit to the global shape) differs by a median factor of 1.139 with SD 0.124 (`field.log`). Speed variation over the crossing is admitted to be unmeasured (§6). Lane-B speeds use a different method (gauge lag). Speed and truck are confounded on day 1 (r = 0.98).

**Fix: no new data needed.**

- Report both speed estimators and explain the 14 % offset (geometry or model error, or real acceleration).
- Propagate the speed uncertainty into every C, ratio and MAE, for example by recomputing Tables 3 and S2–S3 with the alternative speed, or by a Monte Carlo over speed.
- Repeat the lane comparison with the same speed method in both lanes; lane-A gauge-lag speeds are available.
- State in §4.2 that the lane ratio depends on the speed method.

### 3. The Cầu Mây uncertainty model is mislabelled and heuristic, and the data needed to reproduce it are incomplete

- **Mislabelled scatter.** §5.2 says the six readings "have a standard deviation of 1.9–2.0 % about their mean". The log shows that this is the relative standard error of the mean; the standard deviation is 4.7 % (N8) and 5.0 % (N7). The paper itself says the readings are not replicates, so this is spatial and transverse variability, not measurement uncertainty. Dial-gauge resolution, frame stability and temperature are not considered at all.
- **Heuristic model-form term.** The 1.75 % comes from the spread of six hand-picked variants divided by 2√2 (`ident_static.py` l. 143, comment "uniform-ish"). τ is then 2σ.
- **No degrees of freedom.** Two readings are fitted with two parameters (α, κ). The admissible set is bounded only from below, and the headline factor of 6.6 is a direct function of τ. Table S7 shows that at τ = 3 % the set excludes α = 1.
- **Frequencies.** The "identified first and third vertical frequencies" (§5.3) include an f1 that was never measured. The span-wise frequencies in Table S10 (3.43 / 3.64 / 3.63 Hz on a continuous girder, with the two symmetric side spans different) indicate local or measurement artefacts.
- **Missing inputs.** The truck positions are not tabulated (S8), so no reader can rebuild the static model.

**Fix: no new data needed.**

- Correct the wording.
- Give a proper uncertainty model with separate measurement, transverse and model-form components and justified distributions, or a Bayesian or profile-likelihood treatment with stated priors.
- Move the τ-dependence (Table S7) into the main text and state the conclusion as conditional on τ.
- Relabel the 0.24 bound as hypothetical ("if f1 were measured").
- Tabulate the longitudinal axle positions of every truck for both load cases.
- Explain how the dial-gauge frames were "fixed to the ground" at mid main span over the Kinh Môn River.
- Clarify "k fitted to the designer's FE output". The designer's MIDAS predictions in `data/bridges/cau-may/cau-may_main_static_deflection.csv` are 5.93 / 16.70 mm, whereas calibration A predicts 5.686 / 17.324 mm.

### 4. Inference on very small samples overstates what is shown

- Percentile bootstrap CIs over n = 7–8 test runs are too narrow. The mean-weight CI of 1.9–2.0 is degenerate.
- Table 3 reports a "best single gauge (chosen after the fact)" next to pre-specified estimators. This is selection on the test data.
- Twelve TOST tests are run without multiplicity control. The single "equivalent within ±10 %" gauge (ch11, TOST p = 0.048) is about what one false pass among 12 tests would produce at α = 0.05.
- χ² non-rejection is read as "stable within the noise". On day 2 the noise model over-predicts the scatter, so the test has no power.
- The uncertainty of the day-1 driver-reported weights (21.2–22.8 t) is not propagated, although it is of the order of the observed CV of 5.6 %.
- The pooled two-truck CI is known to be too narrow (log note), but the paper does not say so.
- The st36/st40 ratio comparison uses a mean of ratios whose denominator gauge has CV 34 %.

**Fix: no new data needed.**

- Use t-based or BCa intervals, or exact permutation intervals, and state their limits at n = 7–8.
- Remove the post-hoc best gauge from Table 3, or label it clearly as optimistic and add a nested selection inside the cross-validation.
- Apply a Holm correction across gauges, or report the gauge average only as the primary endpoint.
- Treat χ² results as diagnostics and report the residual-to-noise variance ratios.
- Propagate the reference-weight uncertainty.
- Use a ratio of means with delta-method SE or a log-scale analysis for gauge ratios.
- Pre-specify a primary endpoint (gauge average, LOO MAE) in the text.

### 5. The error budget is not a budget, and the reproducibility package is incomplete

**Error budget.** Table 8 lists terms, says they are "not combined", and fills several entries with "not evaluated":

- Gain and speed measurement are not evaluated.
- δ₀, the term that dominates the conclusion that single-point weighing is "marginal", is assumed (0.02–0.5 mm) rather than measured. The authors' own deflection records give only pre-to-post drift (0.23 mm), which they correctly say does not bound δ₀.
- Laboratory BPM deviations of +1.1–1.2 % are presented as verification without any uncertainty on EI. The sensitivity of I to wall thickness (2.03 mm nominal) and of E to the material alone is of order ±2–4 %. The BPM deviation is therefore within an unquantified uncertainty, and the raw cycle data needed to estimate repeatability do not exist.

**Package.**

- Tables 6 and 7 and the §4.2 beam numbers come from `code/v3` and `code/fieldplan`, which are not in the submitted package.
- `run_all.sh` does not run the v4 analyses, contrary to S1.
- The README references `docs/` and `traceability.md` and carries legacy SCHM-v2 numbering.
- The README figure numbers (S5–S6, S7–S9) disagree with the Supplementary captions (S6–S7, S8–S10).

**Fix.**

- Error budget, no new data needed: give a GUM-style combined standard uncertainty at least for the laboratory BPM and SLM (E, t, span, LVDT, weights) and for one field SLM case (noise, speed, reference weight, lane). Keep the scenario terms separate.
- δ₀: demonstrate a residual-offset estimate on the authors' own Gie Cục and Phương Độ records, for example from the mid-crossing baseline deviation after linear re-zeroing in vehicle-free windows of crossing length. Otherwise label every δ₀-based conclusion as conditional. A real δ₀ for long-span absolute deflection needs new data.
- Package, no new data needed: add `v3_numbers.py` and `fieldplan_compute.py` with English labels; make one driver run every v4 script in order (about 25 min); remove the `docs/` references and the legacy sections; align the figure numbers.

## 5. Minor points

1. The Supplementary GLS-resid errors "10.4 % in sample, 28.4 % out of sample" are RMS. Fig. 7 and Table 3 use MAE (8.5 / 23.4). Use one metric.
2. Table S5 gives 12.7 % and `v4.log` gives 12.8 % (two definitions of the predicted SD). Harmonise them.
3. In Table 8, "field per-crossing SD of the gauge average predicted 19.8 % (day 2), 5.3 % (day 1)": state that the day-1 value is predicted from vehicle-free noise. It coincides numerically with the day-1 MAE in Table 3, which invites confusion.
4. The committed `multisensor_placement.log` was produced before a label edit in the script. Regenerate it so that log and script agree.
5. The Fig. 5 records show free vibration of about 0.5 µε continuing after the integration window closes, 5 s after exit. Show the sensitivity of the integrals to the window extension (the authors' own moving-force study suggests a 20–28 % change of the dynamic error).
6. Abstract: "invariance … within margins of 10–27 %" should state that ±10 % holds for one of 12 gauges and ±27 % for the day-2 average.
7. Fig. 6a: add the ±10 % TOST interpretation to the caption, or plot the 90 % CIs that the test actually uses.
8. The Cầu Mây section properties (5.482 and 59.61 m⁴) come from load-rating output. The data inventory in `data/bridges/cau-may/INVENTORY.md` itself flags the vertical-bending axis as "[NEED VALUE, confirm]", and lists a larger on-pier value of 79.8 m⁴. Confirm the axis, and justify using the near-pier value in the $h^{2.943}$ fit.
9. §5.1 says "four trucks … six trucks", but Table S9 lists ten trucks without saying which stood where. Add the assignment.
10. Data Availability: state that the laboratory raw cycles were not retained, and that the acceptance-test report and design model are not shared.
11. The README says `nb_v4.py` takes "about 35 s"; it takes 45 s plus the 7.5 min `nb_field.py` cache build from raw files. Document the dependency on the git-ignored raw files and their checksums (MANIFEST).
12. "Speed effect … not resolved" (Table 8): give the equivalence bound that could be excluded, as is done for invariance.
13. The structure-aware estimators in `multisensor_mc.log` have a mean error with z = +16.75. Explain it, or qualify "unbiased".
14. The Supplementary says S1–S8 "follow items (i)–(xi)". The mapping is not one-to-one; list it explicitly.
