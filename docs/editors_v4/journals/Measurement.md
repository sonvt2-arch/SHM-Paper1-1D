# Desk assessment: *Measurement* (Elsevier, journal of IMEKO)

**Manuscript:** "Blind loci and design criteria for integral load-monitoring channels on continuous girder bridges, with laboratory verification and an assessment on public field records" (v4, about 14,200 words in the main text, 9 figures, 8 tables, 3 appendices, plus Supplementary Material)

**Perspective:** Editor-in-Chief, desk stage. Assessed on 2026-10-19 against the journal's current Guide for Authors (Aims and scope, Notes, Article types) and a sample of recent *Measurement* papers on bridge influence lines and weigh-in-motion.

---

## 0. The journal's tests, applied literally

The current Aims and scope adds desk-level notes that are enforced:

1. *"Papers including measurement results that … offer no new insights in an area different from measurement science or technology, do not fall within the scope."* The paper has to advance **how to measure**, not how a bridge behaves.
2. *"The disciplined usage of well-known metrological terms is strongly required … VIM and GUM."*
3. *"The paper must clearly describe the measurement context … by undertaking a critical review of the state-of-the-art of the relevant body of knowledge in instrumentation and measurement and by showing how the research presented advances it."*
4. *"The letter accompanying the submission must describe clearly how the paper satisfies the above requirements."*
5. *Measurement* "is interested in publishing new methods, techniques, procedures, algorithms … that show how to better measure", and the "capability to describe metrological-related details … represents a major difference between papers published by this journal and by other journals publishing papers on similar topics."

Review is double-anonymised.

---

## 1. Scope fit: **5 / 10** as written (7 / 10 is reachable after reframing)

**What fits**
- The subject is an indirect measurement of a physical quantity: the gross vehicle weight, obtained from a record integral divided by a constant. Several items in the stated scope match: "measurement and estimation techniques", "evaluation procedures for performance analysis of measurement systems, processes and algorithms", "mathematical models for measurement-oriented purposes" and "measurement data processing and fusion algorithms" (the GLS and zero-sum combinations).
- The journal does publish in this area. Recent examples:
  - Wang et al., *Bridge influence line identification by load-response spatiotemporal synchronization and KDE-based statistical analysis under long-term monitoring*, Measurement (2025), doi:10.1016/j.measurement.2025.119035
  - Zhang et al., *Extraction of horizontally curved beam influence lines based on a unilateral step-by-step loading inversion algorithm*, Measurement (2025), doi:10.1016/j.measurement.2025.117255
  - Adresi et al., *A review of different types of weigh-in-motion sensors*, Measurement (2023), doi:10.1016/j.measurement.2023.114042
  - Zhou et al., *Vehicle weight identification system … machine vision*, Measurement 159 (2020) 107801
  - Zhang et al., *A review of methods and applications in SHM for bridges*, Measurement 245 (2024) 116575
  - Bernardini et al., *Corrosion detection on steel truss railway bridges using local strain gauges*, Measurement 253 (2025) 117456
  - Zhou et al., *Dynamic load factors from deflection measurements during ambient traffic*, Measurement (2024), doi:10.1016/j.measurement.2024.114245
- Some content already has a measurement-science flavour: the offset-equivalent load $P_\delta$, which is in effect an uncertainty contribution expressed in the units of the measurand; the Cramér–Rao bound on $\ln C_8$; the Fisher-matrix singularity; out-of-sample validation with bootstrap CIs; the finding that vehicle-free noise covariance does not represent crossing-residual covariance; and the Monte Carlo check of the estimator variances.

**What does not fit, as written**
- **The framing is structural engineering.** The title, the keywords ("Structural health monitoring; … Continuous girder") and most of Section 2 (closed-form blind loci from end moments, the three-moment equation, slope-deflection, Möbius law for pier stiffness) belong to structural analysis. The recent *Measurement* bridge papers are centred on an identification or measurement algorithm with an accuracy claim. This manuscript is centred on beam theory.
- **Uncertainty is treated outside the GUM framework, and the paper says so.** Section 6 states that the budget is "indicative, not an evaluation according to the GUM". For this journal that sentence is close to a self-declared desk reject.
- **The paper's own field result is negative for the measuring system.** On both days every estimator was worse than a predictor that returns the mean calibration weight (Table 3), and weight discrimination could not be tested. A measurement journal will ask what the measurement uncertainty of the system is. The paper cannot quote one.
- **The measurement state of the art is thin.** The introduction reviews BWIM and moving-force identification from structural journals. It cites no instrumentation and measurement literature: COST 323 is cited but not used as an accuracy-class framework, and there is no reference to *Measurement*, *MST* or *IEEE TIM* work on WIM uncertainty, the uncertainty of indirect measurements, or optimal experiment design.

---

## 2. Desk decision AS IS

**Decision: Desk reject (out of scope as framed; metrological terminology not in line with VIM and GUM). Authors are encouraged to resubmit a reframed version.**

**Estimated probability of being sent to review as is: about 20 %.**

Reasons an editor would give, in order:

1. **No GUM-consistent uncertainty evaluation.** The paper explicitly disclaims one.
   - The laboratory BPM and SLM deviations of +0.6 % to +1.2 % (Table 2) are reported without uncertainties. The uncertainties of $E$, $I$ (tube wall tolerance), $l$ (with sensitivity 4), the LVDT calibration and the M1 masses are not propagated. A reader cannot tell whether the 1.1 % deviation is significant.
   - The "standard uncertainty of 2.64 % per reading" at Cầu Mây combines transverse-position scatter, which the authors admit is not a repeatability, with an assumed "model-form standard uncertainty of 1.75 %" whose evaluation (Type A or Type B) is not explained.
2. **Metrological vocabulary is loose relative to VIM.**
   - "Calibration A/B" means model updating, not calibration in the VIM 2.39 sense.
   - "Error budget" and "sensitivity budget" are used where VIM and GUM language would be "uncertainty budget" with sensitivity coefficients $c_i$.
   - "Bias", "error", "scatter" and "accuracy" (through MAE) are mixed.
   - The "gain" of a strain channel is not related to the VIM term "sensitivity of a measuring system".
   - The measurand is not defined. It is variously gross weight, total load or $P_\mathrm{tot}$, given in kN, t and % GVW.
   - "Integral constant" plays the role of a calibration coefficient (an instrument constant), but the paper never says so.
   - "Observability" and "identifiability" are used correctly in the systems sense. They are fine.
3. **The contribution is stated as design criteria for a structure, not as an advance in measurement.** None of the five listed contributions is phrased as better measurement of the measurand: lower uncertainty, a traceable calibration route, or a validated measurement model.
4. **The cover letter is written for another journal.** The file in the package is `cover_letter_SCHM.md`. It does not answer the mandatory question of how the paper satisfies the measurement-science requirements.
5. **The manuscript is not anonymised for double-anonymised review.** It carries author names and affiliations, "two of the present authors used …" [37], and a Conflicts of Interest statement that names the author who ran the test. This alone causes a technical return. It is not a scientific reject, but it signals the paper was not prepared for this journal.

Something that softens the decision: the analysis is honest and careful. CIs are given everywhere, out-of-sample testing is used, limitations are stated plainly, and the code is released. An editor who skims Section 4.3 and the identifiability section may see measurement-science value and send it to review against the formal tests. That is where the roughly 20 % comes from.

---

## 3. Probability of review AFTER the best no-new-experiment reframing: **about 45–50 %**

The reframe turns the paper from "where a beam is blind" into **"measurement model, calibration and uncertainty of an integral (influence-area) gross-weight measuring system, with a model-based method for designing channels that are fit for purpose"**. All of it can be done with existing data and scripts.

### 3.1 Title (suggested)
> **Uncertainty-based channel design for integral bridge weigh-in-motion on continuous girders: measurement model, observability limits and evaluation on laboratory and field records**

An alternative: *"Measurement uncertainty and observability of influence-area gross-weight estimation on continuous girders"*.

Keywords: bridge weigh-in-motion; measurement uncertainty; indirect measurement; sensor placement; calibration; observability. Drop "Structural health monitoring" from the first position.

### 3.2 Contribution statement (rewrite Section 1, last paragraphs)
1. A **measurement model** for integral gross-weight measurement, $P = J/C$, with $C$ identified as the calibration coefficient of the measuring system, and two calibration routes: by reference vehicle (SLM, a calibration against a reference standard, the weighed truck) and by model (BPM, a Type B route). The **sensitivity coefficients** of $P$ to every input are derived in closed form.
2. A **condition-number / observability criterion** for channel selection. Blindness ($C\to 0$) is presented as the singular case in which the sensitivity coefficient $\partial P/\partial J = 1/C$ diverges, so the uncertainty contributions of offset, noise and model error grow without bound. The indicators $N_M$, $N_w$ and $R$ are presented as **dimensionless sensitivity measures for design** before installation, and the near-blind band is presented as the region where $u(P)/P$ exceeds a target.
3. **Optimal channel placement and channel combination** as a minimum-variance (Gauss–Markov) measurement design. The new evidence is that the input covariance must be evaluated from calibration-crossing residuals, not vehicle-free noise. This is a genuine measurement-science finding about evaluating correlated input quantities (GUM §5.2). Make it a headline result.
4. **Calibration-coefficient uncertainty under model-parameter uncertainty** (the Möbius law plus Cramér–Rao), presented as the Type B uncertainty of a model-based calibration. This leads to a rule for which additional measurement (a pier tiltmeter, or an integral ratio) minimises the uncertainty of $C$: an optimal-experiment-design result.
5. **Performance evaluation** on laboratory and public field records, with a GUM-consistent uncertainty for the laboratory test and an accuracy-class-style assessment (COST 323 tolerance framework) on the field data, with its statistical limits stated.

Keep the sentence that says neither the identity nor GLS is new. It earns reviewer trust.

### 3.3 Uncertainty treatment (the decisive change; computation only)
- **Rename Section 6 "Measurement uncertainty"** and delete the "not according to GUM" disclaimer.
- **Laboratory (Section 3).** Write the full measurement model and the uncertainty budget table for the BPM estimate.
  - Inputs: $E$ (rectangular, for example ±2.5 %), $I$ (from the wall-thickness tolerance), $l$ (with sensitivity 4), LVDT resolution and calibration, OIML M1 mass MPE converted to standard uncertainty, quadrature error (the known −0.50 % trapezoid bias as a correction with its uncertainty), and support seating.
  - Give the combined standard uncertainty $u_c$, the expanded uncertainty $U$ ($k=2$), and **normalised errors $E_n$** for Table 2.
  - Do the same for SLM, where $E$, $I$ and $l$ cancel. This shows quantitatively why SLM is better, which the paper currently argues only qualitatively.
  - Use GUM Supplement 1 Monte Carlo (the code already has Monte Carlo machinery) to confirm the linearisation.
- **Field (Section 4).** Express the per-crossing scatter as a Type A standard uncertainty of the gauge-average estimator, report $u(P)/P$, and compare it with COST 323 tolerances to state the accuracy class the data can and cannot support. Say explicitly that, with reference weights varying by only a few per cent, the data assess **precision and invariance of the calibration coefficient (reproducibility across trucks and lanes)**, not trueness over the measuring interval. Use the VIM terms: repeatability, intermediate precision, reproducibility conditions, measuring interval.
- **In-service girder (Section 5).** Present the admissible set and the Cramér–Rao bound as the **uncertainty of a model-based calibration coefficient**: $u(\ln C_8)$ = 0.87 with two readings, 0.18 with a tiltmeter. Re-derive the 2.64 % as a properly classified Type B evaluation (state the distributions), or present it openly as an assumed value with a sensitivity study. Do not call position scatter a standard uncertainty of a reading.
- **Offset term.** Present $P_\delta$ as the standard-uncertainty contribution $u_\delta(P) = L_\mathrm{tot}\,u(\delta_0)/C$. Table 7 becomes an uncertainty-contribution table.
- **Terminology pass** (VIM 3 / JCGM 200:2012):
  - "Calibration A/B" becomes "model update A/B" or "parameter set A/B". Reserve "calibration" for the SLM reference-vehicle procedure.
  - "Error budget" becomes "uncertainty budget".
  - "Sensitivity" means $c_i = \partial P/\partial x_i$.
  - Define the measurand once (gross vehicle weight, in kN, or mass in t, not both) and keep "error" for measured value minus reference value.
  - "Gain" becomes "sensitivity of the strain channel".
  - Define the "integral constant" as the calibration coefficient $C$.

### 3.4 What to cut or move (also needed for the length limit)
- **Move to Supplementary Material:** most of Table 1 except strain and deflection; the rotation, shear and reaction closed forms; Appendix A derivations; the asymmetric and haunched detail; the "invariant weighting function" proof of Appendix B (keep one sentence and the result); the Möbius-law derivation (keep Eq. (15) and one line); the speed-truncation remarks. Keep Figs. 1–3 at most as two panels.
- **Cut** the 60-line nomenclature to about 25 symbols, and the long collapse-motivation paragraph.
- **Condense** Section 5.3 (strain placement at Cầu Mây) to one paragraph. Keep Table 6 as "predicted discriminating measurements", stated as optimal-experiment-design output.
- **Target** about 9,000–10,000 words in the main text, 7 figures and 6 tables.
- **Harmonise labels.** Fig. 7 still uses "immune" and "immune-eq" while the text says "zero-sum". Fix this.

### 3.5 Emphasis
- Lead the abstract with the measurement problem: "the uncertainty of integral gross-weight measurement on continuous girders diverges at predictable channel locations; we derive the measurement model and sensitivity coefficients, a pre-installation criterion, and minimum-variance channel designs, and evaluate them …".
- Put the **covariance finding** (vehicle-free noise $\rho=0.90$ against crossing residuals $\rho=0.63$, with GLS significantly worse out of sample) and the **calibration-coefficient identifiability** result (6.6-fold against 1.5-fold) up front. Both are about how to measure, which is exactly what this journal wants.
- Present the negative field outcome as a **validation of the uncertainty model** (the predicted per-crossing SD agrees with the observed one) rather than as "no estimator beat the mean".
- **New cover letter**, written for *Measurement*, with one paragraph answering each of the journal's notes (measurement context, advance over the instrumentation and measurement state of the art, VIM/GUM compliance).
- Add 6–10 measurement references: GUM (JCGM 100:2008) and GUM-S1 (JCGM 101:2008); VIM (JCGM 200:2012); COST 323 used substantively; *Measurement* and *MST* WIM papers (for example Adresi et al. 2023, and the MST 2024 paper on bending and shear strain load measurement); and optimal experiment design and Fisher-information papers on sensor placement.
- **Anonymise the manuscript** and move the conflict-of-interest details to the title page.

With the reframe the paper would pass the formal scope tests, and the desk decision would turn on whether the editor thinks the core is still structural mechanics. That is why the estimate is about 45–50 %, not higher.

---

## 4. Rough probability of eventual acceptance

| Case | P(sent to review) | P(accept, given review) | P(eventual acceptance) |
|---|---|---|---|
| As is | ~20 % | ~25 % (reviewers from instrumentation and measurement will ask for the full GUM treatment and question the field value; likely major revision, then reject or a second major revision) | **~5 %** |
| After the reframing in Section 3 | ~45–50 % | ~40–45 % (likely major revision; the remaining weak points are the field data that cannot test trueness and the static-only laboratory test) | **~18–22 %** |

For reference, the journal's overall acceptance rate is low (on the order of 20 % of submissions), and it reports about 7 days from submission to first decision, which is consistent with heavy desk screening.

---

## 5. Three main desk-level risks for this journal

1. **"Not a contribution to measurement science"** (scope note 1). The core is closed-form structural analysis of influence areas on beams. If the reframe leaves Section 2 dominated by end-moment algebra, the editor will see a structural paper with a measurement wrapper and redirect it to *Struct. Control Health Monit.*, *Eng. Struct.*, *J. Bridge Eng.* or *J. Civ. Struct. Health Monit.*
2. **Misuse or absence of VIM and GUM** (scope note 2). The disclaimer that the budget is not GUM, the unevaluated laboratory uncertainties, "calibration" meaning model updating, and "standard uncertainty" built from non-replicate position scatter are each enough for a desk reject at this journal.
3. **Weak experimental evidence of measurement performance.** The laboratory test is static, has equal spans and only two multi-load configurations, and the blind configuration is untested. The field data are a third-party dataset with near-constant reference weights, where every estimator loses to the mean predictor and day-1 weights are driver-reported, so trueness cannot be demonstrated. For a measurement journal, a measuring method with no demonstrated uncertainty over its measuring interval is a hard sell. Framing it as a design method plus an uncertainty model, validated on precision and invariance, is the only route that needs no new experiment.

Procedural risks with simple fixes: the paper is not anonymised for double-anonymised review; the cover letter is for another journal; and the length is near or over the limit (see Section 6).

---

## 6. Article type, length limits and fees

- **Article type:** Original research paper. (The journal accepts original research papers, reviews and letters, and short communications of at most 3 pages.)
- **Length:** Research papers, reviews and letters must **not exceed 30 pages**. The Guide for Authors does not state a word limit. In practice the 30 pages are judged on the submitted manuscript or on a typeset estimate. At about 14,200 words with 9 figures, 8 tables and 3 appendices, v4 is at or beyond the limit in double-spaced form (roughly 40–50 pages), though inside it typeset (roughly 22–26 pages). Cutting to about 9,000–10,000 words, as proposed in Section 3.4, removes the risk. Supplementary Material does not count.
- **Review model:** Double-anonymised. Prepare a separate title page and an anonymised manuscript.
- **Fees:**
  - **Subscription (hybrid, non-OA) route:** no publication charge. Colour figures appear online at no cost.
  - **Gold open access:** APC **USD 3,480, excluding taxes** (the figure on the journal homepage as of October 2026; "actual APCs may differ based on individual author circumstances"). Check for an Elsevier institutional or national agreement and for Research4Life-type waivers. Viet Nam's eligibility for a waiver or discount should be checked at submission.
- **Timeline (journal's figures):** about 7 days to first decision, 57 days to a decision after review, and 126 days from submission to acceptance. Impact factor 6.1, CiteScore 10.2.

---

*Sources: Measurement Guide for Authors and journal homepage (sciencedirect.com/journal/measurement, accessed 2026-10-19); IMEKO scientific publications page; recent Measurement papers listed in Section 1.*
