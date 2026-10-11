# Traceability of numeric values in `manuscript.md`

Abbreviations for sources:
- **OLD** = `manuscript/text/CSHM-D-26-00881.txt` (previous JCSHM manuscript; line numbers of that file).
- **WP2** = `docs/wp2_three_span_theory.md`; **V3** = `code/analysis/logs/verify_3span.log`.
- **WP3** = `docs/wp3_continuous_bridges.md`; **L3** = `code/analysis/logs/wp3_run.log`; **R3** = `code/analysis/results/wp3_Cm_summary.csv`; **CMI** = `data/bridges/cau-may/INVENTORY.md`; **CMD** = `data/bridges/cau-may/cau-may_main_static_deflection.csv`; **CMS** = `data/bridges/cau-may/section_properties.csv`.
- **WP4** = `docs/wp4_dynamic_records.md`; **L4** = `code/analysis/logs/wp4.log`.
- **NOV** = `docs/novelty_matrix.md`; **REF** = `docs/reference_check.md`.
- **DER** = simple arithmetic on sourced values, done in this session (shown).

Automatic check: `scratchpad/xcheck.py` extracted 491 distinct numbers from the manuscript body (title to end of figure captions) and searched each verbatim in all the sources above. Only 8 were not found verbatim: citation ranges (14,15; 44,45; 46,47), the laboratory masses 2145, 2550, 4684, 5100 (OLD line 979 writes them with a thin space, "2 145 g"), and the postcode 11618 (author-address convention of the viet-tu-nhien rules, v3.3).

## Abstract and Highlights

| Value | Source |
|---|---|
| $(3+\sqrt{33})/6 = 1.45743$ | OLD Eq. (11c), l. ~609–663; Table 1 l. 607 |
| $6\beta^3-15\beta-4=0$, 1.700594 | WP2 §3 table l. 53; V3 sec. B ("beta_crit … 1.700593981702490") |
| $2\cos(\pi/9) = 1.879385$ | WP2 l. 54; V3 sec. B ("1.879385241571817") |
| 1.19 %, 0.70 % | OLD Table 5 l. 1069 ff. |
| 82 % | WP3 §3.1 finding 1; R3 `negpos_base_kFE = -0.8168` |
| about fourteenfold | WP3 l. 69 (7.3e−6 vs 1.0e−4 m²/kN); R3 `Cm_base_pinned 7.264e-06`, `Cm_base_fixed 0.0001016` (ratio 13.99, DER) |
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
| μ = 4/5; 1.3 times two-span value | WP2 l. 34 and draft l. 160 |
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
| 5 + 10 + 10 t, about 25 t, 3.60 m, 1.35 m, 6.0 m, two abreast | CMI §2; WP3 §1 |
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
| about 6 %; +1.7 to +3.6 %; −1.2 to +0.1 % | WP4 §3.2 table and draft §5 |
| 2.06 mm, 18 %, −36.4 % | WP4 §3.2 |
| +7, −16, −60, +34, −170 % | WP4 §3.2 bullet (whole record) |
| −44 to −83 %; about −100 % | WP4 §3.2 table |
| 2 Hz; 5.2–6.0 Hz; 0.9999–1.0010; 0.001–0.022; 3–16 % | WP4 §3.3 |
| 27–36 km/h; 30–40 km/h; 47–62 km/h | WP4 §3.1 |
| 26–33 % | WP4 §3.4 and draft §5 |
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
