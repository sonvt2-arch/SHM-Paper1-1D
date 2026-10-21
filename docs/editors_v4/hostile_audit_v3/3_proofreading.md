# Hostile audit v3 – 3. Proofreading

## Scope and method

Files read in full, line by line: `manuscript/ase/manuscript.md` (431 lines), `supplementary_material.md` (443 lines), `cover_letter_ASE.md` (34 lines). Built PDFs (`word/Manuscript_ASE.pdf`, 29 pp.; `word/Supplementary_Material_ASE.pdf`, 29 pp.; `word/Cover_Letter_ASE.pdf`, 2 pp.) were extracted with `pdftotext -layout` and rendered with `pdftoppm` (80, 130 and 300 dpi zooms) into `/tmp/claude-0/-home-user-SHM-Paper1-1D/f082bf06-32d9-5afb-abb0-31b2feb90905/scratchpad/proof/`. Script checks: reference list against in-text citations (57 entries, both directions), British-spelling scan, hyphen-minus and en-dash scan, sentence-initial "Fig./Eq.", thousands separators, cross-references to every Eq./Fig./Table/Section/S-item, and recomputation of the repeated numbers (Abstract, Sections 1–7, Supplementary, cover letter).

Main-text line numbers below are `manuscript.md` source lines ("md L…") and, where the PDF is meant, PDF page/line ("PDF p. x, l. y").

Known decisions not reported: address without diacritics, "Matuso", θ6/θ7, "base model" in the Abstract.

## Checks with no finding

- No "¿", "�" or missing-equation glyphs in any of the three PDFs; all 14 numbered equations and Eqs. (S1)–(S2) are present.
- Reference list and citations match one-to-one (57/57); alphabetical order and Sage Harvard author/year form are consistent; Dang et al. (2023) and Vu et al. (2023) are cited exactly once each and listed correctly.
- American spelling throughout (only "regularised", which is in a cited title and correct to keep).
- No sentence begins with "Fig." or "Eq."; "Figure"/"Equation" are spelled out at sentence starts.
- Number–unit spacing (12 %, 0.1 mm, kN m/rad), en dashes for ranges, true minus signs, thin-space thousands separators for numbers with five or more digits (10 000, 12 000, 16 530, 36 057) are consistent.
- Figures 1–7, Tables 1–3, Figs. S1–S17 and Tables S1–S19 are all cited, numbering is continuous, and every pointer resolves to the right target (spot-checked all of them).
- Repeated numbers agree: 0.19–0.32 band (Abstract, §2.2, Table 1, Table S3, Conclusions); λ = 1.4574 = (3+√33)/6; 8.5 pp, 20.4 % vs 11.9 %; 12 %/27 % margins (§4.2, Table S7, Conclusions); 22–26 % (Table S7: 0.740–0.783); 0.79, 0.92; 6.6/1.5 and 2.4/1.1 (Abstract, §1, §5.2, Conclusions, Table S13, cover letter); 3.4/1.4 and 1.5/1.1 at τ = 4 and 3 %; B_m 0.51/0.12; 16–25 % and 41–271 % (recomputed from Table S17 constants); means 5.55 and 15.43 mm and 25.06 t (recomputed from Tables S11–S12); 2.05 mm ≈ 13 %; 1.0049 (= 1.0110/1.0061); 3644 mm = 2500 × 1.4574; 605 m; κ_B = 1.2 × 10⁸/0.716 = 1.68 × 10⁸; 14.0 and 0.59 (Table 3); 28 % below design.
- Laboratory, NOR-BWIM and Mây Bridge sections contain no broken sentences from the shortening edits other than those listed below.

## Findings

### Blocking

**B1. PDF (manuscript and supplement): every stretchy right-hand "]" and "|" renders as ")".** Confirmed at 300 dpi. Examples: Eq. (2) "y_m[q_0)" (PDF p. 4) and in the text l. 103, 105; "[0, L_p)" l. 100, which reads as a half-open interval; Eq. (13) "[C_∞ + …)" (p. 11); "|N_w) ≤ 0.10" l. 142; "|N_w) < 0.2" l. 148; "|N_M) < 0.2" l. 154, 156, 442; "|N) < 0.2" l. 163; "1/|C)" l. 171; Eq. (9) "|A⁻)"; "|C)" l. 213; "B_m = |∂ ln C_m/∂ ln κ)" l. 233; "M̄_main = …/[3β²(…))" l. 237; "|ln r_87) ≤ 2τ" l. 386. Supplement: M_B in S2 "/[8(…))", Eq. (S2) "cos[⅓ arccos(…))", main-span formula "8[…)" and "ν = …/[β²(…))", S3 "[0, L_p)" and "∫[g(u+s) − g(u+s′))", "|N_M) ≥ 0.39" (S8), checklist items "|N_M) < 0.2", "|N_w) < 0.2". The `\lvert…\rvert` in the symbol tables renders correctly. Problem: mismatched delimiters in the key equations. Fix: in the converter, make LibreOffice Math use matching right delimiters (or write `\lvert…\rvert`, `\left[…\right]` explicitly) and rebuild both PDFs.

**B2. Cover letter PDF p. 1 and p. 2: address and signature blocks are fully justified.** "The ……… Editors-in-Chief", "*Advances* … *in* … *Structural* … *Engineering*", "Thai-Son ……… Vu ……… (corresponding ……… author)" and "55 Giai Phong, Bach Mai ward, …" are stretched across the line width. Fix: left-align these lines (line breaks without justification).

**B3. manuscript.md §1, para 3, last two sentences (md L27; PDF p. 3, l. 70–73):** "…or shows how they shift with uncertain boundary conditions. Such criteria are needed to choose, before installation, the few channels…" followed by "This paper supplies such criteria." Problem: "Such criteria" has no antecedent, because no criteria have been mentioned (an orphan from the rewrite). Fix: "Criteria that locate these zeros are needed to choose…" (then "This paper supplies them.").

### Should fix

**S1. Manuscript PDF p. 3–4: the heading "Principal symbols (full list: Supplementary Table S1)" is alone at the foot of p. 3 and its table is on p. 4.** Fix: keep with next (page break before the heading).

**S2. Manuscript PDF p. 7–8: the Fig. 3 caption splits across pages.** "(a) Equal two-span beam;" is on p. 7 and "(b) symmetric three-span beam…" on p. 8. Fix: keep figure and caption together.

**S3. Supplement PDF p. 22–23: Table S13 breaks after its first data row** (τ = 3 %), and the header repeats on p. 23. Its unit cells also wrap badly ("(m²/k | N)", "9.1 × | 10⁻⁵–1.4 | × 10⁻⁴"). Fix: move the table to p. 23 or set it landscape/smaller, and keep the units unbroken.

**S4. Supplement PDF p. 23–24: the Table S15 footnotes ᵃ/ᵇ are separated from the table onto the next page.** Fix: keep the notes with the table.

**S5. Supplement PDF p. 26–27: Table S18 breaks after its first row.** Fix: start the table on p. 27.

**S6. Supplement Table S1, row ν (supp L70), against main §2.5 (md L142).** Table S1 has "ν | moment parameter of the main span…", but the main text calls M̄_main "the end-moment parameter" of the main span, and ν = 3(γ+β³)/[β²(2γ+3β)] = 1.5 M̄_main (pinned: ν = 1.2 against M̄ = 0.8 for equal spans). Problem: two "moment parameters" for one span differ by a factor of 1.5. Fix: "ν | deflection coefficient of the main span, ν = 1.5 M̄_main (Section S2)".

**S7. manuscript.md §6, para 2 (md L241; PDF p. 21, l. 451–455):** "Single-point influence-area weighing on this 200 m unit is therefore marginal even at the best location, and non-contact techniques, such as terrestrial laser scanning of bridge deflection (Vu et al., 2023), must establish their residual offset on site, because…" Problem: the sentence added for Vu et al. joins two unrelated claims under one "therefore". Fix: end the sentence after "location." and start "Non-contact techniques, such as …, must establish…".

**S8. Supplement S4, last sentence (supp L147):** "…under the assumptions of Section 5.3 (ρ = 0.9, calibration A)". Main §5.3 (md L229) states no ρ and instead points back to "the assumed noise model of Supplementary Section S4". Problem: circular pointer. Fix: "under the noise model above (σ = 0.01 mm, δ₀ = 0.1 mm, ρ = 0.9, calibration A)".

**S9. Supplement S6 (supp L157) against main §3 (md L150).** S6 gives the "measured-to-analytical integral ratio (1.010, 1.016 and 1.017…)", while §3 says "the ratio of the measured reference integral to its exact value" is 1.0049. Both are correct (1.010 is the trapezoidal-to-trapezoidal ratio; the trapezoidal rule is 0.500 % low), but a reader sees two different "ratios" for the single load. Fix: "measured-to-analytical integral ratio, both by the trapezoidal rule (1.010, …)".

**S10. Eq. (S2) and Table 1 inline fractions (supp PDF p. 4; manuscript PDF p. 8).** `\tfrac13`, `\tfrac25` and `\sqrt{10/3}` render as "√10/3 cos[1/3 arccos(2/5 √6/5)]" and Table 1 shows "ζ₀=1/2(1−√…)". "1/3 arccos" can be read as 1/(3 arccos). Fix: use stacked fractions (`\frac`) in Eq. (S2), or parenthesize "(1/3)".

**S11. manuscript.md §2.1, Eq. (2) and §4.1 (PDF p. 4, 12):** the source has `\mathrm{d}x`, `\mathrm{d}u`, `\int\varepsilon\,\mathrm{d}x`, but the PDF renders the differential d in italic. Fix: force an upright d in the converter (or accept italic d and also remove `\mathrm` from the source, for consistency).

### Minor

**M1. Abstract (md L15), §1 (i) (md L29) and cover letter item 1: "five channel types", but Table 1 has six rows.** End reaction and interior reaction are counted as one type. Fix: "five channel types (reactions counted once)" or merge the two reaction rows into "Reaction".

**M2. §1, contribution (ii) (md L29):** "The rule itself is not tested in the field". Fix: "has not been tested".

**M3. §1, last para (md L29):** "the public records check its assumptions and noise model". Problem: the noise model belongs to §2.4, not to "the identity". Fix: "its assumptions and the noise model of the estimators".

**M4. §4.2, para 3 (md L168):** "both observations make a spread of gauge factors an unlikely cause". Problem: the cause of what is left implicit. Fix: "…an unlikely cause of these differences".

**M5. §5.2, para 2 (md L201):** "the remaining misfit ratio of 4–9 %". Problem: the ratio is 1.039–1.092, not a percentage. Fix: "the remaining misfit of 4–9 %".

**M6. §4.3 (md L185):** "MAE 8.5 % in sample", and in the same subsection the GLS penalty is also "+8.5 percentage points". Two different 8.5s in one subsection invite confusion. Fix: no change needed, but "8.5 % of GVW in sample" would help.

**M7. Conclusions item 4 (md L254):** "(20.4 % against 11.9 %)" does not name the measure. Fix: "(MAE 20.4 % against 11.9 %)".

**M8. §6 (md L241) and Supp S10:** "The speed estimator alone can shift the weight…". Fix: "The choice of speed estimator alone…" (as in S10).

**M9. Figure citations:** Fig. 5b is cited before Fig. 5a (md L164); Fig. 7b is never cited in the main text (only in Supp S8). Fix: cite "Fig. 7b" in §5.2/§5.3 (e.g. with the Cramér–Rao sentence, md L231).

**M10. Main §5.3 (md L231):** the Cramér–Rao values 0.87 → 0.18 and the 167 µrad pier rotation point to Supplementary Section S8, which gives only 0.24 (frequencies) and 0.04 (at B). The same applies to "10.6 %" (md L229), which does not appear in S4. Fix: add the three numbers to S8/S4, or point to the script log.

**M11. Data availability (md L295):** "derived data (CSV and NumPy files)", against Supp S11 (supp L407) "provided as CSV files". Fix: make both say "CSV and NumPy files".

**M12. Supp S10 (supp L357):** "A crossing of the 200 m … unit, plus the wheelbase, takes 12.4 s at 60 km/h". (200 + 4.8–5.3 m)/16.67 m/s = 12.3 s. Fix: check the length used, or write "about 12 s".

**M13. Supp Table S11 decimals:** "25" and "25.3" against "25.66"; "1.9" against "1.85"; "3.7". Fix: use a uniform number of decimals (25.00, 1.90, 3.70 or as weighed).

**M14. Supp Table S17:** the 0.02 mm column has one decimal ("3.3–5.0 %"), the other columns are integers. Fix: harmonize.

**M15. "main text" hyphenation:** "main-text Fig. 5a/6c/Table" in most places, but "(main text Table 2)" in Table S10 (supp L259). Fix: "main-text Table 2".

**M16. Undefined abbreviations:** "HUCE consultancy" (Acknowledgements, Declaration) is never expanded; "SD" is used in S7 (supp L199) before it is defined in the Table S10 caption (it is defined in Table S1). Fix: "(HUCE: Hanoi University of Civil Engineering)"; "standard deviation (SD)" at the first use in S7.

**M17. Principal symbols table (md L39):** "α | effective-to-design girder rigidity" lacks "ratio" (Table S1 has "ratio of effective to design girder rigidity"). Fix: "effective-to-design girder rigidity ratio".

**M18. Non-breaking spaces (PDF):** "(Fig. | 1)" p. 5, l. 129–130; "Figure | 3" p. 7, l. 156–157; "( | |N_M|=μ)" p. 7, l. 155–156; "Eq. | (2)" in the symbol table; "(Fig. | 5a)" p. 13, l. 287–288; "a 55 | + 90 + 55 m" p. 15, l. 338–339 and cover letter p. 1; "( | β=1.636)" p. 15, l. 339–340; "(Q.- | B. Nguyen)" p. 23, l. 522–523; Fig. 1 caption line beginning ", adjacent span" (p. 6, l. 133). Fix: non-breaking spaces after "Fig."/"Eq." and inside "55 + 90 + 55 m", "Q.-B.", and no break before a comma or after "(".

**M19. Supp S2 (PDF p. 4–5):** ν renders in Times as "v" and is hard to tell from italic v. Fix: none required; optionally use another symbol.

**M20. Cover letter, signature:** "on behalf of Quoc-Bao Nguyen". Fix: "on behalf of both authors" (or "and Quoc-Bao Nguyen").

**M21. Yan et al. (2022) title:** "bridge weight-in-motion". Fix: verify against the publisher; keep if original (it is a cited title).

**M22. Inline math in tables (Table 1, Table 3) is set larger than the surrounding 10 pt table text** (PDF p. 8, 19). Fix: optional; reduce the equation font size in tables.
