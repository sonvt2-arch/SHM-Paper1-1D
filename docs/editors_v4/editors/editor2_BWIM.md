# Associate Editor assessment (BWIM / moving-force identification / influence lines)

**Manuscript:** "Blind loci and design criteria for integral load-monitoring channels on continuous girder bridges, with laboratory verification and an assessment on public field records" (Nguyen, Vu, Nguyen), submitted to *Structural Control and Health Monitoring*.

**Material read:** manuscript v4, Supplementary Material, cover letter, Figs. 1–9 (PNG). Spot checks: closed forms of Eqs. (6)–(8), Table A.1 and the strain near-blind band recomputed independently; field estimator log `code/norbwim/logs/v4.log` and speed diagnostics in `code/norbwim/logs/field.log` compared with Table 3 and Supplementary Tables S5–S6.

---

## 1. Decision

**Return before review (to restructure and resubmit), not send out in its present form.** If the Editor-in-Chief prefers to send it, I expect **major revision tending to reject**.

The writing is careful and unusually frank. The closed forms are correct (I reproduced λ_crit = 1.4574, ξ* = 0.4215, β_crit = 1.7006, the end of the locus at 2cos(π/9), N_w(β = 1.636, ξ = 0.5) = 0.164 and the two-span strain band 0.676–0.812). The trouble is the evidence behind the claims. The paper makes three claims. Its theoretical core, the blind loci and near-blind bands, follows in one or two lines from the classical identity the authors themselves call textbook: C equals the response to a uniform unit load, so a strain gauge is blind at the contraflexure points of the uniform-load moment diagram. No experiment tests these loci. The laboratory beam has equal spans and the blind configuration was not built. The field gauges lie about 35 m from any zero-moment point and are strain, not deflection, gauges. The second claim is the field "assessment of what estimators can deliver". On these data no estimator beats a constant predictor (MAE 2.0–2.2 %), because the reference weights differ by only a few per cent. The invariance tests resolve nothing finer than 10–27 %. With n = 7–8 runs, the field part therefore cannot assess weighing performance at all. The third claim is the Cầu Mây identifiability study. With two parameters and two averaged readings, it is a textbook non-identifiability. Its headline figure (a factor of 6.6 on C₈) depends on admitting α ≈ 0.5, which the authors themselves call implausible; with a prior α ∈ [0.9, 1.3] the range collapses (Table S7). Each of the three parts is a reasonable conference-length note. Stapled together, none is carried to the point where a BWIM reviewer would see a validated advance. A focused resubmission could be worth reviewing. Options are (a) the design-criteria paper with a physical test at or near a blind configuration and a comparison against influence-line BWIM on the same records, or (b) the identifiability paper with the moving-load test the authors say they have designed.

## 2. Scores (1–10)

- **Novelty relative to the BWIM literature: 3/10.** A useful compilation, but every ingredient is classical or standard: the influence-area identity, contraflexure points, GLS/BLUE, differential measurement, Sherman–Morrison reanalysis, and the trade-off between EI and support stiffness in static tests. The genuinely new items are specific closed-form numbers and the "near-blind band" convention.
- **Technical correctness of the BWIM-related parts: 6/10.** The algebra and FE checks are sound and the GLS analysis is honest. Three problems lower the score: (i) a local speed is used to convert a 605 m time integral to space, and the authors' own log shows a whole-record speed 14 % higher than the axle-spike speed (SD 12 %); (ii) failure to reject is presented as consistency (χ² with n = 7–8); (iii) a few reporting inconsistencies (see Problem 5).
- **Honesty and adequacy of the field assessment: 6/10.** It is honest: negative results are reported, along with confidence intervals and the mean-weight baseline. It is not adequate. The data cannot test the paper's central claims, there is no influence-line BWIM baseline on the same runs, and the framing (title, contribution 5, cover letter) still promises more than the data give.
- **Relevance to practice: 4/10.** Telling practitioners to keep strain gauges away from contraflexure points and to calibrate per lane and per gauge with weighed trucks is sound but already standard practice. The error budget (Table 7) shows that single-point integral weighing on long spans is marginal even at the best location. That undercuts the practical case for the method the criteria are designed for.

## 3. The five claimed contributions

**C1. Closed-form catalogue of blind loci (deflection, strain, rotation, shear, reaction; two-, three-span and haunched; near-blind band). Verdict: partly new (compilation and specific numbers new; the principle known).**

- That C is the uniform-load response, and hence that a channel is blind where the uniform-load response vanishes, is the classical identity the authors cite: Ghali, Neville & Brown, *Structural Analysis* (CRC, 2017), and Ojio & Yamada, ICWIM3 (2002). Contraflexure of the uniform-load moment at 0.75L in two equal spans (0.25L from the interior support) is tabulated in every structural-analysis text. "Strain gauges are blind at zeros of M_q" is that fact restated.
- The cancellation problem for area-based weighing on continuous bridges is explicitly identified, with a work-around (absolute-value area), by Deng, Liu, Huang & Kaewunruen, *Appl. Sci.* 15(11) (2025) 6028 [44].
- Integration-based GVW on multi-span and continuous bridges, with gauges placed at positive-moment regions, appears in Cardini & DeWolf, *J. Bridge Eng.* 14(6) (2009) 418 [24], Helmi, Bakht & Mufti, *JCSHM* 4 (2014) 195 [25] (seven-span) and Yamaguchi et al., *Adv. Struct. Eng.* 12(1) (2009) 115 (two-span continuous BWIM; not cited).
- Shear and reaction channels for indeterminate bridges: Bao, Babanajad, Taylor & Ansari, *J. Bridge Eng.* 21(1) (2016) 04015029 (shear-strain BWIM explicitly for determinate and indeterminate bridges, including a box girder; not cited); Lobo-Aguilar & Christenson (2018) [30].
- Ill-conditioning of sensors near nodal or zero points in moving-force identification on continuous bridges: Zhu & Law, *MSSP* 20(7) (2006) 1759 [19].
- What is new: the closed-form deflection blind span ratios (λ = (3+√33)/6, β = 1.7006), the endpoint 2cos(π/9), and the identity N_F = ξ₀. These are correct, but they are exercises in three-moment algebra, and the 0.2 threshold defining the "near-blind band" is a convention, not a derived quantity.

**C2. Strain indicator N_M, cancellation ratio R, normalisation of N_w. Verdict: largely known; R is a minor new definition.**

- N_M = 8M_q/(q₀L²) is the moment coefficient relative to the simple-span moment, which appears in standard tables of beam coefficients (Ghali et al. [38]; also design-code moment-coefficient tables). That it needs no reference rigidity is immediate.
- R = C/A⁺ (net over positive influence area) is a sensible descriptor, and I know of no BWIM paper that defines it under this name. Deng et al. (2025) [44] used the ratio of net to absolute area implicitly to motivate their absolute-area method, and Döring et al., *Infrastructures* 8(4) (2023) 72 [35] used ratio-based integrated influence lines as features.
- The observation that N_w = 2.5 versus N_M = 1 at a simply supported mid-span is editorial housekeeping, not a contribution.

**C3. Placement rule: optimal sensors at the extremes of the uniform-load response. Verdict: known.**

- Placing the gauge where the response per unit load is largest (mid-span of the main girder) is standard BWIM practice. See COST 323 (Jacob, OBrien & Jehaes, 2002) [7], Žnidarič & Baumgärtner, "Bridge weigh-in-motion systems — an overview", *Proc. 2nd European Conf. on WIM*, Lisbon (1998), and Ojio & Yamada (2002).
- The argument itself, that a convex quadratic on a box is maximised at a vertex, is the standard result for maximum-SNR / D-optimal design with a scalar parameter (e.g., Udwadia, *J. Eng. Mech.* 120(2) (1994) 368, "Methodology for optimum sensor locations for parameter identification in dynamic systems").
- Differential (zero-sum) measurement against a reference is the authors' own admitted textbook item.
- A more general BWIM sensor-placement formulation already exists: Zhou, Demartino, Narazaki, Xu, Chatzi & Spencer, *MSSP* 241 (2025) 113522 [45].
- The only new nuance is to use cM_q/EI rather than M_q on haunched girders, which is the definition of strain.

**C4. Identifiability under pier stiffness; Möbius law in κ = k/α; naming the resolving measurement. Verdict: partly new (application new; mathematics known).**

- That static responses scale as f(k/α)/α is degree −1 homogeneity of the stiffness matrix αK_g + kK_p, which is trivial.
- The linear-fractional dependence on a single spring stiffness is the Sherman–Morrison rank-one reanalysis result. See Akgün, Garcelon & Haftka, "Fast exact linear and non-linear structural reanalysis and the Sherman–Morrison–Woodbury formulas", *IJNME* 50(7) (2001) 1587–1606, and Kirsch, *Reanalysis of Structures* (Springer, 2008).
- Non-identifiability of EI versus boundary or bearing restraint from a few static readings is well known in load testing and static model updating: Sanayei, Imbaro, McClain & Brown, *J. Struct. Eng.* 123(6) (1997) 792; Bakht & Jaeger, "Bridge testing — a surprise every time", *J. Struct. Eng.* 116(5) (1990) 1370.
- Recommending a pier tiltmeter, or an extra frequency, to break the trade-off follows standard Fisher-information reasoning.
- What is new: applying these known results to the integral constant of a BWIM channel, and the quantitative Cầu Mây case. The case rests on only two averaged readings, with longitudinal truck positions "given as drawings in the test report and not tabulated", so it is not reproducible from the Supplement.

**C5. Assessment on a laboratory beam and public moving-truck records. Verdict: partly new as data analysis; adds little evidence.**

- The laboratory test (static weights on a 2 × 2.5 m tube, three load cases, one of which had its load order fixed by the data) only confirms superposition. That does not need confirmation.
- The NOR-BWIM data [49] have already been processed with influence-line BWIM by their authors: Moghadam, AlHamaydeh & Sarlo, *Autom. Constr.* 137 (2022) 104179; *J. Struct. Integr. Maint.* 8(2) (2023) 79; *Autom. Constr.* 148 (2023) 104768 [41–43]. Re-analysing the same data with integral estimators is new, but the outcome is that no estimator beats the mean weight.
- The GLS finding (a covariance estimated from vehicle-free noise mis-specifies crossing-to-crossing error) is a correct and useful caution, but it is the generic misspecification problem. BWIM errors are known to be dominated by vehicle dynamics, transverse position and local deck effects, not sensor noise. See OBrien, Žnidarič & Ojio, "Bridge weigh-in-motion — latest developments and applications world wide", *ICWIM5* (2008), and Žnidarič, Kalin & Kreslin, *SIE* 14(4) (2018) 412 [11].
- Lane- and gauge-specific constants are known: Wu et al. (2020) [40] and Yamaguchi et al. (2009).

## 4. The five most serious problems (ranked) and concrete fixes

**1. The experimental evidence does not test the paper's central claims.**
The novelty sits in the blind loci, near-blind bands and placement rule. But the laboratory blind configuration (2500/3644 mm) was not tested, the field gauges are far from any zero-moment point, and no deflection pair exists in the field.
*Fix:* Test the laboratory beam at, and either side of, the predicted deflection blind ratio. This rig needs only a support moved to 3644 mm. Add a strain gauge in the near-blind band 0.19–0.32L from the interior support, and show the predicted loss of conditioning under repeated moving or stepped loads. Alternatively, find a field data set with gauges near contraflexure; several published continuous-bridge BWIM installations exist. Without this the paper is a theoretical note and should be framed and titled as such: drop "laboratory verification" from the title.

**2. The field assessment cannot discriminate weights, and there is no BWIM baseline.**
Reference GVWs span only about 2–4 %, so the mean-weight predictor beats every estimator. The day-1 weights are driver-reported, n = 7–8, and on day 1 speed is confounded with truck (r = 0.98). "Consistency" is inferred from failure to reject χ² and TOST at margins of 10–27 %. As it stands this is a data-quality report, not an assessment of "what integral estimators can deliver".
*Fix:* (a) Run a standard Moses/OBrien influence-line BWIM, with the influence line calibrated from the same calibration runs (OBrien et al. 2006 [9]), on exactly the same LOO folds. The integral estimators then have a meaningful comparator; the 4.6 % from [42] on different runs is not one. (b) Report results against the COST 323 accuracy classes [7]. (c) Either find records with weight spread (the Smart Road also has other campaigns; the dissertation [50] lists additional runs) or demote Section 4 to a short "consistency check" and remove contribution 5 as a claimed novelty.

**3. Conversion from time to space over a 605 m crossing uses a local speed, contrary to the paper's own requirement that the integral be taken in space.**
Section 2.4 and Appendix B correctly state that a time integral weights space by 1/v(x). Yet each record is converted with the speed measured from axle spikes at the gauges, over a 605 m, roughly 25–60 s crossing in which span 2 contributes 170 % and the adjacent spans −92 % of the net integral. The authors' log `code/norbwim/logs/field.log` reports a whole-record low-pass fitted speed / spike speed ratio of median 1.139, SD 0.124 (n = 22). That points to speed variation along the bridge, or to a model mismatch of the same order as the errors reported in Table 3. The manuscript says only that "speed variation over a 605 m crossing was not measured" and that speeds agree with the dataset script within 1–2 %, but that script is also local.
*Fix:* Report this diagnostic in the paper. Estimate v(x) from the arrival times of the global response at several stations, or from the fitted global shape, and integrate in space with v(x). Quantify the effect on Tables 3 and S2–S6. If it cannot be resolved, state explicitly that the speed term is a dominant, unquantified error source in Table 8. Cite the BWIM work on non-constant speed (Lansdell, Song & Dixon, *Eng. Struct.* 152 (2017) 709).

**4. The novelty claims overstate what is derived; the paper should be rebalanced.**
The paper concedes that the identity and GLS are standard. Even so, contributions 1–4 are presented as "criteria", although each is a one-step consequence of known results: contraflexure points, moment coefficients, the vertex of a convex quadratic, Sherman–Morrison and homogeneity. The Möbius law is presented as a named result without citing structural reanalysis.
*Fix:* Cite Akgün et al. (2001) and Kirsch (2008) for the rank-one law, Sanayei et al. (1997) and Bakht & Jaeger (1990) for EI–restraint non-identifiability, Bao et al. (2016) for shear channels on indeterminate bridges, and Yamaguchi et al. (2009) for continuous-bridge BWIM. Then restate the contributions honestly, for example as "a design checklist with closed-form values" plus "a quantified non-identifiability case". Move the obvious items (N_w normalisation, convexity) out of the contribution list. Shorten Section 2 accordingly.

**5. The Cầu Mây headline is inflated, the case is not reproducible, and several reported numbers are inconsistent.**
- The factor of 6.6 on C₈ (abstract, Section 5.2, Conclusions) comes from an admissible set with α down to 0.51. The authors themselves describe such a value as a 28 % loss of rigidity, implausible for a new prestressed girder, and that is at 0.716. With a prior α ∈ [0.9, 1.3] the N8 indicator range shrinks to 0.12–0.30 (Table S7).
- The tolerance τ = 5.3 % mixes transverse-position scatter, which the authors admit is not repeatability, with an assumed 1.75 % model-form term.
- The longitudinal truck positions are not tabulated, so a reader cannot rerun the identification.
- Reporting inconsistencies: Supplementary S3 gives GLS with residual covariance as "10.4 % in sample, 28.4 % out of sample". These are RMS values (log: LOO MAE 23.4 %, RMS 28.4 %; in-sample RMS 10.4 %, MAE 8.5 %), whereas every table uses MAE.
- Fig. 7 labels estimators "immune"/"immune-eq", but the text calls them "zero-sum".
- Fig. 7c is titled "12 gauges" but shows only two single gauges.

*Fix:* Headline the plausible-prior range and give the 6.6 only as the no-prior worst case. Tabulate the truck positions (axle coordinates) for both static arrangements. Base τ on replicate or repeatability data, or present results as a function of τ (Table S7 already does) without picking one. Report MAE and RMS consistently. Harmonise the Fig. 7 labels and panel titles.

Further points for any revision: Table 3's caption should state that the best single gauge is selected post hoc, which makes it in-sample. Section 6 should not give single-crossing errors of "5–12 %" without noting that the mean predictor achieves 2 %. The recommendation of preliminary overload screening should engage with Richardson et al. (2014), who conclude that even axle-based BWIM is suitable only for pre-selection.

## 5. Missing references a BWIM reviewer would expect

1. Yamaguchi, E., Kawamura, S., Matsuo, K., Matsuki, Y., Naito, Y. Bridge-weigh-in-motion by two-span continuous bridge with skew and heavy-truck flow in Fukuoka area, Japan. *Adv. Struct. Eng.* 12(1) (2009) 115–125. doi:10.1260/136943309787522614. (Continuous-bridge BWIM; directly relevant to C1.)
2. Bao, T., Babanajad, S.K., Taylor, T., Ansari, F. Generalized method and monitoring technique for shear-strain-based bridge weigh-in-motion. *J. Bridge Eng.* 21(1) (2016) 04015029. doi:10.1061/(ASCE)BE.1943-5592.0000782. (Shear channels on determinate and indeterminate bridges, including a box girder.)
3. Sekiya, H., Kubota, K., Miki, C. Simplified portable bridge weigh-in-motion system using accelerometers. *J. Bridge Eng.* 23(1) (2018) 04017124. doi:10.1061/(ASCE)BE.1943-5592.0001174. Also the one-year field verification in *J. Bridge Eng.* (2019), doi:10.1061/(ASCE)BE.1943-5592.0001411. (Deflection-based simplified BWIM; relevant to deflection channels and the baseline/offset issue.)
4. Richardson, J., Jones, S., Brown, A., OBrien, E., Hajializadeh, D. On the use of bridge weigh-in-motion for overweight truck enforcement. *Int. J. Heavy Veh. Syst.* 21(2) (2014) 83–104. (Screening versus enforcement; needed for Section 6.)
5. Žnidarič, A., Baumgärtner, W. Bridge weigh-in-motion systems — an overview. *Proc. 2nd European Conf. on Weigh-in-Motion of Road Vehicles*, Lisbon, 1998. And OBrien, E.J., Žnidarič, A., Ojio, T. Bridge weigh-in-motion — latest developments and applications world wide. *Proc. ICWIM5*, Paris, 2008. (Sensor-placement practice; error sources.)
6. Lansdell, A., Song, W., Dixon, B. Development and testing of a bridge weigh-in-motion method considering nonconstant vehicle speed. *Eng. Struct.* 152 (2017) 709–726. (Speed variation; Problem 3.)
7. Zhao, H., Uddin, N., Shao, X., Zhu, P., Tan, C. Field-calibrated influence lines for improved axle weight identification with a BWIM system. *Struct. Infrastruct. Eng.* 11(6) (2015) 721–743. And Ieng, S.-S. Bridge influence line estimation for bridge weigh-in-motion system. *J. Comput. Civ. Eng.* 29(1) (2015) 06014006. (Measured influence lines as the baseline that should be compared.)
8. Frøseth, G.T., Rønnquist, A., Cantero, D., Øiseth, O. Influence line extraction by deconvolution in the frequency domain. *Comput. Struct.* 189 (2017) 21–30. Also SCHM's own influence-line identification papers (e.g., Zheng, Yang, Yi & Li on influence-line identification from dynamic responses, *SCHM* 2020; the authors should verify and cite the relevant SCHM items).
9. González, A., Rowley, C., OBrien, E.J. A general solution to the identification of moving vehicle forces on a bridge. *Int. J. Numer. Methods Eng.* 75(3) (2008) 335–354. (MFI with regularisation; the moving-force identification context.)
10. Kalin, J., Žnidarič, A., Anžlin, A., Kreslin, M. Measurements of bridge dynamic amplification factor using bridge weigh-in-motion data. *Struct. Infrastruct. Eng.* 18(8) (2022) 1164–1176. (The quasi-static/dynamic term in the error budget is based only on Frýba's constant-force bound.)
11. Akgün, M.A., Garcelon, J.H., Haftka, R.T. Fast exact linear and non-linear structural reanalysis and the Sherman–Morrison–Woodbury formulas. *IJNME* 50(7) (2001) 1587–1606. Kirsch, U. *Reanalysis of Structures*, Springer, 2008. (Prior art for the "Möbius law".)
12. Sanayei, M., Imbaro, G.R., McClain, J.A.S., Brown, L.C. Structural model updating using experimental static measurements. *J. Struct. Eng.* 123(6) (1997) 792–798. Bakht, B., Jaeger, L.G. Bridge testing — a surprise every time. *J. Struct. Eng.* 116(5) (1990) 1370–1383. (Static identifiability; unintended restraint in load tests.)
13. Udwadia, F.E. Methodology for optimum sensor locations for parameter identification in dynamic systems. *J. Eng. Mech.* 120(2) (1994) 368–390. (Fisher-information placement; prior art for the vertex argument and the Cramér–Rao analysis.)

(Bibliographic details for items 8, 10 and 13 are from memory and should be verified by the authors before citation.)
