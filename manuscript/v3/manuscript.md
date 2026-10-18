# Load observability of continuous girder bridges: a general response-integral theorem, optimal offset-immune estimation and field verification

Quoc-Bao Nguyen^a^, Thai-Son Vu^a,\*^, Hung-Son Nguyen^a^

^a^ Faculty of Bridge and Road Engineering, Hanoi University of Civil Engineering, 55 Giai Phong, Bach Mai ward, 11618 Ha Noi, Viet Nam

\* Corresponding author: Thai-Son Vu. Tel.: +84 971 899 888. E-mail: sonvt2@huce.edu.vn

E-mail addresses: baonq@huce.edu.vn (Q.-B. Nguyen), sonvt2@huce.edu.vn (T.-S. Vu), sonnh@huce.edu.vn (H.-S. Nguyen)

---

## Abstract

Influence-area weigh-in-motion estimates gross vehicle weight from the area under one bridge response record. We ask which response channels, at which positions, can observe the total load on a continuous girder. For any linear channel (deflection, rotation, strain or support reaction) and a complete quasi-static crossing, the record integral equals the total load times a constant, the channel's response to a uniform unit load. Blind positions follow from one static analysis: strain gauges are blind at the zeros of the uniform-load moment diagram, which every continuous girder has; deflection gauges are blind only at particular span ratios, for example $(3+\sqrt{33})/6$ for two spans. For several channels, generalised least squares gives the minimum-variance invariant estimator; zero-sum weights make it immune to common-mode offset and drift, and the optimal sensors lie at the extremes of the uniform-load response. On public moving-truck strain records from a five-span continuous box girder, a 5-axle and a 3-axle truck gave the same constant (ratio 0.999 ± 0.140), and one weighed reference crossing predicted the other trucks within 6.5–7.0 % mean absolute error on the quieter day. Gauges 2 m apart had constants differing by up to 2.7 times, which a beam model cannot predict. On a 55 + 90 + 55 m box girder, two static readings bound the pier-to-girder stiffness ratio only from below, leaving the side-span deflection index between 0.12 and 0.82. A residual offset of 0.1 mm would bias a 25 t truck by 21–25 % at mid main span.

**Keywords:** Structural health monitoring; Sensor placement; Bridge weigh-in-motion; Continuous girder; Observability; Identifiability

---

## Nomenclature

| Symbol | Meaning |
|---|---|
| $A^+$ | positive part of the area under an influence line |
| $B_m$ | boundary-conditioning indicator $\lvert\partial\ln C_m/\partial\ln\kappa\rvert$ |
| $C_r$, $C_m$ | invariance constant of channel $r$; of a deflection channel at $m$ (m²/kN) |
| $c$ | distance of the gauged fibre from the neutral axis (m) |
| $EI$, $EI_\mathrm{mid}$ | flexural rigidity; design value at mid main span (kN m²) |
| $I_r$ | record integral over a complete crossing, in space |
| $k$, $k_g$ | rotational stiffness of a monolithic pier; antisymmetric pier stiffness of the girder (kN m/rad) |
| $L_\mathrm{tot}$ | length of the integration record (m) |
| $M_q$ | bending moment under a uniform load $q_0$ over the whole path |
| $N_w$, $N_M$ | deflection and strain (moment) indicators, Eqs. (10) and (9) |
| $P_\mathrm{tot}$, $P_0$ | total load of a crossing; weighed reference load (kN) |
| $P_\varepsilon$ | offset-equivalent load $\varepsilon_0L_\mathrm{tot}/C_m$ (kN) |
| $R$ | cancellation ratio $C/A^+$ |
| $w$ | weight vector of a multi-channel estimator |
| $\alpha$ | ratio of effective to design girder rigidity |
| $\beta$, $\rho_L$ | main-to-side span ratio (three spans); adjacent-to-instrumented span ratio (two spans) |
| $\varepsilon_0$ | residual zero offset after pre/post re-zeroing (mm) |
| $\eta_m$ | influence line of the channel at $m$ |
| $\kappa$ | pier-to-girder stiffness ratio $k/\alpha$ (kN m/rad) |
| $\mu$ | interior-moment parameter, $\mu=-8M_B/(q_0L_1^2)$ |
| $\rho$ | common-mode fraction of the offset between channels |
| $\xi$ | sensor position as a fraction of its span |
| BPM, SLM | beam-property method; standard-load method |

---

## 1. Introduction

Heavy vehicles above the design envelope shorten the life of highway bridges and, in extreme cases, contribute to collapse. A span of the Yangmingtan Bridge failed in 2012 under four overloaded trucks crossing together [1]. In other documented failures, heavy traffic acted together with design deficiencies or material degradation [2–4]. Knowing the loads that a bridge actually carries is therefore part of risk-informed asset management [5,6].

Pavement weigh-in-motion (WIM) is mature [7,8] and has codified accuracy classes [9], but stations are costly to install and maintain [10], and they weigh the vehicle rather than the load on a particular bridge. Bridge weigh-in-motion (BWIM), introduced by Moses [11], fits the measured response to axle loads times influence-line ordinates. It now includes influence lines calibrated from measurements [12], regularised solutions [13], accuracy improvements [14,15], contactless sensing [16] and virtual-axle methods without axle detectors [17]. Moving-force identification recovers axle-load histories in the time or frequency domain [18–20], on multi-span bridges [21] and with dynamic, Bayesian, Kalman-filter and machine-learning formulations [22–26]. These methods aim at axle loads and need several sensors, a structural model or a regularised inversion.

A simpler family estimates only the gross weight from the area under the response. Ojio and Yamada integrated the strain records of plate-girder stringers, multiplied the result by the speed and calibrated it against a truck of known weight [27]. The method has been used in long-term monitoring [28] and on a seven-span slab-on-girder bridge, where it was accurate to within 5 % for test trucks with well-estimated speeds [29,30]. Strain-area and strain-integral variants [31–34], a sparse-sensing influence-area system that chose the number and location of strain gauges on a single-span bridge [35], simplified BWIM in the field [36] and load-cell reactions [37] followed. The integral of the influence line has also served as a damage feature [38,39]. The present authors used the integral of mid-span deflection to identify the total load on a simply supported beam [40], where the influence line has one sign.

On continuous girders the influence line changes sign over each interior support, so positive and negative areas partly cancel. Gross weight has been obtained without influence lines from distributed fibre-optic strain on a five-span continuous bridge [41]. Lane-specific influence lines were needed on a continuous multi-girder bridge [42]. Long-span continuous box girders have been weighed from deck strain with a nothing-on-road BWIM system [43–45]. Optimal sensor placement for BWIM has been posed through an augmented Kalman filter [46], and deflection-based load identification as a regularised stochastic problem [47,48]. Measured deflection influence lines have been inverted for the stiffness of variable-section continuous girders [49]. What these studies do not provide is a criterion, available before installation, that says which channel at which position can observe the total load at all, how well, and how robustly to the uncertain boundary conditions of a real girder.

This paper develops such criteria for designing load-monitoring channels on continuous girders. Its contributions are as follows.

1. A theorem for any linear response channel: over a complete crossing, the record integral equals the total load times the channel's response to a uniform unit load. It yields closed-form blind loci for deflection, strain, rotation and reaction channels on two- and three-span girders. Strain channels are blind at every zero of the uniform-load moment diagram, deflection channels only near particular span ratios.
2. Observability and conditioning indicators that remain valid for non-prismatic girders. The strain indicator $N_M$ needs no reference stiffness, and the cancellation ratio $R = C/A^+$ separates cancellation between spans from restraint.
3. A minimum-variance invariant multi-channel estimator and an offset-immune variant with zero-sum weights, together with a placement rule proved for both: sensors belong at the extremes of the uniform-load response.
4. An identifiability analysis of the indicator under boundary uncertainty. For a symmetric girder with monolithic piers, the constant depends on the pier stiffness through one ratio and a Möbius law, which shows which additional measurement identifies it.
5. Verification at three levels: a laboratory two-span beam, public moving-truck strain records with weighed trucks on a five-span continuous box girder [50,51], and an application to an in-service 55 + 90 + 55 m box girder, for which the measurements that would decide between competing models are predicted.

"Observability" is used in the narrow sense of total-load observability: a non-zero constant, so that the total load maps to a non-zero integral. It is not the observability of a state-space model. Section 2 develops the theory, Sections 3–5 the laboratory, field and in-service verification, Section 6 the error budget and Section 7 the design workflow.

---

## 2. Theory

This section states the response-integral theorem for any channel, gives closed-form blind loci, defines the indicators, derives the optimal multi-channel estimator and analyses how boundary uncertainty enters the constant. Derivations are in Appendices A–C.

### 2.1. Response-integral theorem for any channel

Consider a linear-elastic structure whose properties do not change during a crossing, with any distribution $EI(x)$ and any linear elastic supports. A response channel at a fixed point $m$ is any fixed linear functional $r_m$ of the displacement field, measured from the unloaded state: the deflection $w(x_m)$, the rotation $w'(x_m)$, the bending moment, the fibre strain $\varepsilon = cM/EI$, the shear force or a support reaction. Let $\eta_m(x)$ be its influence line, the response to a unit vertical force at $x$, with $\eta_m = 0$ outside the loaded path $[0, L]$. A convoy of axle loads $P_i$ at fixed offsets $a_i$ ($a_1 = 0$) crosses quasi-statically, so the record is, by superposition,

$$y_m(x)=\sum_{i=1}^{n}P_i\,\eta_m(x-a_i). \tag{1}$$

Integrating Eq. (1) over the complete crossing, from the entry of the first axle to the exit of the last, and substituting $u = x - a_i$ term by term gives

$$I_r=\int_0^{L+a_\mathrm{max}}y_m\,\mathrm{d}x=P_\mathrm{tot}\,C_r,\qquad C_r=\int_0^L\eta_m(u)\,\mathrm{d}u=\frac{r_m[q_0]}{q_0}, \tag{2}$$

where $r_m[q_0]$ is the response of the channel to a uniform load $q_0$ over the whole path. The second equality needs superposition only: a uniform load is a continuous sum of point loads. For a deflection channel Eq. (2) reduces to $C_m = w_q(x_m)/q_0$, the deflection at the sensor under a uniform unit load. For a strain gauge,

$$C_\varepsilon=\frac{c_m\,M_q(x_m)}{EI_m\,q_0}. \tag{3}$$

The constant depends only on the structure, the channel and the load path, not on the number, loads or spacings of the axles. The local section constants $c_m$ and $EI_m$ enter Eq. (3) only as a gain, so a strain channel is blind exactly at the zeros of the uniform-load moment diagram, for any $EI(x)$ and any elastic supports. At constant speed $v$ the time integral is $I_r/v$. The theorem requires linearity, time invariance, a quasi-static response, axles that follow the path on which $\eta_m$ is defined, and a record re-zeroed to the unloaded state. On a deck, the path is a lane, and $C_r$ is the response to a uniform load on that lane. Truncating the record when the first axle leaves is not harmless: on a two-span example it changes the rotation integral by up to 59 % (Appendix B).

### 2.2. Closed-form blind loci

For a prismatic span under a uniform load, every channel is fixed by the two end moments. Write them as hogging parameters $m_l$ and $m_r$, with $m = -8M/(q_0L^2)$. For the instrumented span of a two-span beam and for the side span of a symmetric three-span beam, $(m_l, m_r) = (0, \mu)$. Here $\mu$ is the classical interior-moment parameter (Appendix A; [52]):

$$\mu_\mathrm{2span}=\frac{1+\rho_L^3/\rho_{EI}}{1+\rho_L/\rho_{EI}},\qquad \mu_\mathrm{3span}=\frac{2(\rho_{EI}+\beta^3)}{2\rho_{EI}+3\beta}, \tag{4}$$

with $\rho_L$ and $\rho_{EI}$ the adjacent-to-instrumented span and stiffness ratios of the two-span beam, and $\beta = L_m/L_s$ and $\rho_{EI} = EI_m/EI_s$ for three spans. The deflection constant at $\xi = x_m/L$ is

$$\frac{192EI\,C_m}{L^4}=8F(\xi,\mu),\qquad F(\xi,\mu)=\xi(1-2\xi^2+\xi^3)-\frac{\mu}{2}\,\xi(1-\xi^2). \tag{5}$$

Setting $F = 0$ gives the deflection blind condition on $\mu$ alone,

$$C_m=0\;\Leftrightarrow\;\mu=\mu_\mathrm{crit}(\xi)=\frac{2(1+\xi-\xi^2)}{1+\xi}, \tag{6}$$

which exists only for $1<\mu<2$. For a mid-span sensor on two spans of equal stiffness, the blind span ratio and the optimal sensor position are exact:

$$\rho_{L,\mathrm{crit}}=\frac{3+\sqrt{33}}{6}=1.4574,\qquad \xi^*=\frac{1+\sqrt{33}}{16}=0.4215. \tag{7}$$

For the symmetric three-span beam with uniform rigidity and a mid side-span sensor, the blind main-to-side ratio is the real root of $6\beta^3-15\beta-4=0$,

$$\beta_\mathrm{crit}=\sqrt{10/3}\,\cos\!\Big[\tfrac13\arccos\!\Big(\tfrac25\sqrt{6/5}\Big)\Big]=1.7006, \tag{8}$$

which Eq. (8) gives in exact trigonometric form, and the side-span blind locus ends at $\beta = 2\cos(\pi/9) = 1.8794$. The near-blind band $|N_w|<0.2$ covers $1.385<\rho_L<1.525$ on two spans and $1.621<\beta<1.775$ on three. Beyond the blind ratio the constant is negative but non-zero and remains observable. Fig. 1 defines the notation. Table A.1 and Fig. 2 give the optimal side-span positions and the observability map, and Appendix A gives asymmetric layouts. All closed forms agree with finite element (FE) evaluations of Eq. (2) in 981 checks, with a maximum error of 8.1 × 10⁻¹¹ on the normalised indicators.

The strain channel follows from the same end moments:

$$N_M=\frac{8M_q(x_m)}{q_0L^2}=4\xi(1-\xi)-m_l(1-\xi)-m_r\xi,\qquad \xi_0=1-\frac{\mu}{4}. \tag{9}$$

Eq. (9) gives the strain blind point $\xi_0$ in the instrumented or side span: $0.75L$ for two equal spans. In the main span of a symmetric girder, $m_l = m_r = \mu/\beta^2$ and the blind point lies at $\eta_0 = \tfrac12(1-\sqrt{1-\mu/\beta^2})$ of the main span from the pier: 0.276 for three equal spans and 0.177 for $\beta = 1.636$. Strain blind points exist in every span that has a sagging zone ($\mu<4$), so they are a property of every continuous girder, not of particular span ratios. The near-blind band $|N_M|<0.2$ is a ring around each zero. For two equal spans it covers $0.676<\xi<0.812$, which is 0.19–0.32 of the span from the interior support. A gauge at the support section is well conditioned, with $|N_M| = \mu$. A gauge set back from the pier to clear the diaphragm, or placed at a quarter point, can fall into the band. Table 1 collects the blind loci of all channels; Fig. 3 shows the indicators along two prismatic girders.

**Table 1.** Blind loci of response channels under the uniform-load criterion, prismatic beams with $\rho_{EI} = 1$ unless stated. $\mu$ from Eq. (4).

| Channel | Blind where | Two-span beam (span 1) | Symmetric three-span beam |
|---|---|---|---|
| Strain, moment, curvature | zeros of $M_q$ | $\xi_0 = 1-\mu/4$ (0.75 at $\rho_L = 1$) | side $\xi_0 = 1-\mu/4$; main $\eta_0=\tfrac12(1-\sqrt{1-\mu/\beta^2})$ |
| Deflection | zeros of $w_q$ | $\mu = \mu_\mathrm{crit}(\xi)$, only for $1<\mu<2$; mid-span: $\rho_L = 1.4574$ | mid side span: $\beta = 1.7006$; locus ends at $\beta = 1.8794$ |
| Rotation | extrema of $w_q$ | end: $\mu = 2$ ($\rho_L = 1.6180$); pier: $\rho_L = 1$ for any $\rho_{EI}$ | end: $\beta = 2\cos(\pi/9)$; pier: $\beta = \sqrt{3/2}$ for any $\rho_{EI}$; mid main span: always |
| Shear | maxima of $M_q$ | $\xi = \xi_0/2$ | side $\xi_0/2$; mid main span: always |
| End reaction | no sagging zone in the end span | $\mu = 4$ ($\rho_L = 2.3028$) | $\mu = 4$ ($\beta = 2.6691$) |
| Interior reaction | never under a full uniform load | – | – |

Two identities in Table 1 have practical value. The end-reaction indicator equals the strain blind abscissa, $2R_A/(q_0L_1) = \xi_0$, for any $EI(x)$ and any pier springs, because statics of the end segment gives $M_q = R_Ax - q_0x^2/2$. The deflection blind locus ends where the end rotation vanishes, which explains the limit $2\cos(\pi/9)$.

### 2.3. Observability and conditioning indicators

Every estimator below divides by $C$, so to first order the sensitivity to measurement error scales as $1/|C|$. For a deflection channel the normalised indicator is

$$N_w=\frac{192EI_\mathrm{ref}\,C_m}{L^4}, \tag{10}$$

with $L$ the span containing the sensor. For a prismatic beam $N_w$ equals 1 at mid-span of a simply supported span, and $|N_w|<0.2$ marks near-blind locations. For a non-prismatic girder $N_w$ depends on the choice of $EI_\mathrm{ref}$, and Section 5 shows that this choice can dominate the result. The strain indicator $N_M$ of Eq. (9) needs no reference stiffness: it is the uniform-load moment relative to the free simple-span moment, and the threshold 0.2 keeps one meaning for any $EI(x)$. The section enters only through the gain $c/EI$ of Eq. (3), which sets the absolute signal level. A second measure that needs no reference is the cancellation ratio

$$R=\frac{C}{A^+}=1-\frac{|A^-|}{A^+}, \tag{11}$$

the net influence area divided by its positive part. $R$ equals 1 for a simply supported span and 4/7 for the mid-span deflection of two equal spans. It is 0 at a blind configuration. A small $N$ with $R$ near 1 indicates restraint, not cancellation. The strain influence line is more local than the deflection line, so at every prismatic location examined it cancels less: $R_\varepsilon = 0.667$ against $R_w = 0.571$ at mid-span of two equal spans.

Neither index carries the absolute signal level, on which the offset error depends. A residual offset $\varepsilon_0$, left after the record has been re-zeroed before and after the crossing, adds $\varepsilon_0L_\mathrm{tot}$ to the integral. With $I = CP$ the relative bias is

$$\Big(\frac{\delta P}{P}\Big)_{\varepsilon_0}=\frac{P_\varepsilon}{P},\qquad P_\varepsilon=\frac{\varepsilon_0L_\mathrm{tot}}{C}. \tag{12}$$

The offset-equivalent load $P_\varepsilon$ is the load at which the offset causes a 100 % bias. It combines sensor position, baseline stability and the lightest vehicle to be screened into one number.

### 2.4. Multi-channel estimation, offset immunity and placement

Let channel $j$, a deflection or strain, give the integral $I_j = C_jP + \varepsilon_{0,j}L_\mathrm{tot} + n_j$, with white noise $n_j$ and offsets that may be correlated between channels, and let $\Sigma$ be the covariance of the vector $I$. A linear estimator $\hat P = w^\top I$ is unbiased for every axle configuration if and only if $w^\top C = 1$. Minimising its variance under this constraint gives the generalised least-squares weights

$$w^\star=\frac{\Sigma^{-1}C}{C^\top\Sigma^{-1}C},\qquad \mathrm{Var}\,\hat P^\star=\big(C^\top\Sigma^{-1}C\big)^{-1}, \tag{13}$$

the Gauss–Markov best linear unbiased estimator of $P$. For one channel, Eq. (13) returns $\hat P = I/C$ with variance $\sigma_{P,\mathrm{noise}}^2 + P_\varepsilon^2$, so $C^\top\Sigma^{-1}C$ generalises $|C|$ to several channels.

Within one channel, uniform weighting is optimal only in a restricted sense. A non-uniform weight $g(x)$ gives a mean $\sum_aP_a\int g(x)\eta(x-s_a)\,\mathrm{d}x$, which is independent of the axle positions for every influence line only if $g$ is constant (Appendix B). The uniform weight is therefore the only weight that is translation-invariant for every structure, which is the property the standard-load method needs. When the influence line is known, other invariant weights exist. For two equal spans their white-noise variance is 1.5–6.6 times smaller, depending on the range of axle entry shifts, but a 20 % stiffness error in the adjacent span then produces configuration-dependent errors of −1.1 % to +2.0 %. Two consequences for signal processing follow. A record integrated uniformly in time weights space by $1/v(x)$, so the integral must be taken in space. A linear time-invariant prefilter with unit static gain leaves the integral unchanged, whereas tapering windows do not.

Across channels, a common-mode offset can be removed exactly. Adding $\sum_jw_j = 0$ for each channel type to $w^\top C = 1$ makes $\hat P$ insensitive to any disturbance shared by the channels: a constant offset, a drift, or motion of the reference frame. With equal noise and offset statistics, the variance becomes

$$\mathrm{Var}\,\hat P_\mathrm{imm}=\frac{\sigma^2\Delta x\,L_\mathrm{tot}+(1-\rho)\varepsilon_0^2L_\mathrm{tot}^2}{\sum_j(C_j-\bar C)^2}, \tag{14}$$

where $\rho$ is the common-mode fraction of the offset and $\Delta x$ the sampling interval. Eq. (14) does not contain the common offset. For two channels, $w = (1,-1)/(C_1-C_2)$, and a second sensor over a support ($C_2 = 0$) gives the familiar differential measurement against a reference target. The price is a white-noise variance higher by the factor $2C_1^2/(C_1-C_2)^2$, 1.65–2.0 on the beams studied. This is negligible, because the white-noise term was about 10⁻⁴ of the offset term at $\sigma = 0.01$ mm and $\varepsilon_0 = 0.1$ mm. The standard-load ratio $P_t = P_0\,w^\top I_t/w^\top I_0$ with $\sum w_j = 0$ cancels the common offset in both crossings, which a single gauge cannot do.

If the noise statistics do not depend on position, $1/\mathrm{Var}$ is a convex quadratic in the vector of constants $C(x_j)$, for both Eq. (13) and Eq. (14). A convex function on a box attains its maximum at a vertex. Optimal sensors therefore lie only at the maximum and the minimum of the uniform-load response: of $w_q(x)$ for deflection and of $M_q(x)$ for strain. Placement needs the same single static analysis as Eq. (2). Independent offsets call for clustering at the maximum; correlated offsets call for one sensor at the minimum, which is a support or the most negative point. A brute-force search over 96 cases found no design better than the vertex design. A Monte Carlo study with 10⁵ random axle configurations per case confirmed that the estimators are unbiased, that their scatter does not depend on the number of axles, and that the variances of Eqs. (13) and (14) hold to within 0.6 % (Supplementary Material). Fig. 4 shows the gain over the best single sensor.

### 2.5. Identifiability of the indicator under boundary uncertainty

A girder with monolithic piers has a stiffness matrix $\alpha K_g + kK_p$. Here $\alpha$ scales the girder rigidity and $k$ is the rotational stiffness of each pier. Every static response then scales as $\alpha^{-1}g(\kappa)$ with $\kappa = k/\alpha$, so two static readings fix $\alpha$ for each $\kappa$ and constrain $\kappa$ only through their ratio. For a mirror-symmetric girder with equal piers, the uniform load excites only the antisymmetric pier-rotation pattern, and the Sherman–Morrison formula gives (Appendix C)

$$C_m(\kappa)=C_\infty+\frac{C_0-C_\infty}{1+\kappa/k_g}. \tag{15}$$

$C_0$ and $C_\infty$ are the constants for pinned and fixed piers, and $k_g$ is the girder's own antisymmetric pier stiffness. The ratio $C_\infty/C_0$ is the full range that pier fixity can produce at a gauge. The local measure is the boundary-conditioning indicator $B_m = |\partial\ln C_m/\partial\ln\kappa|$, the relative error in $C_m$ per unit relative error in $\kappa$. For a symmetric prismatic three-span beam with rotational springs $k$ at the piers, slope-deflection gives

$$\mu(K)=1+\frac{\beta(2\beta^2-3)}{3\beta+2\rho_{EI}+\beta K},\qquad K=\frac{kL_s}{EI_s}, \tag{16}$$

Eq. (16) replaces $\mu_\mathrm{3span}$ in Eq. (5) and agrees with FE to 4.4 × 10⁻⁷. For $\beta = 1.636$ the side-span index at $\xi = 0.4$ rises from 0.287 (pinned) to 1.037 (fixed), whereas the mid main-span index falls from 0.755 to 0.500. Rotational restraint moves the side-span gauge away from blindness but makes its constant strongly dependent on $k$.

The theory thus gives, from one static analysis, the constant of every channel, its blind loci, the optimal placement and its sensitivity to the boundary conditions. Sections 3–5 test it.

---

## 3. Laboratory verification

This section verifies the deflection influence line, the integral and the two estimators on a laboratory two-span beam. The loads were positioned statically at successive points, so the tests check the model and the algorithm, not performance under moving traffic. The equal spans are also the layout furthest from blindness.

### 3.1. Specimen and procedure

The specimen was a steel hollow square tube, 25 mm × 25 mm with a wall thickness of 2.03 mm ($I = 16\,530$ mm⁴, $E = 200$ GPa), on three supports forming two equal spans of 2500 mm. The end supports were rollers and the interior support a knife edge. The theoretical constant at mid-span of the first span is $C_m = l^4/(192EI) = 61.54$ mm²/N, and shear deformation adds 8 × 10⁻⁴ of the bending deflection. Deflection at that point was measured with a linear variable differential transformer (LVDT) of 0.005 mm resolution. Calibrated steel weights were suspended at 250 mm steps along the whole traverse, and each reported deflection is the mean of three loading and unloading cycles. Three configurations were tested: a single 40.64 N reference load; two loads of 2145 g and 4684 g, 250 mm apart; and three loads of 2550 g, 5100 g and 5100 g. The order of the three-load group was not recorded independently. The order used here, with the 2550 g load leading and the others 500 mm and a further 250 mm behind, fits the record with a root-mean-square residual of 0.030 mm, against 0.55 mm for the reverse spacing. The three-load result is therefore not a fully independent test. The data are listed in Appendix D, and Fig. 5 shows the specimen and the single-load influence line.

### 3.2. Results

The analytical influence line matched the single-load record within 0.0126 mm, 0.44 % of the peak, with predominantly positive residuals that indicate a small systematic component such as slight support flexibility. The trapezoidal rule on the 250 mm grid underestimates the exact single-load integral by 0.500 %, a property of the quadrature, whereas Simpson's rule reduces this to +0.027 %. Simpson's rule loses its advantage when the entry and exit kinks of trailing loads fall inside its panels: −0.92 % and −0.44 % for the two- and three-load records. The trapezoidal rule is used throughout.

**Table 2.** Identified total loads against direct weighing (trapezoidal rule).

| Configuration | Weighed (N) | BPM (N) | BPM deviation | SLM (N) | SLM deviation |
|---|---|---|---|---|---|
| Two loads | 66.99 | 67.73 | +1.10 % | 67.40 | +0.61 % |
| Three loads | 125.08 | 126.57 | +1.19 % | 125.95 | +0.70 % |

Table 2 compares the beam-property method (BPM), $P = I/C_m$, with the standard-load method (SLM), $P_t = P_0I_t/I_0$, which is the Ojio–Yamada calibration written for a deflection record [27]. The ratio of the two estimates is 1.0049 for both configurations, which equals the ratio of the measured reference integral to its exact value. SLM absorbs the calibration error of the reference record; BPM does not.

The measured-to-analytical integral ratio depends on the load group: 1.010 for the single load, 1.016 for two loads and 1.017 for three loads. The SLM residuals of 0.61 % and 0.70 % are exactly this step. The data cannot separate a mild non-proportionality of the support seating from errors in the stated masses or load positions. Because the configurations differ in both total load and spacing, the tests support the invariance of Eq. (2) only indirectly. A direct test with a fixed total load at several spacings and magnitudes, and a test of the predicted blind configuration (spans of 2500 mm and 3644 mm on the same rig), have not been carried out. The field records of Section 4 supply the moving-load test on a continuous structure that the laboratory lacks.

---

## 4. Field verification on a five-span continuous box girder

This section tests the theorem with moving, weighed trucks on a real continuous girder, using a public dataset. The tests address invariance to axle configuration, the standard-load method, speed, superposition, lane, noise and the limits of a beam model.

### 4.1. Data

The Nothing-on-Road BWIM dataset [50] (CC0 licence) contains strain records of the Virginia Smart Road Bridge, documented in [43–45,51]. The bridge is a post-tensioned concrete box girder continuous over five spans of 86.5 + 3 × 144 + 86.5 m = 605 m. The box depth varies from about 3.8 m at mid-span to 9.5 m at the piers. Strain transducers on the soffit of the top slab, in line with the wheel path at about 2 m pitch, lie near mid-span of span 2, 158.5 m from the first abutment. On the first day two 3-axle construction trucks, with driver-reported gross weights of 21.17–22.82 t per pass, were recorded at 100 Hz on 12 channels. On the second day a 3-axle truck of 26.8 t and a 5-axle truck of 25.9 t, both weighed on a static scale, were recorded at 200 Hz on four channels. They ran in the instrumented lane (lane A), on the return trip in the other lane (lane B), and in two in-line two-truck runs. Axle spacings were measured on site [51].

Speeds were obtained from the local strain spikes of the axles and the measured wheelbase; they agree with the GPS speeds of the dataset authors within 1–2 %. For each crossing a linear baseline was fitted to quiet segments before and after the event. The strain was integrated over the whole time the truck was on the 605 m bridge plus 5 s at each end, and converted to $\int\varepsilon\,\mathrm{d}x$ with the speed. The noise of each integral was estimated from 80 vehicle-free records of the same length on the same day and channel. Three day-1 runs with two trucks on the bridge, and four passes without documented weights, were excluded. Fig. 6 shows three crossings with the integration windows.

### 4.2. Invariance, standard-load estimation and speed

Table 3 summarises the tests. On day 1 the per-gauge coefficient of variation of $\int\varepsilon\,\mathrm{d}x/\mathrm{GVW}$ over seven crossings at 10–20 m/s was 5.8–13.5 % for the four wheel-path gauges and 5.6 % for their average. This scatter is explained by the measured integral noise ($\chi^2$ p = 0.14–0.60 per gauge). The gauge common to both days gave $-2.18 \pm 0.09$ µε m/t on day 1 and $-2.12 \pm 0.25$ µε m/t on day 2, although trucks, axle configurations and speeds differed (Fig. 7). On day 2 the 5-axle and 3-axle trucks gave the same constant within noise: their ratio was 0.999 ± 0.140 for the gauge average and 1.010 ± 0.115 for the best gauge. This is the axle-configuration independence that Eq. (2) predicts.

**Table 3.** Field tests on the NOR-BWIM records (lane A unless stated; ± one standard error).

| Test | Quantity | Result |
|---|---|---|
| Invariance, day 1 (3-axle, 10–20 m/s, n = 7) | CV of $\int\varepsilon\,\mathrm{d}x/\mathrm{GVW}$, gauge average (noise-expected) | 5.6 % (6.1 %) |
| Invariance, day 2 (3- and 5-axle, 13–28 m/s, n = 8) | CV, gauge average (noise-expected) | 14.4 % (20.2 %) |
| Axle configuration, day 2 | $C$(5-axle)/$C$(3-axle), average; best gauge | 0.999 ± 0.140; 1.010 ± 0.115 |
| SLM, one reference crossing, day 1 | mean absolute error, same / other truck | 7.0 % / 6.5 % |
| SLM, all runs of the 3-axle truck as reference, day 2 | mean absolute error for the 5-axle truck | 5.1 % |
| Speed, day 1 | slope of $C$ per 10 m/s, average | −3.6 ± 5.8 % |
| Superposition (5-axle + 3-axle in line, 52.7 t) | measured / sum of single-truck predictions | 0.93 ± 0.11; 0.92 ± 0.11 |
| Lane | $C_B/C_A$, average (range of gauges) | 0.81 ± 0.09 (0.66–1.02) |
| Gauges at one section | integral ratio to the reference gauge: model; measured | 0.978–1.003; 0.68–2.71 |

As a standard-load estimator with a single reference crossing, the integral predicted the gross weight of the other day-1 crossings with mean absolute errors of 7.0 % (same truck) and 6.5 % (other truck) for the gauge average. Calibrating on all runs of the 3-axle truck and weighing the 5-axle truck gave 5.1 %; the reverse direction gave 17.1 %. On day 2 the single-reference errors were larger, 17.8 % for the average, because the integral noise per crossing was 3–4 times higher (Section 4.4). No speed effect was resolved between 10 and 28 m/s: the slope was $-3.6 \pm 5.8$ % per 10 m/s on day 1 and $+5.2 \pm 13.0$ % on day 2. The local axle spikes and the deck vibration after exit integrate out (Fig. 6).

### 4.3. Superposition, lane and the limits of a beam model

The two in-line two-truck events gave integrals of 0.93 ± 0.11 and 0.92 ± 0.11 of the sum predicted from the single-truck constants. Superposition therefore holds within uncertainty, and the combined weight of 52.7 t was recovered as 48.8 t and 48.5 t (−7.3 % and −7.9 %). The constant belongs to the load path, as Eq. (2) states. Return trips of the same trucks in the far lane gave 0.81 ± 0.09 of the lane-A constant for the gauge average, and 0.66–1.02 for individual gauges. Each lane needs its own constant, as found on another continuous girder [42].

Gauges a few metres apart at one cross-section had constants differing by up to 2.7 times. The 12 day-1 channels ranged from 0.68 to 2.71 times the reference gauge, and on day 2, in lane B, the ratios to the reference gauge were 1.82 ± 0.10 and 2.41 ± 0.10. A one-dimensional beam model predicts 0.978–1.003 for all of them. The difference is not noise, and it is unlikely to be gauge-factor spread, because the ratios change with the lane (about 3.2 in lane A against 1.8 in lane B for the same pair). The deck-soffit gauges respond to slab bending and shear lag as well as to girder bending. The integral is invariant for every gauge separately, but its value cannot be predicted from a beam model. On such girders the constant must come from a weighed reference vehicle (SLM) or from a three-dimensional model; a beam-model BPM would fail.

A beam model of the girder (Euler–Bernoulli, parabolic haunch, $I\propto h^2$) reproduces the global shape of the strain history ($r^2$ = 0.79–0.94 for the documented single-truck crossings). It places the zero-moment points of the uniform-load moment diagram in span 2 at 121.6 m and 190.8 m, about 35 m from the gauges on either side. The gauges are therefore not blind; their strain constant is 0.69 of the largest on the girder, which is found at an interior pier (0.56–0.93 across the stiffness laws tested). Only about half of the integral comes net from the instrumented span: its net-to-positive ratio is 0.51. The adjacent spans contribute −26 % and −66 % of the net integral and span 4 adds +23 %, so the whole 605 m crossing must be integrated.

### 4.4. Noise and its implication

The day-2 records carry low-frequency strain wander of about 0.1–0.3 µε below 0.2 Hz, inside the band of the global response. At the reference gauge the integral noise per crossing was 5.5 µε m on day 1 and 18.8 µε m on day 2, against signals of 50–130 µε m. For one crossing of a 25 t truck this corresponds to a weight error of 10 % (day 1) or 35 % (day 2), and longer or quadratic baselines did not reduce it. This is the residual-offset term of Eq. (12) in strain form: a slow disturbance integrated over a long window. Combining the beam-model shape with the measured noise, a gauge within ±12 m of a zero-moment point would see its constant fall below half the mid-span value, so its weight error would at least double. If the wander is common to gauges whose constants differ, the zero-sum combination of Eq. (14) would remove it. The constants at one section here differ by factors of 2–3, but whether the wander is common-mode was not tested.

The field data confirm invariance to axle configuration, the standard-load estimator, speed independence and superposition on a continuous girder under moving load, and show that lane, local deck action and slow drift limit the accuracy. The tests rest on two axle counts, four trucks and driver-reported weights on day 1, and the gauge calibration factors and exact positions are not published, so absolute constants cannot be checked.

---

## 5. In-service box girder: identifiability and channel design

This section applies the criteria to an in-service three-span box girder with static acceptance-test data. The question is how far the observability of each installed gauge is determined by the available data, which channel and position would be robust, and which measurements would decide between the admissible models.

### 5.1. Bridge, data and model

The Cầu Mây Bridge carries provincial road DT389 over the Kinh Mon River in Hai Duong, Viet Nam. Its main bridge is a three-span continuous prestressed concrete box girder of 55 + 90 + 55 m built by balanced cantilever ($\beta = 1.636$). The depth varies from 2.40 m at mid-span to 5.40 m at the piers, with design second moments of 5.482 m⁴ and 59.61 m⁴ and $E_c = 36\,057$ MPa. The inner piers are monolithic with the girder; the end piers carry pot bearings. In the June 2020 acceptance test, four trucks stood in side span N8 and six in centre span N7. The trucks were three-axle, nominally 5 + 10 + 10 t, with a weighed mean of 25.06 t. Dial gauges read the peak deflection under centric and eccentric transverse positions. Gauge N8 is at 0.4L of the side span and N7 at mid main span. The mean of six readings is 5.55 mm at N8 and 15.42 mm at N7.

The girder was modelled with Euler–Bernoulli elements, a parabolic depth variation over $L_v = 44$ m from each inner pier and $I\propto h^{2.943}$ fitted to the two design sections. Each inner pier is a rotational spring $k$. The depth law and the pier dimensions are not documented, so $L_v$ = 40 and 45 m, exponents of 2.5 and 3.2, and a ±1.5 m rigid pier zone were tested as model-form variants. Three reference calibrations are reported. Calibration A is the design model ($\alpha = 1$, $k = 2.75\times10^7$ kN m/rad fitted to the designer's FE output); it misfits the measurements by +2.4 % at N8 and +12.3 % at N7. Calibration A′ rescales A to the measurements ($\alpha = 1.088$; misfits −4.6 % and +5.0 %). Calibration B is the joint least-squares fit ($\alpha = 0.716$, $k = 1.2\times10^8$ kN m/rad; misfits −2.8 % and +2.9 %).

### 5.2. What the static data identify

The ratio of the measured-to-model ratios at N8 and N7 never reaches 1. It falls from 1.126 at $\kappa = 10^7$ kN m/rad to a minimum of 1.058 at $\kappa = 1.68\times10^8$ kN m/rad, which is calibration B, and returns to 1.091 for fixed piers (Fig. 9a). The Fisher information of the two readings is singular at that minimum. The model-form variants move the minimum between 1.039 and 1.092 but never to 1, so the 4–9 % residual is model-form error, not a calibration choice. B is therefore the nearest fit, not an exact one, and its $\alpha = 0.716$ would mean a 28 % loss of rigidity in a young, uncracked prestressed girder.

The admissible range is reported instead of point calibrations. The relative standard error of each mean reading is 1.9–2.0 %, and the model-form spread adds 1.75 % per gauge. A 2σ tolerance of 5.3 % on both gauges admits every $\kappa \ge 1.8\times10^7$ kN m/rad: the static data bound $\kappa$ only from below. Over this set the N8 index ($EI_\mathrm{ref} = EI_\mathrm{mid}$) lies between 0.12 and 0.82 and $R$ between 0.13 and 1.00, whereas the N7 index stays between 0.19 and 0.29 (Table 4, Fig. 9b). The upper part of the N8 range requires $\alpha \approx 0.5$–0.7. A prior $\alpha \in [0.9, 1.3]$ leaves N8 at 0.12–0.30.

The Möbius law of Eq. (15) explains the asymmetry. With $k_g = 4.36\times10^7$ kN m/rad, $C_\infty/C_0$ is 14.0 at N8 and 0.59 at N7, and the design stiffness sits at $\kappa/k_g = 0.63$, near the steepest part of the curve. At that point $B_m$ is 0.51 at N8 and 0.12 at N7. Calibrating the model to the N8 reading does not fix the N8 constant either: over the static admissible set, the ratio of $C_m$ to the modelled N8 deflection varies by a factor of 6.5, against 1.5 for N7.

**Table 4.** Observability indicators of the Cầu Mây gauges. $N_w$ from Eq. (10) with $EI_\mathrm{ref} = EI_\mathrm{mid}$ of the design section and $L$ the span containing the gauge; $R$ from Eq. (11) in brackets. Static set: tolerance 5.3 %; joint set: static set plus the mode-3 interpretation of the measured frequencies (Section 5.3). The bound column covers pinned to fixed piers with design $EI$ and all $L_v$ variants; it is a bound, not an uncertainty range. –: not computed.

| Gauge | Prismatic, pinned | A (design) | A′ ($\alpha$ = 1.088) | B ($\alpha$ = 0.716) | Static set | Joint set | Bound, pinned … fixed |
|---|---|---|---|---|---|---|---|
| N8, 0.4L (installed) | 0.287 (0.14) | 0.181 (0.18) | 0.160 (0.17) | 0.476 (0.56) | 0.124–0.822 (0.13–1.00) | 0.124–0.390 (0.13–0.46) | 0.023 … 0.446 |
| N8 at mid side span | 0.163 (0.08) | 0.105 (0.11) | 0.089 (–) | 0.377 (0.49) | – | – | −0.066 … 0.375 |
| N7, mid main span (installed) | 0.755 (0.70) | 0.209 (0.59) | 0.194 (0.58) | 0.234 (0.77) | 0.190–0.286 (0.56–1.00) | 0.190–0.222 (0.56–0.72) | 0.263 … 0.145 |

Calibration B's N8 value of 0.476 lies outside the bound column because the bound uses design $EI$; normalised by $\alpha EI_\mathrm{mid}$ it is 0.341. The centre-span index is low (0.19–0.29) although $R$ is 0.56–1.00, so its smallness reflects restraint by the haunches, not cancellation. The prismatic threshold $|N_w|<0.2$ therefore does not transfer to haunched girders unless it is stated with $EI_\mathrm{ref}$, whereas $R$ separates the two effects.

### 5.3. Measured frequencies as conditional evidence

The test report gives vertical frequencies of 3.43, 3.64 and 3.63 Hz at mid-span of N6, N7 and N8, one value per span and without mode shapes. A mass model (24.4–29.7 t/m) and a dynamic-to-static modulus ratio of 1.0–1.2 were assumed. The values cannot be the first vertical mode, which lies at 1.19–2.48 Hz in the model and would need $\alpha \ge 1.91$. Nor can they be the antisymmetric second mode, which has a node at mid N7 and no admissible joint set. They are compatible only with the third mode, the first symmetric mode dominated by the side spans. Under this interpretation calibration B is excluded: it predicts 2.89 Hz, and at most 3.28 Hz with the lightest mass and the stiffest dynamic modulus. The joint admissible set becomes $\kappa = 1.8\times10^7$–$1.1\times10^8$ kN m/rad and $\alpha = 0.80$–1.15, with an N8 index of 0.12–0.39 and an N7 index of 0.19–0.22 (Table 4). The selection is conditional, because the approach spans give similar values (3.0–3.1 Hz) and a truck-bounce response cannot be ruled out. Without the frequency row, the range falls back to the static set.

### 5.4. Which channel, where

For this girder the deflection channel at mid main span is the robust choice: over the joint set its constant spans only $3.3$–$3.8\times10^{-4}$ m²/kN. A side-span deflection gauge is ill-conditioned with respect to pier stiffness and should not take its constant from a design model unless that stiffness is identified. The strain channel behaves differently from the deflection channel on this girder (Fig. 8). The haunches move every zero-moment point towards mid-span. The side-span zero lies 26.0–33.3 m from the abutment over the range of pier fixity, so a strain gauge at mid side span would be blind under calibration A ($N_M = 0.048$) and change sign with pinned piers. The centre of the main span is near-blind for strain in every haunched model ($N_M$ = 0.163–0.212 at N7), again through restraint ($R_\varepsilon$ = 0.65–1). The best-conditioned strain locations are 5–10 m from the piers, where $|N_M| \ge 0.39$ in all haunched models; the gain $c/EI$ there is about one fifth of that at mid-span, assuming $c\propto h$. Bearing load cells at the end supports give $N_R = \xi_0$ = 0.47–0.61 and cannot be blind unless the side span loses its sagging zone.

For several deflection channels, Section 2.4 places the second sensor at the most negative constant, in the side span 4–10 m from the inner pier. The pair at 100 m and 152 m from the end support T5 is within 0.9 % of the calibration-specific optimum under both A and B. At $\sigma = 0.01$ mm and $\varepsilon_0 = 0.1$ mm, it lowers the standard deviation of the load from 24.8 % with N7 alone to 10.6 % at $\rho = 0.9$ and 0.071 % at $\rho = 1$ (calibration A). Placement is thus insensitive to the unresolved pier stiffness, unlike the observability of the side-span gauge.

If a model-based constant is wanted, the most informative additional measurement is a tiltmeter on the monolithic pier T7. Under the side-span convoy it would read about 167 µrad. Added to the two deflections, it would reduce the Cramér–Rao standard deviation of $\ln C_m$ at N8 from 0.87 to 0.18. An identified first vertical frequency would reduce it to 0.24, whereas a rotation reading at the end bearing T8 adds little, because its sensitivity duplicates that of N8.

### 5.5. Predicted discriminating measurements

A field test with moving weighed trucks has been designed for this bridge; Table 5 gives the predicted values that would decide between the reference calibrations. These are design predictions, not results. The ratio of integrals at the side-span and centre-span deflection gauges is independent of truck weight and absolute rigidity, and it differs by a factor of 2.3 between A and B. The integral of a strain gauge at the zero-moment point of calibration A is nearly zero under A and 0.17 of the mid-span strain integral under B.

**Table 5.** Predicted discriminating measurements at Cầu Mây for a 25 t three-axle truck (design predictions from the field-test plan; not measured).

| Measured quantity | Calibration A | Calibration B |
|---|---|---|
| Integral ratio, N8 at 0.4L / N7 at mid-span | 0.121 | 0.284 |
| Peak girder rotation over pier T7 (µrad) | −58 | −29 |
| Strain integral at the zero-moment point of A (171.3 m) / at mid N7 | 0.006 | 0.17 |
| Frequency ratios $f_2/f_1$; $f_3/f_1$ (assumed mass) | 1.78; 2.30 | 1.59; 1.75 |

At 40 km/h the crossing of the 200 m unit takes 18.6 s, and $T_\mathrm{cr}/T_1 = 26$ with the modelled fundamental period, which satisfies the quasi-static condition of Section 6.

The in-service girder thus shows that a side-span deflection gauge on a layout near the prismatic blind locus is not identifiable from static acceptance data, that a centre-span gauge is, and that one tiltmeter or one integral ratio would close the gap.

---

## 6. Error budget

This section states the error terms of the integral estimator with their sensitivities and with the values that this paper measures or assumes. The budget is indicative: it is not an evaluation according to the GUM, because several entries are scenario ranges and the correlations between terms are not quantified.

### 6.1. Error terms

To first order, the relative error of BPM is the sum of the relative errors of the rigidity, of four times the span length, of the gain, of the speed and of the offset term of Eq. (12). SLM removes the structural terms, because they belong to $C$. Every other term survives as the difference between the target and reference crossings and vanishes only when the error is common to both. The offset term never cancels fully for one channel, because the sensitivity $L_\mathrm{tot}/I$ differs between crossings. Random noise is negligible, because integration averages it: in the laboratory, noise at half the transducer resolution gave a standard deviation of 0.07 % in the identified load. A single reference crossing adds its own independent error; averaging five or more reference crossings with a vehicle comparable to the screened traffic reduces it.

For a constant force crossing the laboratory beam, the quasi-static error is at most about 1 % for $T_\mathrm{cr}/T_1 \ge 8$ and below 4.2 % for $T_\mathrm{cr}/T_1 \ge 4$. Below 2.5 it exceeds 15 % and changes sign, mainly because the beam has not returned to its datum when the load leaves [53]. This bound omits vehicle–bridge interaction and road roughness, so it is a necessary condition, not a sufficient one. The NOR-BWIM records showed no speed effect over 10–28 m/s (Section 4.2).

### 6.2. Residual offset at bridge scale

Table 6 evaluates Eq. (12) for the Cầu Mây gauges with $L_\mathrm{tot} = 200$ m and the mean weighed truck of 25.06 t, over offsets from 0.02 mm to 0.5 mm. The lower values are of LVDT class. Absolute deflection on a 90 m span over water would usually come from a non-contact technique, whose residual offset after re-zeroing has to be established on site, since environmental effects act over the same window [54,55]; the authors' own deflection records from simply supported spans showed post-minus-pre level differences of up to 0.23 mm (Supplementary Material).

**Table 6.** Bias of a single-channel estimate caused by a residual offset $\varepsilon_0$, Eq. (12), for a 25.06 t truck; $L_\mathrm{tot}$ = 200 m. Ranges are over the joint admissible set of Section 5.3.

| Gauge | Model | $C$ (m²/kN) | 0.02 mm | 0.05 mm | 0.1 mm | 0.2 mm | 0.5 mm |
|---|---|---|---|---|---|---|---|
| N7, mid main span | joint set | 3.28–3.84 × 10⁻⁴ | 4.2–5.0 % | 11–12 % | 21–25 % | 42–50 % | 106–124 % |
| N7, mid main span | A / B | 3.61 / 4.05 × 10⁻⁴ | 4.5 / 4.0 % | 11 / 10 % | 23 / 20 % | 45 / 40 % | 113 / 101 % |
| N8, 0.4L | joint set | 3.00–9.39 × 10⁻⁵ | 17–54 % | 43–136 % | 87–271 % | 173–543 % | 433–1356 % |
| N8, 0.4L | A / B | 4.38 / 11.5 × 10⁻⁵ | 37 / 14 % | 93 / 35 % | 186 / 71 % | 372 / 142 % | 930 / 355 % |

At $\varepsilon_0 = 0.1$ mm a single centre-span gauge biases a 25 t truck by 21–25 %, and a single side-span gauge by 87–271 %. With present absolute-deflection technology, single-point integral weighing on a long-span girder is therefore marginal even at the best location. The offset-immune pair of Section 2.4 addresses exactly this term: it cancels the common-mode part of the offset and leaves only the independent part.

### 6.3. Transverse position and multiple presence

The constant belongs to the load path. On the five-span girder the far-lane constant was 0.81 of the near-lane value for the gauge average and 0.66–1.02 for individual gauges, and at Cầu Mây the readings across one section spread by up to 2.05 mm in the eccentric N7 case, about 13 % of the mean reading. A single channel therefore carries the transverse position of the vehicle as an error term unless the lane is identified and lane-specific constants are used. Several vehicles on the structure return their combined weight: superposition held within 7–8 % on the five-span girder. A crossing of the 200 m Cầu Mây unit takes 12.4 s at 60 km/h, and every crossing that overlaps another vehicle in that window must be discarded or treated as a group. The fraction of usable isolated crossings depends on the traffic and was not quantified.

**Table 7.** Indicative sensitivity budget of the integral estimator. Values are those measured or assumed in this paper; they are not combined.

| Term | Sensitivity | Cancels in SLM? | Value in this paper |
|---|---|---|---|
| Flexural rigidity $EI$ | 1 | yes | BPM only; Cầu Mây N8 shape factor varies 6.5-fold over the static set |
| Span length | 4 | yes | BPM only |
| Gain | 1 | if not recalibrated between crossings | not evaluated |
| Reference weighing $P_0$ | 1 | no | laboratory: accuracy class [NEED VALUE]; field: day-1 weights driver-reported |
| Residual offset $\varepsilon_0$ | $L_\mathrm{tot}/I$ | only with zero-sum weights, Eq. (14) | Table 6; NOR-BWIM integral noise 10 % (day 1) and 35 % (day 2) per crossing at the reference gauge |
| Speed | 1 | no | NOR-BWIM: slope −3.6 ± 5.8 % per 10 m/s, not resolved |
| Dynamics | 1 | partly | ≤ 1 % for $T_\mathrm{cr}/T_1 \ge 8$ (constant force) |
| Transverse position | lane-dependent $C$ | no, unless lane-specific | NOR-BWIM $C_B/C_A$ = 0.81; Cầu Mây spread 2.05 mm |
| Multiple presence | group weight | – | superposition 0.92–0.93 |
| Linearity, seating | 1 | no | laboratory step 1.010 → 1.017 |
| Random noise | < 0.1 | no | 0.07 % (laboratory) |

In the laboratory the reference record and the load-dependent step limit SLM to 0.6–0.7 %. In the field, slow drift, lane and speed dominate. The method is therefore proposed for preliminary overload screening, with the decision threshold set apart from the legal limit and the design live loads [56,57]; setting that threshold needs field calibration beyond this study.

---

## 7. Design workflow and recommendations

The results combine into a procedure for designing load-monitoring channels on a continuous girder before installation.

1. **Constants.** For each candidate channel and position, compute $C$ from one static analysis under a uniform unit load on each lane, Eq. (2). Use Eqs. (4)–(9) for prismatic two- and three-span beams.
2. **Blindness.** Locate the blind loci of Table 1. Keep strain gauges out of the ring $|N_M|<0.2$ around every zero-moment point, including gauges set back from a pier to clear the diaphragm. Keep deflection gauges out of the near-blind bands, for example $1.385<\rho_L<1.525$ for a mid-span gauge on two spans and $1.621<\beta<1.775$ for a mid side-span gauge on three spans.
3. **Conditioning.** Report $N_M$ for strain (no reference stiffness needed), $N_w$ with its $EI_\mathrm{ref}$ for deflection, and $R$ for both. Rank locations by $|R|$ and $|N|$ together; a small $N$ with $R$ near 1 is restraint, not cancellation.
4. **Boundary robustness.** Evaluate $C$ over the plausible range of pier stiffness. For a symmetric girder, Eq. (15) gives the whole curve from the pinned and fixed constants. Avoid locations with large $C_\infty/C_0$ or $B_m$, or plan the measurement that identifies $\kappa$: a tiltmeter on a monolithic pier, an identified first frequency, or an integral ratio between two gauges.
5. **Placement.** Place sensors at the extremes of the uniform-load response of each channel type: the maximum for the main signal, and the minimum (a support or the most negative point) for a second sensor when offsets are correlated.
6. **Estimator.** Use SLM with a weighed vehicle comparable to the screened traffic, averaging at least five reference crossings, and lane-specific constants. With two or more channels of one type, use zero-sum weights, Eq. (14), and estimate the common-mode fraction $\rho$ from the quiet segments of simultaneous channels. Use BPM only where the location is well conditioned and the structure is known; on box girders with deck-mounted gauges, a beam model does not give the constant.
7. **Offset and dynamics.** Evaluate $P_\varepsilon$, Eq. (12), for the residual offset that the instrumentation actually achieves after re-zeroing, and compare it with the lightest vehicle to be screened. Check $T_\mathrm{cr}/T_1 \ge 8$ with the measured fundamental frequency.
8. **Processing.** Integrate in space over the complete crossing, re-zero before and after each crossing, reject records whose end levels differ beyond a tolerance, remove dynamics with a low-pass filter well below $f_1$ and never with a high-pass filter, and discard overlapping crossings.

The procedure positions the integral as a reduced alternative to influence-line BWIM, not a competitor. It returns the gross weight of a vehicle or group, needs only the scalar constant of each channel instead of an influence line, and involves one weighted sum instead of a regularised inversion. Its natural role is low-cost screening across many continuous structures, with instrumented BWIM or enforcement weighing reserved for the vehicles it flags. Influence-line BWIM does not suffer the blindness of a single integral at the loci of Table 1, because it fits the whole record shape.

Several limitations remain. The laboratory beam had equal spans and statically positioned loads, the invariance was tested there only indirectly, and the predicted blind configuration has not been tested. The field verification rests on one public dataset with two axle counts and four trucks, with no gauge at a zero-moment point. The in-service application uses static data, a two-dimensional model with assumed depth law and equal pier springs, and a frequency interpretation that the available report cannot confirm. The treatment is one-dimensional along each lane.

---

## 8. Conclusions

This paper set out criteria for designing channels that monitor the total load on continuous girder bridges. The main findings are as follows.

1. For any linear response channel, the integral over a complete quasi-static crossing equals the total load times the channel's response to a uniform unit load. One static analysis therefore gives the constant, the blind loci and the optimal placement of every candidate channel.
2. Strain channels are blind at every zero of the uniform-load moment diagram, which every continuous girder has: at $0.75L$ for two equal spans, and generally at $\xi_0 = 1-\mu/4$. Deflection channels are blind only near particular span ratios, such as $(3+\sqrt{33})/6$ for two spans and 1.7006 for a mid side-span gauge on three symmetric spans. The strain indicator needs no reference stiffness, and the cancellation ratio separates cancellation from restraint on haunched girders.
3. Among invariant linear estimators, generalised least squares across channels is optimal, and the uniform weight within a channel is the only one invariant for every structure. Zero-sum weights remove any common-mode offset or drift exactly, and optimal sensors lie at the extremes of the uniform-load response.
4. On public moving-truck records from a five-span continuous box girder, a 5-axle and a 3-axle truck gave the same constant (ratio 0.999 ± 0.140), the integral was speed-independent over 10–28 m/s, superposition held within uncertainty, and one weighed reference predicted the other trucks within 6.5–7.0 % mean absolute error on the quieter day. Gauges at one section had constants differing by up to 2.7 times, so the constant should come from a weighed vehicle, not from a beam model.
5. On a 55 + 90 + 55 m box girder, two static readings bound the pier-to-girder stiffness ratio only from below. The side-span deflection index lies anywhere between 0.12 and 0.82 (0.12–0.39 if the measured frequencies are the third mode), whereas the centre-span index stays at 0.19–0.29. A residual offset of 0.1 mm would bias a 25 t truck by 21–25 % at mid main span, so baseline stability, not the estimator, limits single-point deflection weighing on long spans.

The next steps are the moving-load test designed for the in-service girder, laboratory tests of the blind configuration and of fixed total load at several spacings, and a field test of the offset-immune pair.

---

## Appendix A. Closed forms for two- and three-span beams

For unequal spans the uniform-load support moment of a two-span beam is $M_B = -q_0(L_1^3/EI_1+L_2^3/EI_2)/[8(L_1/EI_1+L_2/EI_2)]$. Superposing the simply supported uniform-load deflection of span 1 and the deflection due to $M_B$, evaluating at $x_m$ and dividing by $q_0$ gives Eq. (5) with $\mu = -8M_B/(q_0L_1^2)$, which is $\mu_\mathrm{2span}$ of Eq. (4). Setting $F = 0$ factors as $(1-\xi)(1+\xi-\xi^2)$ and gives Eq. (6). With uniform stiffness, the blind condition for a mid-span sensor is $3\rho_L^2-3\rho_L-2=0$, and maximising $F$ over $\xi$ at $\mu = 1$ gives $8\xi^2-\xi-1=0$, hence Eq. (7). In units of $L_1^4/(192EI_1)$, the positive contribution of the instrumented span varies only between 1.50 and 2.00 for $\rho_L$ from 0.5 to 2.0, whereas the negative contribution of the adjacent span sweeps from −0.125 to −4.00; the degeneracy is driven almost entirely by the adjacent span.

For the symmetric three-span beam the three-moment equation gives $M_B = M_C = -q_0L_s^2\mu/8$ with $\mu_\mathrm{3span}$ of Eq. (4). Three equal spans give $\mu = 4/5$ and a mid side-span constant 1.3 times the two-span value. The optimal side-span position solves $8\xi^3-(12-3\mu)\xi^2+(2-\mu)=0$. The near-blind band at mid side span runs from the root of $30\beta^3-69\beta-16=0$ (1.621) to that of $10\beta^3-27\beta-8=0$ (1.775). A mid main-span deflection sensor is blind at $\beta = 0.9647$. For a sensor at $\eta = x/L_m$ in the main span, $192EI_mC_m/L_m^4 = 8[\eta(1-2\eta^2+\eta^3)-\nu\eta(1-\eta)]$ with $\nu = 3(\rho_{EI}+\beta^3)/[\beta^2(2\rho_{EI}+3\beta)]$. Asymmetric layouts follow from the three-moment equations solved symbolically (Supplementary Material); with the sensor at mid span 1 and $L_3/L_2$ between 0.3 and 0.6, the blind ratio $L_1/L_2$ stays between 0.587 and 0.592.

**Table A.1.** Symmetric three-span beam, uniform rigidity: optimal side-span position $\xi^*$ and deflection indicator $N_w$.

| $\beta$ | $\mu$ | $\xi^*$ | $N_w$ at $\xi^*$ | $N_w$ at $\xi = 1/2$ |
|---|---|---|---|---|
| 1.0 | 0.800 | 0.4460 | 1.322 | 1.300 |
| 1.2 | 0.9743 | 0.4251 | 1.076 | 1.039 |
| 1.4 | 1.208 | 0.3875 | 0.7585 | 0.6884 |
| 1.5 | 1.346 | 0.3582 | 0.5807 | 0.4808 |
| 1.636 | 1.558 | 0.2994 | 0.3316 | 0.1632 |
| 1.7 | 1.666 | 0.2608 | 0.2202 | 0.0015 |

## Appendix B. General channels and invariant weights

For a prismatic span with hogging end parameters $m_l$, $m_r$ and $\xi = s/L$, the indicators normalised to the simply supported reference are $N_w = 8\Phi$ with $\Phi = \xi(1-2\xi^2+\xi^3)-\tfrac{m_l}{2}(2\xi-3\xi^2+\xi^3)-\tfrac{m_r}{2}(\xi-\xi^3)$, $N_\theta = 24EI\,C_\theta/L^3 = \Phi'(\xi)$, $N_M$ of Eq. (9) and $N_V = 2C_V/L = 1-2\xi+(m_l-m_r)/4$. For the two-span beam, $(m_l, m_r) = (0, \mu)$ in span 1 and $(\mu/\rho_L^2, 0)$ in span 2; for the symmetric three-span beam, $(0, \mu)$ in the side span and $(\mu/\beta^2, \mu/\beta^2)$ in the main span. Strain zeros solve $4\xi^2-(4+m_l-m_r)\xi+m_l=0$. The verification covered two-span, symmetric and asymmetric three-span and four-span beams, zero-moment positions, ten blind configurations, the theorem itself for a two-truck convoy on piecewise-prismatic girders with elastic pier springs (relative error 2.8 × 10⁻⁹), and the haunched Cầu Mây FE against an independent force-method solution (5.4 × 10⁻¹⁰). Truncating the record when the first axle leaves changed the integral by up to 59 % (rotation) and 10 % (moment) on the two-span example.

For the most general linear estimator $\hat P = \sum_j\int g_j(x)z_j(x)\,\mathrm{d}x$, the mean is $\sum_aP_ah(s_a)$ with $h(s) = \sum_j\int g_j(x)\eta_j(x-s)\,\mathrm{d}x$. If $h$ must be constant in $s$ for every set of influence lines supported on $[0, L]$, then $\int_0^L[g(u+s)-g(u+s')]\eta(u)\,\mathrm{d}u = 0$ for every admissible $\eta$, so $g(u+s) = g(u+s')$ almost everywhere, and steps of length at most the entry-shift range connect any two points of the record. Each $g_j$ is therefore constant, and the only freedom lies across channels.

## Appendix C. Identifiability: sensitivities and Möbius law

Let $G = K^{-1}$ with $K = \alpha K_g + kK_p$, where $K_p$ has a unit entry on each inner-pier rotational degree of freedom, and $C_m = e_m^\top Gq$ with $q$ the consistent uniform load. Then $\mathrm{d}C_m/\mathrm{d}k = -\sum_i\theta_{m,i}\theta_{q,i}$, where $\theta_{m,i}$ and $\theta_{q,i}$ are the pier rotations under a unit load at the gauge and under the uniform load, and $S_\alpha + S_k = -1$ by Euler's theorem, because $C_m$ is homogeneous of degree −1 in $(\alpha, k)$. Mirror symmetry decouples the symmetric and antisymmetric pier-rotation patterns, the uniform load excites only the antisymmetric one, and the Sherman–Morrison formula gives Eq. (15) with $1/k_g$ the antisymmetric pier flexibility of the girder at $k = 0$. For the Cầu Mây model the law holds to a relative error of 5 × 10⁻⁶ over $k = 10^5$–$10^{12}$ kN m/rad. With two static readings the Fisher matrix has a determinant proportional to $(S_{y8}-S_{y7})^2$, which vanishes at the minimum of the ratio misfit. A frequency adds a row with the mass as nuisance parameter; frequency ratios depend on $\kappa$ alone. A pier rotation adds a row without nuisance. Unequal pier stiffnesses would bring in the symmetric pattern, which Eq. (15) does not cover.

## Appendix D. Laboratory data

**Table D.1.** Mid-span deflection of the first span (mm), mean of three cycles. Single load 40.64 N; analytical values from the closed-form influence line.

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

---

## Computational Implementation

All analyses were implemented by the authors in reproducible scripts: the closed forms and their FE verification, the multi-channel estimators, placement study and Monte Carlo simulation, the identifiability analysis of the in-service girder, the processing of the public field records and the laboratory evaluation. Generative artificial intelligence was used as an assistance tool during code development and debugging. Every equation and numerical output was checked independently against an analytical, finite element or convergence-based route, and the scripts and the console output of each run are provided as supplementary material.

## Data Availability

The field strain records analysed in Section 4 are publicly available in the NOR-BWIM dataset (figshare, https://doi.org/10.7294/26880898.v1, CC0) [50]. The laboratory deflection data are given in full in Appendix D. The derived data behind every figure and table, the analysis scripts and the console output of each run are provided as supplementary material. The Cầu Mây load test was performed by an author of this paper, and the authors are permitted to publish the processed data (static deflection readings, truck positions, weighed truck masses and reported frequencies), which are available at [NEED VALUE: repository name and DOI].

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

The supplementary material contains: (i) the analysis scripts and the console output of each run; (ii) the derived data behind every figure and table; (iii) the Monte Carlo verification of the multi-channel estimators, the structure-aware invariant weights and the full placement grid; (iv) the quadrature study and the laboratory Monte Carlo analysis; (v) the asymmetric three-span closed forms and their FE verification; (vi) the moving-force analysis behind the dynamic bound of Section 6.1; (vii) the deflection records of two simply supported bridges (Gie Cuc I and Phuong Do), which illustrate baseline handling and low-pass filtering; (viii) additional field figures (speed, lane and superposition, beam-model observability, gauge ratios, and the synthetic records of the dataset authors); (ix) the Cầu Mây indicators in graphical form and the identifiability maps; (x) the predicted records and sensor layout of the planned Cầu Mây field test.

---

## References

[1] Y. Fan, J. Zhu, J. Pei, Z. Li, Analysis for Yangmingtan Bridge collapse, Eng. Fail. Anal. 56 (2015) 20–27. https://doi.org/10.1016/j.engfailanal.2015.05.003

[2] H.M. Salem, H.M. Helmy, Numerical investigation of collapse of the Minnesota I-35W bridge, Eng. Struct. 59 (2014) 635–645. https://doi.org/10.1016/j.engstruct.2013.11.022

[3] S. Invernizzi, F. Montagnoli, A. Carpinteri, Very high cycle corrosion fatigue study of the collapsed Polcevera bridge, Italy, J. Bridge Eng. 27 (1) (2022) 04021102. https://doi.org/10.1061/(ASCE)BE.1943-5592.0001807

[4] M. Morgese, F. Ansari, M. Domaneschi, G.P. Cimellaro, Post-collapse analysis of Morandi's Polcevera viaduct in Genoa, Italy, J. Civ. Struct. Health Monit. 10 (2020) 69–85. https://doi.org/10.1007/s13349-019-00370-7

[5] R. Ventura, B. Barabino, G. Maternini, Estimating the frequency of traffic overloading on road bridges, J. Traffic Transp. Eng. (Engl. Ed.) 11 (4) (2024) 776–796. https://doi.org/10.1016/j.jtte.2023.11.005

[6] F. Fattorini, W. Salvatore, E. Renzi, G. Tamasi, Application to the territorial authorities of the "Guidelines for the classification and management of risk, for the evaluation of safety and for the monitoring of existing bridges". The case study of the Municipality of Rome, Procedia Struct. Integr. 44 (2023) 689–696. https://doi.org/10.1016/j.prostr.2023.01.090

[7] J. Gajda, R. Sroka, P. Burnos, M. Daniol, Long-term assessment of the properties of load sensors applied in weigh-in-motion systems, Sensors 25 (8) (2025) 2421. https://doi.org/10.3390/s25082421

[8] I. Al-Qadi, H. Wang, Y. Ouyang, K. Grimmelsman, J.E. Purdy, LTBP Program's Literature Review on Weigh-in-Motion Systems, Report FHWA-HRT-16-024, Federal Highway Administration, Washington, DC, 2016. https://rosap.ntl.bts.gov/view/dot/35735

[9] B. Jacob, E.J. OBrien, S. Jehaes (Eds.), Weigh-in-Motion of Road Vehicles: Final Report of the COST 323 Action, LCPC, Paris, 2002.

[10] U.S. Department of Transportation, Federal Highway Administration, Comprehensive Truck Size and Weight Study, Vol. II: Issues and Background, Report FHWA-PL-00-029, Washington, DC, 2000. https://rosap.ntl.bts.gov/view/dot/4747

[11] F. Moses, Weigh-in-motion system using instrumented bridges, Transp. Eng. J. ASCE 105 (3) (1979) 233–249. https://doi.org/10.1061/TPEJAN.0000783

[12] E.J. OBrien, M.J. Quilligan, R. Karoumi, Calculating an influence line from direct measurements, Proc. Inst. Civ. Eng. Bridge Eng. 159 (1) (2006) 31–34. https://doi.org/10.1680/bren.2006.159.1.31

[13] E.J. OBrien, C.W. Rowley, A. González, M.F. Green, A regularised solution to the bridge weigh-in-motion equations, Int. J. Heavy Veh. Syst. 16 (3) (2009) 310–327. https://doi.org/10.1504/IJHVS.2009.027135

[14] A. Žnidarič, J. Kalin, M. Kreslin, Improved accuracy and robustness of bridge weigh-in-motion systems, Struct. Infrastruct. Eng. 14 (4) (2018) 412–424. https://doi.org/10.1080/15732479.2017.1406958

[15] Y. Yu, C.S. Cai, L. Deng, State-of-the-art review on bridge weigh-in-motion technology, Adv. Struct. Eng. 19 (9) (2016) 1514–1530. https://doi.org/10.1177/1369433216655922

[16] T. Ojio, C. Carey, E.J. OBrien, C. Doherty, S.E. Taylor, Contactless bridge weigh-in-motion, J. Bridge Eng. 21 (7) (2016) 04016032. https://doi.org/10.1061/(ASCE)BE.1943-5592.0000776

[17] W. He, T. Ling, E.J. OBrien, et al., Virtual axle method for bridge weigh-in-motion systems requiring no axle detector, J. Bridge Eng. 24 (9) (2019) 04019086. https://doi.org/10.1061/(asce)be.1943-5592.0001474

[18] S.S. Law, T.H.T. Chan, Q.H. Zeng, Moving force identification: a time domain method, J. Sound Vib. 201 (1) (1997) 1–22. https://doi.org/10.1006/jsvi.1996.0774

[19] T.H.T. Chan, S.S. Law, T.H. Yung, X.R. Yuan, An interpretive method for moving force identification, J. Sound Vib. 219 (3) (1999) 503–524. https://doi.org/10.1006/jsvi.1998.1904

[20] S.S. Law, X.Q. Zhu, Study on different beam models in moving force identification, J. Sound Vib. 234 (4) (2000) 661–679. https://doi.org/10.1006/jsvi.2000.2867

[21] X.Q. Zhu, S.S. Law, Moving load identification on multi-span continuous bridges with elastic bearings, Mech. Syst. Signal Process. 20 (7) (2006) 1759–1782. https://doi.org/10.1016/j.ymssp.2005.06.004

[22] L. Deng, C.S. Cai, Identification of dynamic vehicular axle loads: theory and simulations, J. Vib. Control 16 (14) (2010) 2167–2194. https://doi.org/10.1177/1077546309351221

[23] Z. Chen, Y. Fang, X. Kong, L. Deng, Identification of multi-axle vehicle loads on beam type bridge based on minimal residual norm steepest descent method, J. Sound Vib. 563 (2023) 117866. https://doi.org/10.1016/j.jsv.2023.117866

[24] S. Luo, J. Jiang, F. Zhang, M.S. Mohamed, Distributed dynamic load identification of beam structures using a Bayesian method, Appl. Sci. 13 (4) (2023) 2537. https://doi.org/10.3390/app13042537

[25] J. Jiang, S. Luo, M.S. Mohamed, Z. Liang, Real-time identification of dynamic loads using inverse solution and Kalman filter, Appl. Sci. 10 (19) (2020) 6767. https://doi.org/10.3390/app10196767

[26] T. Kapoor, H. Wang, A. Núñez, R. Dollevoet, Physics-informed machine learning for moving load problems, J. Phys. Conf. Ser. 2647 (2024) 152003. https://doi.org/10.1088/1742-6596/2647/15/152003

[27] T. Ojio, K. Yamada, Bridge weigh-in-motion systems using stringers of plate girder bridges, in: Proceedings of the Third International Conference on Weigh-in-Motion (ICWIM3), Orlando, FL, 2002, pp. 209–218.

[28] A.J. Cardini, J.T. DeWolf, Implementation of a long-term bridge weigh-in-motion system for a steel girder bridge in the interstate highway system, J. Bridge Eng. 14 (6) (2009) 418–423. https://doi.org/10.1061/(ASCE)1084-0702(2009)14:6(418)

[29] K. Helmi, B. Bakht, A. Mufti, Accurate measurements of gross vehicle weight through bridge weigh-in-motion: a case study, J. Civ. Struct. Health Monit. 4 (3) (2014) 195–208. https://doi.org/10.1007/s13349-014-0076-5

[30] M. Lydon, S.E. Taylor, D. Robinson, A. Mufti, E.J. OBrien, Recent developments in bridge weigh in motion (B-WIM), J. Civ. Struct. Health Monit. 6 (1) (2016) 69–81. https://doi.org/10.1007/s13349-015-0119-6

[31] J. Yang, P. Hou, C. Yang, Study on the method of moving load identification based on strain influence line, Appl. Sci. 11 (2) (2021) 853. https://doi.org/10.3390/app11020853

[32] J. Yang, P. Hou, C. Yang, Investigation on the moving load identification for bridges based on long-gauge strain sensing and skew-Laplace fitting, Smart Mater. Struct. 32 (8) (2023) 085026. https://doi.org/10.1088/1361-665x/ace4ac

[33] J. Zhu, C. Wang, T. Qi, Y. Zhou, Vehicle load identification on orthotropic steel box beam bridge based on the strain response area, Appl. Sci. 12 (23) (2022) 12394. https://doi.org/10.3390/app122312394

[34] P. Agüero-Barrantes, R.E. Christenson, S. Lobo-Aguilar, Utilizing Kriging metamodeling to provide practical and effective bridge weigh-in-motion, J. Bridge Eng. 28 (2) (2023) 04022138. https://doi.org/10.1061/jbenf2.beeng-5760

[35] P. Agüero-Barrantes, S. Lobo-Aguilar, R.E. Christenson, Sparse sensing bridge weigh-in-motion for single-span bridges, Métodos y Materiales 11 (2021) 43–53. https://doi.org/10.15517/mym.v11i0.46400

[36] N. Zolghadri, M.W. Halling, N.R. Johnson, P.J. Barr, Field verification of simplified bridge weigh-in-motion techniques, J. Bridge Eng. 21 (6) (2016) 04016063. https://doi.org/10.1061/(asce)be.1943-5592.0000930

[37] S. Shi, M. Yarnold, S. Hurlebaus, J. Mander, Evaluation of a load cell-based bridge weigh-in-motion system, Transp. Res. Rec. 2679 (2) (2025) 535–549. https://doi.org/10.1177/03611981241263336

[38] A. Döring, M. Vogelbacher, O. Schneider, Investigations of ratio-based integrated influence lines as features for bridge-damage detection, Infrastructures 8 (4) (2023) 72. https://doi.org/10.3390/infrastructures8040072

[39] D. Huang, Y. Lu, Influence line theory supported single sensor-based strain feature for bridge defect diagnosis, Struct. Health Monit. (2025), online first. https://doi.org/10.1177/14759217251376931

[40] Q.B. Nguyen, T. Hoang, H.S. Nguyen, [Determination of the load applied on a simply supported beam based on measured deflection data], J. Sci. Technol. Civ. Eng. (HUCE) 18 (2V) (2024) 61–71 (in Vietnamese). https://doi.org/10.31814/stce.huce2024-18(2V)-05

[41] M.T.A. Chaudhary, M. Morgese, T.W. Taylor, F. Ansari, Method and application for influence-line-free distributed detection of gross vehicle weights in bridges, Structures 73 (2025) 108298. https://doi.org/10.1016/j.istruc.2025.108298

[42] H. Wu, H. Zhao, J. Liu, Z. Hu, A filtering-based bridge weigh-in-motion system on a continuous multi-girder bridge considering the influence lines of different lanes, Front. Struct. Civ. Eng. 14 (5) (2020) 1232–1246. https://doi.org/10.1007/s11709-020-0653-0

[43] A. Moghadam, M. AlHamaydeh, R. Sarlo, Bridge-weigh-in-motion approach for simultaneous multiple vehicles on concrete-box-girder bridges, Autom. Constr. 137 (2022) 104179. https://doi.org/10.1016/j.autcon.2022.104179

[44] A. Moghadam, M. AlHamaydeh, R. Sarlo, Nothing-on-road bridge-weigh-in-motion used for long-span, concrete-box-girder bridges: an experimental case study, J. Struct. Integr. Maint. 8 (2) (2023) 79–90. https://doi.org/10.1080/24705314.2023.2165606

[45] A. Moghadam, M. AlHamaydeh, R. Sarlo, Dual-purpose procedure for bridge health monitoring and weigh-in-motion used for multiple-vehicle events, Autom. Constr. 148 (2023) 104768. https://doi.org/10.1016/j.autcon.2023.104768

[46] C. Zhou, C. Demartino, Y. Narazaki, Y. Xu, E. Chatzi, B.F. Spencer, Optimal sensor placement for bridge weigh-in-motion using an augmented Kalman filter, Mech. Syst. Signal Process. 241 (2025) 113522. https://doi.org/10.1016/j.ymssp.2025.113522

[47] J. Zhang, Y. Liu, X. Fan, An AR(1)-Tikhonov-SVD-GCV framework for stochastic moving load identification driven by bridge multi-point deflection data, Structures 88 (2026) 111844. https://doi.org/10.1016/j.istruc.2026.111844

[48] Z. Shen, W. Peng, X. Zhang, et al., A lightweight weigh-in-motion system based on vehicle-induced bridge deflection and impact dynamic responses, Int. J. Struct. Stab. Dyn. (2026), online. https://doi.org/10.1142/s0219455427503664

[49] Y. Zhou, Z. Feng, S.-K. Di, Z.-J. Jia, A novel approach for bending stiffness inversion and rapid evaluation of continuous beam bridges based on a deflection influence line, Struct. Control Health Monit. 2026 (2026) 1361157. https://doi.org/10.1155/stc/1361157

[50] A. Moghadam, R. Sarlo, Nothing-on-Road Bridge-Weigh-In-Motion (NOR-BWIM) Dataset, version 1, University Libraries, Virginia Tech, figshare, 2024. https://doi.org/10.7294/26880898.v1

[51] A. Moghadam, Integration of Traffic and Structural Health Monitoring Systems Using a Novel Nothing-On-Road (NOR) Bridge-Weigh-In-Motion (BWIM) System, PhD dissertation, Virginia Polytechnic Institute and State University, Blacksburg, VA, 2022. http://hdl.handle.net/10919/111390

[52] A. Ghali, A.M. Neville, T.G. Brown, Structural Analysis: A Unified Classical and Matrix Approach, CRC Press, Boca Raton, 2017. https://doi.org/10.1201/9781315273006

[53] L. Frýba, Vibration of Solids and Structures under Moving Loads, 3rd ed., Thomas Telford, London, 1999.

[54] H. Sohn, Effects of environmental and operational variability on structural health monitoring, Philos. Trans. R. Soc. A 365 (1851) (2007) 539–560. https://doi.org/10.1098/rsta.2006.1935

[55] E.J. Cross, K.Y. Koo, J.M.W. Brownjohn, K. Worden, Long-term monitoring and data analysis of the Tamar Bridge, Mech. Syst. Signal Process. 35 (1–2) (2013) 16–34. https://doi.org/10.1016/j.ymssp.2012.08.026

[56] EN 1991-2:2003, Eurocode 1: Actions on Structures – Part 2: Traffic Loads on Bridges, CEN, Brussels, 2003.

[57] AASHTO, LRFD Bridge Design Specifications, 10th ed., American Association of State Highway and Transportation Officials, Washington, DC, 2024.

---

## Figure Captions

**Fig. 1.** Continuous beams considered: (a) two-span beam with instrumented span $L_1$, adjacent span $L_2 = \rho_LL_1$ and sensor at $\xi L_1$; (b) symmetric three-span beam with side spans $L_s$, main span $L_m = \beta L_s$ and side-span sensor at $\xi L_s$.

**Fig. 2.** Deflection observability of a three-span beam with uniform rigidity: (a) symmetric beam, $N_w$ over $\beta$ and the side-span sensor position $\xi$, with the blind locus (thick line), the near-blind band (hatched), the optimum $\xi^*(\beta)$ (dashed) and the Cầu Mây layout with a mid side-span sensor (open circle); (b) asymmetric beam, sensor at mid span 1, over $L_1/L_2$ and $L_3/L_2$. Colours are clipped at ±1.5.

**Fig. 3.** Indicators of four channels along prismatic girders, each normalised to the simply supported reference of its own span: deflection $N_w$, rotation $N_\theta$, strain or moment $N_M$ and shear $N_V$. (a) Equal two-span beam; (b) symmetric three-span beam with $\beta = 1.636$. The grey band marks $|N|<0.2$.

**Fig. 4.** Multi-channel estimation: (a) variance with two or three optimally placed sensors relative to the best single sensor, against the common-mode fraction $\rho$ of the offset; (b) standard deviation of the load against the offset level for single sensors and three-sensor designs; (c) offset-immune pair at $\rho = 1$ against the white-noise level. 2S-eq: equal two-span beam; 3S-b2.0: three-span beam with $\beta = 2$; CM-A, CM-B: Cầu Mây calibrations A and B.

**Fig. 5.** Laboratory two-span beam: (a) elevation and instrumentation; (b) mid-span deflection of the first span against the position of a single 40.64 N load, analytical and measured, with the residuals.

**Fig. 6.** NOR-BWIM strain records of three single-truck crossings of the five-span girder: a 5-axle and a 3-axle truck on day 2 and a 3-axle truck on day 1. Shaded: integration window; dashed: beam-model shape scaled to the reference gauge. The legend gives each gauge's integral $\int\varepsilon\,\mathrm{d}x$ (µε m).

**Fig. 7.** Invariance of $\int\varepsilon\,\mathrm{d}x/\mathrm{GVW}$ at the gauge common to both days, per crossing with one-standard-error bars from vehicle-free records; truck, axle count and speed are given below each point. Horizontal line: weighted mean.

**Fig. 8.** Cầu Mây girder, indicators along the girder for a prismatic model with pinned piers and for the haunched model under calibrations A and B: (a) deflection $N_w$; (b) strain $N_M$, with strain blind points; (c) strain indicator including the section gain $c/EI$, assuming $c\propto h$. Dotted lines: gauge positions N7, N8 at mid side span and N8 at 0.4L.

**Fig. 9.** Identifiability of the Cầu Mây pier stiffness from two static readings: (a) ratio of the measured-to-model ratios at N8 and N7 against $\kappa = k/\alpha$, with model-form variants (grey) and the admissible band; (b) N8 and N7 indicators and cancellation ratios along the static valley.
