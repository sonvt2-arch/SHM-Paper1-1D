# WP3: Cầu Mây and Thái Bình continuous box girders: load observability (C_m) and a static consistency check

Date: 2026-10-11. Role: Bridge Modeller (WP3).
Scripts: `code/analysis/wp3_sections.py`, `code/analysis/wp3_fe.py`, `code/analysis/wp3_run.py`.
Log: `code/analysis/logs/wp3_run.log`.
Tables: `code/analysis/results/wp3_*.csv`.
Figures: `figures/wp3_influence_lines.png`, `figures/wp3_Cm_normalised_bar.png`, `figures/wp3_EI_profiles.png`.
Section data: `data/bridges/cau-may/section_properties.csv`, `data/bridges/lang-am/section_properties.csv`.

**Scope.** This work applies the observability criterion and runs a static consistency check on test data that already exist. It does **not** validate the dynamic deflection-integral theorem. Both bridges were tested only with parked convoys, and each test gives one reading per measuring point per load case.

## 1. Data sources (each input and where it comes from)

| Input | Value | Source |
|---|---|---|
| CM spans, system | 55+90+55 m; T6/T7 monolithic, T5/T8 movable pot bearings; pile caps modelled as elastic springs in the designer's model | Report PDF sec. 1; LRFR PDF sec. 3.3.1 (Drive `1HNyul9T5k12wWprgo9gNZMh-w0qRNyWw`) |
| CM section properties | mid-span A = 7.233 m², I_yy = 5.482 m⁴; pier face A = 14.437 m², I_yy = 59.612 m⁴ (z(+)+z(−) = 2.40 / 5.40 m, so I_yy is vertical bending) | LRFR PDF p.5 |
| CM cross-section dimensions | full mid-span and pier-face drawings (webs 400/600 mm, bottom slab 250/800 mm, bottom width 5550/4800 mm) | LRFR PDF p.3 |
| CM E | E_c = 36,057 MPa (f'c = 45 MPa) | LRFR PDF p.4 |
| CM trucks | 3 axles, 5+10+10 t (nominal, "about 25 t"); axle spacings 3.60 and 1.35 m; 6.0 m clear axle gap between trucks; two trucks side by side | Report sec. 2.1.1.1 (Hình 2.1); weighbridge values [NEED VALUE] |
| CM truck positions | Side span: middle axle of the first row at 0.4L = 22 m from the end-pier axis, 2 rows. Centre span: middle axle of row 2 at mid-span, 3 rows | Test plan `06 - De cuong KDCL cau May.doc` sec. V.4.3, text rule plus Hình 14–16 (rendered and checked) |
| CM sensors | N8 at 0.4L, 22 m from the span end (the tables label it "mid-span"); N7 at mid-span | Plan V.4.3; report sec. 2.1.1.4c |
| CM measured / MIDAS | N8 −5.32…−5.91 mm vs −5.93; N7 −14.62…−16.67 mm vs −16.70 | `04 - Đo tĩnh - Cầu chính.xlsx` sheet V; `cau-may_main_static_deflection.csv` |
| TB spans, system | 42+63+42 m; T12/T13 rigidly fixed to the girder; pot bearings at the end piers. The design note writes "T10–T14"; the test report writes T11–T14 | Design note `T.Minh Thai Binh - 10-9-2020.doc`, "Phần cầu chính" |
| TB geometry | depth 4.0 m (pier) / 2.0 m (mid-span and girder ends), parabolic soffit; top width 11.7 m; bottom width 4.8 / 5.759 m; webs 600 / 250 mm; top slab 220 mm (flange tip) / 250 mm (in box); 2×7 segments of 3.5 m per pier | Design note, same section |
| TB f'c | 45 MPa for girder and main piers, so E_c = 36,057 MPa by the same TCVN 11823 formula (derived) | Design note concrete table, items 2–3 |
| TB trucks | 10 four-axle trucks, 29.20–31.72 t (mean 30.53 t); spacings 1.80 / 3.00 / 1.35 m; two side by side. Axle loads and which truck went where: [NEED VALUE] | Report "Tải trọng"; `test_trucks.csv` |
| TB truck positions | Scheme 4: axle 3 of the leading truck at 16.8 m from T11, 6.0 m axle gap. Scheme 5: 3 trucks, gaps 6.0 m, middle truck centred at mid-span. Scheme 6: front axle of the first truck at 16.8 m from T14 | Report PDF (Drive `1J4YgdZ3y7lATFSOsgt7ZUXEHokAyLOCP`) p.22–24, Hình 8, 11, 12. The printed dimensions were read and the axle locations checked by pixel measurement (20.0 px/m, ±0.1 m) |
| TB measured / FE | N12 3.15–3.28 vs 3.58 mm; N13 6.01–6.04 vs 6.25 mm; N14 3.54–3.68 vs 3.82 mm | Report Bảng 34; `thai_binh_main_bridge_static_deflection.csv` |

Not available or not readable: the CM MIDAS model (inside the 151 MB `.rar`) and the TB drawings (`TẬP 2-2` PDF of 289 MB, and the DWG files). Both exceed the 10 MB download limit of the Drive connector or cannot be parsed. The TB "bản tính kết cấu" (Tập 2.2.2) is not in the folder.

## 2. Model and assumptions

- **Beam model.** 2D Euler–Bernoulli FE written in numpy/scipy (`wp3_fe.py`), 10 elements/m, with consistent loads. The vertical supports at the four piers are rigid. Each inner pier carries a rotational spring k: k = 0 gives a continuous beam (pier pinned), k = ∞ fixes the rotation fully.
- **C_m.** C_m is the area under the deflection influence line at the sensor over the three spans. As a check, the same number was computed as the deflection under a unit uniform load; the two agree to 1.1e−4 in every case. The approach spans are simply supported behind expansion joints, so they add nothing to C_m.
- **Normalisation.** The index is 192·EI_ref·C_m/L⁴, with L the span that contains the sensor and EI_ref = E·I_mid (the mid-span section, the minimum of EI). The near-blind test is |index| < 0.2. We also report the normalisation-free cancellation ratio C_m/A⁺, where A⁺ is the positive part of the influence-line area.
- **EI(x).** The depth follows a parabola, h(d) = h_mid + (h_p − h_mid)(1 − d/Lv)², for distances d < Lv from an inner pier axis. Then I = I_mid·(h/h_mid)ⁿ, with n fitted to the two known sections: n = 2.943 for CM and 3.007 for TB.
  - Lv is not given [NEED VALUE]. Values used: CM 44 m (bracket 40–45 m); TB 30.5 m (bracket 28–31.5 m), which comes from 7 × 3.5 m segments plus an assumed K0 and closure.
  - The pier diaphragm is ignored. This is a small and conservative omission.
- **CM I values** come from the designer's table (LRFR p.5). As a check, the polygon routine reproduces them from the p.3 drawing to within A −0.3/−0.5 % and I −5.8/−2.6 %.
- **TB I values** were computed with the same polygon routine from the design-note dimensions. Missing dimensions were filled with Cầu Mây values and marked [NEED VALUE]: bottom slab, flange root and haunches.
  - Baseline: bottom slab 0.25/0.80 m, giving I_mid = 3.177 m⁴ and I_pier = 25.53 m⁴.
  - Variant: bottom slab 0.21/0.59 m (Cầu Mây thickness/depth ratio), giving 2.941 / 23.74 m⁴.
- **Pier stiffness** cannot be built from data because pier dimensions are not in the files read. We therefore use three cases:
  - (i) bracket the result with k = 0 and k = ∞;
  - (ii) calibrate **k_FE**, the single k that makes the design-EI model reproduce the deflections of the report's own FE model. This is our best estimate of the "design model" a BPM user would adopt;
  - (iii) jointly fit EI scale α and k to the measured deflections, as a diagnostic only.
- **Transverse behaviour** is ignored. The 2D beam carries the total load of the two trucks in each row. The measured value is the mean of the three gauges for the centric and eccentric cases (six readings).
- **TB axle loads** are unknown. The baseline splits each truck's gross weight equally over its four axles and uses the mean gross weight. The hard bounds put each truck's whole gross weight on the axle with the lowest (or highest) influence ordinate and use the lightest (or heaviest) n trucks.

## 3. Results

### 3.1 Observability index (`wp3_Cm_summary.csv`, Fig. `wp3_Cm_normalised_bar.png`, `wp3_influence_lines.png`)

| Sensor | Const. EI, pinned (WP2 style) | Var. EI, **k_FE** | Var. EI, pinned … fixed (all variants) | neg/pos at k_FE | C_m/A⁺ at k_FE |
|---|---|---|---|---|---|
| CM N8 at 0.4L (measured point) | 0.287 | **0.181 (near-blind)** | 0.023 … 0.446 | −0.82 | 0.18 |
| CM N8 mid-span (alt.) | 0.163 | 0.105 | −0.066 … 0.375 | −0.89 | 0.11 |
| CM N7 mid-span | 0.755 | 0.209 | 0.145 … 0.263 | −0.41 | 0.59 |
| TB N12 / N14 mid-span | 0.481 | 0.395 | 0.196 … 0.451 | −0.35 | 0.65 |
| TB N12 0.4L / N14 0.6L (alt.) | 0.572 | 0.468 | 0.277 … 0.523 | −0.30 | 0.70 |
| TB N13 mid-span | 0.705 | 0.187 | 0.171 … 0.263 | −0.23 | 0.77 |

Absolute C_m at k_FE, in m²/kN: CM N8 4.38e−5, CM N7 3.61e−4, TB N12 5.59e−5, TB N13 1.34e−4.

Findings:
1. **The actual Cầu Mây side-span gauge is near-blind** in the best-estimate model. Its index is 0.181, and 82 % of its positive influence area is cancelled by the negative lobe in the 90 m centre span.
   - The result depends strongly on pier fixity. C_m changes by a factor of about 14 between pinned (7.3e−6 m²/kN) and fixed (1.0e−4 m²/kN) piers.
   - So C_m, and any BPM load estimate from this gauge, is ill-conditioned with respect to an unmeasured support parameter.
2. **Variable EI matters more than the span ratio.** For both main-span gauges, the constant-EI index (0.70–0.76) falls to about 0.19–0.21 once the haunches are included. With the design-model pier stiffness, both cross below or onto 0.2.
   - This reflects the choice EI_ref = EI_min. Stiff haunches make a mid-span gauge "see" less net area relative to its local flexibility.
   - The cancellation ratio C_m/A⁺ for these gauges is still 0.59–0.77, so they are not blind in the cancellation sense.
   - Conclusion: the 0.2 threshold derived for prismatic beams does not transfer directly to haunched girders. The paper should either define EI_ref explicitly or use C_m/A⁺ as the threshold variable (WP2 to decide).
3. The Thái Bình side-span gauges are well conditioned. The index is 0.40 at k_FE (0.20–0.45 over all variants), C_m/A⁺ = 0.65, and only 35 % of the positive area is cancelled.

### 3.2 Static consistency (`wp3_loadtest_summary.csv`)

| Sensor | Convoy | W (t) | Measured (mm) | Report FE (mm) | This model at k_FE (mm) | meas/FE_report | meas/model(k_FE) | Pinned … fixed (mm) |
|---|---|---|---|---|---|---|---|---|
| CM N8 0.4L | 4 × 25 t | 100 | 5.55 | 5.93 | 5.69 | 0.936 | 0.977 | 7.18 … 2.75 |
| CM N7 mid | 6 × 25 t | 150 | 15.42 | 16.70 | 17.32 | 0.923 | 0.890 | 22.99 … 8.34 |
| TB N12 mid | 4 trucks | 122.1 | 3.21 | 3.58 | 3.18 | 0.897 | 1.010 | 5.93 … 2.48 |
| TB N13 mid | 6 trucks | 183.2 | 6.03 | 6.25 | 7.64 | 0.965 | 0.789 | 17.56 … 5.71 |
| TB N14 mid | 4 trucks | 122.1 | 3.63 | 3.82 | 3.37 | 0.950 | 1.078 | 6.34 … 2.61 |

- **Cầu Mây.** One rotational stiffness, k_FE = 2.7×10⁷ kN·m/rad (2.5–3.6×10⁷ over the Lv variants), reproduces both MIDAS values to within ±4.2 %. This supports the EI(x) model and the truck positions.
  - With k fixed at k_FE, the measured deflections imply an effective stiffness EI_eff/EI_design = **1.09**: the bridge is about 8 % stiffer than the design model.
  - Directly against the report FE, the ratio is 1.07–1.08 (1/0.936 and 1/0.923).
- **Thái Bình.** No single k reproduces the three report-FE values. The best compromise misses them by −11, +22 and −12 %. In the 2D beam the centre-span to side-span ratio is 2.1–3.0 for every plausible k and I_pier/I_mid tried. The report FE gives 1.75 and the measurements give 1.88.
  - The likely causes are the analogue cross-section dimensions, the unknown K0, closure and pier geometry, transverse effects, or a different truck assignment. TB absolute predictions are therefore low-confidence.
  - The report-FE ratios (measured/FE = 0.90–0.97, EI_eff/EI_FE = 1.04–1.11) are the more reliable stiffness evidence for TB.
  - The TB truck-position reading is supported by the N14/N12 asymmetry. The report FE gives 3.82/3.58 = 1.067 and this model gives 1.06 at k_FE, although the two side-span convoys are nominally the same.
- **Linearity.** It cannot be tested directly. No span was loaded with more than one convoy size while deflection was read. CM Scheme V (10 trucks) was read for strain only.
  - The available evidence is indirect:
    - (a) measured/FE ratios are similar for 4-truck and 6-truck convoys (CM 0.936 vs 0.923; TB 0.897/0.950 vs 0.965);
    - (b) the three gauges across the section agree (TB spread ≤ 0.14 mm; CM spread up to 2.05 mm between the edge lines in the eccentric N7 case, from torsion).
  - The measured N14/N12 ratio is 1.13, against 1.06–1.07 predicted, for the same nominal 4-truck convoy. This 6 % difference is an upper estimate of the combined position and weight-assignment scatter.

### 3.3 Implications: BPM (C_m from design EI) vs SLM

- BPM divides a measured deflection integral by the design C_m. Here the design models are 4–11 % more flexible than the structure. Ignoring other errors, a design C_m therefore underestimates the total load by roughly this amount (EI_eff/EI_design = 1.04–1.11).
- Where a gauge is near-blind (CM N8), the bigger risk is that the plausible range of pier rotational stiffness changes C_m by an order of magnitude. A design-model C_m at such a point is not usable for BPM.
- SLM calibrates C_m with a known vehicle, which removes both the EI bias and the support uncertainty, provided the response is linear. Linearity is supported only indirectly by these data.
- Even with SLM, a near-blind gauge gives a small signal-to-noise ratio for the integral. The criterion should be used before installation to avoid such points. For Cầu Mây, the centre-span mid-span gauge (C_m/A⁺ = 0.59) is preferable to the side-span gauge at 0.4L (0.18).

## 4. Limitations

1. Static, parked-truck data only. Nothing here tests ∫y dx = P·C_m.
2. Thái Bình EI(x) rests partly on analogue dimensions (bottom slab, flange root, haunches) [NEED VALUE], and the 2D model does not reproduce the report-FE span ratio.
3. The depth-law length Lv, the K0 and closure lengths, the pier and foundation stiffness, and the diaphragm are unknown. They are bracketed (Lv) or calibrated (k_FE against the report FE, which is itself a model).
4. CM truck weights are nominal (25 t). TB axle loads and the per-scheme truck assignment are unknown; this is bracketed.
5. The CM N8 section is 0.4L in the plan and report text but "mid-span" in the tables. Both are computed, and the conclusion (near-blind) holds for both: 0.181 and 0.105 at k_FE.
6. 2D beam: shear deformation, shear lag, torsion and transverse distribution are ignored. For 55–90 m spans with L/h ≥ 10 at mid-span, shear deformation is expected to be secondary, but this was not quantified.
7. Requests to the authors (add to `docs/03_thu_xin_so_lieu.md`):
   - the CM MIDAS file (in the .rar);
   - TB Tập 2.2.2 (structural calculation) or the cross-section drawings (bottom slab thickness, K0, closure);
   - pier dimensions (T6/T7, T12/T13);
   - TB per-scheme truck plates and axle loads;
   - any adjacent-span gauge readings.

## 5. Draft subsection (English, ≤ 900 words)

### Application to two in-service continuous box-girder bridges

The observability criterion was applied to two prestressed concrete box girders built by balanced cantilever in northern Vietnam and load-tested at acceptance. Cầu Mây (55 + 90 + 55 m, 2020) is a single-cell box whose depth varies from 2.40 m at mid-span to 5.40 m at the piers. Thái Bình (42 + 63 + 42 m, 2023) varies from 2.0 m to 4.0 m. In both bridges the two inner piers are monolithic with the girder and the end piers carry pot bearings. Both acceptance tests used parked truck convoys and dial gauges under the soffit. Cầu Mây was loaded with four 25 t trucks in a side span and six in the centre span. Thái Bình was loaded with four, six and four trucks of 29.2–31.7 t in its three spans. Each load case gives one reading per gauge. The tests therefore cannot check the deflection-integral identity itself, and this section is an application of the observability criterion with a static consistency check, not a validation of the dynamic theory.

Influence lines and C_m were computed with a two-dimensional Euler–Bernoulli model with variable stiffness. For Cầu Mây, the second moments of area at mid-span and at the pier face were taken from the designer's rating calculation (5.48 and 59.6 m⁴). For Thái Bình, they were computed from the design cross-section; dimensions not stated in the available documents were taken from the Cầu Mây section. The depth was assumed to vary parabolically between the two sections. The inner piers were represented by a rotational spring. Because pier dimensions were unavailable, the spring was bounded by the pinned and fixed limits. A best estimate, k_FE, was obtained by fitting the deflections that each test report gives for its own finite-element model.

For Cầu Mây, a single k_FE reproduced the reported model deflections at both gauges to within 4 %, using the convoy positions defined in the test plan. Measured deflections were 0.92–0.94 of the reported model values. At fixed support stiffness this corresponds to an effective flexural stiffness 8–9 % above the design value. Thái Bình showed measured/model ratios of 0.90–0.97. Its two-dimensional model could not match the reported centre-to-side-span deflection ratio (1.75, against 1.88 measured), so only the report ratios are used as stiffness evidence for that bridge. The six-truck and four-truck convoys gave similar measured/model ratios. This is consistent with linear behaviour, but it is not a direct test, because no span was loaded with more than one convoy size.

The normalised index 192·EI_ref·C_m/L⁴, with EI_ref the mid-span stiffness, gave a clear field example of a near-blind gauge. The Cầu Mây side-span gauge, placed at 0.4L from the end support as the test plan prescribes, has an index of 0.18 in the best-estimate model. The negative lobe in the 90 m centre span cancels 82 % of the positive influence area. Between pinned and fixed piers, C_m at this gauge changes by a factor of about fourteen (normalised index 0.02 to 0.45). A load estimate from this gauge would therefore depend mainly on a support parameter that was never measured. The centre-span gauge of the same bridge, with a cancellation of 41 %, and the Thái Bình side-span gauges, with 35 %, are better conditioned.

A second observation concerns non-prismatic girders. Including the haunches lowered the index at both centre-span gauges from about 0.7 for a prismatic beam to about 0.2. The cause is that the haunches restrain the span, so the net area is small relative to the mid-span flexibility used for normalisation; the cancellation is not the cause, since the net-to-positive area ratio is still 0.59–0.77. The 0.2 threshold derived for prismatic beams should therefore be stated together with its reference stiffness. For haunched girders, the net-to-positive area ratio C_m/A⁺, which does not depend on the normalisation, is the more transparent measure of how much the adjacent spans cancel.

For practice, the two bridges show the following:
- A C_m taken from the design model carries the design-model stiffness bias. Here that bias was 4–11 % and would under-estimate the total load by a similar amount.
- At a near-blind location, uncertainty in the support conditions can make a design-model C_m unusable.
- Calibration with a vehicle of known weight (SLM) removes both errors, provided the structure responds linearly.
- The criterion is most useful before installation. On Cầu Mây, moving the side-span gauge to the centre span, or adding a second gauge there, would have avoided the near-blind configuration.

Neither data set contains a crossing record. A direct test of the integral identity on a continuous girder therefore still needs slow-crawl or dynamic passes of weighed vehicles.
