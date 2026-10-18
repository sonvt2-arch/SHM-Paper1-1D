# Blind readability review — manuscript v4

Reviewer brief: readability only. One file read (`manuscript/v4/manuscript.md`), two passes (one straight read-through, then a slow pass sentence by sentence). [NEED VALUE] placeholders and the missing figures were ignored. Scientific merit and numerical correctness were not assessed.

---

## 1. Scores

| # | Criterion | Score | Main reason |
|---|---|---|---|
| 1 | Abstract clarity | 6.0 | The opening four sentences are excellent, but the second half packs three field findings into long sentences that use terms the abstract never defines ("restraint", "crossing residuals", "invariance ... within margins of 10–27 %"). |
| 2 | Introduction flow and motivation | 7.3 | The paragraphs move cleanly from safety to WIM, BWIM, integral methods and then the continuous-girder gap, and the novelty statement is honest; the second paragraph is a citation list that slows the reader before the actual gap appears. |
| 3 | Signposting and structure | 7.5 | Every section opens with a "this section..." statement and most subsections lead with their conclusion; the drawback is several forward references (Section 2.2 relies on indicators that Section 2.3 defines, and Section 2.4 cites field results from Section 4.3 and parameters from Section 5.3). |
| 4 | Sentence-level clarity | 6.5 | Sentences are mostly short and grammatical, but many depend on unstated links ("Two facts explain this", "so GLS and the zero-sum estimator are both", "The data cannot tell whether ... cause it"). |
| 5 | Information density | 5.0 | Sections 4.2, 5.2–5.3 and 6 often put three or four numbers with CIs in one sentence, near-duplicate figures (6.6 vs 6.5, 24.8 % vs 22.5 %) compete for attention, and Appendix A is a single wall of closed forms. |
| 6 | Terminology and notation | 5.5 | The Nomenclature helps, but symbols are overloaded (c, a, h, L/l), the span names change from sentence to sentence (centre span, main span, mid main span), the abstract lists four channel types where the paper lists five, and one estimator carries three names. |
| 7 | Equations in prose | 7.0 | Equations are introduced and followed up properly and every symbol is explained near its use; Eq. (5) is presented before the indicator it equals, and Appendix B/C compress derivations into long inline formulas. |
| 8 | Results presentation (tables included) | 6.0 | Tables 1–3 and 6 are clear; Table 4 needs two footnotes and a normalisation caveat to read, Table 8's "Value" column is a set of telegraphic fragments, and the field results (Section 4.2) describe CI-based equivalence tests in prose that is hard to follow. |
| 9 | Conclusions | 7.0 | They are numbered, specific and quantitative; item 3 mixes a theoretical placement result with a field failure, and items 4–5 repeat CI-level detail better left in the body. |

**Overall: 6.4 / 10.**

Weighting: I weighted sentence-level clarity, information density and terminology most heavily (about 20 % each), because they determine the friction a specialist meets on every page. Results presentation and the abstract come next (about 12 % each), and the remaining criteria share the rest. The paper has a sound skeleton: the section openers, the numbered contribution list, the workflow in Section 7 and the conclusions all help a reader find their way. Close reading, though, is slowed by density and notation. From Section 4 on, nearly every sentence carries a number, a CI or a calibration label. Several quantities are near-twins (factor 6.6 vs 6.5; indicator vs constant vs ratio of constant to deflection), and terms such as "restraint", "in-line", "step" or "crossing residual" are used before they are explained, or never explained. A specialist will get through it, but will have to re-read often, which places the paper below the 8 that marks a well-edited paper in a good journal.

---

## 2. Places re-read on the first pass

- **Title.** A 30-word title with two "and"s and a comma clause. I had to parse it twice to see that it covers three contributions.
- **Abstract, sentence 5:** "the area under a record equals the load times the channel's response to a uniform unit load, the integral constant." On first reading "the integral constant" seems to name the load, not the response.
- **Abstract:** "A cancellation ratio separates cancellation from restraint." "Restraint" has not been introduced, so the sentence gives no information at this point.
- **Abstract:** "invariance of the constant could be shown only within margins of 10–27 %". It was unclear whether this is a positive or a negative result.
- **Abstract:** "because crossing residuals are much less correlated between gauges than vehicle-free noise". "Crossing residuals" is undefined in the abstract.
- **§1, contribution 4:** "in which the constant depends on pier stiffness only through the scaled pier stiffness κ = k/α and a linear-fractional (Möbius) law, and which names the measurement that resolves it". Two relative clauses, the second with an unclear antecedent ("it" = the indicator? κ?).
- **§2.2, after Eq. (5):** "The left-hand side of Eq. (5) is the deflection indicator of Section 2.3, Eq. (10)". This is a forward reference to a quantity not yet defined.
- **§2.2:** "The side-span blind locus ends at β = 2cos(π/9) = 1.8794, where the end rotation under the uniform load vanishes." It is not explained why a vanishing end rotation ends the deflection locus.
- **§2.2:** "A channel is called near-blind when its indicator (Section 2.3) is below 0.2". This is another forward reference, and the threshold is used before its meaning is explained (8 % vs 20 %, §2.3).
- **§2.2:** "For two equal spans the band lies 0.19–0.32 of the span from the interior support". Table 1 gives the same band as 0.676 < ξ < 0.812 measured from the other end. I had to convert to check that they agree.
- **§2.2:** "Strain blind points exist in every span that has a sagging zone (μ<4)". The condition μ < 4 applies to the end span only, not to "every span".
- **§2.4:** "For one channel, Eq. (13) returns P̂ = J/C with variance σ²_{P,noise} + P_δ²". The symbol σ_{P,noise} appears nowhere else.
- **§2.4, paragraph on g(x):** It moves from invariance to transmissibility to time-versus-space integration in four sentences.
- **§2.4:** "This price is small, because for the long-span parameters of Section 5.3 with Δx = 0.1 m the white-noise term ... is only about 5 × 10⁻⁶ of the offset term." This relies on parameters given three sections later.
- **§3:** "The SLM deviations of 0.61 % and 0.70 % match the growth of this ratio relative to its one-load value of 1.010. The data cannot tell whether support seating or errors in the stated masses cause it." The antecedent of "it" is unclear.
- **§4.1:** "Day 2 has four in-line channels" and later "two in-line two-truck runs". "In-line" means two different things and is defined for neither.
- **§4.2, first paragraph:** "The constant is stable within the noise for most gauges, but invariance between trucks can be shown only within margins of 10–27 %." This is followed by "eight of the twelve gauges scatter as much as the measured noise predicts". The link between scatter and invariance is not made explicit.
- **§4.2:** "0.98 (95 % CI 0.70–1.37) ... cannot exclude differences of up to about 27 %". The reader cannot see at once how 27 % follows from this CI.
- **§4.2:** "so gauge-factor spread is an unlikely cause". The logic (a lane-dependent ratio rules out a constant gain error) is left for the reader to supply.
- **§4.3:** "The paired difference is +8.5 points (95 % CI +2.3 to +15.1), so GLS and the zero-sum estimator are both significantly worse". The paired difference shown applies to GLS only.
- **§4.3:** "As anticipated in Section 2.4". Section 2.4 already reported this field result, so the reasoning appears circular.
- **§5.1:** "Each gauge has six readings (three lines, each centric and eccentric)". "Lines" (load lines? transverse truck rows?) is undefined.
- **§5.2, first paragraph:** "Two facts explain this: a model-form misfit that no pier stiffness removes, and the Möbius law". On first reading it is not obvious how a misfit explains a factor of 6.6.
- **§5.2:** "its α = 0.716 would mean a 28 % loss of rigidity in a young prestressed girder". The implied judgement (implausible) is not stated.
- **§5.2, Table 4 and footnotes.** I read this three times to see why calibration B lies above the fixed-pier value.
- **§5.2:** "the ratio of C_m to the modelled N8 deflection varies by a factor of 6.5". This is easily confused with the factor of 6.6 two paragraphs earlier, and the purpose of the ratio is not stated.
- **§5.2:** "would narrow the admissible set further if they belonged to the third vertical mode". This is cryptic without the Supplementary Material.
- **§5.3:** "The pair at 100 m and 152 m from the end support T5". I had to compute that these points are mid main span and 7 m into the far side span.
- **§5.3:** "for the 200 m record used in Section 6 the single-gauge value is 22.5 %". This is a second number for the same quantity in the same sentence.
- **§5.3, Cramér–Rao paragraphs.** The bound "0.87" is given without saying what a bound of 0.87 on SD(ln C₈) means physically (about a factor of 2.4).
- **Table 6, row 3:** "Strain integral at the zero-moment point of A (171.3 m) / at gauge N7". N7 is a deflection gauge, so it is unclear what strain "at gauge N7" means.
- **§6:** "post-minus-pre level differences". This is jargon.
- **Table 8:** "laboratory step 1.010 → 1.017" and §6 "the load-dependent step". "Step" was never introduced in §3.
- **Table 8:** "field per-crossing SD of the gauge average predicted 19.8 % (day 2)". It is unclear what predicted this, and why the value differs from Table 3.
- **§6:** "the weight errors of single crossings, 5–12 % on these records". The source of this range is not stated (Table 3 gauge-average LOO MAE?).

---

## 3. The 10 hardest-to-read passages

1. **Abstract:** "On public moving-truck records from a five-span box girder, invariance of the constant could be shown only within margins of 10–27 %, and the narrow range of reference weights did not allow weight discrimination to be tested. Generalised least-squares weights estimated from vehicle-free noise performed worse out of sample than the gauge average, because crossing residuals are much less correlated between gauges than vehicle-free noise."
   - *Why hard:* Two long sentences with three findings, a passive "could be shown only", and two undefined terms ("crossing residuals", "out of sample").
   - *Fix:* "On public moving-truck records from a five-span box girder, the constant was the same for different trucks to within the 10–27 % that the data could resolve; the reference weights varied too little to test weight discrimination. Combining gauges by generalised least squares did not help: the per-crossing errors of different gauges were far less correlated than the vehicle-free noise from which the weights were estimated."

2. **§1, contribution 4:** "an identifiability analysis of the indicator under boundary uncertainty, in which the constant depends on pier stiffness only through the scaled pier stiffness κ = k/α and a linear-fractional (Möbius) law, and which names the measurement that resolves it;"
   - *Why hard:* Two stacked relative clauses, the second with an ambiguous antecedent; "only through ... and a ... law" mixes a variable and a functional form.
   - *Fix:* "an identifiability analysis under uncertain pier stiffness: the constant follows a linear-fractional (Möbius) law in the scaled pier stiffness κ = k/α, and one additional measurement is identified that fixes κ;"

3. **§2.2:** "The left-hand side of Eq. (5) is the deflection indicator of Section 2.3, Eq. (10), with EI_ref = EI. Setting F = 0 gives the deflection blind condition, which depends on μ alone:"
   - *Why hard:* The reader must jump forward to a definition not yet made, and Eq. (5) uses "8F" while the indicator is later called N_w = 8Φ (Appendix B), which is a third symbol.
   - *Fix:* Move the definitions of N_w and N_M (current §2.3, first two paragraphs) to the start of §2.2, then write Eq. (5) directly as "N_w = 8F(ξ, μ)". Use one symbol (F or Φ) throughout.

4. **§2.4:** "Could a non-uniform weighting function g(x) along a single record do better than the plain integral? Appendix B shows that it cannot: only a uniform g keeps the estimate independent of the axle configuration for every structure, and SLM relies on this invariance. It also links SLM to transmissibility-based weighing [34]: a transmissibility is a ratio of response spectra, and at zero frequency it equals the ratio of record integrals. A record integrated uniformly in time weights space by 1/v(x), so the integral must be taken in space."
   - *Why hard:* Three unrelated points in one paragraph; "It also links" has no clear subject (Appendix B? the invariance?).
   - *Fix:* Split into three short statements: (i) the uniform-g result; (ii) a separate sentence in §1 or §2.1 linking SLM to transmissibility ("At zero frequency a transmissibility reduces to the ratio of record integrals, so SLM is its static limit"); (iii) move the space-versus-time remark to §2.1, next to "At constant speed v the time integral is J_m/v".

5. **§3:** "Second, the ratio of the measured to the analytical integral, both from the trapezoidal rule, grows with the number of loads: 1.010, 1.016 and 1.017 for one, two and three loads. The SLM deviations of 0.61 % and 0.70 % match the growth of this ratio relative to its one-load value of 1.010. The data cannot tell whether support seating or errors in the stated masses cause it."
   - *Why hard:* The reader must work out 1.016/1.010 ≈ 1.006 to see the "match"; "it" is ambiguous.
   - *Fix:* "...grows with the number of loads, from 1.010 (one load) to 1.016 and 1.017 (two and three). Relative to the one-load value, this is a growth of 0.6 % and 0.7 %, which equals the SLM deviations in Table 2. Whether support seating or errors in the stated masses cause this growth cannot be decided from the data."

6. **§4.2:** "The constant is stable within the noise for most gauges, but invariance between trucks can be shown only within margins of 10–27 %. On day 1, eight of the twelve gauges scatter as much as the measured noise predicts, and one gauge, ch11, gives the same constant for both trucks within ±10 % (Fig. 6a)."
   - *Why hard:* "Stable within the noise", "invariance ... shown only within margins" and "equivalent within ±10 %" are three different statistical statements (χ² consistency, CI width, TOST equivalence) presented as if they were one.
   - *Fix:* State the test before its outcome: "Two questions were asked of each gauge: does its scatter exceed the measured noise (χ² test), and is the constant the same for both trucks within ±10 % (equivalence test)? On day 1, eight of twelve gauges pass the first test; only ch11 passes the second. The CIs are wide, so differences of 10–27 % cannot be excluded."

7. **§5.2:** "The static data leave the constant of the side-span gauge N8 uncertain by a factor of 6.6, whereas the constant of the centre-span gauge N7 is well determined. Two facts explain this: a model-form misfit that no pier stiffness removes, and the Möbius law of Eq. (15)."
   - *Why hard:* The causal chain (misfit → wide tolerance → κ bounded only from below → steep Möbius curve at N8 → large spread) is compressed into "two facts explain this".
   - *Fix:* "...is well determined. The reason has two parts. First, no pier stiffness makes the beam model fit both readings, so the tolerance must be wide, and at that tolerance the data bound κ only from below. Second, by the Möbius law of Eq. (15), the N8 constant is very sensitive to κ over this unbounded range, whereas the N7 constant is not."

8. **Table 4 and its footnotes:** "ᵃ Above the fixed-pier value because calibration B has α = 0.716; normalised by the effective rigidity αEI_mid it is 0.341. ᵇ The upper part of this range requires α ≈ 0.5; normalised by the effective rigidity, the range is 0.144–0.422."
   - *Why hard:* The table mixes two normalisations (design EI and effective EI), so rows cannot be compared without reading the footnotes; the caption sentence "the pinned-pier and fixed-pier rows give the extreme values over all model-form variants" also conflicts with the α = 1 statement.
   - *Fix:* Add a second column group "normalised by αEI_mid", or report the absolute constant C (m²/kN) as in Table 7, and drop the footnotes.

9. **§5.3, Cramér–Rao paragraphs:** "Its benefit is measured by the Cramér–Rao bound on the standard deviation of ln C₈. The bound is evaluated at the scaled pier stiffness of calibration A, κ = 2.75×10⁷ kN m/rad, with α refitted to the two readings at that κ (α* = 1.07; the curve α*(κ) of best static fit is shown in Fig. 9b). ... At calibration A the two deflections alone give a bound of 0.87. ... At calibration B the two-reading Fisher matrix is singular, so the deflections alone cannot bound ln C₈, and with the tiltmeter the bound is 0.04."
   - *Why hard:* A long parenthesis, a refitted α, and bounds on a logarithm given without a physical meaning.
   - *Fix:* Say what the number means: "a bound of 0.87 on SD(ln C₈) means the constant is known only to within a factor of about 2.4 (one SD); the tiltmeter tightens this to about ±20 %." Move α* and Fig. 9b to a footnote or to Appendix C.

10. **Table 8, rows "Residual offset" and "Linearity, seating":** "Table 7; field per-crossing SD of the gauge average predicted 19.8 % (day 2), 5.3 % (day 1)" / "laboratory step 1.010 → 1.017".
    - *Why hard:* These are telegraphic fragments with undefined terms ("predicted" by what? "step"?), and 5.3 % repeats the day-1 MAE of Table 3 and the τ of §5.2, so the same number has three meanings.
    - *Fix:* Write full short phrases: "SD per crossing predicted from vehicle-free noise: 19.8 % (day 2), 5.3 % (day 1)"; "measured/analytical integral ratio rose from 1.010 (one load) to 1.017 (three loads)".

---

## 4. Spelling and grammar errors (confident)

- §5.2 Appendix C, l. 538: "that is at calibration B" should read "that is, at calibration B" (missing comma after "that is").
- §3: "a steel hollow square tube" should read "a square hollow steel tube" (conventional adjective order; "square hollow section" is the standard term).
- §2.1: "a linear-elastic structure ... any linear elastic supports". The compound adjective should be hyphenated consistently: "linear-elastic supports".
- §1: "Optimal sensor placement for BWIM has been posed through an augmented Kalman filter [44], deflection-based load identification as a regularised stochastic problem [45,46], and measured deflection influence lines have been inverted..." The elliptical gapping with a change of verb ("has been posed" ... "have been inverted") is ungrammatical as a list. Rewrite as three clauses with their own verbs.
- §2.4: "For one channel, Eq. (13) returns P̂ = J/C with variance σ²_{P,noise} + P_δ²". An undefined symbol is used in running text. This is not a spelling error, but it is an error.
- Spelling consistency: British spelling throughout ("normalise", "generalised", "colours", "labelled"), but the heading reads "Acknowledgments" (American). Use "Acknowledgements" for consistency. The CRediT role names ("Conceptualization") are a fixed taxonomy and may stay as they are.
- Abstract: "the load times the channel's response to a uniform unit load, the integral constant". The appositive attaches to the wrong noun. Use "...equals the load times the integral constant, the channel's response to a uniform unit load."
- §4.3: "so GLS and the zero-sum estimator are both significantly worse than the average". The preceding statistic is for GLS only, so either give the zero-sum difference or write "GLS, and similarly the zero-sum estimator, is significantly worse".
- Ref. [34] title reads "bridge weight-in-motion". Please check against the source; if this is not the original wording, it should be "weigh-in-motion".

---

## 5. Non-standard or inconsistent terms and notation

- **Number of channel types.** The abstract says "four channel types (deflection, strain, rotation, reaction)", while contribution 1 and Table 1 list five (adding shear) and also interior reactions.
- **Span names.** "centre span", "centre-span gauge", "main span", "mid main span", "mid-span" and "C" (subscript c "= centre or main span") are used interchangeably. Choose "main span" throughout, since the subscript is already "c".
- **c.** It denotes the fibre distance (Eq. 3, c/EI) and is also the subscript for the main span (L_c, EI_c). In "cM_q/EI" next to "EI_c" this is confusing; use e.g. y_f or z for the fibre distance.
- **a.** It denotes the channel-weight vector (Eq. 13), the axle offsets a_i (Eq. 1), and the axle index in Appendix B (Σ_a P_a h(s_a)).
- **h.** It denotes the section depth (§5.1, c ∝ h, h^2.943) and the function h(s) in Appendix B. Neither is in the Nomenclature.
- **L / l / L_1 / L_s.** "L" is the span containing the sensor and "l" the laboratory span. The lowercase l is an avoidable extra symbol, since L would do in §3.
- **The indicator function.** F(ξ, μ) (Eq. 5), Φ (Appendix B) and 8F = N_w are three symbols for one function.
- **Missing from the Nomenclature:** ν, Φ, h, L_v, α*, S_{y8}, S_{y7}, e_m, G, q, θ_{m,i}, σ_{P,noise}, ζ_0, ξ_0, ξ*, χ².
- **Order in the Nomenclature.** "N_w, N_M — Eqs. (10) and (9)" lists the equations in reverse order of the symbols, which reads as a mismatch.
- **"The constant" / "integral constant" / C / C_m / C₈ / C_7.** The subscript switches from the location m to the gauge number (8, 7) without a note. Add "C₇, C₈: constants of gauges N7, N8" to the Nomenclature.
- **The zero-sum estimator.** It is called "zero-sum estimator" in the text, "offset-immune" in Fig. 4 and "immune-eq" in Fig. 7. Use one name.
- **"Mean weight" predictor.** It appears as "mean-weight predictor", "Mean weight of the calibration runs" (Table 3) and "mean-GVW" (Fig. 7).
- **"In-line".** It is used for four day-2 channels and for two-truck runs, with different meanings and no definition.
- **"Restraint" vs "cancellation".** This is central to the R ratio but never defined in words. Define it once: "restraint: a small net area because the positive lobe itself is small, as in a fixed-ended span".
- **"Step".** "laboratory step", "load-dependent step" (§6, Table 8) refers back to the ratio growth in §3, where the word "step" is never used.
- **"Lines".** "three lines, each centric and eccentric" (§5.1) is undefined.
- **Indicator thresholds.** "0.2" means 8 % for N_w and 20 % for N_M. The paper says so, but then uses "|N| < 0.2" (Fig. 3) as if the two thresholds were the same.
- **Units of κ.** It is given in kN m/rad while k̂ is dimensionless and κ/k_g is a ratio. Three stiffness scalings (k, k̂, κ, κ/k_g) for one physical quantity are a lot. Consider reporting only κ/k_g in §5.
- **Tolerance and its double.** τ = 5.3 % is described as "at two standard deviations", while Fig. 9 uses |ln r₈₇| ≤ 2τ. A reader may think the tolerance is doubled twice.
- **Day labels.** Day 1 uses the "ch" prefix, day 2 uses "st", and the trucks are not named (e.g. "T3a", "T5"). The text instead uses "the second truck", "the 5-axle truck", and "T5, T7, T8" are support names. Note the clash: "T5" is a support, while "5-axle truck" appears nearby.
- **Abbreviation choice.** "BPM" (beam-property method) is easily read as an unrelated common abbreviation. It is defined, but "model-based constant" might read more easily.

---

## 6. The single change that would most improve readability

**Reduce the numbers per sentence in Sections 4–6, and move the secondary numbers into the tables.** For each paragraph, keep one headline number in the text with its comparison (e.g. "GLS was worse than the plain average, 20.4 % vs 11.9 % MAE") and send every CI, secondary variant and near-duplicate value (24.8 % vs 22.5 %, 6.6 vs 6.5, Cramér–Rao bounds at both calibrations, normalised and design-normalised indicators) to a table or to the Supplementary Material. Each paragraph should state its point in plain words before giving the evidence. This change alone would remove most of the re-reads listed in Section 2, because almost all of them occur where three or more quantified claims share a sentence. Fixing the overloaded notation (c, a, h; one name for the zero-sum estimator; "main span" throughout) is the second most useful change, and it is cheap.
