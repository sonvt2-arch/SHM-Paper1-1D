# Desk assessment: Editor-in-Chief, Structural Control and Health Monitoring

**Manuscript:** "Blind loci and design criteria for integral load-monitoring channels on continuous girder bridges, with laboratory verification and an assessment on public field records" (Nguyen, Vu, Nguyen)
**Files read:** manuscript.md (v4), supplementary_material.md, cover_letter_SCHM.md, Figs. 1–9 (Figs. 2, 4, 5, 7, 8 and 9 examined in detail) and the supplementary captions.
**Note:** I could not run a web check (the search tool was unavailable), so the comments on scope and literature rest on my own knowledge of the journal and the field.

---

## 1. Decision

**Return to authors before review.** The manuscript is careful and honest, and it is unusually reproducible. The closed forms are checked against FE in 981 cases, the field statistics come with confidence intervals and out-of-sample tests, and the negative results are reported plainly. It is in scope. In its present form, however, it will not survive three referees, for three reasons.

- **The theory is thin as a contribution.** Its core is classical. A gauge is blind at the zeros of the uniform-load response (moment diagram, deflection line). The Möbius law is a rank-one Sherman–Morrison update. The estimator is textbook GLS. What is new is the catalogue and the framing, and the manuscript does not show that this framing changes a design decision on a real structure.
- **Nothing tests the theory at structural scale.** No blind or near-blind configuration was measured anywhere: not in the laboratory, not in the field, and not at Cầu Mây, where the key results are predictions (Table 6). The public field records cannot discriminate weights: the mean-weight predictor beats every estimator. They also show that a 1-D beam model does not even predict the constants of deck-soffit gauges (ch11/ch8 = 3.9 against about 1 predicted). That undercuts the premise that 1-D blind loci govern channel design on box girders.
- **The authors' own error budget says the method is marginal.** In Section 6, a 0.1 mm offset biases a 25 t truck by 16–25 % at the best location. The paper therefore gives design criteria for a method it shows to be marginal at the very scale it targets, yet it never states clearly what the criteria are worth in that light.

At about 14,000 words, with five claimed contributions, eight tables, nine figures and 15 supplementary figures, the paper is also too long for its evidence. I would rather the authors fix these points now than spend three referees on them. A shorter, refocused version that tests at least one blind configuration would go out to review.

## 2. Scores (1–10)

| Criterion | Score | Reason |
|---|---|---|
| Scope fit | 7 | Sensor placement, identifiability and BWIM on bridges are core SCHM topics; the "control" side is absent, but that is normal for this journal. |
| Novelty | 4 | The identity, the zeros of the uniform-load response, the Sherman–Morrison step and GLS are all classical; the catalogue, $N_M$/$R$ and the Möbius framing are useful but incremental, and Deng et al. [44] already identified net-area cancellation on continuous girders. |
| Technical quality (desk view) | 7 | The derivations are correct and verified, the statistics are honest and out of sample, and the limitations are stated; the deductions are for the tolerance-dependent identifiability argument and the inferred load order in the laboratory. |
| Strength of evidence at structural scale | 3 | No blind locus is tested at any scale; the field data cannot test weight discrimination and do not follow the 1-D model at the gauge level; Cầu Mây has two static readings and only predicted moving-load results. |
| Clarity and length | 4 | Sentences are clear, but the paper is overlong and hedged throughout, makes five contributions plus an error budget plus a workflow, and pushes key evidence into an 11-item supplement. |
| Likelihood of surviving review (as is) | 3 | A BWIM referee will say the field section shows the method does not work; a mechanics referee will say the theory is textbook; a third will ask for the blind configuration to be tested. |

## 3. The five most serious problems, ranked

**1. The central claim, blind loci as a design criterion, is never tested in any experiment.**
The laboratory test uses equal spans, the one configuration far from blindness, and the paper says "the predicted blind configuration (spans of 2500 mm and 3644 mm) was not tested". The field gauges sit about 35 m from the strain zeros. Cầu Mây has no moving-load data.
*Fix:* Test the blind and near-blind configurations on the existing rig. The rig already exists, so the cost is small. Use 2500 + 3644 mm for mid-span deflection, plus a near-blind case such as λ ≈ 1.40, and put a strain gauge in the near-blind band of the equal-span beam. Show the record integral collapsing and the resulting SLM/BPM error growing as predicted by $1/|C|$ and $P_\delta$. Use moving or rolling loads if at all possible. If the Cầu Mây moving-load test (Table 6) has taken place, include it. It would turn the paper.

**2. The novelty is not shown to matter, and the 1-D premise is undercut by the authors' own field data.**
On the five-span box girder, deck-soffit constants vary 3.9-fold between gauges 6 m apart, and they change with the lane. Gauge-level constants are therefore set by slab bending and shear lag, not by the girder moment diagram whose zeros define the blind loci. The paper concedes this ("a beam-model BPM would fail") but does not draw the consequence for its own criteria.
*Fix:* Show, with a 3-D shell or solid FE model of a box girder (Virginia Smart Road or Cầu Mây), that the 1-D blind loci and near-blind bands survive for web or soffit gauges that respond to girder bending, and say where they fail (deck gauges, eccentric lanes). Then state in one paragraph the design decision that an engineer would get wrong without these criteria. A short survey of instrumented continuous girders in the literature, showing how often installed strain gauges fall in $|N_M|<0.2$, would make the case concrete.

**3. The field assessment cannot carry the weight placed on it, and it is over-interpreted.**
The sample is n = 7–8 runs per day and four trucks. Reference weights vary by only a few per cent, so the mean-weight predictor (2.0–2.2 % MAE) beats every estimator. On day 1, speed and truck are confounded (correlation 0.98), and day-1 weights were reported by the drivers. The invariance check has a CI of 0.70–1.37. The headline "GLS from vehicle-free noise is worse than the average" rests on eight runs and one paired CI. It is also an expected outcome once the residual covariance differs from the noise covariance.
*Fix:* Either add a dataset with clearly different reference weights (other public BWIM datasets exist), or cut Section 4 to a compact case study of processing, lane dependence and the noise-versus-residual covariance caution. Drop it from the title. Remove claims such as "consistent with superposition" when both two-truck events fall at 0.92 of the prediction.

**4. The Cầu Mây identifiability result is fragile and incompletely documented.**
It rests on two static peak readings (means of six non-replicate readings across the section). The model-form misfit of 4–9 % is of the same order as the tolerance τ = 5.3 %, which is itself built from an assumed model-form uncertainty of 1.75 %. The conclusion changes with τ: at 3 % the design rigidity is excluded. The best fit implies a 28 % stiffness loss in a recently built girder, which is implausible. The longitudinal truck positions are "given as drawings in the test report and are not tabulated", so a reader cannot reproduce the analysis. The strain-placement advice is left unresolved: Figs. 8b and 8c rank locations in opposite ways.
*Fix:* Tabulate the truck positions. Use the six readings per section with a transverse (grillage or plate) model rather than their mean, or justify averaging. Present the 6.6-fold factor as conditional on τ, and show it as a function of τ in the main text. Resolve the strain recommendation for a stated noise model. Shorten the Cramér–Rao discussion to the one number that matters.

**5. The paper is too long and too defensive, and the laboratory section adds little in its current form.**
The text runs to about 14k words. The Nomenclature has 60 entries, some only for the supplement. There are five contributions, an error budget table whose terms are "not combined", and an eight-step workflow. Section 3 checks a static influence line on equal spans with an inferred load order, so it confirms superposition and nothing more.
*Fix:* Target about 8–9k words. Restructure as theory → blind-configuration experiment → one structural case. Move the GLS/zero-sum material, the Appendix B weighting-function results and most of the error budget to the supplement. Reduce the contributions to the two or three that are genuinely new. Make the figure labels match the text: Fig. 7 still uses "immune" and "immune-eq" for the zero-sum estimators. Fix Fig. 4a, which joins four ρ values with lines and suggests a continuous cliff.

## 4. Conditions before review, and what can wait

**Conditions (all required for the resubmission to go out):**
1. Add an experiment on at least one blind or near-blind configuration (laboratory is acceptable), with the predicted and observed loss of conditioning.
2. Add a 3-D numerical check, or a reasoned argument backed by one example, that the 1-D blind loci apply to the gauge locations the criteria are meant for. Otherwise restrict the claims explicitly to girder-bending channels such as webs and bottom flanges.
3. Cut the length to about 9k words, with a sharpened statement of novelty that concedes the classical parts in one sentence and leads with the design consequence.
4. Recast the field-data section as a limited case study and drop it from the title, unless a dataset with varied weights is added.
5. Supply the Cầu Mây truck positions and state the τ-dependence of the identifiability result in the main text.
6. Clean the cover letter (see Section 5).

**Can wait for reviewers:**
- Choice of the 0.2 threshold and its different meaning for $N_w$ and $N_M$
- Vehicle–bridge interaction beyond the moving-force bound
- Whether frequencies can be used for identifiability (the mode-assignment question)
- Unequal pier stiffness (symmetric pattern not covered by Eq. 15)
- Details of the bootstrap and TOST procedures
- Comparison with the dataset authors' 4.6 % MAE
- Wording of the screening-threshold recommendation
- Reference completeness: other OSP-for-BWIM work and recent influence-line-free GVW methods

## 5. Cover letter: what helps and what hurts

**Helps:**
- The claims are honest. The letter states plainly that the identity and GLS are classical, and it lists the negative results.
- Data availability is stated clearly (CC0 dataset, scripts, logs), and generative-AI use and the conflict of interest are disclosed.
- It cites and distinguishes the recent SCHM paper on deflection influence lines of continuous beams [48], which shows the authors are aware of the journal.

**Hurts:**
- **"[date of submission]" placeholder.** It signals a template, not a finished submission.
- **Addressee.** The letter is addressed to "Lucia Faravelli, Editor". The authors should confirm the current editorial office of SCHM, which has been published as an open-access Wiley journal since 2022, and address the letter accordingly. A wrong addressee is a small but avoidable bad first impression.
- **The letter leads with weakness.** It says the records "cannot test weight discrimination" and that the test "cannot resolve differences smaller than about 27 %". This is honest, but it tells the editor before page one that the evidence is weak. The letter needs a positive statement of what a practitioner gains.
- **Five "new" claims are too many.** Claims 2–3 (indicators, placement at the extremes) will read to referees as corollaries of classical results. The letter should lead with the one or two claims that are really new.
- **Overlap check is not possible.** "Two other papers by the authors are under review at Structures" without titles or manuscript numbers stops the editor from checking overlap. The authors should give them, and preferably upload them as related manuscripts.
- **Terminology lag.** The letter still uses "offset-immune" for what the manuscript now calls zero-sum estimation.

## 6. Reviewer profiles and likely objections

**Proposed reviewers (three, plus one reserve):**
1. **BWIM specialist:** influence-line and NOR-BWIM, field calibration to COST 323 / accuracy classes, ideally with experience of long-span box girders.
2. **Bridge structural mechanics and model updating:** continuous and haunched PSC box girders, balanced-cantilever construction, boundary-condition identification and identifiability (static plus modal).
3. **SHM sensor placement and statistical estimation:** optimal sensor placement, GLS and covariance estimation, uncertainty quantification, cross-validation with small samples.
4. *(Reserve)* **Field displacement and strain measurement on long-span bridges:** GNSS, radar, vision or LVDT reference frames, baseline drift, and temperature effects on zero offsets.

**Most likely objections:**
- *BWIM specialist:* "Every estimator loses to the mean weight, so there is no evidence that integral BWIM works on this bridge. Offsets of 0.1 mm give 16–25 % bias, so why design channels for a method this marginal? The comparison with influence-line BWIM is missing, and influence-line BWIM is not blind."
- *Mechanics reviewer:* "Blind points at moment zeros and the area-equals-uniform-load identity are textbook (Ghali and Neville). The Möbius law is a rank-one update. Where is the new mechanics? The haunch law and pier dimensions are assumed, and an α of 0.716 signals model-form error, not a property of the girder."
- *Estimation reviewer:* "The GLS failure rests on n = 8 and is predictable when Σ is estimated from the wrong population. The placement rule follows trivially from convexity under position-independent noise, which is exactly the assumption the field data contradict. The vertex optimum is not robust to model error in $C(x)$."
- *Measurement reviewer:* "No feasible technology for absolute deflection on a 90 m span over water with δ₀ ≤ 0.05 mm is shown. Temperature-induced drift within a 12–45 s crossing is not quantified."
- *All reviewers:* "Test the blind configuration. The paper is too long. The laboratory test is static on equal spans, and its load order was inferred from the data."
