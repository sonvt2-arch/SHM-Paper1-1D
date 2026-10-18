# Associate Editor assessment: field monitoring, data quality, uncertainty, reproducibility

Manuscript: "Total-load observability of continuous girder bridges from a single deflection channel: closed-form blind configurations, laboratory verification and sensor placement on an in-service box girder" (SCHM submission).

Material read: `manuscript/schm/manuscript.md`, `manuscript/schm/cover_letter_SCHM.md`, `manuscript/schm/figures/` (Fig3, Fig7, Fig8, Fig9, FigS1, `schm_figures_values.txt`), `code/supplementary/` (README, REPRODUCTION_REPORT.md, scripts, logs). I re-ran `run_all.sh` (s01 to s05) in a scratch copy. It finished in 1 min 52 s, and every log matched the committed logs except the run-time line in `s05`. I did not re-run `--with-analysis`.

---

## Decision

**Major revision.**

The theory is correct and fully reproducible, and it is useful to monitoring practice. The empirical support for the field claims is thin, though. The laboratory test uses statically placed weights on a 25 mm tube. The bridge evidence is two static dial-gauge readings, and the paper's own crossing records contradict the offset assumptions behind its headline field numbers. Several statements about data availability and integrity are still placeholders.

## Scores

| Criterion | Score (1–10) | Basis |
|---|---|---|
| Evidence (do the data support the claims?) | **4** | Theory and FE checks: 9. Laboratory: tests linear beam theory under static loads only (5). Field: zero degrees of freedom in the bridge calibration, no moving record on any continuous girder, and the assumed offsets are not demonstrated (3). |
| Reproducibility | **6** | s01 to s05 re-run bit-for-bit. The DOI for the field data is `[NEED VALUE]`. The raw laboratory cycles and the Abaqus model are absent. The reproduction report is stale against the current text. Six of the eleven manuscript figures are not in the figures folder. The package depends on `code/analysis` and `data/bridges`, which sit outside it. |

## Strongest points

1. **The negative results are reported honestly.** The authors say plainly that the Cầu Mây data are static and do not validate Eq. (2) (Sections 1, 4 and 8). They state that the residual offsets assumed in Section 6 "were not demonstrated" on the field channels (Section 5). They give the side-span result as an unidentifiable range rather than one value, and they withdraw the second girder (42 + 63 + 42 m) because their model could not reproduce its deflections (Section 7.2). This is better practice than is usual in BWIM papers.
2. **The offset-equivalent load is a genuinely useful field quantity.** $P_\varepsilon = \varepsilon_0 L_\mathrm{tot}/C_m$ (Eq. 19, Table 8) turns baseline stability into a load bias for a specific gauge. Field engineers can use it before installation.
3. **The identifiability problem is stated correctly.** Two static readings cannot separate girder $EI$ from pier rotational stiffness (Section 4.2). The k-sensitivity ($\partial\ln C_m/\partial\ln k$ = +0.51 at N8 against −0.12 at N7) is the right way to show why a side-span gauge is ill-conditioned.
4. **The signal-processing guidance is sound and backed by data.** High-pass filtering destroys the integral (−44 to −102 %, Fig. 8). A 2 Hz low-pass leaves it intact (Fig. 9). The rule "never use a high-pass filter as a baseline correction" is worth publishing.
5. **The computational side reproduces.** Every number in Sections 2, 3 and 6.1 to 6.5 and in Appendices A to D is produced by a script with a fixed seed. I re-ran the scripts and got the same output.

---

## Ranked concerns

### 1. The residual offsets used for the bridge are not credible, and the authors' own field data contradict them (critical)
- **Location:** Section 6.2 and Table 8 (ε₀ = 0.02 and 0.05 mm), Table 10 (field offset 2–10 %), Abstract, Section 8. Contrast with Section 5: post-minus-pre differences of 0.17–0.23 mm at Phuong Do N2, a 2.06 mm baseline step at Phuong Do N1, 0.1 mm quantisation at Gie Cuc, and quiet-level scatter of 0.01–0.13 mm.
- **Problem:** The headline "35–93 % at the side-span gauge, 10–11 % at the centre-span gauge" assumes a residual offset of LVDT class, 0.05 mm, on a 90 m span over a river. The paper concedes that such a channel would have to be non-contact. Vision and GNSS systems at that range typically leave residual offsets of 0.1 to several mm; only interferometric radar under good conditions approaches 0.05 mm. The paper's own field channels show offsets 4–40 times larger than the assumed values. At ε₀ = 0.2 mm, Eq. (19) gives a bias of about 370 % at N8 (calibration A) and about 45 % at N7. Read that way, the bridge case does not show a usable centre-span gauge. It shows that single-point integral weighing may be infeasible on a long-span girder with present absolute-deflection technology. The paper understates this.
- **Fix:** Extend Table 8 to ε₀ = 0.1, 0.2 and 0.5 mm, and add a column naming realistic technologies (interferometric radar, vision, GNSS, levelling-referenced LVDT) with literature values for their residual offset. State in the Abstract and the Conclusions which ε₀ the 10–11 % figure assumes. Derive the field offset entry in Table 10 from the Section 5 data, not from [48,49].

### 2. The Cầu Mây measurements are under-described, and the location of the critical gauge is uncertain (major)
- **Location:** Section 4.1, Table 6, Section 4.3 ("the test tables use [mid side span] as a label for N8 while the test plan places the gauge at 0.4L").
- **Problem:** Dial gauges need a fixed reference. How were absolute deflections of 5–15 mm read at mid-span of a 90 m span over the Kinh Mon River? Possible methods include a ground frame, piano wire, levelling or a barge; the paper names none. No resolution, reference stability or temperature record is given. Readings were taken in daylight in hot weather with zero readings between load cycles, and thermal camber of a 90 m box girder over the loading interval can be of the same order as the 0.5 mm spreads quoted. One peak per gauge and load case is reported, so repeatability across the three load cycles is not available, even though three cycles were performed. Most seriously, the gauge whose observability is the main finding has an ambiguous position (0.4L or 0.5L), and at 0.5L the pinned-to-fixed bracket contains an exactly blind state.
- **Fix:** Describe the deflection reference system and the reading procedure. Report the readings from all three cycles per scheme, the time interval and the temperature. Resolve the N8 position from as-built or photographic evidence, or carry both positions through Tables 5, 6 and 8 and the Abstract.

### 3. The bridge calibration has zero degrees of freedom, so the "two calibrations" claim rests on a structural assumption (major)
- **Location:** Section 4.2 and Table 5.
- **Problem:** Calibration B fits two parameters (α, k) to two readings. Calibration A fits k to two model values from the report and then scales α. Neither calibration is tested against any independent observable. The haunch length $L_v$ is assumed (44 m). Prestress, cracking, bearing restraint, shear lag and transverse distribution are all neglected. A 13 % transverse spread (2.05 mm across the N7 section, eccentric case) is larger than the calibration misfits. The conclusion "side-span gauge index 0.18 or 0.48" therefore reflects the model family as much as the bridge.
- **Fix:** Use at least one independent observable that is cheap to obtain: an ambient-vibration first frequency (minutes of accelerometer data), the pier dimensions from as-built drawings, or the six individual readings used as separate data with a transverse model. Otherwise, present the k-range in Table 5 as the main result and call A and B illustrative. Add an explicit statement that the transverse spread exceeds the calibration misfits.

### 4. The uncertainty budget is labelled GUM-consistent but is not a GUM evaluation (major)
- **Location:** Section 6.6 and Table 10, Section 7.2.
- **Problems:**
  - Ranges of plausible errors are entered as standard uncertainties, with no stated probability distributions. A bound "< x" is entered as x.
  - The zero offset is a systematic error that is common within a crossing, yet it is treated as an independent random term. Its correlation between the reference crossing and the target crossing in SLM, which Eq. (18) makes explicit, is ignored in the root-sum-square.
  - The Type A component is "bounded", although three loading/unloading cycles exist. Those raw cycles are not in the package.
  - The accuracy class of the weights is `[NEED VALUE]`.
  - No coverage factor or expanded uncertainty is given. The statement that "0.4–1.0 % is consistent with the observed 0.61 and 0.70 %" is therefore not a test.
  - The load-dependent step in the measured-to-analytical ratio (1.010 → 1.016 → 1.017, Section 3.3) is an unexplained systematic effect that appears nowhere in the budget, although it accounts for the whole SLM residual.
- **Fix:** Either rename Table 10 "sensitivity scenario table" and drop the GUM framing, or do a proper evaluation:
  - Type A from the three cycles.
  - Stated distributions, for example rectangular for resolution-limited terms.
  - Correlation coefficients between the reference and target terms in SLM.
  - An expanded uncertainty U (k = 2) for the laboratory, with |deviation| compared against U.
  - A row for the linearity/seating term.

  Publish the raw cycle data.

### 5. Laboratory realism and scale: a static test of beam theory, not of a measurement (moderate)
- **Location:** Section 3 and the scale argument in Section 3 (introductory paragraphs).
- **Problem:** The specimen is a 25 × 25 × 2 mm tube with span/depth 100, knife-edge supports and loads of 40–125 N hung at 21 stations 250 mm (l/10) apart. Peak deflections are about 3–8 mm, roughly L/300 to L/800, far more flexible than a bridge under traffic. The test therefore checks Euler–Bernoulli superposition, which is never in doubt, rather than the measurement chain. The scale argument is valid for the dimensionless identities. However, the three things that limit field performance cannot be tested at this scale:
  - sensor reference stability;
  - time-domain integration with uncertain speed;
  - long-record drift.

  In addition, the spacings were integer multiples of Δx, so the quadrature bias cancels by construction (Section 6.1). The invariance itself is tested only indirectly, because load and spacing change together.
- **Fix:** Run the direct invariance test the authors already propose: a fixed total load at three or more spacings, including spacings that are not multiples of Δx, and the falsifiable 2500/3644 mm blind-ratio rig. Neither needs new apparatus. A slow rolling-load (cart) pass recorded in time, with speed measured independently, would test the time-domain integral in Section 6.4. Without at least the fixed-load test, describe Section 3 as a "model verification", as the opening sentence of Section 3 already half-does.

### 6. Field crossing records: quality issues are visible in the figures but not discussed (moderate)
- **Location:** Section 5, Figs. 8 and 9.
- **Problems:**
  - Fig. 9 (Phuong Do N1, processed) shows an upward deflection of about −2.9 mm, about 40 % of the peak, lasting about 1 s after the truck leaves a *simply supported* span. Phuong Do N2 shows about −1.2 mm. A simply supported mid-span should not deflect upward by that much, which points to reference-frame movement, a second vehicle, or the hand processing.
  - The Gie Cuc N1 window ends with a second rising event at about 6.3 s and a dropout near the peak at about 3.6 s.
  - The Gie Cuc "dynamic residual" in Fig. 9b is dominated by the 0.1 mm quantisation saw-tooth, so "peaks of 3–16 %" partly measure quantisation, not dynamics.
  - Channel scale factors vary from 0.67 to 5.15 between spans and are undocumented.
  - The sensor type and reference for the SDA-830C channels are not stated.
- **Fix:** State the transducer and its reference. Explain the post-event negative plateau or exclude those records. Mark multi-vehicle and glitch segments. Separate quantisation from dynamics in Fig. 9b, for example by showing the residual of a quiet window. Restrict the conclusions in Section 5 to the processing rules, which the data do support.

### 7. Operational realism of a single channel on a long continuous unit (moderate)
- **Location:** Sections 6.4 and 7.1 (items 5 and 8).
- **Problem:** A crossing of the 200 m unit at 40–60 km/h takes 12–18 s. On a provincial road, a single vehicle alone on 200 m of deck for that long will be rare. Because overlapping crossings must be discarded, the fraction of usable events may be very small, and screening throughput is never estimated. Speed is "likely the largest single field contributor", but the interior zero-crossing method for measuring it is untested. A single channel also cannot detect lane position, which Table 6 shows matters at the 13 % level.
- **Fix:** Use available traffic counts for DT389, or a Poisson argument, to estimate the probability of a lone vehicle on 200 m. Discuss lane/transverse error as a Table 10 entry. Soften the recommendation that a single gauge supports "screening across many secondary structures" for long continuous units, and restrict it to short spans.

### 8. Data availability, integrity statements and the supplementary package (moderate, administrative but blocking)
- **Location:** Data Availability, Conflicts of Interest, Funding, Acknowledgments, Section 7.2, cover letter.
- **Problems:**
  - The repository DOI, the accuracy class of the weights, the conflict-of-interest details, the funding/APC statement and the acknowledgement of the PMU are all `[NEED VALUE]`.
  - The cover letter leaves undeclared any overlap with two related papers under review at *Structures*. This must be resolved before the manuscript can go to review.
  - `REPRODUCTION_REPORT.md` lists mismatches M1 to M10 against an *earlier* text. For example, it quotes "−0.110 %/+0.249 %", "39 %" and "roughly halves", whereas the current manuscript already prints −0.171/+0.014 %, 34.5 % and 20–28 %. A reviewer would read it as a list of live errors.
  - `manuscript/schm/figures/` lacks Figs. 1, 2, 4, 5, 6 and 10.
  - The package is not self-contained. The Section 4 and 5 scripts and the data sit in `code/analysis/` and `data/bridges/`, and `schm_figures.py` was not re-run.
  - The raw laboratory cycles and the Abaqus model are absent.
- **Fix:**
  - Deposit the Cầu Mây readings (all cycles and gauges), the truck masses and positions, the crossing records (raw and processed, with scale factors) and the laboratory cycles in a public repository with a DOI.
  - Make the supplementary archive self-contained.
  - Regenerate the reproduction report against the submitted text.
  - Supply all figures.
  - Complete every placeholder and the cover-letter overlap statement.

### 9. Minor overclaiming in framing (minor)
- **Problems:**
  - The Abstract and Section 8 state the 35–93 % and 10–11 % biases without the ε₀ assumption being prominent.
  - "Never from the design model" (Sections 4.4, 7.1 and 8) generalises from one bridge with an unidentified calibration.
  - The laboratory "within 1.19 % / 0.70 %" is presented next to field numbers, implying a transferability that Section 3 itself disclaims.
- **Fix:** Qualify these statements with the ε₀ value and the static, single-bridge basis, for example "on this girder" or "for a girder near the prismatic blind locus".

---

## Note to the authors (about 150 words)

The theory is correct and fully reproducible, and the observability indicators, especially the offset-equivalent load, are useful to monitoring engineers. Your treatment of the limits of your data is also unusually candid. The field evidence does not yet carry the practical conclusions, however. Your own crossing records show residual offsets of 0.1–0.2 mm and baseline steps of 2 mm, yet Table 8 and the Abstract assume 0.02–0.05 mm on a 90 m span over water. Please re-evaluate the bridge case at offsets that current absolute-deflection technology can achieve, and describe how the Cầu Mây dial gauges were referenced. Resolve whether N8 sits at 0.4L or 0.5L. Either make Table 10 a proper GUM evaluation, using the three recorded cycles, or retitle it as a sensitivity scenario. Run the fixed-load, varying-spacing test on the existing rig. Finally, deposit all field and laboratory data with a DOI, make the supplementary package self-contained, and complete every placeholder and the overlap declaration.
