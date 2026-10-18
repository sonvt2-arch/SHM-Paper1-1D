# Open items for the authors (manuscript v3)

Items that cannot be closed from the repository. Items 1–12 of `manuscript/schm/open_items.md` that are still open are carried over with their new location.

## A. Decisions for the authors

| # | Item | What is needed |
|---|---|---|
| A1 | Title | Current: "Load observability of continuous girder bridges: a general response-integral theorem, optimal offset-immune estimation and field verification". Alternatives: (i) "Which channel sees the load? Response-integral observability, offset-immune estimation and field verification for continuous girder bridges"; (ii) "Designing load-monitoring channels for continuous girder bridges: blind loci, optimal invariant estimation and identifiability, verified on moving-truck field data". Choose one. |
| A2 | Laboratory tests editors asked for | The fixed-total-load test at several spacings and the blind-configuration test (2500 + 3644 mm) are still not done; §3.2 and §7 say so. All four editors rated the lack of a continuous moving-load test as the main weakness; the NOR-BWIM analysis now covers moving loads on a continuous girder, but not the blind configuration. |
| A3 | Field test at Cầu Mây | §5.5 and Table 5 present the field-test plan only as predictions. Confirm that this is acceptable, or remove Table 5 if the test will not be carried out. |
| A4 | Three-load order | §3.1 now states that the order was not recorded independently and was chosen by fit. Confirm, or supply the laboratory log if the order was recorded. |
| A5 | Reference count | 57 references (the house rule is 40–55). Candidates to drop if needed: [6], [26], [10]. |

## B. Values still missing (`[NEED VALUE]` in the files)

| # | Item | Location |
|---|---|---|
| B1 | Accuracy class of laboratory weights | Table 7 row "Reference weighing" |
| B2 | Repository and DOI for the Cầu Mây processed data | Data Availability; cover letter |
| B3 | Authors involved in the HUCE consultancy test and their relationship | Conflicts of Interest |
| B4 | Employer and APC source | Funding Statement |
| B5 | Acknowledgement of Hai Duong PMU and the testing consultant | Acknowledgments |
| B6 | Overlap with the two papers under review at *Structures* | cover letter |
| B7 | Cover-letter date | cover letter |

## C. Figures and files

| # | Item |
|---|---|
| C1 | Fig. 1 (notation) and Fig. 5 (laboratory specimen and influence line) must be supplied by the authors; see `figure_table_plan.md`. |
| C2 | Fig. 8 panel (a) title says "manuscript Eq. 13"; re-plot (`code/theory2/gc_figures.py`) with the v3 equation number (10) or without an equation number. Fig. 3 title: write "Cầu Mây" with diacritics. Fig. 9: produce a PDF and add panel labels. |
| C3 | Supplementary Figs. S17–S18 (field plan) carry Vietnamese labels without diacritics; re-plot in English before submission. |
| C4 | Raw readings of the three laboratory cycles (editor 4) and the Cầu Mây readings of all three load cycles are still not in the package. |

## D. Checks done in this version, with caveats

| # | Item | Status |
|---|---|---|
| D1 | Agüero-Barrantes et al., doi 10.15517/mym.v11i0.46400 | Exists (Crossref). Title "Sparse sensing Bridge Weigh-In-Motion for single-span bridges", Métodos y Materiales 11, 43–53; relevant (influence-area BWIM, number and location of sensors). **Caveat:** Crossref lists the online date as 2025-09-08 while the DOI was created on 2021-12-07; the reference gives 2021 (volume 11). Confirm the year on the journal page. Author order on Crossref: Agüero Barrantes, Lobo Aguilar, Christenson. |
| D2 | Wu et al., doi 10.1007/s11709-020-0653-0 | Exists (Crossref): Front. Struct. Civ. Eng. 14 (5) (2020) 1232–1246; relevant (continuous multi-girder bridge, lane-specific influence lines). Cited in §1 and §4.3. |
| D3 | Ojio and Yamada (2002), primary source | Verified through TRID record 723286 and a library reference list: ICWIM3, Orlando, 13–15 May 2002, pp. 209–218. The full text was not read; the description in §1 (integration of stringer strain, speed, calibration with a known truck) follows the TRID abstract. TRID gives the second author as Koji Yamada. |
| D4 | NOR-BWIM metadata | Dataset DOI verified on DataCite (CC0). The companion papers [43–45] were not opened (paywalled); all metadata come from the dissertation [51] and the dataset files. Driver-reported day-1 weights, the run-to-evaluation mapping and the gauge calibration factors are assumptions of the analysis (3B §2, §5). |
| D5 | Ranges for the alternative N8 position (mid side span) over the admissible sets | Not computed by `ident_static.py`; shown as "–" in Table 4. Can be added by extending the script. |
| D6 | Offset-immune estimator on the NOR-BWIM records | Not evaluated; §4.4 says whether the day-2 wander is common-mode was not tested. A quick test (zero-sum combination of the four day-2 gauges) would turn this sentence into a result. |
| D7 | Transverse-position term | Only the measured lane ratio and the Cầu Mây spread are reported; no grillage/shell model was built. |
| D8 | Probability of isolated crossings on the 200 m unit | Not quantified (§6.3); needs traffic counts. |

## E. Carried over from SCHM v2 and still open

ORCID of the submitting author; suggested reviewers if the form asks; the individual Cầu Mây weigh tickets and convoy composition; whether the report FE values used nominal or weighed loads (SCHM open items 4, 11, 12).
