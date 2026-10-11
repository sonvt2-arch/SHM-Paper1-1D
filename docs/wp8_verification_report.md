# WP8 verification report: `manuscript/structures/manuscript.md`

Scope: mechanical checks only. The manuscript was not edited and nothing was committed. Line numbers refer to `manuscript/structures/manuscript.md` unless another file is named. Check scripts live in the session scratchpad (`xcheck_struct.py`, `xcheck_cite.py`, `doi_check.py`, `numcheck.py`) and are not part of the repository.

## Summary

| Check | Result |
|---|---|
| Numbers (traceability.md, 107 rows, 394 tokens) | 0 unresolved mismatches after rounding and format handling. Derived (DER) values recomputed. Attribution and rounding notes below. |
| Equations | Tags 1–21 and A.1–A.2, sequential. 9 are never cited by number (see I1). |
| Figures | 1–10, sequential, each cited in text. Pass. |
| Tables | 1–9, A.1, B.1, C.1, sequential, each cited in text. Pass. |
| Section cross-references | All exist (2, 2.2, 2.3, 2.4, 3, 3.2, 4, 5, 6, 6.2, 6.3, 6.5, 7, 8). Pass. |
| Abstract vs body | Every number in the abstract appears in the body with the same value. Pass. |
| Citations | 47 entries, all cited, numbered in order of first appearance. Pass. |
| DOIs (Crossref) | 37 DOI entries checked. 34 match directly on first author, year and journal. 2 match after a name-format check ([22], [36]), no action. 1 year/author-list flag ([33]). |
| Missing DOIs | [44] and [45] are journal articles with placeholders and no DOI. Both resolved (see R1, R2). |
| Abstract word count | 245 (each math expression as one word), 258 (raw whitespace split). Limit is 250. Borderline, see F1. |
| Keywords | 6. Pass (limit 6). |
| Highlights | 5 bullets, 73–82 characters each. Pass (limit 85). |
| `[NEED VALUE]` | 11 occurrences (6 in body, 5 in references). Plus 2 other editorial brackets. |

## 1. Numbers

Method: each numeric token in the Value column of `traceability.md` was searched for in the source files named in its Source column (abbreviation map OLD, WP2, V3, WP3, L3, R3, CMI, CMD, CMS, WP4, L4, NOV, REF). Presence only; rounding was not automatically checked.

Derived values recomputed in this session:

| Value | Recomputed | Result |
|---|---|---|
| $(3+\sqrt{33})/6$ | 1.457427 | matches 1.45743 |
| $2\cos(\pi/9)$ | 1.879385 | matches |
| $5250/4168.15$, $5000/2513.43$ | 1.25955, 1.98931 | match 1.2596, 1.9893 |
| $(1.9893-1.2596)/1.9893$ | 36.7 % | matches "about 37 %" |
| $C_m$ fixed / pinned (R3) | $1.016\times10^{-4}/7.264\times10^{-6}$ = 13.99 | matches "about fourteenfold" |
| $3.61\times10^{-4}/4.38\times10^{-5}$ | 8.24 | matches "about eight times" |
| $2513.43/2501.19$ | 1.00489 | matches |
| $1/0.936$, $1/0.923$ | 1.068, 1.083 | match "1.07–1.08" |
| $4/7$ | 0.5714 | matches $R_m$ |
| $90/55$ | 1.636 | matches $\beta$ |
| $2\sqrt{44765}/1279$ | 0.3308 | matches "0.331" |
| $200\,\mathrm{GPa}\times16\,529.8\,\mathrm{mm}^4$ | $3.3060\times10^9$ N mm² | matches |

| ID | Location | Problem | Suggested fix | Severity |
|---|---|---|---|---|
| N1 | `manuscript/structures/traceability.md` l. 95 (Table 5 row) | Value 0.181 for normalised N8 pinned/kFE. CSV `norm_base_kFE` = 0.1815, which rounds to 0.182 under decimal half-up. 0.181 only under binary float rounding. | Check the unrounded value in `code/analysis/results/wp3_Cm_summary.csv` and state the rounding rule, or use 0.182. | Low |
| N2 | `traceability.md` l. 94 | "0.30" is attributed to V3 sec. C, but the token does not appear in `verify_3span.log`. | Correct the attribution (likely WP2 or WP3). | Low |
| N3 | `traceability.md` l. 45, 111, 117 | Sources cited as "draft l. 160" and "draft §5". No file named `draft` is in the source map, so these cannot be verified. | Name the file path. | Low |
| N4 | `traceability.md` l. 11 | Refers to `scratchpad/xcheck.py`. That script is not in the repository, so the "491 numbers" claim is not reproducible. | Commit the check script under `code/analysis/` and cite its repository path. | Low |
| N5 | `traceability.md` l. 90 | "2.5–3.6 × 10⁷" range: 3.6 is the rounding of 3.615 × 10⁷ (Lv40 line of `wp3_run.log`). Correct, but the range is not stated in the log as written. | No change needed; optionally cite the Lv40 line explicitly. | Info |

No hard mismatches remain. Earlier apparent mismatches (Table 4 values 126.57, 125.95, 7788.93 at OLD l. 1079 and 1087; DER values 1.2596 and 1.9893) were false positives from a space-normalisation bug in the check, and were confirmed manually.

## 2. Internal consistency

| ID | Location | Problem | Suggested fix | Severity |
|---|---|---|---|---|
| I1 | Eqs. at l. 136 (9), 167 (12), 173 (13), 179 (14), 185 (15), 320 (17), 322 (18), 346 (20), 437 (A.1) | Equations are numbered but never cited by number in the text. Eqs. (12)–(15) define $I_y^{\mathrm{trap}}$, $N_m$, $R_m$, $O_m$, the indicators of Section 2.4. Eq. (9) is covered only by the range "Eqs. (4)–(10)". | Cite these equations where the quantities are used, or remove the numbers from unused display equations. | Medium |
| I2 | l. 56 (Introduction, [40]) | "Field WIM from a vision-based mid-span deflection, with an accelerometer for axle detection" is not supported by the Crossref title of [40] ("based on vehicle-induced bridge deflection and impact dynamic responses"). | Check the full paper and correct the description if vision is not used. | Medium |
| I3 | l. 54 (Introduction, [35]) | "area-ratio features of the influence line ... for defect diagnosis" on a "two-span bridge". Crossref title of [35] refers to a "single sensor-based strain feature". | Check the paper and align the description (strain or deflection; span count). | Medium |
| I4 | l. 56 (Introduction, [37]) | "five-span continuous bridge" is not verifiable from Crossref metadata. | Confirm from the paper text (also noted in NOV row 10). | Low |

Checked with no finding: figure numbers 1–10 (each cited, captions sequential); table numbers 1–9, A.1, B.1, C.1; section cross-references; appendix references A–D; abstract numbers ($1.45743$, $1.700594$, $1.879385$, 1.19 %, 0.70 %, 82 %, fourteenfold, 55 + 90 + 55 m) all appear in the body with the same values; highlights 1–5 agree with the abstract.

## 3. References

Citations: every in-text citation [1]–[47] resolves to a list entry, and every entry is cited. Numbers are sequential, and the first-appearance order is 1, 2, …, 47.

Crossref (`https://api.crossref.org/works/<doi>`): first author surname, year and journal compared for the 37 entries with DOIs.

| ID | Location | Problem | Suggested fix | Severity |
|---|---|---|---|---|
| R1 | l. 655, [44] | Title is `[NEED VALUE: title]` and the DOI is missing. Crossref resolves 10.1098/rsta.2006.1935: "Effects of environmental and operational variability on structural health monitoring", Phil. Trans. R. Soc. A 365 (1851), 2007, pp. 539–560. Volume, issue, year and pages in the manuscript match. | Replace the placeholders with the title and `https://doi.org/10.1098/rsta.2006.1935`. Remove the second `[NEED VALUE]`. | High (placeholder) |
| R2 | l. 657, [45] | Title is `[NEED VALUE: title]` and the DOI is missing. Crossref resolves 10.1016/j.ymssp.2012.08.026: "Long-term monitoring and data analysis of the Tamar Bridge", Mech. Syst. Signal Process. 35 (1–2), 2013. Authors and year match. | Replace the placeholders with the title and `https://doi.org/10.1016/j.ymssp.2012.08.026`. | High (placeholder) |
| R3 | l. 661, [47] | "[NEED VALUE: confirm edition and year]" for AASHTO LRFD, 10th ed., 2024. No DOI expected. | Confirm the edition and year against the AASHTO publication. | Medium |
| R4 | l. 633, [33] | Year printed as 2024. Crossref gives online 2024-07-29, but the print issue is vol. 2679 issue 2, which is 2025. The author list has four authors (Shi, Yarnold, Hurlebaus, Mander) but the manuscript gives three without "et al.". | Choose the year convention used by the journal and add "J. Mander" or "et al.". | Medium |
| R5 | l. 579, [6] | Editorial note "[check exact title wording]" left in the entry. Crossref title matches the manuscript wording. | Delete the note. | Low |
| R6 | l. 587, [10] | Editorial note "[CAN_TAC_GIA: confirm this is the document intended]". No DOI (report with rosap URL). | Confirm the URL and delete the note. | Low |
| R7 | l. 583, 585, 587, 655, 657, 661 | Missing DOIs: [8], [9], [10], [41]–[43], [46], [47] have none. [41]–[43], [46] and [47] are books or standards, so no DOI is expected. [8] and [10] have URLs. [44] and [45] are journal articles, covered by R1 and R2. | No action beyond R1, R2, R5, R6. | Info |

Crossref results, no action needed:
- [22] family name returned as "Lu Deng". Surname matches "L. Deng" in the manuscript.
- [36] Crossref lists the authors as Nguyễn Quốc Bảo, Hoàng Tiến, Nguyễn Hùng Sơn. This matches "Q.B. Nguyen, T. Hoang, H.S. Nguyen" (name transliteration only). Year, volume, issue and pages match.
- [39] Crossref was first unreachable (connection reset). On retry: Zhang J., Liu Y., Fan X.; 2026; Structures 88. Matches.
- All other entries (1–7, 11–21, 23–32, 34, 35, 37, 38, 40): first author, year and journal match.

## 4. Formatting

| ID | Location | Problem | Suggested fix | Severity |
|---|---|---|---|---|
| F1 | Abstract, l. 15 | 245 words with each math expression as one word; 258 by raw whitespace split. The limit is 250, so the raw count is over. | Trim at least 9 words (for example, shorten "The criterion was applied to the acceptance-test data of a 55 + 90 + 55 m box girder" to "...applied to a 55 + 90 + 55 m box girder"). Recount with the journal's counting rule. | Medium |
| F2 | Keywords, l. 17 | 6 keywords. Pass. | None. | Info |
| F3 | `manuscript/structures/highlights.md` | 5 highlights, 73–82 characters each. Pass. | None. | Info |
| F4 | Body, l. 249, 372, 413, 531 (2×), 539 | 6 `[NEED VALUE]` placeholders in the body (acceptance-test data permission, Type A evaluation, laboratory limitations sentence, data availability, acknowledgement). | Resolve before submission. | High |
| F5 | References, l. 655 (2×), 657 (2×), 661 | 5 `[NEED VALUE]` placeholders in references (see R1–R3). | Resolve as in R1–R3. | High |
| F6 | l. 579, 587 | 2 editorial brackets that are not `[NEED VALUE]` (see R5, R6). | Delete. | Low |

Total `[NEED VALUE]` occurrences: 11.
