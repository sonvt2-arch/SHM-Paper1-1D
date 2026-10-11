# Inventory: "2021 - 05 - Kiểm định cầu Lạng Am - Hải Phòng"
Drive folder id 1vcoz529deyDZDMxknLYfxK8NEdUg_PMe. Listed recursively (all pages). Inventory by Claude via Drive connector; only the three Word/text reports below were read in full or in the relevant parts. [NOT READ] = not opened.

## 1. File tree (size, Drive id)
```
2021 - 05 - Kiểm định cầu Lạng Am - Hải Phòng/   (1vcoz529deyDZDMxknLYfxK8NEdUg_PMe)
├── 10. Báo cáo kiểm định/   (14rtqL6a7m_LVtHBYBO7FIsj5fZ8KwQJe)
│   ├── 01 - Báo cáo kiểm định cầu Lạng Am - 00 Báo cáo.docx          645,590 B   1IRzsxC7iDgwO_te3stJ3l40S1NA_mmps   [READ, main source]
│   ├── 01 - Báo cáo kiểm định cầu Lạng Am - 01 Phụ lục đo động.docx   464,994 B   1D1wuU00d1A-ZAn8tMmHAWc9egLLeJjJQ   [READ: only frequency tables survive text extraction; waveform plots are images]
│   ├── 01 - Báo cáo kiểm định cầu Lạng Am - 02 Phụ lục ảnh.docx     26,348,343 B   1yk3TOvLncJSXD4qQyPorpclcY4GP-hqu   [NOT READ, photo/sensor-layout appendix]
│   └── 01 - Báo cáo kiểm định cầu Lạng Am.pdf                       3,502,382 B   1J4YgdZ3y7lATFSOsgt7ZUXEHokAyLOCP   [NOT READ, assumed = combined report]
├── 02. Đề cương, dự toán/   (1mwxZx1m0JwwoeCV4zd4-LR-ImSrPJF3X)
│   ├── 20200923 - Đề cương kiểm định cầu Lang Am.doc                  670,720 B   1MhFC3azZ1t-QHFsZMb8v2gh70J9Y44xF   [READ via keyword scan]
│   └── 2. Nhiem vu Goi16 - Kiem dinh va thu tai (Binh).docx           430,967 B   1HayzRojmiKA_vHSmaJy94foD4zPSKx2T   [NOT READ]
└── 01. Bản vẽ/   (1mtxmD6QEa7xu7DGgIKOEzwmLCWgEHkc5)
    ├── plot.log                                  171 B        1UKgslLy6lxych5tgK6JZsjUOlzjoS6cV   [READ, irrelevant CAD plot log]
    ├── T.Minh cau Chanh Duong - final 10-9-2020.doc   2,269,696 B  1t4FZmNlNiMKcg4gnGOlbKMkjALyhHYht  [NOT READ, design explanatory note]
    ├── T.Minh Thai Binh - 10-9-2020.doc               2,403,840 B  1LZZj8e5R0HtDuHVhP6-bAZkVOFLdgE39  [NOT READ, design explanatory note; likely holds EI/section data]
    ├── TẬP 2-2 CẦU THÁI BÌNH.pdf                      289,231,113 B 1fLsY3iHvgTLmBqpoc4PaFVaeyzvVA44w  [NOT READ, design drawings]
    ├── BTC cau BVTC-bỏ địa chất.dwg 3,123,969 B 1MUXSjCKHWUCOQdk1ZdgCjdnodn4Sqik8 ; .bak 3,011,979 B 1wRIgfLpewZ2Vcbnsl4xo-x8waDPMyfNj
    ├── MCN cau BVTC.dwg 5,854,049 B 1e1_wWAu86jL0ahtOuikuVqlv2oK4wTnR ; .bak 5,795,325 B 1HewH3RULA5x3cRCFbn3S7mk9V82XBh7c ; MCN cau BVTC_recover.dwg 3,248,118 B 14BSRO4qwbOBQEtj-kNpaND167UASRkIx
    ├── BTC cau BVTC.dwg 3,279,264 B 1hyvcbHW-LjOJWopMWRKcPB2ArIfIHP0_ ; BTC cau Chanh Duong - BVTC.dwg 4,703,168 B 1YXYvccoHcxJRQyn1-RrVTwFCJiY6YhgE
    └── TOPO LangAm_10-12.dwg 6,131,808 B 1uyJImOE2npRSAXmDGW-_m2wrGBe6T-zy ; XR_BinhDo.dwg 2,778,642 B 17jwrlfJx1gTjZsZTxX0rZXo_DArgehkU   [all DWG NOT READ]
```
No .xlsx, no raw sensor data, no CSV/time-history files in the folder. Everything measured is in the report as summary tables and (image) plots.

The report is "Báo cáo thử tải, kiểm tra chất lượng công trình (Đợt 6)", Hà Nội 04/2023, by Công ty TNHH Tư vấn Đại học Xây dựng (HUCE). Two bridges: Chanh Dương (small) and Thái Bình (large). (Folder name says 2021-05; the test report is dated 2023; the docx files date 2023-09.)

## Findings

### 1. Structural system (00 Báo cáo.docx, "Giới thiệu về dự án")
- **Cầu Thái Bình (Km7+155), L = 987.9 m, 26 spans**: (2x20+35+7x40+39.15+(42+63+42)+39.15+8x40+35+2x20) m. Deck width 12 m.
  - **Main bridge: ONE 3-span CONTINUOUS PC box girder, 42+63+42 m (spans N12, N13, N14, piers T11-T14)**, balanced cantilever. Piers T12, T13 monolithic with girder, T11/T14 pot bearings (gối chậu thép). Single-cell box, depth variable 4.0 m (pier) to 2.0 m (midspan), parabolic soffit; bottom width 4.8 to 5.759 m; top slab 11.7 m; web 600 to 250 mm; top slab 220/250 mm. Prestressed concrete. EI not given (variable section, no explicit EI in the test report) [NEED VALUE; section properties likely in "T.Minh Thai Binh - 10-9-2020.doc"].
  - Approaches: 19 simply supported Super-T spans 35-40 m (5 girders, h 1.75 m, 2.3 m spacing), 4 hollow-core slab spans 20 m (12 slabs, h 0.75 m), rubber/pot bearings.
- **Cầu Chanh Dương (Km5+740)**: Lc = 74.75 m, 5 cast-in-place RC slab spans + 4 simply supported PC hollow slab spans of 18 m (12 slabs, 1 m pitch, h 0.65 m), elastomeric bearings. Not continuous. (Report mostly deals with Thái Bình in the load-test tables.)
- Design load HL93 (TCVN 11823-2017). Test year 2023 (April).
- Note: the main box is continuous with span ratio 63/42 = 1.5 (L2/L1 = 1.5, not 1.457, but variable depth and fixed piers T12/T13 make it a rigid-frame-like continuous girder, not a simple beam on rigid supports).

### 2. Test vehicles
10 four-axle trucks, gross (incl. cargo): 31.02, 31.59, 29.20, 31.72, 31.22, 30.40, 30.50, 29.85, 29.22, 30.59 t (sum 305.31 t, mean 30.53 t) -> test_trucks.csv. Axle spacings 1.80 + 3.00 + 1.35 m (total wheelbase 6.15 m), wheel track 1.85 m. **Individual axle loads not given** [NEED VALUE]. Which plate was in which load scheme: not stated in text (figures only) [NEED VALUE]. Same 10 trucks reused for all schemes.

### 3. Measurements
- Deflection: võng kế (mechanical dial deflectometers/"đồng hồ", readings 0.01 mm), under girder soffit; Super-T 5 points/span, hollow slab 12 points, box 3 points/span (right edge, centre, left edge) at mid-span of N12, N13, N14 (the Đề cương planned 0.4L for the 42 m side spans; the report says mid-span, treat as [NEED VALUE: confirm in sensor-layout figures]).
- Strain (strain gauges, bottom fibre; box sections also near piers T12/T13 for schemes 7/8), crack opening of slab (tenzomet).
- Dynamic: SDA-830C vibration meter, 3 directions, mid-span of N2, N4, N11, N12, N13, N14, N24; single truck at 30-40 km/h (scheme 9); piers T1,T2,T11-T14,T23,T24 and abutments M0,M1.
- Static zero-load camber survey (level) of soffit at 3 points per girder (Tables 1-4).

### 4. Load cases
- **Static, parked trucks, one deflection reading per case** (loaded then unloaded; not a crawl pass, no influence-line series). Schemes (all in 2 longitudinal rows, per-lane, symmetric "đúng tâm" and "lệch tâm" transversally):
  - Sơ đồ 4: 4 trucks in span N12; Sơ đồ 5: 6 trucks in span N13; Sơ đồ 6: 4 trucks in span N14 (deflection + strain). Sơ đồ 7/8: 10 trucks near piers T12/T13 (strain only). Sơ đồ 1-3: slab N2 (2 trucks), Super-T N4, N24 (6 trucks).
  - Longitudinal truck positions are shown only in figures [NEED VALUE].
- **Dynamic**: one truck, 30-40 km/h, mid-span records by SDA-830C. Waveform plots exist as images in "01 Phụ lục đo động.docx" (text extraction only returned frequency tables). Text gives only ymax/ymin and (1+IM) (Bảng 23). Sampling rate not stated [NEED VALUE]. This is the only moving-load record in the project, and it contains a full crossing dynamic deflection/acceleration time history at least in principle (device-dependent: SDA-830C is an accelerometer-type meter, so the "ymax/ymin" are probably integrated displacements, not true quasi-static deflection).
- No data of deflection in a non-loaded adjacent span while the load is in another span (negative influence ordinates) is reported.

### 5. Theory/FE vs measured (Bảng 34 etc.)
Main bridge (deflection, mm; measured/FE): N12 3.19-3.28 vs 3.58 (0.88-0.92); N13 6.01-6.04 vs 6.25 (0.96-0.97); N14 3.54-3.68 vs 3.82 (0.93-0.96). Measured smaller by 3.4-11.9 %. Approach spans measured 25-49 % below calc (slabs N2, Super-T N4, N24; Bảng 28-30). Stress also measured < calc. FE model details (software, stiffness assumptions) not in the report.

### 6. Natural frequencies (Bảng 23; CSV)
First/lowest listed values: N12 3.03, N13 2.88, N14 2.96 Hz (box), N2 5.18, N4 3.41, N11 3.22, N24 3.32 Hz; second row 4.58/4.39/4.84 (box), 7.87/5.54/5.82/5.89. Row labelling ("dọc cầu / thẳng đứng / ngang") looks shifted in the extraction: verify which is vertical. Dynamic factors 1+IM: 1.106-1.123 box, 1.217-1.325 approaches. Pier/abutment frequencies in Phụ lục (T11-T14 about 3.0-4.5 Hz).

### 7. Assessment for the paper

| Goal | Possible with this data? |
|---|---|
| (a) deflection-integral invariance (integral of y dx = P*C_m) | **No** for the integral. Only parked-truck mid-span readings (static) and a dynamic summary. The only crossing record is the 30-40 km/h dynamic run, whose raw waveform is in image form and measured with an accelerometer-type SDA-830C (no true quasi-static deflection). Would require digitising plots or asking HUCE for raw SDA files. |
| (b) SLM with two trucks/convoys | **Weak/indirect.** Same 10-truck fleet in groups of 4, 6, 4 trucks gives different totals on different spans. Per-truck deflection (N12 0.80, N13 1.00, N14 0.91 mm per truck, centre, using 4/6/4 trucks, rough, ignoring true positions) is a ratio-style consistency check at best, but different spans have different C_m and truck positions are only in figures. Needs plates per scheme + stationing. |
| (c) sign change / negative lobe on adjacent spans | **No.** Only the loaded span was reported; no reading in the unloaded adjacent span. Would need raw dial readings for all simultaneously placed gauges (the report does not say whether N12/N13/N14 gauges were all installed while one span was loaded; if yes, the neighbours' readings would show the negative lobe, and the raw logbook might hold it) [NEED VALUE]. |
| (d) C_m via uniform-load equivalence | **Partially possible, at the level of a single mid-span value:** with total parked weight and positions known, y_mid = sum P_i * IL(x_i) is a direct static equation that can be compared with BPM (C_m from EI/spans) only if the design EI(x) of the variable-depth box (design note, Tập 2-2 drawings) is available. FE value already given (3.58/6.25/3.82 mm) is a design-model benchmark. |

**Overall usefulness: Low-to-Medium.** Positives: a real full-scale 42+63+42 m continuous PC box girder (the right structure class), known truck weights/axle spacings, repeated eccentric/centred results (very consistent: centre line variation < 0.1 mm), FE benchmark, 2023 date, HUCE-authored (data ownership with the author's own institution). Negatives: static-only, one value per case, no moving crawl crossing, no influence-line series, no raw time history in the folder, no EI/section table in the report, positions only as images. Cannot validate the integral theorem or the blind-ratio prediction directly.

**Extra processing/requests that would raise it to Medium-High:** (1) Ask HUCE lab for raw SDA-830C files and any strain/deflection logs (sampling rate, full crossing time histories of the 30-40 km/h run in N12-N14); (2) extract the loading figures (Hình 8-12) and sensor figures from the 02 Phụ lục ảnh docx / PDF to get truck stations; (3) read "T.Minh Thai Binh" and the drawings for section area, I(x) and compute C_m by beam theory; (4) Check whether adjacent-span gauges were read in each scheme (negative lobe); (5) if possible request a new slow-crawl pass of a single truck over the box (a cheap field retest).

## Files produced
- thai_binh_main_bridge_static_deflection.csv (Bảng 11, 12, 34)
- test_trucks.csv (truck gross weights)
- dynamic_summary_single_truck_30_40kmh.csv (Bảng 23)
