# Associate Editor report 2: BWIM, moving-force and load-identification lens

**Manuscript:** "Load observability of continuous girder bridges: a general response-integral theorem, optimal offset-immune estimation and field verification" (v3)
**Material read:** manuscript/v3/manuscript.md, manuscript/v3/cover_letter_SCHM.md, manuscript/v3/figures/ (Figs 4, 6, 7 looked at in detail; the others checked against their captions).

## Decision

**Major revision.** The paper is a useful, carefully argued account of when integral (influence-area) BWIM can work on continuous girders. In its current form, though, it overstates both the novelty of the core theorem and the multi-channel estimator, and it puts the field evidence in a better light than the data support. Every issue below can be fixed. None of them needs new tests, although a field test of the offset-immune pair would greatly strengthen the paper.

| Criterion | Score (1–10) |
|---|---|
| Novelty | **5** |
| Technical quality | **6** |

## Strongest points

1. **The strain blind ring is a clear, practical result** (Sec. 2.2, Eq. 9, Table 1). Strain integrals are blind at the zeros of the uniform-load moment diagram, a near-blind ring of |N_M| < 0.2 surrounds each zero, and these zeros exist on every continuous girder. That makes this a property of the girder type, not of a particular span ratio. The warning about gauges set back from the pier diaphragm (Sec. 2.2, Sec. 7 step 2) is guidance practitioners can actually use. The identity 2R_A/(q_0 L_1) = ξ_0 is neat.
2. **One static analysis gives all the design quantities.** The constant, blind loci, placement and boundary sensitivity of every candidate channel all come from the same uniform-load analysis (Eq. 2, Sec. 2.4, Sec. 7), and that makes the workflow easy to adopt.
3. **The limits of the beam model are reported honestly** (Sec. 4.3). Gauges about 2 m apart differ by up to 2.7 times, and the ratios change with lane. The authors conclude that BPM fails on deck-mounted gauges in box girders and that SLM or a 3-D model is needed. Most BWIM papers do not report this, and it is valuable.
4. **The offset-equivalent load P_ε (Eq. 12) and Table 6** show convincingly that baseline stability, not the estimator, limits single-point integral weighing on long spans.
5. **The work is reproducible.** It uses a public CC0 dataset, the laboratory data are given in full, the scripts are supplied, and the FE cross-checks are reported at machine precision.

## Ranked concerns

### 1. The response-integral theorem is presented as new, but it is the classical influence-area identity (major)
*Location:* Title, Abstract, Contribution 1 (Sec. 1), Sec. 2.1, cover letter item 1.
The statement that the integral of an influence line equals the response to a uniform unit load, and that the record integral therefore equals P_tot times that area, is textbook (influence lines for distributed loads; see Ghali et al. [52]). It is also the implicit basis of Ojio–Yamada [27], Helmi et al. [29] and the influence-area systems [34,35]. Extending it to any linear functional (rotation, reaction, shear) follows from superposition in one line. The new material is the systematic **use** of the identity: closed-form blind loci, the indicators N_M and R, and the boundary identifiability.
*Fix:* Call it a lemma or proposition, state explicitly that the identity is classical, and move the novelty claim in the title, abstract and cover letter to the blind-locus and observability criteria for continuous girders. Changing "general response-integral theorem" in the title is recommended.

### 2. The multi-channel and offset-immune estimator is textbook theory, and its realism depends on an untested common-mode assumption (major)
*Location:* Sec. 2.4 (Eqs. 13–14), Sec. 5.4, Sec. 6.2, Fig. 4, Conclusion 3.
- Eq. (13) is ordinary GLS/BLUE. Adding the constraint Σw_j = 0 is common-mode rejection, the same idea as differential measurement against a reference target, which the authors acknowledge. The algebra is correct, and the vertex-placement argument is correct under the stated assumptions: 1/Var is a convex quadratic in C, the feasible set is a box, so the maximum lies at a vertex. This is a sound application, not a new estimator.
- **Realism.** Each channel's offset is modelled as a constant with a fixed correlation ρ that does not depend on sensor separation. Real low-frequency disturbances do not behave like that:
  - Thermal deflection of a continuous girder has a spatial shape (gradient-induced curvature), not a common constant.
  - Strain drift from temperature differs from gauge to gauge.
  - NOR-BWIM wander (Sec. 4.4) was not tested for common mode.

  The headline numbers depend on ρ = 1 or ρ = 0.9: 0.071 % at ρ = 1 (Sec. 5.4), and Fig. 4a showing a 10⁻⁵ variance ratio. These numbers are not supported by any data. The placement rule also clashes with physics: with independent offsets it recommends clustering sensors at the maximum, but clustered sensors are exactly the ones whose offsets are most correlated.
- The one case that is plausibly common-mode is reference-frame motion of a single non-contact instrument (camera or laser station). The manuscript mentions it but does not develop it.

*Fix:*
- Present GLS and zero-sum weighting as an application of standard estimation theory.
- Estimate ρ from the simultaneous quiet segments of the NOR-BWIM channels. This needs no new data, since day 1 has 12 channels.
- Apply the zero-sum combination to the day-2 records and report whether the 18.8 µε m noise drops.
- Replace the ρ = 1 headline numbers with a ρ(separation) model, or bound them by measured ρ.
- Restrict the placement claim to the stated noise model.

### 3. The NOR-BWIM field verification is reported selectively in the Abstract and Conclusions (major)
*Location:* Abstract, Sec. 4.2, Table 3, Fig. 7, Conclusion 4, cover letter item 5.
- **The axle-configuration ratio is weak evidence.** The ratio 0.999 ± 0.140 cannot rule out differences of about ±28 % at 2σ. Invariance to axle configuration is mathematically guaranteed under linearity, so the real question is whether the noise allows any practical accuracy. Fig. 7 shows day-2 CV = 34 % at st40, and R15 sits at roughly 40 % of the mean. Present this as "consistent with", and add an equivalence test with a stated margin.
- **The headline errors leave out the worse cases.**
  - The Abstract quotes 6.5–7.0 % MAE "on the quieter day".
  - Day 2 gave 17.8 %, and the reverse calibration direction gave 17.1 %.
  - The day-1 reference weights are driver-reported, so the 6.5 % mixes estimator error with reference error.

  All of these figures belong in the Abstract.
- **Speed.** "Speed-independent" (Conclusion 4, cover letter) overstates a slope of −3.6 ± 5.8 % per 10 m/s, and +5.2 ± 13 % on day 2. Say "no speed effect resolved within ±12 % (2σ)".
- **Superposition.** Both two-truck events fall low (0.93, 0.92). The values are within uncertainty, but two same-sign deviations should be noted, not described simply as "held".
- **Data selection.** Explain why only four of the 12 day-1 channels were used as "wheel-path gauges", and why the seven exclusions were made. State whether the exclusion criteria were fixed before results were seen.
- **Missing baseline comparison.** There is no comparison with the GVW accuracy that Moghadam et al. [43–45] reported for their influence-line NOR-BWIM system on the same bridge. Without it, readers cannot judge what the integral method gives up.

### 4. Single-channel gross-weight claims ignore operational realities on long continuous girders (major)
*Location:* Sec. 4.4, Sec. 6.3, Sec. 7 (positioning as a "screening" tool).
- **Multiple presence.** A crossing of the 605 m Smart Road Bridge takes 22–60 s, and Cầu Mây takes 12–19 s. Under real traffic, isolated crossings may be rare. The paper says the usable fraction "was not quantified". For a method proposed for screening many structures, it must be estimated, at least from a Poisson headway model at typical AADT and truck percentages.
- **Transverse position.** C_B/C_A = 0.81, with a range of 0.66–1.02 per gauge, and the slab-local effects in Sec. 4.3 show that a single deck gauge responds as much to wheel-path position as to weight. Within-lane wander of ±0.3–0.5 m is not quantified. The paper should state how lane and wander would be detected without extra sensors, or note that NOR transverse-position algorithms (e.g. Yu, Cai and Deng 2018) exist.
- **Speed measurement.** Integrating in space requires v(x). In Sec. 4 speed came from axle strain spikes, which amounts to an axle-detecting channel. A speed error passes 1:1 into GVW, so the Sec. 6 budget should include speed-measurement error, not only the speed effect.
- **Noise at the best location.** Per-crossing errors of 10 % on day 1 and 35 % on day 2 at a not-blind gauge (Sec. 4.4) already exceed typical COST 323 class tolerances. "Preliminary overload screening" therefore needs a quantitative statement: what overload ratio can be detected at what false-alarm rate.

### 5. The Cầu Mây section is long and predictive, and its recommended deflection channel is hard to realise (moderate)
*Location:* Sec. 5, Tables 4–6, Conclusion 5.
For a BWIM readership, the main design recommendation is a mid-main-span deflection channel over water with a 0.1 mm residual offset. That relies on non-contact technology whose offset is acknowledged to be unknown. Most of Sec. 5 is identifiability of a 2-D model from two static dial-gauge readings, plus predicted values (Table 5), not measured ones. The useful BWIM message is short: a side-span deflection gauge near the prismatic blind locus cannot be identified from acceptance data, and strain gauges belong 5–10 m from the piers.
*Fix:* Condense Sec. 5 to about half its length, move Tables 4–5 and the frequency-mode argument to the Supplement, and give equal weight to the strain-channel design. Strain is what practical BWIM installs.

### 6. The laboratory verification is weak for a moving-load claim (moderate)
*Location:* Sec. 3.
The loads were static and the load order in the three-load group was inferred, as the paper acknowledges. The specimen is a 25 mm tube, and the measured-to-analytical step grows with load group (1.010 → 1.017). The section verifies the quadrature, not the theorem.
*Fix:* Shorten it, or carry out the cheap test the authors themselves propose: the blind configuration with 2500 + 3644 mm spans on the same rig. This would be the only direct test of a blind locus, which is the paper's most original prediction. No field gauge sits at a zero-moment point.

### 7. Editorial completeness and possible overlap (must fix before review)
*Location:* Table 7 ("accuracy class [NEED VALUE]"), Data Availability, Conflicts of Interest, Funding, Acknowledgments, cover letter (date, repository DOI, overlap statement).
The cover letter mentions two related papers under review at *Structures* without saying whether they share the rig, data or text. Ref. [40] already covers the simply supported case. A clear overlap statement is needed. Without one, the submission risks being treated as salami publication. All [NEED VALUE] placeholders must be resolved.

### 8. Minor points
- The term "observability" (Sec. 1, last paragraph) is defined narrowly. Consider "total-load identifiability" throughout, to avoid confusion with control-theoretic observability in an SCHM readership.
- Eq. (14): state the assumption that all channels in the zero-sum set are the same physical type, and say how strain and deflection channels would be combined.
- Sec. 2.4: the claim that structure-aware weights give 1.5–6.6 times lower variance but −1.1 % to +2.0 % configuration error deserves a figure, or should be cut.
- Sec. 4.4: "a gauge within ±12 m of a zero-moment point" is a model inference, not a field result. Label it as such.
- Abstract: drop the numerical detail on Cầu Mây (κ bounds) and add the day-2 and reverse-direction field errors.
- Fig. 6: integrals are given per gauge, but the window boundaries (5 s margins) are not marked in metres. Fig. 7: mark the excluded runs.

## Missing references (verified by web search)

1. W.-J. Yan, T.-T. Hao, K.-V. Yuen, C. Papadimitriou, "Monitoring gross vehicle weight with a probabilistic and influence line-free bridge weight-in-motion scheme based on a transmissibility-like index," *Mech. Syst. Signal Process.* (2022). https://doi.org/10.1016/j.ymssp.2022.109133
   *Why it matters:* an influence-line-free GVW method based on the ratio of responses at the same location under two loading conditions. At zero frequency this ratio is the SLM ratio of record integrals, so it must be cited and distinguished.
2. S. Lobo Aguilar, R.E. Christenson, "A simplified shear-strain based bridge weigh-in-motion method for in-service highway bridges," *Métodos & Materiales* 8 (2018), LanammeUCR (DOI not confirmed).
   *Why it matters:* an influence-line-free and speed-free GVW alternative that is relevant to Table 1's shear row.
3. Y. Yu, C.S. Cai, L. Deng, "Nothing-on-road bridge weigh-in-motion considering the transverse position of the vehicle," *Struct. Infrastruct. Eng.* 14(8) (2018) 1108–1122.
   *Why it matters:* transverse-position correction in NOR-BWIM, relevant to the lane and wander error in Sec. 6.3.

The authors should also report the GVW accuracy of the original NOR-BWIM system from [43–45] on the same bridge for comparison.

## Note to the authors (150 words)

This manuscript explains clearly when influence-area weighing can work on continuous girders, and the strain blind ring around each zero of the uniform-load moment is a result practitioners will use. However, the integral identity is classical, and the generalised least-squares and zero-sum estimators are standard estimation theory. Please present them as such and move the novelty claim to the blind-locus and identifiability criteria. The offset-immune results depend on a common-mode fraction that is assumed, not measured. Please estimate it from simultaneous quiet segments of the public records, apply the zero-sum combination to the day-2 data, and report the outcome. Please also report the field accuracy without selection: put the day-2 and reverse-calibration errors in the Abstract, describe the speed effect as unresolved rather than absent, and compare with the original NOR-BWIM accuracy. Please quantify multiple presence, wander and speed-measurement error, condense the Cầu Mây predictions, and resolve all placeholders and the overlap statement.
