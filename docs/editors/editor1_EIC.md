# Desk assessment: Editor-in-Chief, Structural Control and Health Monitoring

**Manuscript:** "Total-load observability of continuous girder bridges from a single deflection channel: closed-form blind configurations, laboratory verification and sensor placement on an in-service box girder"
**Material read:** `manuscript/schm/manuscript.md`, `manuscript/schm/cover_letter_SCHM.md`, figures in `manuscript/schm/figures/` (Fig3, Fig7, Fig8, Fig9, FigS1 PNGs).
**Date of assessment:** 2026-10-18

---

## Decision

**Send to reviewers, with conditions.** The paper goes out once conditions C1–C4 below are met at the pre-review stage. It is not a desk reject. The topic fits SCHM, the theory is correct and self-consistent, and the paper is unusually honest about its own limits. Still, the evidence at structural scale is thin, the novelty case is fragile, and the manuscript is far too long. Without the conditions, I expect a "major revision / reject" split from reviewers.

Pre-review conditions:
- **C1.** Complete the overlap declaration in the cover letter (two related papers under review at *Structures*). State whether they share the rig, the data, the derivations or any text, and upload them as "related manuscripts". This is the one placeholder that blocks handling.
- **C2.** Supply every figure the text cites. Figs. 1, 2 and 10 are computed figures, not laboratory figures, and they are not in the submission folder. Figs. 4–6 (lab) are also needed.
- **C3.** Cut the manuscript to about 9,000–10,000 words of main text (currently about 15,500 words including appendices). Move the material listed under Concern 5 to the supplement.
- **C4.** Complete the conflict-of-interest statement: the Cầu Mây load test was a commercial job by the authors' consultancy.

## Scores

| Criterion | Score (1–10) |
|---|---|
| Fit with SCHM scope | **7** |
| Quality (as submitted) | **6** |

Fit: the paper deals with sensor placement and observability for a monitoring channel, plus a measurement-error analysis, which is core SCHM ground (sensor technology, signal processing, SHM theory). It loses points because the structural content is textbook continuous-beam analysis, and part of it would sit as well in *J. Bridge Eng.* or *JCSHM*.
Quality: the derivations are careful, the verification is excellent and the limitations are disclosed with rigour. It loses points because no moving-load or continuous-girder validation exists for the central claim, the field case ends in non-identifiability, and the paper is bloated.

---

## Three strongest points

1. **A clear, useful reframing.** The paper takes influence-area BWIM and turns it into a sensor-placement question that comes before any choice of algorithm. Eq. (3) gives $C_m = w_q(x_m)/q_0$, so observability can be checked before installation from one static analysis. The strain corollary in Sec. 2.1 (a strain sensor is blind at the contraflexure points of the uniform-load moment diagram) is short and practically important.
2. **Exact, checkable results with full verification.** The blind ratios $(3+\sqrt{33})/6$, $\beta_\mathrm{crit} = 1.700594$ and $2\cos(\pi/9)$, plus the optimum $\xi^*$, are in closed form and FE-verified (Tables 1–2, App. D). The observability maps (Fig. 3) are clean and usable as design charts. The three indicators ($N_m$, $R_m$, $P_\varepsilon$) give practitioners actual numbers.
3. **Honest error analysis with a practical lesson.** The paper shows that residual zero offset, not noise, dominates, and that $P_\varepsilon$ grows sharply at ill-conditioned gauges (Table 8). The finding that $R_m$ separates true cancellation from haunch stiffening (Sec. 4.3, FigS1) is a real insight. The authors also show that the prismatic threshold $|N_m|<0.2$ does not carry over to haunched girders. Limitations are stated plainly throughout.

---

## Main concerns, ranked

### 1. The central claim is not validated at structural scale or under moving load
*Location:* Sec. 1, last contribution paragraph; Sec. 3 intro ("tests the identities ... not the scale"); Sec. 4 intro; Sec. 7.2; Abstract.
The only experiment is a 2 × 2.5 m steel tube with weights hung statically at 250 mm steps, and it uses equal spans, which is the case furthest from blindness. The paper's distinctive prediction, the blind configuration, is never tested; the authors call it "a falsifiable prediction" that "has not yet been carried out". The bridge data are parked convoys, so they cannot test Eq. (2). Sec. 5 uses simply supported spans. As a result, nothing in the paper tests total-load observability on a continuous structure under a moving load.
*Fix:* (a) Run the blind and near-blind rig tests the paper already proposes: spans 2500/3644 mm, plus fixed total load at several spacings and magnitudes. This needs no new apparatus, and it would turn "falsifiable" into "confirmed". (b) Ideally add a rolling or crawl test on the rig, or on any continuous girder with a weighed vehicle. (c) If neither is possible, the title and abstract must say "theory and static verification", and "laboratory verification" must not imply anything about moving traffic.

### 2. The novelty case is fragile and the headline results are prismatic
*Location:* Sec. 1, paragraphs 3–5 ("the identity itself is classical ... This result is the foundation, not the headline"); Sec. 2.2–2.3; Sec. 4.3 ("does not transfer directly to haunched girders").
The invariance is the Ojio–Yamada influence-area idea, the reciprocity identity is textbook, and the closed forms are three-moment-equation algebra. The novelty therefore rests on (i) the observability framing and (ii) the blind loci. Yet the paper's own field case shows that the closed forms and the 0.2 threshold do not apply to the haunched box girder that motivates them, where everything comes from a numerical model anyway. Reviewers will ask what the closed forms add over "compute $w_q$ at the sensor with any FE model".
*Fix:* State the contribution as the observability criterion and indicators (computed by Eq. (3) for any $EI(x)$), with the prismatic closed forms as benchmark cases and design charts. Add a short, explicit comparison with OSP-for-BWIM [40], multi-point deflection identification [41], and the influence-area BWIM field literature [27–29,34]: what each needs, and what the single-channel criterion gives that they do not. Extend the threshold to non-prismatic girders, for example a threshold on $R_m$, or $N_m$ with a declared $EI_\mathrm{ref}$ for typical haunch laws, so the criterion is usable on the structures it targets.

### 3. The field case ends in non-identifiability, and its strongest practical claim is generalised from one bridge
*Location:* Sec. 4.2–4.4; Table 5; Abstract ("index of 0.18 or 0.48"); Sec. 7.1 item 5 and Sec. 8 ("never from the design model").
Two calibrations fit the two static readings equally well, so the side-span result is a range spanning poor to reasonable conditioning. The depth law $L_v$ is assumed, and pier stiffness is unknown. The conclusion that side-span gauges "need $C_m$ from an in-situ identified model ... never from the design model" rests on one bridge, two readings and an unresolved trade-off.
*Fix:* Discriminate between calibrations A and B with independent data: an ambient-vibration test (one day, a few accelerometers) giving $f_1$ and $f_2$, or the pier drawings or the designer's model. Otherwise, add a parametric study over a population of three-span layouts and pier stiffnesses, showing that side-span ill-conditioning holds in general. Soften "never" to "should not be relied on unless the pier stiffness is identified".

### 4. Section 5 field records add little and contain anomalies
*Location:* Sec. 5; Figs. 8–9.
The records come from simply supported bridges, with unknown truck weight, speed and lane, undocumented channel scale factors (processed/raw ratio 0.67–5.15) and hand processing. The authors concede that the assumed residual offsets "were therefore not demonstrated". In Fig. 9 the Phuong Do N1 panel shows a negative deflection of about −2.8 mm (about 40 % of the peak) between 4.5 and 5.5 s on a span described as simply supported. That is physically unexpected and unexplained. The Gie Cuc N2/N3 residual panels are dominated by 0.1 mm quantisation saw-tooth, and the N1 panel shows a second event starting at the end of the window.
*Fix:* Either cut Sec. 5 to one paragraph and move Figs. 8–9 to the supplement, or explain the negative lobe (sensor/channel artefact, adjacent-span coupling, second vehicle) and show which baseline choices it affects. The two operational rules (tight re-zeroing; low-pass, never high-pass) can be shown on synthetic records.

### 5. Length, over-precision and structure
*Location:* whole manuscript; Tables 1–2, 9–10, B.1; Sec. 2.4 (Eq. 15), Sec. 6.1–6.6; App. B, D.
About 15.5k words, 10 figures, 10 tables plus appendix tables and four appendices. Numbers are reported to 6–11 significant figures (1.621399, 1.879385, "agree to eleven significant figures"), which signals algebra rather than engineering. The main thread (criterion → lab → bridge → recommendations) is buried under the quadrature, Monte Carlo, matched-filter ($O_m$) and speed-calibration side topics.
*Fix:* Move App. B, App. D, the $O_m$ index, the quadrature discussion beyond one paragraph, Sec. 6.3–6.4 and most of Sec. 5 to the supplement. Report ratios to 3–4 significant figures in the text, with exact forms in the equations. Shorten the title, for example "Total-load observability of continuous girder bridges from a single deflection sensor".

### 6. The error budget and the abstract's headline biases are scenarios, not measurements
*Location:* Abstract (35–93 %, 10–11 %); Sec. 6.2, Table 8; Sec. 6.6, Table 10.
A residual offset of 0.05 mm is assumed at LVDT class. The authors note that a 90 m span over water would use non-contact sensing, whose offset is unknown. The abstract quotes the resulting biases as if they were findings.
*Fix:* Label them in the abstract as "for an assumed residual offset of 0.05 mm". Give $P_\varepsilon$ for realistic offsets of the non-contact techniques actually used on such spans (GNSS, radar interferometry, vision), citing measured stability values.

### 7. The practical role of deflection versus strain sensing is under-discussed
*Location:* Sec. 2.1, final paragraph; Sec. 7.1.
Most BWIM installations use strain. The paper shows that strain sensors have unavoidable blind points on every continuous girder, which arguably matters more to practice than the deflection blind ratios, yet it gives this one paragraph.
*Fix:* Add a short subsection or figure giving the strain counterpart of $N_m$ and $R_m$ for the two- and three-span cases, or justify why deflection is the target channel (absolute deflection is hard to measure on long spans).

### 8. Placeholders and declarations that matter
*Location:* cover letter (overlap with *Structures* submissions); Conflicts of Interest; Data Availability DOI; Sec. 7.2 (accuracy class of weights).
The overlap statement is critical (duplicate-publication screening), and so is the COI wording. The weight accuracy class bears on the 0.6–0.7 % SLM claim, because a reference-weight uncertainty of the same order would make that claim meaningless. Fill these before review.

---

## Sentences that would trigger rejection (as written)

- Sec. 1: "the identity itself is classical, and we did not find it used in this way in the BWIM literature we reviewed. This result is the foundation, not the headline." This invites "no novelty"; rephrase positively and cite precisely.
- Sec. 1: "It is not a validation of the integral identity on a continuous bridge, because no crossing record exists for that structure." Honest, but combined with Sec. 3 it means the core claim is never tested on a continuous structure under moving load.
- Sec. 3: "The laboratory beam therefore tests the identities and the estimators, not the scale." A reviewer will reply that dimensionless identities are already verified by FE to 1e-11, so the lab adds nothing.
- Sec. 7.2: "the predicted blind configuration ... is a falsifiable prediction; neither has yet been carried out." This tells the reviewer the decisive experiment was available and skipped.
- Sec. 4.3: "The observability of the side-span gauge cannot be identified from the design data and the two static readings." The bridge case then reads as inconclusive.
- Sec. 5: "Residual offsets of a few hundredths of a millimetre, as assumed in Section 6, were therefore not demonstrated on these channels." This undercuts Table 8 and the abstract numbers.
- Sec. 6.4: "We propose, without having tested it, ..." Untested proposals belong in outlook, not the method.
- Sec. 1: "neither source we could consult states whether the instrumented span was continuous." This suggests incomplete literature access; consult the primary sources or drop the clause.
- Sec. 2.2: "the two agree to eleven significant figures." This verifies algebra, not engineering; it invites "trivial".
- Sec. 4.4 / Sec. 8: "never from the design model." This generalises from one bridge with an unresolved calibration.

---

## Letter to the authors (about 150 words)

Dear Dr Vu,

Thank you for submitting your manuscript to *Structural Control and Health Monitoring*. Its framing of influence-area weighing as a sensor-placement and observability question fits the journal's scope, and the closed-form blind configurations and indicators are clearly presented. Before I send it to reviewers, please (1) complete the cover-letter statement on overlap with your two manuscripts under review at *Structures* and upload them; (2) supply all cited figures (Figs. 1, 2, 4–6 and 10 are missing); (3) complete the conflict-of-interest statement on the Cầu Mây test; and (4) reduce the main text to about 10,000 words by moving secondary analyses to the supplement. Reviewers will likely focus on the lack of a moving-load or blind-configuration test, the novelty relative to influence-area BWIM, and the unresolved bridge calibration. I strongly encourage the rig test you already propose and independent data, for example natural frequencies, for the box girder.

Yours sincerely,
Editor-in-Chief
