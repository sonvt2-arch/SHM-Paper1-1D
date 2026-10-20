# Hostile audit v2, role 1: equations

Scope: Eqs. (1)–(14) and inline formulas of `manuscript/ase/manuscript.md`; Eqs. (S1)–(S2) and inline formulas of `manuscript/ase/supplementary_material.md`; the principal-symbols table and Table S1; equation numbering and every in-text reference to an equation; agreement with `code/theory2` and `code/analysis`; the built files `manuscript/ase/word/*.pdf` and `*.docx`.

## How the checks were done (all re-derived independently; scripts in the session scratchpad)

- sympy: Eq. (4) (two-span support moment; three-moment equation for the symmetric three-span beam), Eq. (5) (simply supported deflection plus the end-moment deflection), Eq. (6), Eq. (7), the end-reaction identity N_F = ξ0, S3 (Φ, N_θ = Φ′, N_V, strain-zero quadratic), S2 (S1, S2, 6β³−15β−4, 30β³−69β−16, 10β³−27β−8, ν, ζ0 = 0.177, β = 0.9647, 2cos(π/9), √(3/2), 2.3028, 2.6691), Table S2 (every entry), Table S3 (every entry), Eq. (14) and M̄_main (slope-deflection from scratch), the 0.287/1.037/0.755/0.500 values in Section 2.5, the pole k̂ = 3 + 2γ/β (Fig. S7).
- Independent numpy Hermite-beam FE: R_ε = 0.667 and R_w = 0.571 (two equal spans), N_w = 1 at mid-span of two equal spans, prismatic Mây proportions (N_w 0.287/0.755, R 0.14/0.70, mid side span 0.163/0.08).
- Eq. (11)/(12): derived the zero-sum optimum (a ∝ C − C̄, Var = numerator × 1/Σ(C_j − C̄)²) under Σ = σ²ΔxL·I + δ0²L²[(1−ρ)I + ρ11ᵀ]; checked against `multisensor_core.noise_cov/gls/immune`. Reproduced 24.8 % (N7 alone, 220 m), 10.6 % (pair 100 m/152 m, zero-sum, ρ = 0.9), 22.5 % (200 m), and the S4 ratios 5 × 10⁻⁶ and 5 × 10⁻⁵.
- Eq. (13): derived via Sherman–Morrison with K_p = aaᵀ + ssᵀ (a, s the normalized antisymmetric/symmetric pier vectors); checked numerically on the haunched Mây model (`ident_core.Model`): max relative error 3.6 × 10⁻⁶ over k = 10⁵–10¹², C∞/C0 = 13.99 (N8) and 0.592 (N7), k_g = 4.358 × 10⁷ kN m/rad, κ/k_g = 0.630, B_m = 0.511 and 0.115, Euler identity S_α + S_k = −1 (to 5 × 10⁻⁴ by finite differences). Table 3 rows for calibrations A and B reproduced (0.181/0.209/0.18/0.59; 0.476/0.234/0.56/0.77).
- Eq. (10): Table S17 ranges reproduced from the C ranges (e.g. 16.3–24.7 % and 41–271 % at 0.1 mm); Fisher-determinant statement (S5) and CRB values (0.865 → 0.177, 167 µrad) agree with `code/theory2/logs/ident_fisher.log`.
- Dimensions of every display equation checked (C in channel·m/kN; m²/kN for deflection; Eqs. (8), (13), (14) dimensionless where required).
- All 50+ in-text equation references were listed and matched to the equation they cite; all are correct in the Markdown.

Everything not listed below was verified correct.

---

## Blocking

**B1. Section 2.2, paragraph after Eq. (6) (also Table 1, Deflection row, three-span column): the claim that equal spans cannot give a deflection blind point is false for interior spans.**
Quote: "A deflection blind point therefore exists only for $1<\mu<2$. In design terms, a deflection gauge cannot be blind on a girder of equal spans and rigidities; blindness needs a longer or stiffer adjacent span …"
Why wrong: the condition 1 < μ < 2 is derived for a span with end moments (0, μ), i.e. an end span. In an interior span with equal end moments (main span of a symmetric three-span beam), the Supplementary's own formula (S2: $192EI_\mathrm{main}C_m/L_\mathrm{main}^4 = 8[\zeta(1-2\zeta^2+\zeta^3)-\nu\zeta(1-\zeta)]$) gives zeros where $1+\zeta-\zeta^2=\nu$. That has interior roots for 1 < ν ≤ 1.25, i.e. 0.9647 ≤ β < 1.2247 (γ = 1). **Three equal spans (β = 1, ν = 1.2) are inside this range**: the uniform-load deflection of the central span is upward near the piers. It is blind at ζ = (1 − 1/√5)/2 = 0.276 from each pier, and |N_w| ≤ 0.10 along the **whole** central span (min −0.079 at ζ ≈ 0.1, +0.100 at mid-span). I confirmed this by independent FE. A four-equal-span FE also has deflection sign changes in both interior spans. Table 1 lists only the side-span deflection locus for three spans, and S2 mentions only the single mid-main-span value β = 0.9647.
Fix: restrict the sentence to end spans ("a deflection gauge in an end span cannot be blind when the spans and rigidities are equal …"). State that interior spans of equal-span girders do have deflection blind points: on three equal spans, ζ = 0.276 from each pier, and the whole central span is near-blind with |N_w| ≤ 0.10. Add the main-span locus to Table 1: blind points for 0.9647 ≤ β < 1.2247 at ζ = ½(1 − √(5 − 4ν)). Check Conclusion 1 ("deflection channels are blind only near particular span ratios") against this.

**B2. Same paragraph: "blindness needs a longer *or stiffer* adjacent span that raises the interior support moment above its value for two equal spans (μ = 1)".**
Why wrong: from Eq. (4), μ_2span > 1 ⇔ λ³ > λ ⇔ λ > 1, whatever γ is. With λ = 1, μ = 1 for any γ. For λ > 1, ∂μ/∂γ = (λ − λ³)/(γ + λ)² < 0, so a stiffer adjacent span *lowers* μ toward 1. The same holds for three spans: μ_3span > 1 ⇔ β² > 3/2, independent of γ, and ∂μ/∂γ < 0 there. So stiffness alone can never raise μ above 1, and added stiffness moves the girder away from blindness.
Fix: "blindness needs a longer adjacent span (λ > 1, or β > √(3/2)), which raises … ; for a given span ratio, a more flexible adjacent span (smaller γ) raises μ further."

## Should-fix

**S1. Supplementary PDF/DOCX: Eqs. (S1) and (S2) have no equation numbers, yet they are cited as numbered equations.**
Where: `Supplementary_Material_ASE.pdf`, p. 3 (λ_crit, ξ*) and p. 4 (β_crit). Both display without "(S1)"/"(S2)". `pdftotext` finds the strings "(S1)"/"(S2)" only in the checklist text. They are cited in the main text, Section 2.2 ("Eqs. (S1) and (S2)"), and in the S10 checklist item 1.
Why: `manuscript/ase/word/build_docx.sh` runs the supplementary pandoc call without `--lua-filter="$W/eqnum.lua"`, so `\tag{S1}`/`\tag{S2}` are dropped. The main-text call has the filter.
Fix: add the lua filter to the supplementary pandoc command and rebuild the DOCX/PDF.

**S2. Manuscript PDF (and Supplementary PDF): overbars and some brackets render wrongly, changing how the equations read.**
- M̄ renders as **Ḿ** (acute accent) in Section 2.2 ("$(\bar M_l,\bar M_r)$"), Eq. (7), and the Section 2.5 inline M̄_main. C̄ renders as **Ć** in the denominator of Eq. (12) (PDF p. 9). The DOCX uses `m:chr = "‾"` (U+203E) as the accent character, which LibreOffice draws as an acute accent.
- Brackets do not match. Eq. (13) shows "$\frac1\alpha[\,C_\infty + \dots\,)$" with an opening "[" and a closing ")" (PDF p. 10). Eq. (S2) shows "cos[1/3 arccos(2/5√6/5))". The DOCX has correct `[`/`]` delimiters, so this is a PDF-conversion defect.
- `\mathrm{Var}` and the subscripts tot, zs, crit, side, 2span render in italics.
Fix: emit `m:bar` or a combining overline (U+0305) for `\bar`. Re-check the PDF for `\Big[ … \Big]`. If the PDF is uploaded, regenerate it from Word rather than LibreOffice, or check every display equation by eye.

**S3. Section 2.5, paragraph before and after Eq. (13): θ6, θ7 are undefined in the main text.**
Quote: "($\theta_6 = -\theta_7$, a mirror-symmetric deformation)" … "stiffness against this pattern of pier rotation ($\theta_6=-\theta_7$)".
Why: the subscripts are the Mây Bridge pier labels T6/T7. In a general theory section they appear before Section 5, and the main text never names T6 at all: Section 5.1 names only "T7", "T5 and T8". Only Table S1 defines T6.
Fix: write "the two inner-pier rotations θ_B = −θ_C" (or θ_1 = −θ_2), or define the piers at first use. Keep T6/T7 only in Section 5 and in the S8 text.

**S4. Eqs. (10)–(12) and Supplementary S4: δ0 has two meanings.**
Eq. (10) treats δ0 as a deterministic residual offset that produces a bias b. Eqs. (11)–(12) and S4 ("variance $\sigma^2_{P,\mathrm{noise}} + P_\delta^2$") treat δ0 as the standard deviation of a zero-mean random offset, with δ0²L_tot² entering Σ. The claim "unbiased for every axle configuration if and only if $a^\top C=1$" holds only if the offsets $\delta_{0,j}$ have zero mean; otherwise the estimator carries the bias $a^\top\delta_0L_\mathrm{tot}$. Table S1 gives only "residual zero offset".
Fix: after Eq. (11), state that the offsets are modeled as zero-mean random variables with standard deviation δ0 and correlation ρ, and that Eq. (10) is the bias for one realization (or the rms bias). Update the Table S1 entry to match.

**S5. Table S2 and Fig. 2a: the "optimal side-span position ξ*" is the maximizer of the positive N_w, not of |N_w|, so it is not optimal for β ≳ 1.64.**
Table S2, row β = 1.7: ξ* = 0.2608 with N_w = 0.2202. But N_w = −0.435 at ξ = 0.812 in the same span. The cubic 8ξ³ − (12 − 3μ)ξ² + (2 − μ) = 0 has that second root, and the paper's own placement rule (Section 2.4, extremes of C including the negative one) ranks it first. The switch occurs at β ≈ 1.64; at β = 1.636 it is almost a tie (0.3316 against −0.3214). The dashed "optimum ξ*(β)" in Fig. 2a runs to β ≈ 2.4 on the positive branch.
Fix: define ξ* as "position of the largest positive constant", or give the |N_w| maximizer and its value. Footnote the β = 1.7 row, and stop the dashed curve, or switch branch, at β ≈ 1.64.

## Minor

**M1. Section 2.4, paragraph after Eq. (11): "A non-uniform weighting function along one record cannot do better".** Supplementary S3 states that when the influence line is known, other invariant weighting functions *do* better, with white-noise variance lower by 1.5–6.6. The qualifier "for every structure" carries the claim. Suggest: "cannot do better without knowledge of the influence line".

**M2. Symbols used but defined nowhere** (the main text says "full list: Supplementary Table S1"):
- A⁻ (Eq. (9)); C̄ (Eq. (12), the mean of the C_j).
- x, the first-axle position in Eq. (1); n, the number of axles (Eq. (1)), which clashes with the noise n_j (Section 2.4).
- ν (S2); ξ0, ξ*, μ_crit, F(ξ, μ), Φ (S3).
- N_ε (Fig. 6c); L_v; d_max; q0 (appears only inside other entries); c_m and EI_m (Eq. (3)).
Add them to Table S1, or drop "full list".

**M3. Section 2.2, last sentence: "$N_F = 2F_A/(q_0L_1)$".** L1 is two-span notation, but the identity is also used for three spans (Table 1; S8 "N_F = ξ0 = 0.47–0.61"). Write "with L the end span (L1 or L_side)".

**M4. Section 2.4: "with white noise n_j".** n_j is the *integral* of the white noise, with variance σ²ΔxL_tot. Write "with $n_j$ the integrated white noise".

**M5. Section 2.4: C is used both as a scalar and as the vector (C_j) in Eq. (11)**, and C(x) also denotes a function of position. Define the vector at first use.

**M6. Eq. (5) and S3: the same function is called F(ξ, μ) in the main text and Φ in S3**, and F also names the end reaction F_A. Consider one name.

**M7. Code comments cite equation numbers of earlier manuscripts, so they do not match the ASE equations:**
- `code/theory2/gc_theory.py` l. 26: μ "(Eq. (8))"; in ASE, Eq. (8) is N_w.
- `code/theory2/ident_theory.py` l. 18: "Eq. 4 / Eq. 8"; `ident_core.Model.Cm`: "(Eq. 3)".
- `code/supplementary/s04_monte_carlo.py`: "Eq. (16)", "Eq. (20)"; `s05_moving_force.py`: "Eq. (21)"; `s01_symbolic_two_span.py`: "Eq. (15)", "Eq. (6)/(7)" for the blind roots. The manuscript has only 14 equations.
- `code/v3/v3_numbers.py`: "Eq. (19) of v3" for Eq. (10).
- `code/theory2/multisensor_core.py`: "manuscript Section 4.2", "Table 8".
`code/supplementary/ASE_numbering.md` maps figures, tables and sections but not equations.
Also, `ident_theory.py` names M̄_main "nu" while S2 uses ν = 1.5 M̄_main, and the code calls the θ6 = −θ7 pattern "antisymmetric" where the paper says "mirror-symmetric deformation".
Add an equation map to `ASE_numbering.md`, or update the comments. Also remove the "[NEED VALUE]" placeholder for SIG_ROT in `code/theory2/ident_fisher.py` and its log; the paper states 3 % as an assumption.

**M8. Section 2.2, after Eq. (5): "Its left-hand side is the deflection indicator $N_w$, defined in Eq. (8)"** is a forward reference. Eq. (5) uses the span rigidity EI, while Eq. (8) uses EI_ref. Add "(with $EI_\mathrm{ref}$ the rigidity of the instrumented span)".

## Verified correct (no finding)

- Eqs. (1)–(14), (S1), (S2): signs, dimensions and algebra.
- Table 1 (all numeric entries), Tables S2 and S3, the S2 polynomials, and S3 (Φ, N_θ, N_V, strain-zero quadratic).
- R values in Section 2.3; indicator values in Section 2.5.
- Table 3 rows for the prismatic beam and calibrations A and B; the Möbius constants (14.0, 0.59, k_g = 4.36 × 10⁷, κ/k_g = 0.63, B_m = 0.51/0.12).
- Euler identity; Fisher determinant; CRB values; Eq. (12) numbers (24.8 %, 10.6 %, 22.5 %).
- Lab constant 61.54 mm²/N (I = 16 530 mm⁴); BPM/SLM ratio 1.0049; Table S17; error-budget exponents (4 for deflection, 2 for strain); S4 ratios.
- Agreement of Eqs. (4), (5), (7), (11), (12), (13), (14), S3 and M̄_main with `gc_theory.py`, `ident_theory.py`, `ident_core.py` and `multisensor_core.py` (the noise term uses Δx(L − Δx/2) instead of ΔxL, which is negligible).
- Every in-text equation reference in the Markdown points to the right equation.
- Main-text equation tags (1)–(14) are sequential in the PDF.

## Count

- Blocking: 2 (B1, B2)
- Should-fix: 5 (S1–S5)
- Minor: 8 (M1–M8)
