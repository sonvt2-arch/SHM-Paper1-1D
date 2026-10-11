# Response to the WP8 red-team report: SCHM addendum (manuscript/schm)

This addendum covers the SCHM version in `manuscript/schm/` (copied from `manuscript/v2/`, which was left untouched). The v2 response follows unchanged below; its section, table and equation numbers still hold, because no number changed.

## SCHM desk-editor triggers (red-team report §1a)

| Trigger | Status in the SCHM version |
|---|---|
| 1. Cover letter for another journal | Closed. `cover_letter_SCHM.md` is addressed to Lucia Faravelli, Editor (name from the journal homepage), as a Research Article. |
| 2. Placeholders | Reduced to items that need the authors: manuscript 6 `[NEED VALUE]` (weights class; data permission ×2; acknowledgement; conflict of interest, HUCE consultancy; funding statement, employer and APC), cover letter 2 (date; overlap with the two papers under review at *Structures*). The two new ones follow from the SCHM guide, which asks for an explanation of each interest and for the employer and APC source in the funding statement. All are listed in `open_items.md`. |
| 3. Self-undermining abstract | Closed in v2; abstract unchanged (236 words; SCHM limit 300). |
| 4. Keywords | Closed: "Structural health monitoring" and "Sensor placement" lead the six keywords. The current SCHM guide does not mention keywords (`schm_requirements.md`). |
| 5. Section 5 as padding | Further tightened (one duplicated range removed; first and last paragraphs shortened); Fig. 8 and Fig. 9 redrawn with plain-language legends and axis labels. |
| 6. Scale-independence argument | Already present since v2 (opening of Section 3); no change. |
| 7. Long title | Kept (author decision B6 in the v2 list). |

## Items listed as partly done or not done in the v2 response

| v2 item | SCHM status |
|---|---|
| Fig. 3 and Fig. 7 Thái Bình panels "to be removed at redraw" | Done. Both figures redrawn by `code/analysis/schm_figures.py`; Fig. 7 now also carries the calibration-B influence lines. |
| #22 SIE management contribution | Not relevant to SCHM; not pursued. |
| #31 overlap with other submissions | Needs the authors; placeholder in the cover letter, `open_items.md` 5. |
| #32 APC with no funding | Needs the authors; Funding Statement placeholder, `open_items.md` 7. |
| B7 main-text length | 9563 → 9221 words by `wp7b_checks.py manuscript/schm` (Sections 2 and 5 tightened; the two-span decomposition paragraph, the 60-comparison FE check, the main-span closed form and the two-span cubic remark moved to Appendices A and D with pointers). SCHM sets no word limit. The ≤ 9,000 target was not reached without moving content outside Sections 2 and 5. |
| B10 internal docs | Not supplementary material; not edited. |

## SCHM format changes

Highlights removed; declarations renamed and ordered as the SCHM guide recommends (Data Availability, Conflicts of Interest, Funding Statement, Acknowledgments at the end, Supplementary Materials before the references); "CRediT authorship contribution statement" renamed "Author Contributions"; the AI declaration kept verbatim under "Disclosure of Generative AI Use" (Wiley allows disclosure in Methods, Acknowledgements or a separate disclosure), and the Computational Implementation sentence on AI kept verbatim; figure captions moved after the references; captions of Figs. 3, 7, 8 and 9 rewritten to match the redrawn figures; reference style unchanged (SCHM accepts any style and converts to Chicago after acceptance).

---

# Response to the WP8 red-team and verification reports (manuscript v2)

Files: `manuscript/v2/` (v1 kept unchanged in `manuscript/structures/`). Section, table and equation numbers are those of v2. Reference numbers are v2 numbers (old [28]–[40] are now [30]–[42], old [41]–[47] are now [45]–[51]; new [28] Helmi et al. 2014, [29] Lydon et al. 2016, [43] Zhou et al. 2026, [44] Ghali et al. 2017). New numbers come from `code/analysis/wp7b_peps.py` (log `code/analysis/logs/wp7b_peps.log`, cited as P7); counts from `code/analysis/wp7b_checks.py`.

## 1. Red-team issues (report §4)

| # | Issue | Action in v2 / reason if not done |
|---|---|---|
| 1 | Cover letter addressed to *Structures* | Replaced by `cover_letter_SCHM.md` and `cover_letter_SIE.md`, each with a scope paragraph in that journal's words. Neither mentions *Structures* or any earlier decision (orchestrator instruction; the red team's optional mention of the JCSHM decision was therefore not used). |
| 2 | Placeholders and reviewer tags | Removed: truck weights (now "the test report gives no weighbridge values", source INVENTORY), Type A sentence (now states the entries are bounds), refs [6], [10], [48], [49], [51]. Kept, because the facts are not in the repository: weight accuracy class (§7.2), owner permission and owner of the field records (Data availability), acknowledgement choice, cover-letter date and reviewers. Listed in `open_items.md` A1–A4. |
| 3 | Near-blind N8 rests on one calibration (blocking) | §4.2 now reports calibration A (design EI, k_FE; α = 1.088 at k_FE, misfit −4.6/+5.0 %) and calibration B (joint fit α = 0.716, k = 1.2 × 10⁸ kN m/rad, misfit −2.8/+2.9 %), and states that two static readings cannot separate girder rigidity from pier stiffness. Table 5 and §4.3: N8 index 0.181 (82 % cancelled) or 0.476 (44 %); N7 0.209 or 0.234. Message rewritten in abstract, highlight 5, §4.4 and §8: the side-span gauge is not identifiable from design data plus two static readings and is ill-conditioned with respect to pier stiffness; C_m must come from SLM or an in-situ identified model. "Near-blind" is no longer used as a statement about N8. v2 does not argue which calibration is physical (no pier data); `open_items.md` B2. |
| 4 | "Fourteenfold" uses pinned/fixed limits | Removed. §4.3 and Table 5 quote the limits as bounds (0.02–0.45 for N8), not as an uncertainty. Added local sensitivity at k_FE: N8 index 0.124–0.248 for k = 0.5–2 k_FE, ∂lnC_m/∂ln k = 0.51 (N7: 0.191–0.224, −0.12) (P7 Part B). |
| 5 | "BPM underestimates by 7–9 %" | Removed. §4.4 gives per-gauge ratios against the report FE (0.936, 0.923), model A (0.977, 0.890) and model B (1.029, 0.972), and both α values. |
| 6 | "Blind only when β < 0.964706" | §2.3: "blind at β = 0.964706 … negative constant for smaller β". |
| 7 | §7.1 step 2 contradicts the |C_m| logic | Step 2 now reads "stay out of the band |N_m| < 0.2 around the blind locus, on both sides of it", with the band edges 1.385–1.525 (two spans) and 1.621399–1.775 (three spans, mid side span) (P7 Part E). §2.2 states that a negative C_m is observable (|N_m| = 2.0 at ρ_L = 2) and what changes beyond the blind ratio (dominance of the uninstrumented span, sign-reversed processing). |
| 8 | 2cos(π/9) framed as failure | §2.3, abstract and §8: 2cos(π/9) ends the side-span blind locus; beyond it no side-span position is blind, and |N_m| = 0.875 at β = 2 (P7 Part E). |
| 9 | Supplementary logs say "whole side span blind" | Print labels in `code/analysis/verify_3span.py` and `cm_3span_theory.py` changed to "side-span blind locus ends (no positive C_m on the whole side span)"; both scripts rerun; logs differ from the old ones only in that label line. `docs/wp2_three_span_theory.md` and `docs/04_…` not edited (internal, not supplementary); `open_items.md` B10. |
| 10 | No bridge-scale Eq. (19) | Done with repository inputs only (P7 Part A; C_m from `wp3_Cm_table.csv`, L_tot = 200 m): new Eq. (19) form with P_ε = ε0 L_tot/C_m and new Table 8 for both calibrations. 25 t truck, ε0 = 0.05 mm: N8 93 % (A) or 36 % (B); N7 11 % or 10 %. The red team's figures (94 %, 11 %) used L_tot = 204.95 m and are not quoted. Table 10 note limits the 2–10 % field offset entry to well-conditioned gauges. |
| 11 | Table 9 rule inconsistent; GUM misuse | Now Table 10. One rule for every column: root-sum-square of standard uncertainties, after correcting known biases (quadrature bias "corrected" by Simpson), which is how the GUM [47] is now cited. Combined values recomputed (P7 Part D): 0.4–1.0 %, 2.3–10.5 %, 5.6–18.5 %. Bound conventions stated in the caption. |
| 12 | ε0 meaning and technology; contradiction with §5 data | ε0 defined as the residual after pre/post re-zeroing (nomenclature, §6.1). §6.2 states that the ε0 values are of LVDT class and that a non-contact system on a long span must establish its own residual offset (no numbers for those systems were added, because none are sourced in the repository). §5 reports what the field records show (post-minus-pre 0.0–0.1 mm at Gie Cuc at 0.1 mm resolution, 0.17–0.23 mm at Phuong Do N2, quiet scatter 0.01–0.13 mm; WP4) and says that offsets of a few hundredths of a millimetre were not demonstrated on those channels. |
| 13 | Load-dependent lab excess | §3.3 gives the ratios per configuration (1.010, 1.016, 1.017; P7 Part C), shows that the step is exactly the SLM residual (0.61 %, 0.70 %), lists the possible causes (support seating, masses, positions) and asks for repeated loads of different magnitude in the direct test (§7.2). The misattributed "about 1.6 %" was removed. |
| 14 | SLM not credited to Ojio–Yamada | §2.4: "Eq. (11) is the influence-area calibration of Ojio and Yamada [27] written for a deflection record." |
| 15 | Strain corollary missing | §2.1, one paragraph: strain-integral constant c M_q(x_m)/(EI q0); strain blind points at the uniform-load contraflexure points (0.75L on equal two spans), present on every continuous girder, unlike the deflection blind configurations. |
| 16 | Literature gaps | Added and verified on Crossref: Zhou et al. 2026, SCHM, 10.1155/stc/1361157 (deflection-influence-line stiffness inversion of continuous girders; cited in §1 and §4.4 as the kind of in-situ identification the side-span gauge needs). Winnipeg study: Helmi, Bakht, Mufti 2014 (10.1007/s13349-014-0076-5) and Lydon et al. 2016 review (10.1007/s13349-015-0119-6). Checked content: seven-span slab-and-girder bridge; the Ojio–Yamada area method was within 5 % with accurate speeds; the negative GVW came from the asymmetry-coefficient method, not from the area method; continuity of the instrumented span is not stated in the accessible sources, and §1 says so. [39] five-span continuous confirmed from the abstract. Zhou et al. 2025 (old [38], now [40]): abstract not retrievable; still cited only for its title. |
| 17 | Eq. (3) without a classical source | Ghali, Neville, Brown, *Structural Analysis* (CRC, 2017, 10.1201/9781315273006) cited for Maxwell's and Betti's theorems; §1 now says the identity is classical. |
| 18 | "Confirms" for model results | §4.4: "indicates, in a model built from the designer's section data"; §5 and §8: "illustrate", and §8 states that the records come from simply supported spans. |
| 19 | Self-undermining abstract | Abstract rewritten (236 words): leads with the SHM sensor-placement question, gives the bridge-scale result for both calibrations and the offset bias; the "not a validation" clause moved to the body and conclusions. |
| 20 | No scale-independence argument | New paragraph at the start of §3. |
| 21 | Section 5 reads as padding | Shortened to four paragraphs: limitations in one sentence, the residual-offset evidence added, speeds, speed-normalised scatter and the PD N1 lobe moved to supplementary material. |
| 22 | SIE management contribution | Partly: one sentence on the screening workflow in §7.1 and a management framing in `cover_letter_SIE.md`. The main text stays journal-neutral with an SHM framing, as instructed; a full SIE reframing (derivations to appendix, decision table) is listed in `open_items.md` B5. |
| 23 | Keywords | "Structural health monitoring" and "Sensor placement" first; "Measurement uncertainty" dropped to keep six. |
| 24 | R_m sign convention | §2.4 (R_m < 0 beyond blindness, ranking by |R_m|, no threshold) and §7.1 step 3 ("rank locations by |R_m|"). |
| 25 | "Partial cancellation about 37 %" | §6.1: residual magnitude 58 % of the BPM offset term, a 42 % reduction. |
| 26 | Three-load order | §3.1: 2550 g leading, second load 500 mm behind, third a further 250 mm; fits Appendix C with rms 0.030 mm against 0.55 mm (P7 Part C). |
| 27 | Simpson with odd n | §2.4 (3/8 end panel), §3.2 (20, 21 and 23 intervals), §7.1 step 9. |
| 28 | Units | Nomenclature states the m²/kN–mm²/N conversion, defines I_t = I_y/v, k, α, P_ε and the units of L_tot in §6.2; §6.4 uses I_t. |
| 29 | 1.1 × 10⁻⁴ unexplained | §4.2: trapezoidal integration of the nodal influence line on the 0.1 m mesh, against consistent nodal loads in the uniform-load route (from `wp3_fe.py`). |
| 30 | Overhangs | §3.1 and Appendix A: 400 mm of overhang, neglected in the analytical influence line. |
| 31 | Possible overlap with other submissions | Not resolvable from the repository. `open_items.md` B3 asks the authors to cite or disclose if rig, data or text overlap. |
| 32 | SCHM APC with no funding | Not a text change. `open_items.md` B1. |

Other red-team points outside the table: Table 5 now contains the striking fact that the mid side-span bracket (−0.066 … 0.375) contains an exactly blind state (§4.3, B-4); per-gauge ratios replace the single α (B-7); "about eight times" replaced by the computed 8.2 and 3.5 (B-7); the speed "self-calibration" is labelled an untested proposal (§6.4, A-3.6); Fig. 3 and Fig. 7 Thái Bình panels remain to be removed at redraw (`figure_table_plan.md`).

## 2. Verification report

| ID | Item | Action |
|---|---|---|
| N1 | 0.181 vs 0.1815 | 0.181 is the rounding of 0.181497 in `wp3_Cm_table.csv`; kept. Noted in `traceability.md`. |
| N2 | "0.30" attribution | Now V3 l. 107 (−0.30059) and WP2 l. 79. |
| N3 | "draft" sources | Renamed to `docs/wp2_three_span_theory.md` l. 160 and `docs/wp4_dynamic_records.md` l. 76–80. |
| N4 | `xcheck.py` not in repository | The v1 claim of 491 numbers is marked non-reproducible in `traceability.md`. New v2 values are traced to `wp7b_peps.log`, which is in the repository with its script; `wp7b_checks.py` covers counts and equation citations. A full two-way number check was not rerun. |
| N5 | 3.6 × 10⁷ | Attributed to L3 line 1 (Lv40). |
| I1 | Numbered equations not cited | Every numbered equation is now cited by number (Eqs. (9), (12)–(15), (17), (18), (20), (A.1) added in the text); checked by `wp7b_checks.py` (23 tags, none uncited). |
| I2 | [40] description (now [42]) | The Crossref abstract supports vision-based mid-span deflection and end-mounted accelerometers for axle detection; wording refined to "end-mounted accelerometers" and "calibrated influence line". |
| I3 | [35] description (now [37]) | Corrected to "a single-sensor strain feature grounded in influence-line theory … defect diagnosis, with a case study on a two-span continuous bridge" (Crossref abstract); "area-ratio" removed. |
| I4 | [37] five-span (now [39]) | Confirmed from the repository abstract (static load tests on a five-span continuous bridge). |
| R1 | [44] Sohn (now [48]) | Crossref 10.1098/rsta.2006.1935: "Effects of environmental and operational variability on structural health monitoring", Phil. Trans. R. Soc. A 365 (1851) 539–560; matches the intended use (environmental drift in long-term monitoring). Filled. |
| R2 | [45] Cross et al. (now [49]) | Crossref 10.1016/j.ymssp.2012.08.026: "Long-term monitoring and data analysis of the Tamar Bridge", MSSP 35 (1–2) 16–34; matches. Filled. |
| R3 | [47] AASHTO (now [51]) | 10th ed., 2024 confirmed (AASHTO Journal announcement; FHWA memo of 17 March 2026). Note removed. |
| R4 | [33] year/authors (now [35]) | Print issue 2679 (2), 2025; fourth author J. Mander added. |
| R5 | [6] note | Removed; title set to the Crossref wording with its quotation marks. |
| R6 | [10] note | Removed; URL resolves to "Comprehensive Truck Size and Weight Study: Volume II: Issues and Background [2000]". Whether it supports the station-cost statement remains for the authors to confirm (`open_items.md`). |
| R7 | Missing DOIs of books/standards | No action needed. |
| F1 | Abstract length | 236 words (240 by raw whitespace split), within the 240-word target. |
| F2, F3 | Keywords, highlights | 6 keywords; 5 highlights of 73–79 characters. |
| F4, F5 | [NEED VALUE] count | Manuscript: 4 (weights accuracy class; two in Data availability; acknowledgement), down from 11. References: none. |
| F6 | Editorial brackets | Removed. |

## 3. Orchestrator items not covered above

| Item | Action |
|---|---|
| Files moved to `manuscript/v2/` | Done by copy; `manuscript/structures/` untouched. The copied `cover_letter.md` was replaced by the two journal-specific letters. |
| AI disclosure | Declaration and the computational-implementation sentence kept verbatim. |
| Main-text word count | 9563 words (`wp7b_checks.py`; v1 by the same script 8168). |
| Git | Nothing committed. |
