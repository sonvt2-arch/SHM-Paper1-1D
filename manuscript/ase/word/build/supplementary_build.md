# Supplementary Material

**Observability and sensor layout for influence-area load monitoring of continuous girder bridges**

Quoc-Bao Nguyen, Thai-Son Vu, Hung-Son Nguyen

This document accompanies the main text. Equation, table, figure and section numbers without the prefix S refer to the main text; references are to the main-text reference list, cited here by author and year.

Contents: S1 Nomenclature; S2 Closed forms for two- and three-span beams; S3 General channels, finite element verification and invariant weighting functions; S4 Multi-channel estimation and placement; S5 Identifiability, sensitivities and Möbius law; S6 Laboratory test; S7 Public field records; S8 Cầu Mây Bridge; S9 Dynamics and baseline handling; S10 Error budget and design checklist; S11 Scripts, console output and derived data.

## S1. Nomenclature

**Table S1.** Nomenclature.

| Symbol | Meaning |
|---|---|
| $A^+$ | positive part of the area under an influence line |
| $a$ | vector of channel weights of a multi-channel estimator |
| $b$ | relative bias of the load caused by a residual offset, Eq. (12) |
| $B_m$ | boundary sensitivity $\lvert\partial\ln C_m/\partial\ln\kappa\rvert$ |
| $C_0$, $C_\infty$ | integral constant for pinned and for fixed piers at $\alpha = 1$, Eq. (15) |
| $C_m$ | integral constant of the channel at $m$, Eq. (2) (m²/kN for deflection); called "the constant" in the text |
| $C_\varepsilon$, $C_\theta$, $C_V$ | integral constant of a strain, rotation and shear channel |
| $c$ | distance of the gauged fibre from the neutral axis (m) |
| $d_i$ | distance of axle $i$ behind the first axle (m) |
| $EI$, $EI_\mathrm{mid}$, $EI_\mathrm{ref}$ | flexural rigidity; design value at mid main span; reference rigidity used to normalise $N_w$ (kN m²) |
| $F_A$ | end-support reaction (kN) |
| $f_1$, $T_1$ | fundamental frequency and period of the girder |
| $g(x)$ | weighting function applied along a record |
| $h$ | girder depth (m) |
| $I$ | second moment of area |
| $J_m$ | record integral of the channel at $m$ over a complete crossing, in space |
| $k$, $k_g$ | rotational stiffness of a monolithic pier; girder stiffness against antisymmetric pier rotation (kN m/rad) |
| $\hat k$ | pier stiffness relative to the side-span rigidity, $kL_\mathrm{side}/EI_\mathrm{side}$ |
| $K_g$, $K_p$ | girder and pier parts of the stiffness matrix |
| $L$, $l$ | length of the span containing the sensor; span of the laboratory beam (m) |
| $L_p$ | length of the loaded path (m) |
| $L_\mathrm{tot}$ | length of the integration record (m) |
| $M_q$ | bending moment under a uniform load $q_0$ over the whole path |
| $\bar M_l$, $\bar M_r$ | normalised end moments $-8M/(q_0L^2)$ at the left and right ends of a span (positive for hogging) |
| $N_w$, $N_M$ | deflection and strain (moment) indicators, Eqs. (10) and (9) |
| $N_\theta$, $N_V$, $N_F$ | rotation, shear and end-reaction indicators (Section 2.2, Section S3) |
| $P_\mathrm{tot}$, $P_0$ | total load of a crossing; weighed reference load (kN) |
| $P_t$, $J_t$, $J_0$ | load and record integral of a target crossing; record integral of the reference crossing |
| $P_\delta$ | offset-equivalent load $\delta_0L_\mathrm{tot}/C$ (kN) |
| $R$ | cancellation ratio $C/A^+$ |
| $r_{87}$ | measured-to-model ratio at gauge N8 divided by that at gauge N7; $r_{87} = 1$ when one model fits both gauges |
| $S_\alpha$, $S_k$ | logarithmic sensitivities $\partial\ln C_m/\partial\ln\alpha$, $\partial\ln C_m/\partial\ln k$ (Section S5) |
| $t_\mathrm{cr}$ | duration of a crossing (s) |
| $w$, $w_q$ | deflection; deflection under the uniform load $q_0$ over the whole path |
| $\alpha$ | ratio of effective to design girder rigidity |
| $\beta$ | main-to-side span ratio $L_\mathrm{main}/L_\mathrm{side}$ (three spans) |
| $\gamma$ | rigidity ratio: $EI_2/EI_1$ (two spans, span 1 instrumented); $EI_\mathrm{main}/EI_\mathrm{side}$ (three spans) |
| $\delta_0$ | residual zero offset after re-zeroing before and after a crossing, in the units of the channel (mm for deflection) |
| $\zeta$ | position in the main span from the pier, as a fraction of the main span |
| $\eta_m$ | influence line of the channel at $m$ |
| $\kappa$ | scaled pier stiffness $k/\alpha$ (kN m/rad, since $\alpha$ is dimensionless) |
| $\lambda$ | span ratio $L_2/L_1$ of the adjacent to the instrumented span (two spans) |
| $\mu$ | interior-moment parameter, $\mu=-8M_B/(q_0L_1^2)$ |
| $\rho$ | common-mode fraction of the offset or noise between channels |
| $\Sigma$ | covariance matrix of the channel integrals |
| $\sigma$, $\Delta x$ | standard deviation of the white noise of a record; sampling interval along the record |
| $\sigma_{P,\mathrm{noise}}$ | standard deviation of the load estimate caused by white noise |
| $\tau$ | tolerance on the static misfit of a gauge |
| $\xi$ | sensor position as a fraction of its span |
| BPM | beam-property method: load = record integral / modelled constant |
| SLM | standard-load method: constant taken from a crossing of known weight |
| WIM, BWIM, NOR | weigh-in-motion; bridge weigh-in-motion; Nothing-on-Road (no sensors on the road surface) |
| CI, CV, MAE, SD | confidence interval; coefficient of variation; mean absolute error; standard deviation |
| FE | finite element |
| GLS | generalised least squares |
| GUM | Guide to the Expression of Uncertainty in Measurement |
| GVW | gross vehicle weight |
| LOO, LOTO | leave-one-run-out and leave-one-truck-out cross-validation |
| $r^2$ | coefficient of determination |
| TOST | two one-sided tests of equivalence |
| N7, N8 | deflection gauges at mid main span and at 0.4L of a side span (Cầu Mây) |
| T5, T7, T8 | supports of the Cầu Mây main bridge (Section 5.1) |

## S2. Closed forms for two- and three-span beams

For unequal spans the uniform-load support moment of a two-span beam is $M_B = -q_0(L_1^3/EI_1+L_2^3/EI_2)/[8(L_1/EI_1+L_2/EI_2)]$. Superposing the simply supported uniform-load deflection of span 1 and the deflection due to $M_B$, evaluating at $x_m$ and dividing by $q_0$ gives Eq. (5) with $\mu = -8M_B/(q_0L_1^2)$, which is $\mu_\mathrm{2span}$ of Eq. (4). Because $1-2\xi^2+\xi^3 = (1-\xi)(1+\xi-\xi^2)$, setting $F = 0$ gives Eq. (6). With uniform rigidity, the blind condition for a mid-span sensor is $3\lambda^2-3\lambda-2=0$, and maximising $F$ over $\xi$ at $\mu = 1$ gives $8\xi^2-\xi-1=0$, hence Eq. (7). In units of $L_1^4/(192EI_1)$, the positive contribution of the instrumented span varies only between 1.50 and 2.00 for $\lambda$ from 0.5 to 2.0, whereas the negative contribution of the adjacent span sweeps from −0.125 to −4.00; the cancellation is driven almost entirely by the adjacent span.

For the symmetric three-span beam the three-moment equation gives $M_B = M_C = -q_0L_\mathrm{side}^2\mu/8$ with $\mu_\mathrm{3span}$ of Eq. (4). Three equal spans give $\mu = 4/5$. The optimal side-span position solves $8\xi^3-(12-3\mu)\xi^2+(2-\mu)=0$ (Table S2). The near-blind band at mid side span runs from the root of $30\beta^3-69\beta-16=0$ (1.621) to that of $10\beta^3-27\beta-8=0$ (1.775). A mid main-span deflection sensor is blind at $\beta = 0.9647$. For a sensor at $\zeta = x/L_\mathrm{main}$ in the main span, $192EI_\mathrm{main}C_m/L_\mathrm{main}^4 = 8[\zeta(1-2\zeta^2+\zeta^3)-\nu\zeta(1-\zeta)]$ with $\nu = 3(\gamma+\beta^3)/[\beta^2(2\gamma+3\beta)]$. For $\beta = 1.636$ the strain blind point in the main span lies at $\zeta_0 = 0.177$ from the pier.

**Table S2.** Symmetric three-span beam, uniform rigidity: optimal side-span position $\xi^*$ and deflection indicator $N_w$ (Eq. (10); 2.5 for a simply supported mid-span).

| $\beta$ | $\mu$ | $\xi^*$ | $N_w$ at $\xi^*$ | $N_w$ at $\xi = 1/2$ |
|---|---|---|---|---|
| 1.0 | 0.800 | 0.4460 | 1.322 | 1.300 |
| 1.2 | 0.9743 | 0.4251 | 1.076 | 1.039 |
| 1.4 | 1.208 | 0.3875 | 0.7585 | 0.6884 |
| 1.5 | 1.346 | 0.3582 | 0.5807 | 0.4808 |
| 1.636 (= 90/55) | 1.558 | 0.2994 | 0.3316 | 0.1632 |
| 1.7 | 1.666 | 0.2608 | 0.2202 | 0.0015 |

Asymmetric three-span beams. For arbitrary spans $L_1, L_2, L_3$ and rigidities $EI_1, EI_2, EI_3$, the two support moments follow from the three-moment equations at the inner supports, solved symbolically; the sensor deflection under a uniform load then follows by superposition, as above. The general expressions are long and are given in the scripts. Four asymmetric cases agree with FE to a relative error of at most 9.2 × 10⁻¹². With the sensor at mid-span of span 1 and uniform rigidity, the blind ratio $L_1/L_2$ is 0.589774, 0.591969, 0.587260, 0.565712, 0.525757 and 0.461410 for $L_3/L_2$ = 0.3, 0.5, 0.6, 0.8, 1.0 and 1.2 (main-text Fig. 2b).

Strain blind-locus maps. Figs. S1 and S2 map the strain indicator $N_M$ over the sensor position and the span ratio for two-span and symmetric three-span beams. For two equal spans the strain near-blind band is $0.676<\xi<0.812$, that is, 0.19–0.32 of the span from the interior support.

## S3. General channels, finite element verification and invariant weighting functions

For a prismatic span with end-moment parameters $\bar M_l$, $\bar M_r$ and $\xi = x/L$, the indicators are $N_w = 8\Phi$ with $\Phi = \xi(1-2\xi^2+\xi^3)-\tfrac{\bar M_l}{2}(2\xi-3\xi^2+\xi^3)-\tfrac{\bar M_r}{2}(\xi-\xi^3)$, $N_\theta = 24EI\,C_\theta/L^3 = \Phi'(\xi)$, $N_M$ of Eq. (9) and $N_V = 2C_V/L = 1-2\xi+(\bar M_l-\bar M_r)/4$. $N_\theta$, $N_M$ and $N_V$ equal 1 for the simply supported reference (end rotation, mid-span moment, end shear). $N_w$ equals 2.5 at a simply supported mid-span and 1 at mid-span of each span of an equal two-span beam. For the two-span beam, $(\bar M_l, \bar M_r) = (0, \mu)$ in span 1 and $(\mu/\lambda^2, 0)$ in span 2; for the symmetric three-span beam, $(0, \mu)$ in the side span and $(\mu/\beta^2, \mu/\beta^2)$ in the main span with pinned piers; with pier springs, $\mu$ follows from Eq. (16) and the main-span values from $\bar M_\mathrm{main}$ in Section 2.5. Strain zeros solve $4\xi^2-(4+\bar M_l-\bar M_r)\xi+\bar M_l=0$.

All closed forms of Section 2.2 agree with FE evaluations of Eq. (2) in 981 checks, with a maximum error of 8.1 × 10⁻¹¹ on the normalised indicators. The verification covered two-span, symmetric and asymmetric three-span and four-span beams, zero-moment positions, ten blind configurations, the identity for a two-truck convoy on piecewise-prismatic girders with elastic pier springs (relative error 2.8 × 10⁻⁹), and the haunched Cầu Mây FE against an independent force-method solution (5.4 × 10⁻¹⁰). Truncating the record when the first axle leaves changed the integral by up to 59 % (rotation) and 10 % (moment) on the two-span example.

For the most general linear estimator $\hat P = \sum_j\int g_j(x)y_j(x)\,\mathrm{d}x$, with weighting functions $g_j$ along the records $y_j$, the mean is $\sum_iP_i\psi(s_i)$, with $s_i$ the position of axle $i$ and $\psi(s) = \sum_j\int g_j(x)\eta_j(x-s)\,\mathrm{d}x$. If $\psi$ must be constant in $s$ for every set of influence lines supported on $[0, L_p]$, then $\int_0^{L_p}[g(u+s)-g(u+s')]\eta(u)\,\mathrm{d}u = 0$ for every admissible $\eta$, so $g(u+s) = g(u+s')$ almost everywhere. Each $g_j$ is therefore constant, and the only freedom lies across channels. SLM relies on this invariance. An estimate built on the absolute value of the record (Deng et al., 2025) is not linear in the axle loads, so it loses this invariance whenever contributions of opposite sign overlap.

The same argument links SLM to transmissibility-based weighing (Yan et al., 2022): a transmissibility is a ratio of response spectra, and at zero frequency it equals the ratio of record integrals. A record integrated uniformly in time weights space by $1/v(x)$, so the integral must be taken in space; at constant speed $v$ the time integral is $J_m/v$.

When the influence line is known, other invariant weighting functions exist; for two equal spans their white-noise variance is 1.5–6.6 times smaller, but a 20 % rigidity error in the adjacent span then produces configuration-dependent errors of −1.1 % to +2.0 % (Fig. S3).

## S4. Multi-channel estimation and placement

For one channel, Eq. (13) returns $\hat P = J/C$ with variance $\sigma_{P,\mathrm{noise}}^2 + P_\delta^2$, where $\sigma_{P,\mathrm{noise}}$ is the standard deviation of the load estimate caused by white noise. For two channels the zero-sum weights are $a = (1,-1)/(C_1-C_2)$, and a second sensor over a support ($C_2 = 0$) gives the familiar differential measurement against a reference. The white-noise variance then rises by the factor $2C_1^2/(C_1-C_2)^2$, which is 1.65–2.0 on the beams studied. This price is small, because for the long-span parameters of Section 5.3 with $\Delta x = 0.1$ m the white-noise term of Eq. (14) is only about 5 × 10⁻⁶ of the offset term (σ = 0.01 mm, δ₀ = 0.1 mm, $L_\mathrm{tot}$ = 220 m, that is, the 200 m unit plus a 20 m convoy allowance). Strain and deflection channels need separate zero-sum constraints.

Which extreme of $C(x)$ to use depends on the offsets. With independent offsets, every sensor should sit as close as possible to the maximum, because the GLS variance then falls with the sum of the squared constants. With correlated offsets, one sensor should sit at the minimum, because a common offset cancels in the difference of two channels and the variance of Eq. (14) falls with the spread of the constants. The placement rule was verified by a brute-force search over 96 cases, which found no design better than the vertex design, and by a Monte Carlo study with 10⁵ random axle configurations per case, which confirmed that the estimators are unbiased and that Eqs. (13) and (14) hold to within 0.6 %. Fig. S4 shows the gain over the best single sensor under the assumed noise model, Fig. S5 the extremes of $C(x)$ that the rule selects, and Fig. S6 the Monte Carlo verification. For the Cầu Mây girder, the single-gauge standard deviation of the load at mid main span is 22.5 % for a 200 m record under the assumptions of Section 5.3 (ρ = 0.9, calibration A), against 24.8 % for the 220 m record.

## S5. Identifiability, sensitivities and Möbius law

Let $G = K^{-1}$ with $K = \alpha K_g + kK_p$, where $K_p$ has a unit entry on each inner-pier rotational degree of freedom, and $C_m = e_m^\top Gq$ with $q$ the consistent uniform load. Then $\mathrm{d}C_m/\mathrm{d}k = -\sum_i\theta_{m,i}\theta_{q,i}$, where $\theta_{m,i}$ and $\theta_{q,i}$ are the pier rotations under a unit load at the gauge and under the uniform load. The logarithmic sensitivities $S_\alpha = \partial\ln C_m/\partial\ln\alpha$ and $S_k = \partial\ln C_m/\partial\ln k$ satisfy $S_\alpha + S_k = -1$ by Euler's theorem, because $C_m$ is homogeneous of degree −1 in $(\alpha, k)$. Mirror symmetry decouples the symmetric and antisymmetric pier-rotation patterns, the uniform load excites only the antisymmetric one, and the Sherman–Morrison formula gives the linear-fractional (Möbius) law of Eq. (15) with $1/k_g$ the antisymmetric pier flexibility of the girder at $k = 0$. For the Cầu Mây model the law holds to a relative error of 5 × 10⁻⁶ over $k = 10^5$–$10^{12}$ kN m/rad, and Eq. (16) agrees with FE to 4.4 × 10⁻⁷ (Fig. S7).

Because every static response has the form $f(\kappa)/\alpha$, the ratio of two static readings carries all the information about $\kappa$; once $\kappa$ is chosen, either reading gives $\alpha$. With two static readings the Fisher matrix has a determinant proportional to $(S_{y8}-S_{y7})^2$, where $S_{y8}$ and $S_{y7}$ are the logarithmic sensitivities of the N8 and N7 readings to $\kappa$; this determinant vanishes at the minimum of the ratio misfit, that is, at calibration B. A frequency adds a row with the mass as nuisance parameter; a pier rotation adds a row without nuisance. Unequal pier stiffnesses would bring in the symmetric pattern, which Eq. (15) does not cover.

## S6. Laboratory test

The specimen is a steel hollow square tube on three supports forming two equal spans of 2500 mm. Deflection at mid-span of the first span was measured with a linear variable differential transformer of 0.005 mm resolution. The measured single-load influence line of the beam is shown in Fig. S8. Table S3 compares the identified total loads with direct weighing, and Table S4 lists the mid-span deflection for all three load configurations; the order of the three-load group is the best-fitting order discussed in Section 3. On the 250 mm grid the trapezoidal rule underestimates the exact single-load integral by 0.500 %. It is used throughout, because Simpson's rule loses its advantage when the kinks of trailing loads fall inside its panels.

**Table S3.** Identified total loads against direct weighing (trapezoidal rule). BPM: $P = J/C_m$ with the analytical constant; SLM: $P_t = P_0J_t/J_0$ with the single-load record as reference.

| Configuration | Weighed (N) | BPM (N) | BPM deviation | SLM (N) | SLM deviation |
|---|---|---|---|---|---|
| Two loads | 66.99 | 67.73 | +1.10 % | 67.40 | +0.61 % |
| Three loads | 125.08 | 126.57 | +1.19 % | 125.95 | +0.70 % |

**Table S4.** Mid-span deflection of the first span (mm), mean of three cycles. Single load 40.64 N; analytical values from the closed-form influence line.

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

## S7. Public field records

Data. The strain transducers of the Virginia Smart Road Bridge lie 158.5 m from the first abutment, at longitudinal stations about 2 m apart under the wheel path. Day 1 has 12 channels in three groups: four wheel-path gauges with clear axle spikes (ch4, ch5, ch11, ch12), a partner gauge at each of these four stations, and four further gauges without axle spikes (ch1, ch2, ch8, ch9). The bridge depth is about 3.8 m at mid-span and 9.5 m at the piers. Sampling was 100 Hz on day 1 and 200 Hz on day 2. The day-1 driver-reported gross weights were 21.2–22.8 t for the runs used. Errors are given as a percentage of the gross vehicle weight (GVW). Because the weights vary by only a few per cent within each day, a predictor that always returns the mean calibration weight already has a mean absolute error (MAE) of 2.0 % on day 2 and 2.2 % on day 1, and the field data test the scatter and invariance of the integral constant rather than the ability to discriminate weights.

Processing. Speeds were obtained from the axle spikes and the measured wheelbase and agree with the dataset authors' processing script within 1–2 %. A low-pass fit of the records gives lane-A speeds 1.139 times the spike speeds (median; SD 0.124; 22 runs). Lane-B speeds were taken from the lag between gauges. Records were integrated over the whole time the truck was on the bridge plus 5 s at each end. Three day-1 runs with two trucks on the bridge and four passes without documented weights were excluded. Vehicle-free noise windows were at least 70 s from any detected vehicle.

Invariance and speed. On day 1, eight of the twelve gauges have a coefficient of variation (CV) of 5.8–13.5 %, consistent with the noise (χ² p = 0.13–0.71; Table S5). The first truck ran at 10.4–12.8 m/s and the second at 19.1–19.8 m/s, so speed and truck are confounded. Day-2 speeds were 13–28 m/s; no speed effect was resolved (+6 % per 10 m/s, 95 % CI −23 to +35 %), but the confidence interval of the slope is too wide to call the constant speed-independent (Fig. S11). Equivalence was tested by two one-sided tests (TOST; Table S6). Day-2 noise amplitudes at the median speed were 13.7–32.8 µε m.

Lanes, superposition and gauges. In lane B, the channels that fail the χ² test have CV 31–40 % (χ² p = 0.016–0.027). Lane B, st36: ratio 0.64 (95 % CI 0.47–0.81). The two-truck runs gave 0.92 and 0.92 of the summed single-truck predictions (pooled 95 % CI 0.77–1.06); the GLS combination gave 0.82 (95 % CI 0.73–0.91). A one-dimensional beam model predicts ch11/ch8 ratios of 0.978–1.003. The ratio of st36 to st40 constants is 3.24 ± 0.56 in lane A against 1.82 ± 0.10 in lane B (± one standard error), about 2.5 standard errors apart.

Estimators. Table S8 gives all out-of-sample errors, including leave-one-truck-out (LOTO) and the four wheel-path gauges of day 1; Fig. S10 also shows in-sample results. On day 2, GLS with the measured covariance was significantly worse than the gauge average (paired difference +8.5 percentage points, 95 % CI +2.3 to +15.1); on day 1 the estimators cannot be told apart, and on both days every estimator is worse than the mean-weight predictor. Table S7 and Fig. S9 give the correlations behind this result, and Table S9 shows that the covariance of the crossing residuals, unlike the vehicle-free covariance, predicts the observed order of GLS and gauge average. The day-2 per-crossing SD predicted by the vehicle-free covariance (% of GVW) is 16.2 for the best single gauge, 32.5 for the worst single gauge, 19.8 for the gauge average, 19.4 for GLS with diagonal Σ, 12.7 for GLS with measured Σ, 13.3 for the zero-sum estimator with measured Σ and 16.1 for the zero-sum estimator with Σ = identity. The GLS weights with the measured Σ are st40 +0.16 and st36 −0.35. GLS with Σ estimated from the crossing residuals has a mean absolute error of 8.5 % of GVW in sample and 23.4 % out of sample (RMS 10.4 % and 28.4 %), that is, it over-fits with eight runs.

Beam model and limits. The beam model of the five-span girder (Euler–Bernoulli, parabolic haunch, second moment proportional to h²) gives r² = 0.79–0.94 against the strain histories; zeros of the uniform-load moment in span 2 at 121.6 m and 190.8 m; a strain constant of the gauges 0.69 of the largest on the girder (0.56–0.93 across rigidity laws); a cancellation ratio R = 0.51; and contributions of span 2 of about 170 % of the net integral and of the adjacent spans −26 % and −66 % (Fig. S12). Fig. S13 shows the synthetic records of the dataset authors processed with the same integration. The tests rest on four trucks, two axle counts and seven or eight runs per day. The gauge calibration factors and exact positions are not published, so absolute constants cannot be checked. The dataset authors reported a mean absolute GVW error of 4.6 % for their influence-line system on this bridge (Moghadam et al., 2023a); it was obtained on different runs and is not compared directly with the results of the main text.

**Table S5.** Integral constant $C$ and its scatter over the runs, lane A unless stated. CV expected: coefficient of variation predicted from the measured vehicle-free noise. For ch1, ch2, ch8 and ch9 the residual variance is 2.9–5.1 times the vehicle-free noise variance.

| Day, channel | Runs | $C$ (µε m/t), 95 % CI | CV observed (%) | CV expected (%) | χ² p |
|---|---|---|---|---|---|
| 1, ch11 (best) | 7 | −5.85 (−6.17, −5.53) | 5.8 | 6.8 | 0.60 |
| 1, gauge average (4 wheel-path gauges) | 7 | −4.03 (−4.24, −3.82) | 5.6 | 6.1 | 0.53 |
| 1, ch1, ch2, ch8, ch9 | 7 | −1.49 to −2.38 | 17.2–19.1 | 7.8–11.0 | ≤ 0.012 |
| 2, st36 | 8 | −5.97 (−6.57, −5.38) | 12.0 | 16.5 | 0.73 |
| 2, gauge average (4 gauges) | 8 | −4.12 (−4.62, −3.63) | 14.4 | 20.2 | 0.79 |
| 2, lane B, average | 8 | −3.27 (−4.19, −2.35) | 33.7 | 23.2 | 0.027 |

**Table S6.** Ratio of the integral constants of two trucks, lane A unless stated. Day 1: second to first truck, both 3-axle; day 2: 5-axle to 3-axle truck. Equivalence by two one-sided tests (TOST) at the 5 % level: the 90 % CI of the ratio lies inside the stated margin (for ch11, 0.904–1.098), so a 95 % CI can extend beyond a margin that is shown.

| Day, channel | Ratio (95 % CI) | Equivalence |
|---|---|---|
| 1, ch11 (best) | 0.996 (0.874–1.136) | shown within ±10 % |
| 1, gauge average (4 wheel-path gauges) | 0.955 (0.863–1.057) | shown only within ±11.8 % |
| 1, ch1, ch2, ch8, ch9 | 0.740–0.783 | invariance rejected (CIs exclude 1) |
| 2, st36 | 1.005 (0.735–1.375) | not shown |
| 2, gauge average (4 gauges) | 0.978 (0.697–1.374) | shown only within ±26.7 % |
| 2, lane B, average | 0.749 (0.440–1.276) | – (constants fail the χ² test, Table S5) |

**Table S7.** Correlation between gauges of the integrated strain: means over gauge pairs, with 95 % bootstrap CIs in brackets. Vehicle-free windows: 1227 on day 2 and 3405 on day 1. Crossing residual: deviation of a crossing's integral from its calibrated value. –: not computed.

| Correlation of | Day 2, 4 gauges | Day 1, 12 gauges |
|---|---|---|
| vehicle-free noise, non-overlapping windows | 0.92 (0.83–0.96) | 0.42 (0.26–0.54) |
| vehicle-free noise, window length of each crossing | 0.90 | – |
| crossing residuals | 0.63 | – |
| crossing residuals, st40 with its neighbours | 0.30–0.37 | – |

**Table S8.** Mean absolute error of the gross weight (% of GVW), out of sample, with 95 % bootstrap CIs over the test runs (n = 8 on day 2, n = 7 on day 1). LOTO: calibrated on one truck, tested on the other. The leave-one-run-out columns contain every row of the estimator table of the main text (Table 2).

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

**Table S9.** Day 2: per-crossing standard deviation (SD) of the gross weight predicted by two covariance models, and the observed error (% of GVW). SD and MAE are different measures; the table compares the order of the two estimators, not magnitudes.

| Quantity | GLS, measured $\Sigma$ | Gauge average |
|---|---|---|
| SD predicted from the vehicle-free covariance | 12.7 | 19.8 |
| SD predicted from the covariance of the crossing residuals | 21.0 | 14.6 |
| Observed MAE, leave-one-run-out (main text Table 2) | 20.4 | 11.9 |

## S8. Cầu Mây Bridge

Bridge and test. The bridge carries provincial road ĐT389. In the June 2020 acceptance test, four trucks stood in the side span (gauge N8) and six in the main span (gauge N7). The trucks were 3-axle, nominally 5 + 10 + 10 t, with a weighed mean of 25.06 t (Table S12). Mitutoyo dial gauges, mounted on independent frames fixed to the ground, read the peak deflection under central and eccentric transverse positions at three measuring points across each section (Table S11). The longitudinal truck positions are given as drawings in the test report and are not tabulated. The readings across one section differ by up to 2.05 mm in the eccentric N7 case, about 13 % of the mean reading.

Model. Design sections: depth 2.40 m (mid-span) to 5.40 m (piers), second moments 5.482 m⁴ and 59.61 m⁴, $E_\mathrm{c}$ = 36 057 MPa. Model-form variants: $L_\mathrm{v}$ = 40 and 45 m (base 44 m), exponents 2.5 and 3.2 (base 2.943), rigid pier zone ±1.5 m. The misfit ratio r₈₇ is 1.126 at κ = 10⁷ kN m/rad, has its minimum 1.058 at κ = 1.68 × 10⁸ kN m/rad (calibration B) and is 1.091 for fixed piers.

Admissible sets (Table S10). The conclusions depend on the tolerance. At τ = 3 % the admissible set shrinks and excludes the design rigidity, α = 1.

Frequencies. The measured vertical frequencies (3.43–3.64 Hz; Table S13) would narrow the admissible set further if they belonged to the third vertical mode. This interpretation is conditional: Fig. S14 shows the predicted vertical frequencies against the scaled pier stiffness κ, and Fig. S15 the static misfit over the plane of α and k with contours of the third vertical frequency. The acceptance test reports only one frequency per span, so the first frequency is not identified, and the Cramér–Rao bound of 0.24 that the first and third frequencies would give (Section 5.3) assumes a measurement that was not made.

Indicators and channels (Table S14). Going from pinned to fixed piers multiplies the N8 constant by 14.0 but reduces the N7 constant to 0.59 of its pinned value. A strain gauge at mid side span would be practically blind under calibration A ($N_M = 0.048$) and would change sign with pinned piers. A rotation reading at the end bearing T8 adds little, because its sensitivity duplicates that of N8. At calibration B the two-reading Fisher matrix is singular, so the deflections alone cannot bound $\ln C_8$ (Section S5).

**Table S10.** Admissible set of the Cầu Mây model against the tolerance τ on the misfit of each gauge.

| Tolerance, prior | κ (kN m/rad) | α | N8 indicator, $\alpha EI_\mathrm{mid}$ | N8 indicator, design $EI_\mathrm{mid}$ | C₈ (m²/kN) |
|---|---|---|---|---|---|
| τ = 3 % | 1.0–3.0 × 10⁸ | 0.64–0.80 | – | – | – |
| τ = 4 % | 4.2 × 10⁷–2.0 × 10⁹ | 0.54–0.98 | – | – | – |
| τ = 5.3 % | ≥ 1.8 × 10⁷ | 0.51–1.15 | 0.14–0.42 | 0.12–0.82 | 3.0 × 10⁻⁵–2.0 × 10⁻⁴ |
| τ = 5.3 %, prior α ∈ [0.9, 1.3] | – | – | 0.14–0.27 | 0.12–0.30 | – |

**Table S11.** Cầu Mây acceptance test (June 2020): measured peak deflection (mm, downward positive) at the two gauge sections, at three measuring points across each section, under central and eccentric truck arrangements.

| Section | Measuring point | Central | Eccentric |
|---|---|---|---|
| N8, side span, 0.4L from T8 | right edge | 5.32 | 5.91 |
| N8, side span, 0.4L from T8 | axis | 5.56 | 5.55 |
| N8, side span, 0.4L from T8 | left edge | 5.76 | 5.22 |
| N7, mid main span | right edge | 14.68 | 14.62 |
| N7, mid main span | axis | 15.24 | 15.51 |
| N7, mid main span | left edge | 15.83 | 16.67 |

**Table S12.** Weighed 3-axle test trucks: gross weight and axle spacings (front to middle axle; middle to rear axle) and track width. Mean gross weight 25.06 t.

| Truck | Gross weight (t) | Front axle spacing (m) | Rear axle spacing (m) | Track (m) |
|---|---|---|---|---|
| 1 | 24.7 | 3.45 | 1.35 | 1.9 |
| 2 | 25 | 3.65 | 1.45 | 1.85 |
| 3 | 25.66 | 3.45 | 1.35 | 1.85 |
| 4 | 25.06 | 3.85 | 1.35 | 1.85 |
| 5 | 25.05 | 3.45 | 1.35 | 1.85 |
| 6 | 25.3 | 3.65 | 1.45 | 1.85 |
| 7 | 25.1 | 3.7 | 1.45 | 1.9 |
| 8 | 25.5 | 3.65 | 1.45 | 1.9 |
| 9 | 24.6 | 3.65 | 1.45 | 1.85 |
| 10 | 24.6 | 3.6 | 1.45 | 1.85 |

**Table S13.** Vertical natural frequencies of the main-bridge spans reported in the acceptance test.

| Span | Vertical frequency (Hz) |
|---|---|
| Side span T5–T6 (55 m) | 3.43 |
| Main span T6–T7 (90 m) | 3.64 |
| Side span T7–T8 (55 m) | 3.63 |

**Table S14.** Deflection indicator $N_w$ (Eq. (10)), cancellation ratio $R$ (Eq. (11)) and boundary sensitivity $B_m$ of the Cầu Mây gauges, including the mid side-span position. $EI_\mathrm{ref}$ = design $EI_\mathrm{mid}$ and $L$ the span containing the gauge. Calibration A and the pinned-pier and fixed-pier rows have $\alpha = 1$, calibration B has $\alpha = 0.716$, and the admissible set spans $\alpha$ = 0.51–1.15; the haunched pinned-pier and fixed-pier rows give the extreme values over all model-form variants. $B_m$ at the design stiffness, with $k_g = 4.36\times10^7$ kN m/rad. –: not computed.

| Model | $N_w$, N8 at 0.4L (installed) | $N_w$, N8 at mid side span | $N_w$, N7 (installed) | $R$, N8 at 0.4L | $R$, N8 at mid side span | $R$, N7 |
|---|---|---|---|---|---|---|
| Prismatic beam, pinned piers | 0.287 | 0.163 | 0.755 | 0.14 | 0.08 | 0.70 |
| Haunched, calibration A | 0.181 | 0.105 | 0.209 | 0.18 | 0.11 | 0.59 |
| Haunched, calibration B | 0.476ᵃ | 0.377 | 0.234 | 0.56 | 0.49 | 0.77 |
| Haunched, admissible set ($\tau$ = 5.3 %) | 0.124–0.822ᵇ | – | 0.190–0.286 | 0.13–1.00 | – | 0.56–1.00 |
| Haunched, pinned piers | 0.023 | −0.066 | 0.263 | – | – | – |
| Haunched, fixed piers | 0.446 | 0.375 | 0.145 | – | – | – |
| $B_m$ at the design stiffness | 0.51 | – | 0.12 | – | – | – |

ᵃ Above the fixed-pier value because calibration B has $\alpha$ = 0.716; normalised by the effective rigidity $\alpha EI_\mathrm{mid}$ it is 0.341. ᵇ The upper part of this range requires $\alpha \approx 0.5$; normalised by the effective rigidity, the range is 0.144–0.422.

## S9. Dynamics and baseline handling

For a constant force moving across the laboratory beam, the quasi-static error is at most about 1 % when the ratio of the crossing time to the fundamental period, $t_\mathrm{cr}/T_1$, is at least 8, and it exceeds 15 % below 2.5 (Frýba, 1999). This bound omits vehicle–bridge interaction and road roughness. The moving-force analysis is reproduced by `s05_moving_force.py`; its console output (`s05_moving_force.log`) lists the quasi-static error against $t_\mathrm{cr}/T_1$, the effect of damping and the axle-configuration spread under dynamics.

The authors' deflection records from two simply supported bridges showed post-minus-pre level differences of up to 0.23 mm. Linear re-zeroing removes such differences, so this value bounds the drift before re-zeroing, not $\delta_0$. Figs. S16 and S17 show these records, which illustrate the baseline handling and the low-pass filtering recommended in Section S10.

## S10. Error budget and design checklist

The budget below is indicative, not an evaluation according to the Guide to the Expression of Uncertainty in Measurement (GUM): several entries are scenario ranges and the correlations between terms are not quantified. To first order, the relative error of BPM is the sum of the relative errors of the rigidity, the gain, the speed and the offset term of Eq. (12), plus four times the relative error of the span length. SLM removes the structural terms, because they belong to $C$. Every other term survives as the difference between the target and the reference crossings.

Speed enters twice. It affects the response itself, and it enters again through its measurement, because the space integral is the time integral times the speed measured at the gauges; a speed error therefore passes one-to-one into the weight. Speed variation over a 605 m crossing was not measured. On lane A, speeds from a low-pass fit of the records were 1.139 times those from the axle spikes (SD 0.124, 22 runs), so the choice of speed estimator alone can shift the weight by more than 10 %.

Table S15 evaluates Eq. (12) for the Cầu Mây gauges over the admissible set, with $L_\mathrm{tot} = 200$ m and the mean weighed truck of 25.06 t. The smaller offsets in Table S15 are typical of displacement transducers. Absolute deflection on a 90 m span over water would usually come from a non-contact technique, whose residual offset after re-zeroing has to be established on site, since environmental effects act over the same window (Sohn, 2007; Cross et al., 2013). At $\delta_0 = 0.1$ mm a single main-span gauge biases a 25 t truck by 16–25 %, and a single side-span gauge by 41–271 %. The zero-sum pair addresses this term only to the extent that the offset is common-mode during crossings.

Transverse position and multiple presence add further terms; Table S16 collects all terms. On the five-span girder the far-lane constant was 0.79 of the near-lane value. At Cầu Mây the readings across one section differ by up to 2.05 mm in the eccentric N7 case, about 13 % of the mean reading. Several vehicles on the structure return their combined weight; on the five-span girder the two-truck events gave 0.92 of the prediction. A crossing of the 200 m Cầu Mây unit takes 12.4 s at 60 km/h, and every crossing that overlaps another vehicle in that window must be discarded or treated as a group. The fraction of usable isolated crossings was not quantified. In the laboratory, the reference record and the load-dependent growth of the integral ratio cause the SLM deviations of 0.6–0.7 %. In the field, the noise, the lane and the gauge position dominate, and the weight errors of single crossings, 5–12 % on these records, exceed the spread of the reference weights.

**Table S15.** Bias of a single-channel estimate caused by a residual offset $\delta_0$, Eq. (12), for a 25.06 t truck; $L_\mathrm{tot}$ = 200 m. Ranges over the admissible set ($\tau$ = 5.3 %).

| Gauge | $C$ (m²/kN) | 0.02 mm | 0.05 mm | 0.1 mm | 0.2 mm | 0.5 mm |
|---|---|---|---|---|---|---|
| N7, mid main span | 3.3–5.0 × 10⁻⁴ | 3.3–5.0 % | 8–12 % | 16–25 % | 33–50 % | 82–124 % |
| N8, 0.4L | 3.0 × 10⁻⁵–2.0 × 10⁻⁴ | 8–54 % | 21–136 % | 41–271 % | 82–543 % | 206–1356 % |

**Table S16.** Indicative sensitivity budget of the integral estimator. Values are those measured or assumed in this study; they are not combined.

| Term | Sensitivity | Cancels in SLM? | Value in this study |
|---|---|---|---|
| Flexural rigidity $EI$ | 1 | yes | BPM only; Cầu Mây N8 constant varies 6.6-fold over the admissible set |
| Span length | 4 | yes | BPM only |
| Gain | 1 | if not recalibrated between crossings | not evaluated |
| Reference weighing $P_0$ | 1 | no | laboratory: OIML class M1 weights; field: day-1 weights driver-reported |
| Residual offset, drift $\delta_0$ | $L_\mathrm{tot}/J$ per unit offset | only if common-mode during crossings | Table S15; field per-crossing SD of the gauge average predicted 19.8 % (day 2), 5.3 % (day 1) |
| Speed effect | 1 | no | day 2: +6 % per 10 m/s (95 % CI −23 to +35 %), not resolved |
| Speed measurement | 1 | no | 1–2 % against the dataset speeds; a second estimator differs by a factor of 1.139 (SD 0.124) |
| Dynamics | 1 | partly | ≤ 1 % for $t_\mathrm{cr}/T_1 \ge 8$ (constant force) |
| Transverse position | lane-dependent $C$ | no, unless lane-specific | field lane ratio 0.79; Cầu Mây range 2.05 mm across a section |
| Multiple presence | group weight | – | two-truck events 0.92 of prediction |
| Linearity, seating | 1 | no | laboratory integral ratio 1.010 → 1.017 |

Design checklist. The results combine into the following procedure for designing load-monitoring channels on a continuous girder before installation.

1. Constants. For each candidate channel and position, compute $C$ from one static analysis under a uniform unit load on each lane, Eq. (2). Use Eqs. (4)–(9) for prismatic two- and three-span beams.
2. Blindness. Locate the blind loci of Table 1. Keep strain gauges out of the near-blind band $|N_M|<0.2$ around every zero-moment point, including gauges set back from a pier. Keep deflection gauges out of the near-blind bands $|N_w|<0.2$, for example $1.385<\lambda<1.525$ for a mid-span gauge on two spans and $1.621<\beta<1.775$ for a mid side-span gauge on three spans.
3. Conditioning. Report $N_M$ for strain, $N_w$ with its $EI_\mathrm{ref}$ for deflection (or the absolute constant), and $R$ for both. A small indicator with $R$ near 1 is restraint, not cancellation.
4. Boundary robustness. Evaluate $C$ over the plausible range of pier stiffness; for a symmetric girder, Eq. (15) gives the whole curve from the pinned and fixed constants. Avoid locations with large $C_\infty/C_0$ or $B_m$, or plan the measurement that identifies $\kappa$: a tiltmeter on a monolithic pier, an identified first frequency, or an integral ratio between two gauges.
5. Placement. Place sensors at the extremes of $C(x)$ of each channel type: $w_q$ for deflection and $cM_q/EI$ for strain.
6. Estimator. Use SLM with weighed vehicles of clearly different weights, several reference crossings and lane-specific constants. Combine channels by GLS or zero-sum weights only after estimating $\Sigma$ from the residuals of calibration crossings and checking it out of sample against the gauge average; covariances from vehicle-free windows alone can mislead. Use BPM only where the location is well conditioned and the structure is known; on box girders with deck-mounted gauges, a beam model does not give the constant.
7. Offset and dynamics. Evaluate $P_\delta$, Eq. (12), for the residual offset that the instrumentation achieves after re-zeroing, and compare it with the lightest vehicle to be screened. Check $t_\mathrm{cr}/T_1 \ge 8$ with the measured fundamental frequency $f_1 = 1/T_1$.
8. Processing. Integrate in space over the complete crossing, re-zero before and after each crossing, remove dynamics with a low-pass filter whose cut-off is well below the fundamental frequency $f_1$ and never with a high-pass filter, and discard overlapping crossings.

The integral method is a simplified alternative to influence-line BWIM, not a competitor. It returns the gross weight of a vehicle or group from one scalar constant per channel and one weighted sum. Its natural role is low-cost screening across many continuous structures, with instrumented BWIM or enforcement weighing for the vehicles it flags.

## S11. Scripts, console output and derived data

The archive `scripts.zip` contains the analysis scripts and the console output of every run. `README.md` in the archive maps every table and figure to a script and a log file, and `ASE_numbering.md` converts its numbering to that of the article and this document. `run_all.sh --v4` reruns the closed forms and their FE verification, the multi-channel placement study and Monte Carlo simulation, the identifiability analysis of the in-service girder, the processing of the public field records and the laboratory evaluation. Every equation and numerical output was checked independently against an analytical, finite element or convergence-based route. The derived data behind every figure and table are provided as CSV files in the same archive. The raw field records are not redistributed; they are available from the NOR-BWIM dataset (https://doi.org/10.7294/26880898.v1).

## Supplementary figure captions

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS1_strain_map_2span.png){width=15.5cm}

**Fig. S1.** Two-span beam: (a) strain indicator $N_M$ over the sensor position and the span ratio $\lambda$, with the strain and deflection blind loci and the near-blind band; (b) blind positions against $\lambda$.

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS2_strain_map_3span.png){width=15.5cm}

**Fig. S2.** Symmetric three-span beam: strain indicator $N_M$ (a) in the side span and (b) in the main span measured from the pier, over the span ratio $\beta$, with the blind loci, the near-blind band and the Cầu Mây span ratio.

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS3_structure_aware_weights.png){width=15.5cm}

**Fig. S3.** Structure-aware weighting functions for two equal spans (Section S3): (a) weighting functions along the record, (b) white-noise variance relative to uniform weighting against the range of entry shift, (c) configuration-dependent error under a rigidity error in the adjacent span.

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS4_multichannel_gain.png){width=15.5cm}

**Fig. S4.** Multi-channel estimation under the assumed noise model: (a) variance with two or three optimally placed sensors relative to the best single sensor, against the common-mode fraction $\rho$ of the offset; (b) standard deviation of the load against the offset level for single sensors and three-sensor designs; (c) zero-sum pair at $\rho = 1$ against the white-noise level. 2S-eq: equal two-span beam; 3S-b2.0: three-span beam with $\beta = 2$; CM-A, CM-B: Cầu Mây calibrations A and B.

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS5_Cx_extremes.png){width=15.5cm}

**Fig. S5.** Uniform-load response $C(x)$ along six girders (two-span, three-span and the Cầu Mây girder under calibrations A and B), with the maximum and minimum selected by the placement rule.

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS6_multichannel_montecarlo.png){width=15.5cm}

**Fig. S6.** Monte Carlo verification: distribution of the load error for a single gauge, GLS and the zero-sum estimator with three gauges, (a) on a 30 + 60 + 30 m beam and (b) on the Cầu Mây girder (calibration A), and (c) scatter against the number of axles relative to theory.

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS7_mobius_closedform.png){width=15.5cm}

**Fig. S7.** Cầu Mây proportions, prismatic beam: (a) deflection indicators of the side-span and main-span gauges against the relative pier stiffness $\hat k$, closed form against FE; (b) boundary sensitivity $B_m$.

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS8_lab_influence_line.png){width=15.5cm}

**Fig. S8.** Laboratory two-span beam: measured and analytical influence line of the mid-span deflection of the first span for the single 40.64 N load (Table S4).

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS9_norbwim_noise_correlation.png){width=15.5cm}

**Fig. S9.** NOR-BWIM: correlation matrices of the integrated vehicle-free noise between gauges, for windows of crossing length; day 1 (12 gauges) and day 2 (4 gauges).

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS10_norbwim_estimators.png){width=15.5cm}

**Fig. S10.** NOR-BWIM: mean absolute error of the gross weight for single-gauge, gauge-average, GLS, zero-sum and mean-weight (mean-GVW) predictors, with 95 % bootstrap confidence intervals: in sample (IN), leave-one-run-out (LOO) and leave-one-truck-out (LOTO). (a) Day 2, 4 gauges; (b) day 1, 4 wheel-path gauges; (c) day 1, 12 gauges (multi-gauge estimators use all 12; only the single gauges ch5 and ch11 are shown). GLS-diag: diagonal covariance; zero-sum-eq: zero-sum estimator with equal noise ($\Sigma$ = identity matrix); GLS-resid: covariance from crossing residuals.

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS11_norbwim_speed.png){width=15.5cm}

**Fig. S11.** NOR-BWIM: integral constant against speed for the day-1 gauge average, gauge ch1 and the day-2 gauge average, by truck; the panel titles give the fitted slope per 10 m/s with its 95 % CI.

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS12_norbwim_beam_observability.png){width=15.5cm}

**Fig. S12.** Five-span girder, beam model with uniform rigidity and two haunch laws: uniform-load moment (top) and strain constant (middle) along the girder, normalised at the gauges, and the single-gauge error expected from the measured noise for a 25 t truck (bottom). Red line: gauge position; dotted lines: zero-moment points.

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS13_veb_synthetic.png){width=15.5cm}

**Fig. S13.** Synthetic strain records of the dataset authors: integral per unit gross weight by truck and lane, and for a 3-axle truck against speed.

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS14_caumay_freq_vs_kappa.png){width=15.5cm}

**Fig. S14.** Cầu Mây: first, second and third vertical frequencies against the scaled pier stiffness κ, for low, base and high mass, with the measured band.

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS15_caumay_alpha_k_map.png){width=15.5cm}

**Fig. S15.** Cầu Mây: static misfit over the rigidity factor α and the pier stiffness k, with contours of the third vertical frequency equal to the measured values.

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS16_giecuc_phuongdo_baseline.png){width=15.5cm}

**Fig. S16.** Deflection records of two simply supported bridges (Gie Cục I and Phương Độ): deviation of the event integral from a linear pre/post baseline for several baseline treatments and high-pass filters.

![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/supplementary/FigS17_giecuc_phuongdo_lowpass.png){width=15.5cm}

**Fig. S17.** The same records: (a) deflection relative to the linear baseline, unfiltered and low-pass filtered at 2 Hz; (b) dynamic residual removed by the low-pass filter.
