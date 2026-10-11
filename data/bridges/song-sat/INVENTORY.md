# Song Sat bridge (Hai Duong) - Drive inventory for deflection-integral validation

Folder "2022 - 11 - TT cầu qua sông Sặt - Hải Dương" (id 1T0cKDsNUmJL26r7Sse35UL_jlinXUhiM). Inventoried 2026-10-11. Pagination exhausted for all folders.
Read in full: report docx (01), proposal docx (000-01), dynamic appendix docx, both small xlsx (stress/deflection workbook, dynamic). NOT read: scanned PDF, photo appendix, 02.HSTK .doc (10 MB) and .rar (117 MB), .dwg/.mcb/.OUT/.CA1 binaries, ultrasonic/rebound xlsx (concrete NDT, irrelevant).

## 1. File tree (size bytes; Drive id)
- 01. Đề cương kiểm định (1H8gvXqEZYOwoUFtN2Wegy11TmmUN-hSG)
  - 000 - 01 - Đề cương cầu qua sông Sặt.docx (1,111,997; 14VtktlTBIUwTAkCGU9IcmXL-F6J5W1rE) [read]
  - 00 - Cau qua song Sat.dwg (1,159,585; 1BySRX3aG9zcQ5r85PCknWHkL_d8TKeN9)
  - BTC cau vuot song Sat_28-09-2021.dwg (1,032,426; 1QPAVyizrUI14r67aJd68mFV_35NXmMNu)
- 02. HSTK (1jUErsuIWa3BT2UltAbO5npH2Heep8BwU)
  - Thuyet minh chung DT394B_28-08-2021_A4 (sau KCS).doc (10,364,416; 163lckeIadUO_h4lREYShWvGVoH1hfzPe) [design memo, unread; may hold EI/section/bearing details]
  - Ho so BVTC (sau TD).rar (117,318,398; 1SvvsvJB4h2wsFLxg-43SNKPUcgf8qYgp) [shop drawings, unread]
- 07. Báo cáo kiểm định (1qk88S8v_qTJe1Slwv4iDXjvchC_QxNVx)
  - 01. Báo cáo KĐ cầu Sông Sặt.docx (1,368,780; 1PUvyx34cZI4SBf7268wEXlx5RKlT_TsB) [main report, read]
  - 01. Báo cáo KĐ cầu Sông Sặt_Scan.pdf (19,892,762; 1_btp9ECLq2kW485iTtmoVm44fAVUTRtU) [signed scan of same]
  - 03. Báo cáo KĐ cầu Sông Sặt - 03. Phụ lục ảnh.docx (7,691,387; 1t73jm7o5j1cZQzKS1MFfUEynANlJ5Zn-) [photos]
  - 04. Phụ lục đo động.docx (578,521; 14l-BvLEzabx5wJ-KwS-x1phdoYPOaczc) [only f/T tables; time-history plots are images]
  - 04. Đo động.xlsx (16,401; 1UzQxYyaoSP2TviCFrEaUFBs25BKN5oAU) [read]
  - Kết quả đo ứng suất, võng_cầu Sông Sặt_Thay Bao gui lai.xlsx (180,692; 1tBVDpSpfDRS4egD0cLYjW27ezxPa-_u7) [key data, read]
  - CauSongSat/ (1ic-3uA2oZyKTS4VcZuuZK7aHszSCE2Tx): MotDN_Plate.OUT (57,681; 1nKnFCSP983wm0LzbtVY_ypOTj8yZs8ft), MotDN_Plate.CA1 (4,790,400; 1drvhQa3TwP6hPRZ4pX6Mr9v32uj2DAoe), MotDN_Plate.mcb (585,948; 1F6aft_moIufnheZgsubk3VW_6g_cj3hk), MotDN_Plate.bak (585,948; 1WFpW9Rcz1pziPakjawPU_wKwVgkGRjax), MotDN.mcb (1,795,672; 1Aq7ItOzdSsFLJM1AWdJlh18ewhRorFIN), CauMay-SuperT-N1.mcb (4,537,816; 1IOmC3ZrQnFgPRVhLZI3DRqcWNNXAKsqi), MCN.dwg (53,060; 1bfZVfC19OfxmlfT-joytvYfrat6vGihr) [Midas Civil models of one span unit; the FE source of "theory" values]
  - Thí nghiệm/ (1GINydtl-DGTIcpprqPX4ue0B16dN2Uo3): 9 xlsx concrete NDT workbooks (ultrasonic "siêu am" x4 for dầm 1, dầm_2, mố-trụ x2; rebound "bật nảy" x3; cover-depth "Chieu day BTBV" x3: Dầm_1 85,893; Dầm_2 85,908; Mố trụ 63,832). Ids: 1KO88hci_9U5a7sAN9S434Rv6Ff_IwK-X, 1yJt9ZK6xbMPbq8mEPkNL0YW1etbxINQT, 1fVLs2G1ngsmedCgs6P6I4FB6PIfkEoeA, 1wgmAQiD96hLMcrFjjFLZ19KckkdJ0xea, 1Kim0xiH4vZdCLzg9XnIrsPgp_zt8Yjfo, 15xwWpdel219LV1dnxn8_AgWpI-FQRS11, 19VrZRKU388xKxVxd2h5zogW6fwpx7Usv, 1g5WYbjbf1z2n11PtMK0ddxVS-mlmC4iA, 1dJhkxFa6OXw54u6wYTz1bgPSs_x7Tpgo. Concrete-quality data only; not relevant.

## 2. Findings

### 2.1 Bridge and structural system
- Source: report sec 2.2.3 and 5.3.2; proposal sec II.
- Three-span (39.15 + 40 + 39.15 m) prestressed-concrete Super-T bridge, total length 128.45 m, two separate carriageway units (each 11.87 m wide), 5 Super-T girders per unit (38.3 m long, H = 1.75 m, spacing 2.35 m), 180-200 mm cast-in-situ deck, 2 end cross-girders (0.8 x 0.9 m) per span, pot bearings, U abutments and solid piers on D1.2 m bored piles. Design load HL-93.
- Structural system: the girders are simply supported per span; the deck slab is described as "nối liên tục nhiệt" (thermally continuous, i.e. continuity of the slab only at piers, not structural flexural continuity). So the system is **simply supported spans with a continuous deck**, NOT a continuous beam. The text never says "continuous girder"; confirm in the Midas model (MotDN.mcb) and 02.HSTK memo. EI, I, A: [NEED VALUE] (E_c from report = 38,007 MPa; Midas sheet uses E_bmc 2.81e4 / E_dam 3.78e4 [unit unclear]).
- Test year: proposal 2022; field work 15 Aug 2024 (strain log timestamps); report 2024.

### 2.2 Test vehicles
- 6 trucks weighed (gross 27.56, 27.86, 28.04, 28.01, 27.69, 28.11 t; mean 27.88 t), 4 axles, spacings 1.80 / 3.20 / 1.35 m, track 1.85 m (report sec 7.1, Fig 11). The proposal specified 12 trucks (3 longitudinal x 2 x 2 units); weights of the other 6 and per-axle loads [NEED VALUE] (sheet hints split 15/15/35/35 percent).
- Truck axle positions along the loaded span (m from support, "Xe tải" block of the xlsx): truck 1 axles at 1.8, 3.6, 6.8, 8.15; truck 2 at 14.15, 15.95, 19.15, 20.5; truck 3 at 26.5, 28.3, 31.5, 32.85 (the second column is the mirror, 38.3 - x). Only the one final loading is documented.
- Dynamic runs: one truck at 30-40 km/h (proposal sec V.3.4).

### 2.3 Measurement
- Static deflection: dial gauge/"võng kế" (indicators), 1 point per girder at mid-span of span N1 only, 10 points (5 per unit). Readings are dial counts (0.01 mm) before loading (Ko), under load (DT) and after unloading, with support settlement also recorded. Static girder soffit levelling (level NA2) before loading, 3 points per girder.
- Strain: 30 gauges (3 per girder, mid-span N1), longitudinal; also a logged TDS data set (36 readings, timestamps 11:13-12:25, 15 Aug 2024) - discrete states, not a time history of a crossing.
- Dynamics: SDA-830C vibration meter, 3 directions at mid-span of N1, N2, N3 of both units, and on abutments/piers.

### 2.4 Load cases and data type
- Static: only 2 final positions per unit (concentric, eccentric), each with 3 repeats + trial; truck positions NOT varied. No influence-line style series, no crawl-speed crossing.
- Dynamic: moving truck 30-40 km/h, mid-span records for all 3 spans but only as images in the appendix; report extracts only f, T, y_max, y_min, 1+IM. Sampling rate [NEED VALUE]. Raw files not in the Drive folder.
- Midas "theory" is for the same static layout only.

### 2.5 Theory vs measurement
- Mid-span N1 deflections: measured 3.5-8.5 mm vs Midas 6.9-16.6 mm; measured/theory about 0.43-0.67 (report 8.1 sums per cross-section: 50-65%, e.g. "Tổng võng" 31.10 vs 19.13 etc.). Model overpredicts ~2x (E increased only about 15% in the model). Stresses measured 11-77% below theory. Transverse distribution factors agree well (0.22-0.52). Data: static_deflection_midspan_N1.csv.

### 2.6 Natural frequencies
- Vertical 3.09-3.58 Hz (T 0.28-0.32 s); longitudinal 4.2-4.73 Hz; transverse 7.5-8.1 Hz; 1+IM 1.21-1.24 (all spans, both units). Abutments/piers also given. Data: natural_frequencies.csv.

### 2.7 Assessment for the paper
- (a) Deflection integral invariance: Low. No moving crossing record and no static truck positions at multiple stations, so the integral over a crossing cannot be computed. The dynamic mid-span records (all 3 spans, 30-40 km/h, one truck) would be exactly suitable IF raw displacement/acceleration files existed, but deflection there is a dynamic record from SDA-830C (likely acceleration-integrated, uncertain) and only plots are present.
- (b) SLM with two trucks/convoys: Low. Two load cases (concentric/eccentric, 12 trucks, 27.9 t each) give a static ratio but not a crossing ratio; a ratio of static mid-span deflection is only a weak proxy.
- (c) Sign change on adjacent spans of a continuous beam: None. Spans are simply supported (deck continuity only); no loading of N2/N3 with deflection measured in N1. The mid-span records of N1/N2/N3 under a truck in a neighbouring span might show it, but not available as numbers.
- (d) C_m via uniform-load equivalence: Low to Medium for a static check. Midas model (MotDN.mcb) and mid-span deflection at 12 known trucks allow comparing measured with computed static deflection, but the model is 2x stiffer-looking than reality and the truck weight/axle layout is only partly documented.
- Overall rating: **Low** for the continuous-beam claims; Low-Medium as a 38 m simply supported PC girder field example with known truck weights.
- Extra work required: ask the consultant (Cty TNHH Tư vấn ĐHXD / Nguyen Quoc Bao, Nguyen Hung Son) for raw SDA-830C dynamic files and crawl-speed passes if any; extract EI, section from the Midas model and 02.HSTK memo; obtain remaining 6 truck weights and axle loads.
