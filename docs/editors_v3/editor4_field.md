# Editor 4 (field monitoring lens): manuscript v3, SCHM

**Manuscript:** Load observability of continuous girder bridges: a general response-integral theorem, optimal offset-immune estimation and field verification
**Lens:** whether the measurement assumptions are realistic, how honestly the field data are treated, the uncertainty budget, reproducibility, and overclaiming
**Material read:** manuscript/v3/manuscript.md, cover_letter_SCHM.md, figures in manuscript/v3/figures/, and code/{supplementary, theory2, norbwim, v3}

## Decision: Major revision

The theory is sound. The NOR-BWIM processing is careful and reproducible. However, the field evidence is reported more selectively and more confidently than the code output supports. The paper's own multi-channel claim (offset immunity) could be tested on data the authors already hold, and it was not. In the Cầu Mây part, the headline conclusions depend on an uncertainty model and a tolerance that are not justified.

| Criterion | Score (1-10) |
|---|---|
| Evidence (field support for the claims) | 5 |
| Reproducibility | 7 |

## What I ran

- `code/norbwim/nb_field.py` takes about 5 minutes from the cached figshare pickles. It regenerates `results/events_field.csv` byte-identical.
- `code/norbwim/nb_tests.py` takes about 8 s. All result CSVs and `tests.log` are identical; only the PDF timestamps change.
- `code/v3/v3_numbers.py` reproduces Table 6 and the beam-model numbers of Section 4.3.
- I read the `theory2/logs/ident_static.log` and `ident_freq.log` logs against Sections 5.2–5.3. Every number I checked in Tables 3, 4 and 6 matches a log.
- I wrote my own script in the scratchpad (`cm.py`). It computes cross-channel correlations of the vehicle-free integral noise using the authors' functions (results in concern 1).
- All repository files that my runs touched were restored. Nothing was committed.

## Strongest points

1. The field pipeline is engineered with care:
   - axle speeds are cross-checked against the dataset script;
   - the integral noise comes from 80 vehicle-free windows of the same length on each channel and day;
   - exclusions are logged with their reasons;
   - the processing is deterministic and reruns exactly.
2. The negative results are reported honestly:
   - the reverse SLM direction gives 17.1 %;
   - day-2 single-reference errors are 17.8 %;
   - a beam model cannot predict the ratios between gauges;
   - the lane constant ratio is 0.81;
   - the laboratory three-load spacing is ambiguous.
3. The 5-axle versus 3-axle comparison on day 2 is the right test of the theorem, and it uses statically weighed trucks.
4. Section 5 reports admissible ranges instead of a point calibration, labels the frequency evidence as conditional, and marks Table 5 as predictions, not results.
5. The offset-equivalent load P_ε (Eq. 12) and Table 6 are practical. They tie the method's feasibility to the baseline stability the instrumentation can actually achieve.

## Ranked concerns

### 1. The offset-immune estimator is never tested on field data the authors already hold (Sections 2.4, 4.4, 6.2, 7; cover letter item 3)

Section 4.4 states that "whether the wander is common-mode was not tested." The four day-2 channels are simultaneous, so the test is cheap.

- **My result:** using the authors' own `noise_integrals` (80 windows, T = 50 s), the vehicle-free integral noise is strongly correlated between channels on day 2 (r = 0.83–0.96). On day 1 it is moderate (r up to 0.86 among ch3–ch7 and ch10–ch12, and about 0.1–0.4 for ch1, ch2, ch8 and ch9).
- **What this means:** the noise is correlated but has unequal amplitudes (sd 0.82–1.82 µε s), so equal-weight zero-sum differencing helps only partly. A GLS combination with the measured covariance Σ reduces the day-2 per-crossing error for a 25 t truck at 20 m/s to:
  - about 15.6 %, against 24.7 % for the gauge average and 19.9 % for the best single gauge;
  - the 15.6 % is in-sample and optimistic.
- **Fix:**
  - Report the noise correlation matrix and the estimated ρ.
  - Apply Eq. (13) with the empirical Σ (cross-validated or leave-one-out) and Eq. (14) to the day-2 crossings, and report the SLM error.
  - This would turn contribution 3 from a purely simulated claim into a field result. It also corrects the implicit equal-amplitude assumption in Eq. (14) and in the Cầu Mây values ρ = 0.9 and ρ = 1 (Section 5.4), which are assumed, not measured.

### 2. Selective reporting of day-1 channels in the invariance and speed tests (Section 4.2, Table 3, abstract)

The "four wheel-path gauges" are `AVG1 = ch4, ch5, ch12, ch11` in `nb_field.py`, chosen by axle-spike strength. In the same run (`logs/tests.log`), the other channels behave differently:

- ch1, ch2, ch8 and ch9 fail the χ² invariance test (p = 0.000–0.012).
- Truck T2 gives a constant 0.74–0.77 times that of truck T1 on those channels (both trucks are 3-axle).
- The same channels show a speed slope of −34 to −39 % per 10 m/s (about 4σ).
- On day 1, truck and speed are fully confounded: T1 ran at 10–13 m/s and T2 at 19–20 m/s.

Stating "No speed effect was resolved" from the four-gauge average is therefore incomplete.

**Fix:**
- Report all 12 channels in a supplementary table.
- State the channel-selection rule before presenting the results.
- Discuss the truck/speed confound on day 1.
- Offer a physical explanation for the failing channels, for example transverse wheel-path offset between trucks or local deck action.
- Temper the abstract and Conclusion 4 accordingly.

### 3. The field tests have low statistical power, and the wording overstates them (abstract, Section 4.2, Conclusion 4)

- **Ratio test:** the 5-axle/3-axle ratio of 0.999 ± 0.140 cannot exclude differences of about 25 %.
- **χ² test:** on day 2 the observed CV (14.4 %) is below the noise-expected CV (20.2 %). This suggests the noise is overestimated, which makes "scatter explained by noise" a weak test.
- **Cross-day agreement:** the day-2 standard error at the common gauge is 12 %, so the agreement across days says little.
- **Common gauge (st40) on its own:**
  - day-2 SLM MAE is 54 %;
  - cross-day SLM MAE is 24 %;
  - CV is 34 % (Fig. 7).
- **Lane B constants:** they themselves fail invariance (p = 0.016–0.027 for st36, st31 and the average). Yet they are used for C_B/C_A = 0.81 ± 0.09 and for the gauge ratios 1.82 ± 0.10 and 2.41 ± 0.10.

**Fix:**
- Add an equivalence or power statement, for example: "differences above X % excluded at 95 %."
- Report the single-gauge performance alongside the average.
- Flag that lane-B invariance fails.
- Replace "speed-independent" with "no speed effect resolved within ±12 % (2σ) over 10–20 m/s (day 1)."

### 4. Reference weights and the gauge metadata limit what the field data can show (Sections 4.1, 4.3; Table 7)

- **Day-1 weights:** they are driver-reported and vary per pass (21.17–22.86 t), with unknown accuracy. The headline "6.5–7.0 % MAE" is measured against these weights. The abstract should say so.
- **One gain for all channels:** `nb_io.GAIN = −521.2² × 10⁻³` is applied to all 12 day-1 channels. Yet Section 4.4 states that the gauge calibration factors are not published.
- **Gauge-factor argument:** the case against gauge-factor spread rests on the lane-A st36/st40 ratio of 3.2. Its sd across crossings is 1.58 (se 0.56), so the difference from the lane-B value of 1.8 is about 2.5σ. In addition, a ratio of noisy means is biased upward.
- **Gauge geometry is contradictory:**
  - "in line with the wheel path at about 2 m pitch" (longitudinal);
  - "Gauges a few metres apart at one cross-section" (Section 4.3, Table 3);
  - the code comment says "one per longitudinal station."
- **Fix:**
  - Resolve the geometry from [44,45,51] or state the uncertainty.
  - Give the "2.7 times" result with its uncertainty, and moderate "which a beam model cannot predict" to "which the 1D model does not reproduce."
  - Fill the Table 7 entry "[NEED VALUE]" for the laboratory weighing class.

### 5. Measurement assumptions and uncertainty at Cầu Mây (Sections 5.1–5.3, 6.2; Tables 4 and 6)

- **Instruments:** dial gauges on a 90 m span over a river need a fixed reference. State:
  - the actual instrument (precise levelling? a total station?) and its reference datum;
  - how temperature was corrected;
  - the load-hold time and creep;
  - the zero-reading procedure.
- **Standard error of the readings:** "Relative SE 1.9–2.0 %" is computed from 3 lines × 2 transverse cases (`ident_static.log`). These are systematic transverse variations, not replicates. The SE is therefore not a measurement uncertainty, and the 2σ tolerance τ = 5.27 % rests on it.
- **Sensitivity to τ:** `ident_static.log` shows that τ = 3 % gives κ between 1×10⁸ and 3×10⁸ with α = 0.64–0.80, which excludes the design rigidity. τ = 5.27 % gives "bounded only from below." So the abstract conclusion depends on τ.
  - **Fix:** show the admissible set against τ, or adopt a likelihood or Bayesian treatment with a stated error model.
- **Abstract figure:** "21–25 %" uses the joint set, which depends on the conditional mode-3 interpretation. The static set gives 16–25 % (v3_numbers: C₇ up to 4.95×10⁻⁴). Quote the static-set range or label the condition.
- **Frequencies:** the approach spans give the same 3.0–3.1 Hz, which suggests a non-modal origin. Report the measurement method, record length and spectra.

### 6. The residual-offset scale is not tied to any real sensor (Sections 6.2 and 7, Table 6)

- The quoted evidence, post-minus-pre level differences of up to 0.23 mm (Phuong Do, `wp4.log`), is exactly what pre/post linear re-zeroing removes. It is not ε₀.
- Eq. (12) assumes a constant residual offset. Real drift after linear detrending is curved, and the bias then depends on the window shape.
- **Fix:**
  - Estimate ε₀ as the residual after the paper's own baseline procedure, using vehicle-free records (as was done for NOR-BWIM).
  - Give typical ε₀ for named non-contact techniques (radar interferometry, camera, GNSS, total station) over a window of 12–20 s, with sources.
  - Treat linear and quadratic drift explicitly.

### 7. Speed over 605 m is assumed constant (Section 4.1; `nb_field.finalize`)

Each integral is computed as Idx = v·∫ε dt, with v measured at the gauge only. The window spans 30–60 s, and the trucks turn around near the bridge ends. Section 2.4 itself warns that time-uniform integration weights space by 1/v.

**Fix:** bound the effect of speed variation, for example from the strain-spike timing at gauges further apart, or from the GPS logs in [51]. Alternatively, include it in Table 7.

### 8. Reproducibility and data availability gaps

- **Cầu Mây data:** the processed data and repository DOI are "[NEED VALUE]" in both the manuscript and the cover letter. The conflict-of-interest entry (an author's team performed the test) is incomplete.
- **Stale README:** `code/supplementary/README.md` describes an earlier manuscript, with different equation and table numbers. It points to `code/analysis/`, which is not in the v3 package list. There is no README for `theory2/`, `norbwim/` or `v3/`, and no single driver script for the v3 numbers.
- **Data path:** the NOR-BWIM raw files are read from `data/public/...`, outside `code/`. The ~230 MB pickle cache is committed, which also hides whether the raw-parse path still works.
- **Log side effect:** `nb_field.py` truncates `logs/field.log` on import (`LOG = open(..., "w")` at module level). The committed `field.log` is incomplete: it stops mid-event list compared with a fresh run. Make it write only under `main()`.
- **Hard-coded constants:** `v3_numbers.py` copies the C values from logs by hand. Read them programmatically.
- **Raw laboratory records:** they are not available (means only), and the supplementary README says so.
- **Fix:** add a v3 README with one driver script mapping every table and figure to a script and log, deposit the package with a DOI, and fill all [NEED VALUE] entries.

### 9. Smaller points

- Section 4.1 says speeds "agree with the GPS speeds of the dataset authors." The comparison value `v_script` comes from the dataset's processing script, so confirm that it really is GPS.
- The day-1 SLM test is effectively truck-to-truck between two 3-axle vehicles, not across axle configurations. Say so.
- Fig. 6 shows post-exit deck vibration inside the integration window, and peak strains of only 1.5–4 µε against 0.1–0.3 µε of wander. State the SNR explicitly.
- Table 7 should state the GUM-style limitations once. Avoid presenting the 0.07 % laboratory noise figure next to field terms that are two orders of magnitude larger without comment.

## Note to authors (150 words)

The theory is elegant, and your NOR-BWIM processing reruns exactly. As a field paper, however, it needs a more even-handed account. First, the day-1 results use four of twelve channels. The other four channels fail invariance and show a strong apparent speed effect, which is confounded with truck identity. Report all twelve and explain the selection. Second, test your own offset-immune estimator. The four simultaneous day-2 channels have strongly correlated vehicle-free noise (r ≈ 0.83–0.96 in our rerun), and a GLS combination with the measured covariance could markedly reduce the 18–25 % day-2 errors. That would be the paper's most valuable field result. Third, state the power of the invariance tests, and qualify day-1 accuracy as relative to driver-reported weights. At Cầu Mây, specify the instruments and the reference datum, base the tolerance on a defensible error model, and show how sensitive the conclusions are to that tolerance. Finally, deposit the bridge data, fill every [NEED VALUE], and refresh the supplementary README for v3.
