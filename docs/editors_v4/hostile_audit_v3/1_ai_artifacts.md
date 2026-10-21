# Hostile audit v3, report 1: AI and tool artifacts in the ASE submission package

## Scope and method

Package audited: `manuscript/ase` (manuscript.md, supplementary_material.md, cover_letter_ASE.md; word/*.docx and *.pdf; figures/*.png, figures/supplementary/*.png, GraphicalAbstract.png; word/scripts.zip unzipped into a fresh scratch directory and only read or grepped, nothing executed). Nothing in the repository was edited except this report. Method: regex sweeps of the three Markdown sources, of the PDF text (`pdftotext -layout`) and of `word/document.xml` text and OMML runs in each DOCX; inspection of comments.xml, tracked-change tags, core.xml, app.xml, custom.xml, footers and bookmarks; `pdfinfo` and `pdffonts`; a page render of the PDF equation pages; a full read of manuscript.md and cover letter and of the prose parts of the supplement; each of the 25 PNG figures opened and read visually; full file listing, grep and README/script-header reading of scripts.zip (195 files).

Categories checked with no finding:
- Placeholders in the three sources, in the DOCX/PDF text and in scripts.zip: no `[NEED VALUE]`, `[CITE]`, TODO, XXX, TBD, FIXME. (The only "TBD"-like hits in the zip are false positives such as "Warning" and "NaN" in logs.)
- Markdown/LaTeX residue in DOCX and PDF text: no `**`, backticks, `$`, `{#..}`, `<!-- -->`, raw `\commands`, `¿`, or `??`. The `#`/`^` hits in the PDF are line numbers and hat accents.
- DOCX tracked changes and comments: 0 `w:ins`, 0 `w:del`, 0 comment references, 0 `w:comment` elements in all three DOCX; no `w:author`; core.xml has empty creator, title and keywords; custom.xml is empty.
- Vietnamese prose in the manuscript, supplement, cover letter, figures and scripts.zip: only proper names (Mây, Hải Dương, Giẽ, Phương Độ, Công ty ...) occur. (Vietnamese prose does occur in non-package files of the folder, see B2.)
- Credentials, e-mail addresses, Google Drive IDs, `__pycache__`, `.pyc`, `.DS_Store`, `.git*` in scripts.zip: none. Data or labels of the Thái Bình and Lang Am bridges: none found (`thai.?binh`, `lang.?am`, `láng` return nothing; the three data CSV files are Mây Bridge only).
- Figures: no debug text, file names, stray panel letters, overlapping legends over data, or British spellings in any of the 25 PNG files; fonts are consistent (one sans family) apart from the minor items below.
- Chatty AI vocabulary ("delve", "crucial", "pivotal", "notably", "it is worth noting", "in summary", "let us", "shed light", "leverage", "comprehensive", "robust", "novel" etc.) in the three sources: none in author prose. Hits are only "robust" and "novel" inside reference titles or the phrase "the robust choice" (see P3), and ordinary uses of "clearly". No em dashes. No emoji.
- Spelling: American throughout the prose ("fiber", "normalized", "analyze"); "regularised" appears only inside a reference title (OBrien et al., 2009), which is correct as published.

## Findings

### Blocking

**B1. Mismatched delimiters in equations of the PDF (DOCX is fine).**
- File and location: `word/Manuscript_ASE.pdf`, p. 11 (printed lines 229-237), Eq. (13) and two inline formulas; the same renderer is used for `Supplementary_Material_ASE.pdf`.
- Quote (as rendered): Eq. (13) is drawn as a large left square bracket "[" closed by a thin round ")" (`C_m(α,κ) = 1/α [ C_∞ + (C_0−C_∞)/(1+κ/k_g) )`); line 233 reads `B_m = | ∂ ln C_m / ∂ ln κ )` (right bar drawn as ")"); line 237 reads `... / [ 3β²(β k̂ + 3β + 2γ) ) , which reduces to` (closing "]" drawn as ")").
- Why: a reviewer opening the PDF sees visibly broken equations. The DOCX OMML is correct (`m:begChr "["`, `m:endChr "]"`, and `|`...`|`), so the defect is LibreOffice's rendering of stretchy (`<m:grow/>`) delimiters, but the PDF is what reviewers read first. The same defect can affect any grown "[ ]", "| |" and "( )" in the supplement (for example the nested brackets of Eq. (S2) and the denominators of S2).
- Minimal fix: in `word/postprocess.py` strip `<m:grow/>` from every `<m:dPr>` (so delimiters stay at text size), or rewrite Eq. (13), the `B_m` and `M_main` expressions without `\Big`/`|...|` (for example `\kappa\mapsto` with `\bigl[`...`\bigr]` removed and `\lvert` replaced by `\mathrm{abs}`), rebuild with `build_docx.sh --pdf`, and re-inspect every page that carries an equation; or export the PDF from Word.

**B2. Internal, Vietnamese-language and process files sit inside the package folder `manuscript/ase`.** Blocking if the folder (rather than the six built files, the figures and the zip) is uploaded or zipped as is.
- Files: `submission_checklist.md`; `figure_map.md`; `word/build/manuscript_build.md`, `word/build/supplementary_build.md`, `word/build/reference.docx`; `word/build_docx.sh`, `eqnum.lua`, `make_reference.py`, `postprocess.py`, `prep_md.py`, `prep_supp.py`; `tools/harvard.py`; `data_release/`.
- Quotes: `submission_checklist.md` is written in Vietnamese ("Gói nộp Advances in Structural Engineering (Sage Track)", "thầy giữ 'viết đủ'", "Cổng 4 (20/10): vòng 1 cả 4 BTV 'sửa rồi gửi'"), and cites "Hostile audit 19/10: `docs/editors_v4/hostile_audit/`", "Quy tắc V.1", "đọc mù chuẩn mực 18 lượt", "kiem_khoa", "v4.4", "đã gỡ cầu Thái Bình, mã Drive, [NEED VALUE], wp7b_checks.py" and a local path `docs/editors_v4/`. `figure_map.md` maps "ASE" numbers to "v4"/"v4.4" figure files. `word/prep_md.py` line 1: "Prepare manuscript.md for pandoc (Quy tac viet chung V.1, V.1.1)".
- Why: it exposes the editorial process, internal reviewer/editor codes and role names, the fact that the Thái Bình bridge data was removed, the AI-assisted "blind-read" rounds, and the pandoc/LibreOffice toolchain. Several of these files are Vietnamese prose, which is itself a stated defect class.
- Minimal fix: upload only `word/Manuscript_ASE.docx|pdf`, `Supplementary_Material_ASE.docx|pdf`, `Cover_Letter_ASE.docx`, `figures/Fig1-7*.png`, `GraphicalAbstract.png` and `word/scripts.zip`; do not zip or share the folder. Keep the rest in the repository only.

### Should fix

**S1. Absolute path in a log inside scripts.zip.**
- File: `code/fieldplan/results/fieldplan_compute.log`, last line (line 120).
- Quote: `figures written to /home/user/SHM-Paper1-1D/code/fieldplan/figures`
- Why: reveals the user name, the sandbox path and the repository name (all other logs were sanitized to `<repository>`, e.g. `verify_general.log:929`, so this one is a miss).
- Fix: replace with `<repository>/code/fieldplan/figures` (or `figures written to code/fieldplan/figures`) and rebuild the zip.

**S2. Editorial/process language and internal version labels in code comments and README inside scripts.zip.**
- `code/theory2/ident_static.py:99`: `# reproduce WP3 / editor numbers` (mentions an "editor"; internal work-package code).
- `code/supplementary/beam_theory.py:21-27`: "equation numbers follow the article (an earlier version used Eq. (6), (11), (12), (13)-(15) of an older draft)"; "(an earlier version used scipy.integrate.simpson ...)".
- `code/supplementary/README.md` lines 48 and 96: "given in the main text as Table 4 in earlier versions" and "Table 4 of earlier versions"; folder names `code/v3`, `code/v4` and file prefix `v4_` in README table rows (lines 14-15, 23, 32-36, 63-66, 94).
- `code/analysis/wp3_*.py`, `wp4_dynamic_records.py`, `wp7b_peps.py`, `wp7b_peps_2506.log`, `wp9_truckweight_check.py`: internal work-package codes (and a stray date-like suffix "2506") appear in file names, in the README and in `run_all.sh`.
- `code/v4/graphical_abstract.py:1`: "Graphical abstract for the ASE submission"; `code/v4/graphical_abstract.py` and `fig1_beams.py:9` point to `manuscript/ase/figures` and `manuscript/v4/figures`; `code/analysis/schm_figures.py:17-18` writes to `manuscript/schm/figures` (an earlier target journal's folder); `code/v4/num_diff.py:1`: "Compare the numeric tokens of two manuscript versions" (a manuscript-editing tool, not part of the analysis).
- `code/analysis/wp3_sections.py:8-9`: "load-rating report of the Mây Bridge main girder (supplied by the consultancy, not public)".
- Why: reveals version history, an earlier journal target, internal editorial vocabulary, and the non-public provenance of the input report, which the manuscript says the authors are permitted to publish in processed form.
- Fix (minimal): reword the three comments (drop "editor", "older draft", "earlier version"), rename or relabel `v3`/`v4`/`wp*` in README only if renaming files is too risky (README can say "offset-bias numbers", "figure scripts"), delete `num_diff.py` and `schm_figures.py`'s journal path, and say "report supplied by the bridge owner's consultant" instead of "not public".

**S3. Unverifiable process claim in the supplement.**
- File: `supplementary_material.md`, S11, 5th sentence.
- Quote: "Every equation and numerical output was checked independently against an analytical, finite element or convergence-based route."
- Why: reads as a tool-produced verification assertion; "every" cannot be demonstrated to a reader and the sentence belongs to the author's process, not to the paper.
- Fix: replace with a checkable statement, e.g. "The closed forms agree with finite element evaluations in 981 checks (Section S3)", or delete.

**S4. Data-availability wording is inconsistent between the three documents and the archive.**
- `cover_letter_ASE.md`: "the derived data behind every figure and table, and all analysis scripts ... are provided as Supplementary Material."
- `manuscript.md`, Data availability: "...the records behind Figs. S16 and S17 are not." The archive README ("What is not here") confirms that the Giẽ and Phương Độ records and the laboratory raw records are absent, yet `code/supplementary/logs/analysis/wp4.log` prints per-sample statistics of those events.
- Why: a statement of completeness that the archive contradicts; a hostile reader will test it.
- Fix: in the cover letter add the Figs. S16-S17 exception ("except the raw dynamic records behind Figs. S16 and S17 and the raw laboratory records").

**S5. DOCX metadata describes a document that is not this one.**
- Files: `docProps/app.xml` of all three DOCX (including the 29-page-equivalent manuscript and supplement).
- Quote: `<Application>Microsoft Word 12.0.0</Application>`, `<Words>83</Words>`, `<Pages>1</Pages>`, `<Template>Normal.dotm</Template>`, `<TotalTime>6</TotalTime>` (identical in the manuscript, supplement and cover letter).
- Why: it is the stale pandoc reference-document template; the word and page counts and the application are false, and a Sage system that reads them will show 83 words. The PDFs carry `Creator: Writer`, `Producer: LibreOffice 24.2` and no Title or Author.
- Fix: in `postprocess.py` delete `docProps/app.xml` content other than `<Application>` (or write true Words/Pages), and set `dc:title` in core.xml and the PDF title (for example through `--convert-to 'pdf:writer_pdf_Export:{"DocumentTitle"...}'`); leave author empty. Do not add personal data.

**S6. Repetitive contrastive construction ("X, not Y") used as the paper's stock move.**
- Quotes: manuscript.md line 29 "the contribution is a set of design criteria built on them, not a new weighing algorithm"; line 257 "The contribution is thus a set of design criteria for choosing channels and locations, not a new weighing method"; cover letter "the contributions are the criteria built on them"; line 148 "checks the model and the algorithm, not performance under moving traffic"; line 199 "scenarios, not an estimate and a correction"; line 221 "restraint by the haunches, not cancellation"; line 243 "global bending, not for deck-soffit gauges"; line 128 "common-mode ... not merely in vehicle-free periods"; supplement S3/S7/S10: "restraint, not cancellation" (twice), "indicative, not an evaluation according to ... GUM", "a simplified alternative to influence-line BWIM, not a competitor", "the table compares the order of the two estimators, not magnitudes".
- Why: 15 occurrences of the same rhetorical shape in about 19 000 words, three of them restating the same claim (introduction, conclusion, cover letter). It reads as formulaic.
- Fix: keep the two that carry scope (line 29 and the Section 3 sentence), recast the others as positive statements, and delete the second restatement in the conclusions.

### Minor

**P1. Empty signposting.** `manuscript.md` abstract: "The paper gives three main results. First, ... Second, ... Third, ..." and Section 7: "The main results are as follows." followed by a numbered list that repeats the abstract almost word for word (the 6.6 / 1.5 / 2.4 / 1.1 numbers occur in the abstract, Section 5.2, Section 7, the cover letter). Fix: delete "The main results are as follows." and cut the numbers from the conclusions to one occurrence.

**P2. Repeated sentence openings.** Section 4.2: "For the gauge average, return trips ...", "For the gauge average, the two runs ..." and in S7 "For the gauge average the lane-B constant ..." (three adjacent openings); manuscript.md has 21 paragraphs or sentences beginning "The/This/These" at line start and about 10 beginning "Each/Both/Neither/Every/No". Fix: vary the three "For the gauge average" openings (for example "Averaged over gauges, ...").

**P3. Mild evaluative wording.** "a single deflection gauge belongs at mid main span" (abstract, line 15); "the robust choice" (Section 5.3, line 225); "clearly resolved" and "clearly different weights" (lines 166, 239, 243, 257). Fix: "is best placed at"; "the better-conditioned choice"; "resolved" and "different" without the adverb.

**P4. Dense punctuation.** manuscript.md has about 100 semicolons and 185 colons; several sentences chain four clauses with semicolons (Section 4.2 first paragraph, Section 6 first paragraph). Not an artifact in itself, but it adds to the formulaic reading; split the longest chains.

**P5. Figure items (all minor).**
- `Fig4_norbwim_crossings.png`: legend values use a hyphen-minus and no spaces ("∫εdx=-67"), whereas other figures use true minus signs; the legend omits the unit (caption gives µε m).
- `FigS15_caumay_alpha_k_map.png`: both the open circle and the filled dot are labelled "A" while the caption says "A" and "A′"; the "f1=1.4" contour label is crossed by its own line; axis label "α = EI_eff/EI_design" uses a mathtext italic subscript that differs from the roman subscripts used elsewhere ("EI_mid", "EI_ref"). Fix: relabel the dot "A′" and use `\mathrm{eff}`/`\mathrm{design}`.
- `FigS13_veb_synthetic.png`: y label of panel (b) "∫εdx/GVW" lacks the unit given in (a) ("µε m/t").
- `FigS17_giecuc_phuongdo_lowpass.png`: panel annotations "I_LP/I = 1.0; net/abs = 0.0" have inconsistent precision with the other rows (0.9999, 0.001) and I_LP, net/abs are not defined in the caption.
- `GraphicalAbstract.png`: the beam schematics use a much smaller font than the other two panels and the third panel keeps its own small lower-case title ("misfit ratio of Mây Bridge gauges N8 and N7") directly under the blue heading, so two titles stack. Fix: enlarge the left panel labels, drop the inner title.
- `Fig6_caumay_channels.png`: the top labels "mid side span" and "N8 0.4L" nearly touch; shift one label.

**P6. British forms in scripts.zip (not in the article).** `README.md` "200 000 realisations" (s04 row), `code/theory2/ident_core.py:102` "discretisation"; the article is American throughout (Rule V.1), so use "realizations", "discretization".

**P7. Stale and unreferenced figure copies in scripts.zip.** `code/norbwim/figures/fig2_invariance.*`, `fig3_slm.*`, `fig4_speed.*`, `fig5_lane_superposition.*` and `code/theory2/figures/ident_theory_closedform.png` etc. are older-numbered outputs not used by any article figure (the README maps `v4_*` files instead); duplicate logs sit in both `code/analysis/logs` and `code/supplementary/logs/analysis`. Fix: delete the unreferenced figure files, or say in the README that they are intermediate outputs.

**P8. Archive date versus article date.** `scripts.zip` was built at 10:52 on 21 Oct; manuscript.md, supplementary files and all built files at 12:05-12:06 the same day. Not an artifact, but confirm that no number changed after 10:52 (run the checker used for the `kiem_khoa` step) before submission.

## Summary by severity

- Blocking (2): B1 mismatched equation delimiters in the PDF (Eq. 13, B_m line 233, M_main line 237, and possibly in the supplement); B2 Vietnamese-language and internal process files (submission_checklist.md, figure_map.md, word/build*, tools/, build scripts) in the package folder, blocking if the folder is shared as is.
- Should fix (6): S1 absolute path /home/user/... in fieldplan_compute.log; S2 "editor", "older draft", "earlier versions", v3/v4/wp*/schm labels and a "not public" provenance note in the code and README of scripts.zip; S3 "Every equation and numerical output was checked independently" in S11; S4 data-availability inconsistency (cover letter against manuscript and archive); S5 stale DOCX app.xml (Word 12, 83 words) and empty PDF title; S6 repeated "X, not Y" construction (15 times).
- Minor (8): P1 empty signposting; P2 repeated openings; P3 mild evaluative wording; P4 punctuation density; P5 figure details (Fig. 4, S13, S15, S17, graphical abstract, Fig. 6); P6 British spellings in the zip; P7 stale figure copies in the zip; P8 zip older than the final text.
