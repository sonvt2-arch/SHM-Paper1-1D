::: {custom-style="Title"}
Blind spots and sensor placement for influence-area weigh-in-motion on continuous girders
:::

::: {custom-style="Title block"}
Quoc-Bao Nguyen^a^, Thai-Son Vu^a,\*^

^a^ Faculty of Bridge and Road Engineering, Hanoi University of Civil Engineering, 55 Giai Phong, Bach Mai ward, 11618 Ha Noi, Viet Nam

\* Corresponding author: Thai-Son Vu. E-mail: sonvt2@huce.edu.vn

E-mail addresses: baonq@huce.edu.vn (Q.-B. Nguyen) and sonvt2@huce.edu.vn (T.-S. Vu)
:::

## Abstract

Influence-area bridge weigh-in-motion divides the area under a response record by an integral constant. On continuous girders this constant can vanish, because influence lines change sign, and a gauge where it vanishes cannot weigh. The paper gives three main results. First, closed forms locate these blind points for five channel types: strain gauges measuring global bending are blind at every zero of the uniform-load moment and nearly blind at 0.19–0.32 of the span from the interior support on two equal spans, whereas deflection gauges are blind only for particular span ratios. Second, for position-independent noise, the best sensor locations are the extremes of the uniform-load response; on one day of public records, weighting gauges by vehicle-free noise covariance raised the error 8.5 percentage points above the gauge average. Third, for symmetric girders with equal piers the constant is linear-fractional in pier stiffness; on an in-service box girder, two static readings leave the side-span deflection constant of the base model uncertain by a factor of 6.6 against 1.5 at mid main span (2.4 against 1.1 with girder rigidity bounded to 0.9–1.3 times the design value). On this girder, a single deflection gauge belongs at mid main span.

**Keywords:** Structural health monitoring; Sensor placement; Observability; Continuous girder; Bridge weigh-in-motion; Identifiability



## 1. Introduction

Heavy vehicles above the design envelope shorten the life of highway bridges and, in extreme cases, contribute to collapse (Fan et al., 2015). Knowing the loads that a bridge actually carries is therefore part of risk-informed asset management (Ventura et al., 2024). Pavement weigh-in-motion (WIM) is mature (Jacob et al., 2002; Al-Qadi et al., 2016), but it weighs the vehicle rather than the load on a particular bridge. Bridge weigh-in-motion (BWIM), introduced by Moses (1979) and reviewed by Yu et al. (2016), fits the measured response to axle loads times influence-line ordinates and has been refined with measured influence lines (OBrien et al., 2006), regularization (OBrien et al., 2009), accuracy improvements (Žnidarič et al., 2018) and the transverse position of the vehicle (Yu et al., 2018). Strain time histories have given axle weights in model tests on simply supported and continuous beams (Hao et al., 2019), and the transverse load distribution coefficient has given vehicle weights on multi-T-girder bridges (Zuo et al., 2019). Moving-force identification recovers axle-load histories (Law et al., 1997; Chan et al., 1999; Law and Zhu, 2000), also on multi-span bridges (Zhu and Law, 2006). These methods aim at axle loads and need several sensors, a structural model or a regularized inversion.

A simpler family estimates only the gross weight from the area under the response. Ojio and Yamada (2002) integrated the strain records of plate-girder stringers and calibrated the result against a truck of known weight; this calibration is called the standard-load method (SLM). It has been used in long-term monitoring (Cardini and DeWolf, 2009) and was accurate to within 5 % on a seven-span slab-on-girder bridge for test trucks with well-estimated speeds (Helmi et al., 2014). Later work used strain areas and integrals (Yang et al., 2021; Zhu et al., 2022; Agüero-Barrantes et al., 2023), shear strain (Lobo Aguilar and Christenson, 2018), sparse sensing that chose gauge number and location on a single-span bridge (Agüero-Barrantes et al., 2021), load-cell reactions (Shi et al., 2025) and an influence-line-free probabilistic index (Yan et al., 2022). Nguyen et al. (2024) used the integral of mid-span deflection on a simply supported beam.

The identity behind these methods is classical: the area under an influence line equals the response to a uniform unit load, as design codes use for distributed lane loads (Ghali et al., 2017). On continuous girders, however, the influence line changes sign over each interior support, and positive and negative areas partly cancel. Continuous bridges have been weighed from distributed fiber-optic strain (Chaudhary et al., 2025), with lane-specific influence lines (Wu et al., 2020) and from deck strain on long-span box girders (Moghadam et al., 2022, 2023a, 2023b); Deng et al. (2025) replaced the small net area of a multi-span displacement influence line by its absolute area. Sensor placement for BWIM has been posed through an augmented Kalman filter (Zhou et al., 2025). Deflection-based load identification has been posed as a regularized stochastic problem (Zhang et al., 2026). Deflection influence lines have been identified from moving-vehicle records (Wang et al., 2026) and inverted for girder stiffness (Zhou et al., 2026) or for the presence and location of stiffness loss in a beam (Dang et al., 2023), and influence lines have been used to estimate the boundary spring stiffness of a suspension-bridge girder (Lin et al., 2023). Strain-history areas along continuous girders have served damage identification (Hong et al., 2016; Wu et al., 2018), and BWIM has been applied to a two-span continuous bridge (Yamaguchi et al., 2009). Single-channel SLM assumes that the integral constant is well away from zero and independent of the boundary conditions, yet none of these studies reads the zeros of the integral constant as blind loci for weighing, or shows how they shift with uncertain boundary conditions. Criteria that locate these zeros are needed to choose, before installation, the few channels that screen continuous bridges for overloads.

This paper supplies them. Neither the influence-area identity nor the generalized least-squares (GLS) estimator is new; the contribution is a set of design criteria built on them, not a new weighing algorithm. (i) Where a gauge is blind: a closed-form catalog gives the blind and near-blind loci of five channel types on prismatic two- and three-span girders. Its strain criterion, the zeros of the uniform-load moment, holds for any girder in beam theory and, unlike the absolute area of Deng et al. (2025), keeps the estimate linear in the axle loads (Supplementary Section S3). (ii) Where to place sensors: extreme-point optimal design (Elfving, 1952; Pukelsheim, 2006) gives a closed-form placement rule for the gross weight, with optimal sensors at the extremes of the uniform-load response for position-independent noise, whereas Zhou et al. (2025) optimized sensors numerically for axle-force histories. The rule itself is not tested in the field; on one day of public records, GLS weights from vehicle-free noise did worse than the gauge average (Section 4.3). (iii) How pier stiffness moves the constant: for a symmetric girder with equal piers, the constant follows a linear-fractional (Möbius) law, a consequence of the Sherman–Morrison formula (Sherman and Morrison, 1950); on an in-service box girder, two static readings leave a side-span deflection constant several times more uncertain than the main-span constant (Section 5.2). The laboratory test checks the identity, the public records check its assumptions and noise model (not weighing accuracy), and the in-service girder illustrates the limits of identifiability. The blind loci are verified analytically and by finite element (FE) evaluation, not experimentally, and the blind configuration of the laboratory beam (spans of 2500 mm and 3644 mm) was not tested.



**Principal symbols** (full list: Supplementary Table S1)

| Symbol | Meaning | Symbol | Meaning |
|:---|:---|:---|:---|
| $C$ | integral constant of a channel, Eq. (2) | $\gamma$ | rigidity ratio of adjacent spans |
| $N_w$ | deflection indicator, Eq. (8) | $\kappa$ | scaled pier stiffness $k/\alpha$ |
| $N_M$ | strain (moment) indicator, Eq. (7) | $\alpha$ | effective-to-design girder rigidity |
| $R$ | cancellation ratio, Eq. (9) | $k$ | rotational stiffness of a monolithic pier |
| $\mu$ | interior-moment parameter, Eq. (4) | $\tau$ | tolerance on the static misfit of a gauge |
| $\lambda$ | span ratio, two spans | $B_m$ | boundary sensitivity $\lvert\partial\ln C_m/\partial\ln\kappa\rvert$ |
| $\beta$ | main-to-side span ratio, three spans | $P_\delta$ | offset-equivalent load, Eq. (10) |

## 2. Theory

### 2.1. Influence-area identity

Consider a linear-elastic structure, unchanged during a crossing, with any distribution $EI(x)$ and any linear-elastic supports. A response channel at a fixed point $m$ is any fixed linear functional of the displacement field measured from the unloaded state (deflection, rotation, fiber strain $\varepsilon = cM/EI$, shear force or reaction), with an influence line $\eta_m(x)$ that is zero outside the loaded path $[0, L_p]$. For a convoy of axle loads $P_i$ at fixed offsets $d_i$ ($d_1 = 0$) crossing quasi-statically, the record is

$$y_m(x)=\sum_{i=1}^{n}P_i\,\eta_m(x-d_i). \tag{1}$$

Its integral over the complete crossing is

$$J_m=\int_0^{L_p+d_\mathrm{max}}y_m\,\mathrm{d}x=P_\mathrm{tot}\,C_m,\qquad C_m=\int_0^{L_p}\eta_m(u)\,\mathrm{d}u=\frac{y_m[q_0]}{q_0}, \tag{2}$$

where $d_\mathrm{max}$ is the largest axle offset, $P_\mathrm{tot}$ the total load and $y_m[q_0]$ the response to a uniform load $q_0$ over the whole path. This is the classical influence-area identity (Ojio and Yamada, 2002; Ghali et al., 2017); the second equality, $C_m = y_m[q_0]/q_0$, needs superposition only. $C_m$ is called the integral constant, or the constant, and a channel is blind where $C_m = 0$. A channel observes the total load where $C_m \neq 0$, a scalar notion narrower than state-space observability. For a strain gauge at distance $c_m$ from the neutral axis of a section of rigidity $EI_m$ at $x_m$,

$$C_\varepsilon=\frac{c_m\,M_q(x_m)}{EI_m\,q_0}. \tag{3}$$

The section enters only as a gain, so a strain channel is blind exactly at the zeros of the uniform-load moment diagram $M_q$, for any $EI(x)$ and any elastic supports. This is a beam-theory result for gauges that measure global bending, such as gauges on a girder flange or web; deck-soffit gauges also respond to local slab action (Section 4.2). The beam-property method (BPM) computes $C$ from a structural model and returns the estimate $\hat P = J/C$ of $P_\mathrm{tot}$; SLM takes the constant from a reference crossing of known weight $P_0$ and returns $P_t = P_0J_t/J_0$ (Ojio and Yamada, 2002).

Equation (2) assumes a linear, time-invariant structure, a quasi-static response, axles on the path on which $\eta_m$ is defined (so each lane has its own constant), a complete crossing and re-zeroing to the unloaded state; Sections 3 and 4 test these assumptions, and Section 6 discusses their limits. The complete crossing matters: truncating the record when the first axle leaves changes the rotation integral by up to 59 % on a two-span example (Supplementary Section S3).

### 2.2. Closed-form blind loci

A channel is blind where its constant $C$ vanishes and near-blind where its normalized indicator (Section 2.3) is below 0.2 in magnitude. For a prismatic span under a uniform load, every channel is determined by the two end moments, written as $\bar M = -8M/(q_0L^2)$, positive for hogging: $\bar M_l$ at the left end and $\bar M_r$ at the right end. In the instrumented span of a two-span beam and in the side span of a symmetric three-span beam, $(\bar M_l, \bar M_r) = (0, \mu)$, with the classical interior-moment parameter (Ghali et al., 2017)

$$\mu_\mathrm{2span}=\frac{1+\lambda^3/\gamma}{1+\lambda/\gamma},\qquad \mu_\mathrm{3span}=\frac{2(\gamma+\beta^3)}{2\gamma+3\beta}. \tag{4}$$

Here $\lambda = L_2/L_1$ and $\beta = L_\mathrm{main}/L_\mathrm{side}$ are the span ratios and $\gamma$ is $EI_2/EI_1$ or $EI_\mathrm{main}/EI_\mathrm{side}$ (Fig. 1). The deflection constant at $\xi = x_m/L$ is

::: {custom-style="Figure"}
![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/Fig1_beams.png){width=14cm}
:::

::: {custom-style="Caption justified"}
**Figure 1.** Continuous beams considered: (a) two-span beam with instrumented span $L_1$ of rigidity $EI_1$, adjacent span $L_2 = \lambda L_1$ of rigidity $EI_2 = \gamma EI_1$, and sensor at $\xi L_1$; (b) symmetric three-span beam with side spans $L_\mathrm{side}$ of rigidity $EI_\mathrm{side}$, main span $L_\mathrm{main} = \beta L_\mathrm{side}$ of rigidity $EI_\mathrm{main} = \gamma EI_\mathrm{side}$, and side-span sensor at $\xi L_\mathrm{side}$.
:::

$$\frac{192EI\,C_m}{L^4}=8F(\xi,\mu),\qquad F(\xi,\mu)=\xi(1-2\xi^2+\xi^3)-\frac{\mu}{2}\,\xi(1-\xi^2). \tag{5}$$

Its left-hand side is the deflection indicator $N_w$ of Eq. (8). Setting $F = 0$ gives the deflection blind condition, which depends on $\mu$ alone:

$$C_m=0\;\Leftrightarrow\;\mu=\mu_\mathrm{crit}(\xi)=\frac{2(1+\xi-\xi^2)}{1+\xi}. \tag{6}$$

In design terms, an end-span deflection gauge is blind only if the interior support moment lies between its value for two equal spans ($\mu = 1$) and twice that value, which needs a longer adjacent span ($\lambda > 1$, or $\beta^2 > 3/2$); on equal spans it cannot be blind. The main span of a symmetric three-span girder is the exception: with nearly equal spans it has deflection blind points, and with three equal spans $|N_w| \le 0.10$ along the whole main span. Table 1 lists the blind span ratios (Fig. 2); Supplementary Section S2 gives their closed forms, the optimal gauge position and the near-blind bands (Eqs. (S1) and (S2), Tables S2 and S3). All closed forms agree with FE evaluations of Eq. (2) in 981 checks (Supplementary Section S3).

::: {custom-style="Figure"}
![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/Fig2_obs_map_3span.png){width=14cm}
:::

::: {custom-style="Caption justified"}
**Figure 2.** Deflection observability of three-span beams of uniform rigidity: (a) symmetric beam, $N_w$ over $\beta$ and side-span sensor position $\xi$, with blind locus (thick line), near-blind band $|N_w|<0.2$ (hatched), optimum $\xi^*(\beta)$ of the positive indicator (dashed; the negative one near the pier is larger beyond $\beta = 1.639$) and Mây Bridge proportions (open circle: mid side span; filled circle: N8 at 0.4$L$); (b) asymmetric beam, sensor at mid-span of span 1, over $L_1/L_2$ and $L_3/L_2$.
:::

For strain, with $(\bar M_l, \bar M_r) = (0, \mu)$, the indicator and the blind point $\xi_0$ are

$$N_M=\frac{8M_q(x_m)}{q_0L^2}=4\xi(1-\xi)-\bar M_l(1-\xi)-\bar M_r\xi,\qquad \xi_0=1-\frac{\mu}{4}. \tag{7}$$

Strain blind points exist in every span that has a sagging zone ($\mu<4$), so every continuous girder has them. For two equal spans, $\xi_0 = 0.75$ and the near-blind band $|N_M|<0.2$ lies 0.19–0.32 of the span from the interior support: a gauge at the support section is well conditioned ($|N_M| = \mu$), but one set back from the pier to clear the diaphragm can fall into the band. Figure 3 shows the indicators along two prismatic girders. The end-reaction indicator $N_F = 2F_A/(q_0L_1)$, with $F_A$ the end reaction, equals $\xi_0$ for any $EI(x)$ and pier springs, because $M_q = F_Ax - q_0x^2/2$ in the end segment.

::: {custom-style="Figure"}
![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/Fig3_channels_prismatic.png){width=14cm}
:::

::: {custom-style="Caption justified"}
**Figure 3.** Indicators along prismatic girders: deflection $N_w$ (2.5 at a simply supported mid-span), rotation $N_\theta$, strain $N_M$ and shear $N_V$ (1 for the simply supported reference). (a) Equal two-span beam; (b) symmetric three-span beam, $\beta = 1.636$. Gray band: $|N|<0.2$. Each indicator is normalized by the span containing the sensor, so the steps of $N_w$, $N_\theta$ and $N_M$ at the piers are changes of scale; the step of $N_V$ is the support reaction.
:::

**Table 1.** Blind loci of response channels: positions or span ratios at which the constant $C$ of Eq. (2) vanishes. Prismatic beams with $\gamma = 1$ unless stated; $\mu$ from Eq. (4); $\zeta$: position in the main span from the pier, as a fraction of the main span.

| Channel | Blind where | Two-span beam (span 1) | Symmetric three-span beam |
|:---|:---|:---|:---|
| Strain, moment, curvature | zeros of $M_q$ | $\xi_0 = 1-\mu/4$ (0.75 at $\lambda = 1$); band $0.676<\xi<0.812$ at $\lambda = 1$ | side: $\xi_0 = 1-\mu/4$; main: $\zeta_0=(1-\sqrt{1-\mu/\beta^2})/2$ from the pier (0.276 at $\beta = 1$) |
| Deflection | zeros of the uniform-load deflection $w_q$ | $\mu = \mu_\mathrm{crit}(\xi)$, only for $1<\mu<2$; mid-span: $\lambda = 1.4574$, band $1.385<\lambda<1.525$ | mid side span: $\beta = 1.7006$, band $1.621<\beta<1.775$; locus over all side-span positions ends at $\beta = 1.8794$; main span: blind for $0.9647 \le \beta < 1.2247$ (equal spans: 0.276 from each pier) |
| Rotation | extrema of $w_q$ | end: $\mu = 2$ ($\lambda = 1.6180$); pier: $\lambda = 1$ for any $\gamma$ | end: $\beta = 2\cos(\pi/9)$; pier: $\beta = \sqrt{3/2}$ for any $\gamma$; mid main span: always |
| Shear | maxima of $M_q$ | $\xi = \xi_0/2$ | side: $\xi_0/2$; mid main span: always |
| End reaction | no sagging zone in the end span | $\mu = 4$ ($\lambda = 2.3028$) | $\mu = 4$ ($\beta = 2.6691$) |
| Interior reaction | never under a full uniform load | – | – |

### 2.3. Observability and conditioning indicators

Every estimator below divides by $C$, so to first order the sensitivity to measurement error scales as $1/|C|$. For a deflection channel the normalized indicator is

$$N_w=\frac{192EI_\mathrm{ref}\,C_m}{L^4}, \tag{8}$$

with $L$ the span containing the sensor and $EI_\mathrm{ref}$ a reference rigidity. $N_w$ equals 2.5 at mid-span of a simply supported span, where $N_M$ equals 1. The rotation and shear indicators (Supplementary Section S3) equal 1 for the simply supported end rotation and end shear. A common threshold of 0.2 is 8 % of the simply supported value for deflection and 20 % for strain; this threshold is a design convention. Because the offset-equivalent load of Eq. (10) scales as $1/C$, an indicator of 0.2 multiplies it by 12.5 relative to a simply supported mid-span deflection gauge and by 5 relative to a strain gauge there. Supplementary Table S3 gives the near-blind bands for thresholds of 0.1, 0.2 and 0.3. On a non-prismatic girder $N_w$ also depends on the choice of $EI_\mathrm{ref}$, which, as Section 5 shows, can dominate the result, whereas $N_M$, the uniform-load moment relative to $q_0L^2/8$, needs no reference rigidity. Neither does the cancellation ratio

$$R=\frac{C}{A^+}=1-\frac{|A^-|}{A^+}, \tag{9}$$

the net influence area divided by its positive part $A^+$ (cf. the comparison of net and absolute areas by Deng et al., 2025). $R$ is defined for $C > 0$ (for $C < 0$, $A^+$ and $A^-$ change roles); it equals 1 for a simply supported span and 0 at a blind configuration, so a small indicator with $R$ near 1 indicates restraint rather than cancellation. At mid-span of two equal spans, strain influence lines cancel less than deflection influence lines ($R_\varepsilon = 0.667$ against $R_w = 0.571$), but near a zero of $M_q$ the order reverses.

A residual offset $\delta_0$, in the units of the channel, left after re-zeroing before and after the crossing, adds $\delta_0L_\mathrm{tot}$ to the integral over a record of length $L_\mathrm{tot}$. With $J = CP_\mathrm{tot}$ the relative bias $b$ of the load is

$$b=\frac{P_\delta}{P_\mathrm{tot}},\qquad P_\delta=\frac{\delta_0L_\mathrm{tot}}{C}. \tag{10}$$

The offset-equivalent load $P_\delta$, at which the bias reaches 100 %, combines sensor position and baseline stability into one number, to be compared with the lightest vehicle to be screened.

### 2.4. Multi-channel estimation and sensor placement

Let channel $j$ give the integral $J_j = C_jP_\mathrm{tot} + \delta_{0,j}L_\mathrm{tot} + n_j$, with white noise $n_j$ and offsets that may be correlated between channels, and let $\Sigma$ be the covariance matrix of $J$. A linear estimator $\hat P = a^\top J$ is unbiased for every axle configuration if and only if $a^\top C = 1$, and minimizing its variance gives the GLS weights

$$a^\star=\frac{\Sigma^{-1}C}{C^\top\Sigma^{-1}C},\qquad \mathrm{Var}\,\hat P^\star=\big(C^\top\Sigma^{-1}C\big)^{-1}, \tag{11}$$

the Gauss–Markov best linear unbiased estimator. A non-uniform weighting function along one record cannot do better, because only uniform weighting keeps the estimate independent of the axle configuration for every structure (Supplementary Section S3). Adding the constraint $\sum_ja_j = 0$ within each channel type cancels any disturbance shared by the channels, such as an offset, a drift or motion of the reference frame. With equal statistics in all channels, the variance of this zero-sum estimator is

$$\mathrm{Var}\,\hat P_\mathrm{zs}=\frac{\sigma^2\Delta x\,L_\mathrm{tot}+(1-\rho)\delta_0^2L_\mathrm{tot}^2}{\sum_j(C_j-\bar C)^2}, \tag{12}$$

with $\sigma$ the standard deviation of the white noise, $\Delta x$ the sampling interval and $\rho$ the common-mode fraction of the offset (Supplementary Section S4).

If the noise statistics do not depend on position, $1/\mathrm{Var}$ is a convex quadratic in the constants $C(x_j)$ for both Eqs. (11) and (12), and the feasible constants form a box bounded by the smallest and largest $C(x)$ along the girder. A convex function on a box is maximal at a vertex, as in extreme-point optimal design (Elfving, 1952), so optimal sensors lie at the maximum and the minimum of $C(x)$: of $w_q(x)/q_0$ for deflection, with $w_q$ the uniform-load deflection, and of $c\,M_q(x)/(EI\,q_0)$ for strain, whose extremes on a haunched girder differ from those of $M_q$. With independent offsets every sensor should sit near the extreme of largest $|C|$; with correlated offsets one sensor should sit at the minimum, because a common offset cancels in the difference. A brute-force search and a Monte Carlo study (Eqs. (11) and (12) within 0.6 %) confirm this (Supplementary Section S4). The zero-sum estimator helps only if the disturbance is common-mode during the crossings themselves, not merely in vehicle-free periods, and Section 4.3 shows that real records can violate this.

### 2.5. Identifiability of the constant under boundary uncertainty

A girder with monolithic piers has the stiffness matrix $\alpha K_g + kK_p$, where $K_g$ and $K_p$ are its girder and pier parts, $\alpha$ is the ratio of effective to design girder rigidity and $k$ is the rotational stiffness of each pier. Every static response therefore has the form $f(\kappa)/\alpha$, where $\kappa = k/\alpha$ is the scaled pier stiffness. Only the ratio of two static readings, which is independent of $\alpha$, informs $\kappa$. Identifiability is meant here in the sense of Katafygiotis and Beck (1998), and the Fisher-information criteria used for sensor placement (Udwadia, 1994; Papadimitriou, 2004) are applied in Section 5.3 to the single scalar $C$. For a mirror-symmetric girder with equal piers, the uniform load rotates the two inner piers by equal and opposite amounts ($\theta_6 = -\theta_7$) and excites no other pattern of pier rotation, and the Sherman–Morrison formula gives (Supplementary Section S5)

$$C_m(\alpha,\kappa)=\frac{1}{\alpha}\Big[C_\infty+\frac{C_0-C_\infty}{1+\kappa/k_g}\Big]. \tag{13}$$

$C_0$ and $C_\infty$ are the constants for pinned and for fixed piers at $\alpha = 1$, and $k_g$ is the girder's own stiffness against this pattern of pier rotation ($\theta_6 = -\theta_7$). Equation (13) is referred to below as the Möbius law. The ratio $C_\infty/C_0$ is the full change that pier fixity can produce at a gauge, and the boundary sensitivity $B_m = |\partial\ln C_m/\partial\ln\kappa|$ is the local slope of the Möbius curve $C_m(\kappa)$.

For a symmetric prismatic three-span beam with rotational springs $k$ at the piers, the slope-deflection method gives, with $\hat k$ the pier stiffness relative to the side-span rigidity,

$$\mu(\hat k)=1+\frac{\beta(2\beta^2-3)}{3\beta+2\gamma+\beta\hat k},\qquad \hat k=\frac{kL_\mathrm{side}}{EI_\mathrm{side}}. \tag{14}$$

Equation (14) replaces $\mu_\mathrm{3span}$ in Eq. (5). In the main span the end-moment parameter becomes $\bar M_\mathrm{main}=2(\beta^3\hat k+3\beta^3+3\gamma)/[3\beta^2(\beta\hat k+3\beta+2\gamma)]$, which reduces to $\mu/\beta^2$ for pinned piers. For $\beta = 90/55 = 1.636$, the span ratio of the bridge in Section 5, the side-span indicator at $\xi = 0.4$ rises from 0.287 with pinned piers to 1.037 with fixed piers, while the mid main-span indicator falls from 0.755 to 0.500. Rotational restraint thus moves the side-span gauge away from blindness but makes its constant strongly dependent on $k$.



## 3. Laboratory check of the identity

A static test on a two-span beam checks the model and the algorithm, not performance under moving traffic. A steel hollow square tube, 25 mm × 25 mm × 2.03 mm ($I = 16\,530$ mm⁴, $E = 200$ GPa), formed two equal spans of 2500 mm, giving $C_m = L^4/(192EI) = 61.54$ mm²/N at mid-span of the first span ($L$ the span length). Deflection there was measured with 0.005 mm resolution while calibrated weights of the International Organization of Legal Metrology (OIML) class M1 were suspended at 250 mm steps: a single 40.64 N reference load, two loads 250 mm apart, and three loads. The order of the three loads was not recorded; the order used fits the record best (root-mean-square residual 0.030 mm against 0.55 mm for the reversed order), so the three-load result is not a fully independent test.

The analytical influence line matched the single-load record within 0.0126 mm, 0.44 % of the peak. With the trapezoidal rule, BPM overestimated the weighed totals of 66.99 N and 125.08 N by 1.10 % and 1.19 %, and SLM by 0.61 % and 0.70 % (Supplementary Table S4). The BPM-to-SLM ratio equals 1.0049, the ratio of the measured reference integral to its exact value: SLM absorbs the calibration error of the reference record, whereas BPM does not (Supplementary Section S6). The test supports the invariance of Eq. (2) only indirectly.



## 4. Assumptions and noise model on public moving-truck records

Public records test the assumptions of the identity and the noise model of Section 2.4, with 95 % confidence intervals (CIs).

### 4.1. Data and processing

The Nothing-on-Road BWIM (NOR-BWIM) dataset (Moghadam and Sarlo, 2024) contains strain records of the Virginia Smart Road Bridge (Moghadam, 2022; Moghadam et al., 2022, 2023a, 2023b), a post-tensioned concrete box girder continuous over five spans of 86.5 + 3 × 144 + 86.5 m = 605 m, from transducers on the top-slab soffit near mid-span of span 2. Day 1 has 12 channels (names beginning "ch"), four of them without axle spikes; day 2 has four channels in one line under the wheel path (names beginning "st"). On day 1, two 3-axle trucks with driver-reported gross weights ran in the instrumented lane (Moghadam, 2022). On day 2, a 3-axle truck of 26.8 t and a 5-axle truck of 25.9 t, weighed on a static scale, ran in the instrumented lane (lane A), in the other lane (lane B), and in two runs one behind the other. Each record was re-zeroed with a linear baseline fitted to vehicle-free segments before and after the crossing, integrated over the whole crossing and converted to $\int\varepsilon\,\mathrm{d}x$ with the speed from the axle spikes (Fig. 4); the noise of the integral came from vehicle-free windows of crossing length.

::: {custom-style="Figure"}
![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/Fig4_norbwim_crossings.png){height=12cm}
:::

::: {custom-style="Caption justified"}
**Figure 4.** NOR-BWIM strain records of three single-truck crossings of the five-span girder, against time; the integrals are converted to space with the measured speed. Thin traces: the same gauges unfiltered; thick traces: low-pass filtered at 0.5 Hz; vertical lines: entry and exit of the truck. Shaded: integration window; dashed: beam-model shape; legend values: integral $\int\varepsilon\,\mathrm{d}x$ per gauge, in µε m.
:::

### 4.2. Invariance, lanes and gauges

The records show invariance between trucks only within margins of 12 % (day 1) to 27 % (day 2). On day 2, the ratio of the gauge-average constants of the 5-axle and the 3-axle truck is 0.98 (95 % CI 0.70–1.37; Fig. 5b): consistent with Eq. (2), but with eight runs an equivalence test (90 % CI 0.76–1.27) cannot exclude differences of up to about 27 %, so it is a coarse check of linearity and processing. On day 1, the four gauges without axle spikes give constants 22–26 % lower for the second truck, but speed and truck are almost perfectly confounded, so wheel path, local deck action or speed may cause this. Per-gauge tests (Fig. 5a), the confounding and the speed effect are treated in Supplementary Section S7 (Tables S6 and S7, Fig. S9).

::: {custom-style="Figure"}
![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/Fig5_norbwim_invariance.png){width=14cm}
:::

::: {custom-style="Caption justified"}
**Figure 5.** Ratio of the integral constants of two trucks, per gauge and gauge average, with 95 % confidence intervals: (a) day 1, second to first 3-axle truck, gauge average over the four wheel-path gauges; (b) day 2, 5-axle to 3-axle truck; the CI of st40 in (b) extends beyond the axis. Gray band: ±10 %. Red: invariance rejected; blue: equivalent within ±10 %; orange: inconclusive.
:::

The evidence favors lane-specific constants. For the gauge average, return trips in lane B gave constants 0.79 times those of lane A (95 % CI 0.59–1.00), as on another continuous girder (Wu et al., 2020), but the lane effect is clearly resolved for one gauge only (st36; Supplementary Section S7). For the gauge average, the two runs with the trucks one behind the other gave 0.92 of the summed single-truck predictions (pooled 95 % CI 0.77–1.06), consistent with superposition although both runs fall below the prediction.

Each deck gauge needs its own constant, from a weighed vehicle or a three-dimensional model, because the deck-soffit gauges also respond to slab bending and shear lag. The constant of ch11 is 3.9 times that of ch8, although the gauges are within 6 m of each other and a one-dimensional beam model predicts nearly equal constants, and the st36-to-st40 ratio changes with the lane (Supplementary Section S7); both observations make a spread of gauge factors an unlikely cause. A beam model still reproduces the global shape of the strain histories and confirms two points of Section 2: the gauges are not blind, since the zeros of the uniform-load moment diagram in span 2 lie about 35 m away, and the whole 605 m crossing must be integrated, since span 2 contributes about 170 % of the net integral (Supplementary Section S7).

### 4.3. Noise model and multi-channel estimators

Single gauges, the gauge average, GLS (Eq. (11)) and the zero-sum estimator (Eq. (12)) were compared by leave-one-run-out cross-validation with $\Sigma$ from vehicle-free windows (Table 2; further results in Supplementary Table S8 and Fig. S10).

**Table 2.** Mean absolute error (MAE) of the gross weight (% of gross vehicle weight), leave-one-run-out, with 95 % percentile bootstrap CIs (10 000 resamples of the test runs; 8 runs on day 2, 7 on day 1). GLS uses $\Sigma$ measured in vehicle-free windows. With so few runs, percentile intervals may under-cover.

| Estimator | Day 2, 4 gauges | Day 1, 12 gauges |
|:---|---:|---:|
| Gauge average | 11.9 (6.0–18.6) | 5.3 (2.5–7.8) |
| GLS, measured $\Sigma$ | 20.4 (12.3–28.8) | 5.8 (3.5–8.1) |
| Best single gauge (chosen after the fact) | 8.4 (2.9–15.3) | 4.8 (1.8–7.9) |
| Mean-weight predictor (mean of the calibration runs) | 2.0 (1.9–2.0) | 2.2 (1.1–3.5) |

On day 2, GLS was worse than the gauge average, 20.4 % against 11.9 % MAE, with a paired difference of +8.5 percentage points (95 % CI +2.3 to +15.1); the zero-sum estimator (20.3 %) was worse as well. On day 1 the estimators cannot be told apart. A predictor that always returns the mean calibration weight beats every estimator on both days, so the records cannot show weight discrimination.

The vehicle-free noise of the four day-2 channels is strongly common-mode, but the crossing residuals (deviations of each crossing's integral from its calibrated value) are much less correlated between gauges: 0.63 against 0.90 for vehicle-free noise at the same window length. The vehicle-free covariance therefore predicted GLS to beat the average; the residual covariance reproduces the observed order, an in-sample consistency check only (Supplementary Section S7). The gauge-specific component of each crossing, plausibly from the wheel path and local slab action, is amplified by the large GLS weights of opposite sign on st40 and st36. Vehicle-free windows are therefore not enough to estimate $\Sigma$, and hence $\rho$. Crossing residuals are the better basis but were not sufficient here: with eight runs, $\Sigma$ estimated from them over-fitted (MAE 8.5 % in sample against 23.4 % out of sample; Supplementary Section S7), so enough calibration crossings and an out-of-sample check are needed.



## 5. Design case: an in-service three-span box girder

### 5.1. Bridge, data and model

The Mây Bridge crosses the Kinh Môn River in Hải Dương, Viet Nam. Its main bridge is a 55 + 90 + 55 m continuous prestressed concrete box girder built by balanced cantilever ($\beta = 1.636$), 2.40 m deep at mid-span and 5.40 m at the piers. The inner piers T6 and T7 are monolithic with the girder; the end supports T5 and T8 carry pot bearings. In the June 2020 acceptance test, 3-axle trucks with a mean weighed gross weight of 25.06 t stood in the side and main spans, and dial gauges read the peak deflection at N8, in the side span at 0.4$L$ (22 m) from T8, and at N7, mid main span. Each section has six readings (three points across, central and eccentric arrangements), with means of 5.55 mm at N8 and 15.43 mm at N7 (Supplementary Tables S11 and S12; axle positions in Table S16).

The Euler–Bernoulli model has a parabolic depth variation over $L_\mathrm{v} = 44$ m from each inner pier, a second moment proportional to $h^{2.943}$, where $h$ is the girder depth, and a rotational spring $k$ at each inner pier; other haunch lengths and exponents and a rigid pier zone were tested as model-form variants (Supplementary Section S8). Calibration A, the design model, has $\alpha = 1$ and $k = 2.75\times10^7$ kN m/rad fitted to the designer's FE output and deviates from the measurements by +2.4 % at N8 and +12.3 % at N7. Calibration B, the joint least-squares fit, has $\alpha = 0.716$ and $k = 1.2\times10^8$ kN m/rad, with misfits of −2.8 % and +2.9 %. A lies at $\kappa = 2.75\times10^7$ kN m/rad and B at $\kappa = 1.68\times10^8$ kN m/rad. Both $k$ and $\alpha$ are effective parameters: they also absorb mechanisms that the beam model omits, such as shear deformation, shear lag, frame action of the monolithic piers and bearing friction. Figure 6 shows the indicators along the girder.

::: {custom-style="Figure"}
![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/Fig6_caumay_channels.png){height=12cm}
:::

::: {custom-style="Caption justified"}
**Figure 6.** Mây Bridge girder: indicators for a prismatic model with pinned piers and for the haunched model under calibrations A and B: (a) deflection $N_w$; (b) strain $N_M$; (c) strain indicator including the gain, $N_\varepsilon = N_M\,(c/EI)/(c/EI)_\mathrm{mid}$, that is, the strain constant $C_\varepsilon$ in units of $(c/EI)_\mathrm{mid}L^2/8$, with $(c/EI)_\mathrm{mid}$ the gain of the mid main-span section and $c\propto h$. Dots in (b): strain blind points (zeros of the uniform-load moment). Dotted lines: gauges N7 and N8 (0.4$L$) and the mid side-span position. In all panels each indicator is normalized by the span containing the point, so steps at the piers are changes of scale.
:::

### 5.2. What the static data identify

The admissible set contains every model whose misfit at each gauge is within $\tau$ = 5.3 %, two combined standard uncertainties (measurement and model form) of a section mean (Supplementary Section S8). Over this set, the largest constant of the side-span gauge N8 is 6.6 times the smallest, against 1.5 for the main-span gauge N7, when the effective-to-design rigidity ratio $\alpha$ is free, and 2.4 against 1.1 when $\alpha$ is bounded to the material range 0.9–1.3 (Table 3; Supplementary Table S13). Across the model-form variants the factors are 2.6–16 for N8 against 1.3–1.6 for N7, so the contrast holds although its size depends on the model. The two factors are scenarios, not an estimate and a correction: the bound $\alpha$ = 0.9–1.3 excludes calibration B. The factor of 6.6 is carried by the N8 constant $C_8$, which ranges from $3.0\times10^{-5}$ to $2.0\times10^{-4}$ m²/kN; its upper end needs $\alpha \approx 0.5$ with $\kappa$ toward fixity (Table 3, note b).

No single model fits both gauges; the remaining misfit ratio of 4–9 % is model-form error. The misfit ratio $r_{87}$ (measured-to-model ratio at N8 divided by that at N7) has its minimum, 1.058, at calibration B (Fig. 7a), and the model-form variants move the minimum between 1.039 and 1.092 but never to 1. The $\alpha = 0.716$ of calibration B is an effective rigidity 28 % below design, which is implausible as a material loss in a recently built prestressed girder.

::: {custom-style="Figure"}
![](/home/user/SHM-Paper1-1D/manuscript/ase/figures/Fig7_caumay_identifiability.png){width=14cm}
:::

::: {custom-style="Caption justified"}
**Figure 7.** Identifiability of the Mây Bridge pier stiffness: (a) misfit ratio $r_{87}$ against $\kappa = k/\alpha$, with model-form variants (gray: haunch length $L_\mathrm{v}$, haunch exponent, rigid pier zone) and admissible band $|\ln r_{87}|\le 2\tau$ implied by a misfit within $\tau$ = 5.3 % at each gauge; (b) N8 and N7 indicators and cancellation ratios along the best static fit $\alpha^*(\kappa)$; shaded: admissible range of $\kappa$. $r_{87}$: measured-to-model ratio at N8 divided by that at N7; $\alpha^*(\kappa)$: effective-to-design rigidity ratio that best fits both readings at given $\kappa$ (log least squares; equal and opposite log misfits at N8 and N7).
:::

At $\tau$ = 5.3 % the data bound $\kappa$ only from below: every $\kappa \ge 1.8\times10^7$ kN m/rad is admissible, with $\alpha$ between 0.51 and 1.15. The tolerance treats the six transverse readings as independent samples, so Supplementary Table S13 repeats the analysis at $\tau$ = 3 and 4 %; the contrast between the gauges persists (1.5 against 1.1 and 3.4 against 1.4), and at $\tau$ = 3 % the admissible set excludes the design rigidity, $\alpha = 1$.

The side-span constant is this uncertain because the design pier stiffness lies near the steepest part of the Möbius curve of Eq. (13), where the boundary sensitivity $B_m$ is 0.51 at N8 against 0.12 at N7; calibrating to the N8 reading does not fix the N8 constant either (Supplementary Section S8 and Table S15).

**Table 3.** Deflection indicator $N_w$, Eq. (8), and cancellation ratio $R$, Eq. (9), of the installed Mây Bridge gauges; $EI_\mathrm{ref}$ = design $EI_\mathrm{mid}$ (mid main span), $L$ = span containing the gauge. $\alpha = 1$ except for calibration B ($\alpha = 0.716$) and the admissible sets ($\tau$ = 5.3 %; $\alpha$ = 0.51–1.15, or 0.90–1.15 with the prior $\alpha$ = 0.9–1.3); haunched rows: base model ($L_\mathrm{v}$ = 44 m). Values at mid side span: Supplementary Table S15.

| Model | $N_w$, N8 at 0.4$L$ | $N_w$, N7 | $R$, N8 at 0.4$L$ | $R$, N7 |
|:---|---:|---:|---:|---:|
| Prismatic beam, pinned piers | 0.287 | 0.755 | 0.14 | 0.70 |
| Haunched, calibration A | 0.181 | 0.209 | 0.18 | 0.59 |
| Haunched, calibration B | 0.476ᵃ | 0.234 | 0.56 | 0.77 |
| Haunched, admissible set | 0.124–0.822ᵇ | 0.190–0.286 | 0.13–1.00 | 0.56–1.00 |
| Haunched, admissible set with prior $\alpha$ = 0.9–1.3 | 0.124–0.297 | 0.190–0.211 | 0.13–0.34 | 0.56–0.66 |
| Haunched, pinned piers | 0.030 | 0.248 | 0.02 | 0.51 |
| Haunched, fixed piers | 0.422 | 0.147 | 1.00 | 1.00 |

ᵃ Above the fixed-pier value because calibration B has $\alpha$ = 0.716; normalized by the effective rigidity $\alpha EI_\mathrm{mid}$: 0.341. ᵇ The upper part requires $\alpha \approx 0.5$; normalized by the effective rigidity: 0.144–0.422.

The main-span indicator is low (0.19–0.29) although $R$ is 0.56–1.00, so its smallness reflects restraint by the haunches, not cancellation.

### 5.3. Which channel, where

For this girder the deflection channel at mid main span is the robust choice. A side-span deflection gauge is ill-conditioned with respect to pier stiffness and should not take its constant from a design model unless that stiffness is identified.

Strain channels are no better on this girder (Fig. 6). The haunches move every zero-moment point toward mid-span, so a strain gauge at mid side span would be practically blind under calibration A ($N_M = 0.048$), and mid main span lies in or at the edge of the near-blind band in every haunched model ($N_M$ = 0.163–0.212 at N7), again because of restraint. By $N_M$ alone the best strain locations in all haunched models are 5–10 m from the piers, but with $c\propto h$ their gain $c/EI$ is about one quarter to one third of that at mid-span (Fig. 6c), so the placement rule, which ranks by $C_\varepsilon = cM_q/(EI\,q_0)$, disagrees with the ranking by $N_M$. Which governs depends on whether strain resolution or offset sets the noise. Further strain and end-reaction values are in Supplementary Section S8.

Placement is insensitive to the unresolved pier stiffness. The placement rule puts a second deflection sensor at the most negative constant, in the side span 4–10 m from the inner pier, and the pair at 100 m and 152 m from T5 is within 1 % in variance of the calibration-specific optimum under both A and B. Under the assumed noise model of Supplementary Section S4 (calibration A), the standard deviation of the load for a 220 m record (200 m plus a 20 m convoy allowance) falls from 24.8 % with N7 alone to 10.6 % with the pair and the zero-sum estimator; this gain is an upper bound, because such common-mode behavior need not hold during crossings (Section 4.3).

If a model-based constant is wanted, a tiltmeter on the monolithic pier T7 is the most informative of the measurements compared: at the design pier stiffness (Supplementary Section S8), the Cramér–Rao bound on the standard deviation of $\ln C_8$ falls from 0.87 with the two deflections to 0.18 with the tiltmeter. The bound assumes standard uncertainties of 2.64 % per deflection and 3 % of the pier rotation; the rotation itself is about 167 µrad under the side-span test load.

A moving-load test with weighed trucks has been designed but not performed; its predictions are in Supplementary Table S19. The ratio of the N8 and N7 integrals is independent of truck weight and absolute rigidity and differs by a factor of 2.3 between A and B.



## 6. Design implications and limitations

For design before installation (checklist in Supplementary Section S10), one static analysis under a uniform unit load on each lane gives the constant of every candidate channel. Strain gauges should stay out of the near-blind band $|N_M|<0.2$ around every zero-moment point, including gauges set back from a pier, and deflection gauges out of the bands of Table 1. Equation (13) gives the constant over the plausible range of pier stiffness; locations with large $C_\infty/C_0$ or $B_m$ should be avoided, or a measurement that identifies $\kappa$ should be planned (a pier tiltmeter, an identified first frequency or an integral ratio between two gauges). SLM with lane-specific constants from weighed vehicles of clearly different weights is preferred to GLS or zero-sum weights unless $\Sigma$ is checked out of sample (Section 4.3).

The residual offset limits single-channel accuracy on long spans. Over the Mây Bridge admissible set, with $L_\mathrm{tot} = 200$ m, $\delta_0 = 0.1$ mm biases a 25 t truck by 16–25 % at a single main-span gauge and by 41–271 % at a single side-span gauge (Supplementary Table S17). Single-point influence-area weighing on this 200 m unit is therefore marginal even at the best location. Non-contact techniques, such as terrestrial laser scanning of bridge deflection (Vu et al., 2023), must establish their residual offset on site, because environmental effects act over the same window (Sohn, 2007; Cross et al., 2013). The speed estimator alone can shift the weight by more than 10 %, and dynamics add a further term (Frýba, 1999; Supplementary Sections S9 and S10). The method is therefore proposed for preliminary overload screening. Its threshold should be set with a margin below the legal limit and the design live loads (CEN, 2003; AASHTO, 2024), and flagged vehicles should be weighed by influence-line BWIM, which does not suffer the blindness of Table 1 because it fits the whole record shape.

Several limitations remain. The strain criterion holds for gauges that measure global bending, not for deck-soffit gauges (Sections 2.1 and 4.2). The laboratory beam had equal spans and statically positioned loads. The field data come from one public dataset with four trucks, nearly constant reference weights, no deflection channel and no gauge at a zero-moment point, so weight discrimination, the strain and deflection blind loci and a deflection pair could not be tested, and a screening threshold still needs field calibration with trucks of clearly different weights. The in-service analysis uses static data and a beam model with an assumed depth law and equal pier springs. The treatment is one-dimensional along each lane.



## 7. Conclusions

The main results are as follows.

1. Blind loci. Strain channels that measure global bending are blind at every zero of the uniform-load moment diagram, which every continuous girder has, and nearly blind at 0.19–0.32 of the span from the interior support on two equal spans. On prismatic girders, deflection channels are blind only near particular span ratios, such as $\lambda = (3+\sqrt{33})/6$ for a mid-span gauge on two spans of equal rigidity and $\beta = 1.7006$ for a mid side-span gauge on three symmetric spans, and in the main span of three nearly equal spans.
2. Placement. For position-independent noise, optimal sensors lie at the extremes of the uniform-load response, for strain at the extremes of $cM_q/EI$.
3. Pier stiffness. For a symmetric girder with equal piers, the constant is a linear-fractional (Möbius) function of the scaled pier stiffness. On a 55 + 90 + 55 m box girder, two static readings leave the side-span deflection constant of the base model uncertain by a factor of 6.6 against 1.5 for the main-span constant, or 2.4 against 1.1 with girder rigidity bounded to 0.9–1.3 times the design value; at the design pier stiffness a pier tiltmeter would reduce the Cramér–Rao bound on the standard deviation of $\ln C_8$ from 0.87 to 0.18.
4. Public records. On public moving-truck records, the gauge-average constants were consistent with invariance and superposition within the 12 % (day 1) to 27 % (day 2) that the noise resolves, although four day-1 gauges differed by 22–26 % between trucks; each deck gauge needed its own constant. On one day, GLS weights from vehicle-free noise were worse out of sample than the gauge average (20.4 % against 11.9 %).
5. Residual offset. On the same box girder, with a 200 m record, a residual offset of 0.1 mm would bias a 25 t truck by 16–25 % even at mid main span.

The contribution is thus a set of design criteria for choosing channels and locations, not a new weighing method. The next steps are the moving-load test designed for the in-service girder, laboratory tests of the blind configuration, and field calibration with trucks of clearly different weights.



## Acknowledgments

The authors gratefully acknowledge the Laboratory of Transportation Technology and Systems, Faculty of Bridge and Road Engineering, Hanoi University of Civil Engineering, for providing the test facilities used in this study, and A. Moghadam and R. Sarlo for making the NOR-BWIM dataset publicly available. They also thank the Hải Dương provincial project management unit and Công ty TNHH Tư vấn Đại học Xây dựng (HUCE consultancy) for permission to use the acceptance-test data of the Mây Bridge.

During the preparation of this work the authors used Claude (Anthropic) to assist with code development and debugging and with language editing. All scientific formulations, procedures, numerical results and interpretations were independently reviewed and verified by the authors, who take full responsibility for the content of the manuscript.

## Author contributions

Quoc-Bao Nguyen: Conceptualization, Methodology, Investigation, Data curation, Formal analysis, Software, Writing – original draft. Thai-Son Vu: Conceptualization, Investigation, Validation, Supervision, Project administration, Writing – review & editing.

## Statements and Declarations

### Ethical considerations

Not applicable.

### Consent to participate

Not applicable.

### Consent for publication

Not applicable.

### Declaration of conflicting interests

The Mây Bridge load test analyzed in Section 5 was performed by an author of this paper (Q.-B. Nguyen) as part of inspection work carried out by Công ty TNHH Tư vấn Đại học Xây dựng (HUCE consultancy). The authors declare that there is no other conflict of interest regarding the publication of this article.

### Funding

This research did not receive any specific grant from funding agencies in the public, commercial or not-for-profit sectors. The work was carried out as part of the authors' employment at Hanoi University of Civil Engineering.

### Data availability

The field strain records analyzed in Section 4 are publicly available in the NOR-BWIM dataset (figshare, https://doi.org/10.7294/26880898.v1, CC0; Moghadam and Sarlo, 2024). The Mây Bridge load test was performed by an author of this paper, and the authors are permitted to publish the processed data. The laboratory mean readings and the processed Mây Bridge data are in the Supplementary Material; these data, the scripts with their logs and the derived data (CSV and NumPy files) are archived on Zenodo (https://doi.org/10.5281/zenodo.23535533); the records behind Figs. S16 and S17 are not.



## References

AASHTO (2024) *LRFD Bridge Design Specifications*. 10th ed. Washington, DC: American Association of State Highway and Transportation Officials.

Agüero-Barrantes P, Christenson RE and Lobo Aguilar S (2023) Utilizing Kriging metamodeling to provide practical and effective bridge weigh-in-motion. *Journal of Bridge Engineering* 28(2): 04022138. DOI: 10.1061/JBENF2.BEENG-5760.

Agüero-Barrantes P, Lobo Aguilar S and Christenson RE (2021) Sparse sensing bridge weigh-in-motion for single-span bridges. *Métodos y Materiales* 11: 43–53. DOI: 10.15517/mym.v11i0.46400.

Al-Qadi I, Wang H, Ouyang Y, Grimmelsman K and Purdy JE (2016) *LTBP Program's Literature Review on Weigh-in-Motion Systems*. Report FHWA-HRT-16-024, Federal Highway Administration, Washington, DC. https://rosap.ntl.bts.gov/view/dot/35735.

Cardini AJ and DeWolf JT (2009) Implementation of a long-term bridge weigh-in-motion system for a steel girder bridge in the interstate highway system. *Journal of Bridge Engineering* 14(6): 418–423. DOI: 10.1061/(ASCE)1084-0702(2009)14:6(418).

CEN (2003) *EN 1991-2:2003, Eurocode 1: Actions on Structures – Part 2: Traffic Loads on Bridges*. Brussels: CEN.

Chan THT, Law SS, Yung TH and Yuan XR (1999) An interpretive method for moving force identification. *Journal of Sound and Vibration* 219(3): 503–524. DOI: 10.1006/jsvi.1998.1904.

Chaudhary MTA, Morgese M, Taylor TW and Ansari F (2025) Method and application for influence-line-free distributed detection of gross vehicle weights in bridges. *Structures* 73: 108298. DOI: 10.1016/j.istruc.2025.108298.

Cross EJ, Koo KY, Brownjohn JMW and Worden K (2013) Long-term monitoring and data analysis of the Tamar Bridge. *Mechanical Systems and Signal Processing* 35(1–2): 16–34. DOI: 10.1016/j.ymssp.2012.08.026.

Dang NTV, Ho DD and Ha MT (2023) [Diagnosis of stiffness reduction in beam structures using displacement influence line data]. *Journal of Science and Technology in Civil Engineering (HUCE)* 17(3V): 47–65 (in Vietnamese). DOI: 10.31814/stce.huce2023-17(3V)-04.

Deng L, Liu P, Huang T and Kaewunruen S (2025) A novel moving load identification method for continuous rigid-frame bridges using a field-based displacement influence line. *Applied Sciences* 15(11): 6028. DOI: 10.3390/app15116028.

Elfving G (1952) Optimum allocation in linear regression theory. *Annals of Mathematical Statistics* 23(2): 255–262. DOI: 10.1214/aoms/1177729442.

Fan Y, Zhu J, Pei J, Li Z and Wu Y (2015) Analysis for Yangmingtan Bridge collapse. *Engineering Failure Analysis* 56: 20–27. DOI: 10.1016/j.engfailanal.2015.05.003.

Frýba L (1999) *Vibration of Solids and Structures under Moving Loads*. 3rd ed. London: Thomas Telford.

Ghali A, Neville AM and Brown TG (2017) *Structural Analysis: A Unified Classical and Matrix Approach*. 6th ed. Boca Raton: CRC Press. DOI: 10.1201/9781315273006.

Hao T, Xie Z and Yu M (2019) The identification technology of vehicle weight based on bridge strain time-history curve. *Advances in Structural Engineering* 22(7): 1606–1616. DOI: 10.1177/1369433218823487.

Helmi K, Bakht B and Mufti A (2014) Accurate measurements of gross vehicle weight through bridge weigh-in-motion: a case study. *Journal of Civil Structural Health Monitoring* 4(3): 195–208. DOI: 10.1007/s13349-014-0076-5.

Hong W, Cao Y and Wu Z (2016) Strain-based damage-assessment method for bridges under moving vehicular loads using long-gauge strain sensing. *Journal of Bridge Engineering* 21(10): 04016059. DOI: 10.1061/(ASCE)BE.1943-5592.0000933.

Jacob B, OBrien EJ and Jehaes S (eds) (2002) *Weigh-in-Motion of Road Vehicles: Final Report of the COST 323 Action*. Paris: LCPC.

Katafygiotis LS and Beck JL (1998) Updating models and their uncertainties. II: Model identifiability. *Journal of Engineering Mechanics* 124(4): 463–467. DOI: 10.1061/(ASCE)0733-9399(1998)124:4(463).

Law SS and Zhu XQ (2000) Study on different beam models in moving force identification. *Journal of Sound and Vibration* 234(4): 661–679. DOI: 10.1006/jsvi.2000.2867.

Law SS, Chan THT and Zeng QH (1997) Moving force identification: a time domain method. *Journal of Sound and Vibration* 201(1): 1–22. DOI: 10.1006/jsvi.1996.0774.

Lin SW, Du YL, Yi TH and Yang DH (2023) Influence lines-based model updating of suspension bridges considering boundary conditions. *Advances in Structural Engineering* 26(2): 316–328. DOI: 10.1177/13694332221126374.

Lobo Aguilar S and Christenson RE (2018) A simplified shear-strain based bridge weigh-in-motion method for in-service highway bridges. *Métodos y Materiales* 8: 11–22. DOI: 10.15517/mym.v8i1.34551.

Moghadam A (2022) *Integration of Traffic and Structural Health Monitoring Systems Using a Novel Nothing-On-Road (NOR) Bridge-Weigh-In-Motion (BWIM) System*. PhD dissertation, Virginia Polytechnic Institute and State University, Blacksburg, VA. http://hdl.handle.net/10919/111390.

Moghadam A and Sarlo R (2024) *Nothing-on-Road Bridge-Weigh-In-Motion (NOR-BWIM) Dataset*, version 1. University Libraries, Virginia Tech, figshare. DOI: 10.7294/26880898.v1.

Moghadam A, AlHamaydeh M and Sarlo R (2022) Bridge-weigh-in-motion approach for simultaneous multiple vehicles on concrete-box-girder bridges. *Automation in Construction* 137: 104179. DOI: 10.1016/j.autcon.2022.104179.

Moghadam A, AlHamaydeh M and Sarlo R (2023a) Nothing-on-road bridge-weigh-in-motion used for long-span, concrete-box-girder bridges: an experimental case study. *Journal of Structural Integrity and Maintenance* 8(2): 79–90. DOI: 10.1080/24705314.2023.2165606.

Moghadam A, AlHamaydeh M and Sarlo R (2023b) Dual-purpose procedure for bridge health monitoring and weigh-in-motion used for multiple-vehicle events. *Automation in Construction* 148: 104768. DOI: 10.1016/j.autcon.2023.104768.

Moses F (1979) Weigh-in-motion system using instrumented bridges. *Transportation Engineering Journal of ASCE* 105(3): 233–249. DOI: 10.1061/TPEJAN.0000783.

Nguyen QB, Hoang T and Nguyen HS (2024) [Determination of the load applied on a simply supported beam based on measured deflection data]. *Journal of Science and Technology in Civil Engineering (HUCE)* 18(2V): 61–71 (in Vietnamese). DOI: 10.31814/stce.huce2024-18(2V)-05.

OBrien EJ, Quilligan MJ and Karoumi R (2006) Calculating an influence line from direct measurements. *Proceedings of the Institution of Civil Engineers: Bridge Engineering* 159(1): 31–34. DOI: 10.1680/bren.2006.159.1.31.

OBrien EJ, Rowley CW, González A and Green MF (2009) A regularised solution to the bridge weigh-in-motion equations. *International Journal of Heavy Vehicle Systems* 16(3): 310–327. DOI: 10.1504/IJHVS.2009.027135.

Ojio T and Yamada K (2002) Bridge weigh-in-motion systems using stringers of plate girder bridges. In: *Proceedings of the Third International Conference on Weigh-in-Motion (ICWIM3)*. Orlando, FL, pp. 209–218.

Papadimitriou C (2004) Optimal sensor placement methodology for parametric identification of structural systems. *Journal of Sound and Vibration* 278(4–5): 923–947. DOI: 10.1016/j.jsv.2003.10.063.

Pukelsheim F (2006) *Optimal Design of Experiments*. Philadelphia: SIAM. DOI: 10.1137/1.9780898719109.

Sherman J and Morrison WJ (1950) Adjustment of an inverse matrix corresponding to a change in one element of a given matrix. *Annals of Mathematical Statistics* 21(1): 124–127. DOI: 10.1214/aoms/1177729893.

Shi S, Yarnold M, Hurlebaus S and Mander J (2025) Evaluation of a load cell-based bridge weigh-in-motion system. *Transportation Research Record* 2679(2): 535–549. DOI: 10.1177/03611981241263336.

Sohn H (2007) Effects of environmental and operational variability on structural health monitoring. *Philosophical Transactions of the Royal Society A* 365(1851): 539–560. DOI: 10.1098/rsta.2006.1935.

Udwadia FE (1994) Methodology for optimum sensor locations for parameter identification in dynamic systems. *Journal of Engineering Mechanics* 120(2): 368–390. DOI: 10.1061/(ASCE)0733-9399(1994)120:2(368).

Ventura R, Barabino B and Maternini G (2024) Estimating the frequency of traffic overloading on road bridges. *Journal of Traffic and Transportation Engineering (English Edition)* 11(4): 776–796. DOI: 10.1016/j.jtte.2023.11.005.

Vu DC, Luong ND, Cu VH, Vu NQ and Bui NS (2023) Study on the application of TLS for bridge deflection inspection in Vietnam. *Journal of Science and Technology in Civil Engineering (HUCE)* 17(4): 14–25. DOI: 10.31814/stce.huce2023-17(4)-02.

Wang C, Zhang WS, Pan X, He WY and Ren WX (2026) Deflection influence line identification under moving vehicle based on variational modal decomposition and B-spline basis function. *Advances in Structural Engineering* 29(4): 779–792. DOI: 10.1177/13694332251363355.

Wu B, Wu G, Yang C and He Y (2018) Damage identification method for continuous girder bridges based on spatially-distributed long-gauge strain sensing under moving loads. *Mechanical Systems and Signal Processing* 104: 415–435. DOI: 10.1016/j.ymssp.2017.10.040.

Wu H, Zhao H, Liu J and Hu Z (2020) A filtering-based bridge weigh-in-motion system on a continuous multi-girder bridge considering the influence lines of different lanes. *Frontiers of Structural and Civil Engineering* 14(5): 1232–1246. DOI: 10.1007/s11709-020-0653-0.

Yamaguchi E, Kawamura SI, Matuso K, Matsuki Y and Naito Y (2009) Bridge-weigh-in-motion by two-span continuous bridge with skew and heavy-truck flow in Fukuoka area, Japan. *Advances in Structural Engineering* 12(1): 115–125. DOI: 10.1260/136943309787522614.

Yan WJ, Hao TT, Yuen KV and Papadimitriou C (2022) Monitoring gross vehicle weight with a probabilistic and influence line-free bridge weight-in-motion scheme based on a transmissibility-like index. *Mechanical Systems and Signal Processing* 177: 109133. DOI: 10.1016/j.ymssp.2022.109133.

Yang J, Hou P, Yang C and Zhang Y (2021) Study on the method of moving load identification based on strain influence line. *Applied Sciences* 11(2): 853. DOI: 10.3390/app11020853.

Yu Y, Cai CS and Deng L (2016) State-of-the-art review on bridge weigh-in-motion technology. *Advances in Structural Engineering* 19(9): 1514–1530. DOI: 10.1177/1369433216655922.

Yu Y, Cai CS and Deng L (2018) Nothing-on-road bridge weigh-in-motion considering the transverse position of the vehicle. *Structure and Infrastructure Engineering* 14(8): 1108–1122. DOI: 10.1080/15732479.2017.1401095.

Zhang J, Liu Y and Fan X (2026) An AR(1)-Tikhonov-SVD-GCV framework for stochastic moving load identification driven by bridge multi-point deflection data. *Structures* 88: 111844. DOI: 10.1016/j.istruc.2026.111844.

Zhou C, Demartino C, Narazaki Y, Xu Y, Chatzi E and Spencer BF (2025) Optimal sensor placement for bridge weigh-in-motion using an augmented Kalman filter. *Mechanical Systems and Signal Processing* 241: 113522. DOI: 10.1016/j.ymssp.2025.113522.

Zhou Y, Feng Z, Di SK and Jia ZJ (2026) A novel approach for bending stiffness inversion and rapid evaluation of continuous beam bridges based on a deflection influence line. *Structural Control and Health Monitoring* 2026(1): 1361157. DOI: 10.1155/stc/1361157.

Zhu JH, Wang C, Qi TY and Zhou ZS (2022) Vehicle load identification on orthotropic steel box beam bridge based on the strain response area. *Applied Sciences* 12(23): 12394. DOI: 10.3390/app122312394.

Zhu XQ and Law SS (2006) Moving load identification on multi-span continuous bridges with elastic bearings. *Mechanical Systems and Signal Processing* 20(7): 1759–1782. DOI: 10.1016/j.ymssp.2005.06.004.

Žnidarič A, Kalin J and Kreslin M (2018) Improved accuracy and robustness of bridge weigh-in-motion systems. *Structure and Infrastructure Engineering* 14(4): 412–424. DOI: 10.1080/15732479.2017.1406958.

Zuo XH, He WY and Ren WX (2019) Vehicle weight identification for a bridge with multi-T-girders based on load transverse distribution coefficient. *Advances in Structural Engineering* 22(16): 3435–3443. DOI: 10.1177/1369433219854548.



