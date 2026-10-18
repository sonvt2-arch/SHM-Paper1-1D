# Traceability of numeric values in `manuscript/schm/manuscript.md`

## Update 2026-10-18 (new facts from the authors' answers, `docs/08_cap_nhat_2026-10-18_tra_loi_tu_bai_MSSP.md`)

Source code ANS = authors' answers to the MSSP questionnaires (numbering of that questionnaire; mapped to Paper1 codes in docs/08). WP9 = `code/analysis/logs/wp9_truckweight_check.log` (`code/analysis/wp9_truckweight_check.py`). P7w = `code/analysis/logs/wp7b_peps_2506.log` (`python3 code/analysis/wp7b_peps.py --truck-t 25.06`; the original `wp7b_peps.log` is unchanged).

| Value or statement | Location | Source |
|---|---|---|
| Ten weighed trucks, mean 25.06 t; axle spacings 3.60 m, 1.35 m; track 1.85 m; 1.1 m apart transversely, 6.0 m longitudinally; continuous spans loaded from the ten trucks | §4.1 | ANS M3, M4 (data questionnaire), M1 (FEM questionnaire); Paper1 B4 |
| Daylight, hot and sunny; Mitutoyo dial gauges; positions by tape measure and paint, error < 20 cm each direction | §4.1, §4.4 | ANS C8, C9 (FEM questionnaire); Paper1 B6 |
| 25.06 t = 245.84 kN ("245.8 kN"); bias at ε0 = 0.02/0.05 mm: A N8 37.18/92.95 %, B N8 14.19/35.46 %, A N7 4.51/11.27 %, B N7 4.02/10.05 % → printed 37/93, 14/35, 4.5/11, 4.0/10 %; P_ε unchanged | Abstract ("35–93 %", "10–11 %"), §6.2, Table 8 (B N8 0.05 mm: 36 → 35 %), §8, cover letter | P7w Part A. Only the B N8 0.05 mm entry changes at printed precision (35.5 → 35.46 %) |
| Calibration and Table 5/6 values kept with nominal 5 + 10 + 10 t; weighed mean changes measured/model ratios by ≤ 0.003 and indicators by ≤ 0.002 | §4.2 (new sentences), Table 6 caption | WP9 scenarios 1–3: largest ratio change 1.0286 → 1.0261 (scenario 1) and 0.9767 → 0.9743 (scenario 2); largest N_m change 0.1815 → 0.1827 (A N8, scenario 3); α_B 0.7162 → 0.7176, k_FE 2.748 → 2.784 × 10⁷ only if the report FE used 25.06 t |
| Convoy shift ±0.20 m: N8 ≤ 0.6 % (A 0.43 %, B 0.61 %), N7 0.01 % | §4.4 | WP9 Part P |
| Authors performed the load tests and may publish the processed data | Data Availability | ANS C12 (data questionnaire): "Được phép công bố do tác giả là người thực hiện thử tải"; Paper1 B8, C6, D6 |
| Load test by the authors' team within inspection work of Công ty TNHH Tư vấn Đại học Xây dựng | Conflicts of Interest | ANS C12; Paper1 B9; consultant name from the Cầu Mây report (CMI) |

Word counts after this update: see `wp7b_checks.py` output in the hand-over note.

---

## SCHM version

The SCHM manuscript was derived from `manuscript/v2/manuscript.md` by reordering, renaming and tightening only. A two-way check of the sets of numerals (regular expression `\d+(\.\d+)?` over the whole file) found no number in the SCHM file that is absent from v2 and no v2 number that is missing from the SCHM file, so the v2 sources below still apply to every value. Moved text keeps its v2 source:

| Text moved in the SCHM version | New location | Source (unchanged) |
|---|---|---|
| Span-wise decomposition of the two-span constant (1.50–2.00, −0.125 to −4.00, 1.750/−0.750, 4/7, 1.732, 0.692, 1.000 → 1.040) | Appendix A, last paragraph | OLD l. 1895 ff. (old Table 12) and OLD l. 1921 (v1 table, Section 2 rows) |
| 60 FE comparisons, 7.5 × 10⁻¹² | Appendix D, first paragraph | WP2 §6 A; V3 sec. A |
| Main-span closed form with $\nu$ | Appendix D, first paragraph | WP2; `cm_3span_theory.py` |
| Two-span reduction of the optimum cubic | Appendix D, first paragraph | WP2 |

Figure values (new in the SCHM version): every number printed on Figs. 3, 7, 8, 9 and S1 is written by `code/analysis/schm_figures.py` to `manuscript/schm/figures/schm_figures_values.txt`, together with the quantity it represents. Cross-checks against the text:

| Figure value | Text / table value | Agreement |
|---|---|---|
| Fig. 7 / S1: N8 0.4L, $N_m$ 0.1815 (A), 0.4757 (B); $R_m$ 0.1832, 0.5556 | Table 5: 0.181, 0.476; 0.18, 0.56 | Same (rounding) |
| Fig. 7 / S1: N7 $N_m$ 0.2088 (A), 0.2340 (B); $R_m$ 0.5865, 0.7717 | Table 5: 0.209, 0.234; 0.59, 0.77 | Same |
| S1: mid side span $N_m$ 0.1051 / 0.3772, $R_m$ 0.1113 / 0.4888 | Table 5: 0.105, 0.377, 0.11, 0.49 | Same |
| S1 bounds 0.0228…0.4461, −0.0659…0.3753, 0.1448…0.2628 | Table 5: 0.023…0.446, −0.066…0.375, 0.145…0.263 | Same (from `wp3_Cm_summary.csv` norm_min/max) |
| Fig. 7 calibration B: α 0.7162, k 1.1991 × 10⁸; k_FE 2.7482 × 10⁷ | §4.2: 0.716, 1.2 × 10⁸, 2.7 × 10⁷ | Same |
| Fig. 7 C_m: 4.37612e−5, 1.14702e−4, 3.60969e−4, 4.04606e−4 m²/kN | Table 8 | Same |
| Fig. 7a: n 2.9428, L_v 44 m | §4.2: 2.943, 44 m | Same |
| Fig. 3 marker: β 1.636364, N 0.163223 | §4.3: 1.636, 0.163 | Same |
| Fig. 8: tare −5.6 … +6.2 % except PD N1 raw −36.4 %; cubic −1.2 … +3.6 %; HP 0.1 Hz −44.4 … −82.1 %; HP 0.5 Hz −97.6 … −102.3 % | §5: "within about 6 %", 36.4 %, +1.7 to +3.6 % (GC) and −1.2 to +0.1 % (PD), "−44 to −83 %", "about −100 %" | The −83 % end of the §5 range comes from a non-major event (Gie Cuc N1 crossing 3, −83.3 % in `wp4.log` l. 37) that Fig. 8 does not show; the plotted complete crossings reach −82.1 %. Text kept as in v2 (WP4 doc l. 42) |
| Fig. 9: I_LP/I 0.9999–1.0006; residual net/abs 0.000–0.009 | §5: 0.9999 to 1.0010; 0.001–0.022 | Figure shows one record per span, a subset of the §5 ranges (all complete events) |

Word counts (SCHM): abstract 236 words; main text 9221 words; 23 numbered equations, all cited (`python3 code/analysis/wp7b_checks.py manuscript/schm`).

---

## v2 traceability (carried over)

This file carries over the v1 table (`manuscript/structures/traceability.md`) and adds a v2 block at the top. Rows of the v1 table that refer to text removed in v2 are marked *(removed in v2)*. Reference numbers in v2 differ from v1: old [28]–[40] are now [30]–[42], old [41]–[47] are now [45]–[51]; new [28] Helmi 2014, [29] Lydon 2016, [43] Zhou 2026, [44] Ghali 2017.

Abbreviations for sources:
- **OLD** = `manuscript/text/CSHM-D-26-00881.txt` (previous JCSHM manuscript; line numbers of that file).
- **WP2** = `docs/wp2_three_span_theory.md`; **V3** = `code/analysis/logs/verify_3span.log`.
- **WP3** = `docs/wp3_continuous_bridges.md`; **L3** = `code/analysis/logs/wp3_run.log`; **R3** = `code/analysis/results/wp3_Cm_summary.csv`; **CMI** = `data/bridges/cau-may/INVENTORY.md`; **CMD** = `data/bridges/cau-may/cau-may_main_static_deflection.csv`; **CMS** = `data/bridges/cau-may/section_properties.csv`.
- **WP4** = `docs/wp4_dynamic_records.md`; **L4** = `code/analysis/logs/wp4.log`.
- **NOV** = `docs/novelty_matrix.md`; **REF** = `docs/reference_check.md`.
- **DER** = simple arithmetic on sourced values, done in this session (shown).
- **P7** = `code/analysis/logs/wp7b_peps.log` (script `code/analysis/wp7b_peps.py`, run in WP7b); **CHK** = `code/analysis/wp7b_checks.py` (word counts, highlights, equation citations).
- **CR** = Crossref API record of the DOI (checked 2026-10-11).

Automatic check (v1 only; the script was in a session scratchpad and is not in the repository, so this count is not reproducible): `xcheck.py` extracted 491 distinct numbers from the manuscript body (title to end of figure captions) and searched each verbatim in all the sources above. Only 8 were not found verbatim: citation ranges (14,15; 44,45; 46,47), the laboratory masses 2145, 2550, 4684, 5100 (OLD line 979 writes them with a thin space, "2 145 g"), and the postcode 11618 (author-address convention of the viet-tu-nhien rules, v3.3).


## v2 additions and changes (WP7b)

| Value in v2 | Location | Source |
|---|---|---|
| Calibration A: $k_\mathrm{FE}$ = 2.7 × 10⁷ (2.748e7), FE misfit −4.2/+3.7 %; α at k_FE = 1.088, misfit −4.6/+5.0 % | §4.2, §4.4 | L3 line 2 |
| Calibration B: α = 0.716, k = 1.2 × 10⁸ (1.199e8) kN m/rad, misfit −2.8/+2.9 % | Abstract (implicit), §4.2, Table 5 caption, Fig. 7 caption | L3 line 2 |
| N8 0.4L: A 0.181 (neg/pos −0.817 → 82 %, R_m 0.18); B 0.476 (neg/pos −0.444 → 44 %, R_m 0.56) | Abstract (0.18/0.48), §4.3, Table 5, §8, highlight 5 | L3 lines 56, 59; `results/wp3_Cm_table.csv` rows varEI_Lv44 kFE/kMeas (`norm_192EICm_L4` 0.181497, 0.475719; `net_over_pos` 0.183207, 0.555591) |
| N8 mid side (alt.): A 0.105 (R_m 0.11), B 0.377 (R_m 0.49) | Table 5 | L3 lines 57, 60; CSV `net_over_pos` 0.111298, 0.488764 |
| N7: A 0.209 (R_m 0.59, 41 %), B 0.234 (R_m 0.77, 23 %); "0.21–0.23" | Abstract, §4.3, Table 5, §8, highlight 5 | L3 lines 58, 61; CSV `net_over_pos` 0.5865, 0.771729 |
| Pinned/fixed bounds 0.023 … 0.446 ("0.02–0.45"), −0.066 … 0.375, 0.145 … 0.263 | Table 5, §4.3 | L3 lines 74–76 |
| α = 1.088 at k_FE: N8 index 0.160, cancellation 83 % | §4.3 | P7 Part B |
| k = 0.5/2 × k_FE: N8 0.124/0.248; N7 0.224/0.191; ∂lnC_m/∂ln k = +0.51 (N8), −0.12 (N7, −0.115) | §4.3 | P7 Part B |
| C_m: A N8 4.38e−5, N7 3.61e−4; B N8 1.15e−4 (1.14702e−4), N7 4.05e−4 (4.04606e−4) m²/kN; ratios 8.2 / 3.5; factor 2.6 (N8, B/A); 12 % (N7, B/A) | §4.3, §4.4, Table 8 | CSV; P7 Part A (8.25, 3.53); DER 1.14702/0.43761 = 2.62, 4.04606/3.60969 = 1.12 |
| Model B deflections 5.40, 15.87 mm; measured/model B 1.029, 0.972 | Table 6, §4.4 | L3 static block, `varEI_Lv44 kMeas` lines |
| P_ε: A N8 91.4/228.5 kN, B N8 34.9/87.2 kN, A N7 11.1/27.7 kN, B N7 9.9/24.7 kN (ε0 = 0.02/0.05 mm); bias for 25 t (245.25 kN): 37/93 %, 14/36 %, 4.5/11 %, 4.0/10 % | Abstract (36–93 %, 10–11 %), §6.2, Table 8, §8 | P7 Part A |
| L_tot = 200 m; wheelbase 4.95 m adds 2.5 % | §6.2 | P7 Part A; wheelbase 3.60 + 1.35 m (CMI §2) |
| Near-blind band edges: two-span 1.385061–1.524695 ("1.385–1.525"); three-span 1.621399–1.775021 ("1.775") | §2.2, §2.3, §7.1, §8 | P7 Part E |
| β = 2: |N_m| = 0.875 at mid side span | §2.3 | P7 Part E (DER μ = 2.25) |
| ρ_L = 2: |N_m| = 2.0 | §2.2 | Table 1 (−2.00000000) |
| Strain blind point 0.75L (equal two-span, uniform load) | §2.1 | DER: M(x) = 3qLx/8 − qx²/2 = 0 at x = 3L/4 |
| Lab ratios measured/analytical (trapezoidal): 1.010, 1.016, 1.017 (1.0099, 1.0161, 1.0170); SLM residual 0.61/0.70 % | §3.3, §7.2 | P7 Part C; DER 1.0161/1.0099 = 1.0061, 1.0170/1.0099 = 1.0070 |
| Three-load order 2550 g leading, +500 mm, +250 mm; rms 0.030 vs 0.55 mm | §3.1 | P7 Part C (0.0298, 0.5529 mm) |
| Intervals 20/21/23 | §3.2 | P7 Part C |
| 400 mm overhang | §3.1, App. A | DER 5400 − 2 × 2500 |
| SLM offset residual 58 % of BPM term, 42 % reduction | §6.1 | DER 0.7297/1.2596 = 0.579 |
| Table 10 combined 0.4–1.0 %, 2.3–10.5 %, 5.6–18.5 % (RSS) | §6.6 | P7 Part D |
| Field records: post-minus-pre 0.0–0.1 mm (Gie Cuc), 0.17–0.23 mm (PD N2); quiet-level scatter 0.01–0.13 mm; 0.1 mm steps (raw Gie Cuc) | §5 | WP4 l. 9, l. 45 |
| Channel ratio 0.67 to 5.15 | §5 | WP4 l. 80 |
| 1.1 × 10⁻⁴ explanation (trapezoidal integration of nodal IL on 0.1 m mesh vs consistent loads) | §4.2 | `code/analysis/wp3_fe.py` `Bridge.Cm` (np.trapezoid) and `Bridge.uniform` (consistent loads); 10 elements/m |
| Zhou et al. 2026 content | §1, §4.4 | CR 10.1155/stc/1361157 abstract |
| Helmi et al. 2014: Winnipeg slab-on-girder, Ojio–Yamada area method within 5 % with accurate speeds | §1 | CR 10.1007/s13349-014-0076-5; Springer abstract page |
| Lydon et al. 2016: seven-span slab-and-girder bridge; negative GVW from the asymmetry-coefficient method | §1 | CR 10.1007/s13349-015-0119-6; full text (scispace PDF of the UCD repository version), §1.2 |
| [37] Huang & Lu: M-value strain feature, two-span continuous bridge case study | §1 | CR abstract 10.1177/14759217251376931 |
| [42] Shen et al.: mid-span visual deflection, end-mounted acceleration, calibrated deflection IL | §1 | CR abstract 10.1142/s0219455427503664 |
| [39] Chaudhary et al.: five-span continuous bridge | §1 | Kuwait University repository abstract of 10.1016/j.istruc.2025.108298 |
| Owner Hai Duong PMU; tester Công ty TNHH Tư vấn Đại học Xây dựng | Data availability | CMI l. 36 |
| Abstract 236 words (240 raw); main text 9563 words; highlights 73–79 characters | — | CHK |

Removed in v2: "about fourteenfold" (replaced by the bound 0.02–0.45), "about eight times" (replaced by 8.2 / 3.5), "EI_eff/EI_design = 1.09; 1.07–1.08; 7–9 %" (replaced by both α values and per-gauge ratios), "1.86 % at 2250 mm" (sentence cut), Section 5 speeds (27–36, 30–40, 47–62 km/h), 26–33 % scatter and the PD N1 lobe values (40 %, 25 %) (moved to supplementary material), "about 37 %" (replaced by 58 % / 42 %), "2–10 % on a bridge" sentence of §6.2 (the value remains in Table 10), Table 9 combined values 0.5–1.1 / 3–11 / 6–19 % (recomputed), multi-sensor variance formula of §7.1.

Verification-report items N1–N5: N1, 0.181 is the rounding of 0.181497 in `wp3_Cm_table.csv` (the summary CSV prints 0.1815); N2, "0.30" is V3 l. 107 (−0.30059) and WP2 l. 79; N3, "draft l. 160" is `docs/wp2_three_span_theory.md` l. 160 and "draft §5" is `docs/wp4_dynamic_records.md` l. 76–80; N4, see the note on `xcheck.py` above; N5, the 3.6 × 10⁷ upper value is L3 line 1 (Lv40, 3.615e7).

## v1 table (carried over)

## Abstract and Highlights

| Value | Source |
|---|---|
| $(3+\sqrt{33})/6 = 1.45743$ | OLD Eq. (11c), l. ~609–663; Table 1 l. 607 |
| $6\beta^3-15\beta-4=0$, 1.700594 | WP2 §3 table l. 53; V3 sec. B ("beta_crit … 1.700593981702490") |
| $2\cos(\pi/9) = 1.879385$ | WP2 l. 54; V3 sec. B ("1.879385241571817") |
| 1.19 %, 0.70 % | OLD Table 5 l. 1069 ff. |
| 82 % | WP3 §3.1 finding 1; R3 `negpos_base_kFE = -0.8168` |
| about fourteenfold *(removed in v2)* | WP3 l. 69 (7.3e−6 vs 1.0e−4 m²/kN); R3 `Cm_base_pinned 7.264e-06`, `Cm_base_fixed 0.0001016` (ratio 13.99, DER) |
| 55 + 90 + 55 m | CMI §1; WP3 §1 |

## Section 1

| Value | Source |
|---|---|
| 2012, four overloaded trucks | OLD l. 85 |
| five-span continuous bridge [37] | NOV row 10 |

## Section 2

| Value | Source |
|---|---|
| Table 1 (all entries, 11 significant figures) | OLD Table 1, l. 607 |
| $\mu_\mathrm{crit} = 5/3$; Eqs. (6)–(7) | OLD Eqs. (11b)–(11c) |
| 1.039895 | OLD l. 609–663 |
| 10 % of maximum at 0.9L1 | OLD l. 1575 |
| 1.50–2.00; −0.125 to −4.00; 1.750, −0.750; 4/7 | OLD l. 1895 ff. (Table 12) and Section 2.3 text |
| 1.750→1.732, 0.750→0.692, 1.000→1.040 | OLD l. 1921 |
| ρL = 1.6: −0.78, +0.33, 2.14 | OLD l. 1611 |
| ρL = 1.45: 0.021; ξ = 0.266: 0.233 | OLD l. 1621–1623 |
| near-blind 0.2, "five times" | OLD l. 1595 |
| μ = 4/5; 1.3 times two-span value | WP2 l. 34 and l. 160 |
| 60 comparisons, 7.5 × 10⁻¹² | WP2 §6 A; V3 sec. A (max relerr 7.5e-12 at β = 1.8, ρ = 0.7) |
| $\rho_{EI,\mathrm{crit}} = 3\beta(2\beta^2-5)/4$ | WP2 §3 table |
| 1.621399, $30\beta^3-69\beta-16=0$ | WP2 l. 55 |
| Eq. (10) $6\beta^3/(15\beta+4)$ | WP2 §2; V3 sec. C |
| cubic for ξ*; 0.964706 | WP2 §3 table l. 57–58; V3 sec. B |
| Table 2 (all values); FE slope ≤ 3.6 × 10⁻⁷ | WP2 §3 table l. 62–69; V3 sec. B |
| ∂μ/∂ρ ∝ 3β − 2β³; √(3/2) | WP2 l. 81 |
| 0.587–0.592 (L3/L2 0.3–0.6); Appendix D list 0.589774 … 0.461410; 9.2 × 10⁻¹² | WP2 §4 l. 91; §6 D; V3 sec. D |
| 1 % span → 4 % load | OLD Section 2.4 |
| $O_m = 2\sqrt{44765}/1279 = 0.331$ | OLD l. 845 |
| $R_m = 4/7$ for equal two-span | DER: $C_m/C_m^+ = 1.000/1.750$ (OLD Table 12) |

## Section 3

| Value | Source |
|---|---|
| 5400 mm, 2500 mm, 25 × 25 × 2.03 mm, I = 16 529.8 mm⁴, E = 200 GPa, EI = 3.3060 × 10⁹ N mm², Cm = 61.541 mm²/N | OLD l. 950–960 |
| shear 8 × 10⁻⁴, span/depth 100 | OLD l. 899 |
| LVDT 0–50 mm, 0.005 mm, TDS-303, Δx = 250 mm, three cycles | OLD Section 3.2 |
| 4.143 kg (40.64 N); 2145/4684 g; 2550/5100/5100 g; 250/500 mm; 5000/5250/5750 mm | OLD l. 979 ff.; 40.64 N from Fig. 4/Table 2 caption |
| 0.0125 mm, 0.43 %, 2.5 × resolution | OLD l. 1015 |
| 1.86 % at 2250 mm | OLD l. 1019 |
| Table 3 (2501.19, 2488.68, 2501.85, 2513.43; −0.500, +0.027, +0.49 %) | OLD Table 3 l. 1041 |
| Table 4 (66.99, 67.73, 67.40, 125.08, 126.57, 125.95 N; 4168.15, 7788.93 mm²; +1.10, +0.61, +1.19, +0.70 %) | OLD Table 5 l. 1069 |
| 1.00489; 2513.43/2501.19 | OLD l. 1091 |
| 0.50 %, 1.6 %, 1.10 → 1.61 % | OLD l. 1105 |
| $I_y = 62.229P$, R² = 0.99998, 1.12 % | OLD l. 1115 |

## Section 4 (Cầu Mây)

| Value | Source |
|---|---|
| DT389, Kinh Mon River, Hai Duong; balanced cantilever; 2.40/5.40 m | CMI §1 |
| β = 90/55 = 1.636 | WP2, WP3; CMI ("L2/L1 = 1.636") |
| I = 5.482 / 59.612 m⁴; Ec = 36 057 MPa; f'c = 45 MPa | CMS rows `Iyy_vertical`, `Ec`; WP3 §1 |
| T6/T7 monolithic; T5/T8 pot bearings | CMS `supports`; WP3 §1 |
| June 2020 | CMI §1 (logger 19/06/2020; report 30/07/2020) |
| 5 + 10 + 10 t nominal, 3.60 m, 1.35 m, 6.0 m, two abreast ("about 25 t" and "no weighbridge values" replaced on 2026-10-18 by the weighed mean 25.06 t, see the 2026-10-18 block) | CMI §2; WP3 §1; ANS M3, M4 |
| Scheme III 4 trucks 100 t, Scheme IV 6 trucks 150 t; axle positions | CMI §2; WP3 §1 row "CM truck positions"; L3 `[positions]` |
| 0.4L = 22 m | WP3 §1; CMI §3 |
| eccentric outer wheel 0.6 m from kerb; three repetitions | CMI §2 and §4 |
| 5.55 vs 5.93 mm; 15.42 vs 16.70 mm | WP3 §3.2 table; L3 static block |
| individual readings 5.22–5.91, 14.62–16.67 mm | CMD |
| 10 elements/m; parabolic depth; n = 2.943; Lv = 44 m (40–45) | WP3 §2; L3 `[model]` |
| k_FE = 2.7 × 10⁷ (2.5–3.6 × 10⁷) kN m/rad; misfit −4.2 % to +3.7 % | L3 `[calib] CM varEI_Lv44 … (FE misfit % [-4.2, 3.7])`, Lv40/45 lines |
| 1.1 × 10⁻⁴ | L3 `[check] max |C_m(IL area)/w(uniform) - 1| … 1.07e-04` |
| polygon −0.3/−0.5 % (A), −5.8/−2.6 % (I) | CMS polygon rows; L3 `[check] CM … polygon` |
| 0.163 (uniform EI, mid side); 0.921; ξ* 0.2994, 0.332 | WP2 §3 tables; V3 sec. B, C |
| span-wise 1.870395, −1.902566, 0.195395; (+, −, +); main 0.754630, 0.30 | V3 sec. C |
| Table 5 (0.287, 0.181, 0.023…0.446, 0.82, 0.18; 0.163, 0.105, −0.066…0.375, 0.89, 0.11; 0.755, 0.209, 0.145…0.263, 0.41, 0.59) | R3; L3 "Range of normalised C_m"; WP3 §3.1 table |
| 7.3 × 10⁻⁶ and 1.0 × 10⁻⁴ m²/kN | R3 `Cm_base_pinned_m2_per_kN`, `Cm_base_fixed_m2_per_kN` (N8 0.4L) |
| 3.61 × 10⁻⁴ (N7), 4.38 × 10⁻⁵ (N8) m²/kN | WP3 §3.1 "Absolute C_m"; R3 |
| "about eight times" | DER: 3.61e−4 / 4.38e−5 = 8.2 |
| Table 6 (5.69, 17.32 mm; 0.936, 0.923; 0.977, 0.890; 7.18…2.75; 22.99…8.34) | WP3 §3.2; L3 static block (`kFE`, `pinned`, `fixed` lines) |
| EI_eff/EI_design = 1.09 (1.088) | L3 `alpha at k_FE = 1.088`; WP3 §3.2 |
| 1.07–1.08 | WP3 §3.2 (1/0.936, 1/0.923) |
| 7–9 % | DER from 1.07–1.09 (replaces the two-bridge range 4–11 % of WP3, because Thái Bình is excluded) |
| 2.05 mm spread | WP3 §3.2 linearity bullet (b) |

## Section 5 (field records)

| Value | Source |
|---|---|
| 25.7 m; 17.5 m; SDA-830C, 200 Hz, 15 s; seven complete crossings | WP4 §1, §3.1; INVENTORY files of gie-cuc-1 / phuong-do |
| channel ratios 1.00, 3.25, 5.15, 0.67, 1.34; up to 7.7 times | WP4 §3.4 |
| about 6 %; +1.7 to +3.6 %; −1.2 to +0.1 % | WP4 §3.2 table and l. 76 |
| 2.06 mm, 18 %, −36.4 % | WP4 §3.2 |
| +7, −16, −60, +34, −170 % | WP4 §3.2 bullet (whole record) |
| −44 to −83 %; about −100 % | WP4 §3.2 table |
| 2 Hz; 5.2–6.0 Hz; 0.9999–1.0010; 0.001–0.022; 3–16 % | WP4 §3.3 |
| 27–36 km/h; 30–40 km/h; 47–62 km/h | WP4 §3.1 |
| 26–33 % | WP4 §3.4 and l. 80 *(removed in v2)* |
| PD N1 lobe: 40 %, 25 % | WP4 §3.5 |

## Section 6

| Value | Source |
|---|---|
| −0.5000 %; 300 mm −0.110 %; 375 mm +0.249 %; 0.4–0.75 % | OLD l. 1235–1257 |
| (1.2596 − 1.9893) mm⁻¹ | DER correction of OLD l. 1269 (0.1260 − 0.1989 was a decimal error): 5250/4168.15 = 1.2596; 5000/2513.43 = 1.9893; flagged in `docs/rejection_evidence.md` §2 (A3) |
| about 37 % | OLD l. 1269 (unchanged by the decimal correction: (1.9893 − 1.2596)/1.9893 = 0.367) |
| Table 7 (all) | OLD Table 6 l. 1303 |
| 0.4–1.0 %; 2–10 % | OLD l. 1319, 1327 |
| 200 000; 0.07 %; 60 %; 1.47; 2.11 %, 3.09 %, 2.12 %; five reference crossings | OLD l. 1341–1440 |
| interior zero crossing; factor of two | OLD Section 4.4 |
| 1.464 kg/m; 2 %; 11.942 Hz; 1000 → 16 000 steps, 0.002 points; 47 speeds; 0.6–120 | OLD l. 1653–1675 |
| Table 8 (17.6 … 0.08) | OLD Table 9 l. 1681 |
| ≥ 8 → ≈1 %, ≥ 4 → < 4 %; 2.5, 15 % | OLD Eq. (22) l. 1697 |
| 39 % at 1.5; four periods halves error; 0.5–5 % damping | OLD l. 1703–1711 |
| 0.33 % at 11.9; 1.95 % at 3.0; 0.5–1.5 m | OLD l. 1763 |
| 10–30 m, 50–80 km/h, 7–20 | OLD Table 10 and l. 1747 |
| Table 9 (all entries); 0.61, 0.70 % | OLD Table 11 l. 1789 ff. |

## Section 7 and 8

| Value | Source |
|---|---|
| 2500 mm and 3644 mm | OLD l. 2101 |
| l/20; Nrep ≥ 5; Tcr/T1 ≥ 8 | OLD Section 5.5 |
| Thái Bình 42 + 63 + 42 m; −11 %, +22 %, −12 % | WP3 §3.2; L3 `[calib] TB … (FE misfit % [-11.1, 22.2, -11.8])` |
| $(\mathbf c^\mathrm T\boldsymbol\Sigma^{-1}\mathbf c)^{-1}$ | OLD Section 5.3 |

## Appendices

| Value | Source |
|---|---|
| Eq. (A.1), 13P/32, 11P/16, −3P/32 | OLD l. 291 |
| Eq. (A.2) | OLD Eq. (6) (garbled text export); branches re-derived symbolically in this session (SymPy, reciprocity with unit load at l/2; R_B = 11/16) and checked against OLD Table 2 (e.g. x = 1.5l gives −1.1255 mm for P = 40.64 N) |
| 2.875, 71.9 %, 0.480l, 72.1 % | OLD l. 377 |
| μ = 0.750 at ρL = 1/2, 1 at equal spans, 3 at ρL = 2 | OLD l. 589 |
| Table A.1 | OLD Table 8 l. 1629 |
| Table B.1 | OLD Table 7 l. 1365 |
| Table C.1 | OLD Tables 2 and 4 (l. 1001, 1053) |

## Declarations

| Item | Source |
|---|---|
| CRediT roles | OLD l. 2273 |
| Funding sentence | OLD l. 2265 |
| AI declaration (verbatim) | OLD l. 2293 ff. |
| Acknowledgement | OLD l. 2305 (Department → Faculty, per viet-tu-nhien rule v3.3) |
| References | OLD list l. 2311 ff. corrected per REF ([9] → Al-Qadi et al. 2016, [10] → FHWA 2000, [33] → Vietnamese title marked); new entries from NOV §1 (Crossref metadata) |
