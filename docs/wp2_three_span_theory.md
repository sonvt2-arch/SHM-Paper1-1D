# WP2 – Closed-form invariance constant for three-span continuous beams

Author role: Structural Theorist (WP2). Status: draft for the author team, not committed.

Every number in this note comes from one of these scripts. The logs hold their console output:

| script | purpose | log / output |
|---|---|---|
| `code/analysis/cm_3span_theory.py` | SymPy derivation, blind loci, ξ*, observability maps | `code/analysis/logs/cm_3span_theory.log`, `figures/fig_obs_map_3span.png`, `code/analysis/data/obs_map_3span.csv`, `code/analysis/data/obs_map_3span_asym.csv` |
| `code/analysis/cm_multispan.py` (extended) | FE: EI(x), haunch profile, exact non-prismatic element | `code/analysis/logs/cm_multispan.log` |
| `code/analysis/verify_3span.py` | closed form vs FE; FE vs force method; haunch tables | `code/analysis/logs/verify_3span.log`, `code/analysis/data/haunch_3span.csv` |

**Notation warning.** In this note ρ ≡ ρ_EI = EI_m/EI_s, which is main-span rigidity over side-span rigidity (as in the WP2 brief). Eq. (11a) of the manuscript uses ρ_EI = EI_1/EI_2, which is instrumented span over adjacent span. For a side-span sensor the two definitions are reciprocal, so the notation must be unified before the section goes into the paper.

---

## 1. Derivation

1. **Starting point.** The Maxwell–Betti corollary, Eq. (10), gives C_m = w_q(x_m)/q_0. Each C_m below is therefore the deflection at the sensor under a uniform load q_0 on all three spans. The structure has two degrees of static indeterminacy.
2. **Span solution.** Take span i as simply supported, with UDL q_i, rigidity EI_i and end moments M_l, M_r. Sagging is positive, w is positive downward and M = −EI w''. SymPy integrates EI w'''' = q_i with w(0) = w(L) = 0 and the two moment conditions.
3. **Compatibility.** Requiring slope continuity at B and C gives two linear equations in the redundants M_B and M_C (the three-moment equation). SymPy solves them for arbitrary L_1, L_2, L_3, EI_1, EI_2, EI_3 and q_1, q_2, q_3. That general solution is used for the asymmetric map and for the span-wise contributions.
4. **Symmetric beam.** Set L_1 = L_3 = L_s, L_2 = L_m = βL_s, EI_1 = EI_3 = EI_s and EI_2 = ρEI_s. Then M_B = M_C and

$$M_B=M_C=-\frac{q_0L_s^2}{4}\,\frac{\rho+\beta^3}{2\rho+3\beta}\equiv-\frac{q_0L_s^2}{8}\,\mu .$$

5. **Sensor deflection.** Superpose the simply supported UDL response and the end-moment response, evaluate at the sensor and divide by q_0. Then normalise by L^4/(192EI) of the instrumented span.

## 2. Final closed forms (all verified symbolically: `equals F_side(xi,mu)? True`)

**Side-span sensor at ξ = x/L_s:**

$$\boxed{\frac{192EI_sC_m}{L_s^4}=8\Big[\xi(1-2\xi^2+\xi^3)-\frac{\mu}{2}\,\xi(1-\xi^2)\Big],\qquad \mu=\frac{2(\rho+\beta^3)}{2\rho+3\beta}}\tag{11d}$$

Eq. (11d) has the same form as Eq. (11a). Only the scalar μ changes. For two spans, μ = (1+ρ_L³/ρ_EI)/(1+ρ_L/ρ_EI). For three spans the weights 2 and 3 appear because the far span restrains the interior support. With β = ρ = 1, μ = 4/5, compared with μ = 1 for two equal spans.

**Main-span sensor at η = x/L_m:**

$$\boxed{\frac{192EI_mC_m}{L_m^4}=8\Big[\eta(1-2\eta^2+\eta^3)-\nu\,\eta(1-\eta)\Big],\qquad \nu=-\frac{12M_B}{q_0L_m^2}=\frac{3(\rho+\beta^3)}{\beta^2(2\rho+3\beta)}}\tag{11e}$$

**Span-wise contributions** for a mid side-span sensor with uniform EI, each obtained by loading one span only. They are normalised by L_s⁴/(192EI_s):

$$C_1=\frac{15\beta^2+28\beta+8}{2(\beta+2)(3\beta+2)},\quad C_2=-\frac{3\beta^3}{3\beta+2},\quad C_3=\frac{3\beta}{(\beta+2)(3\beta+2)},\qquad \frac{|C_\text{neg}|}{C_\text{pos}}=\frac{6\beta^3}{15\beta+4}.$$

The FE confirms the sign of the influence line in each span: side sensor (+, −, +), main sensor (−, +, −). The influence line does not change sign inside any span, so the span-wise split equals the split into negative and positive area. The general (ξ, β, ρ) expressions are printed in `cm_3span_theory.log`.

## 3. Blind loci and optimal sensor position

| result | formula | value (ρ = 1) | algebraic nature |
|---|---|---|---|
| blind μ, side sensor | μ_crit(ξ) = 2(1+ξ−ξ²)/(1+ξ) | 5/3 at ξ = ½ | same as two-span |
| blind stiffness ratio | ρ_crit(β,ξ) = β[β²(1+ξ) − 3(1+ξ−ξ²)] / [(1−ξ)(1+2ξ)] | — | rational, explicit |
| ditto, ξ = ½ | ρ_crit = 3β(2β²−5)/4 | Cầu Mây 0.436138; Thái Bình −0.5625 (no blind ρ) | explicit |
| blind β, mid side span | 6β³ − 15β − 4 = 0 → β_crit = √(10/3)·cos[⅓ arccos((2/5)√(6/5))] | **1.700594** | cubic, discriminant 65448 > 0, casus irreducibilis (three real roots; no real-radical form, trigonometric closed form) |
| whole side span blind (μ ≥ 2) | β³ − 3β − ρ = 0 → β = 2cos(π/9) | 1.879385 | cubic, trigonometric |
| near-blind edge, \|N\| = 0.2, ξ = ½ | μ = 23/15 ⇔ 30β³ − 69β − 16 = 0 | 1.621399 | cubic |
| blind ν, main sensor | ν_crit(η) = 1 + η − η² | 5/4 at η = ½ | — |
| blind β, mid main span | 3β³ + 10ρβ² − 12ρ = 0 | 0.964706 (main span shorter than side spans) | cubic |
| optimum ξ*, side sensor | 8ξ³ − (12−3μ)ξ² + (2−μ) = 0 | see table below | cubic in ξ. The two-span case reduces to a quadratic only because μ = 1 makes ξ = 1 a root |

**Optimal side-span sensor position (uniform EI).** Closed form from the cubic; FE values in `verify_3span.log`, section B.

| β | μ | ξ* | 192EI_sC_m/L_s⁴ at ξ* | at ξ = ½ |
|---|---|---|---|---|
| 1.0 | 0.80000000 | 0.44603660 | 1.32176895 | 1.30000000 |
| 1.2 | 0.97428571 | 0.42508293 | 1.07563406 | 1.03857143 |
| 1.4 | 1.20774194 | 0.38747142 | 0.75849895 | 0.68838710 |
| 1.5 (Thái Bình) | 1.34615385 | 0.35820014 | 0.58065335 | 0.48076923 |
| 1.63636 (Cầu Mây) | 1.55785124 | 0.29944923 | 0.33162780 | 0.16322314 |
| 1.7 | 1.66563380 | 0.26077470 | 0.22018607 | 0.00154930 |

**Negative-to-positive contribution** for a mid-span sensor, uniform EI (closed form, section C of the log):

| case | C_1 | C_2 | C_3 | sum | neg/pos |
|---|---|---|---|---|---|
| β = 1, side sensor | 1.700000 | −0.600000 | 0.200000 | 1.300000 | 0.31579 |
| Thái Bình, side (β = 1.5) | 1.840659 | −1.557692 | 0.197802 | 0.480769 | 0.76415 |
| Cầu Mây, side (β = 1.636) | 1.870395 | −1.902566 | 0.195395 | 0.163223 | 0.92099 |
| Thái Bình, main | −0.205128 | 1.115385 | −0.205128 | 0.705128 | 0.36782 |
| Cầu Mây, main | −0.162159 | 1.078947 | −0.162159 | 0.754630 | 0.30059 |

**Effect of a piecewise-constant ρ.** ∂μ/∂ρ ∝ 3β − 2β³. For β > √(3/2), a stiffer main span therefore lowers μ and improves the observability of the side span.

## 4. Asymmetric spans and the observability map

`figures/fig_obs_map_3span.png` has two panels:
- **(a)** symmetric beam, uniform EI, 192EI_sC_m/L_s⁴ over β ∈ [0.5, 2.5] and ξ ∈ (0, 1), with the blind locus (thick line), the near-blind band (hatched) and ξ*(β);
- **(b)** asymmetric beam, uniform EI, mid span-1 sensor, over L_1/L_2 and L_3/L_2 ∈ [0.3, 1.2], computed from the general SymPy closed form.

The CSV files listed in the table at the top hold the plotted grids.

The far span has only a weak effect while it stays short. With the sensor at mid span 1, the blind L_1/L_2 is 0.589774, 0.591969, 0.587260, 0.565712, 0.525757 and 0.461410 for L_3/L_2 = 0.3, 0.5, 0.6, 0.8, 1.0 and 1.2.

## 5. Variable EI: haunched box girders

**Assumptions (to be marked in the paper):**
- A1: I ∝ hⁿ with E constant. n = 2, 2.5 and 3 are reported as a sensitivity range.
- A2: parabolic soffit, h = h_mid + (h_pier − h_mid)(1 − d/L_c)², where d is the distance to the pier. The main span has L_c = L_m/2. Each side span has L_c,side = L_m/2 (the balanced-cantilever arm) and constant h_mid beyond it; L_c,side = L_s and 30 m are reported as alternatives for Cầu Mây.
- A3: no constant-depth pier segment, no diaphragms, no shear deformation.
- A4: C_m is normalised by EI(h_mid) of the instrumented span. This is the smallest EI in the span and so the pessimistic choice. The neg/pos ratio does not depend on the normalisation.

**FE.** A non-prismatic element is built from the exact flexibility integrals ∫m_i m_j/EI (8-point Gauss), with 20 elements per span and nodes at the haunch ends. It agrees with an independent force-method solution with adaptive quadrature to ≤ 8e-12 relative in all four checks. The original Hermite element with Gauss-integrated stiffness converges only to about 1e-8 at 200 elements per span. Refining further adds round-off, because the condition number of a fourth-order problem grows as N⁴.

**Cầu Mây** (55+90+55 m; h_mid = 2.4 m, h_pier = 5.4 m; uniform-EI values are 0.1632 at mid side span and 0.7546 at mid main span):

| n | L_c,side (m) | side ξ = ½ | shift vs uniform | neg/pos | ξ* | max side C_m | main η = ½ | neg/pos |
|---|---|---|---|---|---|---|---|---|
| 2.0 | 45 | −0.0242 | −0.1874 | 1.0165 | 0.240 | 0.1451 | 0.3549 | 0.4219 |
| 2.0 | 55 | −0.0326 | −0.1959 | 1.0257 | 0.231 | 0.1224 | 0.3483 | 0.3955 |
| 2.0 | 30 | −0.0601 | −0.2234 | 1.0342 | 0.234 | 0.1403 | 0.3826 | 0.4499 |
| 2.5 | 45 | −0.0404 | −0.2036 | 1.0296 | 0.229 | 0.1222 | 0.2913 | 0.4575 |
| 2.5 | 55 | −0.0436 | −0.2068 | 1.0383 | 0.220 | 0.1006 | 0.2833 | 0.4241 |
| 2.5 | 30 | −0.0940 | −0.2572 | 1.0552 | 0.218 | 0.1119 | 0.3250 | 0.4883 |
| 3.0 | 45 | −0.0494 | −0.2127 | 1.0388 | 0.221 | 0.1050 | 0.2388 | 0.4940 |
| 3.0 | 55 | −0.0472 | −0.2104 | 1.0460 | 0.211 | 0.0851 | 0.2297 | 0.4540 |
| 3.0 | 30 | −0.1206 | −0.2838 | 1.0729 | 0.204 | 0.0894 | 0.2777 | 0.5252 |

Haunching moves the mid side-span value by −0.187 to −0.284, from +0.163 to between −0.024 and −0.121. The value crosses the blind locus: the negative area now exceeds the positive (neg/pos 1.017–1.073). In all nine cases |N| stays below the 0.2 threshold. Even the best side-span position gives only 0.085–0.145, below 0.2, whereas the uniform-EI optimum gives 0.332. **Under assumptions A1–A4, no side-span sensor position on Cầu Mây is outside the near-blind band.** The main span stays observable (0.230–0.383), but haunching roughly halves it relative to the uniform-EI value of 0.755.

**Thái Bình** (42+63+42 m). The depths are **[NEED VALUE]**, so the results are parametrised by r = h_pier/h_mid with L_c,side = 31.5 m. Uniform-EI values are 0.4808 at mid side span and 0.7051 at mid main span.

| r | n = 2 | n = 2.5 | n = 3 | (main η = ½, n = 2 / 2.5 / 3) |
|---|---|---|---|---|
| 1.0 | 0.4808 | 0.4808 | 0.4808 | 0.7051 / 0.7051 / 0.7051 |
| 1.5 | 0.3289 | 0.3006 | 0.2754 | 0.4846 / 0.4396 / 0.3982 |
| 2.0 | 0.2547 | 0.2221 | 0.1964 | 0.3583 / 0.2989 / 0.2484 |
| 2.25 | 0.2311 | 0.1992 | 0.1753 | 0.3136 / 0.2518 / 0.2009 |
| 2.5 | 0.2128 | 0.1824 | 0.1607 | 0.2770 / 0.2144 / 0.1644 |
| 3.0 | 0.1870 | 0.1602 | 0.1428 | 0.2207 / 0.1592 / 0.1128 |

The side-span value of Thái Bình falls below 0.2 when r ≥ 2 with n = 3, when r ≥ 2.25 with n = 2.5, and when r = 3 with n = 2. Moving the sensor to ξ* recovers 0.24–0.44 over the same range (full table in the log and CSV).

## 6. Verification summary (`code/analysis/logs/verify_3span.log`, tolerance 1e-8, **0 failures**)

- **A.** 60 symmetric comparisons over 6 (β, ρ) pairs and 5 sensor positions, using both FE routes (w_q/q_0 with consistent load, and the exact Hermite integral of the influence line). Maximum relative error 7.5e-12 (12 elements per span). The dimensional bridges in metres agree to ≤ 4.3e-13.
- **B.** At β_crit, ρ_crit and the mid-main β_crit the FE gives |N| ≤ 1.8e-13. FE(ξ*) matches the closed form, and the FE slope at ξ* is ≤ 3.6e-7 (central difference, δ = 1e-4).
- **C.** Span-wise contributions agree to ≤ 4.6e-13.
- **D.** Four asymmetric cases agree to ≤ 9.2e-12.
- **E.** The haunched FE (flex element) agrees with the force method to ≤ 8e-12. The piecewise-constant ρ case with the Gauss-stiffness route agrees to 6.4e-11.

Two implementation notes on `cm_multispan.py`:
- With prismatic elements and nodes at the supports and sensor, the FE is nodally exact. Coarse meshes (12 elements per span) are therefore *more* accurate than fine ones. At 800 elements per span the round-off reaches 6e-5 relative.
- The original `__main__` cases and output are unchanged, apart from the new haunch block.

---

## 7. Draft text — Section 2.4 "Three-span continuous beams"

> **2.4. Three-span continuous beams**
>
> The continuous box girders that dominate medium-span construction in Vietnam are mostly symmetric three-span units with a long main span, for example 55+90+55 m at Cầu Mây and 42+63+42 m at Thái Bình. The corollary of Section 2.2 extends to this layout without new ingredients. C_m is still the deflection at the sensor under a uniform load q_0 on the whole structure, divided by q_0. Only the number of redundants increases.
>
> Let the side spans have length L_s and rigidity EI_s, and the main span L_m = βL_s and EI_m = ρEI_s, with EI piecewise constant. By symmetry the two support moments are equal. Slope continuity at an interior support (the three-moment equation) gives M_B = M_C = −q_0L_s²μ/8, with μ = 2(ρ+β³)/(2ρ+3β). Superposing the simply supported response and the end-moment response, as in Section 2.3, gives for a sensor at ξ = x/L_s in a side span
>
> 192EI_sC_m/L_s⁴ = 8[ξ(1−2ξ²+ξ³) − (μ/2)ξ(1−ξ²)], (11d)
>
> and for a sensor at η = x/L_m in the main span
>
> 192EI_mC_m/L_m⁴ = 8[η(1−2η²+η³) − νη(1−η)], ν = 3(ρ+β³)/[β²(2ρ+3β)]. (11e)
>
> Eq. (11d) is Eq. (11a) with a different scalar μ. The far side span restrains the interior support, so a symmetric three-span beam with equal spans has μ = 4/5 rather than 1 and its constant is 1.3 times the two-span value. Both expressions agree with the finite element evaluation of Eq. (10) to better than 1 × 10⁻⁸ relative, and in fact to 10⁻¹¹ (Table X).
>
> Because the form of F is unchanged, the blind condition for a side-span sensor is again μ = μ_crit(ξ) = 2(1+ξ−ξ²)/(1+ξ). The stiffness ratio at which a sensor at mid side span is blind is explicit, ρ_crit = 3β(2β²−5)/4. For uniform rigidity the critical main-to-side span ratio is the real root of 6β³ − 15β − 4 = 0:
>
> β_crit = √(10/3) cos[⅓ arccos((2/5)√(6/5))] = 1.70059. (11f)
>
> Unlike the two-span constants of Eq. (11c), β_crit is a cubic irrational in the irreducible case. It has no expression in real radicals, and the trigonometric form is its exact closed form. The near-blind band |192EI_sC_m/L_s⁴| < 0.2 begins at β = 1.62140 (root of 30β³ − 69β − 16 = 0). For β ≥ 2cos(π/9) = 1.87939, no position in the side span gives a positive constant. The negative contribution of the loaded main span relative to the positive contribution of the two side spans is 6β³/(15β+4) for a mid side-span sensor. It equals 0.764 for 42+63+42 m and 0.921 for 55+90+55 m. Under uniform rigidity the latter is already inside the near-blind band (0.163).
>
> The optimal sensor position solves 8ξ³ − (12−3μ)ξ² + (2−μ) = 0. For two spans this cubic factors into the quadratic of Eq. (11c) because μ = 1. For three spans it does not. ξ* moves towards the abutment as the main span lengthens: 0.4460 for β = 1, 0.3582 for β = 1.5 and 0.2994 for β = 1.636. At β = 1.636 the dimensionless constant doubles, from 0.163 to 0.332. The main span is rarely critical: a mid-main sensor becomes blind only when β < 0.96471.
>
> Fig. Y maps the constant over β and ξ for the symmetric case and over both side-span ratios for asymmetric layouts. The far side span matters little while it is short. For L_3/L_2 between 0.3 and 0.6 the blind ratio L_1/L_2 stays between 0.587 and 0.592.
>
> Real box girders are haunched, and this changes the picture qualitatively. We assumed a parabolic soffit between h_mid and h_pier over the cantilever arm L_m/2, constant E and I ∝ hⁿ with n = 2–3 *[assumption]*, and normalised by the mid-span rigidity. For Cầu Mây (h = 2.4 m at mid-span and 5.4 m at the piers) the mid side-span value moves from +0.163 to between −0.024 and −0.049. The stiff pier regions attract hogging moment, so the main-span uplift exceeds the side-span sag (negative-to-positive ratio 1.017–1.039). No side-span position then exceeds 0.145. The result holds for side-span haunch lengths of 30, 45 and 55 m. Prismatic theory therefore understates the near-blindness of haunched three-span girders. Eq. (11d) remains useful as a screening tool, but for a haunched girder the constant must come from a model with EI(x) or, preferably, from a static uniform-load test, as Section 2.2 recommends. For Thái Bình the depths were not available *[NEED VALUE]*. Over pier-to-mid depth ratios of 1.5–3 its mid side-span value falls from 0.481 to 0.143–0.329.

Word count of the draft section: about 735 words (counted with wc, including the formula lines). The approved section must replace the placeholders Table X and Fig. Y with numbered table and figure references.
