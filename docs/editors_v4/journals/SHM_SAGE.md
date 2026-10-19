# Desk assessment: Structural Health Monitoring: An International Journal (SAGE)

**Manuscript:** "Blind loci and design criteria for integral load-monitoring channels on continuous girder bridges, with laboratory verification and an assessment on public field records" (v4)
**Assessor role:** Editor-in-Chief, desk decision
**Date:** 2026-10-19
**Material read:** manuscript.md (in full), supplementary_material.md (structure and S2–S8 skimmed), Figs. 2, 7 and 9 inspected; the other figures were checked by caption.

---

## 1. Scope fit: 6 / 10

**Why it fits:**
- The aims and scope cover "sensor network design", "monitoring of ... aging structures and infrastructure", "advanced signal processing and interpretation" and "SHM system integration and validation". A method for choosing, before installation, which channel at which position can observe the total load, and how robustly, is a sensor-network design question for civil infrastructure.
- The journal has an active line on bridge influence lines and on static, traffic-induced features. Examples: Cai, Chen and Zhu, "A comprehensive review of bridge influence lines: from identifications to applications in bridge health monitoring" (SHM, 2025, doi:10.1177/14759217251350415); Huang and Lu (SHM, 2025, online first), on an influence-line-integral strain feature, which the manuscript cites as [36]; and Dan and Kong (SHM, 2022/23), on influence-line characteristic functions from monitoring big data. BWIM appears in these papers as an application of influence lines rather than as a core topic.
- The identifiability analysis (Möbius law, admissible set, Cramér–Rao bound for a pier tiltmeter) is the kind of model-based monitoring design that SHM readers value.

**Why it is not higher:**
- SHM's stated preference is for "balanced studies containing both theoretical and experimental aspects" that advance SHM methods. The theory here is closed-form beam statics built openly on a classical identity (influence area = uniform-load response) and on standard GLS. The experiments are thin: a static test on a 25 mm steel tube with weights hung by hand, a public dataset that cannot test weight discrimination, and static acceptance-test readings from one bridge.
- The paper's main subject is gross-weight estimation, a traffic-load measurement problem. Damage assessment and condition monitoring appear only implicitly. The natural homes for the BWIM part are J. Bridge Eng., JCSHM, Struct. Infrastruct. Eng. and Eng. Struct.
- Recent SHM content on bridges leans heavily towards data-driven and vision methods and long-term monitoring systems. A one-dimensional analytical paper will look somewhat old-fashioned to a handling editor.

## 2. Desk decision AS IS

**Decision: borderline. I would most likely desk-reject with a recommendation to transfer (J. Bridge Eng. or JCSHM), or at best send it to one associate editor with low enthusiasm.**

**Probability of being sent to review as is: about 35 %.**

What argues for review: the work is careful and reproducible (981 FE checks, scripts and logs, honest confidence intervals, cross-validated estimators). It names its limitations openly, cites recent work including SHM's own papers, and the figures are of publication quality.

What argues against:
- The title and abstract sell "blind loci" of a classical identity. The abstract then reports mostly negative or inconclusive outcomes: invariance only within 10–27 %, no weight discrimination possible, GLS worse than averaging, a constant uncertain by a factor of 6.6.
- An editor skimming the abstract sees no positive, validated SHM capability.
- The main text runs about 14,000 words, with 9 figures, 8 tables, a two-page nomenclature and three appendices. That is too long for the contribution as framed.

## 3. After the best reframing that needs no new experiments

**Probability of being sent to review: about 55 %.**

**The reframing:**

1. **New framing and title.** Present the paper as a *pre-installation observability and identifiability analysis for load-monitoring sensor networks on continuous bridges*. A possible title: "Observability and identifiability of integral load-monitoring sensors on continuous girder bridges: design criteria, field evidence and an in-service case". "Blind loci" becomes one result, not the headline.
2. **Lead with the SHM contributions, in this order:**
   - (a) The placement rule: optimal sensors lie at the extremes of the uniform-load response, including the section gain for strain.
   - (b) The identifiability law: the constant depends on (α, k) only through κ = k/α and follows a Möbius law. Add the Fisher/Cramér–Rao design of the extra measurement: a pier tiltmeter reduces the bound from 0.87 to 0.18, and identified frequencies reduce it to 0.24.
   - (c) The field lesson for multi-sensor fusion: covariances from vehicle-free windows (correlation 0.90) mispredict the crossing residuals (0.63). GLS and zero-sum fusion therefore fail out of sample, with 20.4 % against 11.9 % MAE. This lesson generalises to any SHM fusion of static channels and should be stated positively.
   - (d) Blind loci and indicators (N_M, R) as the screening tool that feeds (a) and (b).
3. **Rewrite the abstract** around what a monitoring engineer can do with the paper, before installation. Keep every limitation, but move the purely negative numbers (no weight discrimination; every estimator worse than the mean weight) from the abstract to the field-assessment discussion.
4. **Cut to about 9,000–10,000 words:**
   - Move Table 1's lesser channels (shear, reaction), most of Appendix B and Table A.1 to the Supplementary Material.
   - Shorten the laboratory section to one paragraph that verifies the identity, with the full results in the SI.
   - Shrink the nomenclature to the symbols used in the main text.
   - Merge the error budget (Section 6) into the design workflow (Section 7).
5. **Strengthen the in-service section's framing as an SHM design case.** Place the predicted discriminating measurements of Table 6 (integral ratio, pier rotation) in the conclusions as falsifiable predictions for the planned moving-load test.
6. **Use SHM-facing keywords:** sensor placement; identifiability; influence line; bridge weigh-in-motion; continuous bridges; multi-sensor fusion. In the cover letter, cite the 2025 SHM influence-line review and position the work as filling its noted gap on design criteria for influence-line-based monitoring.

## 4. Eventual acceptance (rough)

| Case | P(sent to review) | P(accept, given review) | P(accept overall) |
|---|---|---|---|
| As is | ~35 % | ~40 % | **~14 %** |
| Reframed as above | ~55 % | ~50–55 % | **~28–30 %** |

Reviewers will very likely ask for a moving-load test with trucks of clearly different weights, or a gauge near a predicted blind point. The reframing works partly because it makes such requests less central: the paper's claim becomes design and identifiability, not weighing accuracy. Expect at least one major revision either way.

## 5. Three main desk-level risks for this journal

1. **Novelty seen as textbook statics.** The authors themselves say that neither the identity nor the GLS estimator is new. An editor may judge the closed forms (μ_crit, λ_crit = 1.4574, β_crit = 1.7006) to be classical structural analysis rather than an SHM advance, especially with one-dimensional Euler–Bernoulli models only.
2. **Thin or negative experimental validation for a journal that asks for balanced theory and experiment.** The laboratory test is static, on a 25 mm tube, with the blind configuration untested. The public field data cannot test weight discrimination, and every estimator is worse than the mean-weight predictor. The in-service bridge has only static readings, and the moving test is predicted, not performed. The evidence for the central claim (that the criteria choose good channels) is therefore indirect.
3. **Fit and length.** At about 14k words, dense in notation, the paper is centred on gross-weight estimation rather than condition assessment, so an EiC can easily say "better suited to J. Bridge Eng. / JCSHM / Struct. Infrastruct. Eng." and transfer it. Further minor flags: the disclosed use of generative AI in coding and editing (acceptable under SAGE policy, but it draws attention), an author's consultancy performing the Cầu Mây test (disclosed), and a single public dataset whose gauge calibration factors are unknown.

## 6. Article type, length, fees

- **Article type:** Original Research Article. The journal also publishes Reviews, Letters to the Editor and Book Reviews.
- **Length:** SAGE's author instructions for SHM state **no hard word or page limit**. They require an unstructured abstract, at least 5 keywords, and a "Statements and Declarations" section with all sub-headings: ethical considerations, consent, contributions, funding, competing interests, data availability. Typical SHM research articles run about 7,000–10,000 words, with 10–15 figures and tables. At about 14k words plus appendices, this manuscript is at the long end and invites a "shorten" request. Word or LaTeX are accepted; no template is needed at first submission. Review is single-anonymised, and preprints are allowed.
- **Fees, subscription route:** **no submission or publication charge.** Colour is free online; colour in print is charged at production on request.
- **Fees, open access (Sage Choice, hybrid gold):** optional APC of **about US$4,400 (about £3,230)**, according to a secondary listing; check the current Sage Choice price list before deciding. The charge may be discounted or waived under a Sage Open Access agreement if the corresponding author's institution participates. HUCE (Viet Nam) is probably not covered, but this should be checked at acceptance. Green self-archiving of the accepted manuscript is allowed under Sage's archiving policy.

Sources consulted: SAGE author instructions for SHM (journals.sagepub.com/author-instructions/shm); SAGE journal aims and scope page; recent SHM papers on influence lines (Cai, Chen and Zhu 2025; Huang and Lu 2025; Dan and Kong 2022/23); secondary listing for the Sage Choice APC.
