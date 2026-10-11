# Open items for the authors (manuscript v2)

Reference numbers below are the v2 numbers.

## A. Missing values ([NEED VALUE] in the files)

| # | Where | What is needed |
|---|---|---|
| A1 | manuscript §7.2 | Accuracy class (or calibration uncertainty) of the laboratory weights; Table 10 uses 0.1 % for reference weighing. |
| A2 | Data availability | Permission statement of the owner (Hai Duong PMU) for the Cầu Mây acceptance-test data; owner of the Gie Cuc I and Phuong Do records and the permission statement for them. |
| A3 | Acknowledgements | Whether to thank Hai Duong PMU and the testing consultant. |
| A4 | Cover letters | Date; suggested reviewers (two placeholders in each letter). |
| A5 | Type A evaluation (no placeholder in the text) | The individual readings of the three laboratory cycles are not in the repository. With them, the "A (bound)" rows of Table 10 can be replaced by evaluated values. The text now states that the entries are bounds. |
| A6 | Truck weights (no placeholder in the text) | The text says that the test report gives no weighbridge values (source: `data/bridges/cau-may/INVENTORY.md`). If weighbridge tickets exist, Table 6 and Table 8 should be recomputed with them. |

Resolved since v1: ref. [48] Sohn 2007 and ref. [49] Cross et al. 2013 (titles and DOIs from Crossref, matching the intended content: environmental and operational variability in SHM, and long-term monitoring of the Tamar Bridge); ref. [51] AASHTO LRFD 10th ed. 2024 (confirmed by the AASHTO Journal announcement and an FHWA memo of 17 March 2026); ref. [6] title now follows Crossref; ref. [10] note removed (URL resolves to FHWA-PL-00-029, Vol. II; the authors should still check that it supports the statement on station cost); ref. [35] Shi et al. now 2025, issue 2, four authors.

## B. Decisions for the authors

| # | Decision | Default in v2 |
|---|---|---|
| B1 | Target journal | Main text is journal-neutral with an SHM sensor-placement framing (title, abstract, keywords). Two cover letters: `cover_letter_SCHM.md`, `cover_letter_SIE.md`. The red team recommends SCHM; SCHM is gold open access with an APC and the paper declares no funding. Check the APC and any waiver before choosing (red-team issue 32). |
| B2 | Which Cầu Mây calibration is "physical" | v2 reports both and does not choose. Calibration B implies a girder 28 % softer than design on piers about four times stiffer than k_FE; calibration A implies a girder 9 % stiffer. The authors may add an engineering argument if they have pier drawings, the MIDAS model or ambient frequencies. Without such data, the text should stay as it is. |
| B3 | Possible overlap with the authors' other submissions (red-team issue 31) | If the laboratory rig, data or text overlap with the two papers under review elsewhere, cite them or disclose in the cover letter. Not done, because the repository does not show what those papers contain. |
| B4 | Conflict-of-interest wording | The Cầu Mây test was carried out by the HUCE consultancy (Công ty TNHH Tư vấn Đại học Xây dựng), named in the Data availability statement. Decide whether the competing-interest statement should mention it. |
| B5 | SIE-specific reframing (red-team issue 22) | Only light changes in the neutral text (a sentence on the screening workflow in §7.1). If SIE is chosen, consider moving most of Section 2 derivations to an appendix and adding a decision table for the owner (gauge option against expected bias). |
| B6 | Title | v2: "Total-load observability of continuous girder bridges from a single deflection channel: closed-form blind configurations, laboratory verification and sensor placement on an in-service box girder". |
| B7 | Main-text length | 9563 words by `code/analysis/wp7b_checks.py` (v1 measured by the same script: 8168). SCHM has no strict limit; check the SIE guide if SIE is chosen. Candidates for further cuts: §6.5 second half, §2.2 decomposition paragraph. |
| B8 | Ojio and Yamada (2002) original | Still cited through Cardini and DeWolf [27] and Helmi et al. [28]; Helmi et al. list it as a 3rd ICWIM paper. Add the original if it can be obtained. |
| B9 | Computational-implementation sentence on AI | Kept unchanged, as is the AI declaration. |
| B10 | Internal docs with the old "whole side span blind" wording | `docs/wp2_three_span_theory.md` and `docs/04_tong_hop_ket_qua_lo_trinh_A.md` still use it. They are not supplementary material and were not edited. The two console logs that will ship as supplementary material were relabelled (script labels changed and scripts rerun; numbers unchanged). |

## C. Recommended further work (not done)

- Direct invariance test on the existing rig (fixed total load, varying spacing and load magnitude) and the blind-configuration test (spans 2500 + 3644 mm): §3.3, §7.2.
- Cầu Mây: pier drawings, MIDAS model or ambient natural frequencies, to separate girder rigidity from pier stiffness (§4.2).
- Fig. 7 redraw with the calibration-B influence lines (`figure_table_plan.md`).

## D. Checks done in WP7b

- `python3 code/analysis/wp7b_checks.py`: abstract 236 words (240 by raw whitespace split; limit set to 240); main text 9563 words (Sections 1–8, prose only; inline math as one word); highlights 73–79 characters; 6 keywords; 23 numbered equations, all cited by number.
- `python3 code/analysis/wp7b_peps.py` → `code/analysis/logs/wp7b_peps.log`: P_ε and bias for both calibrations, C_m sensitivity to k, laboratory linearity ratios, Table 10 by root-sum-square, near-blind band edges.
- References renumbered by order of first appearance (51 entries, all cited).
