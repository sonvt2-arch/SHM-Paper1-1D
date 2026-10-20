# Hostile audit v2, role 6: Abstract / Introduction contributions / Conclusions / Declarations / Cover letter vs Results

Scope: every claim in the Abstract, the contribution paragraph of Section 1 (items i–iii and the sentences that follow), Section 7, Data availability and the other declarations, the cover letter (`manuscript/ase/cover_letter_ASE.md`) and the Graphical Abstract. Each claim was traced to Sections 2–6, Supplementary S1–S11 and the logs in `word/scripts.zip`. The built PDF (`word/Manuscript_ASE.pdf`, extracted with pdftotext) has the same text as `manuscript.md` in all the places checked.

Checked and found consistent (not findings): 0.19–0.32 band (S2: 0.676<ξ<0.812, i.e. 0.188–0.324); λ = (3+√33)/6 = 1.4574 and β = 1.7006; GLS against average 20.4 against 11.9, paired +8.5 pp (`v4_estimator_paired.csv`: 8.474, CI 2.35–15.06); 6.6/1.5 and 2.4/1.1 (Table S13; `ident_static.log` C8 3.00e-5–1.98e-4, C7 3.28e-4–4.95e-4); CRB 0.87 → 0.18 (`ident_fisher.log`, κ = 2.748e7: 0.865 → 0.177); B_m 0.51/0.12 (S_C8 = 0.511, S_C7 = −0.115); offset bias 16–25 % and 41–271 % (`v3_numbers.log`); 22–26 % for the four day-1 gauges (ratios 0.740–0.783); 3644 mm = 2500 × 1.4574; NOR-BWIM DOI, version 1 and CC0 licence (confirmed through the figshare API); "5 tables" in the cover letter (4 numbered tables plus the symbol table, as the submission checklist counts them).

---

## Blocking

### B1. Abstract, last sentence: "side-span constants need identified pier stiffness or a pier tiltmeter" goes beyond the body
- Location: Abstract, final sentence. The same idea, slightly weaker, appears in cover letter item 3 ("a pier tiltmeter is the most informative additional measurement").
- Quote: "On this girder, deflection gauges belong at mid main span, and side-span constants need identified pier stiffness or a pier tiltmeter."
- Why wrong: the body limits this to model-based constants. Section 5.3 says "should not take its constant from a design model unless that stiffness is identified" and "If a model-based constant is wanted, a tiltmeter on the monolithic pier T7 is the most informative of the measurements compared". Section 6 and S10 step 6 recommend SLM with weighed vehicles. SLM gives the constant directly and does not need κ. The abstract drops the "model-based (BPM)" condition, so it contradicts the paper's own recommended route. "Identified pier stiffness or a pier tiltmeter" is also redundant, because the tiltmeter is one way to identify κ.
- Fix: "...and a model-based side-span constant needs the pier stiffness identified, for example by a pier tiltmeter; otherwise the constant must come from weighed vehicles."

### B2. Introduction contribution (ii): the "one day" scope is dropped, and Table S8 contradicts the general statement
- Location: Section 1, last paragraph, item (ii).
- Quote: "On public records, GLS weights from vehicle-free noise did worse than the gauge average (Section 4.3)."
- Why wrong: the difference is resolved only on day 2 with 4 gauges (Table 2: 20.4 against 11.9; paired +8.5, CI +2.3 to +15.1). On day 1 the estimators "cannot be told apart" (Section 4.3). On the day-1 wheel-path set GLS is numerically better than the average (Table S8: 4.9 against 5.4). The Abstract ("on one day of public records"), Conclusion 4 ("On one day") and the cover letter ("On one day") all keep the scope. Item (ii) is the only place that states the finding for the public records in general.
- Fix: "On one day of public records (four gauges), GLS weights from vehicle-free noise did worse out of sample than the gauge average; on the other day the estimators could not be told apart (Section 4.3)."

## Should-fix

### S1. Abstract, Conclusion 3, Intro (iii), cover letter item 3: the headline factor 6.6 holds only for the base model and τ = 5.3 %, and neither condition is stated
- Location: Abstract sentence 4; Conclusion 3; Intro item (iii); cover letter item 3. In the body, Section 5.2 paragraph 1 and the Table 3 "admissible set" row also omit "base model".
- Quote (Abstract): "two static readings leave the side-span deflection constant uncertain by a factor of 6.6 against 1.5 at mid main span".
- Why wrong: Table S13 is explicitly the "base model, L_v = 44 m". `ident_static.log` (admissible sets at τ = 5.27 %) gives quite different C8 max/min ratios for the model-form variants the paper itself uses: L_v = 40 m 12.9, L_v = 45 m 5.8, n = 2.5 2.6, n = 3.2 16.1, rigid pier zone 11.6. The corresponding C7 ratios are 1.3–1.6. The ratio also depends on τ: 1.5 against 1.1 at τ = 3 % and 3.4 against 1.4 at τ = 4 % (Table S13). The qualitative contrast (N8 ≥ 2.6, N7 ≤ 1.6) survives every variant, but the number 6.6 does not, and the summary places present it as a property of the girder.
- Fix: in Section 5.2, add "in the base model; across the model-form variants the N8 factor is 2.6–16 against 1.3–1.6 for N7" (and a line in S8 or Table S13). In the Abstract and Conclusion 3, write "by a factor of 6.6 against 1.5 in the base model at a 5.3 % misfit tolerance (2.6–16 against 1.3–1.6 across model-form variants)", or state only the robust contrast.

### S2. Abstract: "deflection gauges belong at mid main span" conflicts with the placement result of Section 5.3 and leaves out that the single gauge is marginal
- Location: Abstract, last sentence. Conclusion 5 is consistent; the Conclusions contain no placement recommendation for this girder.
- Quote: "On this girder, deflection gauges belong at mid main span".
- Why wrong: (a) Section 5.3 puts the second deflection sensor in the side span, 4–10 m from the inner pier (the pair at 100 m and 152 m from T5). So not all deflection gauges belong at mid main span. Only the single robust channel does ("the deflection channel at mid main span is the robust choice"). (b) The N7 indicator is itself at or below the 0.2 near-blind threshold in part of the admissible set (Table 3: 0.190–0.286; fixed piers 0.145). Section 6 calls single-point weighing on this unit "marginal even at the best location" (16–25 % bias at δ0 = 0.1 mm). (c) The recommendation appears in the Abstract but in none of Conclusions 1–5. That is an Abstract/Conclusion inconsistency.
- Fix: "On this girder, a single deflection gauge belongs at mid main span, although a 0.1 mm residual offset still biases a 25 t truck by 16–25 %..." Add the same recommendation to Conclusion 3 or 5.

### S3. Abstract, Conclusion 2, cover letter item 2: the placement rule is set next to the field result as if the field result tested it, and "the rule itself is not tested in the field" is dropped
- Location: Abstract sentence 3; cover letter item 2; Conclusion 2 (which omits the caveat).
- Quote (Abstract): "For position-independent noise, optimal sensors lie at the extremes of the uniform-load response; on one day of public records, weighting by vehicle-free noise raised the error 8.5 percentage points above the gauge average."
- Why wrong: the field comparison is about estimating Σ for GLS at fixed gauge positions. All NOR-BWIM gauges sit within about 6 m of each other at one station, so placement was not tested. Intro (ii) says "the rule itself is not tested in the field", and Section 6 says "a deflection pair could not be tested". Joining the two clauses with a semicolon reads as field evidence about the rule. The placement rule is verified only by brute-force search and Monte Carlo (S4).
- Fix: split the sentence and add "(verified by brute-force search and Monte Carlo, not in the field)". Present the field result as a check of the noise model.

### S4. Abstract: the field error statement leaves out the estimator, the metric and the mean-weight baseline
- Location: Abstract sentence 3.
- Quote: "weighting by vehicle-free noise raised the error 8.5 percentage points above the gauge average."
- Why wrong: it does not say that "the error" is the out-of-sample (leave-one-run-out) MAE of a GLS estimator on four gauges. It also omits the body's key qualifier: a predictor that always returns the mean calibration weight (2.0 % MAE) beats every estimator, "so the records cannot show weight discrimination" (Section 4.3). Without this, a reader could take 11.9 % as a weighing accuracy. The cover letter states the limitation; the Abstract does not.
- Fix: "...GLS weights from vehicle-free noise raised the out-of-sample mean absolute error of four gauges from 11.9 % to 20.4 %; the records check the noise model, not weight discrimination."

### S5. Conclusion 4: "10–27 %" is attributed to the gauge average, but the gauge-average margins are 11.8 % and 26.7 %
- Location: Section 7, item 4 (and Section 4.2, first sentence, which uses 10–27 % for the records in general).
- Quote: "the gauge-average constants were consistent with invariance and superposition within the 10–27 % that the noise resolves".
- Why wrong: Table S7 gives the gauge-average equivalence only within ±11.8 % (day 1) and ±26.7 % (day 2). The 10 % applies only to the single gauge ch11. Superposition was not equivalence-tested at these margins: gauge average 0.92, pooled CI 0.77–1.06. The GLS combination gave 0.82, CI 0.73–0.91 (S7), which excludes 1, and the main text does not mention this.
- Fix: "...consistent with invariance within the 12–27 % that the noise resolves, and with superposition (0.92, 95 % CI 0.77–1.06)". In Section 4.2, say that 10 % refers to ch11 only.

### S6. Data availability and the cover letter claim more than the archive holds
- Location: Statements and Declarations, Data availability; cover letter "Data availability" paragraph; S11.
- Quotes: "The laboratory and Mây Bridge data, the analysis scripts with the console output of each run, and the derived data behind every figure and table are provided as Supplementary Material." S11: "The derived data behind every figure and table are provided as CSV files."
- Why wrong: according to `code/supplementary/README.md` in `scripts.zip` ("What is not here"): (a) only the three-cycle means of the laboratory test exist (Table S5 and `lab_single_load_influence_line.csv`), with no raw laboratory records; (b) the raw dynamic records of the Gie Cục I and Phương Độ bridges behind Figs. S16–S17 (and the 0.23 mm in S9) are not included, and no CSV of derived data for those figures is in the archive; (c) `schm_figures.py` (Fig. 2, Figs. S16–S17) is marked "not re-run", with no console output; (d) several derived data sets are `.npz`, not CSV (`ident_static_scan.npz`, `mc_errors.npz`, `T4_weights.npz`, `ident_freq_curves.npz`). The Data availability statement never mentions the Gie Cục I and Phương Độ data at all. The main text says "Mây Bridge data", while the cover letter says "processed data of the in-service bridge". These should match.
- Fix: "The laboratory data (mean deflections, Table S5), the processed Mây Bridge data, the analysis scripts with their console output and the derived data (CSV and NumPy files) are provided... The dynamic records of the Gie Cục I and Phương Độ bridges (Figs. S16–S17) are available from the corresponding author on reasonable request [or: cannot be shared because ...]." Use "processed" in both documents.

## Minor

### M1. Abstract and Conclusion 1: the equal-rigidity condition is missing from the 0.19–0.32 band
- Quote: "nearly blind 0.19–0.32 of the span from the interior support on two equal spans". Table 1 and Table S3 give it for prismatic beams with γ = 1. Fix: "on two equal spans of equal rigidity".

### M2. Abstract, Conclusion 3, Intro (iii), cover letter: "side-span deflection constant" generalizes from the gauge at 0.4 L
- The admissible-set analysis covers only N8 at 0.4 L. Mid side span is "–" (not computed) in Table S15. Fix: "the deflection constant at 0.4 of the side span".

### M3. Intro (iii) uses "and" where the Abstract and Conclusion 3 use "or"
- Intro: "6.6 against 1.5 ... from the static data alone, and 2.4 against 1.1 with girder rigidity bounded". Section 5.2 stresses that these are alternative scenarios ("not an estimate and a correction"). Fix: use "or" everywhere.

### M4. Intro contribution (i): "blind and near-blind loci of five channel types"
- Near-blind bands are given only for strain and deflection (Tables 1 and S3). Rotation, shear and end reaction have blind loci only. Fix: "the blind loci of five channel types and the near-blind bands of strain and deflection channels".

### M5. Intro, sentence after (iii): "the in-service girder shows identifiability"
- The girder shows that the side-span constant is poorly identifiable. Fix: "the in-service girder illustrates the identifiability analysis".

### M6. Conclusion 1: "deflection channels are blind only near particular span ratios"
- In the closed form they are blind at exact span ratios and near-blind near them, and the condition depends on μ, i.e. also on the rigidity ratio γ (Eq. 6, "a longer or stiffer adjacent span"). Fix: "blind only at particular span and rigidity ratios (μ between 1 and 2), and nearly blind near them".

### M7. Cover letter item 1: "indicators that need no reference rigidity"
- Only N_M and R need no reference rigidity. N_w (Eq. 8) needs EI_ref, and Section 2.3 and Section 5 stress that the choice can dominate. Fix: "the strain indicator and a cancellation ratio that need no reference rigidity" (as in Conclusion 2).

### M8. Cover letter item 3: the tiltmeter claim drops its conditions
- Body: "the most informative of the measurements compared", "at the design pier stiffness", "If a model-based constant is wanted", with assumed uncertainties of 2.64 % and 3 %. Fix: "of the additional measurements compared, a pier tiltmeter is the most informative when a model-based constant is wanted".

### M9. Graphical Abstract, right panel: the headline does not match what the panel shows
- Headline "pier stiffness controls the side-span constant", but the panel plots the misfit ratio r87 against κ, not the constant. The middle panel also keeps a stray "(a)" label from Fig. 2. Fix: either plot N_w/C8 along α*(κ) (as in Fig. 7b) or retitle the panel, for example "Static readings bound pier stiffness only from below"; remove "(a)".

### M10. Conclusion 5 and Section 6 use a 200 m record; Section 5.3 uses 220 m
- Conclusion 5 and Section 6 / Table S17 use L_tot = 200 m. The 24.8 % single-gauge SD in Section 5.3 uses 220 m ("the 200 m unit plus a 20 m convoy allowance", S4), and S4 notes that 200 m gives 22.5 %. A complete crossing (Eq. 2) needs L_p + d_max > 200 m. Fix: use one record length in all summary statements, or state in Conclusion 5 that 200 m is a lower bound for a complete crossing.

---

## Results not shown in the body
None found. Every numerical claim in the Abstract, Conclusions and cover letter appears in Sections 2–6 or in the Supplementary Material and its logs. The only cross-place inconsistencies are those listed above: B2, S2(c), S5, M3 and M10.

## Count
- Blocking: 2 (B1, B2)
- Should-fix: 6 (S1–S6)
- Minor: 10 (M1–M10)
