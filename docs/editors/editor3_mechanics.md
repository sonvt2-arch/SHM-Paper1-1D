# Associate Editor assessment (mechanics lens): SCHM submission

**Manuscript:** "Total-load observability of continuous girder bridges from a single deflection channel: closed-form blind configurations, laboratory verification and sensor placement on an in-service box girder"

**Editor 3: structural mechanics, continuous and haunched box girders, FE modelling**

**Material read:** `manuscript/schm/manuscript.md`, `cover_letter_SCHM.md`, the figures in `manuscript/schm/figures/` (Figs. 3, 7, 8, 9 and S1 are present; Figs. 1, 2, 4, 5, 6 and 10 are not in the folder). I ran `code/analysis/wp3_run.py` and `cm_3span_theory.py` from a scratch copy, plus my own hand and numerical checks.

---

## Decision

**Major revision.** The theory is correct and checks out in every closed form I tested, and the laboratory section is honest. The Cầu Mây section is a different matter. Its headline claim ("two calibrations reproduce the measured deflections, giving 0.18 or 0.48") is not accurate as written, and the non-identifiability argument is stated loosely in mechanical terms. Both points can be fixed with the existing model; no new data are needed.

- **Technical soundness: 7/10.** Theory 9; laboratory 7; in-service analysis 5 as presented.
- **Clarity: 7/10.** The writing is dense but precise. Section 4 overloads "calibration A".

---

## Verified items (independent checks)

1. **Eq. (4)–(5).** I re-derived both from the simply supported uniform-load deflection plus the end-moment term. $F(1/2,1)=1/8$ gives $L^4/192EI$. $\mu$ follows from the standard $M_B$.
2. **Eq. (6)–(7).** The factorisation $(1-\xi)(1+\xi-\xi^2)$ gives $\mu_{crit}$. $1-\rho+\rho^2=5/3$ gives $(3+\sqrt{33})/6=1.45743$. $F'=0$ factors as $(\xi-1)(8\xi^2-\xi-1)$, which gives $\xi^*=0.42154$.
3. **Table 1 and Table A.1 entries.** Reproduced by hand at $\rho_L$ = 0.5, 0.7, 1.6 and 2.0, and at $\xi$ = 0.7.
4. **Two-span statements in the text.** Confirmed: $\rho_L=1.6$ ($-0.78$, $+0.33$, crossing at 2.14); $\rho_L=1.45$ (0.021 and 0.233); band 1.385–1.525; $\partial\mu/\partial\rho_{EI}\propto\rho(1-\rho^2)$.
5. **Eq. (8).** The three-moment equation with $M_B=M_C$ gives $\mu=2(\rho+\beta^3)/(2\rho+3\beta)$. Three equal spans give $\mu=4/5$, and the mid side-span value is 1.3.
6. **Eq. (9).** The blind ratio is $\beta_{crit}=1.700594$, and the trigonometric form is correct (script output: 1.70059398).
7. **Band edges.** The lower edge solves $30\beta^3-69\beta-16=0$, giving 1.621399. The upper edge 1.775 is the root of $10\beta^3-27\beta-8=0$; this cubic is not stated in the paper.
8. **End of the side-span blind locus.** $\mu_{crit}(\xi)$ falls monotonically from 2 to 1, so the locus ends at $\mu=2$, i.e. $\beta^3-3\beta-1=0$, giving $2\cos(\pi/9)$. Correct.
9. **Eq. (10) and the span-wise contributions.** $1.870395+0.195395-1.902566=0.163224$, and the ratio is 0.921.
10. **Main-span results.** $\nu$ (Appendix D) re-derived. Mid main-span blind at $\beta=0.964706$. The prismatic N7 value is 0.754630.
11. **Optimal-position cubic.** $8\xi^3-(12-3\mu)\xi^2+(2-\mu)=0$ confirmed. $\partial\mu/\partial\rho_{EI}\propto 3\beta-2\beta^3$ confirmed.
12. **Indicator definitions.** $R_m=4/7$ is correct. $O_m=2\sqrt{44765}/1279=0.3308$ was checked by numerical quadrature of Eq. (A.2).
13. **Laboratory numbers.**
    - $I=16\,530$ mm⁴, $C_m=61.54$ mm²/N, $f_1=11.94$ Hz (from $m=1.464$ kg/m).
    - Table 4 BPM and SLM values, 1.00489.
    - Table 7.
    - Offset residual $(1.2596-1.9893)$, i.e. 58 %.
    - Regression slope 62.228 (+1.12 %).
14. **Bridge constants and Table 8.** $EI_{mid}=1.977\times10^8$ kN m². $C_m$ recovered from $N_m$: $3.61\times10^{-4}$, $4.05\times10^{-4}$ and $4.36\times10^{-5}$ m²/kN. Table 8 checked in full: $P_\varepsilon$ values, 245.8 kN, and biases of 37/93, 14/35, 4.5/11 and 4.0/10 %. Ratios 8.2, 3.5, 2.6 and 12 % also confirmed.
15. **Table 10.** All five root-sum-square totals reproduce.
16. **Calibrations.** `wp3_run.py` reproduces $k_{FE}=2.748\times10^7$, $\alpha=1.088$ at $k_{FE}$ (misfits −4.6/+5.0 %) and calibration B ($\alpha=0.716$, $k=1.199\times10^8$; misfits −2.8/+2.9 %). The Fig. 7 / S1 values file matches Table 5.

---

## Ranked concerns

### 1. Calibration A as used in Table 5 and Table 8 does not reproduce the measurements (major)

**Location:** Abstract; Section 4.2 ¶2; Table 5 and its caption; Section 4.3 ¶2; Table 8; Conclusions ¶4; cover letter item 4.

**Problem:**
- Calibration A, as used in Tables 5 and 8, is design $EI$ with $k=k_{FE}$. It is fitted to the *report FE* deflections. Against the measurements it misfits N7 by 11 % (Table 6: measured/model A = 0.890).
- The variant that does fit the measurements is $\alpha=1.088$ at $k_{FE}$. For that variant the text itself gives $N_m=0.160$ and 83 % cancellation.
- So the statement "two calibrations reproduce the acceptance-test deflections but give a side-span gauge index of 0.18 or 0.48" is not true for the 0.18 value.
- The 93 % bias in Table 8 also uses this non-fitted variant.

**Fix:** Define calibration A as $(\alpha=1.088, k_{FE})$. Then report $N_m$, $R_m$ and $C_m$ for it in Tables 5 and 8; I expect about 0.160 and $C_m\approx4.0\times10^{-5}$, so the bias rises above 93 %. Alternatively, rephrase every occurrence so that A is "the design model matched to the report FE". Make the abstract, conclusions and cover letter consistent with whichever choice is made.

### 2. The pier-stiffness non-identifiability is described incorrectly in mechanical terms (major)

**Location:** Section 4.2, sentence "Two static readings cannot separate girder rigidity from pier stiffness: a stiffer girder on more flexible piers and a softer girder on stiffer piers deflect alike at the two gauges"; Section 4.4.

**Problem:**
- In a linear model, $(\alpha,k)$ enter as one shape parameter $k/\alpha$ and one scale $1/\alpha$. The gauge ratio N8/N7 depends only on $k/\alpha$.
- I scanned $k$ with the authors' model. The quantity (measured/predicted at N8) ÷ (measured/predicted at N7) is U-shaped in $k/\alpha$:
  - 1.126 at $10^7$
  - 1.097 at A
  - minimum 1.058 at $\approx1.7\times10^8$, which is calibration B
  - 1.09 at the fixed limit
- No $(\alpha,k)$ reproduces both readings. Calibration B is the point of closest approach, which is why a two-parameter fit to two data leaves ±2.9 %.
- The real issue is therefore twofold. First, a residual model error of about 6 % in the gauge ratio. Second, a flat valley in $k/\alpha$ over which N8's $C_m$ varies by a factor of about 2.6.

**Fix:**
- Replace the sentence with this reasoning.
- Add a small figure or table with two curves against $k/\alpha$: the gauge-ratio misfit with a measurement-uncertainty band, and $N_8$, $N_7$ and $R_m$.
- Derive the admissible range of the N8 index from the region where the misfit lies within the uncertainty. Use the uncertainty of the *mean*, not the range of individual readings.
- Report that range as the result, instead of two points.

### 3. Physical plausibility of α = 0.716 is not discussed (major)

**Location:** Section 4.2 and Section 4.4 ¶1.

**Problem:**
- Calibration B implies an effective modulus about 28 % below design ($E_{eff}\approx25.8$ GPa) for a young, uncracked prestressed C45 box girder.
- In acceptance tests, measured/design deflection ratios below 1 (here 0.92–0.94) normally mean the structure is *stiffer* than designed: higher in-situ $E$, barriers, surfacing.
- A prior $\alpha\gtrsim1$ excludes the high-$k$ branch. With that prior the side-span gauge is placed firmly in the poorly conditioned regime ($N_m\approx0.16$–0.18). That is a sharper conclusion than "cannot be identified".

**Fix:** Discuss the plausible ranges of $E_c$ and pier $k$. Estimate $k$ from typical pier geometry, e.g. $4EI_p/h$ or a twin-wall pier, even approximately. Use these ranges to bound the admissible set in concern 2. If B is retained, justify it.

### 4. Bridge-model assumptions that affect the side-span index are not tested (moderate)

**Location:** Section 4.2.

**Problem:** The following are not addressed:
- the rigid zone and diaphragm width over the monolithic piers;
- the pier-top offset, since the rotational spring is applied at the axis;
- axial frame action;
- shear lag in a 5.4 m deep haunched box;
- the $I\propto h^n$ law with $n=2.943$, fitted to only two sections.

Each of these moves the side-span negative lobe in the same way that $k$ does. They also partly explain the irreducible 6 % ratio misfit identified in concern 2.

**Fix:**
- Run a sensitivity check of $N_8$ to a pier rigid zone of ±(diaphragm width)/2 and to $n$ (for example 2.5–3.2).
- State that these assumptions are absorbed by $k$.
- Tables 5 and 6 order the bound columns inconsistently. Table 5's N7 row is listed min…max (0.145…0.263), but under the header "pinned … fixed" it should read 0.263 … 0.145, as Table 6 does.
- Calibration B's N8 value of 0.476 lies outside the "bound" 0.023–0.446. The reason is that the bound uses design $EI$; say so in the caption.

### 5. Laboratory configuration and invariance evidence (moderate)

**Location:** Section 3.1 (three-load spacing chosen "because it fits the record"); Section 3.3 (ratio rising 1.010 → 1.017).

**Problem:**
- Inferring the test configuration post hoc from the response is a data-provenance problem. The cover-letter and README note that the early package states the reverse order.
- The load-dependent excess means linearity, the premise of both estimators, is not demonstrated.

**Fix:** Cite the laboratory log for the spacing, or state the uncertainty explicitly and show the results under both orders. Strongly consider running the fixed-load/varied-spacing test and the falsifiable 2500 + 3644 mm blind test proposed in Section 7.2. Both need no new apparatus, and either would turn the laboratory section from indirect into direct support.

### 6. Minor items

1. **Section 2.1, truncation remark.** It says the trailing-axle tail "lies where $\eta_m$ is negative". That holds only when the sensor is not in the exit span. Qualify it.
2. **Section 2.4, Simpson accuracy.** It is "nearly exact" only when the sensor and supports fall on *panel* edges. In the laboratory the sensor (1250 mm) and the support (2500 mm) are odd multiples of Δx, which explains the +0.027 %. Say so.
3. **Upper band edge.** Give the cubic $10\beta^3-27\beta-8=0$ for 1.775, to parallel the lower edge.
4. **Fig. 6 regression.** Specify the $R^2$ definition. The uncentred value is 0.999997, not 0.99998.
5. **Fig. 3a marker.** It marks Cầu Mây at ξ = 0.5, but the installed gauge is at 0.4. Add a second marker.
6. **Missing figure files.** Figs. 1, 2, 4, 5, 6 and 10 are absent from `figures/`; they are needed for submission.
7. **Unresolved placeholders.** Several [NEED VALUE] items remain: weight accuracy class, data DOI, COI and funding details, and the overlap with two submissions under review at *Structures* (cover letter). The overlap point must be resolved before review.
8. **Section 4.3 wording.** "Cancellation of only 0.30" for N7 means $|A^-|/A^+$. Use $R_m=0.70$ to stay with the defined index.
9. **Section 6.2 and Table 10, offset scenarios.** The authors' own records (Section 5) did not demonstrate the assumed residual offsets of 0.02–0.05 mm. The abstract's 35–93 % figures should be flagged as conditional on that offset.

---

## Note to authors (about 150 words)

The closed-form part of this paper is correct and useful. Every expression I re-derived holds: Eqs. (4)–(10), $\beta_{crit}=1.700594$, the $2\cos(\pi/9)$ terminus and the main-span results. The laboratory numbers and Table 8 also reproduce.

The revision should concentrate on Section 4. First, the 0.18 index comes from a model matched to the designer's FE, not to the measurements. The measurement-fitted variant ($\alpha=1.088$) gives about 0.16, so the abstract, conclusions and Table 8 must be made consistent with that. Second, since girder rigidity and pier stiffness enter only through $k/\alpha$ and a scale, no parameter pair reproduces both readings. Calibration B is the closest approach, with a residual of about 6 % in the gauge ratio. Please replace the two-point presentation with the admissible range of the side-span index over $k/\alpha$, and discuss whether $\alpha=0.716$ is physically plausible. Third, test the rigid-zone and depth-law assumptions, and document the three-load spacing. With these changes the conclusions will follow from the evidence.
