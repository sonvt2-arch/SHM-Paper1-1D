# v4 NOR-BWIM re-analysis: all channels, equivalence tests, measured noise covariance, out-of-sample estimators

Date: 2026-10-18. Script: `code/norbwim/nb_v4.py` (run `python3 -I nb_v4.py`, about 35 s, deterministic). Log: `code/norbwim/logs/v4.log`. Results: `code/norbwim/results/v4_*.csv`. Figures: `code/norbwim/figures/v4_{invariance,speed,noise_corr,estimators}.png/.pdf`. Input: the existing crossing integrals (`results/events_field_qc.csv`, from `nb_field.py` + `nb_tests.py`) and the cached raw records, which are used for the noise windows. Every number below is copied from `v4.log`.

Responds to: Editor 2 concerns 2–3, Editor 3 concern 1, Editor 4 concerns 1–3 and 8 (log side effect), and summary items 2–3 of `docs/editors_v3/00_TONG_HOP_V3.md`.

**Bug fix.** `nb_field.py` no longer truncates `logs/field.log` when it is imported. The log file is now opened only under `if __name__ == "__main__"`, and `log()` writes only when a file is open. Results are unchanged: after a full rerun of `nb_field.py`, `events_field.csv` is identical (see the check at the end of this document).

**Reference weights.** Day 1 (2020-09-10, Trucks 1 and 2, both 3-axle): the GVWs are **driver-reported per pass** (Moghadam 2022, PhD dissertation, Virginia Tech, hdl:10919/111390, Table 2.4) and range from 21.17 to 22.86 t. Day 2 (2020-09-30, Truck 3 with 3 axles and 26.8 t; Truck 4 with 5 axles and 25.9 t): the GVWs are **static weigh-station weights** (same source, Table 2.1 and §2.2.3). Neither day can test whether the method discriminates weights. On both days a constant predictor (the mean GVW of the calibration runs) has an MAE of only about 2 % (see the table in §4).

Runs used (the exclusions are those of v3): day 1 R1–R4 (T1) and R7–R9 (T2); day 2 lane A R11–R14 (T3) and R15–R18 (T4); lane B R11r–R18r; two-truck runs M1 and M2.

---

## 1. Per-channel invariance (all channels)

The ratio CI comes from a Welch t-test on log|C| using the empirical scatter between runs. TOST concludes equivalence at margin m when the 90 % CI lies inside [1−m, 1+m]. χ² p uses the vehicle-free noise sd, as in v3. A channel is flagged FAIL if χ² p < 0.05 or if the 95 % CI excludes 1, pass if it is equivalent within 10 %, and weak otherwise.

**Table A. Per-channel constant and invariance.** C is in µε·m/t. The ratio is T2/T1 on day 1 and T4/T3 on day 2.

| Day / channel | n | C (95 % CI) | CV % (bootstrap 95 % CI) | CV expected from noise % | χ² p | Ratio (95 % CI) | p TOST ±5 % / ±10 % | Verdict |
|---|---|---|---|---|---|---|---|---|
| D1 ch1 | 7 | −2.07 (−2.43, −1.70) | 19.1 (8.1–23.1) | 7.8 | <0.001 | 0.752 (0.606–0.935) | 0.98 / 0.96 | **FAIL: trucks differ** |
| D1 ch2 | 7 | −1.91 (−2.21, −1.60) | 17.2 (7.7–21.7) | 9.6 | 0.002 | 0.783 (0.631–0.972) | 0.97 / 0.92 | **FAIL** |
| D1 ch3 | 7 | −2.92 (−3.15, −2.69) | 8.6 (4.0–10.9) | 8.2 | 0.389 | 0.929 (0.795–1.086) | 0.64 / 0.31 | inconclusive |
| D1 ch4 (= st40) | 7 | −2.19 (−2.47, −1.92) | 13.5 (5.6–17.8) | 11.1 | 0.157 | 0.861 (0.603–1.228) | 0.79 / 0.65 | inconclusive |
| D1 ch5 | 7 | −5.54 (−5.90, −5.18) | 7.0 (3.1–9.1) | 5.7 | 0.169 | 0.990 (0.858–1.142) | 0.25 / 0.07 | inconclusive |
| D1 ch6 | 7 | −4.42 (−4.75, −4.09) | 8.1 (3.7–10.3) | 7.5 | 0.334 | 0.978 (0.836–1.144) | 0.33 / 0.12 | inconclusive |
| D1 ch7 | 7 | −3.20 (−3.50, −2.89) | 10.4 (4.8–12.9) | 8.1 | 0.130 | 0.938 (0.765–1.150) | 0.56 / 0.31 | inconclusive |
| D1 ch8 | 7 | −1.49 (−1.73, −1.24) | 17.9 (8.8–21.3) | 11.0 | 0.012 | 0.740 (0.630–0.869) | 0.995 / 0.99 | **FAIL** |
| D1 ch9 | 7 | −2.38 (−2.77, −1.98) | 17.8 (7.1–20.6) | 8.6 | <0.001 | 0.776 (0.620–0.970) | 0.97 / 0.93 | **FAIL** |
| D1 ch10 | 7 | −4.24 (−4.48, −3.99) | 6.3 (3.0–7.5) | 8.0 | 0.708 | 0.994 (0.875–1.129) | 0.20 / 0.051 | inconclusive (borderline) |
| D1 ch11 | 7 | −5.85 (−6.17, −5.53) | 5.8 (2.4–7.7) | 6.8 | 0.595 | 0.996 (0.874–1.136) | 0.17 / **0.048** | equivalent within 10 % |
| D1 ch12 | 7 | −2.55 (−2.79, −2.30) | 10.3 (3.5–14.3) | 8.0 | 0.144 | 0.873 (0.704–1.081) | 0.85 / 0.66 | inconclusive |
| D1 avg (ch4, 5, 11, 12) | 7 | −4.03 (−4.24, −3.82) | 5.6 (2.7–6.7) | 6.1 | 0.532 | 0.955 (0.863–1.057) | 0.45 / 0.10 | inconclusive (±11.8 % excluded) |
| D2 st40 | 8 | −2.11 (−2.71, −1.51) | 34.0 (13.5–50.3) | 33.9 | 0.483 | 0.839 (0.378–1.864) | 0.65 / 0.59 | inconclusive |
| D2 st36 | 8 | −5.97 (−6.57, −5.38) | 12.0 (3.6–17.9) | 16.5 | 0.729 | 1.005 (0.735–1.375) | 0.35 / 0.22 | inconclusive |
| D2 st34 | 8 | −2.40 (−2.70, −2.09) | 15.2 (5.7–20.8) | 22.2 | 0.825 | 0.954 (0.676–1.345) | 0.49 / 0.33 | inconclusive |
| D2 st31 | 8 | −6.02 (−6.82, −5.21) | 16.0 (5.4–23.4) | 20.1 | 0.676 | 0.994 (0.666–1.484) | 0.38 / 0.25 | inconclusive |
| D2 avg | 8 | −4.12 (−4.62, −3.63) | 14.4 (5.1–20.2) | 20.2 | 0.793 | 0.978 (0.697–1.374) | 0.41 / 0.26 | inconclusive (±26.7 % excluded) |

The day-2 lane-B constants (return trips, with speeds from the gauge lag) fail χ² for st36 (p = 0.016), st31 (0.020) and avg (0.027). Their CVs are 31–40 %. See `v4_invariance.csv`.

The v3 day-2 ratio of 0.999 ± 0.140 was an inverse-variance weighted ratio with noise-based errors. The Welch estimate here is unweighted and uses the empirical scatter: 0.978 (95 % CI 0.697–1.374). Both say the same thing: the ratio is consistent with 1, but differences up to about 25 % cannot be excluded.

**Failing channels.** ch1, ch2, ch8 and ch9 are the four day-1 channels without axle spikes, so they are probably not under the wheel path. On them, T2 gives a constant 22–26 % lower than T1 (95 % CIs exclude 1), while their scatter within each truck is close to noise. Their crossing residuals also exceed the quiet-window noise variance by a factor of 2.9–5.1 (log, residual diagnostic). Plausible causes, none of which can be tested with these data:
- a different transverse wheel path of the two trucks: off-path gauges respond to slab and shear-lag action that depends on lateral position;
- an effect of speed, which is confounded with truck (§2);
- a gauge-specific local effect.

The data cannot separate these. We therefore report the channels and do not explain them away.

## 2. Speed

Day 1 has **complete confounding**. Truck and speed correlate at r = 0.982 (VIF 28.6). Only 3.5 % of the speed variance lies within trucks: T1 ran at 10.4–12.8 m/s and T2 at 19.1–19.8 m/s. So "the speed effect" on day 1 is equally a truck effect.

Day 2 is not confounded (r = −0.38, VIF 1.2; T3 ran at 16.8–28.1 m/s and T4 at 13.2–23.0 m/s).

Slopes are in % of C per 10 m/s, from OLS with 95 % CIs (`v4_speed.csv`):

| Set | Pooled C ~ v | C ~ truck + v |
|---|---|---|
| D1 avg | −4.3 (−18.6, +10.0) | +41.3 (−25.0, +107.6) |
| D1 ch11 | +0.5 (−15.4, +16.3) | +34.8 (−55.2, +124.8) |
| D1 ch1 / ch8 (failing) | −36.7 (−66.5, −6.9) / −38.1 (−59.3, −16.9) | −50.3 (−242, +142) / −43.7 (−180, +93) |
| D2 avg | +6.7 (−16.6, +30.1) | +6.3 (−22.7, +35.4) |
| D2 st36 | +5.6 (−13.8, +25.0) | +6.2 (−17.9, +30.3) |

No channel shows equivalence even at ±10 %/10 m/s. The manuscript must not say "speed-independent". Supported wording: "no speed effect was resolved; on day 2 (13–28 m/s, unconfounded) the gauge-average slope is +6 % per 10 m/s with a 95 % CI of −23 to +35 %."

## 3. Noise covariance of the integrated noise (vehicle-free windows)

Method: sliding windows (step 2 s) of crossing length on quiet record, at least 70 s from any detected vehicle, with the same pre/post 8 s linear baseline as the crossings. CIs come from a bootstrap over non-overlapping windows. These sds agree with the v3 random-window values (median ratio 0.985 on day 2 and 0.962 on day 1).

| | Day 2 (T = 42 s, 4 ch) | Day 1 (T = 58 s, 12 ch) |
|---|---|---|
| Windows (sliding / non-overlapping) | 1227 / 44 | 3405 / 90 |
| Pairwise r | 0.849–0.965, mean 0.899 | 0.077–0.739, mean 0.430 |
| Common-mode ρ (mean r, non-overlapping, 95 % CI) | 0.921 (0.832–0.961) | 0.424 (0.260–0.542) |
| λ₁/k | 0.925 | 0.495 (wheel-path subset 0.665) |
| Noise sd, µε·s | st40 0.916, st36 1.308, st34 0.691, st31 1.651 | 0.274 (ch8) to 0.582 (ch11) |
| Noise sd, µε·m at median speed | 18.2, 26.0, 13.7, 32.8 (19.9 m/s) | 3.5–7.4 (12.8 m/s) |

On day 2 the quiet-window noise is strongly common-mode, but the channel amplitudes are unequal (ratio 2.4 between st31 and st34). The equal-weight average therefore removes almost nothing: the sd of the channel mean is 1.102, against a mean channel sd of 1.141 (0.600 if the channels were independent). Correlation falls slowly as the window lengthens: from 0.912 at 32 s to 0.845 at 68 s.

## 4. Estimators: out-of-sample comparison

Protocol:
- C_j is the mean of I_j/GVW over the calibration runs only.
- Σ is the quiet-window covariance for the test run's window length, scaled by v². Σ never contains a crossing.
- LOO = leave one run out. LOTO = calibrate on one truck and test on the other (on day 2 this is the 3-axle ↔ 5-axle test). IN = in-sample.
- Errors are % of GVW. CIs are 95 % bootstrap CIs over the test runs, which are few (n = 8 and n = 7).
- Estimators: GLS = Σ⁻¹C/(CᵀΣ⁻¹C). Immune = minimum wᵀΣw subject to wᵀC = 1 and Σw = 0. Immune-eq is the same with Σ = I (the equal-amplitude form of manuscript Eq. 14). GLS-diag uses diag(Σ). GLS-resid takes Σ from the scatter of the calibration crossings.

**Table B. Estimator comparison, out-of-sample (LOO), with in-sample and leave-one-truck-out values.**

| Estimator | D2 LOO MAE (95 % CI) | D2 LOO RMS (95 % CI) | D2 IN RMS | D2 LOTO MAE | D2 sd predicted by Σ | D1 12-ch LOO MAE (95 % CI) | D1 wheel-path 4-ch LOO MAE (95 % CI) |
|---|---|---|---|---|---|---|---|
| Single best gauge (st36 / ch11)* | 8.4 (2.9–15.3) | 12.6 (4.9–19.0) | 11.2 | 7.6 | 16.2 | 4.8 (1.8–7.9) | 4.8 (1.8–7.9) |
| Single worst gauge (st40 / ch8) | 27.9 (12.9–44.5) | 36.2 (16.6–51.1) | 31.8 | 24.3 | 32.5 | 17.6 (11.0–23.4) | 12.1 (ch4) |
| Gauge average | 11.9 (6.0–18.6) | 15.1 (7.6–21.5) | 13.4 | 11.1 | 19.8 | 5.3 (2.5–7.8) | 5.4 (3.3–7.4) |
| GLS-diag | 11.4 (6.0–18.0) | 14.5 (7.3–20.8) | 12.9 | 10.8 | 19.4 | 5.3 (2.5–8.0) | 5.2 (3.3–7.1) |
| **GLS, measured Σ** | **20.4 (12.3–28.8)** | **23.6 (15.4–30.6)** | 21.0 | 17.7 | **12.7** | 5.8 (3.5–8.1) | 4.9 (3.0–6.9) |
| **Offset-immune, measured Σ** | **20.3 (12.4–28.6)** | 23.4 (15.2–30.6) | 20.9 | 18.0 | 13.3 | 6.0 (2.9–9.3) | 8.3 (3.9–13.4) |
| Offset-immune, Σ = I | 12.3 (6.1–20.2) | 15.9 (7.1–23.2) | 14.2 | 10.8 | 16.1 | 13.0 (7.1–19.0) | 8.4 (4.6–12.9) |
| GLS, Σ from crossing residuals | 23.4 (13.1–35.4) | 28.4 (15.7–39.3) | 10.4 | n/a | 10.6 | n/a | 5.5 (2.6–7.7) |
| Trivial: mean GVW of calibration runs | 2.0 (1.9–2.0) | 2.0 | 1.7 | 3.4 | – | 2.2 (1.1–3.5) | 2.2 (1.1–3.5) |

\*The best single gauge is chosen after the fact, so its row is optimistic. Day-1 LOTO MAEs: average 8.9 % (12 ch) and 5.5 % (wheel path), GLS 10.1 % and 4.6 %, immune 7.1 % and 9.8 %.

Paired bootstrap on day-2 LOO: GLS minus average gives ΔMAE = +8.5 points (95 % CI +2.3 to +15.1), and immune minus average gives +8.3 (+2.8 to +14.3). **GLS and the offset-immune estimator are significantly worse than the plain average on the field data.** On day 1 the estimators cannot be told apart: GLS minus average gives +0.5 (−2.9 to +3.5) with 12 channels and −0.5 (−1.9 to +1.1) with the wheel-path set. On day 1 every estimator is worse than the trivial mean-GVW predictor (GLS minus mean-GVW: +3.5, 95 % CI +1.3 to +6.2).

**Why GLS fails on day 2.** The quiet-window Σ predicts a per-crossing sd of 12.8 % for GLS and 19.8 % for the average. The crossing residuals reverse that order: evaluated with the covariance of the crossing residuals themselves, GLS gives 21.0 % and the average 14.6 %. The crossing residuals are much less correlated across gauges (mean r = 0.63; st40 against st36 and st34 only 0.30–0.37) than the quiet noise (0.895). The common-mode wander measured in quiet periods is real. But a crossing also carries a gauge-specific, event-specific component, such as the wheel path and local slab action. The large opposite-sign GLS and immune weights (+0.16 on st40, −0.35 on st36) amplify that component.

Editor 4's "~16 %" (15.6 %) was a noise-model prediction made with the quiet Σ, not an observed error. In our rerun that prediction is 12.7 % RMS, while the observed error is 21.0 % RMS in-sample and 23.6 % out-of-sample. Estimating Σ from the crossings instead overfits: 10.4 % in-sample against 28.4 % LOO.

## 5. Lane effect and two-truck superposition

**Lane** (day 2, same trucks), C_B/C_A with Welch 95 % CI (bootstrap CI in brackets):

| Channel | C_B/C_A (95 % CI) [bootstrap] |
|---|---|
| avg | 0.794 (0.590–1.000) [0.631–1.008], p = 0.050 |
| st36 | 0.640 (0.469–0.807) |
| st34 | 0.857 (0.654–1.070) |
| st31 | 0.842 (0.627–1.069) |
| st40 | 1.018 (0.684–1.536) |

Only st36 shows a lane effect that is clearly resolved.

**Superposition** (M1 and M2, T4 + T3 in line in lane A). Measured integral / sum of single-truck predictions; the CI combines the event noise and the SE of C:
- avg: 0.921 (0.719–1.123) and 0.915 (0.705–1.126); pooled 0.918 (0.772–1.064).
- GLS: 0.827 (0.705–0.950) and 0.809 (0.680–0.938); pooled 0.818 (0.729–0.907).
- The GLS total GVW is 43.6 t (−17.3 %) and 42.6 t (−19.1 %), against 52.7 t.

The gauge average is consistent with superposition but low in both events. The GLS CI, which carries noise only, excludes 1, in line with §4.

---

## 6. Draft text replacing the §4 results paragraphs (about 600 words)

Each day-1 gauge was treated as a separate sensor, and all twelve are reported (Table A). The reference weights differ in quality between the days. On day 1 the gross weights of the two 3-axle trucks were reported by the drivers for each pass (21.2–22.9 t; Moghadam 2022, Table 2.4). On day 2 a 3-axle truck (26.8 t) and a 5-axle truck (25.9 t) were weighed on a static scale. Because the weights vary by only a few per cent within each day, a constant predictor equal to the mean calibration weight would have a mean absolute error of 2.0–2.2 %. The field data therefore test the scatter of the integral constant, not the ability to discriminate weights.

On day 1, eight gauges have a constant whose scatter is consistent with the measured integral noise (CV 5.8–13.5 %, χ² p = 0.13–0.71). The two trucks agree within 10 % only for gauge ch11 (ratio 0.996, 90 % CI 0.904–1.098). For the other seven, and for the four-gauge average (0.955, 95 % CI 0.863–1.057), equivalence within ±10 % cannot be shown with seven runs. Four gauges without axle spikes (ch1, ch2, ch8, ch9) fail: their constant is 22–26 % lower for the second truck (95 % CIs exclude 1). This may reflect a different transverse wheel path, local deck action, or speed, because on day 1 truck and speed are almost perfectly confounded (r = 0.98; 10–13 versus 19–20 m/s). On day 2 the 5-axle/3-axle ratio of the gauge average is 0.98 (95 % CI 0.70–1.37). This is consistent with axle-configuration independence, but differences up to about 27 % cannot be excluded. No speed effect was resolved: on day 2, where speed and truck are not confounded, the slope is +6 % per 10 m/s (95 % CI −23 to +35 %). The constant cannot be called speed-independent.

To test the multi-channel estimators, the covariance of the integrated noise was measured from vehicle-free windows of crossing length. On day 2 the four channels are strongly common-mode (mean r = 0.92, 95 % CI 0.83–0.96), with unequal amplitudes (13.7–32.8 µε·m). On day 1 the correlation is moderate (mean r = 0.42, 95 % CI 0.26–0.54). Single-gauge, gauge-average, GLS (Eq. 13) and offset-immune (Eq. 14) estimators were then compared by leave-one-run-out cross-validation. The constants were calibrated without the test run, and Σ never contained a crossing (Table B). On day 2 the gauge average gave a mean absolute error of 11.9 % (95 % CI 6.0–18.6 %). GLS gave 20.4 % (12.3–28.8 %) and the offset-immune combination 20.3 %, both significantly worse than the average (paired difference +8.5 points, 95 % CI +2.3 to +15.1). This happened although the noise model predicted 12.7 % for GLS. The crossing residuals are much less correlated between gauges (mean r = 0.63) than the vehicle-free noise (0.90). Each crossing therefore carries a gauge-specific component, plausibly the wheel path and local slab action, which the opposite-sign GLS weights amplify. On day 1 the estimators are statistically indistinguishable (gauge average 5.3 %, GLS 5.8 %, best single gauge 4.8 %), and none beats the constant predictor. Calibrating on the 3-axle truck and testing on the 5-axle truck, and vice versa, gave 11.1 % for the average on day 2.

Return trips in the other lane gave constants 0.79 times those of the instrumented lane (95 % CI 0.59–1.00). The lane effect is resolved for one gauge only (st36: 0.64, 0.47–0.81). The two in-line two-truck runs gave 0.92 and 0.92 of the summed single-truck predictions (pooled 0.92, 95 % CI 0.77–1.06). That is consistent with superposition, but low in both events.

In short, the field data support linearity and per-gauge invariance at the 10–25 % level that the noise allows. They do not show any benefit from the GLS or offset-immune combination. The common-mode assumption behind Eq. (14) holds for vehicle-free noise but not for crossing-to-crossing errors.

---

## Verification of the nb_field.py fix

`python3 -I nb_field.py` was rerun in full after the change (exit 0). `results/events_field.csv` is byte-identical to the committed version: git reports no change. `logs/field.log` is now complete, with 88 lines against 32 in the committed file, which had been truncated by an import. The rerun only added lines. Importing `nb_field` from `nb_v4.py` no longer touches the log. Two consecutive runs of `nb_v4.py` give identical `v4.log` files.
