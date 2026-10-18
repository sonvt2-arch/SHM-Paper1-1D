# Blind readability review: manuscript v4 (reviewer 2)

Scope: readability only. I read only `manuscript/v4/manuscript.md`. I ignored the [NEED VALUE] placeholders and the missing figures, and I did not judge scientific merit or check equations and numbers. Method: one straight read-through, marking every place I had to re-read, then a slow second pass sentence by sentence.

---

## 1. Scores

| # | Criterion | Score | Main reason |
|---|---|---|---|
| 1 | Abstract clarity | 5.5 | It packs about nine separate claims into 230 words. One sentence lists three unrelated results in parallel clauses, and the field result is attributed to the wrong cause ("only coarsely, because the reference weights hardly vary"). |
| 2 | Introduction flow and motivation | 7.0 | The motivation leads cleanly to the gap and the numbered contributions, but paragraphs 2 and 3 are catalogues of citations with little synthesis. |
| 3 | Signposting and structure | 7.0 | Every section opens with a purpose sentence and Section 4.5 summarises well. However, the in-service bridge (Cầu Mây) and its numbers turn up in Section 2 before it is introduced, Fig. 9 is cited before Fig. 8, and Section 2.4 depends on parameters from Section 5.3. |
| 4 | Sentence-level clarity | 6.0 | Sentences are short and grammatical, but many are compressed to the point of being cryptic ("Σ never contained a crossing", "consistent with superposition but low"), and several "therefore" links do not follow from the sentence before. |
| 5 | Information density | 4.5 | Almost every sentence in Sections 4 and 5 carries one or more numbers, ranges or CIs. Section 5 spreads overlapping quantities over Tables 8–10, so the reader cannot tell which numbers matter. |
| 6 | Terminology and notation | 5.0 | Heavy symbol overloading: $m$, $L$, $w$, $K$, $r$, $\varepsilon_0$ and "indicator" each carry two or more meanings, and several concepts go by two or three names (zero-sum / offset-immune / immune-eq; crossing residuals / crossing errors). |
| 7 | Equations in prose | 6.0 | Equations are introduced in sentences and numbered, but symbols are often defined after the equation (Eq. 4, Eq. 15) or never ($\sigma$, $\sigma_{P,\mathrm{noise}}$, $\nu$), and Eq. (5) uses the normalisation of Eq. (10) before it is defined. |
| 8 | Results presentation (tables included) | 5.5 | Tables 2, 6 and 11 are clear. Tables 8–10 are hard: they repeat ranges in slightly different forms (0.12–0.82 against 0.124–0.822), use two normalisations side by side and contain many "not computed" cells. A value in Table 9 is explained only after Table 10. |
| 9 | Conclusions | 6.5 | They are numbered, specific and honest about limits, but they are dense with numbers, and item 3 mixes a theoretical rule with a contradicting field finding. |

**Overall: 5.8 / 10.**

How I weighted the scores: sentence clarity (4), density (5), terminology (6) and results presentation (8) count most, because they set the reading cost of every page. The abstract and the conclusions count next, because most readers stop there. Introduction and signposting count least, because the paper is reasonably well organised at section level. The writing is careful and the English is almost free of errors. The friction comes from compression: the paper tries to carry a theory paper, a laboratory note, a statistical re-analysis of a public dataset and a case study at once, and it does this by stripping out explanation instead of material. A specialist can follow Sections 1–3 with moderate effort. Sections 4.2–4.3 and 5.2–5.3 need repeated re-reading, with frequent jumps to the Nomenclature and to tables. This is below the "well-edited, good journal" level of 8. The main gap is density and notation, not language.

---

## 2. Places re-read on the first pass

- **Title.** At 27 words with three subordinate parts, I had to re-read it to find the main noun ("blind loci and design criteria").
- **Abstract**: "Two indicators tell whether a small constant reflects cancellation or restraint, sensors belong at the extremes of the uniform-load response, and a closed-form law gives the effect of uncertain pier stiffness." Three unrelated results are joined as if they were a list. The indicators are not named, and the body later says that only $R$ makes this distinction.
- **Abstract**: "A static laboratory test on a two-span beam confirms the identity." The abstract has spoken of "two classical facts", not of one identity, so it is unclear which identity is meant.
- **Abstract**: "support invariance of the constant only coarsely, because the reference weights hardly vary". In Section 4.1 the narrow weight range limits *weight discrimination*, while the coarseness of the invariance test comes from noise and run count. I re-read to check whether I had misunderstood.
- **Abstract**: "because crossing errors are less correlated between gauges". The comparison is left unfinished (less correlated than what?), and the body says "crossing residuals".
- **Nomenclature**: $C_r$, $C_m$ and $m_l$, $m_r$. Here $m$ is both a position index and a dimensionless end moment, and the subscript $m$ also means "main span" in $L_m$ and $EI_m$.
- **Section 2.1**: "with $\eta_m = 0$ outside the loaded path $[0, L]$". Here $L$ is the path length, but the Nomenclature defines $L$ as the span containing the sensor.
- **Section 2.2, Eq. (4)**: $\lambda$, $\beta$, $\gamma$ are defined only after the equation.
- **Section 2.2, Eq. (5)**: the left-hand side $192EI\,C_m/L^4$ is the indicator $N_w$ of Eq. (10), which has not yet been introduced. The reader also has to wonder why "$=8F$" rather than simply $F$.
- **Section 2.2, Eq. (9)**: a general formula in $m_l$, $m_r$ is followed on the same line by $\xi_0 = 1-\mu/4$, which holds only for $(0,\mu)$.
- **Section 2.3**: "The common threshold of 0.2 therefore means different things for the two channels." The "therefore" depends on the reader having worked out that 0.2/2.5 = 8 %.
- **Section 2.4**: "Within a single record, the weighting function $g(x)$ along the record must be uniform. ... this is the property on which SLM relies." This is abrupt: $g(x)$ appears for the first time, and "this property" has no clear antecedent.
- **Section 2.4**: "for the parameters of Section 5.3 with $\Delta x = 0.1$ m". A forward reference to the case study in the middle of the theory.
- **Section 2.4**: "1/Var is a convex quadratic ... A convex function on a box attains its maximum at a vertex". Correct, but the reader has to supply what the "box" is (the range of feasible constants).
- **Section 2.5**, first paragraph: "For any assumed κ, two static readings therefore fix α, and they constrain κ only through the ratio of the two readings." I read it three times.
- **Section 2.5, Eq. (16)**: $K$ is a dimensionless pier stiffness here, but $K_g$ and $K_p$ are stiffness matrices two paragraphs earlier.
- **Section 2.5**: "For the Cầu Mây span ratio β = 1.636 ...". The bridge is not introduced until Section 5.1.
- **Section 3**: "The SLM deviations of 0.61 % and 0.70 % equal this growth from the one-load value." The reader must divide 1.016 by 1.010 to see what is meant.
- **Section 4.1**: "Four stations each carry two gauges: a wheel-path gauge ... and a partner gauge. The other four gauges show no axle spikes." It is unclear whether the partner gauges show spikes, or how 12 channels split up.
- **Section 4.2**: "All 23 channel and average rows are in the Supplementary Material." Twenty-three is not explained.
- **Section 4.2**: "This agrees with Eq. (2) ... The test therefore checks linearity and processing at a coarse level, not the identity itself." The two statements seem to contradict each other.
- **Table 4**: the "Equivalence" column for lane B reads "fails χ² (Table 3)". That is not an equivalence outcome.
- **Section 4.3**: "In each fold the constants were calibrated without the test run, and Σ never contained a crossing." This is cryptic.
- **Section 4.3**: "The zero-sum estimator therefore pays only for disturbances that are common-mode during crossings". "Pays" is unclear, and "therefore" does not follow from the over-fitting sentence before it.
- **Section 4.4**: "The two in-line two-truck runs are consistent with superposition but low." It is not said what is low.
- **Section 5.1**: "The mean of six readings is 5.55 mm at N8". Why there are six readings is explained only in Section 5.2.
- **Section 5.2**: "Adding a model-form spread of 1.75 % per gauge gives τ = 5.3 % at two standard deviations." The combination rule is not stated.
- **Table 8**: two N8-indicator columns, a "prior" row and footnote ᵃ. I needed several passes.
- **Table 9 against Table 10**: calibration B's N8 value, 0.476, exceeds the "fixed piers" bound, 0.446. The explanation comes in the prose after Table 10.
- **Section 5.3**: "a strain gauge at mid side span would be blind under calibration A ($N_M = 0.048$)". Strictly this is near-blind; the paper's own definitions of blind and near-blind are blurred here.
- **Section 5.3**: "on the valley of best static fit in Fig. 9b". The term is defined only in the figure caption.
- **Section 6**: "The authors' deflection records from simply supported spans showed post-minus-pre level differences of up to 0.23 mm." The source of these records is unclear.

---

## 3. The 10 hardest-to-read passages

1. **Abstract**: "Two indicators tell whether a small constant reflects cancellation or restraint, sensors belong at the extremes of the uniform-load response, and a closed-form law gives the effect of uncertain pier stiffness."
   *Why hard:* three unrelated results are forced into one parallel sentence; "two indicators" is vague; "the effect" of pier stiffness on what?
   *Fix:* "A cancellation ratio separates cancellation from restraint. Optimal sensors lie at the extremes of the uniform-load response. A closed-form (Möbius) law gives the integral constant as a function of uncertain pier stiffness."

2. **Abstract**: "Public moving-truck records from a five-span box girder support invariance of the constant only coarsely, because the reference weights hardly vary."
   *Why hard:* the causal clause belongs to a different limitation (weight discrimination); the coarseness comes from noise and the small number of runs.
   *Fix:* "On public moving-truck records from a five-span box girder, the constant was invariant to within the 10–27 % that noise and eight runs per day allow; because the reference weights hardly varied, weight discrimination could not be tested."

3. **Section 2.5**: "Every static response then equals $\alpha^{-1}$ times a function of $\kappa$ alone, where $\kappa = k/\alpha$ is the scaled pier stiffness; because $\alpha$ is dimensionless, $\kappa$ has the units of $k$. For any assumed $\kappa$, two static readings therefore fix $\alpha$, and they constrain $\kappa$ only through the ratio of the two readings."
   *Why hard:* a scaling argument, a units aside and an identifiability consequence come one after another with no intermediate step.
   *Fix:* split the passage and state the consequence explicitly: "Every static response therefore has the form $y = f(\kappa)/\alpha$. The ratio of two readings, $y_1/y_2 = f_1(\kappa)/f_2(\kappa)$, does not depend on $\alpha$, so only this ratio carries information about $\kappa$; once $\kappa$ is chosen, either reading gives $\alpha$." Move the units remark to the Nomenclature.

4. **Section 2.4**: "Within a single record, the weighting function $g(x)$ along the record must be uniform. Appendix B shows that no other weighting function keeps the integral independent of the axle configuration for every structure, and this is the property on which SLM relies. It also links SLM to transmissibility-based weighing [34]: ..."
   *Why hard:* a new symbol, a strong claim, an unclear antecedent ("this property") and a side remark about transmissibility, all in three sentences.
   *Fix:* "Could a non-uniform weighting $g(x)$ along a record do better than the plain integral? Appendix B shows that it cannot: only a uniform $g$ keeps the estimate independent of the axle configuration for every structure. SLM relies on this invariance." Put the transmissibility link in a footnote or in the Introduction.

5. **Section 4.3**: "Estimating $\Sigma$ from the crossings instead over-fits with eight runs: the error of GLS rises from 10.4 % of GVW in sample to 28.4 % out of sample. The zero-sum estimator therefore pays only for disturbances that are common-mode during crossings, as anticipated in Section 2.4."
   *Why hard:* "instead" is ambiguous in its position; "pays" is opaque; the second sentence does not follow from the first.
   *Fix:* "Estimating $\Sigma$ from the crossing residuals instead of from vehicle-free windows over-fits with only eight runs (GLS error 10.4 % in sample, 28.4 % out of sample). As anticipated in Section 2.4, the zero-sum estimator helps only when the disturbance is common-mode during the crossings themselves."

6. **Section 4.2**: "This agrees with Eq. (2), which makes the constant independent of the axle configuration for a linear structure, but with eight runs differences up to about 27 % cannot be excluded. The test therefore checks linearity and processing at a coarse level, not the identity itself."
   *Why hard:* the reader is told the result agrees with the identity and then that it does not test the identity.
   *Fix:* "The result is consistent with Eq. (2), but with eight runs it cannot exclude differences of up to about 27 %. It is therefore a coarse check of linearity and processing, not a sharp test of the identity."

7. **Section 5.2 and Table 8**: "At this tolerance the static data bound $\kappa$ only from below ... At $\tau = 3$ % the admissible set shrinks and excludes the design rigidity, $\alpha = 1$." Table 8 then has columns for two normalisations, a prior row and "–" cells.
   *Why hard:* the reader must hold the tolerance, two normalisations, a prior and four ranges in mind at once, and the same ranges come back in Table 10 in slightly different form.
   *Fix:* merge Tables 8 and 10 into one table with a single normalisation (design $EI_\mathrm{mid}$) in the main text, give the effective-rigidity variant in a footnote, and move the $\tau = 3$ % and 4 % rows to the Supplementary Material. Open the subsection with the one-sentence result: "The data fix the centre-span constant to ±20 % but leave the side-span constant uncertain by a factor of 6.6."

8. **Section 5.2**: "The six readings of each gauge (three lines, centric and eccentric) spread by 1.9–2.0 % about their mean. This spread comes from the transverse positions and is not a repeatability, because the readings are not replicates. Adding a model-form spread of 1.75 % per gauge gives $\tau = 5.3$ % at two standard deviations."
   *Why hard:* the reader cannot reconstruct 5.3 % (it is not said whether the components are added in quadrature or how 2σ applies), and "three lines" is undefined.
   *Fix:* "With a measurement spread of 2.0 % and a model-form spread of 1.75 %, combined in quadrature to 2.64 % and doubled for two standard deviations, the tolerance is $\tau = 5.3$ %." Define "line" (transverse truck line) in Section 5.1, where the six readings are first mentioned.

9. **Section 2.4**: "For two channels the zero-sum weights are $w = (1,-1)/(C_1-C_2)$ ... The white-noise variance then rises by the factor $2C_1^2/(C_1-C_2)^2$, which is 1.65–2.0 on the beams studied. This price is small, because the white-noise term of Eq. (14) is only about 5 × 10⁻⁶ of the offset term for the parameters of Section 5.3 with $\Delta x = 0.1$ m."
   *Why hard:* it depends on case-study parameters not yet introduced, and $w$ here means weights while $w$ elsewhere means deflection.
   *Fix:* rename the weight vector (for example $\boldsymbol{a}$ or $\boldsymbol{\omega}$), and replace the forward reference with "for typical long-span parameters (Section 5.3) the white-noise term is negligible against the offset term."

10. **Section 4.1**: "Day 1 has 12 channels at 100 Hz, labelled with the prefix "ch". Four stations each carry two gauges: a wheel-path gauge that shows axle spikes (ch4, ch5, ch11, ch12) and a partner gauge. The other four gauges show no axle spikes (ch1, ch2, ch8, ch9)."
    *Why hard:* the reader cannot tell which channels are the partners, whether the partners show spikes, or why the spike-free gauges matter, and these groupings drive Tables 3–4.
    *Fix:* add a small table or schematic (station, channel, wheel-path or not, spikes yes/no), or write: "The 12 gauges fall into three groups: four wheel-path gauges with clear axle spikes (ch4, ch5, ch11, ch12), four partner gauges at the same stations (ch3, ...), and four gauges without spikes (ch1, ch2, ch8, ch9)."

---

## 4. Spelling and grammar errors (confident)

The English is generally clean. The confident errors are:

- **Abstract**: "Two indicators tell whether ..., sensors belong at ..., and a closed-form law gives ...". Faulty parallelism: three independent clauses are joined as list items.
- **Section 2.4**: "the crossing residuals, that is the deviations of each crossing's integral ..., were not." It needs a comma after "that is" ("that is, the deviations").
- **Section 4.1**: "On day 1 two 3-axle trucks ran ..." and "On day 2 a 3-axle truck ...". A comma is needed after the introductory phrase to avoid misreading "1 two 3-axle".
- **Section 4.4**: "The two in-line two-truck runs are consistent with superposition but low." An adjective is left dangling with no noun ("but their response is low").
- **Section 6**: "Speed enters twice. It affects the response, and it enters through its measurement". "Enters ... enters" makes the second sentence read as a restatement; use "It affects the response itself, and it enters again through its measurement".
- **Spelling convention**: British spelling is used throughout ("generalised", "normalise", "modelled", "labelled", "Colours"), but the heading is "Acknowledgments" (US). Use "Acknowledgements", or follow the journal style. ("Conceptualization" in the CRediT statement is standard and fine.)
- **Ref. [34]**: "bridge weight-in-motion". This is probably the original article's typo; check it against the source and keep it only if it is verbatim.
- **Section 2.2 / Table 1**: "Strain, moment, curvature" against "strain or moment" in Fig. 3. Not an error, but the two lists should match.

---

## 5. Non-standard or inconsistent terms and notation

**Symbols with two or more meanings**

- **$m$**: the channel position index ($C_m$, $\eta_m$, $r_m$, $y_m$); the dimensionless end moment ($m$, $m_l$, $m_r$); the subscript "main span" ($L_m$, $EI_m$); and the unit metre. This is the worst overload in the paper.
- **$L$**: the loaded path length ($[0,L]$ in Section 2.1, Eq. 2) and the span containing the sensor (Nomenclature, Eq. 10). "0.4L" in Section 5 is a third use (side-span length). Note also $l$ (laboratory span), $L_\mathrm{tot}$ and $L_v$.
- **$w$**: deflection $w(x)$, $w_q$; the weight vector $w$, $w^\star$; and the subscript of $N_w$.
- **$K$**: stiffness matrices $K_g$, $K_p$, $K$ (Section 2.5, Appendix C) and the dimensionless pier stiffness $K = kL_s/EI_s$ (Eq. 16).
- **$r$**: channel index ($J_r$, $C_r$), response functional $r_m[\cdot]$, ratio $r_{87}$, coefficient of determination $r^2$; and $R$ is the cancellation ratio.
- **$\varepsilon_0$**: defined as an offset "in the units of the channel", yet used in millimetres for deflection channels (Table 12). The strain symbol for a displacement offset is misleading; $\delta_0$ or $e_0$ would be neutral.
- **$\alpha$** (rigidity ratio) and **$\alpha^*$** (best-fit valley): fine, but $\kappa = k/\alpha$ has the units of $k$ only because $\alpha$ is dimensionless, which the reader has to be told.
- **$s$** (Appendix B): position in the span ($\xi = s/L$) and load positions $s_a$.
- **$\xi$ and $\zeta$**: both fractional positions; $\zeta$ is measured from the pier, $\xi$ from the left end of the span. This is easy to confuse in Table 1.
- **$y_m$** (record, Eq. 1) against **$z_j$** (record, Appendix B). Two symbols for one quantity.
- **$J$, $J_r$, $J_j$, $J_t$, $J_0$**, and **$C$, $C_r$, $C_m$, $C_j$, $C_8$, $C_\varepsilon$, $C_\theta$, $C_V$**: index families mix channel type, channel number, gauge name and crossing.

**Symbols used but not defined (or defined late)**

- $\sigma$ (Eq. 14, Section 5.3), $\sigma_{P,\mathrm{noise}}$ (Section 2.4), $\Delta x$ (only in prose) and $\nu$ (Appendix A) are not in the Nomenclature.
- $\lambda$, $\beta$, $\gamma$ are defined after Eq. (4); $k_g$ after Eq. (15).
- $N_w$ is used implicitly in Eq. (5) before Eq. (10).
- $K_g$, $K_p$, $e_m$, $q$, $\theta_{m,i}$ (Appendix C) are not in the Nomenclature.
- "Line" in "three lines, centric and eccentric" (Section 5.2) is undefined.

**Several names for one concept**

- Zero-sum estimator / "offset-immune" (Fig. 4) / "immune-eq" (Fig. 7).
- Crossing residuals / crossing errors (Abstract).
- Gauge average / plain average / wheel-path average / average of 4.
- Leave-one-run-out / leave-one-out (Table 6) / LOO (Fig. 7). LOO is not defined in the Nomenclature, whereas LOTO is.
- Influence-area identity / response-integral identity / area identity / "the identity" / "two classical facts" (Abstract).
- Integral constant / the constant / $C$. "Indicator" is used both for the normalised constant ($N_w$, $N_M$) and for $B_m$, and the heading of Section 2.5, "Identifiability of the indicator", is about the constant.
- Calibrations A and B / "reference calibrations" / "reference models" (Table 9, which also includes the non-calibration "prismatic, pinned" model).
- Mean-weight predictor / mean-GVW / "a predictor that always returns the mean calibration weight".
- Cầu Mây "main bridge" / "200 m unit" / "the girder".
- Design $EI_\mathrm{mid}$ / $EI_\mathrm{ref}$ / "design $EI$".

**Terms used before definition**

- "Blind loci" (title, Abstract) are defined only implicitly in Section 2.2.
- "Cầu Mây" is used in Section 2.5 (β = 1.636, indicator values) and in Fig. 2, but introduced in Section 5.1.
- "Valley of best static fit" (Section 5.3) is defined only in the caption of Fig. 9.
- "Near-blind" is defined in Section 2.2 with reference to the indicator "of Section 2.3".
- "Common-mode fraction" $\rho$ appears in Eq. (14) and is defined in one line; how it is estimated comes two sections later.

**Undefined or inconsistently handled abbreviations**

- WIM (Section 1) is not in the Nomenclature.
- LOO and IN appear only in figures.
- χ² test, CC0, DT389 and PMU are not expanded.
- FE and SD are defined twice (Nomenclature and text), which is harmless, but GVW is expanded in the text after being used in the Abstract in full.

**Units**

- Constants are given in µε m/t (Section 4) and in m²/kN (Section 5); weights are in t, loads in kN and N. A single force unit for the constants would help.
- In Table 13 the "Sensitivity" of the offset is $L_\mathrm{tot}/J$, which is dimensional, while all other entries are dimensionless multipliers.

**Inconsistency between text and figure**

- Section 5.2 defines admissibility as "misfit at each gauge within $\tau$". The caption of Fig. 9 gives the band as $|\ln r_{87}|\le 2\tau$. The reader is not told how the two definitions relate.

---

## 6. The single change that would most improve readability

**Cut the density in Sections 4 and 5 by moving secondary numbers into the Supplementary Material and leading each subsection with its one-sentence result.**

Concretely: (i) merge Tables 8–10 into one table with one normalisation; (ii) in Sections 4.2–4.4 keep only the numbers that support a stated claim, and move per-channel ranges, lane-B details, TOST margins for secondary rows and the in-sample/over-fitting figures to the Supplementary Material; (iii) open each subsection with a bold or topic sentence that states the finding before the evidence (for example, "GLS failed on day 2 because crossing residuals are less correlated than vehicle-free noise"). This would roughly halve the number of figures per paragraph without removing any result.

A close second, and cheap to do: fix the notation overload, chiefly by renaming the end-moment parameter $m$, the weight vector $w$, the dimensionless pier stiffness $K$, the path length $L$ and the offset $\varepsilon_0$, and by using one name each for the zero-sum estimator and for the crossing residuals.
