# Blind readability assessment — manuscript v4

Reader profile: structural engineering / SHM, reading for Structural Control and Health Monitoring. Only the readability of the prose is judged here, not scientific merit. [NEED VALUE] placeholders and missing figures were ignored.

## Scores (0–10)

| # | Criterion | Score | Short reason |
|---|---|---|---|
| 1 | Abstract clarity | 4.5 | After one read I could not state the main message. The abstract holds about 20 numbers and uses undefined terms ("Möbius law", "deflection index (effective-rigidity normalisation)", $cM_q/EI$). It moves from theory to a negative field result to a case study without saying which one is the take-home point. |
| 2 | Introduction flow and motivation | 7.0 | The motivation and the gap ("None of these studies gives a criterion...") are clear, and the contribution list is good. Paragraphs 2–3 are citation catalogues, and there is a digression on transmissibility. |
| 3 | Signposting / structure | 7.5 | Each section opens by saying what it does; 4.5, the closing sentence of 5 and the closing sentence of 2 sum up. Sections 2.2–2.4 do not say up front what was found. |
| 4 | Sentence-level clarity | 6.0 | Sentences are mostly short and active. Recurring problems: ratio-of-ratio phrases, the overloaded label "N8/N7" (gauge vs span), an ambiguous "both", comma splices, and noun stacks such as "offset-equivalent load" and "side-span deflection index". |
| 5 | Information density | 4.0 | Sections 4.2, 4.3, 5.2, 5.3 and the abstract carry 8–15 numbers per paragraph, often with CIs, ranges and alternative normalisations side by side. The reader has to stop on nearly every sentence. |
| 6 | Terminology / notation consistency | 5.0 | "Indicator" alternates with "index". Several symbols are used without being defined or listed in the Nomenclature ($w_q$, $\rho_{EI}$, $N_R$, $N_\theta$, $N_V$, $T_\mathrm{cr}/T_1$, $f_1$, $S_\alpha$, $l$). Gauge prefixes change between days (ch vs st). Some acronyms are defined late or not at all (GVW, LOTO, GUM, T5/T7/T8). |
| 7 | Equations embedded in prose | 7.0 | Most equations have a lead-in and an interpretation; Eqs. (2), (3), (12), (15) are handled well. Eqs. (5)–(8) come in quick succession with little physical reading, and Eq. (16)'s $K$ appears without motivation. |
| 8 | Results presentation, tables/figures | 6.0 | Tables are referenced and captioned. Tables 3–5 are very dense (CIs in every cell, mixed CI levels, a reversed range "0.263 … 0.145"), and Table 4's "predicted sd" column is hard to read against the MAE columns. |
| 9 | Conclusions | 7.0 | They match the text and are numbered. Items 3–5 pack several findings and numbers each; item 3 mixes a design rule with a field failure. |

**Overall: 6.0 / 10.** The overall score gives extra weight to the abstract, density and terminology (criteria 1, 5, 6). Those decide whether an expert gets through the paper without re-reading, and they are where the text loses most. Sentence craft and structure are generally sound.

## Places re-read on the first pass

Abstract, sentences 2, 3 and the last one. Intro paragraph 3 (transmissibility). 2.2, the $(m_l,m_r)$ and $\mu$ definitions. 2.3, the paragraph on threshold equivalence. 2.4, "Independent offsets call for clustering..." 2.5, the first paragraph. 4.1, the day-1 channel description. 4.2, the first paragraph (90 % vs 95 % CIs). 4.3, the paragraph after Table 4. 5.1, "four trucks stood in side span N8". 5.2, all paragraphs. 5.3, the strain paragraph and the Cramér–Rao paragraph. Table 5.

## Ten hardest-to-read passages

1. **Abstract.** "That this area equals the response to a uniform unit load, and that channels can be combined by generalised least squares, is classical; this paper uses both to derive design criteria"
   *Why it is hard:* a long clausal subject delays the verb, and the paper's purpose arrives only after a semicolon.
   *Fix:* "Two classical facts underlie this work: ... We use them to derive ..."

2. **Abstract.** "a placement rule (sensors at the extremes of the uniform-load response, for strain of $cM_q/EI$); and a Möbius law for the effect of uncertain pier stiffness."
   *Why it is hard:* the parenthesis is garbled ("for strain of"), and it uses symbols and a law that the abstract never defines.
   *Fix:* Drop the symbols; say "a closed-form law for pier-stiffness uncertainty".

3. **Abstract.** "two static readings leave the side-span deflection index (effective-rigidity normalisation) between 0.14 and 0.42"
   *Why it is hard:* the index is undefined and the parenthesis is opaque, so the reader cannot judge whether 0.14–0.42 is good or bad.
   *Fix:* State the consequence: "the side-span gauge's constant remains undetermined by a factor of six."

4. **§4.1.** "Day 1 has 12 channels at 100 Hz: four stations, each with one gauge that shows axle spikes (the wheel-path gauges ch4, ch5, ch11, ch12), a partner gauge, and four gauges without axle spikes"
   *Why it is hard:* the list structure is ambiguous. It is unclear whether the "four gauges without spikes" belong to each station.
   *Fix:* "Each of four stations has three gauges: wheel-path, partner, no-spike."

5. **§5.2.** "The ratio $r_{87}$ of the measured-to-model ratios at N8 and N7 never reaches 1 (Fig. 9a)."
   *Why it is hard:* a ratio of ratios is given with no meaning attached, and the reader must reconstruct why 1 matters.
   *Fix:* Add: "r87 = 1 would mean one model fits both gauges exactly."

6. **§1.** "A transmissibility is a ratio of response spectra, and at zero frequency a ratio of spectra equals the ratio of the record integrals that the standard-load method uses; the present paper asks instead"
   *Why it is hard:* a technical digression in the literature review uses "standard-load method" before it is defined, then pivots mid-sentence.
   *Fix:* Cut it, or move it to Section 2.4 after SLM is defined.

7. **§4.3.** "so both estimators are significantly worse than the average, although the noise model predicted a per-crossing standard deviation of 12.7 % for GLS against 19.8 % for the average."
   *Why it is hard:* "both" points back to GLS and offset-immune, but the preceding clause names GLS and the average. There are also two kinds of percentages (MAE and sd).
   *Fix:* Write "GLS and the offset-immune estimator are both significantly worse ...".

8. **§5.2.** "the N8 index is 0.14–0.42 when normalised by the effective rigidity $\alpha EI_\mathrm{mid}$, and 0.12–0.82 with the design $EI_\mathrm{mid}$; the upper part of the latter range requires $\alpha \approx 0.5$."
   *Why it is hard:* two normalisations, two ranges and a conditional sit in one sentence, with no statement of which range the reader should keep.
   *Fix:* Give one normalisation in the text; move the other to Table 5.

9. **§5.3.** "The placement rule, however, ranks locations by $C_\varepsilon = cM_q/(EI\,q_0)$: with $c\propto h$, the gain $c/EI$ there is about one fifth of that at mid-span (Fig. 8c), so the choice depends on"
   *Why it is hard:* "there" is a vague referent (5–10 m from the piers). The sentence reverses the previous recommendation without warning.
   *Fix:* Open with "This ranking changes when the section gain is included:".

10. **§2.4.** "Independent offsets call for clustering at the maximum; correlated offsets call for one sensor at the minimum."
    *Why it is hard:* the design consequence is stated with no reasoning, and "clustering at the maximum" is unclear for distinct sensors.
    *Fix:* Add a "because" clause: correlated offsets cancel in a difference.

Other candidates: §5.1 "four trucks stood in side span N8 and six in centre span N7" (gauge names used as span names); §5.3 "There, the two deflections give a standard deviation of $\ln C_8$ of 0.87; adding the tiltmeter reduces it to 0.18, and identified first and third frequencies to 0.24" (elliptical, and the frequencies are not mentioned earlier); §2.5 "two static readings fix $\alpha$ for each $\kappa$ and constrain $\kappa$ only through their ratio" (it is unclear what "their" refers to).

## Spelling / grammar errors (certain)

- Abstract: "for strain of $cM_q/EI$". The wording is ungrammatical; it should read "for strain, at the extremes of $cM_q/EI$" (as in contribution 3).
- §3: "SLM absorbs the calibration error of the reference record, BPM does not." This is a comma splice; use a semicolon or "whereas".
- Appendix A: "Setting $F = 0$ factors as $(1-\xi)(1+\xi-\xi^2)$". An equation does not factor; write "$F$ factors as ..., and setting $F=0$ gives".
- §1 vs §4.1: "Nothing-on-road systems" vs "Nothing-on-Road BWIM dataset" / "NOR-BWIM". The capitalisation is inconsistent.
- §5.1 vs title/§5: "Hai Duong", "Kinh Mon" are written without diacritics while "Cầu Mây" has them. The mixed diacritic usage is inconsistent.

## Non-standard or inconsistent technical terms

- "indicator" (§2.3, Nomenclature) vs "index" ("side-span deflection index", abstract; "N8 index", "centre-span index", §5.2, §5.4; "side-span index", §2.5). Pick one.
- "constant" / "integral constant" / "record integral" / "strain constant". The base term is fine, but "constant" alone is ambiguous next to "constant predictor" (§4.1, §4.3).
- "vehicle-free noise" / "quiet-window noise" / "quiet noise" / "quiet periods" (§2.4, §4.2, §4.3, Concl. 3). These are synonyms for one concept.
- "crossing residuals" / "crossing errors" / "crossing-to-crossing errors" / "per-crossing errors" (§2.4, §4.3, §4.5, §6).
- "near-blind ring" (strain) vs "near-blind band" (deflection, and also strain in §2.2). "Ring" is non-standard for a 1-D interval.
- "static set" / "static admissible set" / "admissible set" / "static valley" (§5.2, Table 5, Fig. 9).
- "Möbius law" (abstract, §2.5, App. C). Calling it this is non-standard in structural engineering, and it is never explained as a linear-fractional dependence.
- "offset-immune" (§2.4, Table 4). It is non-standard, and "zero-sum weights" is also used for the same estimator.
- "N8"/"N7" are used both as gauge labels and span labels ("side span N8", §5.1). "T5", "T7", "T8" are support labels that are never defined.
- Channel names "ch1…ch12" (day 1) vs "st36", "st40" (day 2); the "st" names are never introduced.
- GVW (§4.5, Table 4, Fig. 7) is not defined, and the text otherwise says "gross weight". LOTO is defined only in a caption, GUM (§6) is not defined, and "two one-sided tests" (Table 3) is not expanded as TOST.
- Undefined or unlisted symbols: $w_q$ (Table 1, §2.4, §7), $\rho_{EI}$ (Nomenclature missing), $N_R$ (§5.3), $N_\theta$, $N_V$ (main text only via App. B), $T_\mathrm{cr}/T_1$ (§6, §7), $f_1$ (§7), $S_\alpha$, $S_k$, $S_{y8}$ (App. C), lowercase $l$ in $C_m = l^4/(192EI)$ (§3).
- §7 limitations: "a two-dimensional model". This conflicts with the Euler–Bernoulli beam model of §5.1 and the "one-dimensional" statement in the next sentence.
- §4.2: the text gives "90 % CI 0.904–1.098" for ch11, while Table 3 gives a 95 % CI of 0.874–1.136. Mixing CI levels for the same quantity confuses the reader.
- §2.4 vs abstract/§4.3: the vehicle-free correlation is given as 0.92 in some places and 0.90 "for the same window length" in others. The reason for two values is not explained where they first appear together.

## Single change that would most improve readability

Rewrite the abstract and the results paragraphs of Sections 4–5 to state each finding in words first and keep at most one or two supporting numbers in the prose. Move ranges, CIs and alternative normalisations to the tables. Doing this also removes most of the undefined terms from the abstract.
