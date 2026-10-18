# Package 3b: Field check of the crossing-integral theorem on the NOR-BWIM data (Smart Road Bridge)

Analysis date: 2026-10-18. Code: `code/norbwim/` (run order: `nb_field.py`, `nb_tests.py`, `nb_fe_veb.py`, `nb_fig1.py`; all with `python3 -I`). Results: `code/norbwim/results/`; figures: `code/norbwim/figures/` (PNG 300 dpi + PDF); logs: `code/norbwim/logs/`. The data were handled as untrusted: they sit in their own directory, were only parsed numerically, and the MATLAB `.mlx` files were unzipped and read as text, never run.

## 1. Data provenance and licence

| Item | Value |
|---|---|
| Dataset | Moghadam, A., Sarlo, R. (2024). *Nothing-on-Road Bridge-Weigh-In-Motion (NOR-BWIM) Dataset*. University Libraries, Virginia Tech. figshare, version 1, published 2024-10-01. https://doi.org/10.7294/26880898.v1 |
| Licence | CC0 1.0 (public domain dedication, as stated by the figshare API and README.rtf) |
| Local copy | `data/public/norbwim_figshare26880898/` holds 150 files (322 MB). Every md5 matched the figshare `computed_md5`. sha256 values are in `MANIFEST.txt`. Files over 50 MB (`Strains200Hz.dat`, `AllStrainData_construction trucks.dat`) and the 34–47 MB CSVs are listed in the folder's `.gitignore`. I skipped `.DS_Store`, `DataWed.xlsx` (a duplicate of the CSV) and the proprietary `.bdb` CSiBridge models. |
| Companion publications (metadata source) | [P1] Moghadam, A., AlHamaydeh, M., Sarlo, R. (2023). Nothing-on-road bridge-weigh-in-motion used for long-span, concrete-box-girder bridges: an experimental case study. *J. Struct. Integrity Maint.* 8(2), 79–90. https://doi.org/10.1080/24705314.2023.2165606. [P2] Moghadam, A., AlHamaydeh, M., Sarlo, R. (2022). Bridge-weigh-in-motion approach for simultaneous multiple vehicles on concrete-box-girder bridges. *Autom. Constr.* 137, 104179. https://doi.org/10.1016/j.autcon.2022.104179. [P3] Moghadam, A., AlHamaydeh, M., Sarlo, R. (2023). Dual-purpose procedure for bridge health monitoring and weigh-in-motion used for multiple-vehicle events. *Autom. Constr.* 148, 104768. https://doi.org/10.1016/j.autcon.2023.104768. [D] Moghadam, A. (2022). *Integration of Traffic and Structural Health Monitoring Systems Using a Novel Nothing-On-Road (NOR) Bridge-Weigh-In-Motion (BWIM) System*. PhD dissertation, Virginia Tech. http://hdl.handle.net/10919/111390. I downloaded the open PDF from VTechWorks and read it. P1–P3 were not opened (paywalled); all metadata below comes from [D] and the dataset files. |

**Correction to the brief.** The field data are **not** "18 tests with 3-, 4-, 5- and 6-axle trucks, single and multiple, two lanes". On the Smart Road Bridge the field campaign ([D] Ch. 2, Table 2.1) used **3-axle trucks (Trucks 1, 2, 3) and one 5-axle truck (Truck 4)**: 18 weighed runs, plus 2 multiple-truck runs (Truck 4 followed by Truck 3, about 10 m apart). The 3-, 4-, 5- and 6-axle records and the zigzag and side-by-side events (`Run*.txt`, `6035_*`, `3axle_speed_*`, `*.xlsx`) are **CSiBridge simulations of a different bridge**: the Varina-Enon Bridge (VEB) approach spans, 45.72 m long, with added noise ([D] Ch. 3–4; `mainMPNORBWIM.mlx`: "The following tests are conducted in CSI Bridge"). Section 6 treats them only as a secondary, synthetic check.

## 2. Metadata (field data, Smart Road Bridge)

Bridge ([D] §2.2.1): 5-span continuous post-tensioned concrete box girder, 86.5 + 3×144 + 86.5 m = 605 m. Two 3.6 m lanes on a 12 m deck. Box depth varies from about 3.8 m (mid-span) to 9.5 m (piers). Span 2 is instrumented. All gauges sit "close to the mid-span of the second span (144/2 m from piers)", on the inside face of the top slab under the wheel path (Row 1). Gauges are BDI ST350 full-bridge transducers, GPS-synchronised.

| Quantity | Value | Source |
|---|---|---|
| Sampling rate | 200 Hz on day 2 (2020-09-30, Trucks 3 and 4); 100 Hz on day 1 (2020-09-10, Trucks 1 and 2) | [D] §2.2.3; `f=200` in `mainSmartRoadBridgeNORBWIM.mlx`; timestamps |
| Day-2 channels | `st40, st36, st34, st31` in `Strains200Hz.dat` (TOA5 header: "microstrain") | file header |
| Day-2 gauge layout | The four gauges lie in one longitudinal line under the wheel path, in the order st40 → st36 → st34 → st31. The st40–st31 distance is 6.02 ± 0.09 m, from spike speed × cross-correlation lag (n = 12), i.e. about 2 m pitch. This matches [D]'s "about 2 m". Exact x of each gauge: [NEED VALUE]. | derived (log `field.log`) |
| Day-1 channels | 12 unnamed channels in `AllStrainData_construction trucks.dat`. `ch4` equals `B.csv` `Column5`, which the authors use as st40. From axle-spike timing: 4 longitudinal stations 2 m apart, {ch3, ch4}, {ch5, ch6}, {ch7, ch12}, {ch10, ch11}, each pair having one strong-spike gauge (ch4, ch5, ch12, ch11, taken as the wheel path). ch1, ch2, ch8 and ch9 show no axle spikes (probably Row 3 on the web, or Row 2). Exact identity: [NEED VALUE]. | derived |
| Units | Strain = −521.2²×10⁻³ × raw (= −271.65 × raw), taken from the authors' script (`Test1_st40=(-521.2*521.2*0.001)*A.st40(...)`). This gives compression as negative, consistent with the global sagging response at the top slab. The same factor is assumed for every channel. Per-gauge calibration factors: [NEED VALUE], so cross-gauge absolute ratios are unverified. | script |
| Truck 3 (3-axle, hired) | GVW 26.8 t; front 7.2 t, rear tandem 19.6 t; axle spacings (AS) 4.78, 1.32 m | [D] Table 2.1 and §2.2.3, off-road weigh station |
| Truck 4 (5-axle, hired) | GVW 25.9 t; front 5.2, tandem 11.0, tandem 9.7 t; AS 6.17, 1.32, 10.62, 1.24 m | [D] Table 2.1 and §2.2.3 |
| Trucks 1, 2 (3-axle construction) | AS 4.24/1.37 and 4.19/1.35 m. Per-run GVW from [D] Table 2.4 (Runs 1–10): 22.82, 22.51, 22.45, 22.18, 22.30 / 22.86, 22.10, 21.17, 21.61, 22.00 t, reported by the drivers each pass | [D] Tables 2.1 and 2.4 |
| Inconsistencies (recorded, not resolved) | (i) The script's axle weights in kips give 58.16 kips = 26.4 t for Truck 3 and 59.54 kips = 27.0 t for Truck 4; [D] gives 26.8 and 25.9 t. [D] is used here; the effect would be ≤4%. (ii) [D] Table 2.1 lists GVW ranges (22.4–23.1, 21.4–23.1 t) that do not match its own Table 2.4. (iii) [D] Table 2.1 speeds ("≈13 & 23" for T3, "≈17 & 27" for T4) disagree with the script's GPS speeds (27.9/17 and 23/13.5 m/s) and with my axle-spike speeds, which agree with the script within 1–2% (table below). (iv) I assume Run k = script Evaluation k (drivers' timestamps are chronological). | |

Run list (lane A = gauge lane, travelling with st40 passed first; lane B = return trip in the other lane, opposite direction). Speeds come from axle spikes and measured axle spacings. Where spikes are weak (lane B), speed = st40–st31 distance / cross-correlation lag.

| Run | Truck (axles) | GVW t | Lane | v used m/s | v script m/s | Status |
|---|---|---|---|---|---|---|
| R1–R4 | T1 (3) | 22.82, 22.51, 22.45, 22.18 | A | 10.4, 12.5, 11.4, 12.8 | 10.5, 12.1, 11.3, 12.2 | used |
| R5 | T1 (3) | 22.30 | A | 12.8 | 12.1 | excluded: T2 enters 43 s later; global-shape fit r² = 0.60 |
| R6 | T2 (3) | 22.86 | A | 19.8 | 19.9 | excluded: T1 crossed 15.7 s earlier |
| R7–R9 | T2 (3) | 22.10, 21.17, 21.61 | A | 19.1, 19.8, 19.8 | 20.0, 19.7, 19.9 | used |
| R10 | T2 (3) | 22.00 | A | 19.1 | 19.0 | excluded: overlaps R5's truck |
| R11–R14 | T3 (3) | 26.8 | A | 27.7, 28.1, 16.9, 16.8 | 27.9, 28.2, 17.1, 16.6 | used |
| R15–R18 | T4 (5) | 25.9 | A | 23.0, 22.8, 13.8, 13.2 | 23.1, 22.9, 13.8, 13.3 | used |
| R11r–R18r | same trucks | 26.8 / 25.9 | B | 10.7–22.0 | – | used (speed from gauge lag) |
| M1, M2 | T4 + T3 in line (about 10 m gap) | 52.7 | A | 13.2/13.0, 13.5/14.0 | – | superposition test |
| M1r, M2r | T4 then T3, 11–12 s apart | 52.7 | B | lag-based | – | flagged: lag speed of T4 inconsistent with the low-pass fit |
| X1, X1r, X2, X2r | unidentified extra 3-axle passes | – | A/B | – | – | excluded: no documented weight |

## 3. Methods

1. **Event isolation.** An automatic detector flags each crossing (|strain − 2-min running median| > 0.8 µε). The script's sample windows in `DataWed.csv` (index offset +299 458 into `Strains200Hz.dat`, verified by exact value matching) and `B.csv` (equal to the `AllStrain` row index) assign the documented runs to detected events.
2. **Speed, direction and timing.** Axle-spike times come from the median-filter high-pass (0.3 s). v is the tape-measured wheelbase divided by the first-to-last spike interval, taken as the median over the channels showing exactly the expected number of spikes, with a pattern rms below 0.03 s. Travel direction comes from the gauge order and from a least-squares fit of the 0.5 Hz low-passed record to the beam-model influence line (Section 3, item 5) in both directions. Lane A trucks enter from the span-5 end. Entry and exit times follow from the sensor abscissa (158.5 m from the span-1 abutment), the wheelbase and v.
3. **Integral.** I_t = ∫ε dt is taken over [t_entry − 5 s, t_exit + 5 s], after removing a linear baseline through the means of 8 s segments before and after the window (the pre/post linear baseline). Then I_x = ∫ε dx = v·I_t, reported in µε·m, and C = I_x/GVW in µε·m/t. For two vehicles at different speeds the theorem in the time domain reads I_t = C·Σ W_k/v_k.
4. **Noise.** For every event, the standard deviation of the same integral was computed over 80 vehicle-free windows of the same length (≥70 s from any detection) on the same day and channel. Measured-scatter CVs are compared with the noise-expected CV, and with χ² of the inverse-variance weighted mean. "avg" is the mean of the four day-2 gauges, and of the four day-1 wheel-path gauges (ch4, ch5, ch11, ch12).
5. **Beam model** (`nb_beam.py`). This imports `cm_multispan.beam_fe`, `_solve` and the `haunch_*` helpers (unmodified). It is a 5-span Euler-Bernoulli FE model, 240 elements per span. EI is either uniform or haunched with h(x) parabolic from 3.8 to 9.5 m and I ∝ hⁿ (n = 2, sensitivity n = 2.5). From it I compute the moment influence line at the sensor, the uniform-load moment diagram M_q(x), its zero points, and the top-fibre strain proxy C_ε(x) ∝ −M_q/hⁿ⁻¹.
6. **SLM.** Every ordered pair (reference run, test run) in the same group gives Ŵ_j = W_ref·I_j/I_ref. I also calibrate on all runs of one truck and predict the other truck. BPM (absolute C from a model) is not possible because E, I(x) and fibre distance are not published: [NEED VALUE].

## 4. Results

### (a) Invariance: C = ∫ε dx / GVW per sensor (`test_a_invariance.csv`, Fig. 2)

| Group | Sensor | n | C (µε·m/t) ± SE | CV measured | CV expected from noise | χ² p |
|---|---|---|---|---|---|---|
| Day 1, T1+T2 (3-axle, 10.4–19.8 m/s) | ch5 | 7 | −5.53 ± 0.12 | 7.0% | 5.7% | 0.17 |
| | ch11 | 7 | −5.84 ± 0.15 | 5.8% | 6.8% | 0.60 |
| | ch10 | 7 | −4.22 ± 0.13 | 6.3% | 8.0% | 0.71 |
| | ch4 (= st40) | 7 | −2.18 ± 0.09 | 13.5% | 11.1% | 0.16 |
| | avg (4 wheel-path) | 7 | −4.02 ± 0.09 | **5.6%** | 6.1% | 0.53 |
| | ch1, ch2, ch8, ch9 (no spikes) | 7 | −1.5 to −2.3 | 17–19% | 8–11% | ≤0.012 |
| Day 2, T3 (3-axle) + T4 (5-axle), 13–28 m/s | st36 | 8 | −5.93 ± 0.34 | 12.0% | 16.5% | 0.73 |
| | st31 | 8 | −5.95 ± 0.42 | 16.0% | 20.1% | 0.68 |
| | st34 | 8 | −2.37 ± 0.18 | 15.2% | 22.2% | 0.83 |
| | st40 | 8 | −2.12 ± 0.25 | 34.0% | 33.9% | 0.48 |
| | avg | 8 | −4.10 ± 0.29 | **14.4%** | 20.2% | 0.79 |
| st40 pooled, both days, 4 trucks | st40/ch4 | 15 | −2.15 | 25.3% | 25.5% | 0.32 |

- **5-axle vs 3-axle (day 2):** C(T4)/C(T3) = 0.999 ± 0.140 (avg), 1.010 ± 0.115 (st36), 1.004 ± 0.140 (st31), 0.95 ± 0.22 (st40).
- **Same gauge on two days:** st40 gives C = −2.18 ± 0.09 on day 1 (T1, T2) and −2.12 ± 0.25 on day 2 (T3, T4).
- **Off-path gauges:** ch1, ch2, ch8 and ch9 are the only gauges whose scatter exceeds noise. Their C is 23–26% smaller for T2 than for T1, whereas the wheel-path gauges give T2/T1 = 0.98–1.00. Because T1 was always slow and T2 always fast, truck, transverse path and speed cannot be separated. The cause is unidentified.

### (b) SLM (`test_b_slm_*.csv`, Fig. 3)

Single-reference, all ordered pairs, |error| in %:

| Group / sensor | Same truck: MAE / RMSE / max | Other truck: MAE / RMSE / max |
|---|---|---|
| Day 1 avg | 7.0 / 7.9 / 14.4 | 6.5 / 7.9 / 15.1 |
| Day 1 ch11 | 7.2 / 9.6 / 19.2 | 6.9 / 7.2 / 10.3 |
| Day 1 ch5 | 9.7 / 11.0 / 22.0 | 7.4 / 9.0 / 21.3 |
| Day 2 lane A avg | 17.8 / 24.9 / 63.9 | 17.8 / 21.1 / 45.4 |
| Day 2 lane A st36 | 12.9 / 20.8 / 53.4 | 14.3 / 17.6 / 37.2 |
| Day 2 lane A st40 | 54 / 77 / 210 | 48 / 73 / 286 |

Calibrated on all runs of one truck and applied to the other (MAE):

- **Day 1 avg:** T1→T2 4.7%, T2→T1 6.1% (ch11: 0.6% and 6.9%).
- **Day 2 avg, across axle counts:** T3 (3-axle)→T4 (5-axle) 5.1% (errors −13.6, −3.9, +2.8, 0.0%); T4→T3 17.1%.
- **Day 2 st36:** T3→T4 1.5%; T4→T3 13.6%.
- **Cross-day, st40:** calibrate on day 1, predict day-2 trucks: 24.4%.

The errors scale with the per-event integral noise, which on day 2 is 3–4 times higher than on day 1 (Section 5).

### (c) Speed (`test_c_speed.csv`, Fig. 4)

Weighted slope of C against v:

- **Day 1:** −3.6 ± 5.8% per 10 m/s (avg), +1.8 ± 5.5% (ch5), +1.0 ± 6.5% (ch11).
- **Day 2:** +5.2 ± 13.0% per 10 m/s (avg).

No speed effect is resolved for the wheel-path gauges over 10–28 m/s. Dynamics (2–3 Hz deck spikes, about 0.8 Hz free vibration after exit; Fig. 1) integrate out. The off-path day-1 gauges show −35 to −39% per 10 m/s, confounded with truck identity (see (a)).

### (d) Lane / transverse position (`test_d_lane.csv`, Fig. 5a)

Same trucks and same weights, C_B/C_A:

| Sensor | C_B/C_A |
|---|---|
| avg | 0.81 ± 0.09 |
| st36 | 0.66 ± 0.06 |
| st31 | 0.86 ± 0.09 |
| st34 | 0.88 ± 0.10 |
| st40 | 1.02 ± 0.16 |

As the theorem predicts, C belongs to the load path. A truck in the far lane must be weighed with that lane's C. Lane-B scatter (CV 31–40%) exceeds noise (p = 0.02–0.16 per sensor), most likely because of the less precise gauge-lag speeds (weak spikes).

### (e) Multiple-truck events (`test_e_superposition.csv`, Fig. 5b)

Measured ∫ε dt divided by the sum of single-truck predictions C_A·Σ W_k/v_k (lane A, T4 + T3 in line, 52.7 t):

| Event | avg | st36 | st31 | st40 | SLM total GVW from avg |
|---|---|---|---|---|---|
| M1 | 0.93 ± 0.11 | 0.93 | 0.92 | 1.12 | 48.8 t (−7.3%) |
| M2 | 0.92 ± 0.11 | 0.91 | 0.95 | 1.01 | 48.5 t (−7.9%) |

Superposition holds within 1σ. The return-lane pairs give 1.06 and 0.95 (avg), but their speeds are flagged.

### (f) Observability (`test_f_model.csv`, `test_f_gauge_ratios.csv`, Fig. 6)

- **Theorem check in the model.** ∫IL_M dx equals M_q(x_s) to 0.08–0.12% for all three EI models.
- **Zero-moment points of M_q in span 2:** x = 121.6 and 190.8 m with the haunch, n = 2 (124.1/188.7 m with n = 2.5; 111.3/200.5 m with uniform EI). That is 35 m from pier 1 and 32–37 m either side of the gauges at 158.5 m.
- **Is the field gauge blind?** No. Its |C_ε| is at 69% of the largest |C_ε| on the girder (the maximum is at an interior pier, under hogging, for this haunch model). Only the off-path gauges are weak.
- **Span shares.** The net integral at the gauge is only 51% of its positive (span-2) part. Shares are span 1 −26%, span 2 +172%, span 3 −66%, span 4 +23%, span 5 −4% (haunch model). The whole 605 m crossing must therefore be integrated; truncating at span 3 would bias C by about 20%.
- **Error map.** Combining the model shape with the measured midspan C and the measured integral noise, one crossing of a 25 t truck gives σ_W/W = 10% (day 1) or 35% (day 2) for st40 at midspan. In span 2, |C_ε| drops below 50% of the midspan value within ±12 m of each zero-moment point, and below 25% within ±6 m. There σ_W/W at least doubles or quadruples, and it diverges at the points themselves. A sensor there would be blind in exactly the sense of the theorem.
- **Model-free shape check (gauge ratios).** The beam model predicts equal C for gauges 2 m apart at one section (ratio 0.978–1.003). The measured integral ratios are far from 1 at the same section: st36/st40 = 1.82 ± 0.10 and st31/st40 = 2.41 ± 0.10 in lane B; day 1 ch5/ch4 = 2.55 ± 0.10, and the 12 day-1 channels range from 0.68 to 2.71 × ch4. This is not noise. It is also unlikely to be gauge-factor spread (typically ±10%), because the ratios change with lane (st36/st40 is about 3.2 in lane A and 1.8 in lane B). The deck-soffit gauges see global bending plus a load-path-dependent slab component (local slab bending, shear lag). Each gauge has its own C, which is invariant (the theorem holds per sensor), but a 1-D beam model cannot predict it. **BPM with a beam-model C would fail here; SLM, or a 3-D/plate C, is needed.**

### Secondary: VEB CSiBridge records (synthetic, other bridge; `fe_veb_*.csv`, Fig. 7)

- **Invariance:** C = 1.223 µε·m/t with CV **1.0%** over 7 lane-2 records (3-, 4- and 5-axle; GVW 23.2–38.6 t).
- **Speed:** CV 1.5% over 15–35 m/s (3-axle).
- **Superposition:** 3-axle + 5-axle in line gives 0.994 (lane 2) and 1.037 (lane 1).
- **A blind case:** the same gauge has a net C of only −0.094 µε·m/t for lane-1 trucks, −0.08 times the lane-2 value. Its positive local and negative global lobes nearly cancel along that path.
- **Records not used:** the 6-axle and 4-axle `6035_*` records are 4.5 s windows that do not cover a complete crossing, and 6-axle axle weights are not given in [D]'s text: [NEED VALUE].

## 5. Limitations (honest)

1. **Noise limits day 2.** Low-frequency (<0.2 Hz) strain wander of about 0.1–0.3 µε, possibly thermal or wind, falls in the band of the global response. The resulting integral noise is about 18–25 µε·m per crossing on day 2, against 5–6 µε·m on day 1, while signals are 50–130 µε·m. Other baselines (8–60 s, linear or quadratic) did not reduce it. Day-2 single-sensor results are noise-limited, though consistent with invariance.
2. **Few configurations.** Only two axle counts (3 and 5) and four trucks have documented weights. The 5-axle vs 3-axle comparison rests on n = 4 + 4 runs. Day-1 weights are driver-reported, and their run mapping is assumed.
3. **Unpublished calibration and layout.** Gauge calibration factors, exact gauge coordinates and day-1 channel names are not published: [NEED VALUE]. Absolute C and BPM cannot be checked. Gauge ratios are interpreted with the caveat of a common gain factor.
4. **No field test at a zero-moment point.** All field gauges sit at one section (mid-span 2). The observability statement for zero-moment points is model-based, using measured noise.
5. **Lane-B speeds.** These come from a calibrated gauge-to-gauge lag and are less precise. M1r and M2r are flagged.
6. **Exclusions.** Three day-1 runs (R5, R6, R10) were excluded for vehicle overlap, and four undocumented passes were excluded. Exclusions were decided from overlap and identity before looking at the integrals, except that R5 and R10 were also identified by their poor shape fit.
7. **The beam model is indicative only.** EI(x) ∝ hⁿ with depths from [D] (3.8–9.5 m), parabolic haunch, no prestress, rigid supports.

## 6. Draft subsection (English, ≤1000 words)

**Field verification on a five-span continuous box-girder bridge (public NOR-BWIM data)**

We tested the crossing-integral relation on the only public field dataset we found that combines a multi-span continuous girder with weighed trucks: the NOR-BWIM dataset of the Virginia Smart Road Bridge (Moghadam and Sarlo, 2024, doi:10.7294/26880898.v1, CC0), documented in Moghadam et al. (2023, *J. Struct. Integrity Maint.* 8(2):79–90) and in Moghadam (2022, PhD dissertation, Virginia Tech, hdl:10919/111390). The bridge is a post-tensioned concrete box girder continuous over five spans (86.5 + 3×144 + 86.5 m) with a depth varying from about 3.8 m at mid-span to 9.5 m at the piers. Strain gauges (BDI ST350) are mounted on the soffit of the top slab near mid-span of span 2, in line with the wheel path at about 2 m pitch. On one day, two 3-axle construction trucks (21.2–22.9 t, driver-reported per pass) were recorded at 100 Hz on 12 channels. On another day, a 3-axle (26.8 t) and a 5-axle (25.9 t) truck, both weighed on a static scale, were recorded at 200 Hz on four channels, in the instrumented lane, on the return trip in the other lane, and in two in-line two-truck runs. Axle spacings were measured on site. We obtained speeds from the axle-induced local strain spikes and the known wheelbase; they agree with the authors' GPS speeds within 1–2%. For each crossing we removed a linear baseline fitted to the quiet records before and after the event and integrated the strain over the full time the truck was on the 605 m bridge. We converted the result to ∫ε dx with the speed, and estimated the measurement uncertainty of each integral from vehicle-free records of the same length.

For the four wheel-path gauges of the first day, the ratio ∫ε dx/GVW has a coefficient of variation of 5.8–8.1% per gauge over seven crossings at 10–20 m/s, and 5.6% for the gauge average. This scatter is fully explained by the measured integral noise (χ² p = 0.17–0.71). The gauge common to both days gives the same constant on both days (−2.18 ± 0.09 and −2.12 ± 0.25 µε·m/t), although the trucks, axle configurations and speeds differ. On the second day the 5-axle and 3-axle trucks give the same constant within noise: their ratio is 0.999 ± 0.140 for the gauge average and 1.010 ± 0.115 for the best gauge, as the axle-configuration independence of C_r requires. No speed dependence was resolved between 10 and 28 m/s (slope −3.6 ± 5.8% per 10 m/s); the local axle spikes and the bridge vibration integrate out. Used as a static-load-model (SLM) estimator with a single reference crossing, the integral predicted the GVW of the other crossings with mean absolute errors of 6.5–7.0% (gauge average, day 1). Calibrating on the 3-axle truck and weighing the 5-axle truck gave a mean absolute error of 5.1%. The second day's records carry about four times more low-frequency strain noise, so its single-reference errors are larger (MAE 18% for the average, 13–14% for the best gauge). The two in-line two-truck events gave integrals of 0.93 ± 0.11 and 0.92 ± 0.11 of the sum predicted from the single-truck constant. Superposition therefore holds within uncertainty, and the combined weight was recovered within 8%.

The data also confirm that C_r belongs to the load path rather than to the vehicle. Return trips of the same trucks in the far lane gave a constant 0.81 ± 0.09 times that of the instrumented lane (0.66–1.02 for individual gauges), so lanes must be calibrated separately. More importantly, gauges a few metres apart at one cross-section have constants differing by factors of up to 2.7, and the ratios change with the lane. A one-dimensional beam model predicts equal constants for all of them. The deck-soffit gauges therefore respond to slab and shear-lag action as well as to girder bending. The integral is invariant for every gauge separately, as the theorem only requires linearity, but its value cannot be predicted from a beam model. On such bridges the reference-vehicle (SLM) route, or a three-dimensional model for the BPM route, is necessary.

A beam model of the girder (Euler-Bernoulli, parabolic haunch, I ∝ h²) reproduces the measured global strain history (r² ≈ 0.9) and places the zero-moment points of the uniform-load moment diagram in span 2 at 121.6 and 190.8 m, about 35 m on either side of the gauges. The instrumented section is far from those points, and its constant is about 69% of the largest one on the girder (found at an interior pier). Only half of the integral comes net from the instrumented span: the adjacent spans contribute lobes of opposite sign (−26% and −66%) and span 4 adds +23%, so the integral must be taken over the complete crossing. Combining the model shape with the measured noise, a gauge within ±12 m of a zero-moment point would see its constant fall below half the mid-span value, at least doubling the weight error (10% per crossing at mid-span on the quieter day). At the zero-moment point the error is unbounded. This is the blind-sensor condition of Section X, here quantified for a real bridge and noise level. The strain records simulated by the dataset authors for a different box-girder bridge (CSiBridge, three 45.72 m spans) show the same features without field noise: a CV of 1.0% across 3-, 4- and 5-axle trucks of 23–39 t, 1.5% across speeds of 15–35 m/s, and superposition within 0.6–3.7%. They also contain a gauge whose net constant almost vanishes for trucks in one lane, a transverse analogue of the zero-moment blind spot.

The main limitations are the small number of weighed configurations (two axle counts, four trucks), driver-reported weights on one day, unpublished gauge calibration factors and positions (which prevent an absolute, model-based estimate), and low-frequency strain noise that dominates single-crossing errors on the second day.
