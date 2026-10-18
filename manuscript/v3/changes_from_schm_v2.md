# Changes from SCHM v2 (`manuscript/schm/manuscript.md`) to v3

Editor concerns are numbered as in `docs/editors/00_TONG_HOP_4_BIEN_TAP.md` (E1–E11). Main text: 9221 → 7461 words (Sections 1–8, prose only); abstract 236 → 247 words; numbered equations 23 → 16; main-text tables 10 → 7; main-text figures 10 → 9.

## Reframing and title

| Change | Why (editor concern) |
|---|---|
| New title: load observability, general response-integral theorem, offset-immune estimation, field verification | E6 novelty; E1 asked that the title not imply moving-load validation that is absent: v3 now has moving-load field data |
| Introduction rewritten around criteria for designing load-monitoring channels; five contributions; the integral idea credited directly to Ojio and Yamada (primary source verified, ICWIM3 2002) | E6, E10 (secondary-source attribution); E2 (BWIM) asked that the estimator not be claimed as new: SLM is now called the Ojio–Yamada calibration in §3.2 |
| Sentences flagged by editor 1 as rejection triggers removed or rewritten ("the identity itself is classical … foundation, not the headline", "eleven significant figures", "falsifiable prediction … not carried out" moved to limitations in neutral form, "never from the design model" softened, "we propose, without having tested it" removed) | E1 list |

## Added

| Added | Source | Concern |
|---|---|---|
| §2.1 general theorem for any linear channel; Eq. (3) strain constant | package 1A | E6, E1 concern 7 (strain under-discussed), E2 concern 3 |
| Eq. (9) and Table 1: closed-form blind loci for strain, rotation, shear and reaction, two- and three-span | 1A | E6, E1 concern 7 |
| §2.3: $N_M$ as a reference-free indicator; $R$ for strain; $P_\varepsilon$ moved here as Eq. (12) | 1A | E6 (threshold must work on haunched girders) |
| §2.4: GLS multi-channel estimator, Eq. (13); offset-immune estimator, Eq. (14); placement theorem; corrected claim "the only weight translation-invariant **for every structure**" | package 1B | E4 (offset dominates); task brief (correct §2.4 claim) |
| §2.5: κ = k/α structure, Möbius law Eq. (15), closed form Eq. (16), $B_m$ | package 1C | E3 (non-identifiability stated loosely) |
| §4: field verification on NOR-BWIM public data (invariance 3- vs 5-axle, SLM, speed, superposition, lane, gauge ratios, beam-model limits, noise) | package 3 (`code/norbwim/`) | E1 (no moving-load test on a continuous structure, all four editors), E8 |
| §5.2–5.3: admissible range instead of two calibrations; A, A′, B as reference points with their real misfits; frequencies as conditional evidence that excludes B under the mode-3 interpretation | 1C | E3 (A does not fit; B is nearest, not exact; α = 0.716 implausible) |
| §5.4: which channel and where on Cầu Mây (strain 5–10 m from piers, end reactions, deflection pair 100/152 m, tiltmeter on T7) | 1A, 1B, 1C | E1 concern 3, E4 concern 3 |
| §5.5 and Table 5: predicted discriminating measurements from the field-test plan, stated as design | `docs/pkg1/3_de_cuong_thu_nghiem_hien_truong.md`, `code/fieldplan/` | E1 concern 3 (discriminate A vs B) |
| Table 6: offset bias for ε0 = 0.02–0.5 mm over the joint admissible set; ε0 stated next to every headline number (abstract now quotes 0.1 mm) | new script `code/v3/v3_numbers.py` | E4 (offsets too optimistic; abstract biases were scenarios) |
| §6.3: transverse position and multiple presence, with measured values (lane ratio 0.81, 2.05 mm spread, superposition 0.92–0.93, 12.4 s window) | 3B, SCHM §4.4, FP | E7 |
| References: Ojio & Yamada 2002 [27]; Agüero-Barrantes et al. 2021 [35]; Wu et al. 2020 [42]; Moghadam et al. 2022/2023/2023 [43–45]; NOR-BWIM dataset [50]; Moghadam 2022 dissertation [51] | Crossref/DataCite/TRID checks (open_items D1–D4) | E10, task brief |

## Corrected

| Item | Old | New |
|---|---|---|
| Table 5 (now Table 4) N7 bound | 0.145 … 0.263 | 0.263 … 0.145 (pinned … fixed) |
| Calibration A presented as reproducing the measurements | "two calibrations reproduce the measured deflections" | A is the design model (misfit +2.4/+12.3 %); A′ and B given with their misfits; static data bound κ only from below |
| Indicator range at N8 | "0.18 or 0.48" | 0.12–0.82 (static), 0.12–0.39 (with frequencies, conditional) |
| Table 10 "GUM-consistent budget" with root-sum-square | combined 0.4–1.0 %, 2.3–10.5 %, 5.6–18.5 % | Table 7 "indicative sensitivity budget", no combination, values only where measured; explicitly not a GUM evaluation (E5) |
| §2.4 claim on uniform weight | "the only weight invariant to translation" | "the only weight that is translation-invariant for every structure" (1B Proposition 2 counterexample) |
| Three-load order | stated as if known | stated as chosen by fit, so not a fully independent test (E10) |
| Numbers rounded | 6–11 significant figures (1.700594, 1.879385, Table 1 to 1e-11) | ≤ 4 significant figures in text; exact forms kept in equations (E9) |

## Moved to appendices or supplementary material

| Moved | Destination | Concern |
|---|---|---|
| Old §5 (Gie Cục I, Phương Độ records; Figs. 8–9) | Supplementary (Figs. S15–S16); one sentence kept in §6.2 (post-minus-pre up to 0.23 mm) | E8 |
| Old Table 1 (closed form vs FE), Table A.1, App. D (asymmetric three-span), main-span formula | Appendix A (condensed) and supplementary scripts | E9 |
| Old Table 2 | Table A.1, rounded | E9 |
| Old App. B (Monte Carlo), Table 7 (lab offset), §6.3 Eq. (20), quadrature details (Eq. 12, Table 3) | Supplementary; one sentence each in §3.2 and §6.1 | E9 |
| Old $O_m$ (Eq. 15) | removed from main text; multi-channel generalisation in supplementary (1B §1) | E9 |
| Old §6.4 speed calibration by interior zero crossing (untested proposal) | removed | E1 trigger list |
| Old §6.5 dynamic envelope (Table 9, Fig. 10) | two sentences in §6.1; analysis in supplementary | E9 |
| Old Table 6 (static consistency) | misfits in §5.1 text | E9 |
| Second girder (42 + 63 + 42 m) mention | removed | length |

## Not changed

Laboratory data (Table D.1), lab identification results (Table 2), AI-disclosure sentence (verbatim), author list and affiliation, declarations other than the data statement.

## Still not addressed (see open_items.md)

E1 laboratory blind-configuration and fixed-total-load tests (A2); E11 raw three-cycle data (C4); author-supplied Figs. 1 and 5 (C1); E8/E2 transverse model (D7); isolated-crossing probability (D8).
