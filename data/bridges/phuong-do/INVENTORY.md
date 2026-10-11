# Phuong Do bridge (Km295+870, QL2, Ha Giang) - Drive inventory

Drive folder "2018 - 04 - cau Phuong Do", id 1xOxvMlGh2A1sNdxbKJLDsvgF_ESRm6-C (owner vuthaison@gmail.com). Inventoried 2026-10-11.

## 1. File tree (sizes in bytes, Drive ids)

```
2018 - 04 - cau Phuong Do  [1xOxvMlGh2A1sNdxbKJLDsvgF_ESRm6-C]
+-- 01 - Ho so quan ly cau Phuong Do  [1NQv5w-QzmBth7XMBUmvKNrUvaillcGTK]   (23 site photos, JPG 2.7-3.6 MB each, 20180305_0856xx-0910xx; not opened)
|     ids e.g. 1I5clTNhpNZWKMjFr4ZVKglpMt7H2ymss (20180305_090015), 1b0zSjYOYZCaU2v2qzqpB2pR4DVQUZxBy (_085647) ...
+-- 02 - De cuong kiem dinh cau Phuong Do, cau Thanh Thuy  [1wStvLX_ggK62W4skIaSl4px5pwsAmtEV]
|     01 - De cuong 2 cau QL2.doc            773,632   1PIy9PxDKX928VmtcI-_0i3U1BSuSMUki   (test plan; text skimmed via grep)
|     00 - Cau Phuong Do.dwg                 813,624   1BNOMN2PODMEHWmZpsMUin5vcEBil8-hO   (not read)
+-- 04 - Bao cao KD cau Phuong Do  [1S92lSVGR_3IiP4wVMbRJuHeoKyzZudCq]
      01 - Bao cao kiem dinh cau Phuong Do - thay Moi.docx   139,966  1w1QpOq3E2-8rrOLLvIjF4odbgBjiXrxs  (MAIN REPORT, read fully)
      01 - Do tinh - Phuong Do T18.xlsx      114,939  1csfZVQbsY6Ij2_RTT67m7Lp8RnEHgf_q  (static test data + Midas results, read)
      01 - KQ do dong Phuong Do.xlsx          16,139  1LhsUMEC4wS3vRwnKC4e47v9-vsIcj5an  (dynamic summary, read)
      Vong dong Phuong Do.xlsx               291,757  1kej9mq7c_FQs6mcTWnVDtYh2VY6S6a3U  (DYNAMIC DEFLECTION TIME HISTORIES, sheets N1, N2; read)
      N1.XLS                               2,236,928  1WTTjiTH_4D2qiU8mKBDqONElh9APphfT  (raw SDA-830C records; NOT downloaded - same format as N2.XLS presumably)
      N2.XLS                               1,369,088  1lrlSETVNPxDm7_o1_SFwx3IUGu1N_LPw  (raw accelerations, file DAT0034.wvd; read)
      01 - Tinh he so phong dai cau Phuong Do.xlsx  21,834  1_JkTkNoU4FNiAvqKuf8SoGwNb0YBI4N6  (read)
      01 - Tong hop ket qua thi nghiem Cau Phuong Do.docx  43,087  1kVtx7vr2DP7HALF5HHmHYCRmGfoGq_qq (concrete tests only, read)
      04 - Kiem toan cau Phuong Do T18.xlsx  357,994   1z0sgpFPtzarXdGLEH0DxjybKcEeeQKuP  (LRFR rating; NOT read)
      02 - CauPhuongDo-N1-T18m.mcb           274,080   1CuwUsb_1pzQEokcpj-qhvUJHIFAKOJ4S  (Midas Civil model; NOT read, binary)
      05 - Phu luc bieu do dao dong cau Phuong Do.docx  681,845  12aI0lj8ahwmgD182eZk3EbtLnbNS_HbD (only image charts; text empty)
      06 - Phu luc anh cau Phuong Do.docx   2,231,643  1JUnroYIPiAdtYwS2ybiKsICEt9nGtHFZ  (photos; NOT read)
      06 - Phu luc anh cau Phuong Do 2.docx   775,027  1DmJKQn1NoM08nTp-B96kYyRtwb3NscGB (photos; NOT read)
      Cau Phuong Do _ cad 2007.dwg          713,440  1th9bAAQZbCIjsuV6PoQZHJv9ngw8SqXP (not read)
      00 - Cau Phuong Do.dwg                764,709  1vnrKtaN2-C5wZtv3U6Gtbx1kXMwW3oyr (not read)
      01 - Cao dac cau Phuong Do.xlsx        38,027  1XS0YfLdScnS35L4XaMjWiPN-qeKZPrFu (levelling; not read)
      Xu ly so lieu ... do dong nhat cua be tong.xlsx   80,472  1StR8rQd71gMScDcgwFgosu0CjJVWIwgM (concrete; not read)
      Xu ly so lieu ... chieu day lop BT bao ve.xlsx    81,849  134jvjo2IBcMt2Zn-J7OcXKu_wYsf2IOU (concrete; not read)
      Xu ly so lieu ... cuong do be tong.xlsx           83,894  1Bq568FQfXilLas_W6b9aQlh33sYJ-Sbc (concrete; not read)
```
Saved CSVs (this directory): `vong_dong_N1_midspan_deflection_timehistory.csv`, `vong_dong_N2_midspan_deflection_timehistory.csv`, `N2_DAT0034_raw_accel_ch2-4.csv`, `static_midspan_deflection_N1.csv`.

## 2. Findings

### F1. Structure
- NOT continuous. Report section 2: "02 nhip gian don BTCT lap ghep (2x18) m", total length given as 52.15 m in one place and 55.15 m in another (report inconsistency), built 2005 (in service), tested Oct-Dec 2018 (contract 10/10/2018; photos 5 Mar 2018 from earlier visit). Calc span 17.5 m (Midas/xlsx).
- 6 precast RC T girders per span, h = 110 cm, spacing 2.10 m, 3 cast-in-situ diaphragms (23 x 78 cm), deck width 12 m (11 m carriageway), design load H30-XB80, steel bearings (24x30x8 cm), steel finger expansion joints, RC abutments and a solid RC pier T1.
- Midas girder data (xlsx "Tinh he so phong dai"): I = 0.08324 m^4, E = 29,939,483 kN/m2 (f'c 31 MPa) or 31,500,000 (note says "thay Moi noi"), x0.8 factor suggested by the lead. So EI is available (~2.49e6 kN m2 uncracked, about 2.62e6 with 31.5 GPa).
- Damage: all girders cracked (flexural 0.15-0.27 mm); upper bearing plates displaced up to 4 cm at M1 and T1, girder ends of N2 at pier T1 touch N1 with no gap (partial longitudinal restraint; potential unintended continuity); expansion joints clogged. Deflection camber measurements (Table 3): D1 -17.5, D2 -10, D3 +2, D4 +3, D5 +3, D6 -18.5 mm.

### F2. Vehicles
- Static: 3 trucks, 3 axles (3-axle rigid), 24 t each: front axle 4.8 t, rear two axles 9.6 t (total for the two rears, report column "Trong luong hai truc sau"); axle spacings 3.9 m (front-middle) and 1.36 m (middle-rear); wheel gauge 1.85 m. Midas spreadsheet uses wheel loads 47.088 kN (front) and 94.176 kN (each rear wheel pair... as entered) i.e. per-wheel 2.4/4.8 t.
- Dynamic: "xe tai thu" at 30-40 km/h (plan said 20-40); number of runs, vehicle(s) and weight for the dynamic runs NOT stated: [NEED VALUE]. Plan states 1 truck per run, at least 3 runs per position.
- No second, different truck/convoy weight reported => no SLM with two vehicles.

### F3. Measurements
- Static (N1 only, mid-span of all 6 girders): leveling/deflection "vong ke" (deflectometers), mechanical strain gauges (tenzomet) for crack opening (bottom flange + slab underside) and strain in diaphragms. Camber by level.
- Dynamic: SDA-830C vibration recorder (Japanese 3-axis), midspan of N1 and N2 (only one girder, which one not stated: [NEED VALUE]) in 3 directions, 200 Hz (5 ms) sampling, 15 s records (3000 pts); accelerations also at abutments M1, M2 and pier T1.

### F4. Load cases
- Static: two layouts only (centric = 3 trucks side by side per 3 lanes; eccentric); loads placed with truck rear/mid at mid-span. 3 repeated readings (plus a trial). Only peak values at one truck configuration. NO influence-line series, NO truck-position sweeps (the xlsx has influence-line coordinates for design checks only: ordinates e.g. 0.75, 1.0, 2.9, 4.0 ... m with transverse distribution values, not measured).
- Dynamic: moving pass at 30-40 km/h. Time histories exist in "Vong dong Phuong Do.xlsx" (see F5b).

### F5a. Static results (all read; see static_midspan_deflection_N1.csv)
Measured mid-span deflections N1 (mm): centric D1..D6 = 2.42, 3.64, 4.20, 4.36, 3.83, 2.55; eccentric = 3.29, 4.21, 4.03, 3.81, 3.06, 1.80. Report FE (Midas 6-girder model) centric 3.47, 4.41, 4.98, 4.98, 4.41, 3.47; eccentric 4.99, 5.24, 5.15, 4.58, 3.49, 2.17. Differences (measured below FE) 12-34 %. Sum of measured centric: 21.0 mm vs FE 25.7; the xlsx quotes a different FE set (Midas first run 3.88, 5.02, 5.71 ...) with 23-41 % differences; the xlsx "Tinh he so" also contains H30/XB80 Midas runs (node 115-120 DZ). Theoretical amplification factor computed 1.201; dynamic increment (1+IM) = 1.126 (N1), 1.095 (N2).
- Rating: HL93 RF(IR) at mid-span 1.24 (report Table 18).

### F5b. Dynamic time histories ("Vong dong Phuong Do.xlsx", sheets N1, N2)
Columns: Data No, Time (ms), Vong0 (mm), Vong (mm); 3000 points at 5 ms (15 s). Vong0 = raw dynamic deflection (double integrated from acceleration, drifts); Vong = corrected series. Min of Vong equals the report ymax (N1 -7.60 mm, N2 -7.20 mm), so Vong is the series used in the report.
- N1: event from about 3.7 s to 7.2 s, peak -7.6 mm at 4.27 s, then a POSITIVE lobe up to +3.25 mm at 6.15 s (about 40 % of peak) before returning to baseline -0.18; Vong0 ends with +2 mm offset (drift). Integral of (Vong - baseline) over the window: about -4.7 mm.s (negative part -8.4, positive part +3.7).
- N2: event from about 1.9 s to 5.6 s, peak -7.2 mm at 3.18 s, small rebound +1.37 mm; integral about -8.9 mm.s (negative -9.7, positive +0.8).
- Unknown: truck weight, speed, lane/transverse position, girder measured, whether the runs are same vehicle in the same lane. Sensor is on one girder of a 6-girder deck.
- Integral sanity check (order of magnitude only): single-girder simply supported beam, L = 17.5, EI = E*I (29.9e6*0.0832): C_m = 5L^4/(384EI) = 4.9e-4 m per (kN/m); P = 235 kN (24 t) gives P*C_m = 115 mm.m for the whole cross-section; at v = 9.7 m/s (35 km/h) and transverse share ~0.5-0.6 this is ~6-7 mm.s expected for the girder. Measured 4.7-8.9 mm.s is the same order. This is a plausibility check, not validation, because P, v, and share are not known.
- N2.XLS: raw 3-channel acceleration (file DAT0034.wvd, CH 2/3/4 = vertical / longitudinal / transverse labelled "Dung/Doc"; amplitudes only ~0.08 mm/s2 in the vertical channel so units/scaling must be checked: [NEED VALUE] for conversion). Saved as N2_DAT0034_raw_accel_ch2-4.csv. N1.XLS not downloaded (1.8 MB text).

### F6. Frequencies (Table 12/13, "KQ do dong")
Vertical: N1 5.184 Hz (T = 0.193 s), N2 5.552 Hz; longitudinal 7.052 / 6.882; transverse 6.231 / 6.670 Hz. Abutment/pier: T1 4.72 (long), 4.525 (vert), 4.511 (trans); M1 4.444/5.187/4.728; M2 4.938/5.405/4.762 Hz. Dynamic amplification measured 1.126 (N1), 1.095 (N2) < 1.25.

### F7. Assessment for the paper
Overall rating: MEDIUM-LOW as a validation of the continuous-beam theory (it is simply supported), but MEDIUM as a real field crossing record for the integral-invariance claim.
- (a) Deflection integral = P*C_m: Medium. Two complete mid-span crossing records (N1, N2 at 200 Hz) exist. Needs: truck weight and speed for the runs (from plan/report or ask Prof. Moi / Dr. Bao), transverse position, girder id, and a decision on which series (Vong vs Vong0) is valid; Vong appears baseline-corrected (the positive lobe in N1 may be integration/high-pass artifact or real partial restraint through the touching beam ends). C_m from EI (BPM) is computable: L = 17.5, EI ~ 2.5-2.6e6 kN m2, but cracking and 6-girder load sharing require a grillage/FE factor (the Midas model .mcb exists, not read). Alternatively use sum over all six girders (not measured dynamically).
- (b) SLM two trucks: Low. Only one 24 t truck class; no second known weight. Possible only if N1 and N2 runs were by different loadings (unknown).
- (c) Sign change / negative adjacent-span influence: Low-Medium. Spans are simple, so none expected, but the 4 cm bearing shift and zero gap at pier T1 mean some end restraint; N1 positive lobe (+3.25 mm) could be evidence of partial continuity OR an artifact; raw acceleration needed to decide. Not a clean continuous-beam test.
- (d) C_m via uniform-load equivalence: Medium-Low. The report itself computes an equivalent uniform load q = 8.9 kN/m from 5qL^4/384EI and measured 4.36 mm (with E 29.9 GPa; EI back-calculation consistent with measured stiffness 12-34 % higher than FE). Static data are single-configuration peaks, so only a stiffness check is possible.
- Hence for the paper: use Phuong Do as an additional field example of a simply supported multi-girder bridge with moving-truck deflection history (integral sanity), clearly stated limits, NOT as evidence for continuous-bridge blind-ratio claims. Still worth checking the sister bridge Thanh Thuy (Km309+632) in the same Drive project (not in this folder) and other years' folders for continuous spans.
- Not read: Kiem toan xlsx (LRFR), .mcb, .dwg, photo appendices, concrete-test xlsx, N1.XLS.
