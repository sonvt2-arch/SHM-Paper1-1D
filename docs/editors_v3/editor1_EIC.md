# Desk assessment (Editor-in-Chief), Structural Control and Health Monitoring

**Manuscript:** Load observability of continuous girder bridges: a general response-integral theorem, optimal offset-immune estimation and field verification (v3)
**Material read:** manuscript/v3/manuscript.md, manuscript/v3/cover_letter_SCHM.md, figures in manuscript/v3/figures/ (Figs 2, 3, 4, 6, 7, 8, 9; Figs 1 and 5 not supplied)

## Decision

**Send to reviewers with conditions.** The conditions are listed under "Conditions before handling" below. The paper is in scope and technically careful. It is not a desk reject. However, three things must be fixed before reviewers are invited: the overlap with the authors' two papers under review at *Structures* must be declared, the novelty claim must be stated precisely, and the manuscript must be shortened.

| Criterion | Score (1–10) |
|---|---|
| Scope fit | **8** |
| Quality (as submitted) | **6** |

## Fit to the journal

This is squarely SCHM material. It covers sensor placement, observability and identifiability, estimator design, signal processing for monitoring records, and field data. It also gives a design workflow (Section 7) that practitioners can use. The journal has published related work on deflection influence lines of continuous girders [49], which the authors cite. One point keeps the fit from scoring higher: the structural-scale evidence covers only strain channels, while most of the design theory (deflection blind loci, the offset-immune pair, the Möbius law, Cầu Mây) concerns deflection channels.

## Strongest points

1. **Useful design framing.** One static analysis under a uniform load gives the integral constant, the blind loci and the optimal positions of every candidate channel. This is directly useful to someone planning BWIM or load monitoring before installation. Table 1 and the workflow in Section 7 are practical.
2. **A finding that matters in practice:** strain channels are blind at every zero of the uniform-load moment diagram. Every continuous girder has such zeros, and a gauge set back from a pier can fall into the near-blind band (Section 2.2, Fig. 3, Fig. 8b). Installers often miss this.
3. **Honest field analysis on an open dataset.** The NOR-BWIM analysis (Section 4) reports noise-expected scatter, a χ² consistency check, lane effects, a superposition check, and a negative result: gauges at one section have constants that differ by up to 2.7 times, which a beam model cannot predict. The limitations are stated openly (Sections 4.4, 7).
4. **Identifiability treated rigorously.** The paper reports an admissible set rather than point calibrations, uses Fisher information and Cramér–Rao bounds, and recommends a measurement (a pier tiltmeter). Few load-monitoring papers do this.
5. **Reproducibility.** The analysis scripts, console output and derived data are supplied, the laboratory data are listed in full, and the closed forms were checked against FE in 981 cases.

## Ranked concerns (location, then the concrete fix)

1. **The novelty against the existing literature is overstated or unclear.** (Abstract; Section 1, paragraphs 3–4; Section 2.1; Section 2.4; cover letter items 1 and 3)
   - The "theorem" in Eq. (2) is classical. The area under an influence line equals the response to a uniform unit load, which is how design codes evaluate distributed lane loads, and it underlies Ojio–Yamada [27] and influence-area BWIM [29, 35, 41].
   - Eq. (13) is the textbook Gauss–Markov estimator. The zero-sum weighted pair is the familiar differential or reference-target measurement, as the authors acknowledge themselves.
   - The convex-on-a-box argument for placement is standard.
   - **Fix:** Rename and reframe the result, for example as a "response-integral identity" or "lemma", and state that it is classical. Claim novelty for what is actually new: the blind-locus catalogue across channel types, the $N_M$/$R$ indicators, the vertex placement rule for the offset-immune estimator, and the Möbius identifiability law. Add a short paragraph or table that compares this work point by point with [35] (sparse-sensing placement for influence-area BWIM), [41] (influence-line-free gross weight on a five-span bridge), [46] (BWIM sensor placement with an augmented Kalman filter) and [38, 39] (integrated influence lines).

2. **The structural-scale evidence does not cover the claims it is cited for.** (Title "field verification"; Sections 3–5; Abstract; Conclusions 4–5)
   - The only moving-load structural test uses strain, on one public dataset, with two axle counts, four trucks and n = 7–8 crossings per day.
   - The field result itself shows that the beam-model constant is unreliable for strain (ratios of 0.68–2.71 against a predicted 0.978–1.003). This undermines BPM and the use of beam-model indicators on box girders.
   - No gauge sat near a blind point, so blindness, the central claim, is untested at any scale. The laboratory blind configuration was not built either.
   - The offset-immune pair, and its assumption that offsets are common-mode, are untested.
   - The Cầu Mây evidence consists of two static readings, and its "measurements that decide" are predictions (Table 5).
   - **Fix:** Either (a) add measured evidence, such as the planned Cầu Mây moving-load test or at least the laboratory blind-configuration test, plus a check of common-mode wander between simultaneous NOR-BWIM channels (the data are in hand); or (b) narrow the title, abstract and conclusions to what is verified. For example, change "field verification" to "verification with public field strain records", and present the deflection and offset-immunity results as theory supported by simulation.

3. **The field statistics are weak for the strength of the claims made.** (Section 4.2, Table 3, Fig. 7, Abstract)
   - The headline ratio of 0.999 ± 0.140 has a 14 % standard error, and the per-gauge CV on day 2 is 34 % (Fig. 7). Agreement within such wide limits is weak evidence of invariance.
   - "Speed-independent" rests on a slope of −3.6 ± 5.8 % per 10 m/s, which is a non-detection rather than a demonstration.
   - **Fix:** Use equivalence tests (TOST) with a stated margin, give the 95 % CI for each result, and phrase the conclusions as "consistent with, at the ±X % level". Put the day-2 MAE of 17.8 % beside the 6.5–7.0 % in the abstract, so that readers see the range of accuracy, not only the best day.

4. **The manuscript is too long and tries to cover too much.** (About 13,200 words, 9 figures, 7 tables plus Table A.1 and Table D.1, five contributions, three verification levels)
   - Sections 2.5 and 5 (identifiability and the Möbius law at Cầu Mây) form almost a second paper.
   - The laboratory section is a small-scale 2.5 m static test, and the paper itself concedes that its invariance evidence is indirect.
   - **Fix:** Aim for about 9,000 words. Shorten Section 3 to a validation paragraph and move the rest to the supplement. Condense Section 5 to the identifiability result, Table 4 and the channel recommendation, and move the frequency interpretation of Section 5.3 and the Cramér–Rao detail to the supplement. Shorten Section 6 by merging Table 7 with the text.

5. **The practical significance is not stated clearly enough.** (Sections 6.2, 6.3, 7)
   - By the paper's own error budget, single-point deflection weighing on long spans is "marginal": a 0.1 mm offset gives 21–25 % bias at the best location.
   - The best field accuracy, about 7 % MAE with SLM, is well below COST 323 classes for BWIM.
   - **Fix:** Add a short "use case" paragraph that states the screening accuracy needed, which existing system it replaces or supplements, its cost, and which of its outcomes were demonstrated rather than projected.

6. **Integrity and administrative items, which block handling.** (Cover letter, paragraph on originality; Conflicts of Interest; Data Availability; Funding)
   - The cover letter mentions two related papers under review at *Structures*. Any shared rig, data or text must be declared, and the papers supplied to the editor.
   - The roles in the Cầu Mây consultancy work must be named in the COI statement.
   - The Cầu Mây data DOI must be given.
   - **Fix:** Complete these before reviewers are invited. Include the related manuscripts as confidential "papers for editor".

7. **Figure quality and consistency.** (Figs 3, 4, 8, 9; Figs 1 and 5 missing)
   - The Fig. 8a title says "indicator of manuscript Eq. 13", but the indicator is now Eq. (10).
   - Fig. 9 uses ρ for the misfit ratio, which clashes with ρ (common-mode fraction) and ρ_L in the Nomenclature. Fig. 9 also lacks the (a)/(b) panel labels that its caption cites.
   - Fig. 4 legends use raw text ("rho=0.0"), and the legend in Fig. 4b overlaps the curves.
   - Fig. 3 writes "Cau May" without diacritics.
   - Fig. 6 uses time on the x-axis while the integrals are given in space. Its peak signals of about 2–4 µε deserve a comment on signal-to-noise.
   - Figs 1 and 5 must be supplied.
   - **Fix:** Regenerate the figures with consistent symbols and panel labels, and use vector output.

8. **Assumptions behind the theory that a reader cannot see.** (Section 2.1, Section 2.4)
   - The theorem's requirements (quasi-static response, re-zeroed record, a single fixed lane, axles following the path) are listed, but the field case violates several of them (lane dependence, wander).
   - The placement proof assumes noise statistics that do not depend on position.
   - **Fix:** Add a short "validity envelope" paragraph that links each assumption to the evidence that it holds in the cases studied.

## Conditions before handling

1. Complete the overlap declaration for the *Structures* submissions, the COI statement and the data DOI (concern 6).
2. Rephrase the novelty claim and add the comparison with [35, 41, 46] (concern 1).
3. Bring the title and abstract into line with the verified scope, and shorten the manuscript towards about 9,000 words (concerns 2 and 4).

## Likely reviewer outcome

**Major revision.** A BWIM or load-identification reviewer will challenge whether the theorem is new and will point out that the deflection-channel theory has no moving-load structural test. An SHM or identification reviewer will probably value Sections 2.5 and 5 but will ask for the Cầu Mây moving-load data or a narrower claim. The likely route to acceptance is one major round with a refocused scope. If neither new data nor narrower claims are provided, rejection after review is possible.

## Letter to the authors (about 150 words)

Dear Dr Vu,

Thank you for submitting your manuscript to *Structural Control and Health Monitoring*. The topic falls within the journal's scope. The design-oriented treatment of blind loci, conditioning and offset-immune placement for load monitoring on continuous girders could be useful to practitioners. Before we send the paper to review, please address the following.

1. Declare fully any overlap with your two manuscripts under review at *Structures*, and complete the conflict-of-interest and data-availability statements.
2. State the novelty precisely. The response-integral identity and the Gauss–Markov estimator are classical. Position your contributions explicitly against influence-area BWIM, influence-line-free weighing and BWIM sensor-placement studies.
3. Align the title, abstract and conclusions with the evidence. The structural-scale verification covers strain channels on one dataset, and the deflection, blindness and offset-immunity claims are not yet tested at structural scale.
4. Shorten the manuscript substantially, moving secondary material to the supplement.

We look forward to the revised submission.

Yours sincerely,
Editor-in-Chief
