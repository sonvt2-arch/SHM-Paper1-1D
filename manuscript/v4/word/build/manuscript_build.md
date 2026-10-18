# Blind loci and design criteria for integral load-monitoring channels on continuous girder bridges, with laboratory verification and an assessment on public field records

Quoc-Bao Nguyen^a^, Thai-Son Vu^a,\*^, Hung-Son Nguyen^a^

^a^ Faculty of Bridge and Road Engineering, Hanoi University of Civil Engineering, 55 Giai Phong, Bach Mai ward, 11618 Ha Noi, Viet Nam

\* Corresponding author: Thai-Son Vu. Tel.: +84 971 899 888. E-mail: sonvt2@huce.edu.vn

E-mail addresses: baonq@huce.edu.vn (Q.-B. Nguyen), sonvt2@huce.edu.vn (T.-S. Vu), sonnh@huce.edu.vn (H.-S. Nguyen)

---

## Abstract

Influence-area weigh-in-motion estimates gross weight from the area under a response record. That this area equals the response to a uniform unit load, and that channels can be combined by generalised least squares, is classical; this paper uses both to derive design criteria for continuous girders. It gives closed-form blind loci for deflection, strain, rotation and reaction channels on two- and three-span and haunched girders, including a near-blind ring for strain gauges set back from piers; indicators separating cancellation from restraint; a placement rule (sensors at the extremes of the uniform-load response, for strain of $cM_q/EI$); and a Möbius law for the effect of uncertain pier stiffness. A laboratory two-span beam confirms the integral within 1.2 %. On public moving-truck records from a five-span box girder, the reference weights vary so little that predicting the mean weight (2.0–2.2 % error) beats every estimator, so weight discrimination cannot be tested; a 5-axle/3-axle constant ratio of 0.98 (95 % CI 0.70–1.37) is consistent with invariance but inconclusive. Out of sample, generalised least squares with the measured noise covariance was worse than the plain gauge average (20.4 % against 11.9 % mean absolute error), because errors during crossings are much less correlated between gauges (0.63) than vehicle-free noise (0.92). On a 55 + 90 + 55 m box girder, two static readings leave the side-span deflection index (effective-rigidity normalisation) between 0.14 and 0.42, and a residual offset of 0.1 mm would bias a 25 t truck by 16–25 % at mid main span.

**Keywords:** Structural health monitoring; Sensor placement; Bridge weigh-in-motion; Continuous girder; Identifiability; Field assessment

---

## Nomenclature

| Symbol | Meaning |
|---|---|
| $A^+$ | positive part of the area under an influence line |
| $B_m$ | boundary-conditioning indicator $\lvert\partial\ln C_m/\partial\ln\kappa\rvert$ |
| $C_r$, $C_m$ | integral constant of channel $r$; of a deflection channel at $m$ (m²/kN) |
| $c$ | distance of the gauged fibre from the neutral axis (m) |
| $EI$, $EI_\mathrm{mid}$ | flexural rigidity; design value at mid main span (kN m²) |
| $I_r$ | record integral over a complete crossing, in space |
| $k$, $k_g$ | rotational stiffness of a monolithic pier; antisymmetric pier stiffness of the girder (kN m/rad) |
| $L_\mathrm{tot}$ | length of the integration record (m) |
| $M_q$ | bending moment under a uniform load $q_0$ over the whole path |
| $N_w$, $N_M$ | deflection and strain (moment) indicators, Eqs. (10) and (9) |
| $P_\mathrm{tot}$, $P_0$ | total load of a crossing; weighed reference load (kN) |
| $P_\varepsilon$ | offset-equivalent load $\varepsilon_0L_\mathrm{tot}/C$ (kN) |
| $R$ | cancellation ratio $C/A^+$ |
| $r_{87}$ | ratio of the measured-to-model ratios at gauges N8 and N7 |
| $w$ | weight vector of a multi-channel estimator |
| $\alpha$ | ratio of effective to design girder rigidity |
| $\beta$, $\rho_L$ | main-to-side span ratio (three spans); adjacent-to-instrumented span ratio (two spans) |
| $\varepsilon_0$ | residual zero offset after pre/post re-zeroing (mm) |
| $\eta_m$ | influence line of the channel at $m$ |
| $\kappa$ | pier-to-girder stiffness ratio $k/\alpha$ (kN m/rad) |
| $\mu$ | interior-moment parameter, $\mu=-8M_B/(q_0L_1^2)$ |
| $\rho$ | common-mode fraction of the offset or noise between channels |
| $\tau$ | tolerance on the static misfit of a gauge |
| $\xi$ | sensor position as a fraction of its span |
| BPM, SLM | beam-property method; standard-load method |

---

## 1. Introduction

Heavy vehicles above the design envelope shorten the life of highway bridges and, in extreme cases, contribute to collapse. A span of the Yangmingtan Bridge failed in 2012 under four overloaded trucks crossing together [1]. In other documented failures, heavy traffic acted together with design deficiencies or material degradation [2,3]. Knowing the loads that a bridge actually carries is therefore part of risk-informed asset management [4].

Pavement weigh-in-motion (WIM) is mature [5,6] and has codified accuracy classes [7], but it weighs the vehicle rather than the load on a particular bridge. Bridge weigh-in-motion (BWIM), introduced by Moses [8], fits the measured response to axle loads times influence-line ordinates. It now includes influence lines calibrated from measurements [9], regularised solutions [10], accuracy improvements [11,12], contactless sensing [13] and virtual-axle methods without axle detectors [14]. Nothing-on-road systems also estimate the transverse position of the vehicle [15]. Moving-force identification recovers axle-load histories in the time or frequency domain [16–18], on multi-span bridges [19] and with dynamic and Kalman-filter formulations [20–22]. These methods aim at axle loads and need several sensors, a structural model or a regularised inversion.

A simpler family estimates only the gross weight from the area under the response. Ojio and Yamada integrated the strain records of plate-girder stringers, multiplied the result by the speed and calibrated it against a truck of known weight [23]. The method has been used in long-term monitoring [24] and on a seven-span slab-on-girder bridge, where it was accurate to within 5 % for test trucks with well-estimated speeds [25,26]. Strain-area and strain-integral variants [27–29], shear-strain weighing [30], a sparse-sensing influence-area system that chose the number and location of strain gauges on a single-span bridge [31], simplified BWIM in the field [32] and load-cell reactions [33] followed. Yan et al. proposed a probabilistic, influence-line-free gross-weight scheme based on a transmissibility-like index [34]. A transmissibility is a ratio of response spectra, and at zero frequency a ratio of spectra equals the ratio of the record integrals that the standard-load method uses; the present paper asks instead where such integrals are observable on a continuous girder. The integral of the influence line has also served as a damage feature [35,36], and the present authors used the integral of mid-span deflection on a simply supported beam [37].

The identity behind all of these methods is classical: the area under an influence line equals the response to a uniform unit load, which is how design codes evaluate distributed lane loads [38]. So is the combination of several channels by generalised least squares (GLS), and its zero-sum variant is the familiar differential measurement against a reference. On continuous girders, however, the influence line changes sign over each interior support, and positive and negative areas partly cancel. Gross weight has been obtained without influence lines from distributed fibre-optic strain on a five-span continuous bridge [39], lane-specific influence lines were needed on a continuous multi-girder bridge [40], and long-span continuous box girders have been weighed from deck strain [41–43]. Optimal sensor placement for BWIM has been posed through an augmented Kalman filter [44], deflection-based load identification as a regularised stochastic problem [45,46], and measured deflection influence lines have been inverted for the stiffness of continuous girders [47]. None of these studies gives a criterion, available before installation, that says which channel at which position can observe the total load at all, how robustly to uncertain boundary conditions, and what a multi-channel integral estimator can deliver on real records.

This paper supplies such criteria. The identity and the GLS estimator are used, not claimed. The contributions are:

1. a closed-form catalogue of blind loci for deflection, strain, rotation, shear and reaction channels on two- and three-span and haunched girders, including the near-blind ring of strain gauges set back from the piers;
2. the strain indicator $N_M$, which needs no reference stiffness, the cancellation ratio $R$, which separates cancellation from restraint, and a corrected normalisation of the deflection indicator;
3. a placement rule: optimal sensors lie at the extremes of the uniform-load response, for strain at the extremes of $cM_q/EI$;
4. an identifiability analysis of the indicator under boundary uncertainty, in which the constant depends on pier stiffness through one ratio $\kappa = k/\alpha$ and a Möbius law, and which names the measurement that resolves it;
5. an assessment, on a laboratory beam and on public moving-truck records, of what single- and multi-channel integral estimators can and cannot deliver.

Section 2 develops the theory, Section 3 checks it in the laboratory, Section 4 assesses it on public field records, Section 5 applies it to an in-service box girder, and Sections 6 and 7 give the error budget and the design workflow.

---

## 2. Theory

This section states the classical identity with its validity envelope, then derives the blind loci, the indicators, the multi-channel estimator with its placement rule, and the identifiability of the constant. Derivations are in Appendices A–C.

### 2.1. Response-integral identity

Consider a linear-elastic structure whose properties do not change during a crossing, with any distribution $EI(x)$ and any linear elastic supports. A response channel at a fixed point $m$ is any fixed linear functional $r_m$ of the displacement field, measured from the unloaded state: the deflection $w(x_m)$, the rotation $w'(x_m)$, the bending moment, the fibre strain $\varepsilon = cM/EI$, the shear force or a support reaction. Let $\eta_m(x)$ be its influence line, with $\eta_m = 0$ outside the loaded path $[0, L]$. A convoy of axle loads $P_i$ at fixed offsets $a_i$ ($a_1 = 0$) crosses quasi-statically, so the record is

$$y_m(x)=\sum_{i=1}^{n}P_i\,\eta_m(x-a_i). \tag{1}$$

Integrating Eq. (1) over the complete crossing and substituting $u = x - a_i$ term by term gives

$$I_r=\int_0^{L+a_\mathrm{max}}y_m\,\mathrm{d}x=P_\mathrm{tot}\,C_r,\qquad C_r=\int_0^L\eta_m(u)\,\mathrm{d}u=\frac{r_m[q_0]}{q_0}, \tag{2}$$

where $r_m[q_0]$ is the response of the channel to a uniform load $q_0$ over the whole path. This is the classical influence-area identity [23,38]; the second equality needs superposition only. For a strain gauge,

$$C_\varepsilon=\frac{c_m\,M_q(x_m)}{EI_m\,q_0}. \tag{3}$$

The local section constants enter Eq. (3) only as a gain, so a strain channel is blind exactly at the zeros of the uniform-load moment diagram, for any $EI(x)$ and any elastic supports. At constant speed $v$ the time integral is $I_r/v$.

Eq. (2) holds under five conditions, each of which the later sections test. The structure must be linear and time-invariant during the crossing (Section 3 and the superposition test of Section 4.4). A quasi-static response is assumed (Section 6). Because the axles must follow the path on which $\eta_m$ is defined, each lane has its own constant (Section 4.4). A complete crossing is needed: truncating the record when the first axle leaves changes the rotation integral by up to 59 % on a two-span example (Appendix B). The record must be re-zeroed to the unloaded state, and any residual offset or slow drift enters the integral directly (Sections 2.3 and 4.3).

### 2.2. Closed-form blind loci

For a prismatic span under a uniform load, every channel is fixed by the two end moments. Write them as hogging parameters $m_l$ and $m_r$, with $m = -8M/(q_0L^2)$. For the instrumented span of a two-span beam and for the side span of a symmetric three-span beam, $(m_l, m_r) = (0, \mu)$, with the classical interior-moment parameter (Appendix A; [38])

$$\mu_\mathrm{2span}=\frac{1+\rho_L^3/\rho_{EI}}{1+\rho_L/\rho_{EI}},\qquad \mu_\mathrm{3span}=\frac{2(\rho_{EI}+\beta^3)}{2\rho_{EI}+3\beta}, \tag{4}$$

where $\rho_L$ and $\rho_{EI}$ are the adjacent-to-instrumented span and stiffness ratios of the two-span beam, and $\beta = L_m/L_s$ and $\rho_{EI} = EI_m/EI_s$ for three spans. The deflection constant at $\xi = x_m/L$ is

$$\frac{192EI\,C_m}{L^4}=8F(\xi,\mu),\qquad F(\xi,\mu)=\xi(1-2\xi^2+\xi^3)-\frac{\mu}{2}\,\xi(1-\xi^2). \tag{5}$$

Setting $F = 0$ gives the deflection blind condition on $\mu$ alone,

$$C_m=0\;\Leftrightarrow\;\mu=\mu_\mathrm{crit}(\xi)=\frac{2(1+\xi-\xi^2)}{1+\xi}, \tag{6}$$

which exists only for $1<\mu<2$. For a mid-span sensor on two spans of equal stiffness, the blind span ratio and the optimal sensor position are

$$\rho_{L,\mathrm{crit}}=\frac{3+\sqrt{33}}{6}=1.4574,\qquad \xi^*=\frac{1+\sqrt{33}}{16}=0.4215. \tag{7}$$

For the symmetric three-span beam with uniform rigidity and a mid side-span sensor, the blind main-to-side ratio is the positive root of $6\beta^3-15\beta-4=0$,

$$\beta_\mathrm{crit}=\sqrt{10/3}\,\cos\!\Big[\tfrac13\arccos\!\Big(\tfrac25\sqrt{6/5}\Big)\Big]=1.7006, \tag{8}$$

and the side-span blind locus ends at $\beta = 2\cos(\pi/9) = 1.8794$. The near-blind band $|N_w|<0.2$ (Section 2.3) covers $1.385<\rho_L<1.525$ on two spans and $1.621<\beta<1.775$ on three. Fig. 1 defines the notation, Fig. 2 gives the observability map, and Table A.1 the optimal side-span positions. All closed forms agree with finite element (FE) evaluations of Eq. (2) in 981 checks, with a maximum error of 8.1 × 10⁻¹¹ on the normalised indicators.

The strain channel follows from the same end moments:

$$N_M=\frac{8M_q(x_m)}{q_0L^2}=4\xi(1-\xi)-m_l(1-\xi)-m_r\xi,\qquad \xi_0=1-\frac{\mu}{4}. \tag{9}$$

The strain blind point $\xi_0$ in the instrumented or side span is $0.75L$ for two equal spans. In the main span of a symmetric girder, $m_l = m_r = \mu/\beta^2$ and the blind point lies at $\eta_0 = \tfrac12(1-\sqrt{1-\mu/\beta^2})$ of the main span from the pier: 0.276 for three equal spans and 0.177 for $\beta = 1.636$. Strain blind points exist in every span that has a sagging zone ($\mu<4$), so they are a property of every continuous girder, not of particular span ratios. The near-blind band $|N_M|<0.2$ forms a ring around each zero. For two equal spans it covers $0.676<\xi<0.812$, that is 0.19–0.32 of the span from the interior support. A gauge at the support section is well conditioned, with $|N_M| = \mu$, but a gauge set back from the pier to clear the diaphragm, or placed at a quarter point, can fall into the ring. Table 1 collects the blind loci of all channels; Fig. 3 shows the indicators along two prismatic girders.

**Table 1.** Blind loci of response channels under the uniform-load criterion, prismatic beams with $\rho_{EI} = 1$ unless stated. $\mu$ from Eq. (4).

| Channel | Blind where | Two-span beam (span 1) | Symmetric three-span beam |
|---|---|---|---|
| Strain, moment, curvature | zeros of $M_q$ | $\xi_0 = 1-\mu/4$ (0.75 at $\rho_L = 1$) | side $\xi_0 = 1-\mu/4$; main $\eta_0=\tfrac12(1-\sqrt{1-\mu/\beta^2})$ |
| Deflection | zeros of $w_q$ | $\mu = \mu_\mathrm{crit}(\xi)$, only for $1<\mu<2$; mid-span: $\rho_L = 1.4574$ | mid side span: $\beta = 1.7006$; locus ends at $\beta = 1.8794$ |
| Rotation | extrema of $w_q$ | end: $\mu = 2$ ($\rho_L = 1.6180$); pier: $\rho_L = 1$ for any $\rho_{EI}$ | end: $\beta = 2\cos(\pi/9)$; pier: $\beta = \sqrt{3/2}$ for any $\rho_{EI}$; mid main span: always |
| Shear | maxima of $M_q$ | $\xi = \xi_0/2$ | side $\xi_0/2$; mid main span: always |
| End reaction | no sagging zone in the end span | $\mu = 4$ ($\rho_L = 2.3028$) | $\mu = 4$ ($\beta = 2.6691$) |
| Interior reaction | never under a full uniform load | – | – |

Two identities in Table 1 are useful in practice. The end-reaction indicator equals the strain blind abscissa, $2R_A/(q_0L_1) = \xi_0$, for any $EI(x)$ and any pier springs, because statics of the end segment gives $M_q = R_Ax - q_0x^2/2$. The deflection blind locus ends where the end rotation vanishes, which explains the limit $2\cos(\pi/9)$.

### 2.3. Observability and conditioning indicators

Every estimator below divides by $C$, so to first order the sensitivity to measurement error scales as $1/|C|$. For a deflection channel the normalised indicator is

$$N_w=\frac{192EI_\mathrm{ref}\,C_m}{L^4}, \tag{10}$$

with $L$ the span containing the sensor. With this normalisation $N_w$ equals 2.5 at mid-span of a simply supported span and 1 at mid-span of each span of an equal two-span beam. $N_M$ of Eq. (9) and the rotation and shear indicators of Appendix B equal 1 for the simply supported reference. The near-blind thresholds used here, $|N_w|<0.2$ and $|N_M|<0.2$, are therefore not equivalent: expressed as a fraction of the simply supported mid-span value, they are 8 % for deflection and 20 % for strain. Both are design conventions; the bands quoted in Section 2.2 and Section 7 use them as stated. For a non-prismatic girder $N_w$ also depends on the choice of $EI_\mathrm{ref}$, and Section 5 shows that this choice can dominate the result. $N_M$ needs no reference stiffness: it is the uniform-load moment relative to the free simple-span moment, so its threshold keeps one meaning for any $EI(x)$. The section enters only through the gain $c/EI$ of Eq. (3). A second measure that needs no reference is the cancellation ratio

$$R=\frac{C}{A^+}=1-\frac{|A^-|}{A^+}, \tag{11}$$

the net influence area divided by its positive part. $R$ equals 1 for a simply supported span, 4/7 for the mid-span deflection of two equal spans, and 0 at a blind configuration. A small $N$ with $R$ near 1 indicates restraint, not cancellation. The strain influence line is more local than the deflection line, so at every prismatic location examined it cancels less: $R_\varepsilon = 0.667$ against $R_w = 0.571$ at mid-span of two equal spans.

Neither index carries the absolute signal level, on which the offset error depends. A residual offset $\varepsilon_0$, left after the record has been re-zeroed before and after the crossing, adds $\varepsilon_0L_\mathrm{tot}$ to the integral. With $I = CP$ the relative bias is

$$\Big(\frac{\delta P}{P}\Big)_{\varepsilon_0}=\frac{P_\varepsilon}{P},\qquad P_\varepsilon=\frac{\varepsilon_0L_\mathrm{tot}}{C}. \tag{12}$$

The offset-equivalent load $P_\varepsilon$ is the load at which the offset causes a 100 % bias. It combines sensor position, baseline stability and the lightest vehicle to be screened into one number.

### 2.4. Multi-channel estimation, offset immunity and placement

Let channel $j$, a deflection or strain, give the integral $I_j = C_jP + \varepsilon_{0,j}L_\mathrm{tot} + n_j$, with white noise $n_j$ and offsets that may be correlated between channels, and let $\Sigma$ be the covariance of the vector $I$. A linear estimator $\hat P = w^\top I$ is unbiased for every axle configuration if and only if $w^\top C = 1$. Minimising its variance under this constraint gives the GLS weights

$$w^\star=\frac{\Sigma^{-1}C}{C^\top\Sigma^{-1}C},\qquad \mathrm{Var}\,\hat P^\star=\big(C^\top\Sigma^{-1}C\big)^{-1}, \tag{13}$$

the Gauss–Markov best linear unbiased estimator. For one channel, Eq. (13) returns $\hat P = I/C$ with variance $\sigma_{P,\mathrm{noise}}^2 + P_\varepsilon^2$. Within one channel, the uniform weight is the only weight that keeps the integral invariant for every structure (Appendix B), which is the property the standard-load method needs. A record integrated uniformly in time weights space by $1/v(x)$, so the integral must be taken in space.

Adding $\sum_jw_j = 0$ for each channel type to $w^\top C = 1$ makes $\hat P$ insensitive to any disturbance shared by the channels: a constant offset, a drift, or motion of the reference frame. With equal noise and offset statistics, the variance becomes

$$\mathrm{Var}\,\hat P_\mathrm{imm}=\frac{\sigma^2\Delta x\,L_\mathrm{tot}+(1-\rho)\varepsilon_0^2L_\mathrm{tot}^2}{\sum_j(C_j-\bar C)^2}, \tag{14}$$

where $\rho$ is the common-mode fraction of the offset and $\Delta x$ the sampling interval. For two channels, $w = (1,-1)/(C_1-C_2)$, and a second sensor over a support ($C_2 = 0$) gives the differential measurement against a reference target. The white-noise variance rises by the factor $2C_1^2/(C_1-C_2)^2$, which is 1.65–2.0 on the beams studied. This price is small, because the white-noise term is a minute fraction of the offset term: their ratio $\sigma^2\Delta x/(\varepsilon_0^2L_\mathrm{tot})$ is about 5 × 10⁻⁶ at $\sigma = 0.01$ mm, $\varepsilon_0 = 0.1$ mm, $\Delta x = 0.1$ m and $L_\mathrm{tot} = 220$ m. The zero-sum weights only make sense within one channel type; mixing strain and deflection requires separate constraints.

If the noise statistics do not depend on position, $1/\mathrm{Var}$ is a convex quadratic in the vector of constants $C(x_j)$, for both Eqs. (13) and (14). A convex function on a box attains its maximum at a vertex, so optimal sensors lie at the maximum and the minimum of $C(x)$. For deflection this is $w_q(x)/q_0$. For strain it is $c\,M_q(x)/(EI\,q_0)$, which includes the section gain; on a haunched girder the extremes of $C_\varepsilon$ and of $M_q$ differ. Independent offsets call for clustering at the maximum; correlated offsets call for one sensor at the minimum. A brute-force search over 96 cases found no design better than the vertex design, and a Monte Carlo study with 10⁵ random axle configurations per case confirmed that the estimators are unbiased and that the variances of Eqs. (13) and (14) hold to within 0.6 % (Supplementary Material). Fig. 4 shows the gain over the best single sensor.

These results hold for the noise model assumed, and Section 4.3 shows that the model can fail on real records. Offset immunity helps only if the disturbance is common-mode during the crossings themselves, not merely in vehicle-free periods. On the field records the vehicle-free noise was strongly common-mode, but the crossing-to-crossing errors were not, and GLS weights built from vehicle-free noise did worse than the plain average. The covariance $\Sigma$, and hence $\rho$, should therefore be estimated from the residuals of calibration crossings, with enough crossings to avoid over-fitting, and not from quiet windows alone.

### 2.5. Identifiability of the indicator under boundary uncertainty

A girder with monolithic piers has a stiffness matrix $\alpha K_g + kK_p$, where $\alpha$ scales the girder rigidity and $k$ is the rotational stiffness of each pier. Every static response then scales as $\alpha^{-1}g(\kappa)$ with $\kappa = k/\alpha$, so two static readings fix $\alpha$ for each $\kappa$ and constrain $\kappa$ only through their ratio. For a mirror-symmetric girder with equal piers, the uniform load excites only the antisymmetric pier-rotation pattern, and the Sherman–Morrison formula gives (Appendix C)

$$C_m(\alpha,\kappa)=\frac{1}{\alpha}\Big[C_\infty+\frac{C_0-C_\infty}{1+\kappa/k_g}\Big]. \tag{15}$$

$C_0$ and $C_\infty$ are the constants for pinned and fixed piers at $\alpha = 1$, and $k_g$ is the girder's own antisymmetric pier stiffness. The ratio $C_\infty/C_0$ is the full range that pier fixity can produce at a gauge. The local measure is the boundary-conditioning indicator $B_m = |\partial\ln C_m/\partial\ln\kappa|$. For a symmetric prismatic three-span beam with rotational springs $k$ at the piers, slope-deflection gives

$$\mu(K)=1+\frac{\beta(2\beta^2-3)}{3\beta+2\rho_{EI}+\beta K},\qquad K=\frac{kL_s}{EI_s}. \tag{16}$$

Eq. (16) replaces $\mu_\mathrm{3span}$ in Eq. (5) and agrees with FE to 4.4 × 10⁻⁷. For $\beta = 1.636$ the side-span index at $\xi = 0.4$ rises from 0.287 (pinned) to 1.037 (fixed), whereas the mid main-span index falls from 0.755 to 0.500. Rotational restraint moves the side-span gauge away from blindness but makes its constant strongly dependent on $k$.

From one static analysis, the theory thus gives the constant of every channel, its blind loci, the optimal placement and its sensitivity to the boundary conditions.

---

## 3. Laboratory verification

This section checks the deflection influence line, the integral and the two single-channel estimators on a two-span beam. The loads were positioned statically, so the test checks the model and the algorithm, not performance under moving traffic.

The specimen was a steel hollow square tube, 25 mm × 25 mm × 2.03 mm ($I = 16\,530$ mm⁴, $E = 200$ GPa), on three supports forming two equal spans of 2500 mm. The theoretical constant at mid-span of the first span is $C_m = l^4/(192EI) = 61.54$ mm²/N. Deflection at that point was measured with a linear variable differential transformer of 0.005 mm resolution while calibrated weights were suspended at 250 mm steps along the traverse. Three configurations were tested: a single 40.64 N reference load, two loads 250 mm apart, and three loads. The order of the three-load group was not recorded independently and was chosen by fit (root-mean-square residual 0.030 mm against 0.55 mm for the reverse spacing), so that test is not fully independent. The specimen, the influence line and the data are in the Supplementary Material.

The analytical influence line matched the single-load record within 0.0126 mm, 0.44 % of the peak. The trapezoidal rule on the 250 mm grid underestimates the exact single-load integral by 0.500 %; it is used throughout because Simpson's rule loses its advantage when the kinks of trailing loads fall inside its panels.

**Table 2.** Identified total loads against direct weighing (trapezoidal rule).

| Configuration | Weighed (N) | BPM (N) | BPM deviation | SLM (N) | SLM deviation |
|---|---|---|---|---|---|
| Two loads | 66.99 | 67.73 | +1.10 % | 67.40 | +0.61 % |
| Three loads | 125.08 | 126.57 | +1.19 % | 125.95 | +0.70 % |

Table 2 compares the beam-property method (BPM), $P = I/C_m$, with the standard-load method (SLM), $P_t = P_0I_t/I_0$, which is the Ojio–Yamada calibration written for a deflection record [23]. Two ratios explain the residuals. The measured reference integral divided by its exact analytical value is 1.0049, and the ratio of the BPM and SLM estimates equals it for both configurations: SLM absorbs the calibration error of the reference record, BPM does not. The measured-to-analytical integral ratio, both evaluated with the trapezoidal rule, grows with the load group: 1.010, 1.016 and 1.017 for one, two and three loads. The SLM residuals of 0.61 % and 0.70 % are exactly this step, which the data cannot attribute to support seating or to errors in the stated masses. Because the configurations differ in both total load and spacing, the invariance of Eq. (2) is supported only indirectly, and the predicted blind configuration (spans of 2500 mm and 3644 mm) was not tested.

---

## 4. Assessment on public moving-truck records

This section asks what integral estimators deliver on real moving-load records from a continuous girder. It reports every channel with 95 % confidence intervals (CIs), tests equivalence instead of stating agreement, and compares single- and multi-channel estimators out of sample.

### 4.1. Data and reference weights

The Nothing-on-Road BWIM dataset [48] (CC0 licence) contains strain records of the Virginia Smart Road Bridge, documented in [41–43,49]. The bridge is a post-tensioned concrete box girder continuous over five spans of 86.5 + 3 × 144 + 86.5 m = 605 m, with a depth of about 3.8 m at mid-span and 9.5 m at the piers. Strain transducers on the soffit of the top slab lie near mid-span of span 2, 158.5 m from the first abutment, in longitudinal stations about 2 m apart under the wheel path. Day 1 has 12 channels at 100 Hz: four stations, each with one gauge that shows axle spikes (the wheel-path gauges ch4, ch5, ch11, ch12), a partner gauge, and four gauges without axle spikes (ch1, ch2, ch8, ch9). Day 2 has four in-line channels at 200 Hz.

The reference weights differ in quality between the days. On day 1 two 3-axle trucks ran in the instrumented lane; their gross weights were reported by the drivers for each pass (21.2–22.8 t for the runs used) [49]. On day 2 a 3-axle truck of 26.8 t and a 5-axle truck of 25.9 t were weighed on a static scale [49] and ran in the instrumented lane (lane A), on the return trip in the other lane (lane B), and in two in-line two-truck runs. Because the weights vary by only a few per cent within each day, a constant predictor equal to the mean calibration weight has a mean absolute error (MAE) of 2.0 % on day 2 and 2.2 % on day 1. The field data therefore test the scatter and invariance of the integral constant, not the ability to discriminate weights.

Speeds were obtained from the axle spikes and the measured wheelbase; they agree with the speeds computed by the dataset authors' processing script within 1–2 %. For each crossing a linear baseline was fitted to quiet segments before and after the event, the strain was integrated over the whole time the truck was on the bridge plus 5 s at each end, and the result was converted to $\int\varepsilon\,\mathrm{d}x$ with the speed measured at the gauges. Three day-1 runs with two trucks on the bridge and four passes without documented weights were excluded; the same runs are used throughout. The noise of the integral was measured from vehicle-free windows of crossing length, at least 70 s from any detected vehicle. Fig. 5 shows three crossings.

### 4.2. Invariance of the constant and speed

Table 3 gives the constant of representative channels; all 23 channel and average rows are in the Supplementary Material. On day 1, eight gauges have a constant whose scatter is consistent with the measured noise (coefficient of variation, CV, 5.8–13.5 %; χ² p = 0.13–0.71). The two trucks agree within ±10 % only for ch11 (ratio 0.996, 90 % CI 0.904–1.098). For the four-gauge wheel-path average the ratio is 0.955 (95 % CI 0.863–1.057), and equivalence can be shown only within ±11.8 %. The four gauges without axle spikes fail: their constant is 22–26 % lower for the second truck, and the 95 % CIs exclude 1 (Fig. 6a). Their crossing residuals exceed the quiet-window noise variance by factors of 2.9–5.1.

**Table 3.** Integral constant $C$ (µε m/t) and invariance, lane A unless stated. Ratio: T2/T1 on day 1 (both 3-axle), 5-axle/3-axle on day 2. CV expected from the measured noise in brackets. Equivalence by two one-sided tests at the 5 % level.

| Day, channel | n | $C$ (95 % CI) | CV % (noise) | χ² p | Ratio (95 % CI) | Equivalence |
|---|---|---|---|---|---|---|
| 1, ch11 (best) | 7 | −5.85 (−6.17, −5.53) | 5.8 (6.8) | 0.60 | 0.996 (0.874–1.136) | within ±10 % |
| 1, wheel-path average | 7 | −4.03 (−4.24, −3.82) | 5.6 (6.1) | 0.53 | 0.955 (0.863–1.057) | within ±11.8 % only |
| 1, ch1, ch2, ch8, ch9 | 7 | −1.49 to −2.38 | 17.2–19.1 (7.8–11.0) | ≤ 0.012 | 0.740–0.783 (CIs exclude 1) | fails |
| 2, st36 | 8 | −5.97 (−6.57, −5.38) | 12.0 (16.5) | 0.73 | 1.005 (0.735–1.375) | not shown |
| 2, average of 4 | 8 | −4.12 (−4.62, −3.63) | 14.4 (20.2) | 0.79 | 0.978 (0.697–1.374) | within ±26.7 % only |
| 2, lane B, average | 8 | −3.27 (−4.19, −2.35) | 33.7 (23.2) | 0.027 | 0.749 (0.440–1.276) | fails χ² |

On day 2 the 5-axle/3-axle ratio of the gauge average is 0.98 (95 % CI 0.70–1.37). This is consistent with independence of the axle configuration, which Eq. (2) guarantees for a linear structure, but differences up to about 27 % cannot be excluded with eight runs. The test thus checks linearity and processing at a coarse level, not the identity itself. The day-2 lane-B constants fail the χ² test (p = 0.016–0.027), with CVs of 31–40 %.

Speed and truck are almost perfectly confounded on day 1: the first truck ran at 10.4–12.8 m/s and the second at 19.1–19.8 m/s (correlation 0.98). The 22–26 % difference of the gauges without axle spikes may therefore reflect a different transverse wheel path, local deck action or speed; the data cannot separate them. On day 2, where speed and truck are not confounded (13–28 m/s), the slope of the gauge-average constant is +6 % per 10 m/s with a 95 % CI of −23 to +35 %. No speed effect was resolved, but the constant cannot be called speed-independent (Supplementary Fig. S2).

### 4.3. Single- and multi-channel estimators out of sample

To test Section 2.4 on real records, the covariance of the integrated noise was measured from vehicle-free windows (1227 windows on day 2, 3405 on day 1). On day 2 the four channels are strongly common-mode, with a mean correlation of 0.92 (95 % CI 0.83–0.96), but with unequal amplitudes (13.7–32.8 µε m at the median speed). On day 1 the mean correlation is 0.42 (95 % CI 0.26–0.54) (Supplementary Fig. S1). Single-gauge, gauge-average, GLS (Eq. 13) and offset-immune (Eq. 14) estimators were compared by leave-one-run-out cross-validation: the constants were calibrated without the test run, and $\Sigma$ never contained a crossing. Table 4 and Fig. 7 give the results.

**Table 4.** Mean absolute error of the gross weight (% of GVW), out of sample, with 95 % bootstrap CIs over the test runs (n = 8 on day 2, n = 7 on day 1). LOTO: calibrated on one truck, tested on the other. Predicted sd: per-crossing standard deviation predicted by the vehicle-free covariance.

| Estimator | Day 2, leave-one-out | Day 2, LOTO | Day 2, predicted sd | Day 1, 12 gauges | Day 1, 4 wheel-path gauges |
|---|---|---|---|---|---|
| Best single gauge (chosen after the fact) | 8.4 (2.9–15.3) | 7.6 | 16.2 | 4.8 (1.8–7.9) | 4.8 (1.8–7.9) |
| Worst single gauge | 27.9 (12.9–44.5) | 24.3 | 32.5 | 17.6 (11.0–23.4) | 12.1 |
| Gauge average | 11.9 (6.0–18.6) | 11.1 | 19.8 | 5.3 (2.5–7.8) | 5.4 (3.3–7.4) |
| GLS, diagonal $\Sigma$ | 11.4 (6.0–18.0) | 10.8 | 19.4 | 5.3 (2.5–8.0) | 5.2 (3.3–7.1) |
| GLS, measured $\Sigma$ | 20.4 (12.3–28.8) | 17.7 | 12.7 | 5.8 (3.5–8.1) | 4.9 (3.0–6.9) |
| Offset-immune, measured $\Sigma$ | 20.3 (12.4–28.6) | 18.0 | 13.3 | 6.0 (2.9–9.3) | 8.3 (3.9–13.4) |
| Offset-immune, $\Sigma = I$ | 12.3 (6.1–20.2) | 10.8 | 16.1 | 13.0 (7.1–19.0) | 8.4 (4.6–12.9) |
| Mean weight of the calibration runs | 2.0 (1.9–2.0) | 3.4 | – | 2.2 (1.1–3.5) | 2.2 (1.1–3.5) |

On day 2 the gauge average gave an MAE of 11.9 % (95 % CI 6.0–18.6 %). GLS with the measured covariance gave 20.4 % and the offset-immune combination 20.3 %. The paired difference between GLS and the average is +8.5 points (95 % CI +2.3 to +15.1), so both estimators are significantly worse than the average, although the noise model predicted a per-crossing standard deviation of 12.7 % for GLS against 19.8 % for the average. On day 1 the estimators cannot be told apart (average 5.3 %, GLS 5.8 %, best single gauge 4.8 %). On both days every estimator is worse than the constant predictor.

The failure on day 2 is itself a finding. The crossing residuals are much less correlated between gauges (mean 0.63, and only 0.30–0.37 between st40 and its neighbours) than the vehicle-free noise (0.90 for the same window length). Evaluated with the covariance of the crossing residuals themselves, GLS predicts 21.0 % and the average 14.6 %, which reverses the order. The common-mode wander measured in quiet periods is real, but each crossing also carries a gauge-specific component, plausibly the wheel path and local slab action, and the large opposite-sign GLS weights (+0.16 on st40, −0.35 on st36) amplify it. Estimating $\Sigma$ from the crossings instead over-fits with eight runs: 10.4 % in sample against 28.4 % out of sample. This is the design caution of Section 2.4: offset immunity pays only for disturbances that are common-mode during crossings.

### 4.4. Lane, superposition and the limits of a beam model

Return trips in the other lane gave constants 0.79 times those of lane A for the gauge average (95 % CI 0.59–1.00). The lane effect is clearly resolved for one gauge only (st36: 0.64, 95 % CI 0.47–0.81). Each lane therefore needs its own constant, as found on another continuous girder [40]. The two in-line two-truck runs gave 0.92 and 0.92 of the summed single-truck predictions for the gauge average (pooled 0.92, 95 % CI 0.77–1.06). That is consistent with superposition, but low in both events; the GLS combination gave 0.82 (95 % CI 0.73–0.91).

Gauges within 6 m of each other along the girder have very different constants. On day 1 the constants range from −1.49 µε m/t (ch8) to −5.85 µε m/t (ch11), a factor of 3.9, and the 95 % CIs of these two constants do not overlap (Table 3). A one-dimensional beam model predicts ratios of 0.978–1.003 between them. The difference is unlikely to be gauge-factor spread, because the ratio of st36 to st40 changes with the lane, 3.24 ± 0.56 in lane A against 1.82 ± 0.10 in lane B (± one standard error; about 2.5 standard errors apart). The deck-soffit gauges respond to slab bending and shear lag as well as to girder bending, so the constant must come from a weighed reference vehicle or a three-dimensional model; a beam-model BPM would fail.

A beam model of the girder (Euler–Bernoulli, parabolic haunch, $I\propto h^2$) reproduces the global shape of the strain history ($r^2$ = 0.79–0.94). It places the zero-moment points of the uniform-load moment diagram in span 2 at 121.6 m and 190.8 m, about 35 m from the gauges, so the gauges are not blind; their strain constant is 0.69 of the largest on the girder (0.56–0.93 across the stiffness laws tested). The net-to-positive ratio of the gauge influence line is 0.51. Span 2 contributes about 170 % of the net integral and the adjacent spans −26 % and −66 %, so the whole 605 m crossing must be integrated.

### 4.5. What the field records show

The records support linearity, superposition and per-gauge invariance at the 10–27 % level that the noise allows, and they show that each lane, and each deck gauge, needs its own constant. They cannot show weight discrimination, because the reference weights hardly vary, and they show no benefit from GLS or offset-immune combinations. The common-mode assumption behind Eq. (14) holds for vehicle-free noise but not for crossing errors. The tests rest on four trucks, two axle counts and seven or eight runs per day; the gauge calibration factors and exact positions are not published, so absolute constants cannot be checked, and the GVW accuracy that the dataset authors reported for their influence-line system on this bridge [41–43] was not compared [NEED VALUE: GVW accuracy reported in [41–43] for the same runs, if the authors wish to add it].

---

## 5. In-service box girder: identifiability and channel design

This section applies the criteria to an in-service three-span box girder with static acceptance-test data. It asks how far the observability of each installed gauge is determined by the data, which channel and position would be robust, and which measurement would decide between the admissible models.

### 5.1. Bridge, data and model

The Cầu Mây Bridge carries provincial road DT389 over the Kinh Mon River in Hai Duong, Viet Nam. Its main bridge is a three-span continuous prestressed concrete box girder of 55 + 90 + 55 m built by balanced cantilever ($\beta = 1.636$). The depth varies from 2.40 m at mid-span to 5.40 m at the piers, with design second moments of 5.482 m⁴ and 59.61 m⁴ and $E_c = 36\,057$ MPa. The inner piers are monolithic with the girder; the end piers carry pot bearings. In the June 2020 acceptance test, four trucks stood in side span N8 and six in centre span N7. The trucks were three-axle, nominally 5 + 10 + 10 t, with a weighed mean of 25.06 t. Dial gauges read the peak deflection under centric and eccentric transverse positions [NEED VALUE: instrument type and fixed reference datum of the dial gauges, temperature correction, load-hold time and zero-reading procedure]. Gauge N8 is at 0.4L of the side span and N7 at mid main span. The mean of six readings is 5.55 mm at N8 and 15.42 mm at N7.

The girder was modelled with Euler–Bernoulli elements, a parabolic depth variation over $L_v = 44$ m from each inner pier, $I\propto h^{2.943}$ fitted to the two design sections, and a rotational spring $k$ at each inner pier. Because the depth law and pier dimensions are not documented, $L_v$ = 40 and 45 m, exponents of 2.5 and 3.2, and a ±1.5 m rigid pier zone were tested as model-form variants. Calibration A is the design model ($\alpha = 1$, $k = 2.75\times10^7$ kN m/rad fitted to the designer's FE output); it misfits the measurements by +2.4 % at N8 and +12.3 % at N7. Calibration B is the joint least-squares fit ($\alpha = 0.716$, $k = 1.2\times10^8$ kN m/rad; misfits −2.8 % and +2.9 %).

### 5.2. What the static data identify

The ratio $r_{87}$ of the measured-to-model ratios at N8 and N7 never reaches 1 (Fig. 9a). It falls from 1.126 at $\kappa = 10^7$ kN m/rad to a minimum of 1.058 at $\kappa = 1.68\times10^8$ kN m/rad, which is calibration B, and returns to 1.091 for fixed piers. The model-form variants move the minimum between 1.039 and 1.092 but never to 1, so the 4–9 % residual is model-form error. Calibration B is therefore the nearest fit, not an exact one, and its $\alpha = 0.716$ would mean a 28 % loss of rigidity in a young prestressed girder.

The admissible set depends on the tolerance $\tau$ on the misfit of each gauge. The six readings of each gauge (three lines, centric and eccentric) spread by 1.9–2.0 % about their mean. This is a systematic transverse spread, not a repeatability: the readings are not replicates. Adding a model-form spread of 1.75 % per gauge gives $\tau = 5.3$ % at two standard deviations. At this tolerance every $\kappa \ge 1.8\times10^7$ kN m/rad is admissible, with $\alpha$ = 0.51–1.15: the static data alone bound $\kappa$ only from below. The conclusion depends on the tolerance. At $\tau = 3$ % the admissible set shrinks to $\kappa = 1.0$–$3.0\times10^8$ kN m/rad with $\alpha$ = 0.64–0.80, which excludes the design rigidity; at $\tau = 4$ % it is $\kappa = 4.2\times10^7$–$2.0\times10^9$ kN m/rad with $\alpha$ = 0.54–0.98.

Because $N_w$ depends on $EI_\mathrm{ref}$, Table 5 reports it in two normalisations. Over the static set at $\tau = 5.3$ %, the N8 index is 0.14–0.42 when normalised by the effective rigidity $\alpha EI_\mathrm{mid}$, and 0.12–0.82 with the design $EI_\mathrm{mid}$; the upper part of the latter range requires $\alpha \approx 0.5$. A prior $\alpha \in [0.9, 1.3]$ leaves 0.14–0.27 (effective) or 0.12–0.30 (design). The absolute constant, which needs no reference, spans $C_8 = 3.0\times10^{-5}$–$2.0\times10^{-4}$ m²/kN over the static set, a factor of 6.6, against $C_7 = 3.3$–$5.0\times10^{-4}$ m²/kN for N7.

The Möbius law of Eq. (15) explains the asymmetry. With $k_g = 4.36\times10^7$ kN m/rad, $C_\infty/C_0$ is 14.0 at N8 and 0.59 at N7, and the design stiffness sits at $\kappa/k_g = 0.63$, near the steepest part of the curve, where $B_m$ is 0.51 at N8 and 0.12 at N7. Calibrating the model to the N8 reading does not fix the N8 constant either: over the static set, the ratio of $C_m$ to the modelled N8 deflection varies by a factor of 6.5, against 1.5 for N7.

**Table 5.** Deflection indicators of the Cầu Mây gauges. $N_w$ from Eq. (10) with $EI_\mathrm{ref} = EI_\mathrm{mid}$ of the design section, $L$ the span containing the gauge; $R$ from Eq. (11) in brackets. Static set: $\tau$ = 5.3 %. Bound: pinned to fixed piers with design $EI$ and all $L_v$ variants. –: not computed.

| Gauge | Prismatic, pinned | A (design) | B ($\alpha$ = 0.716) | Static set, design $EI$ | Static set, $\alpha EI$ | Bound, pinned … fixed |
|---|---|---|---|---|---|---|
| N8, 0.4L (installed) | 0.287 (0.14) | 0.181 (0.18) | 0.476 (0.56) | 0.124–0.822 (0.13–1.00) | 0.144–0.422 | 0.023 … 0.446 |
| N8 at mid side span | 0.163 (0.08) | 0.105 (0.11) | 0.377 (0.49) | – | – | −0.066 … 0.375 |
| N7, mid main span (installed) | 0.755 (0.70) | 0.209 (0.59) | 0.234 (0.77) | 0.190–0.286 (0.56–1.00) | – | 0.263 … 0.145 |

Calibration B's N8 value of 0.476 lies outside the bound column because the bound uses design $EI$; normalised by $\alpha EI_\mathrm{mid}$ it is 0.341. The centre-span index is low (0.19–0.29) although $R$ is 0.56–1.00, so its smallness reflects restraint by the haunches, not cancellation. The measured vertical frequencies (3.43–3.64 Hz) would narrow the set further if they were the third vertical mode; that interpretation is conditional, and the analysis is given in the Supplementary Material.

### 5.3. Which channel, where

For this girder the deflection channel at mid main span is the robust choice. A side-span deflection gauge is ill-conditioned with respect to pier stiffness and should not take its constant from a design model unless that stiffness is identified. The strain channel behaves differently (Fig. 8). The haunches move every zero-moment point towards mid-span, and the side-span zero lies 26.0–33.3 m from the abutment over the range of pier fixity, so a strain gauge at mid side span would be blind under calibration A ($N_M = 0.048$) and change sign with pinned piers. The centre of the main span is near-blind for strain in every haunched model ($N_M$ = 0.163–0.212 at N7), again through restraint ($R_\varepsilon$ = 0.65–1). The best-conditioned strain locations by $N_M$ are 5–10 m from the piers, where $|N_M| \ge 0.39$ in all haunched models. The placement rule, however, ranks locations by $C_\varepsilon = cM_q/(EI\,q_0)$: with $c\propto h$, the gain $c/EI$ there is about one fifth of that at mid-span (Fig. 8c), so the choice depends on whether the noise is set by the strain resolution or by the offset. Bearing load cells at the end supports give $N_R = \xi_0$ = 0.47–0.61 and cannot be blind unless the side span loses its sagging zone.

For two deflection channels, Section 2.4 places the second sensor at the most negative constant, in the side span 4–10 m from the inner pier. The pair at 100 m and 152 m from the end support T5 is within 0.9 % of the calibration-specific optimum under both A and B, so placement is insensitive to the unresolved pier stiffness. The placement study used a record of 220 m (the 200 m unit plus a 20 m convoy allowance). With it, at $\sigma = 0.01$ mm and $\varepsilon_0 = 0.1$ mm, the standard deviation of the load falls from 24.8 % with N7 alone (22.5 % for the 200 m record of Table 7) to 10.6 % at $\rho = 0.9$ (calibration A). The value at $\rho = 1$ would be far smaller, but Section 4.3 shows that a common-mode fraction measured in quiet periods need not hold during crossings, so these gains are upper bounds.

If a model-based constant is wanted, the most informative additional measurement is a tiltmeter on the monolithic pier T7, which would read about 167 µrad under the side-span convoy. The Cramér–Rao bounds below are evaluated at calibration A ($\kappa = 2.75\times10^7$ kN m/rad, $\alpha^* = 1.07$), with 2.64 % per static reading and an assumed 3 % for the rotation. There, the two deflections give a standard deviation of $\ln C_8$ of 0.87; adding the tiltmeter reduces it to 0.18, and identified first and third frequencies to 0.24. At calibration B the two-reading Fisher matrix is singular, so the bound from the deflections alone is infinite; with the tiltmeter it is 0.04. A rotation reading at the end bearing T8 adds little, because its sensitivity duplicates that of N8.

A moving-load test with weighed trucks has been designed for this bridge; Table 6 gives the predicted values that would decide between the reference calibrations. These are predictions, not results. The ratio of integrals at the side-span and centre-span deflection gauges is independent of truck weight and absolute rigidity, and it differs by a factor of 2.3 between A and B.

**Table 6.** Predicted discriminating measurements at Cầu Mây for a 25 t three-axle truck (not measured).

| Measured quantity | Calibration A | Calibration B |
|---|---|---|
| Integral ratio, N8 at 0.4L / N7 at mid-span | 0.121 | 0.284 |
| Peak girder rotation over pier T7 (µrad) | −58 | −29 |
| Strain integral at the zero-moment point of A (171.3 m) / at mid N7 | 0.006 | 0.17 |

The in-service girder shows that a side-span deflection gauge on a layout near the prismatic blind locus is not identifiable from static acceptance data, that a centre-span gauge is, and that one tiltmeter or one integral ratio would close the gap.

---

## 6. Error budget

This section states the error terms of the integral estimator with their sensitivities and the values measured or assumed in this paper. The budget is indicative, not an evaluation according to the GUM: several entries are scenario ranges and the correlations between terms are not quantified.

To first order, the relative error of BPM is the sum of the relative errors of the rigidity, of four times the span length, of the gain, of the speed and of the offset term of Eq. (12). SLM removes the structural terms, because they belong to $C$. Every other term survives as the difference between the target and reference crossings. Speed enters twice: as an effect on the response and through its measurement, because the space integral is the time integral times the speed measured at the gauges, and a speed error passes one-to-one into the weight. Speed variation over a 605 m crossing was not measured. For a constant force crossing the laboratory beam, the quasi-static error is at most about 1 % for $T_\mathrm{cr}/T_1 \ge 8$ and exceeds 15 % below 2.5 [50]; this bound omits vehicle–bridge interaction and road roughness.

Table 7 evaluates Eq. (12) for the Cầu Mây gauges with $L_\mathrm{tot} = 200$ m and the mean weighed truck of 25.06 t, over the static admissible set. The lower offsets are of displacement-transducer class. Absolute deflection on a 90 m span over water would usually come from a non-contact technique, whose residual offset after re-zeroing has to be established on site, since environmental effects act over the same window [51,52]. The authors' deflection records from simply supported spans showed post-minus-pre level differences of up to 0.23 mm; linear re-zeroing removes such differences, so this value bounds the drift before re-zeroing, not $\varepsilon_0$.

**Table 7.** Bias of a single-channel estimate caused by a residual offset $\varepsilon_0$, Eq. (12), for a 25.06 t truck; $L_\mathrm{tot}$ = 200 m. Ranges over the static admissible set ($\tau$ = 5.3 %).

| Gauge | $C$ (m²/kN) | 0.02 mm | 0.05 mm | 0.1 mm | 0.2 mm | 0.5 mm |
|---|---|---|---|---|---|---|
| N7, mid main span | 3.3–5.0 × 10⁻⁴ | 3.3–5.0 % | 8–12 % | 16–25 % | 33–50 % | 82–124 % |
| N8, 0.4L | 3.0–20 × 10⁻⁵ | 8–54 % | 21–136 % | 41–271 % | 82–543 % | 206–1356 % |

At $\varepsilon_0 = 0.1$ mm a single centre-span gauge biases a 25 t truck by 16–25 %, and a single side-span gauge by 41–271 %. With present absolute-deflection technology, single-point integral weighing on a long-span girder is therefore marginal even at the best location. The offset-immune pair addresses this term only to the extent that the offset is common-mode during crossings (Section 4.3).

Transverse position and multiple presence add further terms. On the five-span girder the far-lane constant was 0.79 of the near-lane value, and at Cầu Mây the readings across one section spread by up to 2.05 mm in the eccentric N7 case, about 13 % of the mean reading. Several vehicles on the structure return their combined weight; on the five-span girder the two-truck events gave 0.92 of the prediction. A crossing of the 200 m Cầu Mây unit takes 12.4 s at 60 km/h, and every crossing that overlaps another vehicle in that window must be discarded or treated as a group; the fraction of usable isolated crossings was not quantified.

**Table 8.** Indicative sensitivity budget of the integral estimator. Values are those measured or assumed in this paper; they are not combined.

| Term | Sensitivity | Cancels in SLM? | Value in this paper |
|---|---|---|---|
| Flexural rigidity $EI$ | 1 | yes | BPM only; Cầu Mây N8 constant varies 6.6-fold over the static set |
| Span length | 4 | yes | BPM only |
| Gain | 1 | if not recalibrated between crossings | not evaluated |
| Reference weighing $P_0$ | 1 | no | laboratory: accuracy class [NEED VALUE]; field: day-1 weights driver-reported |
| Residual offset, drift $\varepsilon_0$ | $L_\mathrm{tot}/I$ | only if common-mode during crossings | Table 7; field per-crossing sd of the gauge average predicted 19.8 % (day 2), 5.3 % (day 1) |
| Speed effect | 1 | no | day 2: +6 % per 10 m/s (95 % CI −23 to +35 %), not resolved |
| Speed measurement | 1 | no | not evaluated beyond 1–2 % agreement with the dataset speeds |
| Dynamics | 1 | partly | ≤ 1 % for $T_\mathrm{cr}/T_1 \ge 8$ (constant force) |
| Transverse position | lane-dependent $C$ | no, unless lane-specific | field lane ratio 0.79; Cầu Mây spread 2.05 mm |
| Multiple presence | group weight | – | two-truck events 0.92 of prediction |
| Linearity, seating | 1 | no | laboratory step 1.010 → 1.017 |

In the laboratory the reference record and the load-dependent step limit SLM to 0.6–0.7 %. In the field the noise, the lane and the gauge position dominate, and the per-crossing errors of 5–12 % on these records exceed the spread of the reference weights. The method is therefore proposed for preliminary overload screening, with the decision threshold set apart from the legal limit and the design live loads [53,54]; setting that threshold needs field calibration with trucks of clearly different weights, which this study did not have.

---

## 7. Design workflow and limitations

The results combine into a procedure for designing load-monitoring channels on a continuous girder before installation.

1. **Constants.** For each candidate channel and position, compute $C$ from one static analysis under a uniform unit load on each lane, Eq. (2). Use Eqs. (4)–(9) for prismatic two- and three-span beams.
2. **Blindness.** Locate the blind loci of Table 1. Keep strain gauges out of the ring $|N_M|<0.2$ around every zero-moment point, including gauges set back from a pier. Keep deflection gauges out of the near-blind bands $|N_w|<0.2$, for example $1.385<\rho_L<1.525$ for a mid-span gauge on two spans and $1.621<\beta<1.775$ for a mid side-span gauge on three spans.
3. **Conditioning.** Report $N_M$ for strain, $N_w$ with its $EI_\mathrm{ref}$ for deflection (or the absolute constant), and $R$ for both. A small $N$ with $R$ near 1 is restraint, not cancellation.
4. **Boundary robustness.** Evaluate $C$ over the plausible range of pier stiffness; for a symmetric girder, Eq. (15) gives the whole curve from the pinned and fixed constants. Avoid locations with large $C_\infty/C_0$ or $B_m$, or plan the measurement that identifies $\kappa$: a tiltmeter on a monolithic pier, an identified first frequency, or an integral ratio between two gauges.
5. **Placement.** Place sensors at the extremes of $C(x)$ of each channel type: $w_q$ for deflection and $cM_q/EI$ for strain.
6. **Estimator.** Use SLM with weighed vehicles of clearly different weights, several reference crossings and lane-specific constants. Combine channels by GLS or zero-sum weights only after estimating $\Sigma$ from the residuals of calibration crossings and checking it out of sample against the plain average; quiet-window covariances alone can mislead. Use BPM only where the location is well conditioned and the structure is known; on box girders with deck-mounted gauges, a beam model does not give the constant.
7. **Offset and dynamics.** Evaluate $P_\varepsilon$, Eq. (12), for the residual offset that the instrumentation achieves after re-zeroing, and compare it with the lightest vehicle to be screened. Check $T_\mathrm{cr}/T_1 \ge 8$ with the measured fundamental frequency.
8. **Processing.** Integrate in space over the complete crossing, re-zero before and after each crossing, remove dynamics with a low-pass filter well below $f_1$ and never with a high-pass filter, and discard overlapping crossings.

The integral is a reduced alternative to influence-line BWIM, not a competitor. It returns the gross weight of a vehicle or group from one scalar constant per channel and one weighted sum. Its natural role is low-cost screening across many continuous structures, with instrumented BWIM or enforcement weighing for the vehicles it flags. Influence-line BWIM does not suffer the blindness of Table 1, because it fits the whole record shape.

Several limitations remain. The laboratory beam had equal spans and statically positioned loads, and the blind configuration was not tested. The field assessment rests on one public dataset with four trucks, two axle counts, nearly constant reference weights and no gauge at a zero-moment point; it could not test weight discrimination, the deflection blind loci or a deflection pair. The in-service application uses static data, a two-dimensional model with an assumed depth law and equal pier springs. The treatment is one-dimensional along each lane.

---

## 8. Conclusions

This paper derived design criteria for channels that monitor the total load on continuous girder bridges, building on the classical influence-area identity and on standard GLS estimation.

1. Strain channels are blind at every zero of the uniform-load moment diagram, which every continuous girder has, and a near-blind ring surrounds each zero: on two equal spans it lies 0.19–0.32 of the span from the interior support. Deflection channels are blind only near particular span ratios, such as $(3+\sqrt{33})/6$ for two spans and 1.7006 for a mid side-span gauge on three symmetric spans.
2. The strain indicator $N_M$ needs no reference stiffness, and the cancellation ratio $R$ separates cancellation from restraint on haunched girders. The deflection indicator equals 2.5, not 1, at mid-span of a simply supported span, so its threshold must be stated with its normalisation.
3. Optimal sensors lie at the extremes of the uniform-load response, for strain at the extremes of $cM_q/EI$. Zero-sum weights remove a common-mode offset exactly, but on public field records GLS weights built from vehicle-free noise were worse out of sample than the plain gauge average (20.4 % against 11.9 % mean absolute error), because crossing errors were much less correlated between gauges than quiet noise (0.63 against 0.92).
4. On those records, constants were consistent with axle-configuration invariance (5-axle/3-axle ratio 0.98, 95 % CI 0.70–1.37) and with superposition, but the tests were inconclusive at better than 10–27 %, speed was confounded with truck on one day, each lane and each deck gauge needed its own constant, and the reference weights varied too little for any estimator to beat the mean weight.
5. On a 55 + 90 + 55 m box girder, two static readings bound the pier-to-girder stiffness ratio only from below at a 5.3 % tolerance, leaving the side-span deflection index between 0.14 and 0.42; at a 3 % tolerance the design rigidity would be excluded. A pier tiltmeter would identify the constant, and a residual offset of 0.1 mm would bias a 25 t truck by 16–25 % at mid main span.

The next steps are the moving-load test designed for the in-service girder, laboratory tests of the blind configuration, and field calibration with trucks of clearly different weights.

---

## Appendix A. Closed forms for two- and three-span beams

For unequal spans the uniform-load support moment of a two-span beam is $M_B = -q_0(L_1^3/EI_1+L_2^3/EI_2)/[8(L_1/EI_1+L_2/EI_2)]$. Superposing the simply supported uniform-load deflection of span 1 and the deflection due to $M_B$, evaluating at $x_m$ and dividing by $q_0$ gives Eq. (5) with $\mu = -8M_B/(q_0L_1^2)$, which is $\mu_\mathrm{2span}$ of Eq. (4). Setting $F = 0$ factors as $(1-\xi)(1+\xi-\xi^2)$ and gives Eq. (6). With uniform stiffness, the blind condition for a mid-span sensor is $3\rho_L^2-3\rho_L-2=0$, and maximising $F$ over $\xi$ at $\mu = 1$ gives $8\xi^2-\xi-1=0$, hence Eq. (7). In units of $L_1^4/(192EI_1)$, the positive contribution of the instrumented span varies only between 1.50 and 2.00 for $\rho_L$ from 0.5 to 2.0, whereas the negative contribution of the adjacent span sweeps from −0.125 to −4.00; the degeneracy is driven almost entirely by the adjacent span.

For the symmetric three-span beam the three-moment equation gives $M_B = M_C = -q_0L_s^2\mu/8$ with $\mu_\mathrm{3span}$ of Eq. (4). Three equal spans give $\mu = 4/5$. The optimal side-span position solves $8\xi^3-(12-3\mu)\xi^2+(2-\mu)=0$. The near-blind band at mid side span runs from the root of $30\beta^3-69\beta-16=0$ (1.621) to that of $10\beta^3-27\beta-8=0$ (1.775). A mid main-span deflection sensor is blind at $\beta = 0.9647$. For a sensor at $\eta = x/L_m$ in the main span, $192EI_mC_m/L_m^4 = 8[\eta(1-2\eta^2+\eta^3)-\nu\eta(1-\eta)]$ with $\nu = 3(\rho_{EI}+\beta^3)/[\beta^2(2\rho_{EI}+3\beta)]$. Asymmetric layouts follow from the three-moment equations (Supplementary Material).

**Table A.1.** Symmetric three-span beam, uniform rigidity: optimal side-span position $\xi^*$ and deflection indicator $N_w$ (Eq. 10; 2.5 for a simply supported mid-span).

| $\beta$ | $\mu$ | $\xi^*$ | $N_w$ at $\xi^*$ | $N_w$ at $\xi = 1/2$ |
|---|---|---|---|---|
| 1.0 | 0.800 | 0.4460 | 1.322 | 1.300 |
| 1.2 | 0.9743 | 0.4251 | 1.076 | 1.039 |
| 1.4 | 1.208 | 0.3875 | 0.7585 | 0.6884 |
| 1.5 | 1.346 | 0.3582 | 0.5807 | 0.4808 |
| 1.636 | 1.558 | 0.2994 | 0.3316 | 0.1632 |
| 1.7 | 1.666 | 0.2608 | 0.2202 | 0.0015 |

## Appendix B. General channels and invariant weights

For a prismatic span with hogging end parameters $m_l$, $m_r$ and $\xi = s/L$, the indicators are $N_w = 8\Phi$ with $\Phi = \xi(1-2\xi^2+\xi^3)-\tfrac{m_l}{2}(2\xi-3\xi^2+\xi^3)-\tfrac{m_r}{2}(\xi-\xi^3)$, $N_\theta = 24EI\,C_\theta/L^3 = \Phi'(\xi)$, $N_M$ of Eq. (9) and $N_V = 2C_V/L = 1-2\xi+(m_l-m_r)/4$. $N_\theta$, $N_M$ and $N_V$ equal 1 for the simply supported reference (end rotation, mid-span moment, end shear); $N_w$ equals 2.5 at a simply supported mid-span. For the two-span beam, $(m_l, m_r) = (0, \mu)$ in span 1 and $(\mu/\rho_L^2, 0)$ in span 2; for the symmetric three-span beam, $(0, \mu)$ in the side span and $(\mu/\beta^2, \mu/\beta^2)$ in the main span. Strain zeros solve $4\xi^2-(4+m_l-m_r)\xi+m_l=0$. The verification covered two-span, symmetric and asymmetric three-span and four-span beams, zero-moment positions, ten blind configurations, the identity for a two-truck convoy on piecewise-prismatic girders with elastic pier springs (relative error 2.8 × 10⁻⁹), and the haunched Cầu Mây FE against an independent force-method solution (5.4 × 10⁻¹⁰). Truncating the record when the first axle leaves changed the integral by up to 59 % (rotation) and 10 % (moment) on the two-span example.

For the most general linear estimator $\hat P = \sum_j\int g_j(x)z_j(x)\,\mathrm{d}x$, the mean is $\sum_aP_ah(s_a)$ with $h(s) = \sum_j\int g_j(x)\eta_j(x-s)\,\mathrm{d}x$. If $h$ must be constant in $s$ for every set of influence lines supported on $[0, L]$, then $\int_0^L[g(u+s)-g(u+s')]\eta(u)\,\mathrm{d}u = 0$ for every admissible $\eta$, so $g(u+s) = g(u+s')$ almost everywhere. Each $g_j$ is therefore constant, and the only freedom lies across channels. When the influence line is known, other invariant weights exist; for two equal spans their white-noise variance is 1.5–6.6 times smaller, but a 20 % stiffness error in the adjacent span then produces configuration-dependent errors of −1.1 % to +2.0 % (Supplementary Material).

## Appendix C. Identifiability: sensitivities and Möbius law

Let $G = K^{-1}$ with $K = \alpha K_g + kK_p$, where $K_p$ has a unit entry on each inner-pier rotational degree of freedom, and $C_m = e_m^\top Gq$ with $q$ the consistent uniform load. Then $\mathrm{d}C_m/\mathrm{d}k = -\sum_i\theta_{m,i}\theta_{q,i}$, where $\theta_{m,i}$ and $\theta_{q,i}$ are the pier rotations under a unit load at the gauge and under the uniform load, and $S_\alpha + S_k = -1$ by Euler's theorem, because $C_m$ is homogeneous of degree −1 in $(\alpha, k)$. Mirror symmetry decouples the symmetric and antisymmetric pier-rotation patterns, the uniform load excites only the antisymmetric one, and the Sherman–Morrison formula gives Eq. (15) with $1/k_g$ the antisymmetric pier flexibility of the girder at $k = 0$. For the Cầu Mây model the law holds to a relative error of 5 × 10⁻⁶ over $k = 10^5$–$10^{12}$ kN m/rad. With two static readings the Fisher matrix has a determinant proportional to $(S_{y8}-S_{y7})^2$, which vanishes at the minimum of the ratio misfit, that is at calibration B. A frequency adds a row with the mass as nuisance parameter; a pier rotation adds a row without nuisance. Unequal pier stiffnesses would bring in the symmetric pattern, which Eq. (15) does not cover.

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

The supplementary material contains: (i) the analysis scripts and the console output of each run, with a README that maps every table and figure to a script and log; (ii) the derived data behind every figure and table; (iii) the laboratory specimen, influence line, quadrature study and full data (former Appendix D); (iv) the full per-channel invariance table of the field records (23 channel and average rows), the noise correlation matrices, the speed regressions and all estimator results, including in-sample and leave-one-truck-out values (Figs. S1–S2); (v) the beam model of the five-span girder and the synthetic records of the dataset authors (Figs. S3–S4); (vi) strain blind-locus maps (Figs. S5–S6); (vii) the multi-channel placement study, Monte Carlo verification and structure-aware weights (Figs. S7–S9); (viii) the asymmetric three-span closed forms; (ix) the Cầu Mây frequency interpretation, admissible sets against tolerance and the closed-form Möbius law (Figs. S10–S12); (x) the moving-force analysis behind the dynamic bound; (xi) the deflection records of two simply supported bridges, which illustrate baseline handling and low-pass filtering (Figs. S13–S14).

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

## Figures

::: {custom-style="Figure placeholder"}
[Figure 1 to be inserted: source file supplied by the authors]
:::

**Fig. 1.** Continuous beams considered: (a) two-span beam with instrumented span $L_1$, adjacent span $L_2 = \rho_LL_1$ and sensor at $\xi L_1$; (b) symmetric three-span beam with side spans $L_s$, main span $L_m = \beta L_s$ and side-span sensor at $\xi L_s$.

![](/home/user/SHM-Paper1-1D/manuscript/v4/figures/Fig2_obs_map_3span.png){width=16cm}

**Fig. 2.** Deflection observability of a three-span beam with uniform rigidity: (a) symmetric beam, $N_w$ over $\beta$ and the side-span sensor position $\xi$, with the blind locus (thick line), the near-blind band $|N_w|<0.2$ (hatched), the optimum $\xi^*(\beta)$ (dashed) and the Cầu Mây layout with a mid side-span sensor (open circle); (b) asymmetric beam, sensor at mid span 1, over $L_1/L_2$ and $L_3/L_2$. Colours are clipped at ±1.5.

![](/home/user/SHM-Paper1-1D/manuscript/v4/figures/Fig3_channels_prismatic.png){width=16cm}

**Fig. 3.** Indicators of four channels along prismatic girders: deflection $N_w$ (Eq. 10; 2.5 at a simply supported mid-span), rotation $N_\theta$, strain or moment $N_M$ and shear $N_V$ (each 1 for the simply supported reference of its own span). (a) Equal two-span beam; (b) symmetric three-span beam with $\beta = 1.636$, the Cầu Mây span ratio. The grey band marks $|N|<0.2$.

![](/home/user/SHM-Paper1-1D/manuscript/v4/figures/Fig4_multichannel_gain.png){width=16cm}

**Fig. 4.** Multi-channel estimation under the assumed noise model: (a) variance with two or three optimally placed sensors relative to the best single sensor, against the common-mode fraction $\rho$ of the offset; (b) standard deviation of the load against the offset level for single sensors and three-sensor designs; (c) offset-immune pair at $\rho = 1$ against the white-noise level. 2S-eq: equal two-span beam; 3S-b2.0: three-span beam with $\beta = 2$; CM-A, CM-B: Cầu Mây calibrations A and B.

![](/home/user/SHM-Paper1-1D/manuscript/v4/figures/Fig5_norbwim_crossings.png){width=16cm}

**Fig. 5.** NOR-BWIM strain records of three single-truck crossings of the five-span girder: a 5-axle and a 3-axle truck on day 2 and a 3-axle truck on day 1. Shaded: integration window; dashed: beam-model shape scaled to the reference gauge. The legend gives each gauge's integral $\int\varepsilon\,\mathrm{d}x$ (µε m).

![](/home/user/SHM-Paper1-1D/manuscript/v4/figures/Fig6_norbwim_invariance.png){width=16cm}

**Fig. 6.** Ratio of the integral constants of two trucks, per gauge, with 95 % confidence intervals: (a) day 1, second to first 3-axle truck, 12 gauges and the wheel-path average; (b) day 2, 5-axle to 3-axle truck, 4 gauges and their average. Grey bands: ±5 % and ±10 %. Red: invariance rejected; blue: equivalent within ±10 %; orange: inconclusive.

![](/home/user/SHM-Paper1-1D/manuscript/v4/figures/Fig7_norbwim_estimators.png){width=16cm}

**Fig. 7.** Mean absolute error of the gross weight for single-gauge, gauge-average, GLS, offset-immune and constant (mean-GVW) predictors, with 95 % bootstrap confidence intervals: in sample (IN), leave-one-run-out (LOO) and leave-one-truck-out (LOTO). (a) Day 2, 4 gauges; (b) day 1, 4 wheel-path gauges; (c) day 1, 12 gauges. GLS-diag: diagonal covariance; immune-eq: zero-sum weights with equal noise; GLS-resid: covariance from crossing residuals.

![](/home/user/SHM-Paper1-1D/manuscript/v4/figures/Fig8_caumay_channels.png){width=16cm}

**Fig. 8.** Cầu Mây girder, indicators along the girder for a prismatic model with pinned piers and for the haunched model under calibrations A and B: (a) deflection $N_w$; (b) strain $N_M$, with strain blind points; (c) strain indicator including the section gain $c/EI$, assuming $c\propto h$. Dotted lines: gauge positions N7, N8 at mid side span and N8 at 0.4L.

![](/home/user/SHM-Paper1-1D/manuscript/v4/figures/Fig9_caumay_identifiability.png){width=16cm}

**Fig. 9.** Identifiability of the Cầu Mây pier stiffness from two static readings: (a) ratio $r_{87}$ of the measured-to-model ratios at N8 and N7 against $\kappa = k/\alpha$, with model-form variants (grey) and the admissible band $|\ln r_{87}|\le 2\tau$, $\tau$ = 5.3 %; (b) N8 and N7 indicators and cancellation ratios along the static valley $\alpha^*(\kappa)$; shaded: static admissible range of $\kappa$.
