# Associate Editor report (structural mechanics / continuous girders) — manuscript v3

Manuscript: "Load observability of continuous girder bridges: a general response-integral theorem, optimal offset-immune estimation and field verification" (SCHM, v3)
Material read: manuscript/v3/manuscript.md, manuscript/v3/cover_letter_SCHM.md, manuscript/v3/figures/ (Fig 2, 9 inspected in detail). Spot checks: hand derivations plus existing logs and a scratch run of code/v3/v3_numbers.py (Part A).

## Decision

**Major revision.** The mechanics is sound: every closed form I re-derived holds, and the estimator algebra is correct. The revision is needed for other reasons. Several headline claims in the abstract, conclusions and cover letter overstate or misdescribe what the evidence shows. There is one wrong normalisation statement and several internal inconsistencies, two figures are missing, and placeholders are unresolved. None of this needs new experiments, but the framing must change before review can continue.

## Scores

| Item | Score (1–10) |
|---|---|
| Technical soundness, overall | 7 |
| – theory (Sec. 2, App. A–C) | 8 |
| – laboratory (Sec. 3) | 6 |
| – field, NOR-BWIM (Sec. 4) | 5 |
| – in-service bridge identifiability (Sec. 5–6) | 7 |
| Clarity | 7 |

## Verified items (independent checks)

1. **Eq. (5).** The SS term 8ξ(1−2ξ²+ξ³) and the end-moment term −4μξ(1−ξ²) are correct. Eq. (6) factorisation and the range 1<μ<2 are correct.
2. **Eq. (4).** μ_2span and μ_3span follow from the three-moment equation, with ρ_EI used consistently (adjacent/instrumented; EI_m/EI_s).
3. **Eq. (7).** 3ρ²−3ρ−2=0 gives ρ_L,crit=(3+√33)/6=1.4574. dF/dξ at μ=1 gives (ξ−1)(8ξ²−ξ−1), so ξ*=0.4215.
4. **Eq. (8).** 6β³−15β−4=0 gives 1.70059 (residual 4e−15), and the trigonometric form checks. The near-blind bands [1.621, 1.775] and [1.385, 1.525] give N_w = ±0.200 at their ends. The locus end β³−3β−1=0 gives 2cos(π/9).
5. **Table 1.**
   - End rotation: ρ_L=1.618 (golden ratio).
   - Pier rotation: ρ_L=1 and β=√(3/2) for any ρ_EI (μ=1). Checked.
   - End reaction: μ=4 gives 2.3028 and 2.6691.
   - Mid main-span deflection blind at β=0.9647 (App. A).
   - Strain zeros ξ₀=1−μ/4. η₀=0.276 (β=1) and 0.177 (β=1.636).
   - Band 0.676<ξ<0.812.
   - R_A identity 2R_A/(q₀L)=ξ₀.
6. **R values.** R_w=4/7 and R_ε=2/3 for two equal spans. The App. A contributions (1.50–2.00; −0.125 to −4.00) check.
7. **Table A.1.** β=1.636 gives μ=1.557 and N_w(½)=0.164. β=1.7 gives N_w=0.0015.
8. **Eq. (16).** It reduces to μ_3span at K=0 and to μ=1 as K→∞. N8 at ξ=0.4 is 0.287 (pinned) and 1.037 (fixed). Mid main span is 0.755 (pinned) and 0.500 (fixed).
9. **Eq. (14).** It is the minimum-norm solution under wᵀC=1, wᵀ1=0. The two-channel price 2C₁²/(C₁−C₂)² is correct. The convexity/vertex placement argument is valid for the box-shaped feasible set.
10. **Möbius law (Eq. 15) and B_m.**
    - C_∞/C₀ = 0.422/0.030 = 14.0 (N8) and 0.147/0.248 = 0.59 (N7), matching ident_static.log.
    - At κ/k_g=0.63, B_m = 0.512 (N8) and 0.116 (N7). Checked.
11. **Unit conversions (Tables 4, 5, 6).**
    - N_w→C uses EI_mid = 1.977×10⁸ kN m².
    - Offset bias ε₀L/(CP) with P=245.8 kN, e.g. 22.5 % for N7-A at 0.1 mm. Checked by hand and by the v3_numbers.py run.
    - Table 5 ratios 0.121 / 0.284 = C8/C7. Checked.
12. **Laboratory and timing.**
    - C_m = L⁴/(192EI) = 61.54 mm²/N.
    - Load totals: 66.99 N and 125.08 N.
    - SLM residuals equal the step 1.016/1.010 and 1.017/1.010.
    - Crossing times: 18.6 s and 12.4 s.
13. **NOR-BWIM log values.** These match tests.log:
    - C(5-axle)/C(3-axle) = 0.999.
    - Day-1 SLM MAE 7.00 / 6.51 %.
    - Day-2 MAE 17.77 %.

## Ranked concerns

**1. Day-1 weights are driver-reported, and the day-1 SLM test has almost no discriminating power.** (Abstract l.15; Sec. 4.2, Table 3; Concl. 4; cover letter item 5)
- The abstract says "one *weighed* reference crossing predicted the other trucks within 6.5–7.0 % … on the quieter day". The quieter day is day 1, whose weights are driver-reported (Sec. 4.1).
- Day-1 GVWs span only 21.17–22.82 t (±3.7 %). A trivial constant predictor (the mean weight) would give MAE ≈ 2 %. A 7 % MAE is therefore worse than the null model, and it is not evidence that SLM works.
- The 6.5–7.0 % figure is for the gauge average. Single gauges gave 6.6–30.7 % (tests.log). Day 2, the only day with scale weights, gave 17.8 %. The reverse calibration gave 17.1 %, and the reference gauge st40 gave 48–54 %.
- *Fix:*
  - Remove "weighed" for day 1 in the abstract and in the cover letter.
  - Report the null-model MAE beside every SLM figure.
  - Lead with the day-2 scale-weighed results.
  - State explicitly that day 1 cannot test weight prediction, only scatter of C.

**2. The N8 upper bound of 0.82 comes from the normalisation, and "bounded only from below" ignores engineering priors.** (Abstract; Sec. 5.2; Table 4; Concl. 5; Fig. 9b)
- The 0.82 uses EI_ref = design EI_mid while α ≈ 0.51 at the upper end.
- Normalised by αEI_mid (Fig. 9b, solid line), the static-set range is 0.14–0.42 (ident_static.log, N8a). The upper part of the range therefore requires a 49 % stiffness loss in a young post-tensioned girder, which the authors themselves call implausible (Sec. 5.2).
- With the authors' own prior α ∈ [0.9, 1.3], the range is 0.12–0.30. Bracketing k physically would also bound κ from above. ident_static.log brackets k at 5.8×10⁶–1.8×10⁸ kN m/rad, but pier geometry is a placeholder.
- *Fix:*
  - Headline the prior-constrained range, or report both normalisations.
  - Say "the static data alone bound κ only from below".
  - Add the pier-stiffness bracket from the pier geometry.
  - Better still, express identifiability in C (m²/kN) or in P_ε (as in Table 6), which needs no EI_ref.

**3. Wrong normalisation statement.** (Sec. 2.3 after Eq. 10; App. B "normalised to the simply supported reference"; Fig. 3 caption)
- With N_w = 192EI C/L⁴, the mid-span of a simply supported span gives 192·5/384 = **2.5**, not 1. N_w = 1 holds at mid-span of two equal spans; Table A.1 and the lab C_m confirm this normalisation.
- The threshold |N_w|<0.2 is thus 8 % of the SS value, against 20 % for |N_M|<0.2. So the two "0.2" thresholds are not equivalent, contrary to the implied parallel.
- *Fix:*
  - Correct the sentence and the App. B / Fig. 3 wording.
  - Either renormalise N_w to 384EI C/(5L⁴), so that SS mid-span = 1, or justify 0.2 on its own.

**4. Internal inconsistencies in Section 4.**
- (a) Sec. 4.3 and the abstract say gauge constants differ "by up to 2.7 times". The same paragraph reports a pair ratio of about 3.2 in lane A (tests.log: 3.24 ± 0.56). The day-1 range 0.68–2.71 relative to the reference gauge also implies a pairwise ratio of up to 4.0.
- (b) Sec. 4.3 says "only about half of the integral comes net from the instrumented span". The decomposition actually implies that span 2 contributes ≈ 173 % of the net integral (−26 −66 +23 −4 for the others), with R = 0.51.
- *Fix:* restate both claims.
- The lane-dependence argument against gauge-factor spread (3.2 ± 0.56 vs 1.8 ± 0.1) is about 2.5σ. Quote the uncertainties.

**5. Inconsistent numbers within Sections 5–6 and Section 2.4.**
- (a) Sec. 5.4 gives a single-gauge SD of 24.8 % for N7-A at ε₀ = 0.1 mm. Table 6 gives 23 % for the same case. The scripts use L_rec = 220 m in multisensor_core.py against L_tot = 200 m in Table 6. Unify the record length.
- (b) Sec. 2.4 says the white-noise term is "about 10⁻⁴ of the offset term". With Δx = 0.1 m and L = 220 m, the ratio is σ²Δx/(ε₀²L) ≈ 5×10⁻⁶. The value depends on Δx, which is not stated. State Δx and correct the order of magnitude.
- (c) The pair position is 152 m in the text and 155 m in the logs. This is acceptable as "within 0.9 %", but name the optimum.
- (d) Eq. (15) should carry the α⁻¹ factor, or state that C₀ and C_∞ are at α = 1.

**6. The Cramér–Rao figures lack an evaluation point.** (Sec. 5.4: ln C_m SD 0.87 → 0.18 / 0.24)
- Sec. 5.2 states that the two-reading Fisher matrix is singular at calibration B. The CRB is therefore infinite there and depends strongly on location along the valley.
- *Fix:* state the evaluation point (A?), the noise assumptions and the prior. Better, report the admissible-set shrinkage with the tiltmeter added.

**7. The placement rule for strain is misstated on non-prismatic girders.** (Sec. 2.4 "of M_q(x) for strain"; Workflow step 5)
- The vertex result applies to the constants C_ε = cM_q/(EI q₀), which include the section gain. On Cầu Mây that gain is about five times larger at mid-span than near the piers (Sec. 5.4).
- *Fix:* say "extremes of C(x), i.e. of cM_q/EI for strain", and assume position-independent noise in strain units.

**8. Novelty framing of the "theorem".** (Title; Sec. 2.1; contribution 1)
- Eq. (2) is a direct consequence of superposition and Maxwell reciprocity. Its deflection form underlies Ojio–Yamada and the influence-area literature.
- The genuine contributions are the channel-wise blind loci, the indicators, the estimator/placement results and the identifiability analysis.
- *Fix:* call it a proposition and state the known antecedents. The field "axle-configuration independence" test (ratio 0.999 ± 0.140) checks linearity and processing at ±28 % (2σ) power, not the mathematics. Say so.

**9. Laboratory limits.**
- Static positioning, equal spans (the furthest case from blindness), and a three-load order inferred from the fit. The authors state these limits honestly.
- The quantity "measured-to-analytical integral ratio 1.010" (trapezoidal on both) and "ratio 1.0049 = measured reference / exact" use different denominators. Define both explicitly.

**10. Presentation and completeness.**
- Fig. 1 and Fig. 5 are cited but are not in manuscript/v3/figures/.
- Fig. 9a legend lists both "2τ, τ = 5.3 %" and "τ = 5 %" bands. Keep one, and note that the ratio band is ±2τ.
- [NEED VALUE] placeholders remain in Table 7 (reference weighing class), Data Availability, COI, Funding, Acknowledgments and the cover letter. These include the date and the overlap with the two papers under review at *Structures*.
- The overlap must be disclosed before review, since the laboratory rig and [40] may be shared.
- Eq. (8): "which Eq. (8) gives in exact trigonometric form" is redundant. Use "positive root" instead of "real root", since the cubic has three real roots.

**11. Frequency interpretation (Sec. 5.3).**
- It is honestly labelled conditional.
- However, frequencies of 3.4–3.6 Hz measured at all three mid-spans of a 90 m PSC box, one value each, are suggestive of vehicle or bounce response.
- The joint set should not appear in the abstract or conclusions as a parallel result unless that caveat goes with it. The paper currently gives it in parentheses in Concl. 5.

## Note to the authors (150 words)

The mechanics is careful. Every closed form we re-derived holds: Eqs. (4)–(9), (14)–(16), Table 1 and Table A.1. The Möbius identifiability argument for the symmetric girder is instructive. The claims, however, run ahead of the evidence in three places.

First, the day-1 standard-load result is quoted as "weighed", although those weights are driver-reported. Day-1 weights also vary by only ±4 %, so a 7 % MAE does not beat a constant predictor. Reframe the field evidence around the scale-weighed day 2.

Second, the 0.12–0.82 side-span range rests on normalising by design rigidity while α ≈ 0.5. Report it in absolute C or P_ε, under physically plausible priors.

Third, correct the statement that N_w = 1 for a simply supported span; the value is 2.5.

Please also reconcile the 2.7× versus 3.2× gauge ratios, the 23 % versus 24.8 % offset bias and the white-noise ratio. Supply Figs. 1 and 5, resolve all placeholders and disclose the overlap with your related submissions.
