# Blind readability review: manuscript v4 (reviewer 3)

Scope: readability only. I did not judge scientific merit or check whether the equations and numbers are correct. I ignored [NEED VALUE] placeholders and the missing figures. Method: one straight read-through, marking every place I had to re-read, then a slow second pass sentence by sentence.

---

## 1. Scores

| # | Criterion | Score | Main reason |
|---|---|---|---|
| 1 | Abstract clarity | 6.0 | It packs about twelve findings into one paragraph and leans on terms the reader has not met yet ("restraint", "crossing residuals", "integral constant"); the three field sentences are the hardest in the paper. |
| 2 | Introduction flow and motivation | 7.0 | The path from overloads to BWIM to integral methods to the continuous-girder gap is logical, and the gap is stated sharply; the literature paragraphs read like lists, and contribution items 2 and 4 use $N_M$, $R$, $\kappa$ and "Möbius" before defining them. |
| 3 | Signposting and structure | 7.5 | Every section opens by saying what it does, and a roadmap and a design workflow tie the paper together; marks come off for several forward references (Eq. 5 points to Eq. 10, Sections 2.4 and 4.3 point at each other) and for frequent hand-offs to the Supplementary Material. |
| 4 | Sentence-level clarity | 6.5 | Most sentences are short and declarative, but many carry two or three numerical qualifications, and some rely on unclear pronouns ("it", "the same runs", "the second equality"). |
| 5 | Information density | 5.0 | Almost every sentence in Sections 4–6 carries one to three numbers with CIs; specialists will cope, but there is no breathing space and the main message of each subsection is easy to lose. |
| 6 | Terminology and notation | 5.5 | The nomenclature is thorough, but there are real clashes: $N_M$/$N_w$ against gauges N7/N8, $a$ used three ways, subscript 0 meaning both "pinned" and "reference", $F$ against $F_A$ and $\Phi$. Several concepts also have three or four names. |
| 7 | Equations in prose | 7.0 | Equations are introduced in sentences and their symbols are explained close by; some links are ambiguous ("the second equality needs superposition only"), and Section 2.2 uses the indicator before it is defined. |
| 8 | Results presentation (tables included) | 6.0 | The tables are informative and include CIs, but the captions and footnotes are heavy. Table 4 mixes 95 % and 90 % CIs, Table 6's column headers are inconsistent, and Table 8 needs two footnotes to read. |
| 9 | Conclusions | 6.5 | The conclusions are numbered, specific and honest about limits, but they are crowded with numbers, and item 3 mixes a theoretical result with a field failure. |

**Overall: 6.3 / 10**

Weighting: I gave the most weight to sentence-level clarity, information density and terminology (about half of the total), because these decide whether a specialist can read the paper without friction. Its structure, by contrast, is already sound. Abstract, conclusions and results presentation carry about a third, because most readers will see only these. Introduction and equations-in-prose carry the rest. The paper is clearly carefully edited: sentences are short, sections are signposted and claims are hedged. But the density of numbers and the notational clashes make reading slow even for a specialist. It reads as a solid but tiring draft in a good journal, below the 8 I would give a paper that reads without friction.

---

## 2. Places re-read on the first pass

- **Abstract**: "the constant was invariant only within the 10–27 % that noise and run count allow". It took me two reads to see that this means "invariance could only be shown to within ±10–27 %".
- **Abstract**: "A cancellation ratio separates cancellation from restraint". "Restraint" is not defined here, and only becomes clear in Section 2.3 and 5.2.
- **Abstract**: "because crossing residuals are much less correlated between gauges than vehicle-free noise". "Crossing residuals" is undefined until the end of Section 2.4.
- **Introduction, contribution 4**: "the constant depends on pier stiffness only through the scaled pier stiffness $\kappa = k/\alpha$ and a linear-fractional (Möbius) law, and which names the measurement that resolves it". The sentence has too many clauses, and $\alpha$ is undefined at this point.
- **2.1**: "the second equality needs superposition only". Eq. (2) contains three equalities, and it is unclear which one is meant.
- **2.1**: "At constant speed $v$ the time integral is $J_m/v$." This sits oddly after the strain-blind sentence and breaks the train of thought.
- **2.2**: "For a mid-span sensor on two spans of equal rigidity, the blind span ratio and the optimal sensor position are". A mid-span sensor has a fixed position, so "optimal sensor position" ($\xi^* = 0.4215$) reads as a contradiction. It refers to a different question (equal spans, free position).
- **2.2**: "The left-hand side of Eq. (5) is the deflection indicator of Section 2.3, Eq. (10)". This is a forward reference, and I had to jump ahead.
- **2.2, Table 1, Rotation and Shear rows**: "mid main span: always". It is unclear whether this means "always blind" or "always observable".
- **2.2**: "One identity in Table 1 is useful in practice." The identity $N_F = \xi_0$ is not visible in Table 1 itself.
- **2.3**: "It combines sensor position, baseline stability and the lightest vehicle to be screened into one number." $P_\delta$ as defined does not contain the vehicle weight ($b$ does), so I re-read Eq. (12).
- **2.4**: "Optimal sensors therefore lie at the maximum and the minimum of $C(x)$", followed by "With independent offsets, every sensor should sit as close as possible to the maximum". This looks like a contradiction on first read.
- **2.4**: "Adding the constraint $\sum_ja_j = 0$ within each channel type". It is unclear whether this is in addition to $a^\top C = 1$ or instead of it.
- **2.5**: "Once $\kappa$ is chosen, either reading gives $\alpha$." "Chosen" suggests a free choice; "fixed" or "identified" is meant.
- **3**: "The SLM deviations of 0.61 % and 0.70 % match the growth of this ratio relative to its one-load value of 1.010. The data cannot tell whether support seating or errors in the stated masses cause it." The referent of "it" is unclear.
- **4.1**: "a partner gauge at each of these four stations". I could not picture the layout (a transverse partner? a second gauge at the same station?).
- **4.1**: "Three day-1 runs with two trucks on the bridge and four passes without documented weights were excluded; the same runs are used throughout." It is unclear whether "the same runs" means the excluded ones or the retained ones.
- **4.2, Table 4 caption**: "the 90 % CI of the ratio lies inside the stated margin (for ch11, 0.904–1.098)", while the table shows a 95 % CI of 0.874–1.136 for ch11. Two different intervals for one quantity side by side confused me.
- **4.3**: "GLS amplifies this component, because it gives st40 and st36 large weights of opposite sign (+0.16 and −0.35)." I had to check which weight belongs to which gauge.
- **5.1**: "N8 at 0.4L of the side span between pier T7 and end support T8". It is not stated whether 0.4L is measured from T7 or from T8.
- **5.1**: "Each gauge has six readings (three lines, each centric and eccentric)". "Lines" is undefined (load lines? truck rows?), and "centric" is unusual.
- **5.2**: "Calibrating the model to the N8 reading does not fix the N8 constant either. Over the admissible set, the ratio of $C_m$ to the modelled N8 deflection varies by a factor of 6.5". This needed two reads to understand which quantity is being normalised.
- **5.2**: "The measured vertical frequencies (3.43–3.64 Hz)". Frequencies are mentioned here for the first time and are not introduced in 5.1.
- **5.3**: "$N_M$ = 0.163–0.212 at N7". A strain indicator at a deflection gauge's position, written as N…/N…, made me stop.
- **5.3**: "The pair at 100 m and 152 m from the end support T5 is within 0.9 % of the calibration-specific optimum". It is unclear what is within 0.9 %: the variance, the SD or the position.
- **6**: "For a constant force moving across the laboratory beam". Applying the dynamic bound to the laboratory beam in a field error budget is unexpected.
- **6, last paragraph**: "the reference record and the load-dependent step limit SLM to 0.6–0.7 %". "Load-dependent step" is a new name for the 1.010 → 1.017 trend in Section 3.
- **Fig. 9 caption**: "the admissible band $|\ln r_{87}|\le 2\tau$ … which is equivalent to both misfits lying within $\tau$ at the best-fit $\alpha$". This is dense and needs a sentence in the main text.

---

## 3. The 10 hardest-to-read passages

1. **Abstract**: "On public moving-truck records from a five-span box girder, the constant was invariant only within the 10–27 % that noise and run count allow, and the narrow range of reference weights did not allow weight discrimination to be tested."
   *Why hard:* "invariant only within" inverts the logic: the constant was not shown to vary, but invariance could be shown only to a coarse margin. Two separate findings share one sentence.
   *Fix:* "On public moving-truck records from a five-span box girder, the constant was consistent with invariance, but the noise and the small number of runs allowed differences of up to 10–27 % to go undetected. The reference weights varied too little to test weight discrimination."

2. **Abstract**: "Generalised least-squares weights estimated from vehicle-free noise did worse out of sample than the gauge average, because crossing residuals are much less correlated between gauges than vehicle-free noise."
   *Why hard:* "crossing residuals" is undefined, "did worse" is informal, and the causal clause needs the GLS mechanism to make sense.
   *Fix:* "Generalised least-squares (GLS) weights based on vehicle-free noise were less accurate out of sample than a plain gauge average. The noise was strongly correlated between gauges, but the deviations of individual crossings were not, so GLS amplified gauge-specific errors."

3. **Section 1, contribution 4**: "an identifiability analysis of the indicator under boundary uncertainty, in which the constant depends on pier stiffness only through the scaled pier stiffness $\kappa = k/\alpha$ and a linear-fractional (Möbius) law, and which names the measurement that resolves it;"
   *Why hard:* There are two relative clauses ("in which", "and which"), and $\alpha$ is undefined. "Only through … and a law" mixes a variable with a functional form. The referent of "it" is unclear.
   *Fix:* "an identifiability analysis under uncertain pier stiffness: the constant depends on the pier stiffness $k$ and the girder rigidity factor $\alpha$ only through $\kappa = k/\alpha$, following a linear-fractional (Möbius) law, and one additional measurement suffices to identify $\kappa$;"

4. **Section 2.2**: "A deflection blind point therefore exists only for $1<\mu<2$. For a mid-span sensor on two spans of equal rigidity, the blind span ratio and the optimal sensor position are [Eq. 7]"
   *Why hard:* $\lambda_\mathrm{crit}$ is for a mid-span sensor, while $\xi^*$ is the optimum position for equal spans ($\mu = 1$), a different question. Putting both in one equation and one sentence suggests they belong together.
   *Fix:* Split it into two sentences. "For a mid-span sensor on two spans of equal rigidity, the deflection channel is blind at $\lambda_\mathrm{crit} = 1.4574$. For two equal spans, the indicator is largest at $\xi^* = 0.4215$, not at mid-span."

5. **Section 2.4**: "If the noise statistics do not depend on position, $1/\mathrm{Var}$ is a convex quadratic in the vector of constants $C(x_j)$, for both Eqs. (13) and (14). The feasible constants form a box, bounded by the smallest and largest $C(x)$ along the girder, and a convex function on a box attains its maximum at a vertex. Optimal sensors therefore lie at the maximum and the minimum of $C(x)$."
   *Why hard:* This is a compressed proof inside the main text. "Box" and "vertex" are unexplained for a structural audience. The conclusion "maximum and minimum" is then qualified in the next paragraph ("every sensor … as close as possible to the maximum"), which reads as a contradiction.
   *Fix:* State the rule first: "Each optimal sensor sits at either the largest or the smallest value of $C(x)$ along the girder: all at the largest when offsets are independent, one at the smallest when they are correlated." Move the convexity argument to Appendix B or give it as a one-line justification.

6. **Section 4.2, Table 4 caption and text**: "Equivalence by two one-sided tests (TOST) at the 5 % level: the 90 % CI of the ratio lies inside the stated margin (for ch11, 0.904–1.098)." The table itself shows "0.996 (0.874–1.136) | shown within ±10 %".
   *Why hard:* The reader sees a 95 % CI that extends beyond ±10 % next to the verdict "shown within ±10 %", and the reconciling 90 % CI is given only for one row, in the caption.
   *Fix:* Add a column "90 % CI (TOST)" next to the 95 % CI, or report only the 90 % CI in this table and explain why in one sentence in the text.

7. **Section 5.2**: "Calibrating the model to the N8 reading does not fix the N8 constant either. Over the admissible set, the ratio of $C_m$ to the modelled N8 deflection varies by a factor of 6.5, against 1.5 for N7."
   *Why hard:* The point (scaling the model to the measured peak does not rescue the constant) is important but buried in a ratio of two model quantities. $C_m$ is used generically when $C_8$ is meant.
   *Fix:* "Scaling the model so that it reproduces the measured N8 deflection does not help: across the admissible set, $C_8$ divided by the modelled N8 deflection still varies by a factor of 6.5 (1.5 for N7). A static reading therefore cannot replace an identified pier stiffness."

8. **Section 5.3**: "Strain channels behave differently (Fig. 8). The haunches move every zero-moment point towards mid-span. Over the range of pier stiffness the side-span zero lies 26.0–33.3 m from the abutment, so a strain gauge at mid side span would be practically blind under calibration A ($N_M = 0.048$) and would change sign with pinned piers. The centre of the main span lies in the strain near-blind band in every haunched model ($N_M$ = 0.163–0.212 at N7), again because of restraint ($R_\varepsilon$ = 0.65–1)."
   *Why hard:* Five numbers, two hypothetical gauges, and the clash between $N_M$ and gauge label N7. "Again because of restraint" relies on a concept that is never defined.
   *Fix:* Split it into one sentence per location, write "at the N7 position (mid main span)", and define restraint once in Section 2.3 ("a small constant caused by end fixity rather than by sign cancellation").

9. **Section 5.3, tiltmeter paragraphs**: "Its benefit is measured by the Cramér–Rao bound on the standard deviation of $\ln C_8$. The bound is evaluated at the scaled pier stiffness of calibration A, $\kappa = 2.75\times10^7$ kN m/rad, with $\alpha$ refitted to the two readings at that $\kappa$ ($\alpha^* = 1.07$; …)… At calibration A the two deflections alone give a bound of 0.87."
   *Why hard:* A bound of "0.87" has no stated meaning for a structural reader (0.87 in log units is a factor of about 2.4). The evaluation conditions run to three nested parentheses.
   *Fix:* Give the meaning: "a lower bound of 0.87 on the standard deviation of $\ln C_8$, i.e. the constant is uncertain by a factor of about 2.4". Move the evaluation details ($\alpha^*$, the 3 % rotation uncertainty) to the Table 10 caption or the Supplementary Material.

10. **Section 2.1, last paragraph of 2.1 plus Eq. (2) text**: "This is the classical influence-area identity [23,38]; the second equality needs superposition only. $C_m$ is called the integral constant, or simply the constant; $C_\varepsilon$, $C_\theta$ and $C_V$ denote it for strain, rotation and shear channels."
    *Why hard:* "The second equality" is ambiguous (Eq. 2 has three), and the naming convention ($C_m$ indexed by position, but $C_\varepsilon$ by channel type, later $C_7$, $C_8$ by gauge) is introduced in a way that later leads to clashes.
    *Fix:* "The identity $C_m = y_m[q_0]/q_0$ requires only superposition." Then fix one indexing scheme: "$C$ with a subscript for the channel type ($C_w$, $C_\varepsilon$, …); for named gauges, $C_{N7}$, $C_{N8}$."

---

## 4. Spelling and grammar errors I am confident about

- **Abstract**: "did worse out of sample". This is informal for a journal; use "performed worse out of sample" or "was less accurate out of sample".
- **Section 1**: "the near-blind band that can catch strain gauges set back from the piers". "Catch" is colloquial; use "that can contain strain gauges set back from the piers".
- **Section 2.2**: "every channel is fixed by the two end moments". "Determined" is meant; "fixed" clashes with "fixed piers".
- **Section 3**: "calibrated weights were suspended at 250 mm steps along the traverse". "Traverse" is not standard for a beam; use "along the span" or "along the beam".
- **Section 5.1**: "under centric and eccentric transverse positions". "Centric" is non-standard in English engineering prose; use "central (concentric) and eccentric".
- **Section 5.1**: "The Cầu Mây Bridge". "Cầu" already means "bridge". This is acceptable for an international readership, but consider "the Cầu Mây bridge" in lower case or a gloss on first use.
- **Section 6**: "post-minus-pre level differences". This is jargon, not English prose; use "differences between the levels after and before each crossing".
- **Hyphenation, inconsistent**: "mid side span" versus "mid side-span deflection gauge"; "out of sample" versus "out-of-sample" (fine as adverb/adjective, but check consistency); "3-axle" (Section 4) versus "three-axle" (Sections 5 and 6).
- **Affiliation line**: "Bach Mai ward" should be "Bach Mai Ward".
- **Reference [34]**: "bridge weight-in-motion". Check this against the original title. If the original says "weigh-in-motion", correct it; if it does say "weight", keep it but be aware readers will flag it.
- **Supplementary Materials paragraph**: "(former Appendix D)". This is an editorial leftover and should be deleted.
- **Section 4.1**: "by only a few per cent". It is acceptable British usage, but the paper otherwise uses "%"; be consistent.

---

## 5. Non-standard or inconsistent terms and notation

**Symbols with two or more meanings**
- **$N$** stands for the indicators ($N_w$, $N_M$, $N_\theta$, $N_V$, $N_F$) and also begins the gauge labels N7 and N8. "$N_M$ = 0.163–0.212 at N7" and "N8 spans 0.124–0.822" are visually ambiguous. Rename the gauges (e.g. D7, D8) or the indicators (e.g. $\Omega_w$).
- **$a$** is the vector of channel weights ($a$, $a^\star$, $a_j$), the axle offsets ($a_i$, $a_\mathrm{max}$, Eq. 1) and an axle index in Appendix B ($\sum_aP_ah(s_a)$).
- **Subscript 0** means "pinned piers" in $C_0$, "reference crossing" in $P_0$ and $J_0$, the strain zero in $\xi_0$ and $\zeta_0$, the residual offset in $\delta_0$, and the uniform load in $q_0$.
- **$F$**: $F(\xi,\mu)$ (Eq. 5) is the deflection shape function and $F_A$ is the end reaction. The same function is renamed $\Phi$ in Appendix B.
- **$c$** is the fibre distance and also the subscript "centre" ($L_c$, $EI_c$).
- **$\gamma$** has different definitions for two and three spans. This is acknowledged, but it is a trap.
- **$C$ subscripts** carry three indexing schemes: position ($C_m$, $C(x_j)$), channel type ($C_\varepsilon$, $C_\theta$, $C_V$) and gauge number ($C_7$, $C_8$). "$C_8$" can be misread as "position 8".
- **Stars**: $\xi^*$ and $a^\star$ mean "optimal", while $\alpha^*$ means "best static fit".
- **Sensitivities**: $S_k$ is with respect to $k$, while $B_m$ and $S_{y8}$ are with respect to $\kappa$. The reader has to track which variable each one uses.
- **$T$**: T5, T7 and T8 are supports, while $T_1$ is the fundamental period. **$t$** is the tonne unit in "µε m/t" and also time in $t_\mathrm{cr}$.
- **$L$** is "the span containing the sensor", but "0.4L" in N8's label is the side span, which is not stated. The laboratory span gets its own symbol $l$ for no clear reason.
- **$\sigma$** is the white-noise SD of a record, while $\sigma_{P,\mathrm{noise}}$ is the SD of the load (undefined).

**Symbols used but not in the nomenclature or not defined**
- $\nu$ (Appendix A), $h$ (depth, Sections 4.4, 5.1 and 5.3), $L_v$ (Section 5.1), $\sigma_{P,\mathrm{noise}}$ (Eq. 13 text), $R_\varepsilon$ and $R_w$ (subscripts not explained), the generic "$|N|<0.2$" (Fig. 3), and $e_m$, $G$, $q$, $\theta_{m,i}$ (Appendix C, defined locally but $q$ clashes with $q_0$).

**Terms used before definition**
- "restraint": used in the abstract, Sections 2.3, 2.5, 5.2, 5.3 and workflow step 3, but never defined.
- "crossing residuals": used in the abstract, defined at the end of Section 2.4.
- "integral constant": used in the abstract before its formal naming in 2.1 (acceptable, but the abstract definition is convoluted).
- $\kappa$, $\alpha$, $N_M$, $R$ and "Möbius law" appear in the Section 1 contribution list.
- "admissible set": used in the Table 8 caption logic and 5.2, defined mid-5.2.
- "load-dependent step" (Section 6) is the trend first described in Section 3 without that name.
- "the identified first and third vertical frequencies" (5.3) are never reported in 5.1.

**Several names for one concept**
- Total load: "gross vehicle weight", "gross weight", "GVW", "total load", "load", $P$, $P_\mathrm{tot}$.
- Integral constant: "integral constant", "the constant", "absolute constant", "strain constant", $C$, $C_m$.
- Indicators: "indicator", "observability indicator", "conditioning indicator", "normalised indicator", "deflection indicator".
- Blindness: "blind point", "blind locus", "blind configuration", "blind span ratio", "blind abscissa", "blind condition".
- Zero-sum estimator: "zero-sum estimator", "zero-sum pair", "differential measurement", "offset-immune" (Fig. 4), "immune-eq" (Fig. 7).
- Gauge average: "gauge average", "wheel-path average", "average", "the average of the four wheel-path gauges".
- Supports: "pier", "inner pier", "interior support", "monolithic pier"; and "end support" versus "abutment".
- Span positions: "centre span", "main span", "mid main span", "centre-span gauge"; "side span", "end span", "instrumented span".
- Lanes: "lane A", "instrumented lane", "near lane"; and "lane B", "other lane", "far lane", "return trip".
- Sensors: "channel", "gauge" and "sensor" are used interchangeably.
- Record integral: "record integral", "integral", "area under the response", "strain integral", "integral of the record".

**Abbreviations**
- "LOO" appears only in the nomenclature and in Fig. 7; the text always spells out "leave-one-run-out". "IN" (Fig. 7), "2S-eq", "3S-b2.0", "CM-A", "GLS-diag" and "GLS-resid" are figure-only labels.
- Both "Generalised least squares" (nomenclature) and "generalised least-squares" (abstract) appear; choose one.
- "PMU", "TNHH" and "DT389" are not expanded (PMU only in a placeholder).
- "NOR" and "NOR-BWIM" are both used; "NOR-BWIM" is defined only in Section 4.1.

---

## 6. The single change that would most improve readability

**Lower the numerical density of the running text in Sections 4–6 by moving secondary numbers into tables and opening each subsection with one plain-language result sentence.** Today almost every sentence carries one to three values with CIs, and the reader has to dig out the message each time (for example, Section 4.2 restates "invariance can be shown only coarsely" three times between numbers). If each paragraph started with its claim in words ("GLS was less accurate than a plain average because the gauge-specific part of each crossing is not common-mode") and gave at most one key number, with the rest in Tables 3–12, the paper would read much faster. A close second is a notation clean-up: rename the gauges N7 and N8, give $a$ and subscript 0 single meanings, define "restraint", and pick one name each for the constant, the total load and the zero-sum estimator.
