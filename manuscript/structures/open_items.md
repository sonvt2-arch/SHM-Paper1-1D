# Open items for the authors

## A. Missing values ([NEED VALUE] in the files)

| # | Where | What is needed |
|---|---|---|
| A1 | manuscript §4.1 | Weighbridge values of the Cầu Mây test trucks (report states only "about 25 t"). If available, recompute Table 6 with actual weights. |
| A2 | manuscript §6.6, §7.2 | Type A evaluation from the three repeated laboratory cycles: standard deviation of the deflection at each point, or of the integral. The rejection review (A3) noted that these readings exist; they are not in the repo. With them, replace the "A (bound)" rows of Table 9 by evaluated values. |
| A3 | manuscript §7.2 | Accuracy class (or calibration uncertainty) of the laboratory weights; Table 9 uses 0.1 % for reference weighing. |
| A4 | Data availability | Owner/consultant of the Cầu Mây acceptance-test data (Hai Duong PMU; HUCE consultancy as tester per `data/bridges/cau-may/INVENTORY.md`) and a permission statement; same for the Gie Cuc I and Phuong Do records. |
| A5 | Acknowledgements | Whether to thank the Cầu Mây owner and testing consultant. |
| A6 | Ref. [44] Sohn 2007, ref. [45] Cross et al. 2013 | Exact titles and DOIs, copied from the JCSHM reference list (the text export in the repo is truncated after ref. 31; `docs/reference_check.md` confirms journal/volume/pages but does not print titles/DOIs). Titles were left blank rather than supplied from memory. |
| A7 | Ref. [47] AASHTO LRFD | Confirm edition and year (10th ed., 2024 not verified). |
| A8 | Ref. [6] Fattorini 2023 | Check exact title wording (quotation marks in Crossref). |
| A9 | Ref. [10] FHWA | Confirm the intended document; the original "FHWA (2009) … costs of weigh stations" was not found. Entry replaced by FHWA-PL-00-029 (2000). If the cost statement came from another source, replace or delete. |
| A10 | Cover letter | Date; suggested reviewers. |
| A11 | Highlights/graphical abstract | *Structures* recommends a graphical abstract; none prepared. |

## B. Decisions for the authors

| # | Decision | Writer's default in this draft |
|---|---|---|
| B1 | Title wording | "Total-load observability of continuous girder bridges from a single deflection channel: closed-form blind configurations, laboratory verification and application to an in-service box-girder bridge" (23 words). A shorter alternative: "Single-channel total-load observability of continuous girder bridges: closed-form blind configurations and application to an in-service box girder". |
| B2 | Threshold for the cancellation ratio $R_m = C_m/A^+$ | No numerical threshold is proposed; $R_m$ is used for ranking (§2.4, §7.1 step 3). WP3 left this to WP2. If a threshold is wanted, it must be derived (e.g. from the zero-offset sensitivity) before submission. |
| B3 | Notation $\rho_{EI}$ | Unified as adjacent-span over instrumented-span rigidity for both two- and three-span beams. This matches the old nomenclature ($\rho_{EI} = EI_2/EI_1$) and Eq. (11a) of the old manuscript as written ($\mu = (1+\rho_L^3/\rho_{EI})/(1+\rho_L/\rho_{EI})$). The warning in `docs/wp2_three_span_theory.md` (that Eq. (11a) uses $EI_1/EI_2$) appears to be a misreading; please confirm. |
| B4 | Statement "beyond $2\cos(\pi/9)$" | WP2 calls the side span "blind/unobservable" there. The draft says instead that no side-span position gives a positive constant and the response is dominated by the main span, because $C_m$ is negative but non-zero (formally usable, as for two spans beyond the blind ratio). Confirm the wording. |
| B5 | WP2 haunch study ($I \propto h^n$, Thái Bình parametric) | Not used. The Cầu Mây analysis uses the WP3 model with the designer's section values, which supersedes it. Could go to Supplementary Material. |
| B6 | Computational-implementation paragraph | Kept, including the authors' sentence "Generative artificial intelligence was used as an assistance tool during code development and debugging." The formal AI declaration is kept verbatim from the JCSHM version. An earlier diagnosis judged an in-methods AI mention unnecessary for the ES version; delete the in-methods sentence if preferred (the declaration covers it). |
| B7 | References dropped from the old list | Li et al. 2023 (breathing cracks), Hoang et al. 2017, Katori 2018, Yang et al. 2004 (vehicle scanning), Feng & Feng 2018 (vision), Nguyen et al. 2020 (Bo Nghi damage). Reinstate any the authors consider necessary; the list now has 47 entries (rule VII.7 floor 40). |
| B8 | Title-only / excerpt-only citations | [17] He 2019 (title), [35] Huang & Lu 2025 (excerpt), [34] Döring 2023 (excerpt), [38] Zhou 2025 (title), [39] Zhang 2026 (title), [40] Shen 2026 (abstract). Each is cited only for what its title/abstract states. Read the full texts of [34], [37], [38], [39] before submission (`docs/novelty_matrix.md` §5). |
| B9 | Unlocated "Integral Mean of Strain" paper (Measurement 2025) | Not cited. If the authors locate it, add it in §1 and check whether it treats continuous beams or sign-changing influence lines. |
| B10 | Ojio & Yamada 2002 | Cited only through Cardini & DeWolf [27], because the original was not found. |
| B11 | Prior desk rejections | Not mentioned in the cover letter. |
| B12 | Fig. 2 (two-span map) labels | Old Fig. 10 uses $\rho_{EI}$ as defined in the old manuscript; confirm the axis matches B3. |

## C. Recommended further work (not done, outside route A)

- Direct invariance test on the existing rig (fixed total load, varying spacing) and the blind-configuration test (spans 2500 + 3644 mm): §7.2. Decided against for this submission (`docs/02_ke_hoach_va_phan_vai.md` §6).
- Cầu Mây MIDAS model and pier dimensions, to replace the calibrated $k_\mathrm{FE}$ (`docs/03_thu_xin_so_lieu.md`).
- Thái Bình: cross-section drawings and truck assignment, then a decision whether to add it in a later paper.

## D. Checks done by the writer

- Main-text word count 8,071 (Introduction to end of Section 8; tables, table captions, display equations, headings, figure captions, appendices, declarations and references excluded; inline math counted as one word; script `wc_main.py` in the session scratchpad). Abstract 250 words. Highlights 5 bullets, 69–82 characters.
- Equations numbered sequentially (1)–(21), (A.1)–(A.2).
- Two-way number check: all 491 distinct numbers in the manuscript body traced (see `traceability.md`); key source facts (β_crit, near-blind edge, 2cos(π/9), Cầu Mây 0.181/82 %/fourteenfold, lab 1.19/0.70 %) present in the manuscript.
- Eq. (A.2) re-derived symbolically because the old text export was garbled; matches old Table 2.
- Decimal error of old §4.1 corrected to $(1.2596-1.9893)$ mm⁻¹; "one-, two- and three-axle" removed (single load = reference); laboratory loads described as statically positioned throughout.
