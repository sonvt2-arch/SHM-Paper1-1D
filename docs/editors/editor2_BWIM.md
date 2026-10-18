# Associate Editor assessment (BWIM / moving-force / load identification lens)

**Manuscript:** "Total-load observability of continuous girder bridges from a single deflection channel: closed-form blind configurations, laboratory verification and sensor placement on an in-service box girder"
**Journal:** Structural Control and Health Monitoring
**Files assessed:** manuscript/schm/manuscript.md, manuscript/schm/cover_letter_SCHM.md, manuscript/schm/figures/

---

## Decision

**Return to authors before review (unsubmit / technical return). The manuscript is not sent to reviewers in its present form.**

There are two separate reasons.

1. **Administrative.** The submission is incomplete:
   - Unresolved `[NEED VALUE]` placeholders remain in the cover-letter date, the data DOI, the conflict-of-interest statement, the funding statement, the acknowledgements and the accuracy class of the laboratory weights.
   - Most critically, the overlap declaration with **two related papers under review at *Structures*** is still a placeholder. I cannot send a paper to review while possible overlap of rig, data or text is undeclared.
   - The figures folder contains only Figs. 3, 7, 8, 9 and S1. Figs. 1, 2, 4, 5, 6 and 10 are cited in the text but missing.
2. **Substantive.** The contribution sits close to the threshold for SCHM. The core identity is classical. The headline closed forms apply to prismatic beams, which the authors themselves show do not transfer to haunched girders. No moving-load test exists on any continuous structure.

If the authors resubmit with the administrative items resolved and the substantive concerns below at least partly addressed (concerns 1–3 especially), I would send the paper to review. My expectation at that stage would be major revision.

**Novelty score: 4 / 10**
**Technical quality score: 6 / 10.** The derivations are careful and self-consistent, and the limitations are stated honestly. Validation is weak for the claims made.

---

## Strongest points

1. **Clean reciprocity framing.** $C_m = w_q(x_m)/q_0$ (Eq. 3) makes the influence-area calibration constant computable before installation from one static analysis. This is a useful engineering reformulation, even though the identity itself is classical. The authors correctly say so.
2. **Exact blind configurations.** The ratios are exact and verified to round-off against FE: $\rho_L = (3+\sqrt{33})/6$ for two spans, and $\beta_\mathrm{crit} = 1.700594$ with locus end $2\cos(\pi/9)$ for three spans. They give a clear, falsifiable statement of where the influence-area method fails on continuous girders, a failure mode the BWIM literature has largely ignored.
3. **Useful indicators.** The cancellation ratio $R_m$ separates true cancellation from the normalisation effect of haunching (Section 4.3). The offset-equivalent load $P_\varepsilon$ (Eq. 19) is a practical indicator that ties sensor location to the stability of the instrumentation chain. These are the most transferable parts of the paper.
4. **Candid treatment of non-identifiability at Cầu Mây.** Two calibrations fit the same static data but give side-span indicators of 0.18 vs 0.48. The authors present this as a range rather than hiding it. They show that the side-span gauge is ill-conditioned with respect to pier rotational stiffness ($\partial\ln C_m/\partial\ln k = 0.51$), while the centre-span gauge is not ($-0.12$).
5. **Honest error budget.** It identifies the residual zero offset, not noise, as the dominant term, and gives sound processing rules: low-pass, never high-pass, and tight re-zeroing.
6. **Transparent limitations.** The authors repeatedly state that neither the laboratory nor the bridge data validate Eq. (2) under moving loads on a continuous girder.

---

## Ranked concerns

### 1. Novelty relative to influence-area BWIM is incremental; the practical value of the prismatic closed forms is undercut by the paper's own Section 4
**Location:** Abstract; Section 1 (contributions); Sections 2.2–2.3; Section 4.3 (Table 5); Conclusions.

**Problem:**
- The invariance of the response integral is the basis of Ojio–Yamada influence-area BWIM. Its reciprocity form is a textbook Betti/Maxwell result. "The integral is blind where the uniformly loaded structure has zero deflection at the sensor" is therefore a one-line corollary. Any designer can check it with one load case in an existing model.
- The analytically new material is the closed-form location of blind configurations for **prismatic** (or piecewise-prismatic) two- and three-span beams. But medium/long-span continuous box girders are haunched. Section 4 shows the prismatic indicator for the centre-span gauge (0.755) falls to 0.21–0.23 with haunches, and states that the $|N_m| < 0.2$ threshold "does not transfer directly".
- The headline numbers (1.45743, 1.700594, 1.879385) are thus exact for a class of structures for which the influence-area method is least likely to be used. For the structures where the problem matters, the recommended procedure reverts to "run one static FE analysis", which needs no closed form.

**Fix:**
- Reframe the contribution around the observability/conditioning workflow ($C_m$ via Eq. 3, $R_m$, $P_\varepsilon$, sensitivity to pier stiffness) rather than the prismatic constants.
- Demote the closed forms to a benchmark/insight role.
- Provide a parametric study over haunch ratio and $L_v$ showing how the blind locus moves for realistic variable-depth girders. A chart in $(\beta, h_\mathrm{pier}/h_\mathrm{mid})$ would be of real use to practitioners.
- State explicitly what conventional (Moses-type, influence-line-fitting) BWIM loses or does not lose at a blind configuration. A calibrated influence line is not degraded by zero net area, so the problem is specific to the area estimator. The paper should say so clearly so that readers do not infer a general BWIM limitation.

### 2. No moving-load validation on a continuous structure; the field application is not convincing for SCHM
**Location:** Sections 3, 4, 5; Section 7.2.

**Problem:**
- The laboratory loads were statically suspended at 250 mm steps.
- The Cầu Mây data are single peak readings of parked convoys, so Eq. (2) cannot be tested there and only the static model is checked.
- The moving-truck records (Section 5) come from **simply supported** spans with unknown truck weight, speed, lane and channel calibration.
- So none of the data involves a moving load on a continuous girder, which is the subject of the title. "Laboratory verification" means verification of the beam model and quadrature on an equal two-span beam, which is not a blind or near-blind case.
- The falsifiable prediction that the authors themselves propose has not been carried out: the blind rig with spans of 2500 mm and 3644 mm (Section 7.2), and a fixed total load at varying spacings. This is described as needing "no new apparatus".

**Fix (minimum for review):**
- Run the blind/near-blind laboratory configuration and the fixed-load/variable-spacing invariance test. Preferably use a rolling load or cart so that the time-domain processing (speed, baseline, quadrature) is exercised.
- Ideally, add crawl and moving passes of a weighed truck on any continuous span. Even one short two-span overpass would transform the paper.
- Remove Section 5 or move it to the supplement. With undocumented scale factors (0.67–5.15) and 0.1 mm quantisation, it adds length but not evidence.

### 3. Single-sensor, gross-weight claims ignore transverse position, multiple presence and the length of the integration window on long continuous units
**Location:** Section 2.1; Section 4.4 (transverse spread); Section 6.4 (last sentence); Section 7.1 item 5 and final paragraph; Table 10.

**Problem:**
- **Transverse position.** The invariance holds for translation along a fixed line. On a box or multi-girder deck the constant is lane- and transverse-position-dependent. At Cầu Mây the readings across one section spread by up to 2.05 mm in the eccentric case (about 13 % of the mean). This term is absent from the error budget (Table 10), although it is plausibly comparable to or larger than the offset term.
- **Multiple presence.** For a side-span gauge, the integration window must cover the whole 200 m continuous unit plus the vehicle length. At 60 km/h that is roughly 12–13 s of single-vehicle occupancy of a 200 m, two-way deck. On a provincial road with mixed traffic, the fraction of usable isolated crossings could be very small. "Overlapping crossings must be discarded" (Section 6.4) is stated but not quantified.
- **Opposing-lane traffic and temperature drift.** Both act over the same long window, and the offset sensitivity scales with $L_\mathrm{tot}$ (Eq. 19).
- **Strain is the usual BWIM measurand.** The paper notes in passing that a strain sensor is blind at the uniform-load contraflexure points, which "exist on every continuous girder". This is arguably the more important practical finding for BWIM practitioners, yet it gets one paragraph.

**Fix:**
- Add a transverse term to the measurement model and Table 10: lane-specific $C_m$, and $C_m$ as a function of transverse position from a grillage or shell model of the box girder.
- Discuss the multi-sensor sum (summing girders or both webs), as is standard in BWIM.
- Estimate the probability of an isolated crossing for the 200 m unit from a traffic-flow assumption, or restrict the claims to short continuous spans.
- Either develop the strain-sensor case (blind lines, $R_m$ for strain) or explicitly scope the paper to deflection and justify why deflection is preferred despite the much harder baseline problem.

### 4. The bridge-application conclusions are model-dependent and rest on assumed offsets that are not demonstrated
**Location:** Sections 4.2–4.4; Section 6.2 (Table 8); Abstract; Conclusions.

**Problem:**
- **Calibration A** is fitted to the designer's FE output, not to measurements.
- **Inputs are assumed or calibrated rather than known.** The haunch length $L_v$ and the exponent $n$ are assumed, and the pier stiffness $k$ is calibrated.
- **The headline "35–93 % bias at the side-span gauge" depends on an assumed offset.** It comes from an assumed residual offset of 0.05 mm, described as "LVDT class". Yet a 90 m span over water would need non-contact measurement. Section 5 admits that residual offsets of this order "were not demonstrated" on the authors' own channels.
- **The bias magnitudes are therefore scenarios, not findings.** The abstract and conclusions present them as results.
- **Other information was available but not used.** The measured natural frequency of the bridge, which would discriminate between calibrations A and B, is said to be unavailable. Measured-frequency or design-model information could likely be obtained from the owner.

**Fix:**
- Present the Table 8 numbers explicitly as scenario values in the abstract and conclusions.
- Report $P_\varepsilon$ for offsets typical of the non-contact systems that would actually be used (radar interferometry, vision, GNSS), citing values from the literature.
- Make every effort to obtain the pier drawings, the design model or an ambient-vibration frequency to resolve A vs B. Otherwise the main bridge-specific conclusion remains "we cannot tell".

### 5. Laboratory evidence: linearity anomaly, indirect invariance test, weak regression
**Location:** Section 3.3 (ratios 1.010 → 1.016 → 1.017); Fig. 6; Table 4; Section 7.2.

**Problem:**
- The measured-to-analytical ratio increases with load group. The SLM residuals (0.61 %, 0.70 %) are exactly this step, so the reported SLM accuracy is not separable from a possible non-linearity, mass error or position error.
- Three points with different loads *and* spacings cannot test invariance. The authors acknowledge this.
- The order of the three-load group was inferred from fitting the record (Appendix C), which is circular for a validation dataset.
- The weight accuracy class is missing.

**Fix:**
- Repeat with a fixed total load at several spacings and magnitudes.
- Record the load order and positions independently.
- Report the weight certificates.
- Evaluate the Type A uncertainty from the three cycles rather than bounding it.

### 6. Crediting of the integral idea relies on a secondary source
**Location:** Section 1, paragraph 3; Eq. (11) discussion.

**Problem:**
- The influence-area method is attributed to Ojio and Yamada "as described by Cardini and DeWolf [27]". Helmi et al. [28], which the authors cite, attribute the strain-area GVW method to Ojio and Yamada (2002). The primary source should be located and cited.
- The authors should also acknowledge the influence-area BWIM work of Agüero-Barrantes, Lobo-Aguilar and Christenson (see missing references). Their Kriging paper [33] is cited, but their single-span influence-area BWIM paper is not, and that paper addresses sensor number and location, which is directly relevant to the "sensor-placement" framing.
- It should be made clearer that SLM (Eq. 11) *is* the Ojio–Yamada calibration, and BPM is its model-based variant. The manuscript does say this, but the abstract and contributions list still read as if the estimator itself were proposed here.

**Fix:** Cite the primary Ojio–Yamada source. Add the references below. Tighten the contributions list so that only the closed forms, indicators and conditioning analysis are claimed as new.

### 7. Dynamic validity is bounded with a constant force only
**Location:** Section 6.5; Eq. (21); Table 10.

**Problem:**
- The dynamic study omits vehicle–bridge interaction, suspension bounce and road roughness. It is performed on the laboratory beam, not at bridge scale.
- On a near-blind gauge the net integral is a small difference of large lobes, so dynamic effects that differ between the instrumented and adjacent spans are amplified relative to the net signal by roughly $1/R_m$. This amplification is not analysed.

**Fix:**
- Run a VBI simulation (a two-axle sprung vehicle with ISO roughness classes) on the Cầu Mây model or a prismatic three-span model.
- Report the integral error as a function of $R_m$ to show how cancellation amplifies dynamic and offset errors.

### 8. Length and focus
**Location:** whole manuscript (~15,500 words, 10 tables, 10 figures, 4 appendices).

**Problem:** The paper is too long for the contribution. Section 5 (supporting role only), the matched-filter index $O_m$ (Eq. 15), the extensive quadrature discussion and parts of Section 6.3 dilute the message.

**Fix:** Target about 9,000 words. Move Section 5, the Monte Carlo detail and the quadrature detail to the supplement.

### 9. Speed estimation proposal untested
**Location:** Section 6.4.

**Problem:** The interior zero-crossing speed method is proposed "without having tested it", while speed is identified as "likely the largest single field contributor".

**Fix:** Test it in the moving-load laboratory runs requested above, or remove it from the recommendations (Section 7.1, item 9).

---

## Missing references (verified)

1. P. Agüero-Barrantes, S. Lobo-Aguilar, R.E. Christenson, Sparse sensing Bridge Weigh-In-Motion for single-span bridges, *Métodos & Materiales* 11 (2021) 43–53. https://doi.org/10.15517/mym.v11i0.46400
   - Influence-area BWIM from strain time histories, with explicit study of sensor number and location. Directly relevant to the influence-area credit and to the sensor-placement framing.
2. H. Wu, H. Zhao, J. Liu, Z. Hu, A filtering-based bridge weigh-in-motion system on a continuous multi-girder bridge considering the influence lines of different lanes, *Front. Struct. Civ. Eng.* 14 (5) (2020) 1232–1246. https://doi.org/10.1007/s11709-020-0653-0
   - BWIM on a **continuous** bridge, showing that lane-specific influence lines are needed. Relevant to the transverse-position concern and to the claim that the continuous-girder case is unaddressed.

**Not verified, but the authors should locate it:** the primary Ojio & Yamada (2002) influence-area paper, cited secondhand via [27]. Helmi et al. [28] attribute the strain-area GVW method to Ojio and Yamada (2002). I could not confirm its exact bibliographic details.

---

## Note to the authors (about 150 words)

Thank you for submitting to SCHM. The reciprocity reading of the influence-area constant, the exact blind configurations and the indicators $R_m$ and $P_\varepsilon$ are clearly presented and could be useful to monitoring engineers. Before the manuscript can go to review, please resolve all placeholders and supply the missing figures (1, 2, 4, 5, 6 and 10). Please also declare precisely any overlap with your two papers under review at *Structures*.

On substance:
- The closed forms are exact only for prismatic beams. Your own box-girder analysis shows that they do not transfer to haunched girders, so please reframe the contribution around the conditioning workflow.
- No moving load has yet been tested on a continuous structure. The blind-configuration and variable-spacing tests you propose on your existing rig are essential.
- Please quantify transverse position, multiple presence over long integration windows, and realistic non-contact baseline offsets.
- Please cite the primary Ojio–Yamada source and related influence-area BWIM work.

A focused, shorter manuscript addressing these points would be welcome.
