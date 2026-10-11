# SCHM submission checklist

Requirements from the current SCHM author guidelines and Wiley policy, as recorded in `schm_requirements.md` (sources G1, W1, W2, D1, H1). Status: **Done** = met in `manuscript/schm/`; **Author** = needs input from the authors (see `open_items.md`); **At upload** = done when the Word file is built or the submission form is filled; **Unverified** = not stated in the guide, prepared anyway.

| # | Requirement | Source | Status | Note |
|---|---|---|---|---|
| 1 | Article type: Research Article | G1 | Done | Stated in the cover letter |
| 2 | Not published or under consideration elsewhere; all co-authors approve | G1 | Author | Cover letter states it; overlap with the two papers under review at *Structures* must be confirmed (`open_items.md` 5) |
| 3 | Editable .docx with text and tables (or LaTeX + PDF) | G1 | At upload | Build from `manuscript.md`; equations as Word equations |
| 4 | Line numbers | G1 (recommended) | At upload | Switch on continuous line numbering in Word |
| 5 | Title, full author names, full institutional mailing addresses, e-mails | G1 | Done | Faculty of Bridge and Road Engineering address and three e-mails on the title page |
| 6 | Co-author names and e-mails entered at submission | G1 | At upload | Values on the title page |
| 7 | ORCID iD of the submitting author | G1 | Author | `open_items.md` 11 |
| 8 | Short title ≤ 70 characters | G0 only | Unverified | Prepare one if the form asks, e.g. from the title's first clause |
| 9 | Abstract self-contained, citation-free, ≤ 300 words | G1 | Done | 236 words, no citations (`wp7b_checks.py manuscript/schm`) |
| 10 | Keywords | not in G1 | Unverified | Six, starting with "Structural health monitoring; Sensor placement" |
| 11 | Introduction succinct, without subheadings | G1 | Done | Section 1 has no subheadings |
| 12 | Methods detailed enough to replicate; reused methods cited | G1 | Done | Sections 2–4, Appendices A–D; Ojio–Yamada [27] credited for Eq. (11) |
| 13 | Results and discussion; Conclusions | G1 | Done | Sections 3–7; Section 8 Conclusions |
| 14 | Data Availability statement | G1 | Author | Section present; owner permission and record owner `[NEED VALUE]` ×2 (`open_items.md` 2); choose the matching pre-written statement in the form |
| 15 | Conflicts of Interest, with reasons for any interest | G1 | Author | Section present with the SCHM wording; HUCE consultancy question `[NEED VALUE]` (`open_items.md` 6) |
| 16 | Funding Statement naming funders, or the employer when unfunded; APC funding declared | G1 | Author | Section present; employer and APC source `[NEED VALUE]` (`open_items.md` 7) |
| 17 | Acknowledgments at the very end before the references; acknowledged persons agree | G1 | Author | Section present in that position; Hai Duong PMU and consultant `[NEED VALUE]` (`open_items.md` 3) |
| 18 | Supplementary material section before the references, describing each file | G1 | Done / Author | Section present; some promised scripts are not in the repository (`open_items.md` 9) |
| 19 | Generative AI use described (tool, purpose, verification) and disclosed at submission | W1 | Done / At upload | "Disclosure of Generative AI Use" (verbatim) and Computational Implementation sentence (verbatim); tick the AI disclosure in the form |
| 20 | References numbered in order of first citation, square brackets, all cited | G1 | Done | 51 references, [1]–[51]; style converted to Chicago by the publisher after acceptance |
| 21 | Each reference complete and accurate | G1 | Done | Checked in WP7b (Crossref; `traceability.md`, `docs/reference_check.md`); no change in this version |
| 22 | Figures in the manuscript file at submission, cited consecutively | G1 | At upload | Figs. 1–10 cited in order; embed near first citation |
| 23 | Bitmap figures ≥ 300 dpi, or vector | G1 | Done / Author | Figs. 3, 7, 8, 9, S1: 600 dpi PNG and vector PDF in `figures/`. Figs. 1, 2, 4, 5, 6, 10 must come from the authors (`open_items.md` 8) |
| 24 | One source file per figure after acceptance | G1 | Done / Author | One file per figure for the redrawn figures |
| 25 | Tables cited consecutively, descriptive titles, units in headings | G1 | Done | Tables 1–10 and A.1–C.1 |
| 26 | No vertical rules in tables | G1 | At upload | Word table style without vertical borders |
| 27 | SI units; dates written in full | G1 | Done | "June 2020" in §4.1; cover-letter date to be written in full |
| 28 | Highlights / graphical abstract | not in G1 | Done | Highlights removed (Elsevier item) |
| 29 | Word or page limit | G1 (none) | Done | No limit; main text 9221 words |
| 30 | Cover letter | not in G1 | Done / Author | `cover_letter_SCHM.md`; date and overlap statement `[NEED VALUE]` |
| 31 | Suggested reviewers | not in G1 | Unverified | Prepare names if the form asks (`open_items.md` 12) |
| 32 | At most three manuscripts per author under review at SCHM | G1 | Author | Confirm for each author |
| 33 | APC payment attested by the corresponding author | D1, Wiley APC page | Author | DOAJ lists up to 2740 USD with a waiver policy; check the 2026 amount and waiver |
| 34 | Permission for any reused copyrighted material; licence of tools introduced | G1 | Done | No third-party figures; Abaqus [45] cited as software used |
| 35 | Similarity check (iThenticate) | G1 | Author | Relevant to item 2 if text is shared with the *Structures* papers |
