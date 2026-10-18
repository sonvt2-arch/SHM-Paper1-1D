# Readability revision v4.1: report item → action

Input: `docs/editors_v4/blind_readability_v4.md` (overall 6.0/10). Editing mode: biên tập (viet-tu-nhien), English, NT-12, III.9, III.10, II.11, III.15–16. The text before this pass is in `manuscript_pre_readability.md`. No scientific content, number, equation, citation or claim strength was changed. The AI-disclosure paragraph and all seven [NEED VALUE] markers are verbatim. Nothing was committed.

## Checks after editing

- `python3 code/analysis/wp7b_checks.py manuscript/v4`: abstract 250 words (was 251); main text 7776 words (was 7426); 16 numbered equations, all cited; 7 [NEED VALUE] in the manuscript (unchanged).
- `python3 code/v4/num_diff.py manuscript/v4/manuscript_pre_readability.md manuscript/v4/manuscript.md` (new script): 637 distinct numeric values before and after; **no value disappeared, no value appeared**. Count changes come only from (a) values moved from prose into tables, (b) values removed from prose where the same value was already in a table, (c) the abstract rewrite, whose dropped values all remain in the body, and (d) labels (N7, T7, 0.4L, "12 gauges", the reused citation [34]). `traceability.md` has a new section listing every move.
- Tables renumbered after two new tables: new Table 4 (noise and crossing residuals, §4.3) and new Table 6 (admissible set against τ, §5.2). Old Tables 4–8 are now 5, 7, 8, 9, 10. Cross-references were updated in `manuscript.md`, `traceability.md`, `open_items.md` and `figure_table_plan.md`. `changes_from_v3.md` still uses the pre-v4.1 numbering.
- Word and PDF rebuilt: `word/Manuscript_v4.docx`, `word/Manuscript_v4.pdf` (also in `word/build/`).

## Scores and the single most useful change

| Criterion (score) | Action |
|---|---|
| 1 Abstract (4.5) | Rewritten (250 words). The main message comes first, in words: on continuous girders cancellation can blind a gauge, and the paper gives criteria to choose observing channels before installation. It carries three numbers (20.4 % against 11.9 %, factor 6.6). No undefined symbols. "Möbius law" became "a closed-form law for the effect of uncertain pier stiffness", and "for strain of $cM_q/EI$" is gone. The Cầu Mây result is stated as its consequence: the side-span gauge's constant is uncertain by a factor of 6.6, the centre-span gauge is identifiable, and one pier tiltmeter would close the gap. |
| 5 Density (4.0) | §4.2–4.4 and §5.2–5.3 were rewritten so each paragraph opens with its finding in words. Ranges, CIs and alternative normalisations went to Tables 3, 4 (new), 6 (new), 7 and 10. Long paragraphs were split so each holds one finding. Two data-description paragraphs (§4.1, §5.1) still carry many values; this was accepted because they describe the data, not results. |
| 6 Terminology (5.0) | See the terminology section below. |
| 8 Tables (6.0) | Table 3: the TOST/90 % CI rule is now stated in the caption, and the 90 % CI sits in the ch11 cell. The Table 7 (old 5) caption says the bound is listed pinned then fixed and that the N7 indicator falls with fixity, which explains "0.263 … 0.145". |
| Single change | Done (abstract and §4–5 results, as above). |

## Ten hardest passages

| # | Passage | Action |
|---|---|---|
| 1 | Abstract, "That this area equals … is classical; …" | Now: "Two classical facts underlie the work: … From them follow …". |
| 2 | Abstract, "placement rule (… for strain of $cM_q/EI$); and a Möbius law" | Symbols and the law's name removed from the abstract; the rule and the law are stated in words. |
| 3 | Abstract, "side-span deflection index (effective-rigidity normalisation) between 0.14 and 0.42" | Replaced by the consequence: the constant is uncertain by a factor of 6.6 (the value from §5.2). The range 0.14–0.42 remains in §5.2, Table 6 and Conclusion 5. |
| 4 | §4.1 day-1 channels | Rewritten unambiguously: four stations each carry two gauges (a wheel-path gauge with axle spikes, ch4/ch5/ch11/ch12, and a partner gauge), and four further gauges show no spikes (ch1, ch2, ch8, ch9). **Note:** the report's suggested fix ("each of four stations has three gauges") is wrong. `docs/pkg1/3_norbwim_analysis.md` l. 25 shows the stations are pairs and the no-spike gauges are not assigned to stations, so that wording was not used. |
| 5 | §5.2 $r_{87}$ | Defined in one plain clause: "$r_{87} = 1$ would mean that one model fits both gauges exactly". The finding comes first: "No pier stiffness lets the beam model fit both static readings exactly." The nomenclature entry was updated. |
| 6 | §1 transmissibility digression | Moved to §2.4, after the standard-load method's needed property is stated. The clause "the present paper asks instead…" was dropped because the gap paragraph already says it. |
| 7 | §4.3 "so both estimators are significantly worse" | Now "GLS and the offset-immune combination are both significantly worse than the average". The sd prediction is no longer set against MAE in the prose; it points to the Table 5 predicted-sd column. |
| 8 | §5.2 two normalisations in one sentence | The prose keeps the effective-rigidity range (0.14–0.42). The design normalisation, the α ≈ 0.5 condition and the prior-α ranges moved to Table 6. |
| 9 | §5.3 "there … so the choice depends on" | Now opens with "This ranking changes when the section gain is included." The vague "there" became "at those locations". |
| 10 | §2.4 "Independent offsets call for clustering…" | Each design consequence now has a "because" clause tied to Eqs. (13) and (14): with independent offsets the variance falls with the sum of the squared constants; with correlated offsets a common offset cancels in a difference and the variance falls with the spread of the constants. |
| other | §5.1 "side span N8 / centre span N7" | Now "the side span that carries gauge N8 … the main span, which carries gauge N7". The gauges are defined before they are used. |
| other | §5.3 Cramér–Rao paragraph | Split into a settings paragraph and a results paragraph. The frequencies are named as "identified first and third vertical frequencies" and are linked to §5.2. |
| other | §2.5 "constrain κ only through their ratio" | Now "For any assumed κ, two static readings therefore fix α, and they constrain κ only through the ratio of the two readings." |

## Certain errors

| Error | Action |
|---|---|
| Abstract "for strain of $cM_q/EI$" | Removed with the abstract rewrite. Contribution 3 keeps the correct wording. |
| §3 comma splice | "…, whereas BPM does not." |
| App. A "Setting $F = 0$ factors as …" | "Because $1-2\xi^2+\xi^3 = (1-\xi)(1+\xi-\xi^2)$, setting $F = 0$ gives Eq. (6)." The identity is exact and Eq. (6) is unchanged. |
| Nothing-on-Road capitalisation | Now "Nothing-on-Road (NOR)" in §1 and "Nothing-on-Road BWIM (NOR-BWIM)" in §4.1. Reference [15]'s title is left as published. |
| Diacritics | Place names in §5.1 now carry diacritics, like Cầu Mây: Kinh Môn, Hải Dương. The affiliation block (fixed format, VII.6) and the text inside the Acknowledgments [NEED VALUE] marker ("Hai Duong PMU") were left verbatim. |
| §7 "two-dimensional model" | Now "an Euler–Bernoulli beam model with an assumed depth law and equal pier springs", as in §5.1. |
| §4.2 90 % vs Table 3 95 % CI (ch11) | Both are correct and come from `code/norbwim/logs/v4.log` l. 20: 95 % CI 0.874–1.136 and 90 % CI 0.904–1.098. The log header (l. 6) says TOST uses the 90 % CI. Table 3 keeps the 95 % CI in the Ratio column, puts the 90 % CI in the Equivalence cell, and its caption explains the rule. |

## Terminology

| Item | Choice applied everywhere |
|---|---|
| indicator / index | "indicator" (the only "index" left is in the title of reference [34]). |
| vehicle-free / quiet-window / quiet noise / quiet periods | "vehicle-free noise", "vehicle-free windows/segments/periods". |
| crossing residuals / errors / crossing-to-crossing / per-crossing errors | "crossing residuals", defined at first use in §2.4 (the deviation of each crossing's integral from its calibrated value). The weight errors in §6 are called "weight errors of single crossings". "Per-crossing standard deviation" is kept for the predicted sd, a different quantity. |
| near-blind ring / band | "near-blind band", defined once in §2.2 for both deflection ($|N_w|<0.2$) and strain ($|N_M|<0.2$). It is used in the contributions, §2.2, §5.3, §7 and §8. |
| static set / static admissible set / admissible set / static valley | "static admissible set" is defined in §5.2 and shortened to "admissible set" afterwards. The Fig. 9 caption has "valley of best static fit". |
| Möbius law | Explained as a "linear-fractional (Möbius)" dependence in contribution 4, §2.5 and App. C. |
| offset-immune / zero-sum | §2.4 says "this zero-sum estimator is called offset-immune below". |
| constant predictor | "mean-weight predictor" (§4.1, §4.3, Fig. 7). This avoids a clash with "constant" C. |
| N8 / N7 | Used only as gauge labels. Spans are called "side span" and "main span". Both gauges are in the Nomenclature. |
| T5, T7, T8 | Defined in §5.1 (T7 a monolithic inner pier; T5 and T8 end supports on pot bearings) and in the Nomenclature. |
| ch / st channel names | §4.1 says day-1 labels carry the prefix "ch" and day-2 labels keep the dataset's prefix "st". |
| T2/T1 (trucks) | Table 3 caption: "T2/T1, second to first truck". |

## Symbols and acronyms defined at first use and added to the Nomenclature

$w_q$ (Table 1 and Nomenclature), $\rho_{EI}$ (§2.2 wording and Nomenclature), $N_R$ (§2.2), $N_\theta$ and $N_V$ (Nomenclature, pointing to App. B), $T_\mathrm{cr}/T_1$ (§6, in words), $f_1$ (§7), $S_\alpha$ and $S_k$ (App. C), $S_{y8}$ and $S_{y7}$ (App. C), $l$ (§3), $K$ (Eq. 16 lead-in), $C_0$, $C_\infty$, $EI_\mathrm{ref}$, $L$, $\Sigma$ (Nomenclature). Acronyms: GLS (abstract), GVW (§4.1), LOTO (§4.3), GUM (§6, spelled out), TOST (Table 3), NOR (§1), MAE, CV and CI (Nomenclature). These entries were added to the Nomenclature: $C_0$/$C_\infty$, $EI_\mathrm{ref}$, $f_1$/$T_1$, $L$/$l$, $N_\theta$/$N_V$/$N_R$, $S_\alpha$/$S_k$, $T_\mathrm{cr}$, $w_q$, $\rho_{EI}$, $\Sigma$, and an acronym block. That block covers BWIM, NOR, CI, CV, MAE, FE, GLS, GUM, GVW, LOTO and TOST, plus the labels N7, N8, T5, T7 and T8.

## Items noted but not acted on

- Introduction paragraphs 2–3 are citation catalogues (criterion 2). They were left as they are because the task did not cover them.
- Eqs. (5)–(8) come in quick succession (criterion 7). The text around the equations was not changed beyond the near-blind band definition.
- Conclusions 3–5 are dense. Only their terminology was edited, because the numbers there are the paper's anchor values.
- 0.92 against 0.90 (vehicle-free correlation). Table 4 now labels them as "non-overlapping windows" (0.92, `v4.log` l. 98) and "at the window length of each crossing" (0.90, l. 155). Conclusion 3 keeps 0.63 against 0.92 as before.
- The §5.1 location of gauge N8 ("side span between pier T7 and end support T8") is taken from `docs/pkg1/3_de_cuong_thu_nghiem_hien_truong.md` l. 74 (span N8 = 145–200 m; T7 at 145 m, T8 at 200 m). The authors should confirm it.
