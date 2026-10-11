# WP4: Dynamic crossing records, baseline drift and quasi-static integral

Date: 2026-10-11. Script: `code/analysis/wp4_dynamic_records.py` (log: `code/analysis/logs/wp4.log`). Figures: `figures/wp4_*.png`. Tables: `data/bridges/{gie-cuc-1,phuong-do}/wp4_*.csv`.
Truck weight, speed, lane and instrumented girder for these runs are [NEED VALUE]. Every number below is computed from the CSV files; assumptions are flagged.

## 1. Data and conventions
- Gie Cuc I N1-N3 (3 simply supported spans, L = 25.7 m) and Phuong Do N1, N2 (L = 17.5 m); 3000 samples at 200 Hz (15 s). Two channels per record: `Vong0` ("raw") and `Vong` ("proc", the series used in the consultant report). Analysis is on s = -y (downward positive); integrals are in mm·s.
- For N1 of Gie Cuc, raw = proc. For the other four records the two channels differ by a scale and offset (section 4).
- Both Gie Cuc series are staircases (0.1 mm quantum in raw; dead-band and 0.65 mm steps in proc for N2/N3).

## 2. Methods
- Events: detected on the proc channel (smoothed 0.2 s, threshold = 10 % of the largest excursion above the modal level, events merged if closer than 0.6 s, duration >= 0.5 s); the same extents are applied to the raw channel. "Major" = peak >= 25 % of the record's largest peak. Events touching the record end are flagged truncated and excluded from statistics.
- Duration/speed: T10 and T50 (width at 10 % and 50 % of the downward peak, after baseline). Three estimators: (i) point-load mid-span influence line (Euler-Bernoulli), v = 0.933 L/T10; (ii) v = 0.653 L/T50; (iii) least-squares fit of a 3-axle quasi-static model (axle load fractions 0.2/0.4/0.4 and spacings 3.37+1.35 m (Gie) or 3.9+1.36 m (PD) of the STATIC-test truck, an assumption since the dynamic truck is unknown) to the 2 Hz low-passed lobe; fit parameters v, entry time, amplitude.
- Baselines for the integral over [event start - 0.3 s, event end + 0.3 s]: (a) constant = median of the first 0.5 s of the record (tare); (b) straight line between the medians of the quiet windows before and after the event (reference); (c1) cubic polynomial fitted to all quiet samples; (c2, c3) zero-phase Butterworth high-pass (0.1 and 0.5 Hz); "pre-only" (constant pre level). Empirical eps0: eps0_prepost = post - pre level; eps0_eff = (I_a - I_b)/window; bias projected to the whole 15 s record = |eps0_eff|·15/I_b (paper formula). Whole-record check: integral over 15 s with tare vs cubic baseline.
- Low-pass: zero-phase 4th-order Butterworth, fc = 1, 2, 3 Hz (f1 = 5.2-6.0 Hz, so 2 Hz is about f1/3) applied to the full record; ratio of integrals LP/unfiltered with the same baseline (b).
- Illustrative reference only: P·C_m with C_m = 5L^4/(384EI), L_calc = 25.0 m, E·I = 31.5e6·0.32909 kN·m² (Gie, P = 27.5 t) and L = 17.5 m, E·I = 29.94e6·0.08324 (PD, P = 24 t), 100 % of the load on one girder. These are the static-test truck weights, NOT known for the dynamic runs.

## 3. Results

### 3.1 Events and speed (figure `wp4_records_events.png`; table `wp4_events_baseline.csv`)
Complete major events: Gie N1 two (peaks 10.2 and 4.5 mm after baseline, plus a third, truncated at 15 s; a slow 1.2 mm excursion at 8.9-10.0 s is flagged minor and not treated as a crossing), N2 two, N3 one; PD N1 one, N2 one.

| Record / event | T10 (s) | v (IL10) | v (IL50) | v (3-axle fit) | km/h |
|---|---|---|---|---|---|
| Gie N1 e1 | 1.78 | 48.6 | 53.7 | 50.9 | |
| Gie N1 e2 | 1.65 | 52.3 | 53.0 | 54.5 | |
| Gie N2 e1 | 1.58 | 54.8 | 61.6 | 55.7 | |
| Gie N2 e2 | 1.83 | 47.2 | 57.3 | 52.5 | |
| Gie N3 e1 | 1.74 | 49.8 | 55.9 | 53.2 | |
| PD N1 e1 (raw / proc) | 1.89 / 1.80 | 31.1 / 32.7 | 32.7 / 35.5 | 33.6 / 36.2 | |
| PD N2 e1 | 2.18 | 27.0 | 30.1 | 29.9 | |

Gie Cuc: all five events give 47-62 km/h by every estimator, i.e. about 1.3-1.8 times the stated 30-40 km/h (at 40 km/h the point-load T10 would be 2.16 s; observed 1.58-1.83 s). Phuong Do: 27-36 km/h, consistent with the low end of the stated range. Either the Gie Cuc vehicles were faster than stated, the crossing includes different vehicles, or the time axis/channel processing differs; this cannot be resolved without speed records [NEED VALUE]. The fit residual is 2-5 % of the peak, so the shape is consistent with a quasi-static crossing.

### 3.2 Baseline sensitivity (figures `wp4_baseline_methods.png`, `wp4_integral_sensitivity.png`)
Deviation of the event integral from reference (b), complete major events:

| Method | Gie Cuc (5 events) | Phuong Do (4 event-channels) |
|---|---|---|
| (a) tare only | 0 to +2.7 %, N3: -5.6 % | N1 raw **-36.4 %**; N1 proc -1.9 %; N2 +6.2 % |
| (c1) cubic through quiet samples | +1.7 to +3.6 % | -1.2 to +0.1 % |
| (c2) high-pass 0.1 Hz | -44 to -83 % | -50 to -72 % |
| (c3) high-pass 0.5 Hz | -98 to -103 % | -101 to -102 % |

- Empirical drift: Gie Cuc post-minus-pre level 0.0-0.1 mm in raw (resolution is 0.1 mm); PD N2 0.17-0.23 mm; **PD N1 raw 2.06 mm (step, 18 % of its peak)**. Quiet-level scatter (0.5 s blocks) 0.01-0.13 mm.
- For a 2-4 s window the drift effect is small (0-6 %) except PD N1 raw. It grows with the window: with tare only over the whole 15 s record the integral differs from the cubic-baseline value by +7 % (Gie N1), -16 % (N2), -60 % (N3), +34 % (PD N2), and -170 % for PD N1 raw (sign reversal; equivalent eps0 = 1.3 mm) (`wp4_record_totals.csv`). The paper-formula projection |eps0_eff|·15/I_b gives 7-36 % (Gie raw N1/N3) and 22 % (PD N2), 133 % (PD N1 raw). This supports "bias = eps0·T_record/integral": a fraction of a millimetre of zero offset, harmless over a 2 s event, is a tens-of-percent error over a full record. It does not show that drift dominates over short event windows.
- High-pass filtering is not a valid baseline for an integral: a zero-phase high-pass has zero DC gain, so it removes most of the quantity being integrated (the 0.5 Hz result is ~-100 %).
- Caveat: reference (b) is itself an estimate; for the proc channels of Gie N2/N3 the dead-band forces pre = post = 0 (drift removed by the processing, so eps0 = 0 there trivially).

### 3.3 Low-pass / dynamic part (figure `wp4_lowpass.png`; `wp4_lowpass.csv`)
- Integral ratio LP/unfiltered: 0.9999-1.0010 at 2 Hz and 0.999-1.001 at 3 Hz for complete events; at 1 Hz 0.997-1.010. Only the truncated Gie N1 event 4 deviates (1.010 at 2 Hz, 1.093 at 1 Hz).
- The dynamic residual (unfiltered minus LP) integrates to nearly zero: |net| / integral of |residual| = 0.001-0.022, even though the residual peaks reach 3-16 % of the quasi-static peak. Peak ratio unfiltered/LP(2 Hz) is 1.01-1.17 (Gie) and 1.04-1.05 (PD), against reported 1+IM of 1.114-1.152 and 1.095-1.126.
- This cancellation is partly structural (unity DC gain of the filter), so it confirms the integral is insensitive to the dynamic component, not a test of the theory itself.

### 3.4 Consistency across spans (figure `wp4_consistency.png`; `wp4_consistency*.csv`, `wp4_channel_scale.csv`)
- The proc/raw relation Vong = k·Vong0 + c has k = 1.00 (Gie N1), 3.25 (N2), 5.15 (N3), 0.67 (PD N1), 1.34 (PD N2) (corr >= 0.999). The channel scale therefore differs by up to 7.7 times between records, so absolute amplitudes and integrals are not comparable across spans without the sensor calibration [NEED VALUE]. (The inventory's "~3.2-3.3" for N3 is not what the data show.)
- v·I (mm·m) with v from the 3-axle fit, baseline (b): Gie proc 153, 74 (N1), 70, 113 (N2), 131 (N3): mean 108, CV 33 % (15 % if only the largest event per span is used); Gie raw CV 89 %. PD proc 48 and 70 (CV 26 %); PD raw 109 and 52 (CV 50 %). Using nominal 30/35/40 km/h instead changes the level but not the CV (36 % Gie proc, 38 % PD proc). Different events within one record (Gie N1: 153 vs 74) differ by a factor 2, which shows that the events are not the same truck/lane, or not the same load.
- Illustrative absolute check (assumed static-test truck, 100 % on the girder): P·C_m = 132 mm·m (Gie), 115 mm·m (PD). The implied girder share v·I/(P·C_m) is 0.53-1.16 for Gie proc and 0.42-0.61 for PD proc. Shares above ~0.7 are unphysical for one girder (measured static shares 0.45-0.71 Gie, 0.35-0.60 PD), consistent with the inventory's remark that the Gie dynamic channel over-reads (7.8-10.8 mm vs 3.6 mm static under three trucks). **Absolute weight cannot be checked without truck weight, transverse position and calibration.**

### 3.5 Phuong Do N1 positive lobe (figure `wp4_pd_n1_lobe.png`; `wp4_n1_lobe.csv`, `wp4_n2_accel_reintegration.csv`)
- Vong = 0.678·Vong0 up to t = 7.19 s; at 7.19-7.20 s Vong drops by 1.56 mm in one sample (1.39 to -0.17), after which the offset is removed manually while Vong0 stays at +2.03 mm. So the delivered post-event baseline is a processing step.
- In Vong0 the pre level is -0.04 mm and the post level +2.02 mm. The same +2.06 mm plateau already appears at 5.75-6.0 s, right after the downward lobe ends (5.54 s), and again at 7.25-7.5 s (2.03 mm). The baseline therefore stepped by about +2.06 mm near t = 5.7 s, and the lobe (max +4.8 mm at 6.15 s) sits on that step.
- Lobe size relative to the downward peak: 0.43 (tare), 0.30 (linear pre/post), 0.31 (cubic), 0.25 (step baseline at 5.69 s: +2.78 mm), 0.47 (Vong, +3.25 mm). So part (about 40 % of the amplitude) is baseline step, but a lobe of +2.8 mm (25 % of the peak) remains with timing (5.7-7.2 s) after the truck leaves the span. It cannot be classified as real (end restraint through the touching girder ends, or load on the adjacent span) or integration artefact.
- Raw acceleration: only DAT0034 (= N2) is available; N1.XLS was not downloaded. The DAT0034 vertical channel has zero mean, |max| 0.085 and only 1.3 % of its energy below 2 Hz; the 0-2 Hz component of d²Vong0/dt² has RMS 5.7 mm/s², about 6400 times the exported channel. Double integration gives correlation -0.18 to 0.02 with Vong0 for any scale. The exported channel is thus high-pass filtered/scaled and cannot reproduce or test the quasi-static deflection; re-integration with baseline correction is not possible from it. Needed: unfiltered SDA-830C N1 file with units [NEED VALUE].
- Gie Cuc, with a gap at each span end, shows no comparable positive lobe (maximum positive values are dead-band noise, <= 0.8 mm).
- Effect on the integral of PD N1 (raw channel, 3.4-7.5 s window): net -11.6 mm·s (linear baseline), -11.1 (step), -7.4 (tare only); the lobe takes 1.8-3.0 mm·s from the downward part.

## 4. Limitations
Single unknown truck per run; truck weight, speed, lane and girder unknown; channel gains differ by record and are undocumented; the series are quantised and partly manually processed (dead-band, scale, offset, 7.19 s step); only 5 records and 7 complete events; reference baseline (b) is itself an estimate; speed estimators assume a point-load or static-test-truck axle model with L = 25.7/17.5 m; event identification (which event is the test truck) is [NEED VALUE]. Nothing here validates the absolute P·C_m/v relation.

## 5. English draft: "Field records: baseline drift and quasi-static integral"
We examined five mid-span deflection records of moving-truck crossings on two simply supported bridges (Gie Cuc I, three 25.7 m spans; Phuong Do, two spans with a 17.5 m calculation length), sampled at 200 Hz for 15 s with an SDA-830C recorder. Truck weight, speed and lane were not recorded, and the deflection channel is derived by integration from acceleration with an undocumented gain; the records therefore test the signal-processing claims of Section 4, not the absolute value P C_m / v.

Seven complete crossings were identified. Fitting a quasi-static three-axle model to the low-pass component gave speeds of 27-36 km/h at Phuong Do, consistent with the stated 30-40 km/h, but 51-56 km/h at Gie Cuc, which is not; we report this discrepancy without resolving it.

For each crossing the integral of the deflection was computed with a constant tare baseline, a straight line between pre- and post-event quiet windows, and a cubic baseline fitted to all quiet samples. Over the 2-4 s event window the three agree within about 6 % for every crossing but one, and the cubic and linear choices agree within 4 %. The one exception is the raw Phuong Do N1 record, in which the baseline steps by 2.06 mm (18 % of the peak) as the truck leaves the span; the tare-only integral is 36 % below the linear-baseline value. The effect of a small offset grows with the integration time: over the whole 15 s record, tare-only integrals differ from the cubic-baseline values by 7-60 % at Gie Cuc, 34 % for Phuong Do N2 and -170 % (sign reversal) for Phuong Do N1, corresponding to equivalent offsets of 0.04-1.3 mm. This is the behaviour predicted by bias = eps0 T_record / integral, with eps0 of a fraction of a millimetre and an integral of 5-12 mm s. Conversely, high-pass filtering at 0.1 and 0.5 Hz changes the event integral by -44 to -83 % and about -100 %, so it cannot serve as baseline correction when the integral is the target.

A zero-phase low-pass filter at 2 Hz (about one third of f1 = 5.2-6.0 Hz) leaves the event integral unchanged to within 0.1 % (0.2 % at 3 Hz) for complete events, while removing dynamic peaks of up to 17 % of the quasi-static peak; the dynamic residual integrates to 0.1-2 % of its absolute integral. The integral is therefore insensitive to the dynamic component, although part of this follows from the unit DC gain of the filter.

Normalised integrals v times the integral vary by 26-33 % across spans and events, but the channel scale factors relating processed to raw series range from 0.67 to 5.15, so this scatter cannot be attributed to the bridge or to the truck. The positive lobe of Phuong Do N1 (+3.25 mm) is partly a baseline step (about 40 % of its amplitude); a residual of about 25 % of the downward peak remains and cannot be classified as physical or artefactual, because the exported acceleration contains no quasi-static content.
