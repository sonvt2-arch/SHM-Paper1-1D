# SCHM author requirements (checked 2026-10-11)

Journal: *Structural Control and Health Monitoring* (SCHM), Wiley, gold open access (CC BY), ISSN 1545-2263 (online), 1545-2255 (print).

## Sources

| Code | Source | How it was read |
|---|---|---|
| G1 | Current author guidelines, "Author Guidelines - Structural Control and Health Monitoring - Wiley Online Library", served at https://www.hindawi.com/journals/schm/guidelines/ (redirects to the Wiley page; the canonical Wiley URL is https://onlinelibrary.wiley.com/page/journal/schm/author-guidelines) | Full text via Exa crawl; the Wiley URL itself returned "crawl not found", publisher pages give HTTP 403 to direct fetch |
| G0 | Older Wiley "Instructions to Authors", https://onlinelibrary.wiley.com/page/journal/15452263/homepage/guide.htm | Exa snippet only. Pre-2023 (ScholarOne, 250-word abstract). **Superseded by G1; not used except where noted.** |
| H1 | Journal homepage, https://onlinelibrary.wiley.com/journal/schm | Exa crawl showing articles first published up to 4 October 2026: "Edited by: Lucia Faravelli, University of Pavia, Italy" |
| D1 | DOAJ record, https://doaj.org/toc/1545-2263 | Exa snippet: APC up to 2740 USD / 1830 GBP / 2380 EUR; waiver policy exists; OA since 2023 |
| W1 | Wiley AI FAQ, https://www.wiley.com/en-us/publish/ai-insights/research-publishing-faq/ ; Wiley ethics guidelines, https://authorservices.wiley.com/ethics-guidelines/index.html | Exa snippets |
| W2 | Wiley "Submitting your manuscript" help, https://authors.wiley.com/help/submitting-your-manuscript.html | Exa snippet |

"Verified" below means the requirement is stated in G1 (or the listed source). "Unverified" means it could not be confirmed from a primary page and must be checked in the submission system.

## Requirements

| Item | Requirement | Source | Status |
|---|---|---|---|
| Article type | "Research articles … present the results of an original research study". Other type: Reviews. This paper: Research Article. | G1 "Article types" | Verified |
| Submission system | Wiley Research Exchange; Wiley Researcher ID; all co-author names and e-mails required at submission; file is scanned and the author confirms the parsed fields | G1 "Submission"; W2 | Verified |
| ORCID | ORCID iD must be provided for the submitting author | G1 "ORCID" | Verified |
| File format | Editable .doc/.docx with text and tables (or LaTeX .tex plus a PDF for review) | G1 "Formatting" | Verified |
| Line numbers | Recommended | G1 "Formatting" | Verified (recommendation) |
| Title page | Title, full author names, full institutional mailing addresses, e-mail addresses | G1 "Title and authorship information" | Verified |
| Short title | Up to 70 characters | G0 only | Unverified for the current system |
| Abstract | Self-contained, citation-free, **≤ 300 words** | G1 "Abstract" | Verified |
| Keywords | Not mentioned in G1 | G1 | Unverified; the submission form may ask for them. Six keywords kept, including "Structural health monitoring" and "Sensor placement" |
| Structure | Recommended: Title and authorship; Abstract; Introduction (succinct, no subheadings); Materials and methods (subsections allowed); Results and discussion; Conclusions; Data availability; Conflicts of interest; Funding statement; Acknowledgments (at the very end, before the references); Supplementary material section before the references; References | G1 "Formatting" … "References", "Preparation of tables" | Verified. The guide says "We recommend"; descriptive numbered section titles (Theory, Laboratory verification, …) are kept, since the guide does not prescribe heading names |
| Data availability | Statement required; pre-written statements offered at submission; Data Sharing Policy applies | G1 | Verified |
| Conflicts of interest | Declare all interests that could be perceived as conflicting and explain why; if none: "The author(s) declare(s) that there is no conflict of interest regarding the publication of this article" | G1 | Verified |
| Funding statement | Name funders in full with grant numbers; if no specific funding but done as part of employment, name the employer; funding for the APC must also be declared | G1 | Verified |
| Acknowledgments | At the very end before the references; non-author contributors acknowledged with their permission | G1 | Verified |
| Author contributions | Not required by G1 | G1 | Kept as "Author Contributions" (CRediT roles); optional |
| Generative AI | Describe AI use in the Methods section, or via a disclosure, or in the Acknowledgements; state tool, purpose, effect on arguments, and how the authors verified the content; disclose at submission. Spelling/grammar tools are outside scope | W1 | Verified (Wiley-wide policy, not journal page) |
| References | Any style accepted; reformatted to Chicago after acceptance; numbered consecutively in order of first citation; in-text numbers in square brackets, e.g. [9] or [9, 10]; uncited references removed | G1 "References" | Verified |
| Figures | Included in the manuscript file at submission; separate source files after acceptance, one file per figure; cited consecutively; vector (EPS, WMF, …) or bitmap (TIFF, JPEG, …); **bitmap ≥ 300 dpi**; labels in separate layers for bitmaps | G1 "Preparation of figures" | Verified |
| Tables | Cited consecutively; descriptive title; units in column headings; **no vertical rules** | G1 "Preparation of tables" | Verified |
| Units, dates | SI units; dates written out in full | G1 | Verified |
| Word / page limits | None stated; "no space restriction on methods" | G1 | Verified (no limit) |
| Cover letter | Not mentioned in G1 | G1 | Unverified; a cover letter is prepared anyway |
| Suggested reviewers | Not mentioned in G1 | G1 | Unverified; the submission form may ask |
| Highlights, graphical abstract | Not mentioned in G1 (Elsevier items) | G1 | Not used |
| Peer review | Single-anonymised; at least two external reviewers | G1 | Verified (no anonymisation of the manuscript needed) |
| Concurrent submissions | At most three manuscripts per author under review at the journal | G1 | Verified |
| Preprints | Allowed; cite the preprint | G1 | Verified |
| Similarity check | iThenticate CrossCheck | G1 | Verified |
| APC | Journal is OA with an APC; DOAJ lists up to 2740 USD, with a waiver policy | G1, D1 | Amount from DOAJ, not from the Wiley page: unverified for 2026 |
| Editor | "Edited by: Lucia Faravelli, University of Pavia, Italy" | H1 | Name verified; the exact title ("Editor-in-Chief") is not stated on the crawled page |

## Consequences for the manuscript (applied in `manuscript.md`)

- Highlights removed (`highlights.md` not carried over from v2).
- Declarations renamed and ordered as in G1: Data Availability, Conflicts of Interest, Funding Statement; then Author Contributions, the AI disclosure (Wiley's "via a disclosure" route; the Computational Implementation section also states the use), Acknowledgments, Supplementary Materials, References.
- Elsevier wording "Declaration of competing interest" replaced by the G1 wording; the Funding Statement asks the authors to name the employer and the APC source.
- References stay numbered in square brackets in order of first citation; the publisher converts to Chicago after acceptance, so no restyling was done.
- Abstract 236 words (limit 300). No word limit applies; main text 9221 words (`wp7b_checks.py`).
- Figures: ≥ 300 dpi PNG (600 dpi produced) plus vector PDF in `figures/`. Tables: remove vertical rules when the Word file is built.
