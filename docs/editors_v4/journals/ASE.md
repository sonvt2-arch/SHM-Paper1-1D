# Desk assessment: Advances in Structural Engineering (SAGE)

**Manuscript:** "Blind loci and design criteria for integral load-monitoring channels on continuous girder bridges, with laboratory verification and an assessment on public field records" (v4)
**Assessor role:** Editor-in-Chief, desk decision
**Date:** 19 October 2026

Sources checked: ASE aims & scope and submission guidelines (journals.sagepub.com/author-instructions/ase, version of Dec 2025); Sage Choice 2026 hybrid APC list (sagepub.com); recent ASE papers on BWIM / influence lines (listed in Section 1).

---

## 1. Scope fit: 8 / 10

**Why it fits**

- ASE's stated mission is "cutting-edge research on civil engineering structures (e.g. bridges ...)". Its listed focus area (f) is **"Structural health monitoring for performance assessment"**. A paper on how to design load-monitoring channels for continuous girder bridges belongs squarely in (f), and the identifiability part touches (e), life-cycle structural engineering (load knowledge for assessment).
- ASE has a steady, if small, line of BWIM and influence-line papers that this manuscript can cite and speak to:
  - Yu, Cai & Deng (2016), *State-of-the-art review on bridge weigh-in-motion technology*, ASE 19(9) (already cited as [12]);
  - Hao, Xie & Yu (2019), *The identification technology of vehicle weight based on bridge strain time-history curve*, ASE (simply supported and continuous beam model tests);
  - Zuo, He & Ren (2019), *Vehicle weight identification for a bridge with multi-T-girders based on load transverse distribution coefficient*, ASE 22(16);
  - Lin, Du, Yi & Yang (2022), *Influence lines-based model updating of suspension bridges considering boundary conditions*, ASE 26(2). This is directly relevant to Section 5 (boundary stiffness identifiability) and is not cited;
  - Wang, Zhang, Pan, He & Ren (2025/2026), *Deflection influence line identification under moving vehicle based on VMD and B-spline basis function*, ASE;
  - SHM implementation papers such as Zhu, Ren & Wang (2022, Yangluo Bridge) and Zhang et al. (2021, vehicle re-identification for bridge load monitoring).
- The paper's mix of closed-form mechanics, FE checks, a laboratory test and field data is the kind of package ASE reviewers are used to.

**Why not 9–10**

- The strongest BWIM and moving-load work goes to J. Bridge Eng., Struct. Infrastruct. Eng., MSSP, SHM and SCHM. In ASE, BWIM is a niche topic of roughly one or two papers a year, so the reviewer pool is thinner and less specialised.
- The content is measurement theory: observability, estimator variance, Cramér–Rao bounds and identifiability. ASE's readership is structural engineers who expect a structural-engineering payoff, and the manuscript's own conclusion is that integral weighing is "marginal" for long spans. The structural takeaway (where to put gauges on a continuous girder, and why side-span gauges fail) has to be pulled out explicitly.
- Gross-weight-only influence-area weighing is a minor branch of BWIM. A generalist editor will ask who uses it.

---

## 2. Desk decision for the paper AS IS

**Decision: Return to author (technical non-compliance), and on content alone borderline for review.**

**Probability that it is sent to review as is: ~20 %**

Reasons:

1. **Length is far over the limit.** The ASE limit is 12,000 word-equivalents (words + 300 × figures + 300 × tables). By my count:
   - the text is about 14,240 words, including ~1,400 words of references, ~850 words of nomenclature and ~600 words of captions;
   - there are 9 figures (+2,700) and 9 tables, Tables 1–8 and A.1 (+2,700);
   - the total is about **19,600 word-equivalents, 63 % over the limit**. Even without the references and back matter it is about 17,000.
   The editorial office normally unsubmits a manuscript like this before an editor sees it. I put the chance of that happening at about 80 %.
2. **The abstract (~250 words, against ASE's ~150) leads with negative results.** It says invariance "could be shown only within margins of 10–27 %", the reference weights "did not allow weight discrimination to be tested", GLS "performed worse out of sample", and one constant is "uncertain by a factor of 6.6". An editor triaging an ASE submission reads this as "the method was not validated". The positive contributions (the blind-locus catalogue, the placement rule, the Möbius law) are buried.
3. **The paper reads as several papers in one:** five contributions, three datasets (lab, NOR-BWIM, Cầu Mây), about 70 nomenclature entries and an eight-step workflow.

If the length problem were ignored and the paper judged on content only, I would send it to review with probability ~40 %. With the near-certain length return, the overall figure is about 20 %. That assumes the authors fix only the length on resubmission, not the framing.

---

## 3. Probability sent to review AFTER the best reframing (no new experiments): ~60 %

### The reframing

**Reposition the paper as a sensor-layout and observability paper for SHM of continuous girder bridges, compliant with the ≤ 12,000 word-equivalent limit.** It should no longer read as a weigh-in-motion method paper that partly fails in the field.

1. **New title** (short and searchable), for example: *"Where not to put the gauge: observability and boundary-condition identifiability of influence-area load-monitoring channels on continuous girder bridges."* A plainer alternative: *"Observability criteria for influence-area load monitoring of continuous girder bridges."*
2. **Abstract of ~150–180 words.** Lead with the design results:
   - blind loci of five channel types in closed form;
   - the near-blind band for strain gauges set back from piers;
   - the extreme-of-uniform-load-response placement rule;
   - the Möbius law and the pier tiltmeter as the deciding measurement.
   Then one sentence each for the verification: lab identity check ~1 %; field invariance consistent with Eq. (2); a cautionary finding that vehicle-free covariance misleads multi-channel weighting. Then one sentence on the in-service girder: the side-span gauge is not identifiable from static acceptance data, while the main-span gauge is.
3. **Restructure around one storyline: theory → verification → design application.**
   - Section 2, theory: keep it, but move Eq. (14) and the zero-sum variance details, the weighting-function argument, the Table A.1 detail and Appendix B to the Supplement.
   - Section 3, laboratory: compress to ~400 words and fold Table 2 into the text.
   - Section 4, public field records: cut to ~1,200 words, presented as *verification of the identity's assumptions and of the noise model*. Keep the invariance result (Fig. 6b), the lane and gauge findings, and the vehicle-free versus crossing-residual correlation finding (0.90 vs 0.63) as the transferable lesson. Move most of Table 3 and Fig. 7 to the Supplement, keeping one compact table of the LOO MAE for average, GLS and best gauge. **Drop the "every estimator worse than mean-weight predictor" headline from the main text.** Keep the honest statement that weight discrimination was not testable.
   - Section 5, Cầu Mây: make it the worked design case and the strongest section. Keep Tables 4–6 merged into one or two tables and Figs. 8–9.
   - Sections 6–7: merge into a ~800-word "Design implications and limitations" section. Move Tables 7 and 8 to the Supplement and keep the 0.1 mm → 16–25 % sentence.
4. **Trim nomenclature** to essential symbols, or drop it and define symbols in the text, which is common in ASE. Use 7 figures (merge Figs. 1 and 3, and move Fig. 4 or Fig. 5 to the Supplement) and 4–5 tables.
5. **Target:** ~7,500 words of text including references, plus 7 figures and 5 tables, ≈ 11,100 word-equivalents.
6. **Cite and position against ASE's own literature:** Yu et al. 2016, Hao et al. 2019, Zuo et al. 2019, Lin et al. 2022 (boundary conditions in IL updating) and Wang et al. 2025. Add the Cai, Chen & Zhu (2025, SHM) influence-line review.
7. **Replace the cover letter.** The current one is addressed to SCHM. The new one should state the structural-engineering payoff for ASE readers: practical gauge-placement rules for continuous and haunched girders, and a warning about side-span deflection gauges near pier-stiffness-sensitive layouts.

This needs no new experiments. It is editing and relocating material, roughly a 40 % cut.

**Probability sent to review after this reframing: ~60 %.** It is not higher because of the residual risks in Section 5 below: the niche topic, limited validation, and the "classical identity" admission.

---

## 4. Probability of eventual acceptance

| Case | P(sent to review) | P(accept, given review) | P(eventual acceptance, overall) |
|---|---|---|---|
| As is | ~20 % | ~25 % | **~5 %** |
| After best reframing | ~60 % | ~45 % | **~27 % (≈ 25–30 %)** |

Notes:

- Conditional on review, the theory is clean and heavily verified: 981 FE checks, the reproducible scripts are supplied, and the limitations are stated honestly. Most ASE reviewers would recommend major revision rather than reject.
- The main reviewer-stage risk is a request for a moving-load validation with trucks of clearly different weights, or for the designed Cầu Mây moving test. The authors cannot meet that without new experiments.
- The as-is conditional figure is lower because reviewers would also ask for shortening and focus, and fatigue with a 20k-word-equivalent manuscript raises the rejection rate.

---

## 5. The three main desk-level risks for ASE

1. **Length, format and density non-compliance.** At ~19,600 word-equivalents against the 12,000 limit, the abstract is ~250 words against ~150. About 70 symbols, five contributions and three datasets make it read like a monograph. This alone triggers unsubmission, and if it is only trimmed rather than refocused, the editor still sees a diffuse paper.
2. **Validation reads as weak or negative.** Specifically:
   - the laboratory test is static and small, with 2–3 load groups, the load order inferred from the data, and the blind configuration untested;
   - the field data are third-party, with near-constant reference weights, so no weight discrimination is possible and every estimator loses to the mean-weight predictor;
   - the in-service bridge has only two static readings, and the moving-load test is "designed, not performed".
   ASE editors routinely desk-reject when "experimental verification" does not demonstrate that the proposed approach works.
3. **Novelty perceived as incremental or niche.** The authors themselves say the influence-area identity is classical and GLS is standard, and that the contribution is "criteria". Gross-weight-only integral weighing is a minor branch of BWIM. A generalist ASE editor may judge the advance as derivative of textbook continuous-beam analysis (Eqs. 4–9) and not of "significant current interest" to structural engineers, or redirect it to a specialist BWIM, SHM or measurement journal (JBE, SIE, SCHM, Measurement).

Secondary issues for the editorial office:

- The cover letter is addressed to the wrong journal (SCHM).
- A local-language source [37] is cited.
- COI: the Cầu Mây data come from an author's consultancy work. This is declared, which is acceptable.
- AI-use disclosure is present, which is acceptable under Sage policy.

---

## 6. Article type, length limits and fees

**Article type:** Original Research Article (Research Paper). A Technical Note is not suitable: the limit is 5,000 word-equivalents in the current guidelines, and older SAGE pages quote 3,000, so the material would not fit. The paper is not a "New Technology Technical Note" either.

**Length:**

- Research papers should not normally exceed **12,000 word-equivalents**, counted as words in the word processor + 300 × each figure + 300 × each table.
- The abstract should be unstructured, about **150 words**.
- **4–8 keywords** are required, minimum 4.
- Word or LaTeX is accepted, with no template required.
- Peer review is single-anonymised.
- Preprints are accepted.

**Fees:**

- **Subscription (standard) route: no submission or publication charges.** Colour figures are free online. Colour in print is charged if requested, but this is unnecessary.
- **Open access (Sage Choice, hybrid): APC USD 4,440 (≈ GBP 3,256)** on Sage's 2026 Sage Choice price list. Authors can choose it only after acceptance. Fees may be discounted or waived under an institutional Sage Open Access agreement matching the corresponding author's affiliation at acceptance. HUCE is unlikely to be covered, so the authors should check with the library.
- ASE is not a gold-OA journal. The subscription route at zero cost is the realistic choice.

---

### Bottom line

The paper is in scope (8/10), but as submitted it would bounce on length and would likely be desk-rejected on framing (~20 % chance of review, ~5 % eventual acceptance). Cutting it to ≤ 12k word-equivalents and recasting it as an SHM sensor-layout and identifiability paper, with the field records presented as verification of assumptions plus a cautionary finding, raises this to ~60 % chance of review and ~25–30 % eventual acceptance, with no new experiments.
