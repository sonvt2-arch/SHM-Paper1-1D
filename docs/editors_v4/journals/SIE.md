# Desk assessment: Structure and Infrastructure Engineering (SIE)

**Manuscript:** "Blind loci and design criteria for integral load-monitoring channels on continuous girder bridges, with laboratory verification and an assessment on public field records" (Nguyen, Vu, Nguyen; v4)
**Assessor role:** Editor-in-Chief, Structure and Infrastructure Engineering – Maintenance, Management, Life-Cycle Design and Performance (Taylor & Francis)
**Date:** 19 October 2026

Sources I checked: the journal's aims and scope and its instructions for authors (tandfonline.com, journal code nsie20), the journal metrics page (17 % acceptance rate, 35 days to first decision, IF band Q2, CiteScore Q1), and recent SIE and competing-journal papers on BWIM and influence lines. I read the manuscript in full, skimmed the supplementary material and looked at Figs. 2 and 9.

---

## 1. Scope fit: 6 / 10

**Points in favour**

- SIE's scope lists *monitoring, optimization of maintenance and management*, *field testing*, *loads and multi-hazards*, *inspection and diagnostics* and *mathematical modelling*. Bridges are a core asset class. A paper on how to design load-monitoring channels before installation, with a field case on an in-service bridge, falls inside that list.
- SIE has published BWIM work. The manuscript already cites two SIE papers, Žnidarič et al. (2018, *Improved accuracy and robustness of B-WIM*) and Yu, Cai & Deng (2018, *NOR-BWIM with transverse position*), and Zhao et al. (2014, *field-calibrated influence lines for B-WIM*) also appeared in SIE. BWIM is therefore an established, if small, strand in the journal.
- The Cầu Mây section (identifiability of the constant from acceptance-test data, which measurement to add, and a pre-registered moving-load test) is the kind of "theory applied to a significant infrastructure problem" case study that the scope explicitly welcomes.
- The error budget and the screening workflow (Sections 6–7) speak to practitioners.

**Points against**

- SIE's centre of gravity is maintenance, management, life-cycle performance, reliability, risk and decision-making. As written, the paper is a structural-mechanics and measurement-design paper. It never connects the load estimate to a management decision: load rating, fatigue life, permit or overload enforcement, inspection prioritisation, or value of monitoring information. The only gesture is one sentence on "preliminary overload screening".
- About half of the main text is closed-form beam theory: blind loci, indicators, the Möbius law and the GLS and zero-sum algebra. That material belongs more naturally in *J. Bridge Eng.*, *Eng. Struct.*, *MSSP* or *SHM*. SIE readers will find the formula density high relative to the management payoff.
- The BWIM papers SIE has published recently are system- and accuracy-oriented, with field validation against weighed traffic. This paper's field evidence is mostly negative: no weight discrimination, every estimator worse than predicting the mean weight, and GLS worse than a plain average. At SIE that framing raises a desk-level question about practical value.

On balance the topic is in scope, but the framing points to a sensor and mechanics journal. Hence 6 rather than 8.

---

## 2. Desk decision AS IS

**Decision: borderline. I would lean towards sending it to review only if a handling editor with a BWIM or SHM background is available. Otherwise I would desk-reject it as better suited to a bridge-mechanics or SHM journal, and invite resubmission with a management-oriented framing.**

**Estimated probability of being sent to review as is: about 40 %.**

Reasons:

- (+) The work is technically careful and honest. Uncertainty is stated throughout, the closed forms are FE-verified, the data are public, the scripts are provided, and the limitations are explicit. That makes it reviewable rather than an obvious reject.
- (+) Pre-installation channel design and identifiability of the constant under boundary uncertainty is a genuine and usable idea for asset owners.
- (−) The title and abstract read as a mechanics paper ("blind loci", "Möbius law", "Generalised least-squares weights"). The abstract is a list of findings, two of them negative, with no statement of why an infrastructure manager should care.
- (−) The headline field result reads as "the method could not be shown to work on these data". An EiC skimming the abstract sees "invariance only within 10–27 %", "did not allow weight discrimination to be tested", "performed worse out of sample" and "uncertain by a factor of 6.6".
- (−) It is formally out of line with the author instructions: the abstract is about 250 words against the 200-word limit, there are 6 keywords against the required 7–8, and the main text is about 9,300 words plus 8 tables, 9 figures, a nomenclature and 3 appendices. That is at the top of the "typically 5,000–10,000 words" guidance. None of this is fatal alone, but together it signals a dense paper.
- (−) The idea is presented as five contributions. Novelty is diluted, and the paper concedes that neither the core identity nor the estimator is new.

---

## 3. Best reframing without new experiments

**Estimated probability of being sent to review after reframing: about 60 %.**

The reframing presents the paper as a decision-support and monitoring-design paper for owners of continuous girder bridges. The mechanics becomes the tool, not the product.

### Title (suggested)

"Designing low-cost gross-weight screening on continuous girder bridges: observability, boundary identifiability and field evidence"

Alternative: "Which gauge, where? Pre-installation design of integral load-screening channels for continuous girder bridges under boundary uncertainty"

### Contribution statement (one paragraph, replacing the five-item list)

> Bridge owners increasingly want to know the loads their continuous girders actually carry, but cannot instrument every structure with full BWIM. Integral (influence-area) weighing needs only one scalar constant per channel, yet on continuous girders that constant can vanish or become unidentifiable. This paper gives owners a pre-installation procedure that answers three questions: (i) will a candidate gauge observe the total load at all (closed-form blind loci and conditioning indicators); (ii) is its constant robust to the uncertain pier fixity of an existing bridge, and which single extra measurement would resolve it (scaled-pier-stiffness law and Cramér–Rao bound); and (iii) what accuracy the screening can realistically deliver (an error budget calibrated on public moving-truck records). It demonstrates the procedure on an in-service 55 + 90 + 55 m box girder using only its acceptance-test data.

### Emphasis

1. **Lead with the decision problem.** Section 1 should open with overload risk and asset management, then move quickly to the owner's question of where to put one or two sensors on an existing continuous bridge so that a screening system is meaningful. Cite SIE literature on monitoring for management decisions and on the value of SHM information, and the SIE BWIM papers already cited.
2. **Make Cầu Mây the centrepiece.** Move Section 5 up to follow the theory directly, and frame it as a worked asset-owner example: from acceptance-test data to installed-gauge diagnosis, to the recommendation of one tiltmeter or one integral ratio, to pre-registered predictions (Table 6). This is the most SIE-like part of the paper.
3. **Present the NOR-BWIM assessment as calibration of the error budget and as practical cautions,** not as a validation that failed. Each lane and each deck gauge needs its own constant. A beam-model BPM fails on deck-soffit gauges. Covariances estimated from vehicle-free windows mislead GLS. Each of these is a useful lesson for owners. State plainly, once, that weight discrimination could not be tested.
4. **Close with a management-level discussion** that needs no new data, written as qualitative and indicative. Use the existing numbers (Table 7, offset-equivalent load, lane ratio) to say what threshold margin a screening system on such a girder would need, what fraction of heavy vehicles it could plausibly flag, and how that output would feed load rating, fatigue or enforcement. Avoid any new quantitative claim not supported by the analyses already done.

### Length target

- Main text about 7,000–7,500 words, with at most 6 figures and 5 tables.
- Abstract 200 words or fewer, unstructured.
- 7–8 keywords, for example adding "Asset management", "Overload screening" and "Boundary-condition uncertainty", and dropping "Identifiability" or merging it.

### What to cut or move to the Supplementary Material

| Item | Action |
|---|---|
| Section 3, laboratory verification | Compress to one paragraph plus Table 2, or move entirely to the Supplement. Static loads on a 2 × 2.5 m tube add little at SIE level, and the authors themselves call it an indirect check. |
| Section 2.4, GLS/zero-sum derivation, Eqs. (13)–(14), Fig. 4 | Keep the placement rule (extremes of C(x)) and one sentence on the zero-sum idea. Move the variance algebra, Fig. 4 and the Monte Carlo study to the Supplement. Keep the out-of-sample warning in the field section. |
| Appendix B, invariant weighting functions and the transmissibility link | Move to the Supplement. |
| Table 1 and Eqs. (4)–(9) | Keep Table 1 as the practitioner's lookup table and Fig. 2 as the observability map. Move the intermediate closed forms (Eqs. (7)–(8) derivations, Table A.1) to an appendix or the Supplement. |
| Nomenclature (about 60 symbols) | Cut by about half, by moving symbols used only in the appendices or the Supplement. |
| Table 3, field estimator errors | Keep, but reduce to 4–5 rows (best single, average, GLS measured Σ, mean-weight predictor). Move the rest to Table S6. |
| Table 8, error budget | Keep. It is one of the most SIE-relevant items. |
| Section 7, design workflow | Keep, ideally as a flowchart figure, which costs no new work and suits SIE readers. |

### Other presentational fixes

- Rewrite the abstract as problem → procedure → in-service demonstration → field-calibrated limits → practical recommendation. Report the negative field findings in one sentence, as limits.
- Use British spelling consistently and single quotation marks (SIE house style). Use author–date references in the T&F style; reformatting is assumed.
- Keep the AI disclosure and the conflict-of-interest statement on the Cầu Mây data as they are. They are appropriate.

---

## 4. Probability of eventual acceptance

| Case | P(sent to review) | P(accept, given review) | Overall P(accept) |
|---|---|---|---|
| As is | about 40 % | about 35 % | **about 14 %** |
| After best reframing | about 60 % | about 45 % | **about 27 %** |

Notes:

- The journal's overall acceptance rate is 17 %.
- Even after review, expect major revision. Reviewers will almost certainly ask for (a) evidence of weight discrimination with trucks of clearly different weights, and (b) the Cầu Mây moving-load test. Neither can be supplied without new experiments.
- The reframed version gains mainly because reviewers chosen from SIE's monitoring and management pool will judge it on practical value, where the identifiability and channel-design story is strong. A mechanics-oriented reviewer would judge it on the novelty of a classical identity, where the case is weaker.

---

## 5. Three main desk-level risks at SIE

1. **Weak link to maintenance, management or life cycle ("wrong journal" risk).** The editors filter for the management and decision payoff. A paper whose output is closed-form blind loci and an estimator comparison, with no link to rating, fatigue, enforcement or value of information, is easily redirected to *J. Bridge Eng.*, *Eng. Struct.*, *JCSHM* or *SHM*.
2. **The field evidence reads as negative and limited.** One public dataset with four trucks and almost constant reference weights, no estimator beating the mean-weight predictor, GLS worse than averaging, and an in-service case with static data and predictions only. A desk editor may conclude that practical value is undemonstrated. Related to this is the perception that the novelty is incremental, since the core identity and GLS are classical, as the paper concedes.
3. **Length, density and format non-compliance.** About 9,300 main-text words with 8 tables, 9 figures, a long nomenclature and 3 appendices; a 250-word abstract (limit 200); 6 keywords (7–8 required); heavy notation. This invites a "technical check / return to author" or a quick reject for readability.

---

## 6. Article type, length limits and fees

- **Article type:** Research Article. SIE accepts Research Article, Review Article and Data Notes; the journal page also lists book review, commentary and letter to the Editor.
- **Length:** the main text (excluding abstract, declarations and references) is "typically 5,000–10,000 words". The abstract must be unstructured and no more than 200 words, with 7–8 keywords. Element order: title page, abstract, keywords, main text, acknowledgements, declaration of interest, references, appendices, tables (each on its own page), figures, figure caption list. Word or LaTeX, with figures supplied as separate files.
- **Style:** British (-ise) spelling, single quotation marks, T&F reference style. Single-anonymous review by two independent reviewers after editor screening.
- **Fees, subscription route:** no APC and no page charges if published under the standard (non-open-access) route. The journal describes itself as subscription-based, hybrid Open Select. I found no colour-figure charge in the current instructions; online colour is standard.
- **Fees, open access route (Open Select, CC BY or CC BY-NC-ND):** an APC applies. The exact amount is shown only through the T&F APC finder, which I could not retrieve. For T&F hybrid engineering titles it is typically about USD 3,500–4,100 (about GBP 2,600–3,000 / EUR 3,000–3,500); **verify with the APC finder before submission.** It may be reduced or waived if HUCE or a Vietnamese consortium has a T&F open access agreement. Only the corresponding author can claim institutional funding.

---

## Summary

- Scope fit: **6/10**. The topic (bridge monitoring, BWIM, field testing) is in scope, but the framing is mechanics- and sensor-oriented, not management- or life-cycle-oriented.
- As is: borderline; **about 40 %** chance of being sent to review; **about 14 %** overall acceptance.
- After reframing as an owner-facing, pre-installation monitoring-design procedure, with Cầu Mây as the centrepiece, about 7,000–7,500 words, the lab section and GLS algebra moved to the Supplement, and a 200-word abstract: **about 60 %** chance of review; **about 27 %** overall acceptance.
