# Blind readability review: manuscript v4 (reader 1)

This review covers readability only: prose, structure, terminology and presentation. It does not judge scientific merit or check whether equations and numbers are correct. [NEED VALUE] placeholders and missing figures were ignored.

Method: one straight read-through, marking every place I had to re-read, then a slow second pass sentence by sentence.

## Scores (0–10)

| # | Criterion | Score | Main reason |
|---|---|---|---|
| 1 | Abstract clarity | 6.0 | The main message (strain gauges are blind at zeros of the uniform-load moment; criteria come before installation) is recoverable. However, the abstract has 12 sentences and four separate results. It uses "the constant" and "the identity" without saying they are the integral constant and the influence-area identity, and "Indicators separate cancellation from restraint" means nothing on a first read. |
| 2 | Introduction flow and motivation | 7.5 | Clear arc from overload risk, through BWIM, to influence-area weighing and a sharp gap statement. Paragraphs 2–3 are citation catalogues with long compound subjects. "Used, not claimed" and "a corrected normalisation" (corrected relative to what?) are cryptic. |
| 3 | Signposting and structure | 7.5 | Every section opens with a purpose sentence, and Sections 4.5 and 5.3 close with "what this shows". The roadmap is clear. Weak spots: the purpose of 2.3 is implicit, and 4.4 mixes four topics (lane, superposition, gauge spread, why integrate the whole record). |
| 4 | Sentence-level clarity | 6.5 | Most sentences are short and declarative. A minority pack two or three clauses with semicolons and parentheses, and some use referents that are hard to resolve ("this step", "the order", "this ranking", "the choice"). |
| 5 | Information density | 4.5 | This is the main obstacle. Sections 2.2, 2.4, 4.2–4.3 and 5.2–5.3 carry 6–12 numbers or symbols per paragraph. Tables 3, 4, 5 and 7 are close to unreadable without the text. |
| 6 | Terminology and notation | 5.5 | Several symbols are overloaded (ρ, η, R, I, T, ρ_EI). Some terms are used before they are defined (SLM, BPM, zero-sum). The hyphenation of mid-span phrases varies. |
| 7 | Equations in prose | 7.5 | Equations have good lead-ins and usually an interpretation sentence (Eqs. 3, 12, 13, 15). Eqs. (14) and (16) come with less interpretation, and Eq. (8) has none. |
| 8 | Results presentation | 5.5 | The text states each conclusion first, which helps. But the tables are overloaded: Table 7 has 8 columns, with values in brackets and semicolons inside cells. Table 4 mixes predictions, in-sample and out-of-sample values in one column, and the text keeps sending the reader back to it. |
| 9 | Conclusions | 7.0 | Numbered, specific and mostly consistent with the text. Item 3 compares 0.63 against 0.92, while Section 4.3 makes the like-for-like comparison against 0.90. Item 4 ("inconclusive at better than 10–27 %") is awkward. Item 5 ("would identify the constant") is stronger than the Cramér–Rao bound of 0.18 reported in 5.3. |

**Overall: 6.0 / 10.** I weighted information density, sentence clarity and results presentation most heavily, because they set the reading effort for Sections 2–5, which make up the bulk of the paper. The good abstract-to-conclusion structure lifts the score only partly.

## Places re-read on the first pass

- Abstract, sentences 9–11: which "constant"? Why does vehicle-free noise matter?
- 1, paragraph 4: "So is the combination ..." (what is "so"?); zero-sum appears before any definition.
- 2.2: "0.75L" given for ξ₀ (a fraction); the switch from m_l and m_r to μ.
- 2.3: the paragraph on thresholds of 8 % against 20 %.
- 2.4: "Within one channel, the uniform weight is the only weight ..."; the transmissibility aside; "for each channel type".
- 2.5: κ given units of kN m/rad although it is called a ratio.
- 3: the sentence about the order of the three-load group; "exactly this step".
- 4.3: the Table 4 rows on predicted sd; "which reverses the order".
- 4.4: "Gauge-factor spread is an unlikely cause" (cause of what?).
- 5.2: locating calibration B on the κ axis (the reader must compute k/α).
- 5.3: calibration A first has α = 1 (5.1), then "α* = 1.07" (5.3).
- 5.2: "a factor C∞/C0 of 14.0 at N8 but only 0.59 at N7".
- After Table 7: "Calibration B's N8 value lies outside the bound column ...".
- 6: "the relative errors of the rigidity, of four times the span length"; "For a constant force crossing the laboratory beam".
- 6: "The lower offsets are of displacement-transducer class."

## The 10 hardest-to-read passages

1. **Section 2.4:** "Within one channel, the uniform weight is the only weight that keeps the integral invariant for every structure (Appendix B), which is the property the standard-load method needs."
   - Why it is hard: "weight" here means a weighting function along the record, which collides with vehicle weight and with GLS weights. SLM has not been defined yet.
   - Fix: say "uniform weighting function along the record"; define SLM before this point.

2. **Section 5.2:** "With $k_g = 4.36\times10^7$ kN m/rad, pier fixity can change the constant by a factor $C_\infty/C_0$ of 14.0 at N8 but only 0.59 at N7."
   - Why it is hard: "only" with a factor below 1 reads as a smaller effect, yet 0.59 is a decrease. The direction of change is unclear.
   - Fix: "by 14.0 times (increase) at N8 and 0.59 times (decrease) at N7."

3. **Section 3:** "The order of the three-load group was not recorded independently and was chosen by fit (root-mean-square residual 0.030 mm against 0.55 mm for the reverse spacing), so that test is not fully independent."
   - Why it is hard: "order" and "reverse spacing" are undefined, and "independent" is used twice with two meanings.
   - Fix: say which loads were where; split into two sentences.

4. **Section 3:** "The SLM residuals of 0.61 % and 0.70 % are exactly this step, which the data cannot attribute to support seating or to errors in the stated masses."
   - Why it is hard: "this step" refers back to a ratio sequence two sentences earlier.
   - Fix: "equal the increase of the ratio from 1.010 to 1.016/1.017."

5. **Section 4.3:** "With the covariance of the crossing residuals themselves, GLS is predicted to be worse than the average, which reverses the order."
   - Why it is hard: "the order" is unclear (which order, predicted by what?).
   - Fix: "...reversing the order predicted from vehicle-free noise (Table 5)."

6. **Section 2.3:** "expressed as a fraction of the simply supported mid-span value, they are 8 % for deflection and 20 % for strain. Both are design conventions; the bands quoted ... use them as stated."
   - Why it is hard: two thresholds and two normalisations, plus a disclaimer, packed into one sentence.
   - Fix: put the thresholds in a small table, or use one threshold per normalised scale.

7. **After Table 7 (Section 5.2):** "Calibration B's N8 value lies outside the bound column because the bound uses design $EI$ (Table 7)."
   - Why it is hard: the reader must cross-match three columns of Table 7 to see the point.
   - Fix: move this to a table footnote, or delete it.

8. **Section 6:** "the relative error of BPM is the sum of the relative errors of the rigidity, of four times the span length, of the gain, of the speed and of the offset term of Eq. (12)."
   - Why it is hard: "four times the span length" reads as a length, not as a sensitivity factor.
   - Fix: "...rigidity, four times that of span length, ..."

9. **Section 5.3:** "The choice therefore depends on whether the noise is set by the strain resolution or by the offset."
   - Why it is hard: it does not say which location wins in which case.
   - Fix: "near-pier if resolution-limited; mid-span if offset-limited" (or whichever is correct).

10. **Section 5.3:** "evaluated at calibration A ($\kappa = 2.75\times10^7$ kN m/rad, $\alpha^* = 1.07$) with 2.64 % per static reading and an assumed 3 % for the rotation."
    - Why it is hard: α = 1 for calibration A in 5.1 conflicts with α* = 1.07 here. "2.64 % per static reading" lacks a noun (standard deviation?).
    - Fix: explain α* as the best-fit α at this κ; add "standard uncertainty".

Further near-misses:
- 4.4: "Gauge-factor spread is an unlikely cause" (the antecedent is in the previous paragraph).
- 6: "The lower offsets are of displacement-transducer class."
- 1: "The identity and the GLS estimator are used, not claimed."

## Spelling and grammar errors I am confident about

- Section 5.3: "with 2.64 % per static reading". A noun is missing ("a standard uncertainty of 2.64 %").
- Section 2.2: "The strain blind point $\xi_0$ ... is $0.75L$". ξ₀ is a fraction, so "0.75L" mixes a fraction and a length; it should be 0.75 (or "at 0.75L").
- Section 6: "For a constant force crossing the laboratory beam". Needs a hyphen: "constant-force crossing" or "a constant force crossing ...". As written it parses as "a constant (force crossing)".
- Spelling convention: British spelling is used throughout (generalised, normalise, Colours), but "Acknowledgments" is American. Use "Acknowledgements", or make the whole paper consistent.
- Reference [34]: "bridge weight-in-motion". This is probably a typo for "weigh-in-motion"; check it against the original title.
- Conclusions item 4: "the tests were inconclusive at better than 10–27 %". Unidiomatic; use "could not resolve differences smaller than 10–27 %".

## Non-standard or inconsistent terms and notation

- **ρ** is used for three things: ρ (common-mode fraction), ρ_L (span ratio) and ρ_EI. In addition, ρ_EI is defined differently for two and three spans (Nomenclature and Section 2.2).
- **η** is both the influence line η_m and the main-span position η₀, η = x/L_m (2.2, Appendix A).
- **R** is the cancellation ratio, while R_A is a reaction and N_R the end-reaction indicator (2.2, 2.3).
- **I** is the record integral I_r, the second moment of area I (Section 3, Section 4.4, "I ∝ h²") and the identity matrix ("Σ = I", Table 5).
- **T** is T₁ (period) and T_cr (duration), and also T5, T7, T8 (supports).
- **κ** is called a "pier-to-girder stiffness ratio" but given units of kN m/rad (Nomenclature, 2.5, 5.2).
- **ε₀** is given units of mm (Nomenclature) but is also used as a strain offset (2.3, "A residual offset ε₀ ... the integral").
- **μ** has two names: "interior-moment parameter" (Nomenclature, Section 2.2) and "hogging parameter" (m, 2.2).
- **Terms used before definition:**
  - "standard-load method" in 2.4 (defined in Section 3).
  - "BPM" in the Table 2 header (defined in the sentence after the table).
  - "zero-sum variant" in Section 1 (defined in 2.4).
  - "uniform-load criterion" in the Table 1 caption (never defined).
- **Hyphenation varies** across "mid-span", "mid main span", "mid main-span indicator", "mid side span", "mid side-span sensor", "centre-span gauge" and "mid-span of span 2".
- **The same concept has several names:**
  - "constant", "integral constant", "C", "absolute constant".
  - "admissible set" and "static admissible set".
  - "reference stiffness" and "reference rigidity".
  - "pier stiffness", "rotational stiffness" and "pier fixity".
  - "gain" and "section gain".
  - "calibrations A and B" and "reference calibrations".
- **Undefined abbreviations:** "sd" (Tables 4, 5, 10) and "r²" (4.4) are not in the Nomenclature, while CV is.
- **Two names for one estimator:** "Offset-immune" and "zero-sum" are both used (2.4, 4.3, Section 7 item 6, Fig. 7 "immune-eq").
- **"Equivalence"** is used in two senses: TOST equivalence (Table 3) and the non-equivalent thresholds (2.3).

## Single change that would most improve readability

Cut the numerical density of Sections 2.2–2.4, 4.2–4.3 and 5.2–5.3. Keep one or two headline numbers per paragraph in the text, move the remaining ranges and intervals to the tables (or the Supplementary Material), and split Tables 4 and 7 so that each has one kind of quantity per column.
