# Associate Editor assessment (structural mechanics): manuscript v4, SCHM

**Title:** Blind loci and design criteria for integral load-monitoring channels on continuous girder bridges, with laboratory verification and an assessment on public field records

**Assessor's angle:** mechanics of continuous and haunched box girders, closed-form beam theory, FE modelling. I read the manuscript, the Supplementary Material, the cover letter and Figs. 1–9. I checked the mathematics independently with my own scripts (scratch directory `/tmp/claude-0/-home-user-SHM-Paper1-1D/e0d84659-e833-593b-82ad-e0ad845000cf/scratchpad/ed3/`: `c1.py`, `c2.py`, `c3.py`, `cm.py`, `lab.py`), and compared the results with the authors' logs.

---

## 1. Decision

**Return before review (reject in present form, resubmission encouraged once the missing experiment is done).** If it were sent out now, I would expect major revision at best, more likely rejection.

The mathematics is correct. I reproduced every closed form I checked and the main numbers for the in-service girder with an FE model I wrote myself. The paper is also unusually candid about what its data cannot show. The problem is the distance between what is claimed as new and what is shown experimentally. The new items are the blind loci, the near-blind bands, the indicators $N_M$ and $R$, the vertex placement rule and the Möbius identifiability law. Each is a short consequence of the classical identity $C_m = y_m[q_0]/q_0$, three-moment analysis, a convex-on-a-box argument or a rank-one (Sherman–Morrison) update. None of the three experimental parts tests any of them:

- The laboratory test is static, on equal spans, with one gauge. It checks only the classical identity (to about 1 %), and the predicted blind configuration (2500 + 3644 mm) was not built.
- The public field records come from deck-soffit strain gauges far from any zero-moment point. The reference weights hardly vary, so the mean-weight predictor beats every estimator. Invariance can be bounded only to 10–27 %, and the multi-channel result is a negative one from eight runs.
- The in-service bridge has two static dial-gauge readings and a 1-D model. Its decisive measurements (Table 6) are predictions, not results.

As it stands, the paper is a correct but incremental theory note with three validation exercises that do not touch its contributions. SCHM reviewers will say exactly this, so a review round now would cost everyone time. A moving-load test of a blind or near-blind configuration, in the laboratory (cheap: the authors already have the rig) and/or the moving-load test already designed for Cầu Mây, would change the assessment substantially.

## 2. Scores (1–10)

- **Technical soundness overall: 6.** The derivations and numerics are correct, but the evidence does not support the stated contributions, and the in-service identifiability rests on an internally inconsistent tolerance and a physically implausible part of the admissible set.
- **Theory: 7.** Correct and well verified (981 FE checks, which I reproduced in part). Novelty is modest. The pier model (rotational spring only) leaves out frame action.
- **Laboratory verification: 4.** Static loads, equal spans, one LVDT, a three-load order inferred from the data, and no test of the blind or near-blind configuration. Deviations of about 1 % confirm only Eq. (2).
- **Field assessment (NOR-BWIM): 4.** Honest statistics, but the data cannot test weight discrimination, blind loci, deflection channels or placement. Deck-soffit gauges violate the 1-D assumption (ch11/ch8 = 3.9 against a predicted 1.0). Day-1 weights are driver-reported, and day-1 speed is confounded with truck.
- **In-service bridge application: 5.** The mechanics are reproducible and correct, but the analysis uses only two static readings, truck positions are not provided, the headline "factor 6.6" depends on $\alpha \approx 0.5$, and the discriminating test is only predicted.
- **Clarity of presentation: 6.** Well organised, but very dense in numbers, with about 40 nomenclature entries, more than 10 supplementary tables and frequent forward references. The abstract is a list of results rather than a message.

## 3. Results of my own checks

**Closed forms, prismatic (SymPy and NumPy, `c1.py`–`c3.py`).** All hold:

| Item | Check | Result |
|---|---|---|
| Eq. (4), $\mu_\mathrm{2span}$ | three-moment equation, unequal $L$, $EI$ | exact |
| Eq. (4), $\mu_\mathrm{3span}$ | three-moment equation, symmetric | exact |
| Eq. (5) | superposition of the simply supported deflection and the hogging end moment | exact |
| Eq. (6) | solve $F = 0$; $\mu_\mathrm{crit}$ falls monotonically from 2 to 1, so $1<\mu<2$ | exact |
| Eq. (7) | $3\lambda^2-3\lambda-2=0$ gives 1.457427; $8\xi^2-\xi-1=0$ gives 0.421535 | holds |
| Eq. (8) | trigonometric root 1.700594, residual of $6\beta^3-15\beta-4$ about 1e-15 | holds |
| End of the locus at $2\cos(\pi/9)$ | $\mu_\mathrm{3span}=2$ there (end rotation zero) | holds |
| Deflection bands | three spans 1.6214–1.7750; two spans 1.3851–1.5247 | hold |
| Eq. (9), strain band | equal two spans 0.6760–0.8116 (0.19–0.32 from the pier); $|N_M|=\mu$ at the support | holds |
| Table 1 | main-span strain zero 0.2764 ($\beta=1$) and 0.1767 ($\beta=1.636$); rotation end $\lambda=1.6180$; pier $\beta=\sqrt{3/2}$ independent of $\gamma$; shear at $\xi_0/2$; end reaction $\lambda=2.3028$, $\beta=2.6691$; $N_F=\xi_0$ | all hold |
| Appendix A | mid main-span blind $\beta=0.96471$; $\xi^*$ cubic; contributions 1.50–2.00 and −0.125 to −4.00 | hold |
| Eq. (16) | independent slope-deflection derivation with the spring sign fixed by joint equilibrium | identical, symbolic difference 0 |
| §2.5 values | side span at $\xi=0.4$: 0.2870 (pinned) → 1.0368 (fixed); mid main span 0.7546 → 0.5000 | hold |
| §2.3, $R$ | $R_w=4/7=0.571$, $R_\varepsilon=2/3$ (equal two spans, mid-span) | hold |
| Eq. (14) | derived from the constrained minimisation (zero-sum removes the $\rho$ term); white-to-offset ratio $4.5\times10^{-6}$ | holds |

**Eq. (15), Möbius law.** I derived it independently with Sherman–Morrison. It holds for any gauge position, including an off-axis one, provided the load is mirror-symmetric. On the haunched model it matches my FE to 1e-8 relative.

**Table A.1.**

| $\beta$ | 1.0 | 1.2 | 1.4 | 1.5 | 1.7 |
|---|---|---|---|---|---|
| Verified to all digits | yes | yes | yes | yes | yes |

The row labelled $\beta = 1.636$ was actually computed at $\beta = 90/55 = 1.63636$:

| | Printed | At 90/55 | At 1.636 exactly |
|---|---|---|---|
| $\mu$ | 1.558 | 1.5579 | 1.5573 |
| $\xi^*$ | 0.2994 | 0.2994 | 0.2996 |
| $N_w(\xi^*)$ | 0.3316 | 0.3316 | 0.3323 |
| $N_w(1/2)$ | 0.1632 | 0.1632 | 0.1641 |

This is a labelling inconsistency, not an error of substance.

**Cầu Mây, independent FE (`cm.py`).** My model: Hermite elements at 0.25 m, $h = 2.4 + 3(1-s/44)^2$ m within 44 m of each inner pier, $I \propto h^{2.943}$, $E = 36\,057$ MPa. It reproduces the authors' values:

| Quantity | Manuscript | My FE |
|---|---|---|
| Table 4, prismatic pinned: N8 0.4L / N8 mid / N7 | 0.287 / 0.163 / 0.755 | same |
| Table 4, calibration A | 0.181 / 0.105 / 0.209 | 0.182 / 0.105 / 0.209 |
| Table 4, calibration B | 0.476 / 0.377 / 0.234 | same |
| Table 5, $R$ prismatic | 0.14 / 0.08 / 0.70 | 0.144 / 0.079 / 0.699 |
| Table 5, $R$ calibration A | 0.18 / 0.11 / 0.59 | 0.183 / 0.111 / 0.587 |
| Table 5, $R$ calibration B | 0.56 / 0.49 / 0.77 | 0.556 / 0.489 / 0.772 |
| $k_g$ | 4.36e7 kN m/rad | 4.359e7 |
| $\kappa_A/k_g$ | 0.63 | 0.631 |
| $C_\infty/C_0$ at N8 / N7 | 14.0 / 0.59 | 13.99 / 0.592 |
| $B_m$ at N8 / N7 | 0.51 / 0.12 | 0.511 / 0.115 |
| Table 6, integral ratio A / B | 0.121 / 0.284 | 0.1213 / 0.2836 |

The haunched pinned and fixed rows of Table 4 are extremes over the model-form variants, so the base model differs from them: pinned 0.030 / −0.052 / 0.248, fixed 0.422 / 0.354 / 0.147. That is consistent with the caption but confusing (see minor points).

Unit conversions also hold: $C_8 = 3.0\times10^{-5}$ to $2.0\times10^{-4}$ m²/kN from $N_w$ = 0.124–0.822, and the factor 6.6. **Table 7** holds, with $P = 245.8$ kN: at 0.1 mm, N7 gives 16.3–24.7 % and N8 41–271 %. **§5.3** holds: 24.8 % (220 m) and 22.5 % (200 m) for N7 alone.

**Laboratory (`lab.py`).** $I = 16\,530$ mm⁴ and $C_m = 61.54$ mm²/N hold. The trapezoid bias of the exact influence line is −0.500 % (−0.492 % from the rounded column of Table S1). Measured/exact = 1.00496, and BPM/SLM equals this factor in both configurations. Measured/analytical ratios are 1.0099, 1.0160 and 1.0169. Table 2 BPM values (+1.10 %, +1.19 %) hold. SLM: 67.40 N (+0.61 %) holds; for three loads I get 125.94 N (+0.69 %) against 125.95 N (+0.70 %) printed. The difference is rounding or the value of $P_0$, which is immaterial.

**Errors found:** none of substance in the equations or tabulated values I checked. The only discrepancy is the β label in Table A.1 (1.636 against 90/55). One equation is missing: the main-span end moment with pier springs, $\bar M_\mathrm{main} = 2(\beta^3\hat k + 3\beta^3 + 3\gamma)/[3\beta^2(\beta\hat k + 3\beta + 2\gamma)]$. It is needed for the main-span values in §2.5, but only Eq. (16) for the side span is given, and Appendix B's $(\mu/\beta^2, \mu/\beta^2)$ is valid only for pinned piers.

## 4. The five most serious technical problems (ranked)

**1. None of the experiments tests the paper's own contributions.** The laboratory confirms the classical identity under static loads on equal spans. The field records have no gauge near a blind point, no deflection channel and no weight spread. Cầu Mây gives predictions only. The blind/near-blind loci, the conditioning indicators, the vertex placement and the Möbius identifiability are therefore unvalidated beyond the authors' own FE, which checks algebra, not physics.
*Fix:* (a) Test the two-span blind and near-blind configuration in the laboratory (2500 + 3644 mm, plus one span ratio inside the band, e.g. λ = 1.40 and 1.50). Use moving or stepped loads and at least two deflection gauges, one at $\xi^*$ and one near the support, to show the predicted collapse of $C$, the amplification of error as $1/|C|$, and the zero-sum pair. (b) Carry out the Cầu Mây moving-load test with weighed trucks and report the N8/N7 integral ratio and the pier rotation against Table 6.
**New experiments are needed.** At minimum (a); (b) is what would make §5 a result instead of a forecast.

**2. The headline identifiability result at Cầu Mây depends on an inconsistent tolerance and on physically implausible models.** The "factor 6.6" (abstract, §5.2, Conclusion 5) comes from an admissible set that reaches $\alpha = 0.51$, a 49 % loss of rigidity in a recently built prestressed girder. With the authors' own prior $\alpha \in [0.9, 1.3]$ (Table S7) the N8 indicator spans only 0.12–0.30, a factor of about 2.5. The tolerance τ = 5.3 % combines a "measurement" term (1.97 %) with a model-form standard uncertainty of 1.75 %. But the measurement term is a transverse-position scatter that the authors themselves say is not repeatability, and the 1.75 % model-form term contradicts their own demonstration that model-form error leaves a 4–9 % residual in $r_{87}$ that no κ removes. So the tolerance is not defensible from either side, and the conclusion changes with it (at τ = 3 % the set excludes α = 1).
*Fix:* Use a physically bounded prior on α (from concrete-modulus tests or the design creep/cracking assumptions), and derive τ from an explicit model-form study, in which the 4–9 % residual must enter. Report the identifiability (preferably as a profile likelihood or Bayesian posterior of $\ln C_8$, not only local Cramér–Rao bounds, which are singular at B) for that prior, and restate the headline accordingly. Tabulate the longitudinal truck positions; at present calibrations A and B cannot be reproduced from the Supplementary Material (Tables S8–S10 omit them). No new experiment is needed for this item.

**3. The monolithic pier is modelled as a pure rotational spring, and the 1-D Euler–Bernoulli model leaves out effects of the same order as the quantities it is meant to identify.** A pier monolithic with the girder acts as a frame. Vertical load produces pier-top shear and an axial force in the main-span girder, and the pier contributes a coupled rotation–translation stiffness, not $kK_p$ with a single scalar. The axial force shifts the strain zeros (§5.3, Fig. 8b–c) and changes the stiffness structure on which the Möbius law and the $\kappa = k/\alpha$ reduction rest. In addition, a box girder of depth 5.4 m on a 55 m side span ($L/h \approx 10$ near the piers) has shear deformation, shear lag and haunch-induced shear (Résal effect) at the level of several per cent. These are plausible sources of the unexplained 4–9 % $r_{87}$ residual. The depth law and the exponent are assumed, not documented.
*Fix:* Add a frame model (pier columns with foundation flexibility, bearings at T5/T8) and a Timoshenko or shell/3-D check of the haunched girder. Show how the $r_{87}$ minimum, the admissible set and the strain zeros change. State explicitly that Eq. (15) holds only for a single scalar rotational spring per pier and for symmetric loading. No new experiment is needed (design drawings and FE).

**4. The field assessment cannot carry the conclusions drawn from it, and the 1-D strain theory does not transfer to deck-soffit gauges.** The NOR-BWIM gauges sit on the soffit of the top slab and respond to slab bending and shear lag (ch11/ch8 = 3.9 at 6 m spacing against a 1-D prediction of about 1.0). Eq. (3) and the strain blind loci, which hold for girder-level bending strain, therefore do not describe them. The weights vary by a few per cent, day-1 weights are driver-reported, speed is confounded with truck (correlation 0.98), and the space integral assumes constant speed over a 605 m crossing that lasts 20–45 s, with speed variation not measured. The GLS/zero-sum "finding" rests on eight runs and a 4×4 covariance. It is a useful caution, but it is a well-known consequence of estimating Σ from the wrong population, not a property of continuous girders.
*Fix:* Reframe §4 as a limited plausibility check (or move most of it to the Supplementary Material). Add a sensitivity analysis of the integral to speed variation (e.g. using the axle-spike speeds at both ends if available). Remove claims that rely on gauge-level 1-D behaviour, and add a test with web or bottom-flange gauges or deflection, ideally with trucks of clearly different weights. **A new field data set is needed** if the paper is to claim any estimator performance; otherwise the claims must be cut back.

**5. The design criteria are conventions not tied to an error requirement, and the placement rule rests on idealised noise.** The 0.2 threshold means 8 % for deflection and 20 % for strain relative to the simply supported value. The authors acknowledge this but keep it as the main design criterion (Table 1, workflow step 2), although Eq. (12) already provides a physically meaningful criterion, $P_\delta$ against the lightest vehicle to be screened. The vertex placement rule assumes position-independent noise and allows several sensors at the same extreme with independent offsets, which is unrealistic for co-located sensors. The statement that the white-noise price of zero-sum weights is negligible (5 × 10⁻⁶) holds only if $1-\rho \gg 5\times10^{-6}$; in the $\rho \to 1$ regime that motivates zero-sum weights, white noise dominates (as Fig. 4c shows).
*Fix:* Replace the 0.2 threshold by a requirement on $P_\delta$ or $\sigma_P$ for a stated offset or resolution. Give the near-blind bands as functions of that requirement. Add position-dependent noise and a minimum sensor spacing to the placement study. Qualify the zero-sum statement. No new experiment is needed.

## 5. Minor technical points

1. Table A.1: the row labelled $\beta = 1.636$ is computed at $\beta = 90/55$. State "1.636 (= 90/55)" or recompute.
2. Give the main-span end moment with pier springs, $\bar M_\mathrm{main}(\hat k)$ (Section 3 above). Appendix B's $(\mu/\beta^2, \mu/\beta^2)$ holds only for pinned piers.
3. Table 4 mixes base-model rows (calibrations A and B) with extremes over model-form variants (haunched pinned/fixed). This produces the apparent anomaly that calibration B (0.476) exceeds "fixed" (0.446). The base-model fixed value is 0.422 and pinned 0.030. Give base-model rows and put the variant envelope in a separate column.
4. "Deviates from the measurements by +2.4 % / +12.3 %": state the sign convention (model/measured − 1 or the reverse).
5. The Cramér–Rao bounds are local. At B the Fisher matrix is singular by construction (minimum of $r_{87}$), so a bound "with the tiltmeter, 0.04" at that point says little. Use a global measure.
6. Pier rotation: §5.3 gives 167 µrad "under the side-span convoy", Table 6 gives −58/−29 µrad for one truck. Define both loadings in one place.
7. The frequency argument (3.43–3.64 Hz "if they belonged to the third mode") is speculative. Either support the mode assignment with mode shapes or drop it from the main text.
8. The dynamic bound ($t_\mathrm{cr}/T_1 \ge 8$) comes from a constant force on an 11.9 Hz laboratory beam. For long spans it is trivially satisfied, and the real dynamic error comes from vehicle–bridge interaction and roughness, which are excluded. Say so in the workflow.
9. Laboratory: the three-load order was chosen by best fit, so that configuration is not independent. Report the two-load result as the primary test, and give the LVDT repeatability (three cycles are averaged, but their spread is not given).
10. Eq. (3) on a haunched girder: on an inclined soffit, $c$ and the neutral-axis position vary with $x$, and the haunch introduces a vertical component of the flange force. The gain $c/EI$ with $c \propto h$ (Fig. 8c) is a rough assumption; use actual section properties.
11. Eq. (12) treats $\delta_0$ as constant over the record after linear re-zeroing. A residual drift with zero mean at both ends but nonzero integral (e.g. thermal curvature during the crossing) is the realistic case. Model it as a random process.
12. §4.2: "zeros 35 m from the gauges" is 32.3 and 36.9 m (Table S3 notes); give both.
13. Workflow step 6 recommends SLM, which removes the structural terms. The paper should state clearly that the §5 identifiability problem matters only for BPM. With SLM, the relevant issue for N8 is the magnitude of $|C|$ relative to the offset (Table 7), which already rules N8 out.
14. The near-blind band of rotation and shear channels is not given; Table 1 lists only blind loci for them.
15. Nomenclature: $L$ and $l$ for spans of different objects, $\mu$ and $\nu$ (Appendix A) for related quantities, and $\kappa$ against $\hat k$. Consolidate.
16. Data availability: the Cầu Mây truck positions (drawings) and the haunch geometry are needed for reproducibility. Include them in the Supplementary Material.
