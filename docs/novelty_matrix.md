# Novelty matrix and journal fit (WP1)

Scout: Literature Scout, 2026-10-11. Scope: prior art that could pre-empt the invariance theorem (integral of y(x_s,t) over a crossing = P_tot·C_m), the closed-form two-span result, blind span ratios, the |C_m| observability indicator, the optimal sensor position and the error budget.

## 0. Method and limits (read first)

- Bibliographic data and DOIs below were taken from Crossref records I retrieved (`api.crossref.org`) or from publisher/repository pages returned by search. "Seen" in the "Evidence" column says what I actually read: **abstract** (full abstract), **excerpt** (search-engine passage of the full text), **title only** (Crossref metadata, nothing else). Nothing marked "title only" may be cited for its content before someone reads it.
- Paywalled full texts (Elsevier, ASCE, Springer) were not accessible. Moses (1979) was not read in full; what is said about it comes from the FHWA literature review (FHWA-HRT-16-024, chapter 4) and from papers that describe it.
- **The "Integral Mean of Strain" (IMS) paper in Measurement (2025) could not be located.** Searches: Crossref (bibliographic query, ISSN 0263-2241, 2022 onward, several phrasings), Exa web search, general web search, the exact phrase in quotes. No record contains "Integral Mean of Strain". The authors or the internal reviewer who raised it must supply the title/DOI. Until then the paper must not be cited, and it must be treated as an unresolved threat (see section 3, point 6). The nearest hit is Dan et al. 2026 (row 12), which is in Measurement and integrates strain over time, but it is about a railway bridge and is dated 2026, so it is probably not the paper meant.
- Firecrawl credits and Elicit API access were unavailable; OpenAlex rate-limited. The coverage is therefore Crossref + Exa + web search, not a systematic review.

## 1. Matrix

Legend: SS = simply supported; CB = continuous beam/bridge; "Axle info" = needs axle number/spacing (and usually speed) as input; "Neg. IL" = addresses influence lines that change sign (continuous bridges); "Blind" = identifies configurations (sensor position, span ratio) where the integral response is identically zero for any load; "Observ." = a quantitative criterion for choosing a sensor so the total load is observable.

| # | Citation | DOI | Quantity used | Structure | Sensors | Axle info? | CB / neg. IL? | Blind configs? | Observ. criterion? | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Moses F (1979) Weigh-in-motion system using instrumented bridges. Transp Eng J ASCE 105(3):233–249 | 10.1061/TPEJAN.0000783 | Bending strain, least-squares fit of axle loads times IL ordinates; GVW = sum of axle weights | Instrumented bridges (field), SS and later continuous | Multi (strain + axle detectors) | Yes (spacing, speed) | Moses & Ghosn extended to continuous spans (per Cardini & DeWolf 2009, secondary); no sign-change/blind analysis known to me | No | No | Not read in full; FHWA-HRT-16-024 ch.4 (excerpt) |
| 2 | Ojio T, Yamada K (2002) Bridge weigh-in-motion systems using stringers of plate girder bridges. Proc 3rd Int Conf on WIM, Orlando | none seen | Area under strain-time curve times speed = "influence area"; GVW by ratio to a calibration truck | Steel plate-girder SS | Single | No axle info (speed needed) | SS only | No | No | **Secondary only**: described in Cardini & DeWolf 2009 (row 3). Title/venue as quoted there are not verified. The original was not found. |
| 3 | Cardini AJ, DeWolf JT (2009) Implementation of a long-term bridge weigh-in-motion system for a steel girder bridge in the interstate highway system. J Bridge Eng 14(6):418–423 | 10.1061/(ASCE)1084-0702(2009)14:6(418) | Integral of strain curve, "influence area", calibrated against a known truck, speed from two gauge lines | 22.9 m SS steel girder | Single per girder (+ speed gauges) | No axle number/spacing; speed yes | SS only (notes continuous spans were used by Moses & Ghosn) | No | No | Excerpt (full-text PDF at hnutest.hnu.edu.cn, mirror) + Crossref |
| 4 | Agüero-Barrantes P, Christenson RE, Lobo-Aguilar S (2023) Utilizing Kriging metamodeling to provide practical and effective bridge weigh-in-motion. J Bridge Eng 28(2):04022138 | 10.1061/jbenf2.beeng-5760 | Area under strain curve and its centroid, fed to a Kriging model for GVW; "extends the BWIM concept of influence area" | In-service highway bridge, Costa Rica | Single | No | Not addressed | No | No | Abstract |
| 5 | Zolghadri N, Halling MW, Johnson NR, Barr PJ (2016) Field verification of simplified bridge weigh-in-motion techniques. J Bridge Eng 21(6):04016063 | 10.1061/(asce)be.1943-5592.0000930 | Strain, GVW without axle detectors, influence surfaces from calibrated FE | Single-span interstate bridge | Few | No axle detectors | Single span | No | No | Abstract (Exa library) |
| 6 | Yang J, Hou P, Yang C (2021) Study on the method of moving load identification based on strain influence line. Appl Sci 11(2):853 | 10.3390/app11020853 | "Strain integral coefficient α" tied to the envelope area of the mid-span strain influence line; α calibrated with a known vehicle, then load = area/α | Lab model, SS T-beam | Single (per beam) | Speed (from inversion); no axle spacing | SS | No | No | Abstract + excerpt |
| 7 | Yang J, Hou P, Yang C (2023) Investigation on the moving load identification for bridges based on long-gauge strain sensing and skew-Laplace fitting. Smart Mater Struct 32(8):085026 | 10.1088/1361-665x/ace4ac | Envelope area of long-gauge strain IL "directly proportional to vehicle weight"; GVW error <3% sim, <10% experiment | Bridge model | Long-gauge (distributed) | Speed and wheelbase from IL extrema | Not addressed | No | No | Abstract |
| 8 | Zhu J, Wang C, Qi T, Zhou Y (2022) Vehicle load identification on orthotropic steel box beam bridge based on the strain response area. Appl Sci 12(23):12394 | 10.3390/app122312394 | Strain response area matrix, calibrated | Orthotropic steel box girder | Multi (U-ribs) | Speed via cross-correlation | Not addressed | No | No | Abstract |
| 9 | Shi S, Yarnold M, Hurlebaus S (2024) Evaluation of a load cell-based bridge weigh-in-motion system. Transp Res Rec 2679:535–549 | 10.1177/03611981241263336 | Reaction force (load cell); "area method" = integral of response equals GVW times influence area, calibrated | Slab-beam bridge, field | Load cells at supports | Not for area method | SS | No | No | Abstract + excerpt |
| 10 | Chaudhary MTA, Morgese M, Taylor TW, Ansari F (2025) Method and application for influence-line-free distributed detection of gross vehicle weights in bridges. Structures 73:108298 | 10.1016/j.istruc.2025.108298 | Distributed fibre-optic flexural strain along the bridge, spline regression + structural mechanics; no ILD | **Five-span continuous bridge**, static trucks | Distributed (many) | Not required for GVW | **Yes, continuous** | No | No | Abstract. **Closest published work on continuous spans and GVW.** Not read beyond abstract. |
| 11 | Zhou C, Demartino C, Narazaki Y, Xu Y, Chatzi E, Spencer BF (2025) Optimal sensor placement for bridge weigh-in-motion using an augmented Kalman filter. Mech Syst Signal Process 241:113522 | 10.1016/j.ymssp.2025.113522 | Acceleration, augmented Kalman filter, optimisation of sensor layout (from the related conference chapter, NSGA-II) | FE bridge | Multi | FE model of vehicle | Not known | No | Optimisation-based, not a closed-form index | **Title and Exa metadata only; abstract not read.** Must be read: it is the only BWIM sensor-placement paper found. |
| 12 | Dan D, Wang W, Luo M, Zhao (2026) Online traffic load identification of high-speed railway bridge using time integration of strain monitoring data. Measurement 269:120781 | 10.1016/j.measurement.2026.120781 | Time integration of strain (title) | Railway bridge | Unknown | Unknown | Unknown | Unknown | Unknown | **Title only (Crossref).** Closest "integral of strain" hit in Measurement. Read before submitting. Author list incomplete (Crossref shows 4, last name only for the last). |
| 13 | Döring A, Vogelbacher M, Schneider O (2023) Investigations of ratio-based integrated influence lines as features for bridge-damage detection. Infrastructures 8(4):72 | 10.3390/infrastructures8040072 | **Integral of the displacement and curvature influence line** at a sensor, ratio of two sensors cancels load F; analytical Euler–Bernoulli solutions | Prestressed concrete bridge, stepped/beam models incl. one with an intermediate support | 1 or 2 | Not needed (ratio) | Yes (support-bearing beam) | The excerpt says the integral of the curvature IL is zero at specific reference points (x_ref = 3L/8, 5L/8) and that the displacement-IL integral relative difference diverges at x_ref = L/2; authors treat these as sensor-positioning remarks for damage features | Not as a load criterion | Excerpt only (MDPI page itself blocked). **Prior art for "the integral of a deflection IL is a closed-form beam quantity independent of the load", and for zero-integral sensor points, but in damage detection, not load observability.** Must be read in full and cited. |
| 14 | Huang D, Lu Y (2025) Influence line theory supported single sensor-based strain feature for bridge defect diagnosis. Struct Health Monit (online) | 10.1177/14759217251376931 | Ratio features of IL (R-value = area ratios; M-value = max/min) | Two-span continuous bridge case | Single | No | Yes | No | No | Excerpt. Cite for "integral-based IL features exist (R-value)". |
| 15 | Zhang J, Liu Y, Fan X (2026) An AR(1)-Tikhonov-SVD-GCV framework for stochastic moving load identification driven by bridge multi-point deflection data. Structures 88:111844 | 10.1016/j.istruc.2026.111844 | Multi-point deflection | Bridge | Multi | Not known | Not known | Not known | Not known | **Title only.** Directly on deflection-based load identification in *Structures*; read before submission. (Also in Adv Bridge Eng 7:9, 10.1186/s43251-025-00196-y, title only.) |
| 16 | Shen Z, Peng W, Zhang X, et al (2026) A lightweight weigh-in-motion system based on vehicle-induced bridge deflection and impact dynamic responses. Int J Struct Stab Dyn (online) | 10.1142/s0219455427503664 | Mid-span visual deflection + deflection influence lines, calibrated; MAE 6.64% on 580 passages | Short/medium-span bridge, field | Single deflection + accelerometer | Yes (wheelbase via accelerometer axle detection) | Not stated | No | No | Abstract. Shows deflection WIM in the field exists; uses IL fit, not the integral. |
| 17 | Deng L, Liu P, Huang T, Kaewunruen S (2025) A novel moving load identification method for continuous rigid-frame bridges using a field-based displacement influence line. Appl Sci 15(11):6028 | 10.3390/app15116028 | Displacement IL | Continuous rigid-frame bridge | Unknown | Unknown | Yes (title) | Unknown | Unknown | **Title only.** Read before submission. |
| 18 | Yokoyama T (2023) Bridge damage detection by means of displacement based bridge weigh-in-motion. Mater Res Proc 27:243–250 | 10.21741/9781644902455-31 | Deflection IL, virtual axle for damage | Lab + simulation | Single | Yes | Not stated | No | Position of virtual axle matters, no criterion | Abstract |
| 19 | He W, Ling T, OBrien EJ, et al (2019) Virtual axle method for bridge weigh-in-motion systems requiring no axle detector. J Bridge Eng 24(9):04019086 | 10.1061/(asce)be.1943-5592.0001474 | Strain; virtual axles to avoid axle detectors | Bridge | Multi | Axle detector not required | Not known | No | No | Title only (my check printed the first three authors; full list not verified) |
| 20 | Cantero D, Karoumi R, González A (2015) The virtual axle concept for detection of localised damage using bridge weigh-in-motion data. Eng Struct 89:26–36 | 10.1016/j.engstruct.2015.02.001 | Virtual axle for damage detection | Bridge | Multi | Yes | Not known | No | No | Title only. Note the two "virtual axle" meanings (rows 19, 20). |
| 21 | Andersen P, Mukhopadhyay SK (1950) Determination of load distribution on a beam from measurements on its deflected form. Univ Minnesota Bulletin 53(1), Minneapolis | none; hdl.handle.net/11299/124278 | Deflections and strains, polynomial/least-squares fit of load intensity | Aluminium beam, lab | Multi (deflected form) | n/a (static) | Not known | No | No | Abstract/introduction seen (UMN Digital Conservancy). Static load-distribution inversion, not a moving-vehicle integral. |
| 22 | Nguyen QB, Hoang T, Nguyen HS (2024) [Determination of the load applied on a simply supported beam based on measured deflection data]. J Sci Technol Civ Eng (HUCE) 18(2V):61–71 | 10.31814/stce.huce2024-18(2V)-05 | Integral of mid-span deflection, total load | SS beam | Single | No | SS only | No | No | Crossref record (title is Vietnamese). **Authors' own earlier work.** Contents as described in the manuscript. |

### What the matrix shows, candidly

1. **The statement "response integral over a passage = GVW x influence area" is published and old** (rows 2, 3, 4, 6, 7, 8, 9; Ojio & Yamada 2002 as reported by Cardini & DeWolf 2009; Moses-type convolution implies it). For strain it is routine, "influence area" is the established term, and calibration against a known truck is the standard way to get the constant.
2. **For deflection, an area-of-influence-line integral is also published as a damage feature** (row 13). The paper cannot claim that the integral of a deflection influence line is a new object.
3. Maxwell–Betti as the reason that C_m equals the deflection under a uniform unit load: I found no source that states it for BWIM. That is not evidence of absence (Moses and later work are not fully read). Treat it as "not found" and phrase accordingly.
4. No source found treats **blind span ratios, the closed form for a two-span beam with arbitrary span ratio, or an a-priori |C_m| indicator**. Rows 10, 13, 14 are the nearest (continuous spans; zero-integral sensor points; two-span case). All three must be read in full.
5. **Sensor placement for BWIM exists** (row 11) but as acceleration/Kalman-filter optimisation, not as a closed-form observability indicator for static integral weighing.
6. Unresolved: the IMS 2025 paper. If it states the same equation for a continuous or two-span beam, contributions 1 and 2 below shrink.

## 2. Related notes that affect wording

- "Observability" is used here in a narrow sense (nonzero C_m so the total load maps to a nonzero integral). It is not the control-theory observability of a state-space model; say "total-load observability" at first use. This follows the internal reviewer (A2-3 in `docs/rejection_evidence.md`).
- Maxwell–Betti is a derivation tool for the constant, not a novelty claim.

## 3. What remains new (defensible)

Subject to reading rows 10–15 and locating IMS 2025.

1. **Invariance with respect to axle configuration and speed, proved for any linear-elastic beam and any response (deflection, and extendable to strain, rotation, reaction), with C_m identified as the deflection under uniform unit load.** Defensible as a clean, unified statement with an exact characterisation of the constant. Not defensible as "first to relate response area to gross weight" (rows 2–9). Weakest of the claims in terms of novelty; keep it as the foundation, not the headline.
2. **Closed-form C_m for a two-span beam with arbitrary span and stiffness ratio, and its sign change.** Rows 10, 13, 14 involve continuous spans but none gives this closed form in what I have read.
3. **Blind configurations: the locus in (sensor position, span ratio) where C_m = 0**, so that a sensor sees zero integrated response for any vehicle. I found nothing equivalent in BWIM; the zero-integral sensor points in row 13 are the nearest, and they concern damage features, not weighing.
4. **A pre-installation observability indicator |C_m| and the exact optimal sensor position (maximum |C_m|)** as a closed-form rule. Row 11 does sensor optimisation for dynamic AKF-based BWIM; the closed-form static-integral indicator is distinct. Novel in the contribution to design, if no source in rows 10, 11, 15 contradicts it.
5. **An error budget specific to the integral estimator, with zero-offset drift dominant over random noise** (error scales with drift x crossing length / (P C_m)). Defensible as an analysis; measurement-science fit is strongest for *Measurement*.
6. Not claimable: "the first method that needs no axle configuration" (rows 2–9 already need none), "the first deflection-integral weighing" (row 22 is the authors' own earlier paper, plus row 13 for the integral).

## 3a. Exact sentences to use when citing prior art

Replace bracketed numbers with the new reference numbers.

**Moses.** "Bridge weigh-in-motion was introduced by Moses [Moses 1979], who fitted measured bending strain to the sum of axle loads times influence-line ordinates; the method requires axle spacings and speed."

**Influence area (strain).** "A simpler family estimates only the gross weight from the area under the measured response. Ojio and Yamada, as described by Cardini and DeWolf [Cardini 2009], multiply the area under the strain-time record by the speed to obtain an 'influence area' and calibrate it against a truck of known weight; related strain-area and strain-integral formulations have since been proposed [Yang 2021; Yang 2023; Zhu 2022; Agüero-Barrantes 2023], and the same idea has been applied to support reactions [Shi 2024]."

**Integral of influence line, deflection (Döring).** "The integral of the displacement influence line has also been used as a damage feature, where the ratio of two sensors removes the load [Döring 2023]. Here the integral serves a different purpose: it identifies the load itself, and its sign and magnitude decide whether a given sensor can observe it."

**Continuous spans.** "Distributed fibre-optic strain on a five-span continuous bridge has been used to obtain gross weight without influence lines [Chaudhary 2025]. That work uses many sensors along the bridge. The present paper asks when a single sensor can observe the total load at all."

**IMS (draft only, do not use until the paper is located).** "The Integral Mean of Strain [IMS reference] estimates gross vehicle weight from the integral of strain at one section. Our result is the deflection counterpart for statically indeterminate beams, with the additional finding that the integration constant changes sign and vanishes at specific sensor positions and span ratios, which the strain-integral formulation does not address." The last clause is only valid if the IMS paper is silent on this; check first.

**Own prior paper.** "The earlier study [Nguyen 2024] demonstrated the integral of mid-span deflection on a simply supported beam, where the influence line has one sign and no configuration is blind."

**Sensor placement.** "Sensor placement for bridge weigh-in-motion has been treated as a numerical optimisation using an augmented Kalman filter [Zhou 2025]; we give instead a closed-form static indicator."  (Check Zhou 2025 first; this sentence is based on title and related-chapter abstract only.)

## 4. Journal fit

### Evidence gathered

Official Structures aims text (via search result of the Elsevier journal page; page itself returned 403, so quotes come from the search snippet): "Structures aims to publish internationally-leading research across the full breadth of structural engineering"; wants papers with "tangible industrial-related pathways to impact". Will not consider: "Papers where an analytical method is developed but not validated, or where no new insight is offered ... (NB Validation need not necessarily be by means of a laboratory experiment.)"; also salami-sliced papers, and papers applying a numerical method to a slightly different problem. Guide for authors (snippet): "Original research papers (preferably no more than 20 double line spaced manuscript pages including tables and illustrations), reviews, short communications (no more than 10 double line spaced manuscript pages including tables and figures)". Required items per a template page (secondary): Highlights, graphical abstract, CRediT, data availability.

Measurement (journal of IMEKO): aims text (snippet): "novel achievements in all fields of measurement and instrumentation science and technology". Article types and requirements below come from **a third-party guide (manusights.com, 2026-06), not from Elsevier**: research articles with no fixed word limit, technical notes, commissioned reviews; highlights (3–5), data availability, competing interests, CRediT; double-anonymised review; common desk returns: sensor/system application without measurement-science advance, known method on a new target, hand-waved uncertainty, missing critical review. Verify against the official guide before submitting.

### Recent (2023–2026) papers on BWIM / load identification / influence lines

*Structures* (ISSN 2352-0124), all found by Crossref query:
- Heinen S, Lopez R, Miguel L (2024) shear-force-based BWIM for SS structures, 70:107607 (10.1016/j.istruc.2024.107607)
- Agüero-Barrantes P, Lobo-Aguilar S, Hain A, Christenson R (2024) Kriging to alleviate speed reading dependence in BWIM, 68:107086 (10.1016/j.istruc.2024.107086)
- Chaudhary et al. (2025) IL-free distributed GVW, 73:108298 (row 10)
- Chen S, Chen J, Zhao M, et al (2025) BWIM methods under the environmental temperature field, 76:108981 (10.1016/j.istruc.2025.108981; title only)
- Cui S, Li Y, Wang M, et al (2025) IL identification, 80:109793 (10.1016/j.istruc.2025.109793)
- Moghadam A (2025) speed-adaptive NOR-BWIM, 82:110714 (10.1016/j.istruc.2025.110714)
- Wang L, Wu H, Luo C (2025) moving force identification, 73:108322 (10.1016/j.istruc.2025.108322)
- Zhang J, Liu Y, Fan X (2026) multi-point deflection load identification, 88:111844 (row 15)
- Yan B, Liao J, He G (2026) iterative IL identification, 90:112238 (10.1016/j.istruc.2026.112238); Zhou S, Zhu J, Shi T (2026) IL inversion, 89:112030 (10.1016/j.istruc.2026.112030)

*Measurement* (ISSN 0263-2241):
- He W, Liu J, Song S, Liu P (2024) non-contact vehicle weighing with BWIM and computer vision, 225:113994 (10.1016/j.measurement.2023.113994)
- Zhang J, OBrien EJ, Kong X, et al (2024) factors affecting accuracy of vision-based vehicle weight measurement, 224:113840 (10.1016/j.measurement.2023.113840)
- Gao K, Zhang H, Wu G (2024) multispectral vision-based non-contact WIM, 226:114162 (10.1016/j.measurement.2024.114162)
- Yang X, Wang X, Podolsky J, et al (2024) wander effect in hybrid WIM, 234:114870 (10.1016/j.measurement.2024.114870)
- Zhang C, Zhu J, Shi T (2023) IL estimation with Elastic Net, 202:111883 (10.1016/j.measurement.2022.111883; vol 202 is 2022 issue, online 2022)
- Zhu J, Zhang C, Li X (2023) damage detection with quasi-static displacement IL from one sensor, 211:112599 (10.1016/j.measurement.2023.112599)
- You R, Yi T, Ren L (2023) bridge deflection from strain only (EEM), 221:113492 (10.1016/j.measurement.2023.113492)
- Mustafa S (2026) IL identification, Bayesian, 273:121221; Zhao L, Chen Z, Yan W (2026) 258:119083 (10.1016/j.measurement.2025.119083)
- Gao K, Gu J, Chen Z (2026) non-contact WIM review, 290:122919 (10.1016/j.measurement.2026.122919)
- Dan D, Wang W, Luo M (2026) time integration of strain, 269:120781 (row 12)

All entries above are Crossref metadata only unless marked otherwise.

### Recommendation

**Structures (Elsevier) first.** Reasons:
1. It has an active BWIM and influence-line stream (10 papers in 2024–2026 above), including one on a continuous bridge (Chaudhary 2025) and one on deflection-driven load identification (Zhang 2026). A reader there knows the area method.
2. Its stated exclusion is an analytical method that is "developed but not validated", and it explicitly says validation need not be a laboratory test. The paper has FE verification, a laboratory beam and planned case studies on existing bridge data, which meets that rule. A theory + FE + lab + case-study paper on design of sensor layout is within its "new techniques ... new insight" wording.
3. It is not a metrology venue, so the missing field campaign weighs less than at *Measurement*, where the guide (third-party) asks for traceable uncertainty and a measurement-science advance. The error budget helps, but the core contribution is structural mechanics.
4. Length: guide says original research is preferably at most 20 double-spaced pages including tables and figures, which is roughly 7,000–9,000 words with a normal figure load. Fits the plan to cut from about 16,700 words to 8–9k. Short communication (10 pages) is too small for this paper.
5. Risk: Structures says pipelines/roads/railways are out of scope. Bridges are in scope, but frame the paper as structural (bridge girders), not traffic enforcement.

**Measurement as second choice,** only if the paper is rewritten around the error budget, drift handling and the |C_m| indicator as a measurement-design tool. Risks: IMS 2025 appeared there (if the reviewers know it, expect a direct comparison request); double-anonymised review (blind the manuscript); the third-party guide lists "known method on a new target" as a desk return.

Article-type requirements to prepare for either: Highlights (3–5 bullets), graphical abstract (recommended), CRediT statement, data-availability statement, competing-interest and generative-AI declarations (the repo already has them in the ES version), ORCID. Elsevier reference style is numeric or author-year per journal; check the guide for authors.

## 5. Actions before submission

1. Obtain the IMS 2025 reference from whoever raised it; read it.
2. Read in full: Moses 1979 (and Moses & Ghosn), Chaudhary 2025, Döring 2023, Zhou 2025, Zhang 2026, Deng 2025, Dan 2026.
3. Find Ojio & Yamada 2002 original or cite only through Cardini & DeWolf 2009.
4. Confirm Structures page limit and Measurement requirements on the official guide pages (403 from this environment).
