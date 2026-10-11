# WP8 Red-team report: `manuscript/structures/manuscript.md`

Date: 2026-10-11. Reviewer: Red Team (WP8). The manuscript was not edited and nothing was committed.

Files reviewed: `manuscript/structures/{manuscript,highlights,cover_letter,figure_table_plan,open_items}.md`. Context files: `docs/decision_letter_JCSHM.md`, `docs/rejection_evidence.md`, `docs/novelty_matrix.md`, `docs/04_tong_hop_ket_qua_lo_trinh_A.md`. Numbers were spot-checked against `code/analysis/logs/{verify_3span,cm_3span_theory,wp3_run,wp4,cm_multispan}.log`. An independent re-computation (Appendix C data, Eq. (A.2), O_m, Table 9, Eq. (19) at bridge scale) was run with a scratch script (`chk.py`, session scratchpad, not in the repo).

Line numbers below refer to `manuscript.md` as it stands today (661 lines).

---

## 0. Journal scope evidence (checked 2026-10-11)

**Structural Control and Health Monitoring (SCHM, Wiley, gold OA).** Wiley's product page reached through Exa states: "encompasses all theoretical and technological aspects of structural control, structural health monitoring theory and smart materials and structures. The journal focuses on aerospace, civil, infrastructure and mechanical engineering applications. Original contributions based on analytical, computational and experimental methods are solicited in three main areas: monitoring, control, and smart materials and structures, covering subjects such as system identification, health monitoring, health diagnostics, … signal processing, sensor technology … Also of interest are … data acquisition, … measurements, … experimental techniques." The listing reports an acceptance rate of about 37 % and a median of 62 days to first decision. The journal is open access under CC BY, so an APC applies; check the current amount and any waiver for Viet Nam before submitting. The paper declares no funding. One fit signal: SCHM published Zhou, Feng, Di, Jia, "A Novel Approach for Bending Stiffness Inversion and Rapid Evaluation of Continuous Beam Bridges Based on a Deflection Influence Line" (first published 6 Oct 2026). That paper is on the same object (deflection influence lines of continuous girders), so the topic is in scope, and it **must be cited and distinguished**.

**Structure and Infrastructure Engineering (SIE, T&F, subscription with optional OA).** The official T&F "about this journal" page says SIE covers "recent advances in maintenance, management and life-cycle performance of a wide range of infrastructure systems, such as: buildings, bridges …". Papers should "form a significant contribution to the theory or practice of infrastructure engineering … or describe a case study in which theory is applied to a significant infrastructure problem". The listed scope includes "mathematical modelling", "computer and experimental methods", "field testing", "inspection and diagnostics", "loads and multi-hazards", "monitoring, optimization of maintenance and management" and "decision-making". Review is single-anonymous. SIE has published BWIM work before (ref. [14], Žnidarič et al. 2018).

Sources: [Wiley SCHM homepage](https://onlinelibrary.wiley.com/page/journal/15452263/homepage/productinformation.html), [Wiley SCHM description](https://www.wiley.com/en-ie/Structural+Control+and+Health+Monitoring-p-15452263), [Dongguk listing of SCHM aims](https://scholarworks.dongguk.edu/journal/32271), [T&F SIE aims and scope](https://www.tandfonline.com/journals/nsie20/about-this-journal), [IALCCE SIE brochure](https://www.ialcce.org/wp-content/uploads/SIE_Brochure.pdf). The publisher pages returned HTTP 403 to direct fetch, so the wording was taken from Exa's crawl of those pages.

---

## 1. Persona 1: Desk editor

### 1a. Desk editor, SCHM

**Fit score now: 6/10. After the fixes in Section 4: 7.5/10.**

**Would I send it out?** Only after the administrative blockers are cleared. On substance it is borderline-yes. Sensor placement, observability and signal processing for a monitoring channel are SHM-theory topics, and SCHM publishes analytical papers backed by small laboratory checks more readily than JCSHM. The JCSHM editor's objection (scale of the laboratory model) will occur to an SCHM handling editor too, so the paper has to show that its main result does not depend on the laboratory scale.

**Sentences and sections that would trigger desk rejection:**

1. **Cover letter is addressed to *Structures*** ("The Editor *Structures* Elsevier"; "suits *Structures*"). Sending a cover letter for a different journal is an automatic bad first impression. Blocking.
2. **Unresolved placeholders in the manuscript:** L249 truck weights `[NEED VALUE]`; L372 Type A `[NEED VALUE]`; L413 weight accuracy class `[NEED VALUE]`; L531 data owner and permission `[NEED VALUE]` twice; L539 acknowledgement; refs [44] and [45] have no titles or DOIs; ref [6] carries "[check exact title wording]"; ref [10] carries "[CAN_TAC_GIA: …]"; ref [47] "[NEED VALUE: confirm edition]". Editorial screening returns any one of these. Blocking.
3. **Abstract, L15:** "Laboratory tests on a two-span steel beam with statically positioned loads …" followed by "This application is a static consistency check, not a validation of the integral on a continuous bridge." The two sentences together tell a skimming editor that nothing was validated at structural scale. That was exactly the JCSHM reason. The limitation must stay in the paper (honesty), but the abstract should lead with what *is* shown at bridge scale. Major.
4. **Keywords, L17** omit "structural health monitoring" and "sensor placement optimisation" in SCHM vocabulary. Minor, but it affects editor and reviewer matching.
5. **Section 5 (L292–304)** says "Truck weight, speed and lane were not recorded … the channel calibration is not documented … partly processed by hand". On a quick read a "field data" section that admits uncalibrated channels looks like padding. Shorten it to one paragraph plus a supplementary file, or turn it into the bridge-scale argument of Eq. (19). Major for perception.
6. **Section 3 (L195–237):** the specimen is a 25 × 25 × 2.03 mm tube. No sentence argues why scale does not matter for the claims made. Major (scale is the known editorial objection).
7. **Title (23 words).** It is long, but "observability" plus "single channel" plus "in-service bridge" does read as SHM. Minor.

**Framing changes that avoid desk rejection at SCHM:**
- Lead with the SHM-design question: "Before a single-channel load-monitoring system is installed on a continuous girder, can it see the load at all?" Present the indicator as a **sensor-placement and observability criterion for SHM**.
- Add a short **scale-independence argument** to Section 3: every theoretical claim is a dimensionless identity in N_m, R_m, β and ξ, so the laboratory beam tests the identities, not the scale. The quantities that do depend on scale (ε0·L_tot/I_y, T_cr/T1) are then evaluated **at Cầu Mây scale** (see Reviewer B, B-6). That turns the "lab scale" objection into an explicit design argument.
- Make the bridge-scale result concrete: on Cầu Mây, a residual baseline offset of 0.05 mm gives about 94 % load bias at N8 and about 11 % at N7 for a 25 t truck (Eq. (19), computed by this red team). This is a monitoring-design result an SCHM editor will recognise immediately.
- Cite and distinguish the SCHM Oct-2026 continuous-beam deflection-influence-line paper, plus one or two recent SCHM BWIM or load-identification papers.
- Rewrite the cover letter for SCHM. Say plainly that the previous version was declined by JCSHM on scale grounds and that the revision adds bridge-scale analysis. This is optional, but it reads as credible.

### 1b. Desk editor, SIE

**Fit score now: 5/10. After the fixes: 7/10.**

**Would I send it out?** Not in its present framing. SIE editors look for maintenance, management, life-cycle or decision value. The manuscript reads as structural mechanics plus metrology. The Cầu Mây case study fits SIE's "case study in which theory is applied to a significant infrastructure problem" wording, but the paper never states what a bridge owner or asset manager gains.

**Triggers:**
1. Cover letter addressed to *Structures*, and the same placeholders as for SCHM. Blocking.
2. **Introduction L50** mentions asset management in one sentence and then drops it. The contribution list (L60) is entirely about mechanics: constants, closed forms, a blind locus. An SIE editor sees no infrastructure-management contribution. Major.
3. **Section 2 (about 35 % of the main text)** is closed-form beam theory: cubics, trigonometric roots to six decimals. To an SIE editor this suggests a mechanics journal. Major.
4. **Section 6.6 (L390)** "the method is proposed for preliminary overload screening … establishing that threshold … lies outside this study". The management use case is deferred entirely. Major.
5. The laboratory beam carries the only verification of the estimator, and the bridge data are static. SIE readers are practitioners, and "no crossing record exists" (L60) will be read as "not field-tested". Major.

**Framing changes for SIE:**
- Reframe the paper around **monitoring planning for bridge networks**. The indicator is a pre-installation screening step that avoids wasted deployments on continuous girders. Give a worked decision table for Cầu Mây (gauge options against expected bias for a given baseline stability and vehicle weight) and estimate the cost of a blind installation.
- Move most of the derivations to an appendix. Keep only Eqs. (2)–(3), the blind conditions and Table 2 in the text.
- Add a paragraph on how the observability check enters a management workflow: overload screening, then triggering of BWIM or enforcement, then input to load models for assessment (refs [5,6,46,47]).
- Retitle along the lines of "Pre-installation observability check for single-channel load screening on continuous girder bridges: theory and application to an in-service box girder".

---

## 2. Persona 2: Reviewer A (BWIM expert)

**Recommendation: major revision.**

### A-1. Novelty against Moses (1979), Ojio and Yamada, and strain-integral methods
- Eq. (2) follows in one line from the Moses convolution model: integrate Σ P_i·IL(x − a_i) over the record. Eq. (3) is the textbook Maxwell–Betti identity: the area of a displacement influence line equals the deflection under a unit uniform load (it appears in classical structural analysis texts, e.g. Müller-Breslau-type arguments). The manuscript already demotes the invariance to "foundation" (L60), which is correct. It should also **cite a textbook source for Eq. (3)** and limit the claim to its *use* in BWIM ("we did not find it stated in the BWIM literature", L60, is acceptable hedging).
- **The SLM is the Ojio–Yamada calibration under another name.** Eq. (11) is the influence-area calibration of [27]. The manuscript never says so. Say it explicitly in Section 2.4 and use their name for it (major: attribution).
- **Strain counterpart missing.** Practical BWIM uses strain. By the same Betti argument, the strain-integral constant is M_q(x_m)/q0, so for strain sensors the blind points are the **contraflexure points of the uniform-load moment diagram** (for example 0.75L from the outer support on equal two spans). Every BWIM practitioner knows to keep gauges away from these points. A reviewer will ask (a) why deflection rather than strain, and (b) whether the deflection blind locus is anything more than the deflection analogue of a known rule. Fix: add a half-page corollary for strain (moment) sensors. It costs one equation, widens the audience, and makes clear that deflection blindness depends on the span ratio while strain blindness occurs at contraflexure on every continuous girder. Major.
- **Prior use of the area method on multi-span bridges.** The UCD review by Lydon et al. ("Recent developments in B-WIM") describes a Winnipeg seven-span slab-on-girder study that compared the Ojio–Yamada "beta" (influence-area) method with two other GVW methods, and it records a *negative GVW* for one of them. Check whether that structure was continuous and whether the area method failed there. If it did, this is the most direct empirical prior art for "blindness" and must be cited. Cardini and DeWolf [27] also say Moses and Ghosn extended BWIM to continuous spans. Major (literature gap).
- The defensible novelty remains: the closed-form blind locus (two spans with arbitrary ρ_L and ρ_EI; symmetric three spans: β_crit, the near-blind edge, the end of the blind locus at 2cos(π/9)), ξ*, the indicators |C_m| and R_m, and the matched-filter efficiency O_m. A sceptical reviewer will call the closed forms "three-moment-equation exercises". The defence is the engineering consequence, which the paper must quantify at bridge scale (B-6).

### A-2. Are the contribution statements defensible?
| Claim (L60) | Verdict |
|---|---|
| 1. Invariance and C_m by reciprocity | Defensible as stated ("foundation, not headline"). Add the textbook citation. |
| 2. Closed forms for two and three spans | Defensible. Correct (verified, Section 3). |
| 3. Blind configurations in closed form, exact ξ* | Defensible. Fix the "blind when β < 0.964706" wording (B-3). |
| 4. \|C_m\| and R_m as pre-installation indicators | Partly defensible. R_m ignores absolute signal level (B-7). Section 7.1 step 2 contradicts the \|C_m\| logic (B-3). |
| 5. Error budget dominated by drift | Defensible qualitatively. Table 9 is internally inconsistent (B-8) and not evaluated at the scale of the paper's own bridge (B-6). |

### A-3. Overclaims
1. **Cầu Mây "near-blind" headline (abstract L15, L269, L427, highlight 5).** It holds only for the k_FE calibration. `wp3_run.log` shows that a **joint fit to the measured deflections** (α = EI_eff/EI_design = 0.716, k = 1.2 × 10⁸ kN m/rad) reproduces the measurements *better* (misfit ±2.9 %) than k_FE with α = 1.088 (misfit −4.6 to +5.0 %). Under that fit, N8 has N_m = 0.476 and |A⁻|/A⁺ = 0.44, so it is **not near-blind**. The manuscript does not report this alternative. Two static readings cannot identify two unknowns (α and k). This is **blocking** for the bridge claim. Report both calibrations, argue which is physically plausible (a 28 % softer new PSC box is implausible, which favours k_FE, but say so), and soften the highlight to "near-blind under the design-consistent calibration".
2. **"C_m changes about fourteenfold between pinned and fixed piers"** (abstract, L269, L427). Pinned and fully clamped limits are not a plausible uncertainty range for monolithic piers. The relevant uncertainty is C_m over a realistic k range (at least the k_FE range 2.5–3.6 × 10⁷, ideally ±50 % or a range set by pier dimensions). Present the fourteenfold figure as a bound and add ∂ln C_m/∂ln k at k_FE. Major.
3. **"BPM would underestimate the total load by roughly 7–9 %"** (L286, L427). This rests on α = 1.09 at a fixed k. The alternative fit gives α = 0.72, and the two gauges disagree (measured/model 0.977 at N8 against 0.890 at N7). Rephrase as conditional on k_FE. Major.
4. **"The in-service girder thus confirms, on real section data, that a layout near the prismatic blind locus can be near-blind in practice"** (L288). Nothing was measured that bears on C_m. "Indicates, in a model built from real section data" is the correct verb. Major.
5. **"field crossing records confirm that baseline handling can change the integral by tens of per cent"** (L429). The records come from simply supported spans, channels with unknown scale, a quantisation of about 0.1 mm (log: quiet-block scatter 0.000 mm, values in 0.1 mm steps) and hand-processed series. "Illustrate" fits better than "confirm", and the conclusions should say these were simply supported spans. Minor-major.
6. **Speed "self-calibration" from the interior zero crossing** (L352): untested, and it holds only for a single axle. Label it as a proposal. Minor.
7. **Practicality of absolute deflection** (not addressed). On a 90 m span over a river, deflection would have to come from radar interferometry, vision or GNSS, whose drift is at the 0.1–1 mm level, not 0.005–0.05 mm. Section 6.2 and Table 9 assume LVDT-class stability. State the measurement technology the field scenario assumes, and define ε0 as the **residual after pre/post re-zeroing**, not absolute drift. Major.
8. The SCHM 2026 continuous-girder deflection-influence-line paper (Zhou et al.) and Zhou et al. 2025 [38] (read beyond the title) must be discussed. `open_items` B8 lists several references cited from title or excerpt only. A BWIM reviewer will check [37] and [38]. Major.

---

## 3. Persona 3: Reviewer B (structural mechanics and field measurement)

**Recommendation: major revision. The mathematics is correct. Wording, the bridge identifiability problem and the error-budget arithmetic need work.**

### B-1. Derivations verified
| Item | Check | Result |
|---|---|---|
| Two-span μ, Eq. (5) (the "Eq. (11a)" of the old manuscript) | μ = (ρ_EI + ρ_L³)/(ρ_EI + ρ_L) is the moment from slope continuity with ρ_EI = EI₂/EI₁. ∂μ/∂ρ_EI = ρ_L(1−ρ_L²)/(…)² matches L124. ∂μ/∂ρ_L numerator ρ_EI(3ρ_L²−1)+2ρ_L³ matches App. A, with minimum 0.75 at ρ_L = 0.5 and μ = 3 at ρ_L = 2 | Correct. `open_items` B3 is right: ρ_EI is adjacent/instrumented, and the WP2 warning is a misreading. |
| F(ξ, μ), Eq. (4); μ_crit, Eq. (6) | F = ξ(1−ξ)[(1+ξ−ξ²) − μ(1+ξ)/2], so μ_crit = 2(1+ξ−ξ²)/(1+ξ) | Correct. μ_crit decreases monotonically from 2 at ξ → 0. |
| ρ_L,crit = (3+√33)/6 and ξ* = (1+√33)/16 | 3ρ²−3ρ−2 = 0; 8ξ³−9ξ²+1 = (ξ−1)(8ξ²−ξ−1) | Correct. |
| Table A.1, Table 1 | e.g. ρ_L = 1.6: μ = 1.96, 8F = −0.44; ρ_L = 2: −2.00; ρ_L = 1.6, ρ_EI = 0.5/4 → −0.78/+0.33, zero at 2.144 | Correct. |
| C⁺/C⁻ decomposition, L122 | C⁺ = 2.5 − 1.5/(1+ρ), C⁻ = −1.5ρ³/(1+ρ): 1.50–2.00 and −0.125 to −4.00 | Correct. |
| Three-span μ, Eq. (8); main-span ν | Matches the symbolic log (`cm_3span_theory.log`); 60 FE comparisons, max relative error 7.5 × 10⁻¹² | Correct. |
| β_crit, Eq. (9) | 6β³−15β−4 = 0, casus irreducibilis (discriminant > 0); √(10/3)·cos[⅓ arccos(⅖√(6/5))] = 1.700594 | Correct. |
| Near-blind edge 1.621399 | 8F(½, μ) = 2.5 − 1.5μ = 0.2 gives μ = 23/15, hence 30β³−69β−16 = 0, root 1.6213988 | Correct. |
| 2cos(π/9) = 1.879385 | μ = 2 gives β³−3β−1 = 0; with β = 2cosθ, cos 3θ = ½, θ = π/9. Because μ_crit < 2 for every ξ > 0, F < 0 on the whole open side span when μ ≥ 2 | Correct as stated ("no side-span position gives a positive constant"). |
| Eq. (10) | 6β³/(15β+4) = 0.921 at β = 1.636; equals 1 exactly at β_crit | Correct. |
| ξ* cubic, L142 | 8ξ³−(12−3μ)ξ²+(2−μ) = 0; μ = 1 gives root ξ = 1 | Correct. Table 2 matches the log to 8 digits. |
| Mid main-span blind β = 0.964706 | ν_crit(½) = 5/4 gives 3β³+10β²−12 = 0 | The root is correct; the **wording is wrong** (B-3). |
| O_m = 0.331, Eq. (15) | Recomputed 0.33085 = 2√44765/1279; monotone decrease with ξ confirmed (0.397 at ξ = 0.1 to 0.115 at ξ = 0.9) | Correct. |
| Lab constants | I = 16 529.8 mm⁴, C_m = 61.5405 mm²/N, f1 = 11.94 Hz (m = 1.464 kg/m, consistent with A = 186.5 mm²) | Correct. |
| Tables 3/4 and C.1 | Measured trapezoidal integrals recomputed: 2513.43 / 4168.15 / 7788.93. BPM and SLM loads reproduce. Small offsets in the analytical column (≈ 7 × 10⁻⁵) come from P0 = 40.6428 N being displayed as 40.64 | Correct. |
| Cầu Mây (Table 5, Table 6, §4.2–4.3) | N_m and C_m consistent (0.181 → 4.36 × 10⁻⁵ m²/kN with EI_mid = 1.977 × 10⁸ kN m²; 0.209 → 3.61 × 10⁻⁴); pinned/fixed 0.030/0.422 → ratio 14.1; polygon checks −0.3/−0.5 % (A), −5.8/−2.6 % (I); k_FE = 2.748 × 10⁷; misfit −4.2/+3.7 %; α = 1.088 | Match `wp3_run.log`. |

### B-2. Units and notation
- Nomenclature gives L_s and L_m in m and every other length in mm. Section 4 uses m²/kN for C_m (1 m²/kN = 10³ mm²/N). Either state the conversion once or use SI throughout. Minor.
- Section 5 integrals are in mm·s (time domain) while I_y is defined in mm² (space). Introduce I_t = ∫y dt = I_y/v. Minor.
- The C_m check by influence-line area against the uniform-load route agrees to 1.1 × 10⁻⁴ for the haunched model (L253), against 10⁻¹¹ elsewhere. Explain why (influence-line sampling or quadrature in the variable-EI model). Minor.

### B-3. Blind against negative-C_m wording (the |C_m| logic)
The manuscript states the principle correctly (L120, L138: negative C_m is "formally usable"). It then contradicts it in three places:
1. **L142:** "A mid main-span sensor becomes blind only when β < 0.964706". This is wrong. The sensor is blind **at** β = 0.964706, and below it C_m is negative and nonzero (e.g. β = 0.8, ρ_EI = 1.5 gives −0.993 in `verify_3span.log`). Fix: "is blind at β = 0.964706 and has a negative constant for shorter main spans." Major (factual).
2. **§7.1 step 2, L401:** "for two spans with uniform stiffness keep ρ_L well below 1.45743". Under the paper's own indicator, ρ_L = 2 gives |N_m| = 2.0, twice the equal-span value, and R_m = C/A⁺ = −2.0/2.0 = −1, so |R_m| = 1. That is as well-conditioned as a simple span. Either justify avoiding negative C_m on other grounds (sign-reversed processing; dominance of the uninstrumented span, hence sensitivity to its EI and fixity; positive-direction drift then biases downward) or change the step to "avoid |N_m| < 0.2 on either side of the blind ratio". Major.
3. **Abstract, L138, L423 (2cos(π/9)).** The statement is mathematically correct, but it is presented as a failure ("the whole side span reads mainly the main-span load"). The precise reading is that **the side-span blind locus ends at β = 2cos(π/9)**. Beyond it no side-span location is blind, and every one has a negative constant dominated by the main span. At β = 2, mid side span, |N_m| = 0.875, which is adequate by the paper's own threshold. Say this and state what, if anything, makes the negative regime undesirable. Major (consistency of the central indicator).
4. **§7.1 step 3:** "rank locations by R_m" should be |R_m|, or R_m with a stated sign convention, because R_m < 0 beyond blindness. Minor.
5. **Supplementary-material residue.** `verify_3span.log` prints "whole side span blind when mu>=2" and `cm_3span_theory.log` prints "Whole side span blind (mu = 2 …)". The Data/Computational sections say these console logs ship as supplementary material, so they contradict the manuscript's careful wording. `docs/wp2_three_span_theory.md` and `docs/04_tong_hop…` (L17: "không vị trí nào trên nhịp biên quan sát được") make the same error. Relabel to "no positive constant on the whole side span" before release. Minor-major.

### B-4. Pier-fixity sensitivity argument
- The pinned/fixed bracket (L253, Table 5) is fine as a *bound*. "Fixed" means the girder is clamped at the pier, which decouples the spans and is not a realistic state for monolithic piers of unknown height. The argument "a design-model C_m is unusable there" (L286) needs the sensitivity at a plausible k, not between limits (A-3.2).
- **Identifiability (blocking, A-3.1).** k_FE is fitted to the *designer's FE* deflections, not to measurements. The designer's FE presumably modelled the piers somehow, so k_FE inherits an unknown modelling choice. The joint fit to the measurements gives a different (α, k) pair that fits better and removes the near-blind conclusion. With two static readings the paper cannot separate EI from k. Required: report both fits; state which constraints (pier drawings, the designer's MIDAS model, ambient frequencies) would separate them; recast the N8 conclusion as conditional. Section 7.2 already lists the "calibrated rather than measured pier stiffness", but the consequence for the headline is not stated.
- The N8 mid-side alternative (Table 5) has a range of −0.066 to 0.375, which **contains an exactly blind state**. That is a striking fact; say it.

### B-5. C_m/A⁺ indicator
- R_m is scale-free, which is its stated virtue, but that same property makes it blind to absolute signal level. N7 and N8 differ by a factor 8.2 in C_m but only 3.3 in R_m. The zero-offset error depends on C_m, not R_m (Eq. (19)).
- Suggestion: add a dimensional, decision-ready indicator, the **offset-equivalent load** P_ε = ε0·L_tot/C_m, i.e. the vehicle load at which a residual offset ε0 produces 100 % bias. For Cầu Mây with ε0 = 0.05 mm and L_tot ≈ 205 m: P_ε(N8) ≈ 234 kN against P_ε(N7) ≈ 28 kN. For a 25 t (245 kN) truck the bias is therefore about 94 % at N8 and 11 % at N7. This combines placement, baseline stability and target vehicle weight in one number. It answers "how tight must the baseline be" (L175) quantitatively, and it is the bridge-scale evidence the JCSHM editor asked for. Major (recommended addition).
- No threshold for R_m is proposed (`open_items` B2). Using it for ranking only is acceptable, but then §7.1 step 3 should not imply a pass/fail test.

### B-6. Error-budget logic
- **Bridge-scale evaluation missing.** Table 7 and Table 9 use the laboratory ratio L_tot/I_y. The paper has its own bridge, and Eq. (19) evaluated at Cầu Mây gives (red-team computation, C_m at k_FE, L_tot = 204.95 m):

  | Gauge | P (kN) | ε0 = 0.02 mm | ε0 = 0.05 mm |
  |---|---|---|---|
  | N8 | 250 | 37 % | 94 % |
  | N8 | 400 | 23 % | 59 % |
  | N7 | 250 | 4.5 % | 11 % |
  | N7 | 400 | 2.8 % | 7.1 % |

  This contradicts the "Field (SLM) 3–11 %" scenario for long-span continuous girders and should replace or supplement it. SLM does not remove this term (Eq. (18)). Major.
- **Table 9 combination rule is inconsistent.** The caption says independent terms are combined in quadrature and systematic terms summed. Recomputed: Lab SLM 0.5–1.1 % matches a linear sum (quadrature gives 0.44–1.01). Field BPM 6–19 % matches pure quadrature (5.6–18.5). Field SLM 3–11 % matches neither (quadrature 2.3–10.5; sum of systematic terms 3.5–15). In addition, the GUM [43] does not prescribe summing systematic terms: known biases are corrected, and the remaining standard uncertainties are combined in quadrature. Pick one rule, apply it to every column, and remove the GUM claim or follow it. Major.
- **L324 "partial cancellation of about 37 %".** The SLM residual 0.7297ε0 is 58 % of the BPM term 1.2596ε0, which is a 42 % reduction, and 37 % of the reference term. Reword. Minor.
- **Field ε0 assumption against the paper's own field data.** Section 5 reports a 2.06 mm baseline step and about 0.1 mm quantisation. Table 9 assumes 0.02–0.05 mm. Reconcile: state that ε0 is the post-detrending residual and give the residual actually achieved on the Gie Cuc and Phuong Do records after linear pre/post correction. Major.
- **Laboratory linearity signal not discussed.** The measured/theory integral ratio rises with load: 1.010 (40.6 N, 2513.43/2488.50), 1.016 (67 N, 4168.15/4102.14), 1.017 (125 N, 7788.9/7658.8). That rise *is* the 0.6–0.7 % SLM residual. L233 says "measured deflections exceed theory by about 1.6 %", which is true of the multi-load groups but not of the single-load record (+1.0 %). Discuss this as possible mild non-proportionality, a weight error or a positioning error, because linearity is the premise of both SLM and Eq. (2). Major.
- **Load order in the three-load group** (L201). The Appendix C record fits Eq. (A.2) only with the 2550 g load leading, followed by 5100 g at 500 mm and 5100 g at a further 250 mm (rms 0.030 mm). Reading the text as spacings of 250 mm and then 500 mm gives rms 0.55 mm. State the order explicitly. Minor.
- **Simpson rule with odd n.** The two-load record has 21 intervals (0–5250 mm at 250 mm), so Eq. (12) Simpson does not apply directly. Say how the odd panel is handled (3/8 rule). Minor.
- The beam is 5400 mm long on 2 × 2500 mm spans, so 200 mm overhangs exist. Mention them. Minor.

### B-7. Text, table and equation consistency
- Abstract and conclusions say "within 1.19 % by BPM and 0.70 % by SLM". Table 4 agrees.
- Highlights: consistent with the text, but highlight 5 overclaims (A-3.1).
- `figure_table_plan.md`: Fig. 3 must drop the Thái Bình marker (noted there), and Fig. 7 must drop the Thái Bình panels. Fig. 2 axis definition of ρ_EI should be confirmed against Eq. (5) (`open_items` B12).
- Table 6 "Measured / model" 0.977 against 0.890 (an 8.7 % difference between gauges) is reduced to a single "EI_eff/EI_design = 1.09" in L282. Report per-gauge ratios.
- L271 "about eight times less damage (Eq. (19))". Give the numbers (B-6).

---

## 4. Consolidated issue table

| # | Issue | Severity | Location | Concrete fix |
|---|---|---|---|---|
| 1 | Cover letter addressed to *Structures* | Blocking | cover_letter.md | Rewrite for the target journal; scope paragraph in that journal's words; optionally mention the JCSHM scale decision and what was added |
| 2 | `[NEED VALUE]` and reviewer tags left in text and references | Blocking | L249, L372, L413, L531, L539; refs [6], [10], [44], [45], [47] | Fill or delete; remove all bracketed notes |
| 3 | Near-blind N8 claim rests on one calibration; the joint fit to measurements (α = 0.716, k = 1.2 × 10⁸) fits better and gives N_m = 0.476, \|A⁻\|/A⁺ = 0.44 | Blocking | Abstract L15, L269, L286, L427, highlight 5 | Report both fits; discuss identifiability (2 readings, 2 unknowns); argue plausibility; make the headline conditional |
| 4 | "Fourteenfold" uses unphysical pinned/clamped limits as an uncertainty | Major | Abstract, L269, L427 | Present as a bound; add C_m over the k_FE range and ∂ln C_m/∂ln k |
| 5 | "BPM underestimates by 7–9 %" not unique; gauges disagree | Major | L282, L286, L427 | Condition on k_FE; give per-gauge ratios |
| 6 | "Blind only when β < 0.964706" is wrong | Major | L142 | "Blind at β = 0.964706; negative below" |
| 7 | Step "keep ρ_L well below 1.45743" contradicts \|C_m\| logic (ρ_L = 2 gives \|N\| = 2) | Major | L401 (§7.1 step 2), L120 | Use \|N_m\| on both sides of the blind ratio, or justify avoiding negative C_m explicitly |
| 8 | 2cos(π/9) framed as a failure; it is the end of the side-span blind locus, and \|C_m\| can be adequate beyond it | Major | Abstract, L138, L423 | Reword; give \|N_m\| at e.g. β = 2; state what is undesirable about the negative regime |
| 9 | Supplementary logs call μ ≥ 2 "whole side span blind" | Minor-major | verify_3span.log, cm_3span_theory.log (and WP2/04 docs) | Relabel before release as supplementary material |
| 10 | No bridge-scale evaluation of Eq. (19); field budget optimistic for long spans | Major | §6.2, Table 9, §4.3 L271 | Add the Cầu Mây offset-bias table (94 % N8 / 11 % N7 at 0.05 mm, 25 t); introduce P_ε = ε0·L_tot/C_m |
| 11 | Table 9 combination rule inconsistent across columns; GUM misused | Major | L374–388 | One rule for all columns; recompute; follow the GUM or drop the reference |
| 12 | ε0 meaning (absolute vs residual) and sensor technology not stated; contradicts Section 5 data (2.06 mm step, 0.1 mm quantisation) | Major | §6.2, Table 9, §5 | Define ε0 as post-detrending residual; report residual achieved on the field records; name the deflection technology assumed |
| 13 | Load-dependent lab excess (1.0 → 1.6 → 1.7 %) not discussed; "about 1.6 %" misattributed | Major | L205, L233, L235 | Report ratios per configuration; discuss linearity, weights, positions |
| 14 | SLM not credited as the Ojio–Yamada calibration | Major | §2.4 L159–163 | State the equivalence and cite [27] |
| 15 | Strain corollary missing (blind points = uniform-load contraflexure points) | Major | §2.1/§2.4 | Add a short corollary; position deflection blindness against it |
| 16 | Literature gaps: SCHM Oct-2026 continuous-girder deflection-IL paper; Winnipeg multi-span area-method study (Lydon review); [37]/[38] read beyond title | Major | §1 L54–56 | Read and cite; distinguish |
| 17 | Eq. (3) presented without a classical source | Minor | L84–88 | Cite a structural-analysis textbook |
| 18 | "Confirms" for model results; Section 5 "confirm" | Major | L288, L429 | "Indicates" / "illustrate"; say the records are simply supported spans |
| 19 | Abstract self-undermining sentence order (scale + "not a validation") | Major | L15 | Lead with bridge-scale observability and offset-bias result; keep one limitation clause |
| 20 | No scale-independence argument for the lab beam | Major | §3 intro L195 | Add the dimensionless-identity paragraph; move scale-dependent terms to bridge scale |
| 21 | Section 5 reads as padding (uncalibrated, hand-processed) | Major (perception) | L292–304 | Cut to one paragraph plus a supplement, or recast around the residual offset achieved |
| 22 | SIE: no management/decision contribution | Major (SIE only) | §1 L50, L60; §7 | Add a monitoring-planning and decision paragraph and a worked decision table; move derivations to an appendix |
| 23 | Keywords lack SHM terms | Minor | L17 | Add "Structural health monitoring", "Sensor placement" (SCHM) or "Bridge management" (SIE) |
| 24 | R_m ranking sign convention | Minor | §7.1 step 3 L402 | Use \|R_m\| or state the sign rule |
| 25 | "Partial cancellation about 37 %" | Minor | L324 | Reword (42 % reduction of the BPM term) |
| 26 | Three-load axle order ambiguous | Minor | L201 | State the order (2550 g leading; 500 mm then 250 mm) |
| 27 | Simpson with odd interval count | Minor | L167, L408 | Specify the 3/8 end panel |
| 28 | Units: m vs mm, mm² vs mm·s, m²/kN | Minor | Nomenclature; §4–5 | Unify or state conversions; define I_t |
| 29 | 1.1 × 10⁻⁴ route agreement unexplained | Minor | L253 | Explain the source |
| 30 | Overhangs (5400 vs 2 × 2500 mm) | Minor | L199 | Mention |
| 31 | Possible overlap with the authors' two papers under review at *Structures* (same rig or data?) | Major (ethics check) | Cover letter, §3 | If any data or text overlap, cite or disclose in the cover letter |
| 32 | SCHM APC with "no funding" declared | Practical | — | Check APC and waiver eligibility before choosing SCHM |

---

## 5. Recommendation

**Target SCHM first, with SIE as the fallback.**

Reasons:
1. SCHM's stated scope ("structural health monitoring theory … system identification, signal processing, sensor technology … measurements") matches the paper's real contribution: an observability and sensor-placement criterion for a monitoring channel, together with a measurement-error analysis. SIE's scope is maintenance, management and life cycle. Fitting SIE requires a larger rewrite (issue 22) and still leaves the mechanics-heavy core looking off-centre.
2. SCHM has just published a deflection-influence-line paper on continuous beam bridges, which shows the topic is in scope.
3. SCHM is less tied to "structural scale" than JCSHM, but the risk is the same in kind. The fixes in issues 10, 19 and 20 (bridge-scale Eq. (19), P_ε, the scale-independence paragraph) are aimed at that risk.
4. Cost: SCHM is gold OA with an APC, and the paper declares no funding. If the APC cannot be paid, SIE becomes the primary target.

**Estimated desk-pass probability:**

| Journal | Now (as written, after only fixing the cover letter and placeholders) | After all blocking and major fixes |
|---|---|---|
| SCHM | about 35 % | **about 60 %** |
| SIE | about 25 % | **about 45 %** (about 50 % if the management reframing of issue 22 is done thoroughly) |

These are judgement estimates, not data. The largest single lever is issue 3 together with issue 10: a Cầu Mây result that holds up under both calibrations, plus a quantitative bridge-scale consequence. That moves the paper from "lab beam plus static check" to "design-stage observability analysis of a real continuous girder", which is what both editors look for.
