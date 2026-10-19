# Desk assessment: ASCE Journal of Bridge Engineering (JBE)

**Manuscript (v4):** "Blind loci and design criteria for integral load-monitoring channels on continuous girder bridges, with laboratory verification and an assessment on public field records" (Nguyen, Vu, Nguyen; HUCE)

**Perspective:** Editor of JBE making the desk decision. I assume the paper is reformatted to ASCE style: author-date references, a Practical Applications section and ASCE data-availability wording. Checked on 2026-10-19 against the ASCE Author Center, the JBE editor page and recent JBE papers.

---

## 1. Scope fit: **8 / 10**

**Why it fits**

- JBE's stated scope covers "all aspects of the art and science of bridge engineering", including "inspection, evaluation, safety, performance, management". The current Editor names "monitoring" and "heavier vehicle loads" on ageing bridges as priority topics. Overload screening on continuous girders, and the choice of sensors before installation, sit inside that remit.
- JBE is a home venue for this line of work. The manuscript itself cites five JBE papers: Cardini & DeWolf 2009 (long-term BWIM), Ojio et al. 2016 (contactless BWIM), Zolghadri et al. 2016 (simplified BWIM in the field), He et al. 2019 (virtual-axle BWIM) and Agüero-Barrantes et al. 2023 (influence-area BWIM with Kriging). Recent JBE papers on influence lines of continuous girders are close neighbours, e.g., Wan et al. 2024, "Bending stiffness identification of continuous girder bridges using multiple rotation influence lines" (JBE 29(12)). Displacement-transfer-ratio and smart-bearing monitoring papers have also appeared in 2025–26.
- The deliverable is a design rule that a bridge engineer can use before installing sensors. The paper offers closed-form blind loci, a placement rule, a sensitivity law for pier stiffness and an 8-step workflow. JBE explicitly favours practical papers with a Practical Applications statement.

**Why not higher**

- The core is applied mechanics (closed forms, Möbius law, Fisher/Cramér–Rao bounds) plus signal statistics (GLS, cross-validation). JBE readers will ask, "what does the bridge owner gain?" The paper's own field evidence answers that weakly: no estimator beat the mean-weight predictor, and a 0.1 mm offset gives 16–25 % bias even at the best gauge.
- The SHM and sensor-placement angle gives the paper equally good or better homes elsewhere: SCHM, Structural Health Monitoring, MSSP, J. Civil Struct. Health Monit. and Struct. Infrastruct. Eng.

## 2. Desk decision AS IS

**Decision: return to authors without review / desk reject (in practice). Probability of being sent to review as is: about 15 %.**

Reasons:

1. **Length is about twice the limit.** ASCE caps a Technical Paper at 30 double-spaced pages including references, figures, tables, appendices and captions, which is about 10,000 word-equivalents. The main text has about 14,200 words, including a 60-line nomenclature, 55 references, 9 multi-panel figures, 8 tables and 3 appendices. That comes to roughly 19,000–21,000 word-equivalents. The editorial office normally returns such a file at the technical check, before the Editor sees it.
2. If the length were set aside, I would rate the content as reviewable but unfocused, with roughly 40–45 % chance of review on substance. The paper combines four studies:
   - theory;
   - a statically loaded 2.5 m laboratory tube;
   - a mostly negative reanalysis of a public dataset;
   - an identifiability study of one Vietnamese bridge with two static readings.
   The abstract ends on negative findings: invariance shown only within 10–27 %, no test of weight discrimination, GLS worse than the average, and a factor-6.6 uncertainty. An editor skimming the abstract could fairly ask what positive, validated advance the paper offers.
3. The novelty is carefully hedged ("neither the identity nor the GLS estimator is new"). That honesty is good, but a JBE desk editor needs a crisp statement of what practice can do differently tomorrow, and the current framing hides it.

Combined: (probability of passing the length check, about 0.3) × (probability that the Editor sends it out, about 0.45) gives roughly 15 %.

## 3. AFTER the best reframing (no new experiments): **about 55 % sent to review**

### Article type and length
- **Technical Paper**, at most 30 double-spaced pages including everything, a target of about 9,500 word-equivalents. Plan 6 figures and 4 tables at most. Add a 150–200-word **Practical Applications** section (required by ASCE) and a Notation list at the end in ASCE style, kept to the symbols actually used.
- Do not submit as a Technical Note (7 pages): it is too short for the theory. Do not submit as a Case Study either: the contribution is general, not about one bridge.

### Title (suggested)
"Observability of Gross Vehicle Weight on Continuous Girder Bridges: Blind Loci, Sensor Placement, and Pier-Stiffness Sensitivity for Influence-Area Weigh-in-Motion"

(Alternative: "Where Not to Put the Gauge: Design Criteria for Influence-Area Weigh-in-Motion on Continuous Girder Bridges".)

### Contribution statement (one paragraph, front of the Introduction)
"Influence-area (integral) BWIM is cheap and needs no influence-line calibration, but on continuous girders it can be blind. We give engineers a pre-installation check. (1) Closed-form blind loci and near-blind bands for strain, deflection, rotation, shear and reaction channels on two- and three-span and haunched girders show that every continuous girder has strain-blind zones and that a gauge set back from the pier can fall into them. (2) The paper introduces two indicators that need no reference rigidity: the strain indicator N_M and the cancellation ratio R. (3) A placement rule puts sensors at the extremes of the uniform-load response. (4) A closed-form law shows how the integral constant depends on uncertain pier fixity, and which single extra measurement resolves it. The criteria are applied to a 55 + 90 + 55 m haunched box girder, where they show that the installed side-span deflection gauge cannot be calibrated from acceptance-test data and that a pier tiltmeter would fix this. Public moving-truck records from a 605 m box girder show the limits in the field: lane-specific and gauge-specific constants are needed, and covariances from vehicle-free noise should not be used to combine gauges."

### What to cut or move
- **Move to Supplemental Materials:**
  - Laboratory Section 3. In the main text, keep two sentences and the BPM/SLM result: it checks the identity, which is classical, and is statically loaded.
  - Appendix B: general channels, invariant weighting functions, 981 FE checks (summarise in one sentence).
  - Most of Appendix C (keep Eq. 15 and one sentence of derivation).
  - Fig. 4 (multi-channel gain under the assumed noise model) and Fig. 5 (raw crossings).
  - Tables 6 and 8 (keep a compressed error budget as text plus Table 7).
  - The details of the r87 model-form variants.
- **Compress** Section 4 (NOR-BWIM) to about 1,500 words. Keep one merged figure combining Fig. 6b and Fig. 7a, and Table 3 reduced to 4 rows: best single gauge, average, GLS with measured Σ, mean-weight baseline. Present it as a **field check of the assumptions behind the criteria** (per-lane constants, per-gauge constants, crossing residuals not common-mode), not as a performance assessment. State up front that the dataset cannot test weight discrimination.
- **Cut** the nomenclature table in favour of a short ASCE Notation list. Cut the duplicated statements of the 10–27 % margin, which appear 4 times. Trim the introduction to about 600 words and drop the collapse anecdotes beyond one sentence.
- **Merge** Section 7 (workflow) into the Practical Applications section and a short "Design Procedure" section with a single flow chart or table. JBE reviewers like this.

### What to emphasise
- Lead with the practitioner-relevant positive results:
  - strain gauges near piers or at quarter points can be blind on any continuous girder;
  - a mid-main-span deflection gauge is robust, while a side-span gauge is not;
  - one pier tiltmeter cuts the Cramér–Rao bound on ln C8 from 0.87 to 0.18;
  - the integral ratio of two gauges is a weight-independent discriminator.
- Make the haunched-girder application (Cầu Mây, Section 5) the centrepiece. It is the strongest bridge-engineering content and the closest to JBE's "evaluation/management" remit. Present Table 6 explicitly as predictions for a planned moving-load test.
- Rewrite the abstract so that its last sentences are the design recommendations, not the negative findings.

**Probability of being sent to review after reframing: about 55 % (range 45–65 %).**

## 4. Probability of eventual acceptance (rough)

| Case | P(sent to review) | P(accept, given review) | P(accept, overall) |
|---|---|---|---|
| As is | ~15 % | ~35 % (reviewers would demand major cuts and question the weak field validation) | ~5 % |
| Reframed as above | ~55 % | ~55–60 % after 1–2 rounds of major revision | ~30–33 % |

Likely reviewer objections even after reframing:
1. There is no moving-load validation of the blind loci on a real continuous bridge.
2. The Cầu Mây identifiability rests on two static readings and an assumed depth law.
3. The method's practical accuracy (5–12 % single-crossing error, large offset bias) is weak compared with influence-line BWIM.

Reviewers from the BWIM community (OBrien, Žnidarič or Christenson groups) will push on point 3.

## 5. Three main desk-level risks at JBE

1. **Length and format non-compliance.** The paper is about twice the 30-page or 10,000-word-equivalent limit, and it lacks the Practical Applications section ASCE requires. It also uses a nomenclature table and numbered references. Any one of these triggers a technical return before the Editor reads it.
2. **Perceived lack of a validated, positive engineering advance.**
   - The identity and the GLS estimator are admitted to be classical.
   - The laboratory test is static and does not test the predicted blind configuration.
   - On field records, every estimator lost to the mean-weight predictor and GLS was significantly worse than averaging.
   - The predicted Cầu Mây discriminators are untested.
   An editor may conclude: "theory plus negative results; validation pending the moving-load test; resubmit when you have it."
3. **Scope drift and fragmentation.** The mix of applied mechanics, statistics and SHM sensor design (Fisher information, Möbius law, cross-validation of GLS) reads like SCHM, MSSP or SHM, not JBE. Four loosely linked studies dilute the bridge-engineering message. The editor may redirect it to a monitoring journal or ask the authors to split it.

## 6. Article type, limits and fees

**Article types and limits** (ASCE Author Center; each limit includes references, figures, tables, appendices and captions, double-spaced):

| Type | Limit |
|---|---|
| Technical Paper | ≤ 30 pages (~10,000 word-equivalents) |
| Technical Note | ≤ 7 pages (~3,500 word-equivalents) |
| Case Study | ≤ 30 pages; must have broad implications |
| State-of-the-Art Review | ≤ 45 pages |
| Discussion | ≤ 4 pages |

Other requirements:
- Abstract of 150–175 words is typical for ASCE. The current abstract (about 270 words) must be cut.
- Practical Applications statement of 150–200 words, in plain language.
- Data Availability Statement in ASCE wording.
- Supplemental Materials are allowed and encouraged for data-heavy content: they are hosted online and do not count toward the limit.

**Recommended type:** Technical Paper.

**Fees**
- **Subscription (traditional) route:** no submission fee and no page charges. Colour figures are free online. Colour in print may carry an optional colour charge, so choose online-only colour.
- **Hybrid open access** (optional, after acceptance): APC of **US$3,000 (CC BY)** or **US$2,750 (CC BY-NC-ND)**. Waivers apply mainly to ASCE OPEN, so check whether HUCE or a Vietnamese consortium has a read-and-publish agreement.
- Green OA (self-archiving of the accepted manuscript) is permitted under ASCE policy.

---

**Summary numbers:** scope fit 8/10. As is, about 15 % chance of being sent to review (returned for length or desk rejected) and about 5 % eventual acceptance. After reframing as a 30-page Technical Paper centred on design criteria plus the haunched-girder application, with the lab work and most statistics moved to supplements, about 55 % chance of review and about 30 % eventual acceptance.
