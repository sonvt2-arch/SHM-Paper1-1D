# Blind loci and design criteria for integral load-monitoring channels on continuous girder bridges, with laboratory verification and an assessment on public field records

Quoc-Bao Nguyen^a^, Thai-Son Vu^a,\*^, Hung-Son Nguyen^a^

^a^ Faculty of Bridge and Road Engineering, Hanoi University of Civil Engineering, 55 Giai Phong, Bach Mai ward, 11618 Ha Noi, Viet Nam

\* Corresponding author: Thai-Son Vu. Tel.: +84 971 899 888. E-mail: sonvt2@huce.edu.vn

E-mail addresses: baonq@huce.edu.vn (Q.-B. Nguyen), sonvt2@huce.edu.vn (T.-S. Vu), sonnh@huce.edu.vn (H.-S. Nguyen)

---

## Abstract

Influence-area weigh-in-motion estimates gross vehicle weight from the area under a response record. On a continuous girder, positive and negative parts of the influence line can cancel, leaving a gauge blind to the load. This paper gives criteria for choosing, before installation, channels that observe the total load. They build on the influence-area identity: the area under a record equals the load times the channel's response to a uniform unit load, the integral constant. Closed forms give the blind loci of four channel types (deflection, strain, rotation, reaction) on continuous and haunched girders. Strain gauges are blind wherever the uniform-load moment vanishes, and nearly blind in a band around these points. A cancellation ratio separates cancellation from restraint. Optimal sensors lie at the extremes of the uniform-load response. A closed-form law gives the integral constant as a function of uncertain pier stiffness. A static test on a laboratory two-span beam confirms the identity. On public moving-truck records from a five-span box girder, invariance of the constant could be shown only within margins of 10–27 %, and the narrow range of reference weights did not allow weight discrimination to be tested. Generalised least-squares weights estimated from vehicle-free noise performed worse out of sample than the gauge average, because crossing residuals are much less correlated between gauges than vehicle-free noise. On an in-service three-span box girder, two static readings leave the constant of a side-span deflection gauge uncertain by a factor of 6.6, while the centre-span gauge is well determined.

**Keywords:** Structural health monitoring; Sensor placement; Bridge weigh-in-motion; Continuous girder; Identifiability; Field assessment

---

## Nomenclature

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
| $EI$, $EI_\mathrm{mid}$, $EI_\mathrm{ref}$ | flexural rigidity; design value at mid main span; reference rigidity used to normalise $N_w$ (kN m²) |
| $F_A$ | end-support reaction (kN) |
| $f_1$, $T_1$ | fundamental frequency and period of the girder |
| $g(x)$ | weighting function applied along a record |
| $I$ | second moment of area |
| $J_m$ | record integral of the channel at $m$ over a complete crossing, in space |
| $k$, $k_g$ | rotational stiffness of a monolithic pier; girder stiffness against antisymmetric pier rotation (kN m/rad) |
| $\hat k$ | pier stiffness relative to the side-span rigidity, $kL_s/EI_s$ |
| $K_g$, $K_p$ | girder and pier parts of the stiffness matrix |
| $L$, $l$ | length of the span containing the sensor; span of the laboratory beam (m) |
| $L_p$ | length of the loaded path (m) |
| $L_\mathrm{tot}$ | length of the integration record (m) |
| $M_q$ | bending moment under a uniform load $q_0$ over the whole path |
| $\bar M_l$, $\bar M_r$ | normalised end moments $-8M/(q_0L^2)$ at the left and right ends of a span (positive for hogging) |
| $N_w$, $N_M$ | deflection and strain (moment) indicators, Eqs. (10) and (9) |
| $N_\theta$, $N_V$, $N_F$ | rotation, shear and end-reaction indicators (Section 2.2, Appendix B) |
| $P_\mathrm{tot}$, $P_0$ | total load of a crossing; weighed reference load (kN) |
| $P_t$, $J_t$, $J_0$ | load and record integral of a target crossing; record integral of the reference crossing |
| $P_\delta$ | offset-equivalent load $\delta_0L_\mathrm{tot}/C$ (kN) |
| $R$ | cancellation ratio $C/A^+$ |
| $r_{87}$ | measured-to-model ratio at gauge N8 divided by that at gauge N7; $r_{87} = 1$ when one model fits both gauges |
| $S_\alpha$, $S_k$ | logarithmic sensitivities $\partial\ln C_m/\partial\ln\alpha$, $\partial\ln C_m/\partial\ln k$ (Appendix C) |
| $t_\mathrm{cr}$ | duration of a crossing (s) |
| $w$, $w_q$ | deflection; deflection under the uniform load $q_0$ over the whole path |
| $\alpha$ | ratio of effective to design girder rigidity |
| $\beta$ | centre-to-side span ratio $L_c/L_s$ (three spans; $c$ = centre or main span, $s$ = side span) |
| $\gamma$ | rigidity ratio: $EI_2/EI_1$ (two spans, span 1 instrumented); $EI_c/EI_s$ (three spans) |
| $\delta_0$ | residual zero offset after re-zeroing before and after a crossing, in the units of the channel (mm for deflection) |
| $\zeta$ | position in the main span from the pier, as a fraction of the main span |
| $\eta_m$ | influence line of the channel at $m$ |
| $\kappa$ | scaled pier stiffness $k/\alpha$ (kN m/rad, since $\alpha$ is dimensionless) |
| $\lambda$ | span ratio $L_2/L_1$ of the adjacent to the instrumented span (two spans) |
| $\mu$ | interior-moment parameter, $\mu=-8M_B/(q_0L_1^2)$ |
| $\rho$ | common-mode fraction of the offset or noise between channels |
| $\Sigma$ | covariance matrix of the channel integrals |
| $\sigma$, $\Delta x$ | standard deviation of the white noise of a record; sampling interval along the record |
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

---

## 1. Introduction

Heavy vehicles above the design envelope shorten the life of highway bridges and, in extreme cases, contribute to collapse. A span of the Yangmingtan Bridge failed in 2012 under four overloaded trucks crossing together [1]. In other documented failures, heavy traffic acted together with design deficiencies or material degradation [2,3]. Knowing the loads that a bridge actually carries is therefore part of risk-informed asset management [4].

Pavement weigh-in-motion (WIM) is mature [5,6] and has codified accuracy classes [7], but it weighs the vehicle rather than the load on a particular bridge. Bridge weigh-in-motion (BWIM), introduced by Moses [8], fits the measured response to axle loads times influence-line ordinates. It now includes influence lines calibrated from measurements [9], regularised solutions [10], accuracy improvements [11,12], contactless sensing [13] and virtual-axle methods without axle detectors [14]. Nothing-on-Road (NOR) systems also estimate the transverse position of the vehicle [15]. Moving-force identification recovers axle-load histories in the time or frequency domain [16–18]. It has been applied to multi-span bridges [19] and extended with dynamic and Kalman-filter formulations [20–22]. These methods aim at axle loads and need several sensors, a structural model or a regularised inversion.

A simpler family estimates only the gross weight from the area under the response. Ojio and Yamada integrated the strain records of plate-girder stringers, multiplied the result by the speed and calibrated it against a truck of known weight [23]; this calibration is called the standard-load method (SLM) below. The method has been used in long-term monitoring [24]. On a seven-span slab-on-girder bridge it was accurate to within 5 % for test trucks with well-estimated speeds [25,26]. Later work added strain-area and strain-integral variants [27–29], shear-strain weighing [30], a sparse-sensing influence-area system that chose the number and location of strain gauges on a single-span bridge [31], simplified BWIM in the field [32] and load-cell reactions [33]. Yan et al. proposed a probabilistic, influence-line-free gross-weight scheme based on a transmissibility-like index [34]. The integral of the influence line has also served as a damage feature [35,36], and the present authors used the integral of mid-span deflection on a simply supported beam [37].

The identity behind all of these methods is classical: the area under an influence line equals the response to a uniform unit load, which is how design codes evaluate distributed lane loads [38]. Combining several channels by generalised least squares (GLS) is equally standard, and its zero-sum variant, with channel weights that add up to zero, is the familiar differential measurement against a reference.

On continuous girders, however, the influence line changes sign over each interior support, and positive and negative areas partly cancel. Gross weight has been obtained without influence lines from distributed fibre-optic strain on a five-span continuous bridge [39]. Lane-specific influence lines were needed on a continuous multi-girder bridge [40], and long-span continuous box girders have been weighed from deck strain [41–43]. Optimal sensor placement for BWIM has been posed through an augmented Kalman filter [44], deflection-based load identification as a regularised stochastic problem [45,46], and measured deflection influence lines have been inverted for the stiffness of continuous girders [47]. None of these studies gives a criterion, available before installation, that says which channel at which position can observe the total load at all, how robustly to uncertain boundary conditions, and what a multi-channel integral estimator can deliver on real records.

This paper supplies such criteria. Neither the influence-area identity nor the GLS estimator is new; the contribution lies in the criteria built on them:

1. a closed-form catalogue of blind loci for deflection, strain, rotation, shear and reaction channels on two- and three-span and haunched girders, including the near-blind band that can catch strain gauges set back from the piers;
2. the strain indicator $N_M$, which needs no reference stiffness, the cancellation ratio $R$, which separates cancellation from restraint, and a normalisation of the deflection indicator that makes its threshold explicit;
3. a placement rule: optimal sensors lie at the extremes of the uniform-load response, for strain at the extremes of $cM_q/EI$;
4. an identifiability analysis of the indicator under boundary uncertainty, in which the constant depends on pier stiffness only through the scaled pier stiffness $\kappa = k/\alpha$ and a linear-fractional (Möbius) law, and which names the measurement that resolves it;
5. an assessment, on a laboratory beam and on public moving-truck records, of what single- and multi-channel integral estimators can and cannot deliver.

Section 2 develops the theory, Section 3 checks it in the laboratory, Section 4 assesses it on public field records, Section 5 applies it to an in-service box girder, and Sections 6 and 7 give the error budget and the design workflow.

---

## 2. Theory

This section states the classical identity with its validity envelope, then derives the blind loci, the indicators, the multi-channel estimator with its placement rule, and the identifiability of the constant. Derivations are in Appendices A–C.

### 2.1. Influence-area identity

Consider a linear-elastic structure whose properties do not change during a crossing, with any distribution $EI(x)$ and any linear elastic supports. A response channel at a fixed point $m$ is any fixed linear functional of the displacement field, measured from the unloaded state: the deflection $w(x_m)$, the rotation $w'(x_m)$, the bending moment, the fibre strain $\varepsilon = cM/EI$, the shear force or a support reaction. Let $\eta_m(x)$ be its influence line, with $\eta_m = 0$ outside the loaded path $[0, L_p]$. A convoy of axle loads $P_i$ at fixed offsets $a_i$ ($a_1 = 0$) crosses quasi-statically, so the record is

$$y_m(x)=\sum_{i=1}^{n}P_i\,\eta_m(x-a_i). \tag{1}$$

Integrating Eq. (1) over the complete crossing and substituting $u = x - a_i$ term by term gives the record integral

$$J_m=\int_0^{L_p+a_\mathrm{max}}y_m\,\mathrm{d}x=P_\mathrm{tot}\,C_m,\qquad C_m=\int_0^{L_p}\eta_m(u)\,\mathrm{d}u=\frac{y_m[q_0]}{q_0}, \tag{2}$$

where $y_m[q_0]$ is the response of the channel to a uniform load $q_0$ over the whole path. This is the classical influence-area identity [23,38]; the second equality needs superposition only. $C_m$ is called the integral constant, or simply the constant; $C_\varepsilon$, $C_\theta$ and $C_V$ denote it for strain, rotation and shear channels. For a strain gauge,

$$C_\varepsilon=\frac{c_m\,M_q(x_m)}{EI_m\,q_0}. \tag{3}$$

The local section constants enter Eq. (3) only as a gain, so a strain channel is blind exactly at the zeros of the uniform-load moment diagram, for any $EI(x)$ and any elastic supports. At constant speed $v$ the time integral is $J_m/v$.

Two single-channel estimators follow from Eq. (2). The beam-property method (BPM) computes $C$ from a structural model and returns $P = J/C$. The standard-load method (SLM) takes the constant from a reference crossing of known weight $P_0$ and returns $P_t = P_0J_t/J_0$ [23].

Eq. (2) holds under five conditions, each of which the later sections test. The structure must be linear and time-invariant during the crossing (Section 3 and the superposition test of Section 4.4). A quasi-static response is assumed (Section 6). Because the axles must follow the path on which $\eta_m$ is defined, each lane has its own constant (Section 4.4). A complete crossing is needed: truncating the record when the first axle leaves changes the rotation integral by up to 59 % on a two-span example (Appendix B). The record must be re-zeroed to the unloaded state, and any residual offset or slow drift enters the integral directly (Sections 2.3 and 4.3).

### 2.2. Closed-form blind loci

For a prismatic span under a uniform load, every channel is fixed by the two end moments. Each end moment $M$ is written in dimensionless form as $\bar M = -8M/(q_0L^2)$, positive for hogging: $\bar M_l$ at the left end and $\bar M_r$ at the right end. In the instrumented span of a two-span beam and in the side span of a symmetric three-span beam, $(\bar M_l, \bar M_r) = (0, \mu)$, where $\mu$ is the classical interior-moment parameter (Appendix A; [38]). It depends on the span ratio, $\lambda = L_2/L_1$ for two spans and $\beta = L_c/L_s$ for three spans, and on the rigidity ratio $\gamma$, which is $EI_2/EI_1$ for two spans and $EI_c/EI_s$ for three spans:

$$\mu_\mathrm{2span}=\frac{1+\lambda^3/\gamma}{1+\lambda/\gamma},\qquad \mu_\mathrm{3span}=\frac{2(\gamma+\beta^3)}{2\gamma+3\beta}. \tag{4}$$

The deflection constant at $\xi = x_m/L$ is

$$\frac{192EI\,C_m}{L^4}=8F(\xi,\mu),\qquad F(\xi,\mu)=\xi(1-2\xi^2+\xi^3)-\frac{\mu}{2}\,\xi(1-\xi^2). \tag{5}$$

The left-hand side of Eq. (5) is the deflection indicator of Section 2.3, Eq. (10), with $EI_\mathrm{ref} = EI$. Setting $F = 0$ gives the deflection blind condition, which depends on $\mu$ alone:

$$C_m=0\;\Leftrightarrow\;\mu=\mu_\mathrm{crit}(\xi)=\frac{2(1+\xi-\xi^2)}{1+\xi}. \tag{6}$$

A deflection blind point therefore exists only for $1<\mu<2$. For a mid-span sensor on two spans of equal rigidity, the blind span ratio and the optimal sensor position are

$$\lambda_\mathrm{crit}=\frac{3+\sqrt{33}}{6}=1.4574,\qquad \xi^*=\frac{1+\sqrt{33}}{16}=0.4215. \tag{7}$$

For the symmetric three-span beam with uniform rigidity and a sensor at mid side span, the blind main-to-side ratio is the positive root of $6\beta^3-15\beta-4=0$:

$$\beta_\mathrm{crit}=\sqrt{10/3}\,\cos\!\Big[\tfrac13\arccos\!\Big(\tfrac25\sqrt{6/5}\Big)\Big]=1.7006. \tag{8}$$

The side-span blind locus ends at $\beta = 2\cos(\pi/9) = 1.8794$, where the end rotation under the uniform load vanishes.

Close to a blind locus a channel is poorly conditioned. A channel is called near-blind when its indicator (Section 2.3) is below 0.2 in magnitude, and the set of such positions or span ratios is the near-blind band. For a mid side-span deflection gauge on three spans the band covers $1.621<\beta<1.775$; Table 1 gives the other bands. Fig. 1 defines the notation, Fig. 2 maps the observability, and Table A.1 gives the optimal side-span positions. All closed forms agree with finite element (FE) evaluations of Eq. (2) (Appendix B).

The strain channel follows from the same end moments; for $(\bar M_l, \bar M_r) = (0, \mu)$ its blind point is $\xi_0$:

$$N_M=\frac{8M_q(x_m)}{q_0L^2}=4\xi(1-\xi)-\bar M_l(1-\xi)-\bar M_r\xi,\qquad \xi_0=1-\frac{\mu}{4}. \tag{9}$$

In the instrumented span of two equal spans the strain blind point is $\xi_0 = 0.75$. Strain blind points exist in every span that has a sagging zone ($\mu<4$), so every continuous girder has them, whatever its span ratios. Table 1 gives the blind point in the main span.

Each strain blind point is surrounded by a near-blind band, $|N_M|<0.2$. For two equal spans the band lies 0.19–0.32 of the span from the interior support. A gauge at the support section itself is well conditioned, with $|N_M| = \mu$. A gauge set back from the pier to clear the diaphragm, or placed at a quarter point, can fall into the band. Table 1 collects the blind loci of all channels, and Fig. 3 shows the indicators along two prismatic girders.

**Table 1.** Blind loci of response channels, that is, positions or span ratios at which the integral constant $C$ of Eq. (2) vanishes. Prismatic beams with $\gamma = 1$ unless stated; $\mu$ from Eq. (4). Near-blind band: indicator below 0.2 in magnitude.

| Channel | Blind where | Two-span beam (span 1) | Symmetric three-span beam |
|---|---|---|---|
| Strain, moment, curvature | zeros of $M_q$ | $\xi_0 = 1-\mu/4$ (0.75 at $\lambda = 1$); band $0.676<\xi<0.812$ at $\lambda = 1$ | side: $\xi_0 = 1-\mu/4$; main: $\zeta_0=\tfrac12(1-\sqrt{1-\mu/\beta^2})$ from the pier (0.276 at $\beta = 1$) |
| Deflection | zeros of the uniform-load deflection $w_q$ | $\mu = \mu_\mathrm{crit}(\xi)$, only for $1<\mu<2$; mid-span: $\lambda = 1.4574$, band $1.385<\lambda<1.525$ | mid side span: $\beta = 1.7006$, band $1.621<\beta<1.775$; locus ends at $\beta = 1.8794$ |
| Rotation | extrema of $w_q$ | end: $\mu = 2$ ($\lambda = 1.6180$); pier: $\lambda = 1$ for any $\gamma$ | end: $\beta = 2\cos(\pi/9)$; pier: $\beta = \sqrt{3/2}$ for any $\gamma$; mid main span: always |
| Shear | maxima of $M_q$ | $\xi = \xi_0/2$ | side: $\xi_0/2$; mid main span: always |
| End reaction | no sagging zone in the end span | $\mu = 4$ ($\lambda = 2.3028$) | $\mu = 4$ ($\beta = 2.6691$) |
| Interior reaction | never under a full uniform load | – | – |

One identity in Table 1 is useful in practice. The end-reaction indicator $N_F = 2F_A/(q_0L_1)$ equals the strain blind abscissa, $N_F = \xi_0$, for any $EI(x)$ and any pier springs, because statics of the end segment gives $M_q = F_Ax - q_0x^2/2$.

### 2.3. Observability and conditioning indicators

Every estimator below divides by $C$, so to first order the sensitivity to measurement error scales as $1/|C|$. Normalised indicators make this sensitivity comparable between channels. For a deflection channel the indicator is

$$N_w=\frac{192EI_\mathrm{ref}\,C_m}{L^4}, \tag{10}$$

with $L$ the span containing the sensor and $EI_\mathrm{ref}$ a reference rigidity. With this normalisation $N_w$ equals 2.5 at mid-span of a simply supported span. $N_M$ of Eq. (9), and the rotation and shear indicators of Appendix B, equal 1 for the same simply supported reference.

Because the two references differ, a common threshold of 0.2 means different things for the two channels: relative to the simply supported mid-span value, it is 8 % for deflection and 20 % for strain. Both thresholds are design conventions and are used as stated throughout.

For a non-prismatic girder, $N_w$ also depends on the choice of $EI_\mathrm{ref}$, and Section 5 shows that this choice can dominate the result. $N_M$ needs no reference rigidity: it is the uniform-load moment relative to the simple-span moment $q_0L^2/8$, so its threshold keeps one meaning for any $EI(x)$. The section enters a strain channel only through the gain $c/EI$ of Eq. (3).

A second measure that needs no reference rigidity is the cancellation ratio

$$R=\frac{C}{A^+}=1-\frac{|A^-|}{A^+}, \tag{11}$$

the net influence area divided by its positive part. $R$ equals 1 for a simply supported span and 0 at a blind configuration. A small indicator with $R$ near 1 therefore indicates restraint, not cancellation. The strain influence line is more local than the deflection line, so it cancels less at every prismatic location examined: at mid-span of two equal spans, $R_\varepsilon = 0.667$ against $R_w = 0.571$.

Neither indicator carries the absolute signal level, on which the offset error depends. Suppose that a residual offset $\delta_0$, in the units of the channel, remains after the record has been re-zeroed before and after the crossing. It adds $\delta_0L_\mathrm{tot}$ to the integral, and with $J = CP$ the relative bias $b$ of the load is

$$b=\frac{P_\delta}{P},\qquad P_\delta=\frac{\delta_0L_\mathrm{tot}}{C}. \tag{12}$$

The offset-equivalent load $P_\delta$ is the load at which the offset causes a 100 % bias. It combines sensor position, baseline stability and the lightest vehicle to be screened into one number.

### 2.4. Multi-channel estimation and sensor placement

Let channel $j$, a deflection or a strain, give the integral $J_j = C_jP + \delta_{0,j}L_\mathrm{tot} + n_j$, with white noise $n_j$ and offsets that may be correlated between channels. Let $\Sigma$ be the covariance matrix of the vector $J$. A linear estimator $\hat P = a^\top J$, with channel weights $a$, is unbiased for every axle configuration if and only if $a^\top C = 1$. Minimising its variance under this constraint gives the GLS weights

$$a^\star=\frac{\Sigma^{-1}C}{C^\top\Sigma^{-1}C},\qquad \mathrm{Var}\,\hat P^\star=\big(C^\top\Sigma^{-1}C\big)^{-1}, \tag{13}$$

the Gauss–Markov best linear unbiased estimator. For one channel, Eq. (13) returns $\hat P = J/C$ with variance $\sigma_{P,\mathrm{noise}}^2 + P_\delta^2$.

Could a non-uniform weighting function $g(x)$ along a single record do better than the plain integral? Appendix B shows that it cannot: only a uniform $g$ keeps the estimate independent of the axle configuration for every structure, and SLM relies on this invariance. It also links SLM to transmissibility-based weighing [34]: a transmissibility is a ratio of response spectra, and at zero frequency it equals the ratio of record integrals. A record integrated uniformly in time weights space by $1/v(x)$, so the integral must be taken in space.

Adding the constraint $\sum_ja_j = 0$ within each channel type makes $\hat P$ insensitive to any disturbance shared by the channels: a constant offset, a drift, or motion of the reference frame. This estimator is called the zero-sum estimator below. With equal noise and offset statistics in all channels, its variance is

$$\mathrm{Var}\,\hat P_\mathrm{zs}=\frac{\sigma^2\Delta x\,L_\mathrm{tot}+(1-\rho)\delta_0^2L_\mathrm{tot}^2}{\sum_j(C_j-\bar C)^2}, \tag{14}$$

where $\rho$ is the common-mode fraction of the offset and $\Delta x$ the sampling interval.

For two channels the zero-sum weights are $a = (1,-1)/(C_1-C_2)$, and a second sensor over a support ($C_2 = 0$) gives the familiar differential measurement against a reference. The white-noise variance then rises by the factor $2C_1^2/(C_1-C_2)^2$, which is 1.65–2.0 on the beams studied. This price is small, because for the long-span parameters of Section 5.3 with $\Delta x = 0.1$ m the white-noise term of Eq. (14) is only about 5 × 10⁻⁶ of the offset term. Strain and deflection channels need separate zero-sum constraints.

If the noise statistics do not depend on position, $1/\mathrm{Var}$ is a convex quadratic in the vector of constants $C(x_j)$, for both Eqs. (13) and (14). The feasible constants form a box, bounded by the smallest and largest $C(x)$ along the girder, and a convex function on a box attains its maximum at a vertex. Optimal sensors therefore lie at the maximum and the minimum of $C(x)$. For deflection, $C(x)$ is $w_q(x)/q_0$. For strain it is $c\,M_q(x)/(EI\,q_0)$, which includes the section gain, so on a haunched girder the extremes of $C_\varepsilon$ and of $M_q$ differ.

Which extreme to use depends on the offsets. With independent offsets, every sensor should sit as close as possible to the maximum, because the GLS variance then falls with the sum of the squared constants. With correlated offsets, one sensor should sit at the minimum, because a common offset cancels in the difference of two channels and the variance of Eq. (14) falls with the spread of the constants. A brute-force search found no design better than this vertex design, and a Monte Carlo study confirmed that the estimators are unbiased and that Eqs. (13) and (14) hold to within 0.6 % (Supplementary Material). Fig. 4 shows the gain over the best single sensor.

These results hold for the assumed noise model, and Section 4.3 shows that real records can violate it. The zero-sum estimator helps only if the disturbance is common-mode during the crossings themselves, not merely in vehicle-free periods. On the field records the vehicle-free noise was strongly common-mode, but the crossing residuals, that is, the deviations of each crossing's integral from its calibrated value, were not. $\Sigma$, and hence $\rho$, should therefore be estimated from the residuals of calibration crossings, with enough crossings to avoid over-fitting, and not from vehicle-free windows alone.

### 2.5. Identifiability of the constant under boundary uncertainty

A girder with monolithic piers has the stiffness matrix $\alpha K_g + kK_p$, where $\alpha$ is the ratio of effective to design girder rigidity and $k$ is the rotational stiffness of each pier. Every static response therefore has the form $f(\kappa)/\alpha$, where $\kappa = k/\alpha$ is the scaled pier stiffness. The ratio of two static readings does not depend on $\alpha$, so only this ratio carries information about $\kappa$. Once $\kappa$ is chosen, either reading gives $\alpha$.

For a mirror-symmetric girder with equal piers, the uniform load excites only the antisymmetric pattern of pier rotations, and the Sherman–Morrison formula gives (Appendix C)

$$C_m(\alpha,\kappa)=\frac{1}{\alpha}\Big[C_\infty+\frac{C_0-C_\infty}{1+\kappa/k_g}\Big]. \tag{15}$$

$C_0$ and $C_\infty$ are the constants for pinned and for fixed piers at $\alpha = 1$, and $k_g$ is the girder's own stiffness against antisymmetric pier rotation. Eq. (15) makes the constant a linear-fractional (Möbius) function of $\kappa$ and is called the Möbius law below.

Two measures follow from Eq. (15). The ratio $C_\infty/C_0$ is the full change of the constant that pier fixity can produce at a gauge. The boundary sensitivity $B_m = |\partial\ln C_m/\partial\ln\kappa|$ is the local slope of this change.

For a symmetric prismatic three-span beam with rotational springs $k$ at the piers, slope-deflection gives, with $\hat k$ the pier stiffness relative to the side-span rigidity,

$$\mu(\hat k)=1+\frac{\beta(2\beta^2-3)}{3\beta+2\gamma+\beta\hat k},\qquad \hat k=\frac{kL_s}{EI_s}. \tag{16}$$

Eq. (16) replaces $\mu_\mathrm{3span}$ in Eq. (5) (FE check in Appendix C). For $\beta = 1.636$, the span ratio of the bridge studied in Section 5, the side-span indicator at $\xi = 0.4$ rises from 0.287 with pinned piers to 1.037 with fixed piers. The mid main-span indicator moves the other way, from 0.755 to 0.500. Rotational restraint thus moves the side-span gauge away from blindness but makes its constant strongly dependent on $k$.

From one static analysis, the theory thus gives the constant of every channel, its blind loci, the optimal placement and its sensitivity to the boundary conditions.

---

## 3. Laboratory verification

This section checks the deflection influence line, the record integral and the two single-channel estimators, BPM and SLM, on a two-span beam. The loads were positioned statically, so the test checks the model and the algorithm, not performance under moving traffic.

The specimen was a steel hollow square tube, 25 mm × 25 mm × 2.03 mm ($I = 16\,530$ mm⁴, $E = 200$ GPa), on three supports forming two equal spans of 2500 mm. The theoretical constant at mid-span of the first span is $C_m = l^4/(192EI) = 61.54$ mm²/N, where $l$ is the span length. Deflection at that point was measured with a linear variable differential transformer of 0.005 mm resolution, while calibrated weights were suspended at 250 mm steps along the traverse.

Three configurations were tested: a single 40.64 N reference load, two loads 250 mm apart, and three loads. For the three-load group, the order of the loads along the beam was not recorded. The order used here is the one that fits the record best, with a root-mean-square residual of 0.030 mm against 0.55 mm for the reverse order. Because the data fixed this order, the three-load result is not a fully independent test. The specimen, the influence line and the data are in the Supplementary Material.

The analytical influence line matched the single-load record within 0.0126 mm, 0.44 % of the peak. On the 250 mm grid the trapezoidal rule underestimates the exact single-load integral by 0.500 %. It is used throughout, because Simpson's rule loses its advantage when the kinks of trailing loads fall inside its panels.

**Table 2.** Identified total loads against direct weighing (trapezoidal rule). BPM: $P = J/C_m$ with the analytical constant; SLM: $P_t = P_0J_t/J_0$ with the single-load record as reference.

| Configuration | Weighed (N) | BPM (N) | BPM deviation | SLM (N) | SLM deviation |
|---|---|---|---|---|---|
| Two loads | 66.99 | 67.73 | +1.10 % | 67.40 | +0.61 % |
| Three loads | 125.08 | 126.57 | +1.19 % | 125.95 | +0.70 % |

Two ratios explain the deviations in Table 2. First, the measured reference integral is 1.0049 times its exact analytical value, and the ratio of the BPM to the SLM estimate equals this factor in both configurations. SLM absorbs the calibration error of the reference record, whereas BPM does not.

Second, the ratio of the measured to the analytical integral, both from the trapezoidal rule, grows with the number of loads: 1.010, 1.016 and 1.017 for one, two and three loads. The SLM deviations of 0.61 % and 0.70 % match the growth of this ratio relative to its one-load value of 1.010. The data cannot tell whether support seating or errors in the stated masses cause it.

Because the configurations differ in both total load and spacing, the test supports the invariance of Eq. (2) only indirectly. The predicted blind configuration (spans of 2500 mm and 3644 mm) was not tested.

---

## 4. Assessment on public moving-truck records

This section asks what integral estimators deliver on real moving-load records from a continuous girder. It reports every channel with 95 % confidence intervals (CIs), tests equivalence instead of stating agreement, and compares single- and multi-channel estimators out of sample.

### 4.1. Data and reference weights

The Nothing-on-Road BWIM (NOR-BWIM) dataset [48] (CC0 licence) contains strain records of the Virginia Smart Road Bridge, documented in [41–43,49]. The bridge is a post-tensioned concrete box girder continuous over five spans of 86.5 + 3 × 144 + 86.5 m = 605 m. Its depth is about 3.8 m at mid-span and 9.5 m at the piers. Strain transducers on the soffit of the top slab lie near mid-span of span 2, 158.5 m from the first abutment, in longitudinal stations about 2 m apart under the wheel path.

Day 1 has 12 channels at 100 Hz, labelled with the prefix "ch". They fall into three groups: four wheel-path gauges with clear axle spikes (ch4, ch5, ch11, ch12), a partner gauge at each of these four stations, and four further gauges without axle spikes (ch1, ch2, ch8, ch9). Day 2 has four in-line channels at 200 Hz, which keep the dataset's labels with the prefix "st" (for example st36 and st40).

The reference weights differ in quality between the days. On day 1, two 3-axle trucks ran in the instrumented lane; their gross weights were reported by the drivers for each pass (21.2–22.8 t for the runs used) [49]. On day 2, a 3-axle truck of 26.8 t and a 5-axle truck of 25.9 t were weighed on a static scale [49]. They ran in the instrumented lane (lane A), on the return trip in the other lane (lane B), and in two in-line two-truck runs.

Errors below are given as a percentage of the gross vehicle weight (GVW). Because the weights vary by only a few per cent within each day, a predictor that always returns the mean calibration weight already has a mean absolute error (MAE) of 2.0 % on day 2 and 2.2 % on day 1. The field data therefore test the scatter and invariance of the integral constant, not the ability to discriminate weights.

Speeds were obtained from the axle spikes and the measured wheelbase; they agree with the speeds computed by the dataset authors' processing script within 1–2 %. For each crossing a linear baseline was fitted to vehicle-free segments before and after the event. The strain was integrated over the whole time the truck was on the bridge plus 5 s at each end, and the result was converted to $\int\varepsilon\,\mathrm{d}x$ with the speed measured at the gauges. Three day-1 runs with two trucks on the bridge and four passes without documented weights were excluded; the same runs are used throughout. The noise of the integral was measured from vehicle-free windows of crossing length, at least 70 s from any detected vehicle. Fig. 5 shows three crossings.

### 4.2. Invariance of the constant and speed

The constant is stable within the noise for most gauges, but invariance between trucks can be shown only within wide margins. On day 1, eight of the twelve gauges have a coefficient of variation of 5.8–13.5 %, and the χ² test accepts consistency with the noise (Table 3). The full table, with every channel and every average, is in the Supplementary Material.

The four gauges without axle spikes fail the invariance test. Their crossing residuals are much larger than the vehicle-free noise (Table 3), and their constant is 22–26 % lower for the second truck, with 95 % CIs of the ratio that exclude 1 (Table 4, Fig. 6a).

**Table 3.** Integral constant $C$ and its scatter over the runs, lane A unless stated. CV expected: coefficient of variation predicted from the measured vehicle-free noise. For ch1, ch2, ch8 and ch9 the residual variance is 2.9–5.1 times the vehicle-free noise variance.

| Day, channel | Runs | $C$ (µε m/t), 95 % CI | CV observed (%) | CV expected (%) | χ² p |
|---|---|---|---|---|---|
| 1, ch11 (best) | 7 | −5.85 (−6.17, −5.53) | 5.8 | 6.8 | 0.60 |
| 1, gauge average (4 wheel-path gauges) | 7 | −4.03 (−4.24, −3.82) | 5.6 | 6.1 | 0.53 |
| 1, ch1, ch2, ch8, ch9 | 7 | −1.49 to −2.38 | 17.2–19.1 | 7.8–11.0 | ≤ 0.012 |
| 2, st36 | 8 | −5.97 (−6.57, −5.38) | 12.0 | 16.5 | 0.73 |
| 2, gauge average (4 gauges) | 8 | −4.12 (−4.62, −3.63) | 14.4 | 20.2 | 0.79 |
| 2, lane B, average | 8 | −3.27 (−4.19, −2.35) | 33.7 | 23.2 | 0.027 |

On day 1 only one gauge, ch11, shows that the two trucks give the same constant within ±10 %. For the average of the four wheel-path gauges the smallest margin that can be shown is ±11.8 % (Table 4).

**Table 4.** Ratio of the integral constants of two trucks, lane A unless stated. Day 1: second to first truck, both 3-axle; day 2: 5-axle to 3-axle truck. Equivalence by two one-sided tests (TOST) at the 5 % level: the 90 % CI of the ratio lies inside the stated margin (for ch11, 0.904–1.098), so a 95 % CI can extend beyond a margin that is shown.

| Day, channel | Ratio (95 % CI) | Equivalence |
|---|---|---|
| 1, ch11 (best) | 0.996 (0.874–1.136) | shown within ±10 % |
| 1, gauge average (4 wheel-path gauges) | 0.955 (0.863–1.057) | shown only within ±11.8 % |
| 1, ch1, ch2, ch8, ch9 | 0.740–0.783 | invariance rejected (CIs exclude 1) |
| 2, st36 | 1.005 (0.735–1.375) | not shown |
| 2, gauge average (4 gauges) | 0.978 (0.697–1.374) | shown only within ±26.7 % |
| 2, lane B, average | 0.749 (0.440–1.276) | – (constants fail the χ² test, Table 3) |

On day 2 the constant does not depend detectably on the axle configuration, but the test is coarse. The ratio of the gauge-average constants of the 5-axle and the 3-axle truck is 0.98 (95 % CI 0.70–1.37). The result is consistent with Eq. (2), but with eight runs it cannot exclude differences of up to about 27 %. It is therefore a coarse check of linearity and processing, not a sharp test of the identity. In lane B the constants fail the χ² test (Table 3).

On day 1, speed and truck are almost perfectly confounded, with a correlation of 0.98. The first truck ran at 10.4–12.8 m/s and the second at 19.1–19.8 m/s. The 22–26 % difference of the gauges without axle spikes may reflect a different transverse wheel path, local deck action or speed; the data cannot separate them.

On day 2 speed and truck are not confounded (13–28 m/s). No speed effect was resolved, but the confidence interval of the slope is too wide to call the constant speed-independent (Section 6; Supplementary Fig. S2).

### 4.3. Single- and multi-channel estimators out of sample

Combining gauges did not help on these records: on day 2 GLS was significantly worse than the gauge average. To test Section 2.4, the covariance of the integrated noise was measured from vehicle-free windows of crossing length (Table 5). On day 2 the four channels are strongly common-mode, with a mean correlation of 0.92, but their noise amplitudes are unequal (13.7–32.8 µε m at the median speed). On day 1 the mean correlation is only 0.42 (Supplementary Fig. S1).

**Table 5.** Correlation between gauges of the integrated strain: means over gauge pairs, with 95 % bootstrap CIs in brackets. Vehicle-free windows: 1227 on day 2 and 3405 on day 1. Crossing residual: deviation of a crossing's integral from its calibrated value. –: not computed.

| Correlation of | Day 2, 4 gauges | Day 1, 12 gauges |
|---|---|---|
| vehicle-free noise, non-overlapping windows | 0.92 (0.83–0.96) | 0.42 (0.26–0.54) |
| vehicle-free noise, window length of each crossing | 0.90 | – |
| crossing residuals | 0.63 | – |
| crossing residuals, st40 with its neighbours | 0.30–0.37 | – |

Four kinds of estimator were compared by leave-one-run-out cross-validation: single gauges, the gauge average, GLS (Eq. 13) and the zero-sum estimator (Eq. 14). In each fold the constants were calibrated without the test run, and $\Sigma$ was estimated from vehicle-free windows only. Leave-one-truck-out (LOTO) results, calibrated on one truck and tested on the other, are given as well (Table 6, Fig. 7).

**Table 6.** Mean absolute error of the gross weight (% of GVW), out of sample, with 95 % bootstrap CIs over the test runs (n = 8 on day 2, n = 7 on day 1). LOTO: calibrated on one truck, tested on the other.

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

On day 2, GLS with the measured covariance was worse than the gauge average: 20.4 % against 11.9 % MAE (Table 6). The paired difference is +8.5 points (95 % CI +2.3 to +15.1), so GLS and the zero-sum estimator are both significantly worse than the average. The vehicle-free noise model had predicted the opposite order (Table 7). On day 1 the estimators cannot be told apart. On both days every estimator is worse than the mean-weight predictor.

The failure on day 2 is itself a finding: crossing residuals are much less correlated between gauges than the vehicle-free noise, 0.63 against 0.90 at the same window length (Table 5). With the covariance of the crossing residuals, the predicted order reverses, and GLS is expected to be worse than the average, as observed (Table 7).

**Table 7.** Day 2: per-crossing standard deviation (SD) of the gross weight predicted by two covariance models, and the observed error (% of GVW). SD and MAE are different measures; the table compares the order of the two estimators, not magnitudes.

| Quantity | GLS, measured $\Sigma$ | Gauge average |
|---|---|---|
| SD predicted from the vehicle-free covariance | 12.7 | 19.8 |
| SD predicted from the covariance of the crossing residuals | 21.0 | 14.6 |
| Observed MAE, leave-one-run-out (Table 6) | 20.4 | 11.9 |

The common-mode wander measured in vehicle-free periods is real, but each crossing also carries a gauge-specific component, plausibly from the wheel path and local slab action. GLS amplifies this component, because it gives st40 and st36 large weights of opposite sign (+0.16 and −0.35).

Estimating $\Sigma$ from the crossing residuals instead of vehicle-free windows over-fits with only eight runs (Supplementary Material). As anticipated in Section 2.4, the zero-sum estimator helps only when the disturbance is common-mode during the crossings themselves.

### 4.4. Lane, superposition and the limits of a beam model

Each lane needs its own constant. For the gauge average, return trips in the other lane gave constants 0.79 times those of lane A (95 % CI 0.59–1.00). The lane effect is clearly resolved for one gauge only (st36: 0.64, 95 % CI 0.47–0.81). The same need was found on another continuous girder [40].

The two in-line two-truck runs are consistent with superposition, although both fall below the prediction. For the gauge average each gave 0.92 of the summed single-truck predictions (pooled 95 % CI 0.77–1.06); the GLS combination gave 0.82.

Gauges within 6 m of each other along the girder have very different constants. On day 1 the constant of ch11 is 3.9 times that of ch8, and their 95 % CIs do not overlap (Table 3), whereas a one-dimensional beam model predicts ratios of 0.978–1.003.

Gauge-factor spread is unlikely to explain these differences, because the ratio of the st36 and st40 constants changes with the lane: 3.24 ± 0.56 in lane A against 1.82 ± 0.10 in lane B (± one standard error), about 2.5 standard errors apart. The deck-soffit gauges respond to slab bending and shear lag as well as to girder bending. The constant must therefore come from a weighed reference vehicle or a three-dimensional model; a beam-model BPM would fail.

A beam model of the girder (Euler–Bernoulli, parabolic haunch, second moment proportional to $h^2$) reproduces the global shape of the strain history ($r^2$ = 0.79–0.94). The gauges are not blind: the zeros of the uniform-load moment diagram in span 2 lie at 121.6 m and 190.8 m, about 35 m from the gauges.

The same model shows why the whole 605 m crossing must be integrated. The cancellation ratio $R$ of the gauges' influence line is 0.51: span 2 contributes about 170 % of the net integral, and the adjacent spans −26 % and −66 %.

### 4.5. What the field records show

The records support linearity, superposition and per-gauge invariance within the 10–27 % that the noise allows, and they show that each lane, and each deck gauge, needs its own constant. They cannot show weight discrimination, because the reference weights hardly vary. They show no benefit from GLS or zero-sum combinations, because the common-mode assumption behind Eq. (14) holds for vehicle-free noise but not for crossing residuals.

The tests rest on four trucks, two axle counts and seven or eight runs per day. The gauge calibration factors and exact positions are not published, so absolute constants cannot be checked. The GVW accuracy that the dataset authors reported for their influence-line system on this bridge [41–43] was not compared [NEED VALUE: GVW accuracy reported in [41–43] for the same runs, if the authors wish to add it].

---

## 5. In-service box girder: identifiability and channel design

This section applies the criteria to an in-service three-span box girder with static acceptance-test data. It asks how far the data determine the observability of each installed gauge, which channel and position would be robust, and which measurement would decide between the models that fit the data.

### 5.1. Bridge, data and model

The Cầu Mây Bridge carries provincial road DT389 over the Kinh Môn River in Hải Dương, Viet Nam. Its main bridge is a three-span continuous prestressed concrete box girder of 55 + 90 + 55 m, built by balanced cantilever ($\beta = 1.636$). The depth varies from 2.40 m at mid-span to 5.40 m at the piers; the design section properties are in the Supplementary Material. The inner piers, including pier T7, are monolithic with the girder, and the end supports T5 and T8 carry pot bearings.

Two deflection gauges were read: N8 at 0.4L of the side span between pier T7 and end support T8, and N7 at mid main span. In the June 2020 acceptance test, four trucks stood in the side span (gauge N8) and six in the main span (gauge N7). The trucks were 3-axle, nominally 5 + 10 + 10 t, with a weighed mean of 25.06 t. Dial gauges read the peak deflection under centric and eccentric transverse positions [NEED VALUE: instrument type and fixed reference datum of the dial gauges, temperature correction, load-hold time and zero-reading procedure]. Each gauge has six readings (three lines, each centric and eccentric); their mean is 5.55 mm at N8 and 15.42 mm at N7.

The girder was modelled with Euler–Bernoulli elements, a parabolic depth variation over $L_v = 44$ m from each inner pier, a second moment proportional to $h^{2.943}$ fitted to the two design sections, and a rotational spring $k$ at each inner pier. The depth law and the pier dimensions are not documented, so other depth lengths and exponents and a rigid pier zone were tested as model-form variants (Supplementary Material).

Two reference calibrations are used. Calibration A is the design model, with $\alpha = 1$ and $k = 2.75\times10^7$ kN m/rad fitted to the designer's FE output; it misfits the measurements by +2.4 % at N8 and +12.3 % at N7. Calibration B is the joint least-squares fit to the two readings, with $\alpha = 0.716$ and $k = 1.2\times10^8$ kN m/rad; its misfits are −2.8 % and +2.9 %. In terms of the scaled pier stiffness, calibration A lies at $\kappa = 2.75\times10^7$ kN m/rad and calibration B at $\kappa = 1.68\times10^8$ kN m/rad. Fig. 8 shows the indicators along the girder for the prismatic model and both calibrations.

### 5.2. What the static data identify

The static data leave the constant of the side-span gauge N8 uncertain by a factor of 6.6, whereas the constant of the centre-span gauge N7 is well determined. Two facts explain this: a model-form misfit that no pier stiffness removes, and the Möbius law of Eq. (15).

No pier stiffness lets the beam model fit both static readings exactly. The test quantity is $r_{87}$, the measured-to-model ratio at N8 divided by that at N7; $r_{87} = 1$ would mean that one model fits both gauges. It never reaches 1 (Fig. 9a). Its minimum, 1.058, lies at calibration B.

The model-form variants move this minimum between 1.039 and 1.092 but never to 1, so the 4–9 % residual is model-form error. Calibration B is therefore the nearest fit, not an exact one, and its $\alpha = 0.716$ would mean a 28 % loss of rigidity in a young prestressed girder.

The admissible set contains every model whose misfit at each gauge stays within a tolerance $\tau$. The six readings of each gauge spread by 1.9–2.0 % about their mean. This spread comes from the transverse positions and is not a repeatability, because the readings are not replicates. Combined in quadrature with a model-form spread of 1.75 %, it gives a standard uncertainty of 2.64 % per reading, and $\tau = 5.3$ % at two standard deviations.

At this tolerance the static data bound $\kappa$ only from below: every $\kappa \ge 1.8\times10^7$ kN m/rad is admissible, with $\alpha$ between 0.51 and 1.15. The conclusion depends on the tolerance. At $\tau = 3$ % the admissible set shrinks and excludes the design rigidity, $\alpha = 1$ (Supplementary Material).

Over the admissible set, the absolute constant $C_8$ ranges from 3.0 × 10⁻⁵ to 2.0 × 10⁻⁴ m²/kN, whereas $C_7$ stays within 3.3–5.0 × 10⁻⁴ m²/kN. The deflection indicators show the same contrast: with the design rigidity as reference, N8 spans 0.124–0.822 and N7 only 0.190–0.286 (Table 8).

**Table 8.** Deflection indicator $N_w$ of the Cầu Mây gauges, Eq. (10), with $EI_\mathrm{ref}$ = design $EI_\mathrm{mid}$ and $L$ the span containing the gauge. Calibration A and the pinned-pier and fixed-pier rows have $\alpha = 1$, calibration B has $\alpha = 0.716$, and the admissible set spans $\alpha$ = 0.51–1.15; the pinned-pier and fixed-pier rows give the extreme values over all model-form variants. –: not computed.

| Model | N8, 0.4L (installed) | N8 at mid side span | N7, mid main span (installed) |
|---|---|---|---|
| Prismatic beam, pinned piers | 0.287 | 0.163 | 0.755 |
| Haunched, calibration A | 0.181 | 0.105 | 0.209 |
| Haunched, calibration B | 0.476ᵃ | 0.377 | 0.234 |
| Haunched, admissible set ($\tau$ = 5.3 %) | 0.124–0.822ᵇ | – | 0.190–0.286 |
| Haunched, pinned piers | 0.023 | −0.066 | 0.263 |
| Haunched, fixed piers | 0.446 | 0.375 | 0.145 |

ᵃ Above the fixed-pier value because calibration B has $\alpha$ = 0.716; normalised by the effective rigidity $\alpha EI_\mathrm{mid}$ it is 0.341. ᵇ The upper part of this range requires $\alpha \approx 0.5$; normalised by the effective rigidity, the range is 0.144–0.422.

The Möbius law of Eq. (15) explains the asymmetry. Going from pinned to fixed piers multiplies the N8 constant by 14.0 but reduces the N7 constant to 0.59 of its pinned value. The design stiffness sits at $\kappa/k_g = 0.63$, near the steepest part of the curve, where the boundary sensitivity $B_m$ is much larger at N8 than at N7 (Table 9).

Calibrating the model to the N8 reading does not fix the N8 constant either. Over the admissible set, the ratio of $C_m$ to the modelled N8 deflection varies by a factor of 6.5, against 1.5 for N7.

**Table 9.** Cancellation ratio $R$, Eq. (11), and boundary sensitivity $B_m$ of the Cầu Mây gauges. $B_m$ at the design stiffness, with $k_g = 4.36\times10^7$ kN m/rad. –: not computed.

| Quantity | N8, 0.4L (installed) | N8 at mid side span | N7, mid main span (installed) |
|---|---|---|---|
| $R$, prismatic beam, pinned piers | 0.14 | 0.08 | 0.70 |
| $R$, calibration A | 0.18 | 0.11 | 0.59 |
| $R$, calibration B | 0.56 | 0.49 | 0.77 |
| $R$, admissible set | 0.13–1.00 | – | 0.56–1.00 |
| $B_m$ | 0.51 | – | 0.12 |

The centre-span indicator is low (0.19–0.29) although $R$ is 0.56–1.00, so its smallness reflects restraint by the haunches, not cancellation. The measured vertical frequencies (3.43–3.64 Hz) would narrow the admissible set further if they belonged to the third vertical mode. This interpretation is conditional and is analysed in the Supplementary Material.

### 5.3. Which channel, where

For this girder the deflection channel at mid main span is the robust choice. A side-span deflection gauge is ill-conditioned with respect to pier stiffness and should not take its constant from a design model unless that stiffness is identified.

Strain channels behave differently (Fig. 8). The haunches move every zero-moment point towards mid-span. Over the range of pier stiffness the side-span zero lies 26.0–33.3 m from the abutment, so a strain gauge at mid side span would be practically blind under calibration A ($N_M = 0.048$) and would change sign with pinned piers. The centre of the main span lies in the strain near-blind band in every haunched model ($N_M$ = 0.163–0.212 at N7), again because of restraint ($R_\varepsilon$ = 0.65–1).

Judged by $N_M$ alone, the best-conditioned strain locations are 5–10 m from the piers, where $|N_M| \ge 0.39$ in all haunched models. The placement rule, however, ranks locations by the absolute constant $C_\varepsilon = cM_q/(EI\,q_0)$, which includes the section gain. With $c\propto h$, the gain $c/EI$ at those locations is about one fifth of that at mid-span (Fig. 8c). The two rankings therefore disagree (Figs. 8b and 8c), and which one governs depends on whether the noise is set by the strain resolution or by the offset.

Load cells under the end bearings give an end-reaction indicator $N_F = \xi_0$ = 0.47–0.61. They cannot be blind unless the side span loses its sagging zone.

For two deflection channels, Section 2.4 places the second sensor at the most negative constant, in the side span 4–10 m from the inner pier. The pair at 100 m and 152 m from the end support T5 is within 0.9 % of the calibration-specific optimum under both A and B, so placement is insensitive to the unresolved pier stiffness.

Under the assumed noise model, a second gauge reduces the scatter of the load. The placement study assumed $\sigma = 0.01$ mm, $\delta_0 = 0.1$ mm and a record of 220 m (the 200 m unit plus a 20 m convoy allowance). At $\rho = 0.9$ and under calibration A, the standard deviation of the load falls from 24.8 % with N7 alone to 10.6 % with the pair; for the 200 m record used in Section 6 the single-gauge value is 22.5 %. The value at $\rho = 1$ would be far smaller, but Section 4.3 shows that a common-mode fraction measured in vehicle-free periods need not hold during crossings, so these gains are upper bounds.

If a model-based constant is wanted, a tiltmeter on the monolithic pier T7 is the most informative additional measurement; under the side-span convoy it would read about 167 µrad. Its benefit is measured by the Cramér–Rao bound on the standard deviation of $\ln C_8$. The bound is evaluated at the scaled pier stiffness of calibration A, $\kappa = 2.75\times10^7$ kN m/rad, with $\alpha$ refitted to the two readings at that $\kappa$ ($\alpha^* = 1.07$; the curve $\alpha^*(\kappa)$ of best static fit is shown in Fig. 9b). Each static reading has the standard uncertainty of 2.64 % derived in Section 5.2, and the rotation an assumed 3 %.

At calibration A the two deflections alone give a bound of 0.87. Adding the tiltmeter reduces it to 0.18; adding the identified first and third vertical frequencies instead reduces it to 0.24. At calibration B the two-reading Fisher matrix is singular, so the deflections alone cannot bound $\ln C_8$, and with the tiltmeter the bound is 0.04. A rotation reading at the end bearing T8 adds little, because its sensitivity duplicates that of N8.

A moving-load test with weighed trucks has been designed for this bridge, and Table 10 gives the predicted values that would decide between the reference calibrations. These are predictions, not results. The ratio of integrals at the side-span and centre-span deflection gauges is independent of truck weight and absolute rigidity, and it differs by a factor of 2.3 between calibrations A and B.

**Table 10.** Predicted discriminating measurements at Cầu Mây for a 25 t 3-axle truck (not measured).

| Measured quantity | Calibration A | Calibration B |
|---|---|---|
| Integral ratio, N8 at 0.4L / N7 at mid-span | 0.121 | 0.284 |
| Peak girder rotation over pier T7 (µrad) | −58 | −29 |
| Strain integral at the zero-moment point of A (171.3 m) / at gauge N7 (mid main span) | 0.006 | 0.17 |

The in-service girder shows that a side-span deflection gauge on a layout near the prismatic blind locus is not identifiable from static acceptance data, whereas a centre-span gauge is. One tiltmeter or one integral ratio would discriminate between the reference calibrations.

---

## 6. Error budget

This section states the error terms of the integral estimator with their sensitivities and the values measured or assumed in this paper (Table 12). The budget is indicative, not an evaluation according to the Guide to the Expression of Uncertainty in Measurement (GUM): several entries are scenario ranges and the correlations between terms are not quantified.

To first order, the relative error of BPM is the sum of the relative errors of the rigidity, the gain, the speed and the offset term of Eq. (12), plus four times the relative error of the span length. SLM removes the structural terms, because they belong to $C$. Every other term survives as the difference between the target and the reference crossings.

Speed enters twice. It affects the response itself, and it enters again through its measurement, because the space integral is the time integral times the speed measured at the gauges; a speed error therefore passes one-to-one into the weight. Speed variation over a 605 m crossing was not measured.

For a constant force moving across the laboratory beam, the quasi-static error is at most about 1 % when the ratio of the crossing time to the fundamental period, $t_\mathrm{cr}/T_1$, is at least 8, and it exceeds 15 % below 2.5 [50]. This bound omits vehicle–bridge interaction and road roughness.

Table 11 evaluates Eq. (12) for the Cầu Mây gauges over the admissible set, with $L_\mathrm{tot} = 200$ m and the mean weighed truck of 25.06 t. The smaller offsets in Table 11 are typical of displacement transducers. Absolute deflection on a 90 m span over water would usually come from a non-contact technique, whose residual offset after re-zeroing has to be established on site, since environmental effects act over the same window [51,52].

The authors' deflection records from two simply supported bridges (Supplementary Material) showed post-minus-pre level differences of up to 0.23 mm. Linear re-zeroing removes such differences, so this value bounds the drift before re-zeroing, not $\delta_0$.

**Table 11.** Bias of a single-channel estimate caused by a residual offset $\delta_0$, Eq. (12), for a 25.06 t truck; $L_\mathrm{tot}$ = 200 m. Ranges over the admissible set ($\tau$ = 5.3 %).

| Gauge | $C$ (m²/kN) | 0.02 mm | 0.05 mm | 0.1 mm | 0.2 mm | 0.5 mm |
|---|---|---|---|---|---|---|
| N7, mid main span | 3.3–5.0 × 10⁻⁴ | 3.3–5.0 % | 8–12 % | 16–25 % | 33–50 % | 82–124 % |
| N8, 0.4L | 3.0–20 × 10⁻⁵ | 8–54 % | 21–136 % | 41–271 % | 82–543 % | 206–1356 % |

At $\delta_0 = 0.1$ mm a single centre-span gauge biases a 25 t truck by 16–25 %, and a single side-span gauge by 41–271 %. With present absolute-deflection technology, single-point integral weighing on a long-span girder is therefore marginal even at the best location. The zero-sum pair addresses this term only to the extent that the offset is common-mode during crossings (Section 4.3).

Transverse position and multiple presence add further terms. On the five-span girder the far-lane constant was 0.79 of the near-lane value. At Cầu Mây the readings across one section spread by up to 2.05 mm in the eccentric N7 case, about 13 % of the mean reading.

Several vehicles on the structure return their combined weight; on the five-span girder the two-truck events gave 0.92 of the prediction. A crossing of the 200 m Cầu Mây unit takes 12.4 s at 60 km/h, and every crossing that overlaps another vehicle in that window must be discarded or treated as a group. The fraction of usable isolated crossings was not quantified.

**Table 12.** Indicative sensitivity budget of the integral estimator. Values are those measured or assumed in this paper; they are not combined.

| Term | Sensitivity | Cancels in SLM? | Value in this paper |
|---|---|---|---|
| Flexural rigidity $EI$ | 1 | yes | BPM only; Cầu Mây N8 constant varies 6.6-fold over the admissible set |
| Span length | 4 | yes | BPM only |
| Gain | 1 | if not recalibrated between crossings | not evaluated |
| Reference weighing $P_0$ | 1 | no | laboratory: accuracy class [NEED VALUE]; field: day-1 weights driver-reported |
| Residual offset, drift $\delta_0$ | $L_\mathrm{tot}/J$ per unit offset | only if common-mode during crossings | Table 11; field per-crossing SD of the gauge average predicted 19.8 % (day 2), 5.3 % (day 1) |
| Speed effect | 1 | no | day 2: +6 % per 10 m/s (95 % CI −23 to +35 %), not resolved |
| Speed measurement | 1 | no | not evaluated beyond 1–2 % agreement with the dataset speeds |
| Dynamics | 1 | partly | ≤ 1 % for $t_\mathrm{cr}/T_1 \ge 8$ (constant force) |
| Transverse position | lane-dependent $C$ | no, unless lane-specific | field lane ratio 0.79; Cầu Mây spread 2.05 mm |
| Multiple presence | group weight | – | two-truck events 0.92 of prediction |
| Linearity, seating | 1 | no | laboratory step 1.010 → 1.017 |

In the laboratory, the reference record and the load-dependent step limit SLM to 0.6–0.7 %. In the field, the noise, the lane and the gauge position dominate, and the weight errors of single crossings, 5–12 % on these records, exceed the spread of the reference weights.

The method is therefore proposed for preliminary overload screening, with the decision threshold set apart from the legal limit and the design live loads [53,54]. Setting that threshold needs field calibration with trucks of clearly different weights, which this study did not have.

---

## 7. Design workflow and limitations

The results combine into a procedure for designing load-monitoring channels on a continuous girder before installation.

1. **Constants.** For each candidate channel and position, compute $C$ from one static analysis under a uniform unit load on each lane, Eq. (2). Use Eqs. (4)–(9) for prismatic two- and three-span beams.
2. **Blindness.** Locate the blind loci of Table 1. Keep strain gauges out of the near-blind band $|N_M|<0.2$ around every zero-moment point, including gauges set back from a pier. Keep deflection gauges out of the near-blind bands $|N_w|<0.2$, for example $1.385<\lambda<1.525$ for a mid-span gauge on two spans and $1.621<\beta<1.775$ for a mid side-span gauge on three spans.
3. **Conditioning.** Report $N_M$ for strain, $N_w$ with its $EI_\mathrm{ref}$ for deflection (or the absolute constant), and $R$ for both. A small indicator with $R$ near 1 is restraint, not cancellation.
4. **Boundary robustness.** Evaluate $C$ over the plausible range of pier stiffness; for a symmetric girder, Eq. (15) gives the whole curve from the pinned and fixed constants. Avoid locations with large $C_\infty/C_0$ or $B_m$, or plan the measurement that identifies $\kappa$: a tiltmeter on a monolithic pier, an identified first frequency, or an integral ratio between two gauges.
5. **Placement.** Place sensors at the extremes of $C(x)$ of each channel type: $w_q$ for deflection and $cM_q/EI$ for strain.
6. **Estimator.** Use SLM with weighed vehicles of clearly different weights, several reference crossings and lane-specific constants. Combine channels by GLS or zero-sum weights only after estimating $\Sigma$ from the residuals of calibration crossings and checking it out of sample against the gauge average; covariances from vehicle-free windows alone can mislead. Use BPM only where the location is well conditioned and the structure is known; on box girders with deck-mounted gauges, a beam model does not give the constant.
7. **Offset and dynamics.** Evaluate $P_\delta$, Eq. (12), for the residual offset that the instrumentation achieves after re-zeroing, and compare it with the lightest vehicle to be screened. Check $t_\mathrm{cr}/T_1 \ge 8$ with the measured fundamental frequency $f_1 = 1/T_1$.
8. **Processing.** Integrate in space over the complete crossing, re-zero before and after each crossing, remove dynamics with a low-pass filter well below the fundamental frequency $f_1$ and never with a high-pass filter, and discard overlapping crossings.

The integral is a reduced alternative to influence-line BWIM, not a competitor. It returns the gross weight of a vehicle or group from one scalar constant per channel and one weighted sum. Its natural role is low-cost screening across many continuous structures, with instrumented BWIM or enforcement weighing for the vehicles it flags. Influence-line BWIM does not suffer the blindness of Table 1, because it fits the whole record shape.

Several limitations remain. The laboratory beam had equal spans and statically positioned loads, and the blind configuration was not tested. The field assessment rests on one public dataset with four trucks, two axle counts, nearly constant reference weights and no gauge at a zero-moment point; it could not test weight discrimination, the deflection blind loci or a deflection pair. The in-service application uses static data and an Euler–Bernoulli beam model with an assumed depth law and equal pier springs. The treatment is one-dimensional along each lane.

---

## 8. Conclusions

This paper derived design criteria for channels that monitor the total load on continuous girder bridges, building on the classical influence-area identity and on standard GLS estimation.

1. Strain channels are blind at every zero of the uniform-load moment diagram, which every continuous girder has, and a near-blind band surrounds each zero: on two equal spans it lies 0.19–0.32 of the span from the interior support. Deflection channels are blind only near particular span ratios, such as $\lambda = (3+\sqrt{33})/6$ for two spans and $\beta = 1.7006$ for a mid side-span gauge on three symmetric spans.
2. The strain indicator $N_M$ needs no reference stiffness, and the cancellation ratio $R$ separates cancellation from restraint on haunched girders. The deflection indicator equals 2.5, not 1, at mid-span of a simply supported span, so its threshold must be stated with its normalisation.
3. Optimal sensors lie at the extremes of the uniform-load response, for strain at the extremes of $cM_q/EI$. Zero-sum weights remove a common-mode offset exactly. On public field records, however, GLS weights built from vehicle-free noise were worse out of sample than the gauge average (20.4 % against 11.9 % mean absolute error), because crossing residuals were much less correlated between gauges than vehicle-free noise at the same window length (0.63 against 0.90).
4. On those records, the constants were consistent with axle-configuration invariance (5-axle/3-axle ratio 0.98, 95 % CI 0.70–1.37) and with superposition, but the tests could not resolve differences smaller than 10–27 %. Speed was confounded with truck on one day, each lane and each deck gauge needed its own constant, and the reference weights varied too little for any estimator to beat the mean weight.
5. On a 55 + 90 + 55 m box girder, two static readings bound the scaled pier stiffness only from below at a 5.3 % tolerance, leaving the constant of the side-span deflection gauge uncertain by a factor of 6.6, whereas the centre-span gauge is well determined. A pier tiltmeter would reduce the Cramér–Rao bound on $\ln C_8$ from 0.87 to 0.18. A residual offset of 0.1 mm would bias a 25 t truck by 16–25 % even at mid main span.

The next steps are the moving-load test designed for the in-service girder, laboratory tests of the blind configuration, and field calibration with trucks of clearly different weights.

---

## Appendix A. Closed forms for two- and three-span beams

For unequal spans the uniform-load support moment of a two-span beam is $M_B = -q_0(L_1^3/EI_1+L_2^3/EI_2)/[8(L_1/EI_1+L_2/EI_2)]$. Superposing the simply supported uniform-load deflection of span 1 and the deflection due to $M_B$, evaluating at $x_m$ and dividing by $q_0$ gives Eq. (5) with $\mu = -8M_B/(q_0L_1^2)$, which is $\mu_\mathrm{2span}$ of Eq. (4). Because $1-2\xi^2+\xi^3 = (1-\xi)(1+\xi-\xi^2)$, setting $F = 0$ gives Eq. (6). With uniform stiffness, the blind condition for a mid-span sensor is $3\lambda^2-3\lambda-2=0$, and maximising $F$ over $\xi$ at $\mu = 1$ gives $8\xi^2-\xi-1=0$, hence Eq. (7). In units of $L_1^4/(192EI_1)$, the positive contribution of the instrumented span varies only between 1.50 and 2.00 for $\lambda$ from 0.5 to 2.0, whereas the negative contribution of the adjacent span sweeps from −0.125 to −4.00; the degeneracy is driven almost entirely by the adjacent span.

For the symmetric three-span beam the three-moment equation gives $M_B = M_C = -q_0L_s^2\mu/8$ with $\mu_\mathrm{3span}$ of Eq. (4). Three equal spans give $\mu = 4/5$. The optimal side-span position solves $8\xi^3-(12-3\mu)\xi^2+(2-\mu)=0$. The near-blind band at mid side span runs from the root of $30\beta^3-69\beta-16=0$ (1.621) to that of $10\beta^3-27\beta-8=0$ (1.775). A mid main-span deflection sensor is blind at $\beta = 0.9647$. For a sensor at $\zeta = x/L_c$ in the main span, $192EI_cC_m/L_c^4 = 8[\zeta(1-2\zeta^2+\zeta^3)-\nu\zeta(1-\zeta)]$ with $\nu = 3(\gamma+\beta^3)/[\beta^2(2\gamma+3\beta)]$. For $\beta = 1.636$ the strain blind point in the main span lies at $\zeta_0 = 0.177$ from the pier. Asymmetric layouts follow from the three-moment equations (Supplementary Material).

**Table A.1.** Symmetric three-span beam, uniform rigidity: optimal side-span position $\xi^*$ and deflection indicator $N_w$ (Eq. 10; 2.5 for a simply supported mid-span).

| $\beta$ | $\mu$ | $\xi^*$ | $N_w$ at $\xi^*$ | $N_w$ at $\xi = 1/2$ |
|---|---|---|---|---|
| 1.0 | 0.800 | 0.4460 | 1.322 | 1.300 |
| 1.2 | 0.9743 | 0.4251 | 1.076 | 1.039 |
| 1.4 | 1.208 | 0.3875 | 0.7585 | 0.6884 |
| 1.5 | 1.346 | 0.3582 | 0.5807 | 0.4808 |
| 1.636 | 1.558 | 0.2994 | 0.3316 | 0.1632 |
| 1.7 | 1.666 | 0.2608 | 0.2202 | 0.0015 |

## Appendix B. General channels and invariant weighting functions

For a prismatic span with end-moment parameters $\bar M_l$, $\bar M_r$ and $\xi = x/L$, the indicators are $N_w = 8\Phi$ with $\Phi = \xi(1-2\xi^2+\xi^3)-\tfrac{\bar M_l}{2}(2\xi-3\xi^2+\xi^3)-\tfrac{\bar M_r}{2}(\xi-\xi^3)$, $N_\theta = 24EI\,C_\theta/L^3 = \Phi'(\xi)$, $N_M$ of Eq. (9) and $N_V = 2C_V/L = 1-2\xi+(\bar M_l-\bar M_r)/4$. $N_\theta$, $N_M$ and $N_V$ equal 1 for the simply supported reference (end rotation, mid-span moment, end shear). $N_w$ equals 2.5 at a simply supported mid-span and 1 at mid-span of each span of an equal two-span beam. For the two-span beam, $(\bar M_l, \bar M_r) = (0, \mu)$ in span 1 and $(\mu/\lambda^2, 0)$ in span 2; for the symmetric three-span beam, $(0, \mu)$ in the side span and $(\mu/\beta^2, \mu/\beta^2)$ in the main span. Strain zeros solve $4\xi^2-(4+\bar M_l-\bar M_r)\xi+\bar M_l=0$.

All closed forms of Section 2.2 agree with FE evaluations of Eq. (2) in 981 checks, with a maximum error of 8.1 × 10⁻¹¹ on the normalised indicators. The verification covered two-span, symmetric and asymmetric three-span and four-span beams, zero-moment positions, ten blind configurations, the identity for a two-truck convoy on piecewise-prismatic girders with elastic pier springs (relative error 2.8 × 10⁻⁹), and the haunched Cầu Mây FE against an independent force-method solution (5.4 × 10⁻¹⁰). Truncating the record when the first axle leaves changed the integral by up to 59 % (rotation) and 10 % (moment) on the two-span example.

For the most general linear estimator $\hat P = \sum_j\int g_j(x)y_j(x)\,\mathrm{d}x$, with weighting functions $g_j$ along the records $y_j$, the mean is $\sum_aP_ah(s_a)$ with $h(s) = \sum_j\int g_j(x)\eta_j(x-s)\,\mathrm{d}x$. If $h$ must be constant in $s$ for every set of influence lines supported on $[0, L_p]$, then $\int_0^{L_p}[g(u+s)-g(u+s')]\eta(u)\,\mathrm{d}u = 0$ for every admissible $\eta$, so $g(u+s) = g(u+s')$ almost everywhere. Each $g_j$ is therefore constant, and the only freedom lies across channels. When the influence line is known, other invariant weighting functions exist; for two equal spans their white-noise variance is 1.5–6.6 times smaller, but a 20 % stiffness error in the adjacent span then produces configuration-dependent errors of −1.1 % to +2.0 % (Supplementary Material).

## Appendix C. Identifiability: sensitivities and Möbius law

Let $G = K^{-1}$ with $K = \alpha K_g + kK_p$, where $K_p$ has a unit entry on each inner-pier rotational degree of freedom, and $C_m = e_m^\top Gq$ with $q$ the consistent uniform load. Then $\mathrm{d}C_m/\mathrm{d}k = -\sum_i\theta_{m,i}\theta_{q,i}$, where $\theta_{m,i}$ and $\theta_{q,i}$ are the pier rotations under a unit load at the gauge and under the uniform load. The logarithmic sensitivities $S_\alpha = \partial\ln C_m/\partial\ln\alpha$ and $S_k = \partial\ln C_m/\partial\ln k$ satisfy $S_\alpha + S_k = -1$ by Euler's theorem, because $C_m$ is homogeneous of degree −1 in $(\alpha, k)$. Mirror symmetry decouples the symmetric and antisymmetric pier-rotation patterns, the uniform load excites only the antisymmetric one, and the Sherman–Morrison formula gives the linear-fractional (Möbius) law of Eq. (15) with $1/k_g$ the antisymmetric pier flexibility of the girder at $k = 0$. For the Cầu Mây model the law holds to a relative error of 5 × 10⁻⁶ over $k = 10^5$–$10^{12}$ kN m/rad, and Eq. (16) agrees with FE to 4.4 × 10⁻⁷.

With two static readings the Fisher matrix has a determinant proportional to $(S_{y8}-S_{y7})^2$, where $S_{y8}$ and $S_{y7}$ are the logarithmic sensitivities of the N8 and N7 readings to $\kappa$; this determinant vanishes at the minimum of the ratio misfit, that is at calibration B. A frequency adds a row with the mass as nuisance parameter; a pier rotation adds a row without nuisance. Unequal pier stiffnesses would bring in the symmetric pattern, which Eq. (15) does not cover.

---

## Computational Implementation

All analyses were implemented by the authors in reproducible scripts: the closed forms and their FE verification, the multi-channel estimators, placement study and Monte Carlo simulation, the identifiability analysis of the in-service girder, the processing of the public field records and the laboratory evaluation. Generative artificial intelligence was used as an assistance tool during code development and debugging. Every equation and numerical output was checked independently against an analytical, finite element or convergence-based route, and the scripts and the console output of each run are provided as supplementary material.

## Data Availability

The field strain records analysed in Section 4 are publicly available in the NOR-BWIM dataset (figshare, https://doi.org/10.7294/26880898.v1, CC0) [48]. The laboratory deflection data are given in full in the Supplementary Material. The derived data behind every figure and table, the analysis scripts and the console output of each run are provided as supplementary material. The Cầu Mây load test was performed by an author of this paper, and the authors are permitted to publish the processed data (static deflection readings, truck positions, weighed truck masses and reported frequencies), which are available at [NEED VALUE: repository name and DOI].

## Conflicts of Interest

The Cầu Mây load test analysed in Section 5 was performed by the authors' team as part of inspection work carried out by Công ty TNHH Tư vấn Đại học Xây dựng (HUCE consultancy) [NEED VALUE: name(s) of authors involved and nature of relationship]. The authors declare that there is no other conflict of interest regarding the publication of this article.

## Funding Statement

This research did not receive any specific grant from funding agencies in the public, commercial or not-for-profit sectors. [NEED VALUE: name the employer under whose employment the work was performed, and the source of the article processing charge, if any.]

## Author Contributions

**Quoc-Bao Nguyen:** Conceptualization, Methodology, Formal analysis, Software, Writing – original draft. **Thai-Son Vu:** Conceptualization, Investigation, Validation, Supervision, Project administration, Writing – review & editing. **Hung-Son Nguyen:** Investigation, Data curation, Visualization, Writing – review & editing.

## Disclosure of Generative AI Use

During the preparation of this work the authors used Claude (Anthropic) to assist with code development and debugging and with language editing. All scientific formulations, procedures, numerical results and interpretations were independently reviewed and verified by the authors, who take full responsibility for the content of the manuscript.

## Acknowledgments

The authors gratefully acknowledge the Laboratory of Transportation Technology and Systems, Faculty of Bridge and Road Engineering, Hanoi University of Civil Engineering, for providing the test facilities used in this study, and A. Moghadam and R. Sarlo for making the NOR-BWIM dataset publicly available. [NEED VALUE: whether to acknowledge Hai Duong PMU and the testing consultant for access to the acceptance-test report.]

---

## Supplementary Materials

The supplementary material contains: (i) the analysis scripts and the console output of each run, with a README that maps every table and figure to a script and log; (ii) the derived data behind every figure and table; (iii) the laboratory specimen, influence line, quadrature study and full data; (iv) the full per-channel invariance table of the field records (23 channel and average rows, with all χ² p-values), the noise correlation matrices, the speed regressions and all estimator results, including in-sample values, GLS with the covariance estimated from crossing residuals, the predicted per-crossing standard deviation of every estimator, per-channel lane-B results and the confidence interval of the GLS superposition ratio (Figs. S1–S2); (v) the beam model of the five-span girder, including the strain constant of the gauges relative to the largest on the girder, and the synthetic records of the dataset authors (Figs. S3–S4); (vi) strain blind-locus maps (Figs. S5–S6); (vii) the multi-channel placement study (brute-force search over all cases), Monte Carlo verification and structure-aware weighting functions (Figs. S7–S9); (viii) the asymmetric three-span closed forms; (ix) the Cầu Mây design section properties and concrete modulus, the model-form variants (depth lengths, exponents, rigid pier zone), the frequency interpretation, admissible sets against tolerance (3 %, 4 % and 5.3 %, with and without a prior on $\alpha$), the misfit ratio $r_{87}$ over $\kappa$ and the closed-form Möbius law (Figs. S10–S12); (x) the moving-force analysis behind the dynamic bound; (xi) the deflection records of two simply supported bridges, which illustrate baseline handling and low-pass filtering (Figs. S13–S14).

---

## References

[1] Y. Fan, J. Zhu, J. Pei, Z. Li, Analysis for Yangmingtan Bridge collapse, Eng. Fail. Anal. 56 (2015) 20–27. https://doi.org/10.1016/j.engfailanal.2015.05.003

[2] H.M. Salem, H.M. Helmy, Numerical investigation of collapse of the Minnesota I-35W bridge, Eng. Struct. 59 (2014) 635–645. https://doi.org/10.1016/j.engstruct.2013.11.022

[3] M. Morgese, F. Ansari, M. Domaneschi, G.P. Cimellaro, Post-collapse analysis of Morandi's Polcevera viaduct in Genoa, Italy, J. Civ. Struct. Health Monit. 10 (2020) 69–85. https://doi.org/10.1007/s13349-019-00370-7

[4] R. Ventura, B. Barabino, G. Maternini, Estimating the frequency of traffic overloading on road bridges, J. Traffic Transp. Eng. (Engl. Ed.) 11 (4) (2024) 776–796. https://doi.org/10.1016/j.jtte.2023.11.005

[5] J. Gajda, R. Sroka, P. Burnos, M. Daniol, Long-term assessment of the properties of load sensors applied in weigh-in-motion systems, Sensors 25 (8) (2025) 2421. https://doi.org/10.3390/s25082421

[6] I. Al-Qadi, H. Wang, Y. Ouyang, K. Grimmelsman, J.E. Purdy, LTBP Program's Literature Review on Weigh-in-Motion Systems, Report FHWA-HRT-16-024, Federal Highway Administration, Washington, DC, 2016. https://rosap.ntl.bts.gov/view/dot/35735

[7] B. Jacob, E.J. OBrien, S. Jehaes (Eds.), Weigh-in-Motion of Road Vehicles: Final Report of the COST 323 Action, LCPC, Paris, 2002.

[8] F. Moses, Weigh-in-motion system using instrumented bridges, Transp. Eng. J. ASCE 105 (3) (1979) 233–249. https://doi.org/10.1061/TPEJAN.0000783

[9] E.J. OBrien, M.J. Quilligan, R. Karoumi, Calculating an influence line from direct measurements, Proc. Inst. Civ. Eng. Bridge Eng. 159 (1) (2006) 31–34. https://doi.org/10.1680/bren.2006.159.1.31

[10] E.J. OBrien, C.W. Rowley, A. González, M.F. Green, A regularised solution to the bridge weigh-in-motion equations, Int. J. Heavy Veh. Syst. 16 (3) (2009) 310–327. https://doi.org/10.1504/IJHVS.2009.027135

[11] A. Žnidarič, J. Kalin, M. Kreslin, Improved accuracy and robustness of bridge weigh-in-motion systems, Struct. Infrastruct. Eng. 14 (4) (2018) 412–424. https://doi.org/10.1080/15732479.2017.1406958

[12] Y. Yu, C.S. Cai, L. Deng, State-of-the-art review on bridge weigh-in-motion technology, Adv. Struct. Eng. 19 (9) (2016) 1514–1530. https://doi.org/10.1177/1369433216655922

[13] T. Ojio, C. Carey, E.J. OBrien, C. Doherty, S.E. Taylor, Contactless bridge weigh-in-motion, J. Bridge Eng. 21 (7) (2016) 04016032. https://doi.org/10.1061/(ASCE)BE.1943-5592.0000776

[14] W. He, T. Ling, E.J. OBrien, et al., Virtual axle method for bridge weigh-in-motion systems requiring no axle detector, J. Bridge Eng. 24 (9) (2019) 04019086. https://doi.org/10.1061/(asce)be.1943-5592.0001474

[15] Y. Yu, C.S. Cai, L. Deng, Nothing-on-road bridge weigh-in-motion considering the transverse position of the vehicle, Struct. Infrastruct. Eng. 14 (8) (2018) 1108–1122. https://doi.org/10.1080/15732479.2017.1401095

[16] S.S. Law, T.H.T. Chan, Q.H. Zeng, Moving force identification: a time domain method, J. Sound Vib. 201 (1) (1997) 1–22. https://doi.org/10.1006/jsvi.1996.0774

[17] T.H.T. Chan, S.S. Law, T.H. Yung, X.R. Yuan, An interpretive method for moving force identification, J. Sound Vib. 219 (3) (1999) 503–524. https://doi.org/10.1006/jsvi.1998.1904

[18] S.S. Law, X.Q. Zhu, Study on different beam models in moving force identification, J. Sound Vib. 234 (4) (2000) 661–679. https://doi.org/10.1006/jsvi.2000.2867

[19] X.Q. Zhu, S.S. Law, Moving load identification on multi-span continuous bridges with elastic bearings, Mech. Syst. Signal Process. 20 (7) (2006) 1759–1782. https://doi.org/10.1016/j.ymssp.2005.06.004

[20] L. Deng, C.S. Cai, Identification of dynamic vehicular axle loads: theory and simulations, J. Vib. Control 16 (14) (2010) 2167–2194. https://doi.org/10.1177/1077546309351221

[21] Z. Chen, Y. Fang, X. Kong, L. Deng, Identification of multi-axle vehicle loads on beam type bridge based on minimal residual norm steepest descent method, J. Sound Vib. 563 (2023) 117866. https://doi.org/10.1016/j.jsv.2023.117866

[22] J. Jiang, S. Luo, M.S. Mohamed, Z. Liang, Real-time identification of dynamic loads using inverse solution and Kalman filter, Appl. Sci. 10 (19) (2020) 6767. https://doi.org/10.3390/app10196767

[23] T. Ojio, K. Yamada, Bridge weigh-in-motion systems using stringers of plate girder bridges, in: Proceedings of the Third International Conference on Weigh-in-Motion (ICWIM3), Orlando, FL, 2002, pp. 209–218.

[24] A.J. Cardini, J.T. DeWolf, Implementation of a long-term bridge weigh-in-motion system for a steel girder bridge in the interstate highway system, J. Bridge Eng. 14 (6) (2009) 418–423. https://doi.org/10.1061/(ASCE)1084-0702(2009)14:6(418)

[25] K. Helmi, B. Bakht, A. Mufti, Accurate measurements of gross vehicle weight through bridge weigh-in-motion: a case study, J. Civ. Struct. Health Monit. 4 (3) (2014) 195–208. https://doi.org/10.1007/s13349-014-0076-5

[26] M. Lydon, S.E. Taylor, D. Robinson, A. Mufti, E.J. OBrien, Recent developments in bridge weigh in motion (B-WIM), J. Civ. Struct. Health Monit. 6 (1) (2016) 69–81. https://doi.org/10.1007/s13349-015-0119-6

[27] J. Yang, P. Hou, C. Yang, Study on the method of moving load identification based on strain influence line, Appl. Sci. 11 (2) (2021) 853. https://doi.org/10.3390/app11020853

[28] J. Zhu, C. Wang, T. Qi, Y. Zhou, Vehicle load identification on orthotropic steel box beam bridge based on the strain response area, Appl. Sci. 12 (23) (2022) 12394. https://doi.org/10.3390/app122312394

[29] P. Agüero-Barrantes, R.E. Christenson, S. Lobo-Aguilar, Utilizing Kriging metamodeling to provide practical and effective bridge weigh-in-motion, J. Bridge Eng. 28 (2) (2023) 04022138. https://doi.org/10.1061/jbenf2.beeng-5760

[30] S. Lobo Aguilar, R.E. Christenson, A simplified shear-strain based bridge weigh-in-motion method for in-service highway bridges, Métodos y Materiales 8 (2018) 11–22. https://doi.org/10.15517/mym.v8i1.34551

[31] P. Agüero-Barrantes, S. Lobo-Aguilar, R.E. Christenson, Sparse sensing bridge weigh-in-motion for single-span bridges, Métodos y Materiales 11 (2021) 43–53. https://doi.org/10.15517/mym.v11i0.46400

[32] N. Zolghadri, M.W. Halling, N.R. Johnson, P.J. Barr, Field verification of simplified bridge weigh-in-motion techniques, J. Bridge Eng. 21 (6) (2016) 04016063. https://doi.org/10.1061/(asce)be.1943-5592.0000930

[33] S. Shi, M. Yarnold, S. Hurlebaus, J. Mander, Evaluation of a load cell-based bridge weigh-in-motion system, Transp. Res. Rec. 2679 (2) (2025) 535–549. https://doi.org/10.1177/03611981241263336

[34] W.-J. Yan, T.-T. Hao, K.-V. Yuen, C. Papadimitriou, Monitoring gross vehicle weight with a probabilistic and influence line-free bridge weight-in-motion scheme based on a transmissibility-like index, Mech. Syst. Signal Process. 177 (2022) 109133. https://doi.org/10.1016/j.ymssp.2022.109133

[35] A. Döring, M. Vogelbacher, O. Schneider, Investigations of ratio-based integrated influence lines as features for bridge-damage detection, Infrastructures 8 (4) (2023) 72. https://doi.org/10.3390/infrastructures8040072

[36] D. Huang, Y. Lu, Influence line theory supported single sensor-based strain feature for bridge defect diagnosis, Struct. Health Monit. (2025), online first. https://doi.org/10.1177/14759217251376931

[37] Q.B. Nguyen, T. Hoang, H.S. Nguyen, [Determination of the load applied on a simply supported beam based on measured deflection data], J. Sci. Technol. Civ. Eng. (HUCE) 18 (2V) (2024) 61–71 (in Vietnamese). https://doi.org/10.31814/stce.huce2024-18(2V)-05

[38] A. Ghali, A.M. Neville, T.G. Brown, Structural Analysis: A Unified Classical and Matrix Approach, CRC Press, Boca Raton, 2017. https://doi.org/10.1201/9781315273006

[39] M.T.A. Chaudhary, M. Morgese, T.W. Taylor, F. Ansari, Method and application for influence-line-free distributed detection of gross vehicle weights in bridges, Structures 73 (2025) 108298. https://doi.org/10.1016/j.istruc.2025.108298

[40] H. Wu, H. Zhao, J. Liu, Z. Hu, A filtering-based bridge weigh-in-motion system on a continuous multi-girder bridge considering the influence lines of different lanes, Front. Struct. Civ. Eng. 14 (5) (2020) 1232–1246. https://doi.org/10.1007/s11709-020-0653-0

[41] A. Moghadam, M. AlHamaydeh, R. Sarlo, Bridge-weigh-in-motion approach for simultaneous multiple vehicles on concrete-box-girder bridges, Autom. Constr. 137 (2022) 104179. https://doi.org/10.1016/j.autcon.2022.104179

[42] A. Moghadam, M. AlHamaydeh, R. Sarlo, Nothing-on-road bridge-weigh-in-motion used for long-span, concrete-box-girder bridges: an experimental case study, J. Struct. Integr. Maint. 8 (2) (2023) 79–90. https://doi.org/10.1080/24705314.2023.2165606

[43] A. Moghadam, M. AlHamaydeh, R. Sarlo, Dual-purpose procedure for bridge health monitoring and weigh-in-motion used for multiple-vehicle events, Autom. Constr. 148 (2023) 104768. https://doi.org/10.1016/j.autcon.2023.104768

[44] C. Zhou, C. Demartino, Y. Narazaki, Y. Xu, E. Chatzi, B.F. Spencer, Optimal sensor placement for bridge weigh-in-motion using an augmented Kalman filter, Mech. Syst. Signal Process. 241 (2025) 113522. https://doi.org/10.1016/j.ymssp.2025.113522

[45] J. Zhang, Y. Liu, X. Fan, An AR(1)-Tikhonov-SVD-GCV framework for stochastic moving load identification driven by bridge multi-point deflection data, Structures 88 (2026) 111844. https://doi.org/10.1016/j.istruc.2026.111844

[46] Z. Shen, W. Peng, X. Zhang, et al., A lightweight weigh-in-motion system based on vehicle-induced bridge deflection and impact dynamic responses, Int. J. Struct. Stab. Dyn. (2026), online. https://doi.org/10.1142/s0219455427503664

[47] Y. Zhou, Z. Feng, S.-K. Di, Z.-J. Jia, A novel approach for bending stiffness inversion and rapid evaluation of continuous beam bridges based on a deflection influence line, Struct. Control Health Monit. 2026 (2026) 1361157. https://doi.org/10.1155/stc/1361157

[48] A. Moghadam, R. Sarlo, Nothing-on-Road Bridge-Weigh-In-Motion (NOR-BWIM) Dataset, version 1, University Libraries, Virginia Tech, figshare, 2024. https://doi.org/10.7294/26880898.v1

[49] A. Moghadam, Integration of Traffic and Structural Health Monitoring Systems Using a Novel Nothing-On-Road (NOR) Bridge-Weigh-In-Motion (BWIM) System, PhD dissertation, Virginia Polytechnic Institute and State University, Blacksburg, VA, 2022. http://hdl.handle.net/10919/111390

[50] L. Frýba, Vibration of Solids and Structures under Moving Loads, 3rd ed., Thomas Telford, London, 1999.

[51] H. Sohn, Effects of environmental and operational variability on structural health monitoring, Philos. Trans. R. Soc. A 365 (1851) (2007) 539–560. https://doi.org/10.1098/rsta.2006.1935

[52] E.J. Cross, K.Y. Koo, J.M.W. Brownjohn, K. Worden, Long-term monitoring and data analysis of the Tamar Bridge, Mech. Syst. Signal Process. 35 (1–2) (2013) 16–34. https://doi.org/10.1016/j.ymssp.2012.08.026

[53] EN 1991-2:2003, Eurocode 1: Actions on Structures – Part 2: Traffic Loads on Bridges, CEN, Brussels, 2003.

[54] AASHTO, LRFD Bridge Design Specifications, 10th ed., American Association of State Highway and Transportation Officials, Washington, DC, 2024.

---

## Figure Captions

**Fig. 1.** Continuous beams considered: (a) two-span beam with instrumented span $L_1$, adjacent span $L_2 = \lambda L_1$ and sensor at $\xi L_1$; (b) symmetric three-span beam with side spans $L_s$, main span $L_c = \beta L_s$ and side-span sensor at $\xi L_s$.

**Fig. 2.** Deflection observability of a three-span beam with uniform rigidity: (a) symmetric beam, $N_w$ over $\beta$ and the side-span sensor position $\xi$, with the blind locus (thick line), the near-blind band $|N_w|<0.2$ (hatched), the optimum $\xi^*(\beta)$ (dashed) and the Cầu Mây layout with a mid side-span sensor (open circle); (b) asymmetric beam, sensor at mid span 1, over $L_1/L_2$ and $L_3/L_2$. Colours are clipped at ±1.5.

**Fig. 3.** Indicators of four channels along prismatic girders: deflection $N_w$ (Eq. 10; 2.5 at a simply supported mid-span), rotation $N_\theta$, strain or moment $N_M$ and shear $N_V$ (each 1 for the simply supported reference of its own span). (a) Equal two-span beam; (b) symmetric three-span beam with $\beta = 1.636$, the Cầu Mây span ratio. The grey band marks $|N|<0.2$.

**Fig. 4.** Multi-channel estimation under the assumed noise model: (a) variance with two or three optimally placed sensors relative to the best single sensor, against the common-mode fraction $\rho$ of the offset; (b) standard deviation of the load against the offset level for single sensors and three-sensor designs; (c) zero-sum pair (labelled offset-immune in the panel) at $\rho = 1$ against the white-noise level. 2S-eq: equal two-span beam; 3S-b2.0: three-span beam with $\beta = 2$; CM-A, CM-B: Cầu Mây calibrations A and B.

**Fig. 5.** NOR-BWIM strain records of three single-truck crossings of the five-span girder: a 5-axle and a 3-axle truck on day 2 and a 3-axle truck on day 1. Shaded: integration window; dashed: beam-model shape scaled to the reference gauge. The legend gives each gauge's integral $\int\varepsilon\,\mathrm{d}x$ (µε m).

**Fig. 6.** Ratio of the integral constants of two trucks, per gauge, with 95 % confidence intervals: (a) day 1, second to first 3-axle truck, 12 gauges and the gauge average of the four wheel-path gauges; (b) day 2, 5-axle to 3-axle truck, 4 gauges and their average. Grey bands: ±5 % and ±10 %. Red: invariance rejected; blue: equivalent within ±10 %; orange: inconclusive.

**Fig. 7.** Mean absolute error of the gross weight for single-gauge, gauge-average, GLS, zero-sum and mean-weight (mean-GVW) predictors, with 95 % bootstrap confidence intervals: in sample (IN), leave-one-run-out (LOO) and leave-one-truck-out (LOTO). (a) Day 2, 4 gauges; (b) day 1, 4 wheel-path gauges; (c) day 1, 12 gauges. GLS-diag: diagonal covariance; immune-eq: zero-sum estimator with equal noise ($\Sigma$ = identity matrix); GLS-resid: covariance from crossing residuals.

**Fig. 8.** Cầu Mây girder, indicators along the girder for a prismatic model with pinned piers and for the haunched model under calibrations A and B: (a) deflection $N_w$; (b) strain $N_M$, with strain blind points; (c) strain indicator including the section gain $c/EI$, assuming $c\propto h$. Dotted lines: gauge positions N7, N8 at mid side span and N8 at 0.4L.

**Fig. 9.** Identifiability of the Cầu Mây pier stiffness from two static readings: (a) ratio $r_{87}$ of the measured-to-model ratio at gauge N8 to that at gauge N7 against $\kappa = k/\alpha$, with model-form variants (grey) and the admissible band $|\ln r_{87}|\le 2\tau$, $\tau$ = 5.3 %, which is equivalent to both misfits lying within $\tau$ at the best-fit $\alpha$; (b) N8 and N7 indicators and cancellation ratios along the valley of best static fit $\alpha^*(\kappa)$; shaded: admissible range of $\kappa$.
