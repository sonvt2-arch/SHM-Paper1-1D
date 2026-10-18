# Open items that need the authors (SCHM version)

Only items that cannot be closed from the repository are listed. Everything else from the red-team report and from `manuscript/v2/open_items.md` is either done or not relevant to SCHM (see `response_to_red_team.md`, SCHM addendum).

| # | Item | Where it shows | What the authors must supply |
|---|---|---|---|
| 1 | Accuracy class of the laboratory weights | manuscript §7.2 `[NEED VALUE]`; Table 10 uses 0.1 % for reference weighing | Accuracy class or calibration certificate of the steel weights (and of the 4.143 kg reference with hook) |
| 2 | Data repository | Data Availability `[NEED VALUE: repository name and DOI]` | Permission answered 2026-10-18 (C12: an author performed the load tests, so the processed data may be published). Still needed: the repository and DOI where the processed Cầu Mây data and Section 5 records will be deposited; confirm that the permission also covers the Gie Cuc I and Phuong Do records (docs/08 maps C12 to D6) |
| 3 | Acknowledgement | Acknowledgments `[NEED VALUE]` | Whether to thank Hai Duong PMU and the testing consultant (with their permission, as SCHM requires for acknowledged contributors) |
| 4 | Cầu Mây individual weigh tickets | §4.1 says the individual masses are not used | Partly answered 2026-10-18: mean of the 10 weighed trucks 25.06 t, now used in Table 8 (one entry changed, 36 → 35 %) and checked for Tables 5–6 (`wp9_truckweight_check.py`: changes ≤ 0.003, values kept). Still open: the tickets themselves (probably in `Thông tin bổ sung.rar`), which trucks formed each convoy, and whether the report FE values used nominal or weighed loads |
| 5 | Overlap with the authors' two papers under review at *Structures* | cover letter `[NEED VALUE]` | State whether those papers use the same laboratory rig, data or text. If yes, cite them (as "under review") or describe the overlap in the cover letter; SCHM screens with iThenticate |
| 6 | Competing interest, HUCE consultancy | Conflicts of Interest `[NEED VALUE: name(s) of authors involved and nature of relationship]` | Partly answered 2026-10-18: the load test was performed by the authors' team within inspection work of Công ty TNHH Tư vấn Đại học Xây dựng (statement now in the manuscript). Still needed: which author(s) took part and their relationship to the company (employee, consultant, owner or contractor), so that it can be declared as SCHM requires |
| 7 | Funding statement | Funding Statement `[NEED VALUE]` | SCHM asks for the employer when there is no specific grant, and for the source of the APC (DOAJ lists up to 2740 USD with a waiver policy; check the current amount and waiver eligibility) |
| 8 | Laboratory and other figure files | `figure_table_plan.md` | Figs. 1, 2, 4, 5, 6 and 10 from the JCSHM Word file (old Figs. 1, 10, 3, 4, 6, 11) as source files at ≥ 300 dpi or vector; Fig. 1b must be drawn new |
| 9 | Supplementary scripts not in the repository | Computational Implementation; Supplementary Materials | The Monte Carlo study (Appendix B), the moving-load analysis (Section 6.5), the symbolic verification of the two-span solution and the Table 3 quadrature computation were not found in `code/` (searched for Newmark, Monte Carlo and Simpson; `wp7b_peps.py` covers only the interval counts). The manuscript promises them as supplementary material, so supply them or reword that sentence |
| 10 | Cover-letter date | cover letter `[NEED VALUE: date]` | Date of submission (written out in full, e.g. "12 October 2026") |
| 11 | ORCID and co-author e-mails | submission form | ORCID iD of the submitting author (required); e-mails of all co-authors (already on the title page) |
| 12 | Suggested reviewers | submission form, if asked | The guide does not require them; prepare two or three names with affiliations and e-mails in case the form asks |

## Answered on 2026-10-18 (closed)

| Item | Answer used | Where |
|---|---|---|
| Field instruments and conditions (Paper1 B6) | Mitutoyo dial gauges; daylight, hot sunny weather; positions by tape and paint, error < 20 cm | §4.1; effect of a 0.20 m longitudinal shift quantified in §4.4 (`wp9_truckweight_check.py`, Part P); transverse error and temperature stated as not quantified |
| Truck geometry (Paper1 B4, part) | Track 1.85 m; 1.1 m transverse spacing | §4.1 |

Still unanswered from the Paper1 questionnaire (`docs/word/Cau_hoi_bo_sung_so_lieu.docx`): B1–B3 (design FE model of the main bridge, pier dimensions, readings in unloaded spans), B7 (raw files of moving passes), part A (laboratory). These do not create placeholders in the manuscript but limit Section 4 as stated in §7.2.
