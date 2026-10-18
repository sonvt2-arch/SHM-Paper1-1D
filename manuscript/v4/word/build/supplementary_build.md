# Supplementary Material

**Blind loci and design criteria for integral load-monitoring channels on continuous girder bridges, with laboratory verification and an assessment on public field records**

Quoc-Bao Nguyen, Thai-Son Vu, Hung-Son Nguyen

This document accompanies the main text. Sections S1–S8 follow items (i)–(xi) of the Supplementary Material statement in the main text. Equation, table and figure numbers without the prefix S refer to the main text.

## S1. Scripts, console output and derived data (items i–ii)

The archive `scripts.zip` contains the analysis scripts and the console output of every run. `README.md` in the archive maps every table and figure of the main text and of this document to a script and a log file. `run_all.sh` reruns the closed forms and their FE verification, the multi-channel placement study and Monte Carlo simulation, the identifiability analysis of the in-service girder, the processing of the public field records and the laboratory evaluation. The derived data behind every figure and table are provided as CSV files in the same archive. The raw field records are not redistributed; they are available from the NOR-BWIM dataset (https://doi.org/10.7294/26880898.v1).

## S2. Laboratory specimen and data (item iii)

The specimen, a steel hollow square tube on three supports forming two equal spans of 2500 mm, and the measured single-load influence line are shown in Fig. S15. Table S1 lists the mid-span deflection of the first span for all three load configurations; the order of the three-load group is the best-fitting order discussed in Section 3.

**Table S1.** Mid-span deflection of the first span (mm), mean of three cycles. Single load 40.64 N; analytical values from the closed-form influence line.

| $x$ (mm) | Analytical, single | Measured, single | Two loads | Three loads |
|---|---|---|---|---|
| 0 | 0.0000 | 0.0000 | 0 | 0 |
| 250 | 0.8874 | 0.8844 | 0.4625 | 0.5525 |
| 500 | 1.6968 | 1.6975 | 1.8813 | 1.0450 |
| 750 | 2.3501 | 2.3525 | 3.1413 | 2.5413 |
| 1000 | 2.7693 | 2.7738 | 4.0988 | 4.8700 |
| 1250 | 2.8764 | 2.8827 | 4.6350 | 6.7588 |
| 1500 | 2.6253 | 2.6363 | 4.6238 | 7.9350 |
| 1750 | 2.0980 | 2.1100 | 4.0688 | 8.2775 |
| 2000 | 1.4087 | 1.4213 | 3.1375 | 7.6825 |
| 2250 | 0.6713 | 0.6838 | 1.9600 | 6.2800 |
| 2500 | 0.0000 | 0.0000 | 0.7715 | 4.3725 |
| 2750 | −0.5132 | −0.5069 | −0.2689 | 2.2975 |
| 3000 | −0.8644 | −0.8556 | −1.0063 | 0.3021 |
| 3250 | −1.0715 | −1.0600 | −1.4988 | −1.2588 |
| 3500 | −1.1526 | −1.1438 | −1.7813 | −2.3650 |
| 3750 | −1.1255 | −1.1200 | −1.8600 | −3.0363 |
| 4000 | −1.0085 | −1.0013 | −1.7738 | −3.3300 |
| 4250 | −0.8194 | −0.8175 | −1.5525 | −3.2663 |
| 4500 | −0.5763 | −0.5816 | −1.2213 | −2.9450 |
| 4750 | −0.2971 | −0.3019 | −0.8125 | −2.4125 |
| 5000 | 0.0000 | 0.0000 | −0.3325 | −1.7088 |
| 5250 | | | 0 | −1.0713 |
| 5500 | | | | −0.3650 |
| 5750 | | | | 0 |

## S3. Field records: tables and processing details (item iv)

**Table S2.** Integral constant $C$ and its scatter over the runs, lane A unless stated. CV expected: coefficient of variation predicted from the measured vehicle-free noise. For ch1, ch2, ch8 and ch9 the residual variance is 2.9–5.1 times the vehicle-free noise variance.

| Day, channel | Runs | $C$ (µε m/t), 95 % CI | CV observed (%) | CV expected (%) | χ² p |
|---|---|---|---|---|---|
| 1, ch11 (best) | 7 | −5.85 (−6.17, −5.53) | 5.8 | 6.8 | 0.60 |
| 1, gauge average (4 wheel-path gauges) | 7 | −4.03 (−4.24, −3.82) | 5.6 | 6.1 | 0.53 |
| 1, ch1, ch2, ch8, ch9 | 7 | −1.49 to −2.38 | 17.2–19.1 | 7.8–11.0 | ≤ 0.012 |
| 2, st36 | 8 | −5.97 (−6.57, −5.38) | 12.0 | 16.5 | 0.73 |
| 2, gauge average (4 gauges) | 8 | −4.12 (−4.62, −3.63) | 14.4 | 20.2 | 0.79 |
| 2, lane B, average | 8 | −3.27 (−4.19, −2.35) | 33.7 | 23.2 | 0.027 |

**Table S3.** Ratio of the integral constants of two trucks, lane A unless stated. Day 1: second to first truck, both 3-axle; day 2: 5-axle to 3-axle truck. Equivalence by two one-sided tests (TOST) at the 5 % level: the 90 % CI of the ratio lies inside the stated margin (for ch11, 0.904–1.098), so a 95 % CI can extend beyond a margin that is shown.

| Day, channel | Ratio (95 % CI) | Equivalence |
|---|---|---|
| 1, ch11 (best) | 0.996 (0.874–1.136) | shown within ±10 % |
| 1, gauge average (4 wheel-path gauges) | 0.955 (0.863–1.057) | shown only within ±11.8 % |
| 1, ch1, ch2, ch8, ch9 | 0.740–0.783 | invariance rejected (CIs exclude 1) |
| 2, st36 | 1.005 (0.735–1.375) | not shown |
| 2, gauge average (4 gauges) | 0.978 (0.697–1.374) | shown only within ±26.7 % |
| 2, lane B, average | 0.749 (0.440–1.276) | – (constants fail the χ² test, Table S2) |

**Table S4.** Correlation between gauges of the integrated strain: means over gauge pairs, with 95 % bootstrap CIs in brackets. Vehicle-free windows: 1227 on day 2 and 3405 on day 1. Crossing residual: deviation of a crossing's integral from its calibrated value. –: not computed.

| Correlation of | Day 2, 4 gauges | Day 1, 12 gauges |
|---|---|---|
| vehicle-free noise, non-overlapping windows | 0.92 (0.83–0.96) | 0.42 (0.26–0.54) |
| vehicle-free noise, window length of each crossing | 0.90 | – |
| crossing residuals | 0.63 | – |
| crossing residuals, st40 with its neighbours | 0.30–0.37 | – |

**Table S5.** Day 2: per-crossing standard deviation (SD) of the gross weight predicted by two covariance models, and the observed error (% of GVW). SD and MAE are different measures; the table compares the order of the two estimators, not magnitudes.

| Quantity | GLS, measured $\Sigma$ | Gauge average |
|---|---|---|
| SD predicted from the vehicle-free covariance | 12.7 | 19.8 |
| SD predicted from the covariance of the crossing residuals | 21.0 | 14.6 |
| Observed MAE, leave-one-run-out (main text Table 3) | 20.4 | 11.9 |

**Table S6.** Mean absolute error of the gross weight (% of GVW), out of sample, with 95 % bootstrap CIs over the test runs (n = 8 on day 2, n = 7 on day 1). LOTO: calibrated on one truck, tested on the other.

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

Processing details and further results:

- Bridge depth: about 3.8 m at mid-span and 9.5 m at the piers. Sampling: 100 Hz on day 1, 200 Hz on day 2.
- Day-1 driver-reported gross weights: 21.2–22.8 t for the runs used.
- Speeds were obtained from the axle spikes and the measured wheelbase and agree with the dataset authors' processing script within 1–2 %. Records were integrated over the whole time the truck was on the bridge plus 5 s at each end. Three day-1 runs with two trucks on the bridge and four passes without documented weights were excluded. Vehicle-free noise windows were at least 70 s from any detected vehicle.
- Day 1: eight of the twelve gauges have a coefficient of variation of 5.8–13.5 %, consistent with the noise (χ² p = 0.13–0.71). The first truck ran at 10.4–12.8 m/s and the second at 19.1–19.8 m/s. Day 2 speeds: 13–28 m/s; no speed effect resolved (+6 % per 10 m/s, 95 % CI −23 to +35 %).
- Day-2 noise amplitudes at the median speed: 13.7–32.8 µε m.
- GLS weights with the measured Σ: st40 +0.16, st36 −0.35. GLS with Σ estimated from the crossing residuals: error 10.4 % of GVW in sample, 28.4 % out of sample.
- Lane B: st36 ratio 0.64 (95 % CI 0.47–0.81). Two-truck runs: 0.92 and 0.92 of the summed single-truck predictions (pooled 95 % CI 0.77–1.06); GLS combination 0.82 (95 % CI 0.73–0.91).
- Gauges: a one-dimensional beam model predicts ch11/ch8 ratios of 0.978–1.003. Ratio of st36 to st40 constants: 3.24 ± 0.56 in lane A against 1.82 ± 0.10 in lane B (± one standard error), about 2.5 standard errors apart.
- Beam model (Euler–Bernoulli, parabolic haunch, second moment proportional to h²): r² = 0.79–0.94 against the strain histories; zeros of the uniform-load moment in span 2 at 121.6 m and 190.8 m; strain constant of the gauges 0.69 of the largest on the girder (0.56–0.93 across stiffness laws); cancellation ratio R = 0.51; span 2 contributes about 170 % of the net integral and the adjacent spans −26 % and −66 %.

## S4. Beam model of the five-span girder and synthetic records (item v)

The one-dimensional beam model of the five-span girder (Euler–Bernoulli, parabolic haunch) is described in Section 4.2 and in the notes of S3. Fig. S3 shows its observability along the girder, and Fig. S4 the synthetic records of the dataset authors processed with the same integration.

## S5. Strain blind-locus maps (item vi)

Figs. S5 and S6 map the strain indicator $N_M$ over the sensor position and the span ratio for two-span and symmetric three-span beams.

## S6. Multi-channel placement and structure-aware weighting functions (item vii)

Fig. S7 shows the extremes of the uniform-load response $C(x)$ that the placement rule of Section 2.4 selects. Fig. S8 gives the Monte Carlo verification of Eqs. (13) and (14), and Fig. S9 the structure-aware weighting functions of Appendix B.

## S7. Asymmetric three-span beams (item viii)

For arbitrary spans $L_1, L_2, L_3$ and rigidities $EI_1, EI_2, EI_3$, the two support moments follow from the three-moment equations at the inner supports, solved symbolically; the sensor deflection under a uniform load then follows by superposition, as in Appendix A. The general expressions are long and are given in the scripts. Four asymmetric cases agree with FE to a relative error of at most 9.2 × 10⁻¹². With the sensor at mid-span of span 1 and uniform rigidity, the blind ratio $L_1/L_2$ is 0.589774, 0.591969, 0.587260, 0.565712, 0.525757 and 0.461410 for $L_3/L_2$ = 0.3, 0.5, 0.6, 0.8, 1.0 and 1.2 (Fig. 2b).

## S8. Cầu Mây model, admissible sets and frequencies (item ix); dynamics (item x); simply supported records (item xi)

- Placement (Section 2.4): verified by a brute-force search over 96 cases and a Monte Carlo study with 10⁵ random axle configurations per case; white-noise to offset ratio σ²Δx/(δ₀²L_tot) ≈ 5 × 10⁻⁶ at σ = 0.01 mm, δ₀ = 0.1 mm, Δx = 0.1 m, L_tot = 220 m.
- Day-2 per-crossing SD predicted by the vehicle-free covariance (% of GVW): best single gauge 16.2, worst single gauge 32.5, gauge average 19.8, GLS diagonal Σ 19.4, GLS measured Σ 12.7, zero-sum measured Σ 13.3, zero-sum Σ = identity 16.1.
- Lane B, failing channels: CV 31–40 %, χ² p = 0.016–0.027.
- Cầu Mây design sections: depth 2.40 m (mid-span) to 5.40 m (piers), second moments 5.482 m⁴ and 59.61 m⁴, E_c = 36 057 MPa. Model-form variants: L_v = 40 and 45 m (base 44 m), exponents 2.5 and 3.2 (base 2.943), rigid pier zone ±1.5 m.
- Misfit ratio r₈₇: 1.126 at κ = 10⁷ kN m/rad, minimum 1.058 at κ = 1.68 × 10⁸ kN m/rad (calibration B), 1.091 for fixed piers.
- Admissible set against tolerance τ (Table S7):

**Table S7.** Admissible set of the Cầu Mây model against the tolerance τ on the misfit of each gauge.

| Tolerance, prior | κ (kN m/rad) | α | N8 indicator, αEI_mid | N8 indicator, design EI_mid | C₈ (m²/kN) |
|---|---|---|---|---|---|
| τ = 3 % | 1.0–3.0 × 10⁸ | 0.64–0.80 | – | – | – |
| τ = 4 % | 4.2 × 10⁷–2.0 × 10⁹ | 0.54–0.98 | – | – | – |
| τ = 5.3 % | ≥ 1.8 × 10⁷ | 0.51–1.15 | 0.14–0.42 | 0.12–0.82 | 3.0 × 10⁻⁵–2.0 × 10⁻⁴ |
| τ = 5.3 %, prior α ∈ [0.9, 1.3] | – | – | 0.14–0.27 | 0.12–0.30 | – |

Fig. S10 shows the predicted vertical frequencies against the scaled pier stiffness κ, Fig. S11 the static misfit over the plane of α and k, and Fig. S12 the closed-form Möbius law of Eq. (15) against FE.

The moving-force analysis behind the dynamic bound of Section 6 is reproduced by `s05_moving_force.py`; its console output (`s05_moving_force.log`) lists the quasi-static error against $t_\mathrm{cr}/T_1$, the effect of damping and the axle-configuration spread under dynamics.

Figs. S13 and S14 show the deflection records of two simply supported bridges tested by the authors, which illustrate the baseline handling and the low-pass filtering recommended in Section 7.

## Supplementary figure captions

Some panel labels use the notation of an earlier draft: $\rho_L$ = $\lambda$, $\rho_{EI}$ = $\gamma$, $L_m$, $L_s$ = $L_\mathrm{main}$, $L_\mathrm{side}$, $K$ = $\hat k$, "immune" = zero-sum estimator, "boundary-conditioning indicator" = boundary sensitivity $B_m$, "Cau May" = Cầu Mây.

![](/home/user/SHM-Paper1-1D/manuscript/v4/word/../figures/supplementary/FigS1_norbwim_noise_correlation.png){width=15.5cm}

**Fig. S1.** NOR-BWIM: correlation matrices of the integrated vehicle-free noise between gauges, for windows of crossing length; day 1 (12 gauges) and day 2 (4 gauges).

![](/home/user/SHM-Paper1-1D/manuscript/v4/word/../figures/supplementary/FigS2_norbwim_speed.png){width=15.5cm}

**Fig. S2.** NOR-BWIM: integral constant against speed for the day-1 gauge average, gauge ch1 and the day-2 gauge average, by truck; the panel titles give the fitted slope per 10 m/s with its 95 % CI.

![](/home/user/SHM-Paper1-1D/manuscript/v4/word/../figures/supplementary/FigS3_norbwim_beam_observability.png){width=15.5cm}

**Fig. S3.** Five-span girder, beam model with uniform rigidity and two haunch laws: uniform-load moment (top) and strain constant (middle) along the girder, normalised at the gauges, and the single-gauge error expected from the measured noise for a 25 t truck (bottom). Red line: gauge position; dotted lines: zero-moment points.

![](/home/user/SHM-Paper1-1D/manuscript/v4/word/../figures/supplementary/FigS4_veb_synthetic.png){width=15.5cm}

**Fig. S4.** Synthetic strain records of the dataset authors: integral per unit gross weight by truck and lane, and for a 3-axle truck against speed.

![](/home/user/SHM-Paper1-1D/manuscript/v4/word/../figures/supplementary/FigS5_strain_map_2span.png){width=15.5cm}

**Fig. S5.** Two-span beam: (a) strain indicator $N_M$ over the sensor position and the span ratio $\lambda$, with the strain and deflection blind loci and the near-blind band; (b) blind positions against $\lambda$.

![](/home/user/SHM-Paper1-1D/manuscript/v4/word/../figures/supplementary/FigS6_strain_map_3span.png){width=15.5cm}

**Fig. S6.** Symmetric three-span beam: strain indicator $N_M$ (a) in the side span and (b) in the main span measured from the pier, over the span ratio $\beta$, with the blind loci, the near-blind band and the Cầu Mây span ratio.

![](/home/user/SHM-Paper1-1D/manuscript/v4/word/../figures/supplementary/FigS7_Cx_extremes.png){width=15.5cm}

**Fig. S7.** Uniform-load response $C(x)$ along six girders (two-span, three-span and the Cầu Mây girder under calibrations A and B), with the maximum and minimum selected by the placement rule.

![](/home/user/SHM-Paper1-1D/manuscript/v4/word/../figures/supplementary/FigS8_multichannel_montecarlo.png){width=15.5cm}

**Fig. S8.** Monte Carlo verification: distribution of the load error for a single gauge, GLS and the zero-sum estimator with three gauges, (a) on a 30 + 60 + 30 m beam and (b) on the Cầu Mây girder (calibration A), and (c) scatter against the number of axles relative to theory.

![](/home/user/SHM-Paper1-1D/manuscript/v4/word/../figures/supplementary/FigS9_structure_aware_weights.png){width=15.5cm}

**Fig. S9.** Structure-aware weighting functions for two equal spans (Appendix B): (a) weighting functions along the record, (b) white-noise variance relative to uniform weighting against the range of entry shift, (c) configuration-dependent error under a stiffness error in the adjacent span.

![](/home/user/SHM-Paper1-1D/manuscript/v4/word/../figures/supplementary/FigS10_caumay_freq_vs_kappa.png){width=15.5cm}

**Fig. S10.** Cầu Mây: first, second and third vertical frequencies against the scaled pier stiffness κ, for low, base and high mass, with the measured band.

![](/home/user/SHM-Paper1-1D/manuscript/v4/word/../figures/supplementary/FigS11_caumay_alpha_k_map.png){width=15.5cm}

**Fig. S11.** Cầu Mây: static misfit over the rigidity factor α and the pier stiffness k, with contours of the third vertical frequency equal to the measured values.

![](/home/user/SHM-Paper1-1D/manuscript/v4/word/../figures/supplementary/FigS12_mobius_closedform.png){width=15.5cm}

**Fig. S12.** Cầu Mây proportions, prismatic beam: (a) deflection indicators of the side-span and main-span gauges against the relative pier stiffness $\hat k$, closed form against FE; (b) boundary sensitivity $B_m$.

![](/home/user/SHM-Paper1-1D/manuscript/v4/word/../figures/supplementary/FigS13_giecuc_phuongdo_baseline.png){width=15.5cm}

**Fig. S13.** Deflection records of two simply supported bridges (Gie Cục I and Phương Độ): deviation of the event integral from a linear pre/post baseline for several baseline treatments and high-pass filters.

![](/home/user/SHM-Paper1-1D/manuscript/v4/word/../figures/supplementary/FigS14_giecuc_phuongdo_lowpass.png){width=15.5cm}

**Fig. S14.** The same records: (a) deflection relative to the linear baseline, unfiltered and low-pass filtered at 2 Hz; (b) dynamic residual removed by the low-pass filter.

**Fig. S15.** Laboratory specimen and measured single-load influence line. [NEED VALUE: author to supply the photographs and figure]
