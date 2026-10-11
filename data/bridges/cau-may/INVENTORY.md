# Cau May (Hai Duong, DT389) - field-test data inventory

Drive folder "Cầu Mây gửi Thái Sơn", id `1svwpCI8BweSyfOxUUA8AH9gBpQKyu6--`. Inventory date 2026-10-11. Only data actually read is recorded; everything else is marked [NEED VALUE] or "not read".

## 0. File tree (size in bytes, Drive id)

```
Cầu Mây gửi Thái Sơn/                       1svwpCI8BweSyfOxUUA8AH9gBpQKyu6--
├── File Thiết kế cau May (sau tham dinh)_29-6-2019.rar   151,331,197   1j8zJOHkWD7Sfo4WChZdvRbuuBQFczGUk   (NOT READ: archive, design file after appraisal 29-6-2019; may hold drawings / MIDAS model)
├── Đề cương kiểm định/                      1sP8uw6gbUK32gF2s7HA_ImOph4WAEyJo
│   ├── 01 - Bia.doc                         39,936      1FlMjAhFl-GlFUP6Cs7PL1SU-TaHghvNN   (cover, not read)
│   └── 06 - De cuong KDCL cau May.doc       595,968     18MAe-NjPT5w5BurG0oCp_WTLBEAhs7Ko   (READ: test plan)
└── 09 - Báo cáo kết quả kiểm định/          1wqzSqPF9SQb1T1_gkHFjkHHen00f3b_a
    ├── 01 - Báo cáo kiểm định cầu Mây 20200730 (TRANG IN).pdf   10,648,381   1Hr4cAlZxpEQEZLbudIAYmSj_rZSZdXKU   (READ: authoritative final report)
    ├── 01 - Báo cáo kiểm định cầu Mây.docx                      28,760,839   1Rj2PxI2_TwnZxpC7PJaGd75_m9fzjZ1K   (READ: earlier draft, see warning)
    ├── 02 - 01 - Bật nảy cầu Mây.pdf        122,168     1ZBAmWUjXJzAJuBwcKpr7-FVlfWreIDoP   (rebound hammer, not read)
    ├── 02 - 02 - Siêu âm cầu Mây.pdf        121,543     1UDeXvuloiHRWhIjXm2oxAfCuTcA5Pc3s   (ultrasonic, not read)
    ├── 02 - 03 - Chiều dày BT bảo vệ cầu Mây.pdf  141,563   1fEFeBcJFiPg5A7eSghll950SdJFoknDJ   (cover depth, not read)
    ├── 02 - Đo cao độ mặt cầu.xlsx          41,590      1n01c1a6c1U3Oz8Y-mp3h0W44YvBRD-f4   (deck levelling, not read)
    ├── 04 - Đo tĩnh - Cầu chính.xlsx        131,980     1VQKKFnDWtzv4we3aeNk_BGpA3zENvER6   (READ: main-bridge static test, key file)
    ├── 04 - Đo tĩnh - N1.xlsx               2,531,777   1Ckf8l3tVrwTmlPrRThmPyVTxzmBy36r3   (READ: approach span N1 static)
    ├── 04 - Đo tĩnh - N15.xlsx              1,023,595   1KdMAU4wNjuqEumVyYltM85EvvIqiYWy7   (approach span N15, not read; PDF has its results)
    ├── 04 - Đánh giá tải trọng cầu chính.xlsx   2,374,528   1UyEoWhBQGwQcYrEmrUD6nu17360h4_q3   (LRFR rating, xlsx not read; read via its PDF)
    ├── 04 - Đánh giá tải trọng cầu chính.pdf    1,888,378   1HNyul9T5k12wWprgo9gNZMh-w0qRNyWw   (READ: section properties, E, loads)
    ├── 04 - Đánh giá tải trọng cầu dẫn.xlsx     993,774     1TTUQ_xq-UK3Z4Du8waYIcUq8cYIfVh4M   (not read)
    ├── 04 - Đánh giá tải trọng cầu dẫn.pdf      333,039     1iqR5UnGTf9Cdl5PV168eH7_lVyn7k4ME   (not read)
    └── 10 - Đo động.xlsx                    11,084      1pAqzc9OrsChOTY5kD8S0-NzYyAyhAhYC   (READ: only a table of abutment/pier vibration, no time series)
```

Warning on the .docx: the text is an earlier draft that is internally inconsistent with the PDF/xlsx (e.g. approach-span N1 "measured" deflections 2.8-3.6 mm in docx vs 9.4-11.4 mm in `04 - Đo tĩnh - N1.xlsx`; truck count 9 vs "up to 10"). Use the PDF (30 Jul 2020 print version) and the xlsx files as the source of truth. The parts of the docx I read were 77k characters; full text was extracted, images not examined.

Extracted CSVs (only numbers that were read): `cau-may_main_static_deflection.csv`, `cau-may_approach_N1_static_deflection.csv`, `cau-may_span_dynamic_properties.csv`, `cau-may_truck_and_dynamic.csv`.

## 1. Bridge type and structural system

- Cau May, DT389 over Kinh Mon river, Kim Thanh / Kinh Mon, Hai Duong. Built ~2019-2020 (design approved 28/6/2019); acceptance load test and baseline ("state 0") in June 2020 (strain logger timestamps 19/06/2020), report dated 30/07/2020. Client: Hai Duong PMU; tester: Cong ty TNHH Tu van Dai hoc Xay dung (HUCE consultancy). Source: PDF sec. 1, `06 - De cuong`.
- Total layout (plan): 39.15 + 3x40 + 39.15 | **55 + 90 + 55 m** | 39.15 + 5x40 + 39.15 m, total 684.75 m. Width 12 m (2x3.5 m lanes + 2x2.0 m mixed lanes + 2x0.5 m kerbs). Design load HL93.
- **Main bridge = 3-span continuous prestressed concrete box girder, balanced cantilever, 55+90+55 m**, f'c = 45 MPa, Ec = 36,057 MPa (LRFR file; TDS strain sheet uses 36,057 MPa), girder depth 2.40 m at midspan, 5.40 m at pier (variable EI, NOT equal-stiffness prismatic). Spans: N6 and N8 = 55 m side spans, N7 = 90 m centre span (L2/L1 = 1.636); piers T5..T8, T6/T7 monolithic with the box, T5/T8 movable pot bearings (LRFR file 3.3.1). Pot (gối chậu) bearings on main span.
- Section properties (`04 - Đánh giá tải trọng cầu chính.pdf`, midas-style output): midspan A = 7.233 m2, Ixx = 11.756, Iyy = 5.482, Izz = 64.482 m4; near-pier A = 14.437 m2, Ixx 74.456, Iyy 59.612, Izz 90.826 m4; on-pier A = 29.945 m2, Ixx 114.287, Iyy 79.814, Izz 116.734 m4. Which of Ixx/Iyy is vertical bending is not labelled in the text I read (z spans the 2.4 m depth, y the 11.7 m width, so vertical-bending I is probably Iyy = 5.482 m4 at midspan: [NEED VALUE, confirm]). EI(x) is therefore available only piecewise; a full variable-section EI table would have to come from the MIDAS model in the .rar [NEED VALUE].
- Approach spans: 12 simply-supported prestressed Super-T girders (L = 38.3 m effective, H = 1.75 m, 5 girders at 2.35 m spacing), deck slab cast in place and made thermally continuous across piers ("bản liên tục nhiệt"), elastomeric bearings. Two spans were tested: N1 and N15.

## 2. Test vehicles

- Nominal 3-axle truck, ~25 t gross (PDF Hình 2.1): front axle 5 t, two rear axles 2x10 t; front-to-middle axle 3.60 m, middle-to-rear 1.35 m, track 1.85 m; clear distance rear axle of one truck to front axle of next truck in a row = 6.00 m.
- Individual truck weights/weighbridge tickets: [NEED VALUE] (report only states "approx. 25 t"; plan allows 25-30 t and says "9 trucks"/"10 trucks", 25 truck-shifts in total).
- Static convoys: approach span 6 trucks (3 rows x 2); main bridge up to 10 trucks: Scheme III = 4 trucks, midspan-region of side span N8 (loaded length 55 m figure); Scheme IV = 6 trucks on centre span N7; Scheme V = 10 trucks (side span + centre span, 45 m / 22 m offsets) for the pier section T7. Transversely two arrangements: centric (symmetric about axis) and eccentric (outer wheel 0.6 m from kerb). Exact longitudinal truck coordinates exist only as drawing (Hình 2.5, 2.7, 2.8), not as numbers [NEED VALUE].
- Dynamic: a single truck (~25 t) at 30-40 km/h, with abrupt braking over abutment/pier tops for substructure tests.

## 3. Measurement

- Main span deflection: 3 points per section (right line, axis, left line). N7 at midspan (closing segment); N8 at 0.4L = 22 m from span end (plan and PDF sec. 2.1.1.4c), although tables label it "giữa nhịp N8". Instrument not named in the text read (plan lists "indicateur + gá" and total station/level) [NEED VALUE].
- Strain (stress) in the box: TDS-303 data logger, 10 gauges per section inside the box, sections: midspan N8, midspan N7, on pier T7, plus deck-slab crack-width/strain at N7, N8 (`04 - Đo tĩnh - Cầu chính.xlsx`, sheet "Số liệu TDS": 17-20 channels, ~55 timed readings at 3 readings per load step, 19/06/2020 09:48-11:23, 12 load steps interleaved with 5 zero readings).
- Approach spans N1/N15: girder midspan deflection by dial gauges + strain.
- Dynamics: SDA-830C vibration recorder, 3 directions (vertical, longitudinal, transverse) at midspan of N1, N5, N6, N7, N8, N9, N15; piers T1, T5, T6, T7, T8, T14, abutments M1, M2. Sampling rate: not stated anywhere I read [NEED VALUE]. Traces are in the PDF appendix as figures (not tabulated).

## 4. Load cases and data form

- Static: convoy parked at fixed positions (centric / eccentric) in 3 loading repetitions with zero readings between (Thế tải 1-12; raw strain table in `04 - Đo tĩnh - Cầu chính.xlsx`). Deflections reported as one peak value per measuring point per load case (12 numbers for main bridge, see CSV). **No deflection influence-line series (truck at many positions) and no moving/crawl record in the files read.**
- Dynamic: only vibration properties and a dynamic increment (1+IM = 1.20-1.33) are tabulated; the raw SDA-830C time histories appear only as plots in the PDF appendix (not extracted; PDF figures could be digitised, low accuracy). No separate raw file in the folder.

## 5. Theory / FE vs measured

MIDAS (spatial beam model, with as-built survey) deflections: N8 -5.93 mm, N7 -16.70 mm for both centric/eccentric (symmetric load assumption). Measured/theory = 0.88-1.00 (axis line: 0.938 at N8, 0.913 at N7; N7 diff 0.2-12.5 %). Approach N1: measured/MIDAS = 0.79-1.00 deflection, stress 3-20 % below FE. Full table: `cau-may_main_static_deflection.csv`, `cau-may_approach_N1_static_deflection.csv`. Strain: measured 0.3-1.2 MPa-scale values vs MIDAS 0.34-1.77 MPa, differences 2-39 %.
The workbook also contains MIDAS element stresses for the loading cases showing opposite-sign bending in adjacent spans (e.g. under N8 loading: bottom fibre N8 +1.22 MPa vs N7 -0.54 MPa; under N7 loading: N7 +1.77 vs N8 -0.93-ish and T7 -1.12 to +1.63), i.e. the continuous-beam sign reversal is present in the model and in the recorded strains of unloaded neighbouring spans.

## 6. Natural frequencies measured (vertical, midspan, truck-excited)

N1 3.11, N5 3.03, N6 3.43, N7 3.64, N8 3.63, N9 3.09, N15 3.04 Hz (CSV `cau-may_span_dynamic_properties.csv`); pier/abutment frequencies in `10 - Đo động.xlsx` (e.g. T7 vertical 3.47, M1 8.57 Hz). Dynamic amplification 1+IM 1.20 (N8) - 1.33 (N5).

## 7. Assessment

| Test of the paper | Rating | Why / extra work |
|---|---|---|
| (a) Deflection-integral invariance (∫y dx = P·C_m) | **Low** | No crossing record of deflection and no influence-line series; only static peaks. A crossing record exists only as SDA-830C plots (single truck 30-40 km/h, midspan N7/N8) in the PDF appendix. Needs: raw SDA-830C files from authors, or digitised plots (poor accuracy, unknown channel units, sampling rate and whether channel is acceleration or displacement), truck weight and speed. |
| (b) SLM with two trucks/convoys | **Low-Medium** | Trucks identical (5+10+10 t), convoys of 4/6/10 trucks, but all static and on different spans; no pair of moving crossings of different vehicles. Could only check proportionality of static response to total weight (not the paper's integral). |
| (c) Sign change on adjacent spans | **Medium** | Real 55+90+55 continuous bridge; MIDAS and raw strain channels in unloaded neighbour spans (N7 channels while only N8 is loaded) exist and give the reversed-sign signal (strain, not deflection). Needs processing of `Số liệu TDS` block (channel-to-section mapping must be reconstructed from header row, partly ambiguous) and ideally deflection of the neighbour span (not reported). |
| (d) C_m by uniform-load equivalence | **Medium** | Section properties and E give piecewise EI; the MIDAS model (in the .rar, not opened) would give C_m at the N7 and N8 sensors, which is directly comparable with the measured static deflections (ratio 0.88-1.00 shown). Static data cannot test the integral itself. Needs EI(x) table, bearing stiffness, the exact truck coordinates. |

Overall: **Medium as a field-case study of a real continuous box girder (BPM-style check of FE/EI against measured deflections, adjacent-span sign change), Low for the paper's central claim** (crossing-integral invariance) unless the raw dynamic/crossing records are obtained. Note the girder is strongly non-prismatic, which is a deviation from the paper's constant-EI model (needs FE-based C_m, i.e. the BPM must use the variable-EI influence line). Not read: the .rar design archive, N15 xlsx, the cover sheets, the three material-test PDFs, deck levelling xlsx, approach LRFR files.
