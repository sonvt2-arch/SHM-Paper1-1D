# Open items for the authors (manuscript v4)

Items that cannot be closed from the repository. The authors decided that no further experiments will be done; items that would need new tests are recorded as limitations in §7, not as tasks.

## A. Decisions for the authors

| # | Item | What is needed |
|---|---|---|
| A1 | Title | Current: "Blind loci and design criteria for integral load-monitoring channels on continuous girder bridges, with laboratory verification and an assessment on public field records". Alternatives: (i) "Where can an influence-area integral see the load? Design criteria for continuous girders, verified in the laboratory and assessed on public field records"; (ii) "Designing integral load-monitoring channels for continuous girders: blind loci, identifiability and what field records can and cannot confirm". Choose one; the cover letter must follow. |
| A2 | Threshold convention | §2.3 keeps $|N_w|<0.2$ and $|N_M|<0.2$ and states that they correspond to 8 % and 20 % of the simply supported mid-span value. Alternative: renormalise $N_w$ by $384EI/(5L^4)$ so that both equal 1 for the simply supported reference; this would rescale every $N_w$ value (Tables 5, A.1, Figs. 2, 3, 8, 9) by 0.4 and change the deflection near-blind bands, which would then have to be recomputed with `code/theory2/gc_theory.py`. Not done in v4. |
| A3 | Field-test predictions (Table 6) | Kept as predictions. Remove if the Cầu Mây moving-load test will not be carried out. |
| A4 | Comparison with the original NOR-BWIM accuracy | §4.5 carries `[NEED VALUE]` for the GVW accuracy reported in refs [41–43] (Moghadam et al.) for the same bridge. The papers are paywalled and were not read; supply the value or delete the clause. |
| A5 | Yan et al. 2022 [34] | Cited from its Crossref record (title, authors, volume, article number). The full text was not read; the sentence in §1 describes the method only from its title and the general property of transmissibilities at zero frequency. Check against the paper. |
| A6 | Three-load order | As in v3: order chosen by fit (§3). Confirm or supply the laboratory log. |
| A7 | Dropped references | To meet the 55-reference limit, v3 refs [3] Invernizzi (Polcevera), [6] Fattorini, [10] FHWA truck size study, [24] Luo (Bayesian), [26] Kapoor (PIML) and [32] Yang 2023 were removed; 54 references remain. Restore any that the authors consider essential (and drop others). |

## B. Values still missing (`[NEED VALUE]` in the files)

| # | Item | Location |
|---|---|---|
| B1 | Accuracy class of laboratory weights | Table 8 row "Reference weighing" |
| B2 | Dial-gauge instrument type, fixed reference datum, temperature correction, load-hold time, zero-reading procedure (editor 4) | §5.1 |
| B3 | GVW accuracy of the original NOR-BWIM system on the same bridge | §4.5 |
| B4 | Repository and DOI for the Cầu Mây processed data | Data Availability; cover letter |
| B5 | Authors involved in the HUCE consultancy test and their relationship | Conflicts of Interest |
| B6 | Employer and APC source | Funding Statement |
| B7 | Acknowledgement of Hai Duong PMU and the testing consultant | Acknowledgments |
| B8 | Overlap with the two papers under review at *Structures* (rig, data, text); attach them as papers for the editor | cover letter |
| B9 | Cover-letter date | cover letter |

## C. Figures and files

| # | Item |
|---|---|
| C1 | Fig. 1 (notation) and Fig. S15 (laboratory specimen and influence line) must be supplied by the authors. |
| C2 | Supplementary Table S1 (full 23-row invariance table) and Table D.1 (laboratory data, former Appendix D) must be assembled into the supplementary file; sources are `code/norbwim/results/v4_invariance.csv` and `manuscript/v3/manuscript.md` Appendix D. |
| C3 | Field-plan figures (`code/fieldplan`) are not used in v4. They still carry Vietnamese labels without diacritics; relabel before any reuse. |
| C4 | Raw readings of the three laboratory cycles and the Cầu Mây readings of all load cycles are still not in the package. |

## D. Checks done in this version

| # | Item | Status |
|---|---|---|
| D1 | Agüero-Barrantes et al. [31], year | Confirmed 2021 on the journal landing page (Vol. 11 (2021)); v3 caveat closed. |
| D2 | Lobo Aguilar and Christenson [30] | DOI 10.15517/mym.v8i1.34551 resolves; Crossref lists an online date of 2025, but the journal page gives Vol. 8 (2018), citation date 2018, pp. 11–22. Added. |
| D3 | Yu, Cai and Deng [15] | Crossref: Struct. Infrastruct. Eng. 14 (8) (2018) 1108–1122, doi 10.1080/15732479.2017.1401095. Added. |
| D4 | Yan, Hao, Yuen and Papadimitriou [34] | Crossref: MSSP 177 (2022) 109133. Added (see A5). |
| D5 | Self-citation count (rule VII.8) | `kiem_tu_trich.py dem`: 0 matches with the supervisor's list; within the limit. |
| D6 | Figure re-plots | Logs and result files unchanged after rerunning `gc_figures.py`, `multisensor_figures.py`, `ident_static.py`, `nb_v4.py` (git status shows only figure files and the label edits in the scripts). |
| D7 | Multiple presence on a 200 m unit; within-lane wander; speed variation along 605 m | Not quantified; stated as limitations (§6, Table 8). |

## E. Carried over and still open

ORCID of the submitting author; suggested reviewers if the form asks; the individual Cầu Mây weigh tickets and convoy composition; whether the report FE values used nominal or weighed loads.
