# Package 1B: Optimal invariant multi-channel estimation and sensor placement

Status: theory, placement study and Monte Carlo verification complete. Draft subsection in §7.
The manuscript and existing code were not modified. Every number below comes from the scripts in
`code/theory2/` and their logs in `code/theory2/logs/`.

| Script | Purpose | Log / output |
|---|---|---|
| `multisensor_core.py` | models, $C(x)$, influence lines, noise covariance, estimators | — |
| `multisensor_theory.py` | T1 single-sensor reduction, T2 $O_k$, T3 offset-immune estimator, T4 structure-aware weights | `logs/multisensor_theory.log`, `results/T2_Ok.csv`, `T3_immune.csv`, `T4_structure_aware.csv` |
| `multisensor_placement.py` | extreme-point designs, brute-force check, distinct-position designs, robust Cầu Mây design | `logs/multisensor_placement.log`, `results/placement_*.csv` |
| `multisensor_mc.py` | Monte Carlo, $10^5$ realisations per case, fixed seeds | `logs/multisensor_mc.log`, `results/mc_summary.csv`, `mc_errors.npz` |
| `multisensor_figures.py` | Figs. 1–4 (PNG 300 dpi + PDF) | `figures/ms_fig*.png/pdf` |

Models: prismatic beams with $EI = 10^7$ kN m² (two-span 30+30 m "2S-eq" and 30+60 m "2S-r2"; three-span 30+42+30 m "3S-b1.4" and 30+60+30 m "3S-b2.0"), built with `cm_multispan.py` (Hermite FE, 0.1 m elements). Cầu Mây 55+90+55 m uses `wp3_fe.Bridge`: the haunched $EI(x)$ ($L_v$ = 44 m) and the inner-pier springs of manuscript §4.2. That is the model behind Table 5. `cm_multispan.py`'s own `haunch_EI` has neither the springs nor the calibrations. Calibration A: design $EI$ with $k = 2.748\times10^7$ kN m/rad. Calibration B: $\alpha = 0.716$ with $k = 1.199\times10^8$ kN m/rad. Both are taken from `code/analysis/logs/wp3_run.log`. The model reproduces Table 5: $C$ = 3.61×10⁻⁴ / 4.38×10⁻⁵ m²/kN (A) and 4.05×10⁻⁴ / 1.15×10⁻⁴ m²/kN (B) at N7 / N8. Baseline settings: sampling $\Delta x$ = 0.1 m; record $L_\mathrm{rec} = L + 20$ m (20 m convoy allowance); reference loads $P$ = 250 kN (prismatic) and 245.8 kN (Cầu Mây). Strain channels are bottom-fibre strain with $c$ = 0.6 m, $\sigma_s$ = 1 µε and $\varepsilon_s$ = 2 µε.

---

## 1. Formulation and the minimum-variance invariant estimator

**Channel model.** Channel $j$ ($j = 1..k$; deflection in mm or strain in µε) is sampled at $x_i = i\Delta x$, $i = 0..N-1$, $L_\mathrm{rec} = (N-1)\Delta x$. Following Eq. (16) of the manuscript,

$$z_j(x_i)=(1+\gamma_j)\,y_j(x_i)+\varepsilon_{0,j}+\sigma_j\zeta_{ij},\qquad y_j(x)=\sum_a P_a\,\eta_j(x-s_a). \tag{M1}$$

The integral uses trapezoid weights $\omega_i$:

$$I_j=\sum_i\omega_i z_j(x_i)=C_jP+\varepsilon_{0,j}L_\mathrm{rec}+n_j,\qquad \mathrm{Var}\,n_j=\sigma_j^2\,\Delta x\,(L_\mathrm{rec}-\Delta x/2). \tag{M2}$$

Here $C_j=\int\eta_j$ is the deflection invariance constant ($w_q(x_j)/q_0$) or the strain constant $cM_q(x_j)/(EIq_0)$. The gain $\gamma_j$ is absorbed into $C_j$: SLM calibrates it with the reference crossing, and BPM carries it as a bias. Offsets vary randomly from crossing to crossing with covariance $\Sigma_\varepsilon$. The model takes a common-mode fraction $\rho$ among channels of the same type and treats offsets of different types as independent: $\Sigma_\varepsilon=D(\rho T+(1-\rho)I)D$ with $D=\mathrm{diag}(\varepsilon_j)$. The integral covariance is

$$\Sigma=\mathrm{diag}(\sigma_j^2)\,\Delta x\,(L_\mathrm{rec}-\Delta x/2)+L_\mathrm{rec}^2\,\Sigma_\varepsilon . \tag{M3}$$

Cross-channel correlated white noise, such as camera shake, adds off-diagonal terms to the first matrix. Nothing below changes.

**Invariant linear estimators.** Take $\hat P=w^\top I$. Then $E\hat P=P\,w^\top C$ for every axle configuration, so $\hat P$ is unbiased for every convoy if and only if

$$w^\top C=1. \tag{M4}$$

**Optimal weights (generalised least squares).** Minimising $w^\top\Sigma w$ subject to (M4) with a Lagrange multiplier gives

$$w^\star=\frac{\Sigma^{-1}C}{C^\top\Sigma^{-1}C},\qquad \mathrm{Var}\,\hat P^\star=\big(C^\top\Sigma^{-1}C\big)^{-1}. \tag{M5}$$

This is the Gauss–Markov BLUE of $P$ in the linear model $I = CP + e$, $e\sim(0,\Sigma)$. For Gaussian errors it is also the minimum-variance unbiased estimator based on the integrals. $C^\top\Sigma^{-1}C$ is the multi-channel observability. For $k=1$ it is $C^2/\Sigma_{11}$, the square of the manuscript's indicator $|C_m|$ scaled by the noise.

**Reduction to the single sensor.** For $k=1$, (M5) gives $w = 1/C$, i.e. $\hat P = I_y/C_m$, and

$$\mathrm{Var}\,\hat P=\frac{\sigma^2\Delta x(L_\mathrm{rec}-\Delta x/2)}{C^2}+\Big(\frac{\varepsilon_0L_\mathrm{rec}}{C}\Big)^2=\sigma_{P,\mathrm{noise}}^2+P_\varepsilon^2, \tag{M6}$$

where $P_\varepsilon$ is the manuscript's offset-equivalent load, Eq. (19). Check (T1): 2S-eq mid-span with $\sigma$ = 0.01 mm and $\varepsilon_0$ = 0.1 mm gives Var = 3.595984×10² kN² from both (M5) and (M6), with $w = 1/C$ = 2.370370.

**Exchangeable case.** With equal $\sigma$, $\varepsilon$ and $\rho$ for one channel type, $\Sigma=aI+b\mathbf 1\mathbf 1^\top$, where $a=\sigma^2\Delta x(L_\mathrm{rec}-\Delta x/2)+(1-\rho)\varepsilon^2L_\mathrm{rec}^2$ and $b=\rho\varepsilon^2L_\mathrm{rec}^2$. Then

$$\mathrm{Var}^{-1}=\frac1a\Big[\sum_jC_j^2-\frac{b}{a+kb}\Big(\sum_jC_j\Big)^2\Big]. \tag{M7}$$

**Multi-channel price of invariance.** Under white noise only, compare with the multi-channel matched filter for one axle at a known position, $\mathrm{Var}_\mathrm{MF}=\big(\sum_j\int\eta_j^2/(\sigma_j^2\Delta x)\big)^{-1}$:

$$O_k=\sqrt{\frac{\mathrm{Var}_\mathrm{MF}}{\mathrm{Var}\,\hat P^\star}}=\left(\frac{\sum_jC_j^2/\sigma_j^2}{L_\mathrm{rec}\sum_j\int\eta_j^2/\sigma_j^2}\right)^{1/2}\le1 . \tag{M8}$$

For $k = 1$ this is Eq. (15). T1 reproduces $O_m$ = 0.3308 for the equal two-span mid-span sensor, against $2\sqrt{44765}/1279$ = 0.3308 in the manuscript. $O_k^2$ is the $C_j^2/\sigma_j^2$-weighted mean of the $O_j^2$. Adding channels therefore lowers the variance but never raises the efficiency relative to the matched filter, which benefits from the extra channels too (Table 1).

**Table 1.** $O_k$ (white noise, $L_\mathrm{rec} = L$, one axle) from `T2_Ok.csv`.

| Model | Channels | $O_j$ | $O_k$ |
|---|---|---|---|
| 2S-eq | d@12.6 | 0.3509 | 0.3509 |
| 2S-eq | s@30 (pier strain) | 0.9057 | 0.9057 |
| 2S-eq | d@12.6 + s@12.6 + s@30 | 0.3509, 0.4198, 0.9057 | 0.3547 |
| 3S-b2.0 | d@60 + d@98.5 | 0.4919, 0.2153 | 0.4836 |
| Cầu Mây A | d@100 (N7) | 0.3140 | 0.3140 |
| Cầu Mây A | d@100 + d@155 | 0.3140, 0.0724 | 0.3074 |
| Cầu Mây B | d@100 (N7) | 0.4126 | 0.4126 |

The pier strain gauge is nearly a matched filter ($O$ = 0.906): its moment influence line keeps one sign.

**Offsets dominate the price of invariance.** A matched filter can estimate a constant offset jointly with $P$, because a constant does not look like an influence line. The integral cannot. For 2S-eq d@12.6 with $\sigma$ = 0.01 mm and $L_\mathrm{rec}$ = 80 m (T2), the standard deviations are:

| $\varepsilon_0$ (mm) | 0 | 0.02 | 0.1 | 0.5 |
|---|---|---|---|---|
| std, matched filter (kN) | 0.020 | 0.021 | 0.021 | 0.021 |
| std, integral (kN) | 0.064 | 3.648 | 18.236 | 91.179 |
| ratio | 0.3039 | 0.0056 | 0.0011 | 0.0002 |

In practice the price of invariance is paid in offset sensitivity, not white noise. The rest of this package attacks that term.

---

## 2. Why the weight is uniform within a channel, and where that stops being true

The most general linear estimator is $\hat P=\sum_j\int_0^Tg_j(x)z_j(x)\,\mathrm dx$. By superposition its mean is $E\hat P=\sum_aP_a\,h(s_a)$ with

$$h(s)=\sum_j\int g_j(x)\,\eta_j(x-s)\,\mathrm dx , \tag{M9}$$

so $\hat P$ is invariant for every convoy whose axles enter at shifts $s_a\in[0,S]$, $S=T-L$, if and only if $h(s)=1$ on $[0,S]$.

**Theorem 1 (structure-agnostic invariance forces uniform weights).** Suppose $h(s)=\kappa_\eta$, a constant in $s$, is required for every set of influence lines supported on $[0,L]$, i.e. the weights may not depend on the structure, which is the premise of SLM. Then each $g_j$ is constant on $[0,T]$.

*Proof.* Take a single channel and $s,s'\in[0,S]$. Then $\int_0^L[g(u+s)-g(u+s')]\eta(u)\,\mathrm du=\kappa_\eta-\kappa_\eta=0$ for every admissible $\eta$. If that family spans a dense subset of $L^2(0,L)$ (in the limit, $\eta\to\delta(u-u_0)$), then $g(u+s)=g(u+s')$ for almost every $u\in[0,L]$. Steps of length at most $S$ connect any two points of $[0,T]$, so $g$ is constant almost everywhere. With several channels, apply the argument to each channel with the others' influence lines held fixed. ∎

*Corollary.* Every structure-agnostic invariant linear estimator has the form $\hat P=\sum_jw_jI_j$. The only freedom lies across channels, and (M5) is optimal within it.

**Consequences for signal processing.**
- *Time weighting.* $\int y\,\mathrm dt=\int y(x)/v(x)\,\mathrm dx$ is the weight $g = 1/v(x)$. It is invariant only if the speed is constant. The integral must be taken in space, $I_y=\int y\,v\,\mathrm dt$ with the measured $v(t)$.
- *Windows and tapers* (Hann windows, exponential forgetting, weighting the peak) are non-constant $g$ and break invariance.
- *A linear time-invariant prefilter* with unit DC gain does not: $\int(k*z)=K(0)\int z$, provided the record is extended by the filter length. Low-pass anti-aliasing is therefore harmless.
- *Baseline correction from signal-free pre/post segments* subtracts a linear functional of data that contain no load response. It preserves invariance, but it cannot remove the residual $\varepsilon_0$ left inside the window.

**Proposition 2 (structure-aware weights).** If $\eta$ is known up to a scale factor, the invariant weights form an affine set $\mathcal G_\eta=\{g: Ag=\mathbf 1\}$ with $A_{ki}=\eta(x_i-s_k)$. It contains $\omega/C$ and is much larger than that one point. Its minimum-variance member is $g^\star=W^{-1}A^\top(AW^{-1}A^\top)^{-1}\mathbf 1$ with $W=\sigma^2I+\varepsilon^2\mathbf 1\mathbf 1^\top$. Summing the constraints gives $g^\top\Phi=n_s$ with $\Phi=A^\top\mathbf 1$, and Cauchy–Schwarz then yields the lower bound $\|g\|^2\ge n_s^2/\|\Phi\|^2$. The extra constraint $\mathbf 1^\top g=0$ makes a single channel offset-immune. T4 evaluates these weights for 2S-eq d@12.6 (Table 2, Fig. 4).

**Table 2.** Structure-aware invariant weights relative to the uniform weight (`T4_structure_aware.csv`). "Defect" is $(\max h-\min h)/\bar h$ over 400 random off-grid entry shifts when the true structure differs from the one used to design $g$.

| $S$ (m) | Var opt / unif (white) | CS bound | MF / unif | Var immune / unif (white) | Var opt / unif ($\varepsilon_0$ = 0.1 mm) | Defect opt, sensor +0.5 m | Defect opt, span-2 $EI$ ×1.2 | Defect, uniform |
|---|---|---|---|---|---|---|---|---|
| 2 | 0.1513 | 0.1197 | 0.1192 | 0.1782 | 2.87×10⁻⁶ | 7.31×10⁻⁴ | 5.85×10⁻⁴ | 9.0×10⁻⁶ |
| 5 | 0.1828 | 0.1164 | 0.1137 | 0.2235 | 3.44×10⁻⁶ | 4.41×10⁻⁴ | 9.61×10⁻⁴ | 9.1×10⁻⁶ |
| 10 | 0.2139 | 0.1155 | 0.1056 | 0.2719 | 3.88×10⁻⁶ | 3.56×10⁻³ | 6.86×10⁻³ | 9.0×10⁻⁶ |
| 20 | 0.2624 | 0.1275 | 0.0924 | 0.3556 | 4.44×10⁻⁶ | 6.74×10⁻³ | 2.26×10⁻² | 9.1×10⁻⁶ |
| 40 | 0.3540 | 0.1986 | 0.0739 | 0.5476 | 5.47×10⁻⁶ | 9.25×10⁻³ | 3.26×10⁻² | 8.8×10⁻⁶ |
| 80 | 0.5072 | 0.3748 | 0.0528 | 1.0281 | 7.34×10⁻⁶ | 1.24×10⁻² | 4.63×10⁻² | 9.0×10⁻⁶ |
| 160 | 0.6779 | 0.5760 | 0.0336 | 2.1016 | 9.55×10⁻⁶ | 1.35×10⁻² | 5.03×10⁻² | 9.0×10⁻⁶ |

The table points to a needed correction. The manuscript calls uniform weighting "the only weight invariant to translation" (§2.4). That holds only when the weight must work for every structure. If $\eta$ is known, invariant weights exist that are 1.5 times (S = 160 m) to 6.6 times (S = 2 m) more precise under white noise and that cancel the offset almost entirely. The cost is fragility. A 20 % stiffness error in the uninstrumented span gives a configuration-dependent error of up to 2.3 % at S = 20 m, and a 0.5 m sensor-position error gives 0.7 %. The uniform weight stays invariant to 10⁻⁵ whatever the structure. $O_m$ therefore measures the price of structure-agnosticism, which is the property SLM needs. Suggested rewording for §2.4: "The integral weights the record uniformly, the only weight that is translation-invariant for every structure."

---

## 3. Offset-immune combination

A common-mode offset $\varepsilon_c$ adds $\varepsilon_cL_\mathrm{rec}\sum_{j\in t}w_j$ to $\hat P$. Requiring

$$w^\top C=1,\qquad \textstyle\sum_{j\in t}w_j=0\ \text{ for each channel type } t \tag{M10}$$

makes the estimator immune to the common offset. It is in fact immune to any common-mode disturbance $d(x)$, whatever its shape (drift, camera motion, thermal bending of a reference frame), because $\sum_jw_j\int d=0$. With $M=[C,\mathbf 1_t,\dots]$,

$$w_\mathrm{imm}=\Sigma^{-1}M(M^\top\Sigma^{-1}M)^{-1}e_1,\qquad \mathrm{Var}\,\hat P_\mathrm{imm}=\big[(M^\top\Sigma^{-1}M)^{-1}\big]_{11}. \tag{M11}$$

It equals the GLS estimator (M5) in the limit where the common-mode variance goes to infinity, i.e. the common offset treated as a nuisance parameter. A solution exists if and only if at least two channels of the same type have different $C_j$. In the exchangeable case,

$$\mathrm{Var}\,\hat P_\mathrm{imm}=\frac{a}{\sum_j(C_j-\bar C)^2},\qquad a=\sigma^2\Delta x(L_\mathrm{rec}-\tfrac{\Delta x}{2})+(1-\rho)\varepsilon^2L_\mathrm{rec}^2 , \tag{M12}$$

which is independent of the common-mode offset $b$. For two channels, $w=(1,-1)/(C_1-C_2)$. A channel at a support ($C_2 = 0$) acts as a reference target, and the estimator becomes the familiar differential measurement, $w=(1,-1)/C_1$.

**What it costs in random noise.** Under white noise alone ($\rho = 1$), $\mathrm{Var}_\mathrm{imm}/\mathrm{Var}_1=2C_\mathrm{max}^2/(C_1-C_2)^2$. That is below 1 only if $C_2<-(\sqrt2-1)C_1=-0.414\,C_1$. On the beams studied the most negative constant is small: $C_\mathrm{min}/C_\mathrm{max}$ = 0 (2S-eq; a support), −0.102 (2S-r2), −0.021 (3S-b1.4), −0.091 (3S-b2.0), −0.050 (Cầu Mây A) and −0.008 (Cầu Mây B). The white-noise variance therefore rises by factors of 2.000, 1.647, 1.919, 1.680, 1.816 and 1.968 (T3). The white-noise term, however, is about 10⁻⁴ of the offset term at these settings, so the trade is overwhelmingly favourable (Table 3).

**Table 3.** Standard deviation of $\hat P$ (% of $P$), $\sigma$ = 0.01 mm, $\varepsilon_0$ = 0.1 mm, two channels at $C_\mathrm{max}$ and $C_\mathrm{min}$ (`T3_immune.csv`).

| Model | $x(C_\mathrm{max})$, $x(C_\mathrm{min})$ (m) | single best | GLS-2, ρ=0.9 | immune-2, ρ=0.9 | immune with support reference, ρ=0.9 | GLS-2 = immune-2, ρ=1 |
|---|---|---|---|---|---|---|
| 2S-eq | 12.6, 0 (abutment) | 7.294 | 3.180 | 3.262 | 3.262 | 0.0365 |
| 2S-r2 | 62.9, 19.8 | 0.468 | 0.187 | 0.190 | 0.209 | 0.0018 |
| 3S-b1.4 | 51.0, 28.0 | 4.622 | 1.978 | 2.025 | 2.067 | 0.0183 |
| 3S-b2.0 | 60.0, 98.5 | 1.021 | 0.411 | 0.419 | 0.457 | 0.0035 |
| Cầu Mây A | 100.0, 155.0 | 24.80 | 10.34 | 10.57 | 11.09 | 0.0712 |
| Cầu Mây B | 100.0, 148.9 | 22.12 | 9.570 | 9.811 | 9.891 | 0.0661 |

With $\rho<1$ the residual is the independent part, $(1-\rho)\varepsilon^2L_\mathrm{rec}^2$ in (M12). At $\rho$ = 0.9 the standard deviation falls by a factor of 2.3–2.5. As $\rho\to1$ it falls to the white-noise floor, a reduction of 2–3 orders of magnitude. GLS is never worse than the immune estimator, but it needs $\rho$ and $\varepsilon$. The immune estimator needs neither and is the robust choice. For SLM the immune ratio $P_t=P_0\,(w^\top I_t)/(w^\top I_0)$ with $\sum w_j=0$ cancels the common offset in both crossings. It removes the offset residual that Eq. (18) says "never cancels fully" for a single channel.

---

## 4. Sensor placement

**Theorem 3 (extreme-point placement).** Suppose the noise and offset statistics do not depend on position. Then $\mathrm{Var}^{-1}$ is a convex quadratic form in the vector $C=(C(x_1),\dots,C(x_k))$: $C^\top\Sigma^{-1}C$ for GLS and $C^\top(\Sigma^{-1}-\Sigma^{-1}U(U^\top\Sigma^{-1}U)^{-1}U^\top\Sigma^{-1})C$ for the immune estimator. Because $C(x)$ is continuous on a connected beam, every value in $[C_\mathrm{min},C_\mathrm{max}]$ is attainable. A convex function on a box attains its maximum at a vertex. Hence a D-optimal (equivalently A-optimal, since the parameter is a scalar) design places sensors only at $\arg\max C(x)$ and $\arg\min C(x)$ of the uniform-load response, separately for each channel type. ∎

Placement thus needs one static uniform-load analysis (Eq. 3): place sensors at the extreme points of $w_q(x)$, or of $M_q(x)$ for strain. The number at each point depends on $\rho$. With $\rho$ = 0, all sensors go at the maximum and Var falls by $1/k$. With $\rho > 0$, at least one sensor goes to the minimum, which is a support (reference target) or the most negative location. A brute-force search on a 0.5 m/1.0 m grid confirms the theorem in 96 cases: the minimum ratio of brute-force to vertex variance is 1.000000, and the largest is 1.0017, the grid offset of 12.6 m against 13.0 m.

**Table 4.** Optimal designs with distinct positions ≥ 5 m apart (more realistic than co-location), deflection channels, $\sigma$ = 0.01 mm, $\varepsilon_0$ = 0.1 mm. Each entry gives positions in m and then $\mathrm{Var}_k/\mathrm{Var}_1$ (`placement_distinct.csv`). The ratios are the same at $\varepsilon_0$ = 0.5 mm for $\rho<1$.

| Model (best single; std) | ρ = 0, k = 2 | ρ = 0, k = 3 | ρ = 0.9, k = 2 | ρ = 0.9, k = 3 | ρ = 1, k = 2 | ρ = 1, k = 3 |
|---|---|---|---|---|---|---|
| 2S-eq (12.6; 7.29 %) | 12.5, 47.5; 0.500 | 10.2, 15.2, 47.4; 0.354 | 0, 12.5; 0.190 | 0, 12.6, 47.4; 0.140 | 0, 12.5; 2.50×10⁻⁵ | 0, 12.6, 47.4; 1.87×10⁻⁵ |
| 2S-r2 (62.9; 0.468 %) | 60.5, 65.5; 0.510 | 57.8, 62.8, 67.8; 0.351 | 20.0, 63.0; 0.159 | 19.8, 60.4, 65.4; 0.119 | 20.0, 63.0; 1.50×10⁻⁵ | 16.9, 21.9, 62.9; 1.13×10⁻⁵ |
| 3S-b1.4 (51.0; 4.62 %) | 48.5, 53.5; 0.526 | 46, 51, 56; 0.381 | 28, 51; 0.183 | 28, 51, 74; 0.142 | 28, 51; 1.57×10⁻⁵ | 28, 51, 74; 1.18×10⁻⁵ |
| 3S-b2.0 (60.0; 1.02 %) | 57.5, 62.5; 0.511 | 55, 60, 65; 0.354 | 60, 98.5; 0.162 | 57.5, 62.5, 98.5; 0.122 | 60, 98.5; 1.20×10⁻⁵ | 21.5, 60, 98.5; 9.00×10⁻⁶ |
| Cầu Mây A (100; 24.8 %) | 97.5, 102.5; 0.509 | 95, 100, 105; 0.349 | 100, 155; 0.174 | 97.5, 102.5, 155; 0.130 | 100, 155; 8.25×10⁻⁶ | 45, 100, 155; 6.19×10⁻⁶ |
| Cầu Mây B (100; 22.1 %) | 97.5, 102.5; 0.510 | 95, 100, 105; 0.351 | 100, 149; 0.187 | 97.5, 102.5, 148.9; 0.141 | 100, 149; 8.94×10⁻⁶ | 51.1, 100, 148.9; 6.71×10⁻⁶ |

At $\rho$ = 1 the k = 2 design has std 0.0365 % (2S-eq) and 0.0712 % (Cầu Mây A), set by white noise only. The full grid ($\sigma$ = 0.005–0.02 mm × $\varepsilon_0$ = 0.02–0.5 mm × $\rho$ = 0, 0.5, 0.9, 1 × k = 1–3, GLS and immune, deflection/strain/mixed) has 4200 designs in `placement_vertex.csv`.

**Cầu Mây.** The best single gauge is N7 at mid main span under either calibration: std 24.8 % (A) and 22.1 % (B) at $\varepsilon_0$ = 0.1 mm, which matches the offset-equivalent loads of manuscript Table 8 scaled to $L_\mathrm{rec}$ = 220 m. The second sensor belongs at the most negative $C$, in the side span about 10 m (A) or 4 m (B) from the inner pier ($C_\mathrm{min}/C_\mathrm{max}$ = −0.050 and −0.008). A pier reference ($C$ = 0) is almost as good: std 11.09 % against 10.57 % at $\rho$ = 0.9 (A). The minimax design over the two calibrations is (100, 152) m for k = 2. Its worst variance ratio to the calibration-specific optimum is 1.0090 (GLS, $\rho$ = 0.9), whereas the A-optimal design costs 1.0355 under B. For k = 3 the minimax designs are (98, 103, 152) m (GLS, worst ratio 1.0090) and (48, 100, 152) m (immune, 1.0099). Placement is therefore insensitive to the unresolved pier stiffness, unlike the observability of the side-span gauge N8 (Table 5 of the manuscript).

**Mixed deflection and strain.** For 2S-eq with $\varepsilon_0$ = 0.1 mm, $\varepsilon_s$ = 2 µε and $\rho$ = 0.9, the best k = 2 design is the strain pair at the sagging and hogging extremes of $M_q$: s@11.3 (0.375L) and s@30 (pier), with std 2.71 % against 3.18 % for the best deflection pair. Var ratios to the single best are 0.138 (k = 2) and 0.103 (k = 3: s@11.3 plus two s@30). The opposite signs of $C_s$ at sagging and hogging sections make strain pairs naturally suited to offset immunity.

---

## 5. Monte Carlo verification

Each case has $10^5$ realisations with fixed seeds. Configurations are random: 1–6 axles, loads U(20, 120) kN, spacings U(1, 4) m, and a random entry delay within the 20 m allowance. Full records are synthesised with Hermite-exact influence lines, white noise per sample and offsets drawn from $N(0,\Sigma_\varepsilon)$. Settings: $\sigma$ = 0.01 mm, $\varepsilon_0$ = 0.1 mm, $\rho$ = 0.9. The standard error of an MC/theory std ratio is 0.0022.

**Table 5.** MC results (`multisensor_mc.log`, `mc_summary.csv`).

| Case | Estimator | mean error (kN) [z] | std MC / theory (kN) | ratio | noise-free max $\lvert\hat P/P-1\rvert$ |
|---|---|---|---|---|---|
| A: 30+60+30, d@60, d@98.5, d@15 | single (C_max) | +0.0003 [+0.04] | 2.5586 / 2.5527 | 1.0023 | 8.6×10⁻⁷ |
| | GLS-3 | +0.0028 [+0.98] | 0.9133 / 0.9111 | 1.0024 | 1.3×10⁻⁶ |
| | immune-3 | +0.0029 [+1.01] | 0.9184 / 0.9160 | 1.0026 | 1.4×10⁻⁶ |
| B: Cầu Mây A, d@100, d@155, d@178 | single (C_max) | −0.0908 [−0.47] | 61.202 / 60.947 | 1.0042 | 9.8×10⁻⁷ |
| | GLS-3 | +0.0031 [+0.04] | 23.995 / 23.943 | 1.0022 | 1.6×10⁻⁶ |
| | immune-3 | +0.0087 [+0.11] | 24.241 / 24.200 | 1.0017 | 1.7×10⁻⁶ |
| C: 2S-eq, d@12.6, s@12.6, s@30 | single (d@12.6) | −0.0261 [−0.45] | 18.255 / 18.236 | 1.0010 | 6.0×10⁻⁶ |
| | GLS-3 | −0.0095 [−0.47] | 6.368 / 6.384 | 0.9975 | 4.4×10⁻⁶ |
| | immune (strain pair) | −0.0064 [−0.31] | 6.379 / 6.396 | 0.9972 | 4.4×10⁻⁶ |
| D: 2S-eq d@12.6, S = 20 m | uniform | −0.0138 [−0.24] | 18.348 / 18.236 | 1.0062 | 6.0×10⁻⁶ |
| | structure-aware GLS | +0.0020 [+16.8] | 0.0384 / 0.0384 | 0.9997 | 1.55×10⁻⁵ |
| | structure-aware immune | +0.0020 [+16.8] | 0.0384 / 0.0384 | 0.9997 | 1.55×10⁻⁵ |

- **Unbiasedness and invariance.** All structure-agnostic estimators are unbiased (|z| ≤ 1.01). In noise-free records they reproduce $P$ to within 6×10⁻⁶, the trapezoid quadrature error, for every configuration. Their scatter does not depend on the number of axles. The by-axle-count standard deviations (about 16 700 realisations per bin, standard error 0.55 %) deviate from the pooled value by at most 0.92 % in cases A and B (`logs/multisensor_figures.log`; case A GLS 0.9077–0.9169 kN, case B GLS 23.86–24.15 kN; Fig. 3c).
- **Variance.** MC agrees with (M5)/(M11) to within 0.6 %. Case D uniform deviates by 2.8 standard errors. Four seed replicates of that case, in the log under "Seed replication", bracket the theory, which identifies the deviation as sampling scatter.
- **Common-mode drift.** A deterministic drift $d(x)=0.5+0.5x/L_\mathrm{rec}+0.2\sin(3\pi x/L_\mathrm{rec})$ mm was added to all deflection channels. The immune estimator stays unbiased: +0.0041 kN in case A and +0.0077 kN in case B. The single sensor is biased by +20.22 kN (A) and +482.99 kN (B), the GLS estimator by +0.78 kN and +28.54 kN. All agree with the predicted $w^\top\mathbf 1\int d$: +20.23, +0.77, +482.97, +28.53 kN.
- **Structure-aware weights (case D).** The variance matches theory (ratio 0.9997) and is 4.4×10⁻⁶ of the uniform variance. The off-grid invariance defect, 1.55×10⁻⁵ of $P$ (+0.0020 kN, z = 16.8), is detectable at this noise level but negligible. With a misspecified structure (span-2 $EI$ ×1.2) and the scale calibrated as in SLM, the configuration-dependent error spans −1.12 % to +1.99 % (std 0.77 %). The total std rises from 0.038 to 1.657 kN, still well below the uniform 18.3 kN. This is the fragility in Table 2.

---

## 6. Figures

- `figures/ms_fig1_Cx_extremes` — $C(x)$ for the six models with the extreme points, i.e. the optimal sensor sites (Theorem 3).
- `figures/ms_fig2_placement_gain` — (a) $\mathrm{Var}_k/\mathrm{Var}_1$ against $\rho$; (b) std against $\varepsilon_0$; (c) the offset-immune pair against $\sigma_a$.
- `figures/ms_fig3_montecarlo` — MC error histograms with theoretical normal densities, and std/theory by axle count.
- `figures/ms_fig4_structure_aware` — structure-aware invariant weights, their variance against $S$, and their fragility to model error.

---

## 7. Draft subsection (English, ≤ 900 words)

### 2.5. Optimal invariant multi-channel estimation and sensor placement

Section 6 shows that the residual zero offset, not random noise, limits the single-channel estimator: $\varepsilon_0$ enters the integral as $\varepsilon_0L_\mathrm{tot}$ and is not averaged out. This section asks what several channels can do while keeping invariance to the axle configuration.

Let channel $j$, a deflection or strain, give $I_j=C_jP+\varepsilon_{0,j}L_\mathrm{tot}+n_j$ with $\mathrm{Var}\,n_j=\sigma_j^2\Delta x\,L_\mathrm{tot}$, and let $\Sigma$ be the covariance of the $I_j$, including correlated offsets. A linear estimator $\hat P=\sum_jw_jI_j$ is unbiased for every axle configuration if and only if $\sum_jw_jC_j=1$. Minimising its variance under this constraint gives the generalised least-squares weights

$$w^\star=\frac{\Sigma^{-1}C}{C^\top\Sigma^{-1}C},\qquad \mathrm{Var}\,\hat P^\star=\frac{1}{C^\top\Sigma^{-1}C}. \tag{22}$$

For one channel, Eq. (22) returns $\hat P=I_y/C_m$ with variance $\sigma_{P,\mathrm{noise}}^2+P_\varepsilon^2$, Eq. (19). The quantity $C^\top\Sigma^{-1}C$ generalises $|C_m|$ as a multi-channel observability indicator, and Eq. (15) generalises to $O_k^2=\sum_jC_j^2\sigma_j^{-2}/(L_\mathrm{tot}\sum_j\sigma_j^{-2}\int\eta_j^2)$.

Is the uniform weight within a channel itself optimal? If the weight must give an invariant integral for every structure, which is the premise of the standard-load method, it must be constant along the record: any non-uniform weight $g(x)$ yields a mean $\sum_aP_a\int g(x)\eta(x-s_a)\,\mathrm dx$ that depends on the axle positions for some influence line. Time weighting is a special case. A record integrated uniformly in time weights space by $1/v(x)$, so the integral must be taken in space. A linear time-invariant prefilter with unit static gain leaves the integral unchanged, whereas tapering windows do not. When the influence line is known, non-uniform invariant weights do exist. For the equal two-span beam they are 3.8 times (entry-shift range 20 m) to 6.6 times (2 m) more precise under white noise, and they can cancel the offset. They lose invariance under model error, however: a 20 % stiffness error in the adjacent span produces configuration-dependent errors of −1.1 % to +2.0 %. The uniform weight is therefore the only translation-invariant weight for every structure, and $O_m$ measures the price of not knowing the structure. Within this class the only freedom is across channels.

Across channels a common-mode offset can be cancelled exactly. Adding $\sum_jw_j=0$ to $\sum_jw_jC_j=1$ makes $\hat P$ insensitive to any disturbance shared by the channels, whether a constant offset, a drift or a motion of the reference frame, as in camera-based deflection measurement. For channels with equal noise and offset statistics the resulting variance is

$$\mathrm{Var}\,\hat P_\mathrm{imm}=\frac{\sigma^2\Delta x\,L_\mathrm{tot}+(1-\rho)\varepsilon_0^2L_\mathrm{tot}^2}{\sum_j(C_j-\bar C)^2}, \tag{23}$$

where $\rho$ is the common-mode fraction of the offset. Eq. (23) does not depend on the common offset. For two channels $w=(1,-1)/(C_1-C_2)$, and a second sensor over a support ($C_2 = 0$) gives the familiar differential measurement against a reference target. Against random noise alone, immunity costs a factor $2C_1^2/(C_1-C_2)^2$ in variance, which is below one only if $C_2<-0.41C_1$. On the beams studied this factor is 1.65–2.0. It is negligible, because the white-noise term is about $10^{-4}$ of the offset term. At $\sigma$ = 0.01 mm and $\varepsilon_0$ = 0.1 mm the standard deviation of the load at the Cầu Mây centre-span gauge falls from 24.8 % with one sensor to 10.6 % with an immune pair at $\rho$ = 0.9 and to 0.071 % at $\rho$ = 1. The same pair makes the standard-load ratio $P_0\,w^\top I_t/w^\top I_0$ immune to the common offset in both crossings, a residual that Eq. (18) cannot remove for a single gauge.

Because the noise statistics do not depend on position, $1/\mathrm{Var}$ is a convex quadratic in the vector of constants $C(x_j)$. Its maximum over the attainable range therefore lies at the extremes: optimal sensors sit only at the maximum and the minimum of the uniform-load deflection $w_q(x)$, or of $M_q(x)$ for strain gauges. Placement thus needs the same single static analysis as Eq. (3). Independent offsets call for clustering at the maximum, and two sensors 5 m apart halve the variance. Correlated offsets call for one sensor at the minimum, which is either a support or the most negative point of $w_q$. For the Cầu Mây girder the optimal pair is mid main span plus a side-span point 4–10 m from the inner pier. The pair (100, 152) m is within 0.9 % of the optimum under both calibrations of Section 4.2, and at $\rho$ = 0.9 it reduces the variance to 0.17–0.19 of the best single gauge. Three sensors reduce it to 0.13–0.14. Mixed layouts follow the same rule. On the equal two-span beam a strain pair at $0.375L$ and over the pier, whose constants have opposite signs, outperforms the best deflection pair (2.7 % against 3.2 %).

A Monte Carlo simulation with $10^5$ random axle configurations per case confirms that the estimators are unbiased ($|z|\le1.01$), that their scatter does not depend on the number of axles, and that the variances of Eqs. (22) and (23) are reproduced to within 0.6 %. Under an imposed common drift the immune estimator stays unbiased (+0.004 kN), whereas a single gauge is biased by 20–483 kN.

---

## 8. Caveats and items for the main author

1. **Wording in manuscript §2.4.** Change "the only weight invariant to translation" to "for every structure" (§2, Proposition 2). Otherwise a referee can produce a counterexample.
2. **Assumptions behind Theorem 3.** Position-independent $\sigma$ and $\varepsilon_0$, with co-location allowed. For optical systems, noise grows with target distance, and the optimum then moves inward from the extremes. The brute-force tool in `multisensor_placement.py` handles any $\sigma(x)$.
3. **$\rho$ is the key unknown.** It should be estimated from the quiet pre/post segments of simultaneous channels (the sample correlation of their offsets). The $\rho$ = 1 numbers are the white-noise floor, not a design value.
4. **Strain offsets.** Thermal strain drift is partly common-mode. The value $\varepsilon_s$ = 2 µε is a scenario, not a measurement.
5. **SLM with several channels.** The reference crossing estimates $\hat C_j$ with noise, which adds a term like Eq. (20) to each $w_j$. This was not simulated here.
