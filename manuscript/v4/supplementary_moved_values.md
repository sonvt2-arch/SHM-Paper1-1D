# Supplementary Material: field-record tables (NOR-BWIM)

These tables and notes were moved from Section 4 of the main text in the v4.4 readability pass. Values are unchanged; sources are `code/norbwim/logs/v4.log` and `code/norbwim/results/`.

**Table S1.** Integral constant $C$ and its scatter over the runs, lane A unless stated. CV expected: coefficient of variation predicted from the measured vehicle-free noise. For ch1, ch2, ch8 and ch9 the residual variance is 2.9–5.1 times the vehicle-free noise variance.

| Day, channel | Runs | $C$ (µε m/t), 95 % CI | CV observed (%) | CV expected (%) | χ² p |
|---|---|---|---|---|---|
| 1, ch11 (best) | 7 | −5.85 (−6.17, −5.53) | 5.8 | 6.8 | 0.60 |
| 1, gauge average (4 wheel-path gauges) | 7 | −4.03 (−4.24, −3.82) | 5.6 | 6.1 | 0.53 |
| 1, ch1, ch2, ch8, ch9 | 7 | −1.49 to −2.38 | 17.2–19.1 | 7.8–11.0 | ≤ 0.012 |
| 2, st36 | 8 | −5.97 (−6.57, −5.38) | 12.0 | 16.5 | 0.73 |
| 2, gauge average (4 gauges) | 8 | −4.12 (−4.62, −3.63) | 14.4 | 20.2 | 0.79 |
| 2, lane B, average | 8 | −3.27 (−4.19, −2.35) | 33.7 | 23.2 | 0.027 |

**Table S2.** Ratio of the integral constants of two trucks, lane A unless stated. Day 1: second to first truck, both 3-axle; day 2: 5-axle to 3-axle truck. Equivalence by two one-sided tests (TOST) at the 5 % level: the 90 % CI of the ratio lies inside the stated margin (for ch11, 0.904–1.098), so a 95 % CI can extend beyond a margin that is shown.

| Day, channel | Ratio (95 % CI) | Equivalence |
|---|---|---|
| 1, ch11 (best) | 0.996 (0.874–1.136) | shown within ±10 % |
| 1, gauge average (4 wheel-path gauges) | 0.955 (0.863–1.057) | shown only within ±11.8 % |
| 1, ch1, ch2, ch8, ch9 | 0.740–0.783 | invariance rejected (CIs exclude 1) |
| 2, st36 | 1.005 (0.735–1.375) | not shown |
| 2, gauge average (4 gauges) | 0.978 (0.697–1.374) | shown only within ±26.7 % |
| 2, lane B, average | 0.749 (0.440–1.276) | – (constants fail the χ² test, Table S1) |

**Table S3.** Correlation between gauges of the integrated strain: means over gauge pairs, with 95 % bootstrap CIs in brackets. Vehicle-free windows: 1227 on day 2 and 3405 on day 1. Crossing residual: deviation of a crossing's integral from its calibrated value. –: not computed.

| Correlation of | Day 2, 4 gauges | Day 1, 12 gauges |
|---|---|---|
| vehicle-free noise, non-overlapping windows | 0.92 (0.83–0.96) | 0.42 (0.26–0.54) |
| vehicle-free noise, window length of each crossing | 0.90 | – |
| crossing residuals | 0.63 | – |
| crossing residuals, st40 with its neighbours | 0.30–0.37 | – |

**Table S4.** Day 2: per-crossing standard deviation (SD) of the gross weight predicted by two covariance models, and the observed error (% of GVW). SD and MAE are different measures; the table compares the order of the two estimators, not magnitudes.

| Quantity | GLS, measured $\Sigma$ | Gauge average |
|---|---|---|
| SD predicted from the vehicle-free covariance | 12.7 | 19.8 |
| SD predicted from the covariance of the crossing residuals | 21.0 | 14.6 |
| Observed MAE, leave-one-run-out (main text Table 3) | 20.4 | 11.9 |

**Table S5.** Mean absolute error of the gross weight (% of GVW), out of sample, with 95 % bootstrap CIs over the test runs (n = 8 on day 2, n = 7 on day 1). LOTO: calibrated on one truck, tested on the other.

| Estimator | Day 2, leave-one-run-out | Day 2, LOTO | Day 1, 12 gauges | Day 1, 4 wheel-path gauges |
|---|---|---|---|---|
| Best single gauge (chosen after the fact) | 8.4 (2.9–15.3) | 7.6 | 4.8 (1.8–7.9) | 4.8 (1.8–7.9) |
| Worst single gauge | 27.9 (12.9–44.5) | 24.3 | 17.6 (11.0–23.4) | 12.1 |
| Gauge average | 11.9 (6.0–18.6) | 11.1 | 5.3 (2.5–7.8) | 5.4 (3.3–7.4) |
| GLS, diagonal $\Sigma$ | 11.4 (6.0–18.0) | 10.8 | 5.3 (2.5–8.0) | 5.2 (3.3–7.1) |
| GLS, measured $\Sigma$ | 20.4 (12.3–28.8) | 17.7 | 5.8 (3.5–8.1) | 4.9 (3.0–6.9) |
| Zero-sum, measured $\Sigma$ | 20.3 (12.4–28.6) | 18.0 | 6.0 (2.9–9.3) | 8.3 (3.9–13.4) |
| Zero-sum, $\Sigma$ = identity matrix | 12.3 (6.1–20.2) | 10.8 | 13.0 (7.1–19.0) | 8.4 (4.6–12.9) |
| Mean weight of the calibration runs | 2.0 (1.9–2.0) | 3.4 | 2.2 (1.1–3.5) | 2.2 (1.1–3.5) |

## Notes moved from the main text

- Bridge depth: about 3.8 m at mid-span and 9.5 m at the piers. Sampling: 100 Hz on day 1, 200 Hz on day 2.
- Day-1 driver-reported gross weights: 21.2–22.8 t for the runs used.
- Speeds were obtained from the axle spikes and the measured wheelbase and agree with the dataset authors' processing script within 1–2 %. Records were integrated over the whole time the truck was on the bridge plus 5 s at each end. Three day-1 runs with two trucks on the bridge and four passes without documented weights were excluded. Vehicle-free noise windows were at least 70 s from any detected vehicle.
- Day 1: eight of the twelve gauges have a coefficient of variation of 5.8–13.5 %, consistent with the noise (χ² p = 0.13–0.71). The first truck ran at 10.4–12.8 m/s and the second at 19.1–19.8 m/s. Day 2 speeds: 13–28 m/s; no speed effect resolved (+6 % per 10 m/s, 95 % CI −23 to +35 %).
- Day-2 noise amplitudes at the median speed: 13.7–32.8 µε m.
- GLS weights with the measured Σ: st40 +0.16, st36 −0.35. GLS with Σ estimated from the crossing residuals: error 10.4 % of GVW in sample, 28.4 % out of sample.
- Lane B: st36 ratio 0.64 (95 % CI 0.47–0.81). Two-truck runs: 0.92 and 0.92 of the summed single-truck predictions (pooled 95 % CI 0.77–1.06); GLS combination 0.82 (95 % CI 0.73–0.91).
- Gauges: a one-dimensional beam model predicts ch11/ch8 ratios of 0.978–1.003. Ratio of st36 to st40 constants: 3.24 ± 0.56 in lane A against 1.82 ± 0.10 in lane B (± one standard error), about 2.5 standard errors apart.
- Beam model (Euler–Bernoulli, parabolic haunch, second moment proportional to h²): r² = 0.79–0.94 against the strain histories; zeros of the uniform-load moment in span 2 at 121.6 m and 190.8 m; strain constant of the gauges 0.69 of the largest on the girder (0.56–0.93 across stiffness laws); cancellation ratio R = 0.51; span 2 contributes about 170 % of the net integral and the adjacent spans −26 % and −66 %.

## Values moved from Sections 2 and 5 (v4.2–v4.3 passes)

- Section 2.2: the closed forms agree with FE in 981 checks (max error 8.1 × 10⁻¹¹; now in Appendix B). Prismatic main-span strain blind point ζ₀ = 0.177 at β = 1.636 (now in Appendix A).
- Section 2.4: placement verified by a brute-force search over 96 cases and a Monte Carlo study with 10⁵ random axle configurations per case; white-noise to offset ratio σ²Δx/(δ₀²L_tot) ≈ 5 × 10⁻⁶ at σ = 0.01 mm, δ₀ = 0.1 mm, Δx = 0.1 m, L_tot = 220 m.
- Day-2 per-crossing SD predicted by the vehicle-free covariance (% of GVW): best single gauge 16.2, worst single gauge 32.5, gauge average 19.8, GLS diagonal Σ 19.4, GLS measured Σ 12.7, zero-sum measured Σ 13.3, zero-sum Σ = identity 16.1.
- Lane B, failing channels: CV 31–40 %, χ² p = 0.016–0.027.
- Cầu Mây design sections: depth 2.40 m (mid-span) to 5.40 m (piers), second moments 5.482 m⁴ and 59.61 m⁴, E_c = 36 057 MPa. Model-form variants: L_v = 40 and 45 m (base 44 m), exponents 2.5 and 3.2 (base 2.943), rigid pier zone ±1.5 m.
- Misfit ratio r₈₇: 1.126 at κ = 10⁷ kN m/rad, minimum 1.058 at κ = 1.68 × 10⁸ kN m/rad (calibration B), 1.091 for fixed piers.
- Admissible set against tolerance τ:

| Tolerance, prior | κ (kN m/rad) | α | N8 indicator, αEI_mid | N8 indicator, design EI_mid | C₈ (m²/kN) |
|---|---|---|---|---|---|
| τ = 3 % | 1.0–3.0 × 10⁸ | 0.64–0.80 | – | – | – |
| τ = 4 % | 4.2 × 10⁷–2.0 × 10⁹ | 0.54–0.98 | – | – | – |
| τ = 5.3 % | ≥ 1.8 × 10⁷ | 0.51–1.15 | 0.14–0.42 | 0.12–0.82 | 3.0 × 10⁻⁵–2.0 × 10⁻⁴ |
| τ = 5.3 %, prior α ∈ [0.9, 1.3] | – | – | 0.14–0.27 | 0.12–0.30 | – |
