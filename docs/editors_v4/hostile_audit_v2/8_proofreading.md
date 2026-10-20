# Hostile audit v2 — Role 8: proofreading (manuscript, Supplementary, cover letter, built PDFs)

Scope: line-by-line read of `manuscript/ase/manuscript.md`, `supplementary_material.md` and `cover_letter_ASE.md`, plus the built `word/Manuscript_ASE.pdf`, `Supplementary_Material_ASE.pdf` and `Cover_Letter_ASE.pdf`. I extracted the PDFs with `pdftotext -layout`, rendered them to PNG and inspected them visually, and checked the OMML in `Manuscript_ASE.docx`. The PDFs are newer than the .md sources (11:22:24 against 11:22:15), so they reflect the current text. No file was edited.

Checked and found clean (no finding):
- **Spelling (American English):** no British spellings. The one exception is "regularised", which is part of the original title of OBrien et al. (2009) and should stay.
- **En dashes, minus signs and spacing:** every numeric range uses an en dash and every negative number in text uses U+2212. Number–unit spacing and the SI thin-space grouping (16 530, 10 000, 36 057) are consistent. The micro sign is consistently U+00B5 (µε, µrad).
- **Abbreviations at sentence start:** no sentence starts with "Fig." or "Eq."; the text uses "Equation (2)", "Figure 6" and "Figures S1 and S2" there.
- **Citations against references:** every citation has a reference entry, and every reference is cited.
- **Cross-references:** I checked every Eq./Fig./Table/Section reference in all three documents for correct targets; the only wrong one is finding S1.
- **Closed-form numbers:** I recomputed the closed-form values in Table 1 and Eqs. (S1)/(S2): 1.4574, 0.4215, 1.6180, 2.3028, 1.8794, 2.6691, 1.7006, √(3/2) and 0.276. I also recomputed the lab constant 61.54 mm²/N, the blind lab span 3644 mm, the Table S4 percentages, the BPM/SLM ratio 1.0049, the Mây means (5.55 and 15.43 mm), the 2.05 mm range (13 %), the mean truck weight 25.06 t, the Table S16 distances from T8, κ for calibration B (1.68 × 10⁸), the 2.3× ratio in Table 4, κ/k_g = 0.63, the 167 µrad pier rotation (ident_fisher.log) and α* = 1.07 at κ = 2.75 × 10⁷ (ident_fisher.log). All agree with the text.

---

## Blocking

### B1. Built PDFs: several equations and symbols are garbled (LibreOffice rendering of the OMML)
The OMML in `Manuscript_ASE.docx` is correct: the A⁺ superscript is `<m:sSup>…<m:t>+</m:t>`, |·| is `<m:d>` with "|" delimiters, and M̄ is `<m:acc>` with chr U+203E. The PDF exported from it, however, shows visibly broken mathematics. If this PDF is uploaded as the review PDF or as the Supplementary file, readers see wrong equations.

**Manuscript_ASE.pdf**
- **Eq. (9), PDF p. 8, line 174:** the equation breaks apart. It renders as "R = C / (A⁺¿ = 1 − |A⁻| / A⁺, ¿)": the "= 1 − |A⁻|/A⁺" part falls into the denominator of the first fraction, and inverted question marks appear. It should read R = C/A⁺ = 1 − |A⁻|/A⁺.
- **Lines 175–176:** "positive part A⁺¿¿" and "(for C < 0, A⁺¿¿ and A⁻ change roles)".
- **Principal-symbols table, p. 3:** the B_m entry reads "¿∂ln C_m/∂ln κ∨¿", printed in red. It should be |∂ln C_m/∂ln κ|.
- **Fig. 2 caption, line 143:** "optimum ξ^¿(β)"; it should be ξ*(β).
- **Fig. 7 caption, lines 375–376:** "α^¿(κ)" appears twice; it should be α*(κ).
- **M̄ is rendered as M with an acute accent ("Ḿ") throughout:**
  - lines 116–119 (Ḿ = −8M/(q₀L²), Ḿ_l, Ḿ_r);
  - Eq. (7);
  - line 229 (Ḿ_main).
  It must be an overbar: the symbol is defined as the normalized end moment M̄.
- **Upright text in math loses its upright style:** "Var" in Eqs. (11)–(12) and line 199 ("1/Var"), and subscripts such as tot, ref, mid, side, main, crit, 2span and 3span, are set in italic. The docx marks them `m:sty p`.

**Supplementary_Material_ASE.pdf**
- **Table S1:** the A⁺ entry renders as "A +¿ ¿"; the B_m entry renders as "¿∂ln C_m/∂ln κ∨¿"; the R entry renders as "C / A^{+¿¿}".
- **Eq. (S1):** "ξ^¿ = (1+√33)/16".
- **Table S2:** the caption and the column heads "ξ^¿" and "N_w at ξ^¿".
- **S8 "Frequencies" paragraph:** "α^¿ = 1.07".
- **Fig. S15 caption:** "best static fit α^¿(κ)".
- **S3 paragraph and Eq. list:** Ḿ_l, Ḿ_r and Ḿ_main.

**Fix.** Regenerate the PDFs from Word or with a renderer that handles these OMML constructs, rather than LibreOffice. Alternatively, change the OMML that `postprocess.py` writes:
- Write the superscript "+" and "*" as U+002B and U+2217 inside `m:t` with `m:sty p`, or use `\ast`.
- Use `<m:bar><m:barPr><m:pos m:val="top"/>` (or chr U+0305) for M̄.
- Write |·| as `m:d` with U+2223 or U+007C and `m:grow` in inline runs. Pandoc's `\lvert…\rvert` becomes bare "|" runs: the B_m entry is plain `<m:r>|</m:r>` runs.

After regenerating, check every page visually. Grep for "¿" in `pdftotext` output: it should be zero.

---

## Should-fix

### S1. Wrong cross-reference: Section 5.1, para. 1 (manuscript.md l. 193; PDF l. 337)
"…with means of 5.55 mm at N8 and 15.43 mm at N7 (Supplementary Tables S11, S12 and S14; axle positions in Table S16)."

Table S14 lists vertical natural frequencies, which the sentence does not mention; the trucks are in Table S11 and the readings in Table S12. **Fix:** "(Supplementary Tables S11 and S12; axle positions in Table S16)". If frequencies are meant, say so explicitly and cite S14 there.

### S2. Circular and inconsistent reference for the 24.8 % noise figure: Section 5.3 para. 3 (l. 229) against Supplementary S4 (last sentence)
- The main text says: "Under the assumed noise model of Supplementary Section S4 (calibration A), the standard deviation of the load falls from 24.8 % with N7 alone…".
- S4 says: "…22.5 % for a 200 m record under the assumptions of Section 5.3 (ρ = 0.9, calibration A), against 24.8 % for the 220 m record."

Each points to the other for the assumptions. The main text never states that the 24.8 % belongs to L_tot = 220 m, whereas Section 6 and Table S17 use L_tot = 200 m for the same girder. **Fix:**
- In 5.3, write "…(calibration A, ρ = 0.9, σ = 0.01 mm, δ₀ = 0.1 mm, L_tot = 220 m; Supplementary Section S4)…".
- In S4, write "under the noise model stated above", not "the assumptions of Section 5.3".

### S3. Cover letter, para. 6: "It is just under 12,000 word-equivalents with 7 figures and 5 tables"
The manuscript has four numbered tables (Tables 1–4) plus the unnumbered "Principal symbols" table. The editor will count four. **Fix:** "7 figures and 4 tables (plus a table of principal symbols)", or number the symbols table.

### S4. Cover letter PDF: address and signature blocks stretched by justification (Cover_Letter_ASE.pdf p. 1–2)
The forced line breaks in justified paragraphs spread single words across the full line:
- "The                Editors-in-Chief"
- "Advances      in      Structural      Engineering"
- "Thai-Son      Vu      (corresponding      author)"
- "55   Giai   Phong,   Bach   Mai   ward, …"

**Fix:** set these paragraphs left-aligned, or make each line its own paragraph, in the cover-letter build.

### S5. Number–unit pairs broken across lines in the PDF (no non-breaking space)
Examples in Manuscript_ASE.pdf:
- l. 207–208 "within 0.6 / %"
- l. 252–253 "with 95 / % confidence"
- l. 245–246 "125.08 / N"
- l. 311–312 "(20.3 / %)"
- l. 359–360 "τ = 5.3 / %)"
- Fig. 5 caption "±10 / %"
- l. 329–330 "a 55 / + 90 + 55 m"

The cover letter has the same "55 / + 90 + 55 m" break in item 3. **Fix:** use U+00A0 (or U+202F) between number and unit or %, and within "55 + 90 + 55 m", in the prep script.

### S6. Inconsistent typesetting of "symbol = value" in running text
Some equalities are typeset as math, which gives no spaces in the PDF: "α=1", "α=0.716", "L_v=44 m", "N_M=0.048". Others are set as symbol plus text: "τ = 5.3 %", "α = 0.51–1.15", "N_M = 0.163–0.212", "ρ = 0.9". The two forms sit side by side in the same paragraph (5.1–5.3 and Table 3 caption, PDF pp. 15–18), with different fonts and spacing. **Fix:** use one convention throughout, either everything inside `$…$` or the spacing applied consistently.

---

## Minor

### m1. Nomenclature, Table S1: incomplete and out of order
**Missing symbols:**
- q₀ (used in Eqs. (2), (3) and (5)–(7) and in the definition of M̄);
- A⁻;
- E;
- L₁, L₂, L_side, L_main;
- L_v;
- M_B;
- ν (Section S2);
- ξ₀, ζ₀, ξ*;
- α*;
- N_ε (Fig. 6c);
- C₇, C₈;
- θ₆, θ₇;
- M̄_main.

**Out of order:** r² sits between μ and ρ, among the Greek symbols. **Fix:** add the missing rows and move r² next to r₈₇.

### m2. Hyphenation of the compound modifier "main-text"
The Supplementary uses "main-text Fig. 2b", "main-text Fig. 5a" and "main-text Fig. 6c", but Table S10, row 3, reads "(main text Table 2)". **Fix:** write "(main-text Table 2)" there.

### m3. "Supplementary" prefix used inconsistently in the main text
Line 193 has "(Supplementary Tables S11, S12 and S14; axle positions in Table S16)", where the second reference drops the prefix. Line 164 has "(Tables S6 and S7, Fig. S9)" after "Supplementary Section S7". Everywhere else the main text writes "Supplementary Table/Section". **Fix:** keep the prefix on the first item of each parenthesis, or use it everywhere.

### m4. Conclusion 1: mixed forms for parallel blind ratios
"λ = (3+√33)/6 for a mid-span gauge … and β = 1.7006 for a mid side-span gauge". One ratio is given in closed form and the other as a decimal; the text body (Section 2.2) gives both as decimals. **Fix:** "λ = 1.4574" here, or give both forms for both.

### m5. Conclusion 2, PDF l. 471–472: orphaned period
The final "." after the inline math "cM_q/EI" wraps to a line of its own. **Fix:** keep the period inside the math, or use a non-breaking join.

### m6. Cover letter wording
- "Yours sincerely," is British usage; American usage is "Sincerely,".
- The capitalization differs between the subject line, "Submission of an original research article", and the next paragraph, "as an Original Research Article". Use one form; the journal's article-type name is "Original Research Article".
- "on behalf of Quoc-Bao Nguyen" after the signature block is unusual. "on behalf of all authors" is the conventional form.

### m7. Statements heading
"### Declaration of conflicting interest". Sage's standard heading is "Declaration of conflicting interests" (plural). **Fix:** use the plural.

### m8. Reference style consistency
AASHTO (2024) carries "10th ed." and Frýba (1999) "3rd ed.", but Ghali et al. (2017), *Structural Analysis: A Unified Classical and Matrix Approach*, has no edition. It is the 7th edition. **Fix:** add "7th ed.".

### m9. Figure-internal typography
- **Fig. 4 legends:** they use a hyphen-minus ("∫εdx=-67", "-157", …) and give no unit; the caption supplies "µε m". Use "−" and add the unit or "(µε m)" to the legend title.
- **Fig. 5 y-axis:** reads "(95% CI)", while the text uses "95 %".
- **Graphical abstract, middle panel:** it keeps the "(a) symmetric beam, uniform EI" panel label from Fig. 2. Remove the "(a)".

### m10. Table S11: inconsistent decimals
The gross-weight column mixes "25", "25.3" and "25.66", and the track column mixes "1.9" and "1.85". **Fix:** use a uniform number of decimals (25.00, 25.30, 25.66; 1.90, 1.85), or state that the values are as reported.

### m11. Layout of Manuscript_ASE.pdf
About 40 % of p. 15 is empty because Fig. 6 is pushed to p. 16. Because of the wrapped header cells, the principal-symbols table splits across pp. 3–4 with a single row ("β … P_δ") on p. 4. **Fix:** allow the table to stay together, or shorten "integral constant of a channel, Eq. (2)" so it does not wrap. This is cosmetic.

---

## Count per class
- Blocking: **1** (B1: garbled equations and symbols in the built PDFs. It covers Eq. (9), the B_m and A⁺ symbols, ξ*, α* and M̄ in both the manuscript and Supplementary PDFs; the docx OMML itself is correct.)
- Should-fix: **6** (S1–S6)
- Minor: **11** (m1–m11)
