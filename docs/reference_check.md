# Reference check (WP1)

Checked: 2026-10-11. Source list: the 40-entry list of `manuscript/text/JCSHM_Submission_docx_v_drive.txt` (full list). `manuscript/text/CSHM-D-26-00881.txt` is truncated after ref 31 in its text export, but the entries it has match.

Method: every DOI was resolved through the Crossref API (`https://api.crossref.org/works/<doi>`), 31 of 31 returned a record, and authors, title, year, journal, volume, pages were compared. The 9 entries without DOI (9, 10, 11, 32, 34, 35, 36, 39, 40) were checked by search where possible.

## Qiu 2025

- It is **not in the current reference list**. Entry [10] "Qiu, X., Y. Lu, and Y. Chen, Weigh-in-Motion Systems: Calibration, Accuracy and Practical Deployment Challenges. Sensors, 2025. 25(8): p. 2421." occurs only in `01_Research_Paper-03_JMES_version.txt` (line 477) and in `BaoCao_PhanBien.txt` (line 346). Sensors 25(8):2421 resolves in Crossref to **Gajda, Sroka, Burnos, Daniol, "Long-Term Assessment of the Properties of Load Sensors Applied in Weigh-in-Motion Systems"** (10.3390/s25082421). The Qiu entry used Gajda's article number under a different author list and title: **suspected fabricated**, correctly removed. No occurrence of "Qiu" in any of the ES, JCSHM or CSHM texts.
- Current [8] is the correct Gajda entry. Do not re-add Qiu.

## Table

Status key: OK, mismatch (record exists but data differ), not found, suspected fabricated.

| Ref | Status | Notes / corrected entry |
|---|---|---|
| 1 | OK | Fan Y, Zhu J, Pei J, Li Z (2015) Eng Fail Anal 56:20–27. Manuscript says "Fan Y, et al"; fine. |
| 2 | OK | Salem HM, Helmy HM (2014) Eng Struct 59:635–645. Pages given as "635–45": fine. |
| 3 | OK | Invernizzi S, Montagnoli F, Carpinteri A (2022) J Bridge Eng 27(1):04021102. |
| 4 | OK | Morgese M, Ansari F, Domaneschi M, Cimellaro GP (2020) J Civ Struct Health Monit 10:69–85. Crossref online date is 2019; volume 10 is 2020, fine. |
| 5 | OK | Ventura R, Barabino B, Maternini G (2024) J Traffic Transp Eng (Engl Ed) 11(4):776–796. |
| 6 | OK | Li H, Wang T, Wu G (2023) Mech Syst Signal Process 186:109866. |
| 7 | OK (title wording) | Fattorini F, Salvatore W, Renzi E, Tamasi G (2023) Procedia Struct Integr 44:689–696. Crossref title has quotation marks around "Guidelines for the classification and management of risk, ..." Check the full title wording before final. |
| 8 | OK | Gajda J, Sroka R, Burnos P, Daniol M (2025) Sensors 25(8):2421. |
| 9 | **mismatch** | "FHWA (2016) Long-term bridge performance program: weigh-in-motion system accuracy and precision." No report with this title found. The FHWA LTBP report of June 2016 is **Al-Qadi I, Wang H, Ouyang Y, Grimmelsman K, Purdy JE (2016) LTBP Program's Literature Review on Weigh-in-Motion Systems. FHWA-HRT-16-024. Washington DC: FHWA** (https://rosap.ntl.bts.gov/view/dot/35735; fhwa.dot.gov/publications/research/infrastructure/structures/ltbp/16024). Replace and say what the manuscript cites it for (accuracy classes?). |
| 10 | **mismatch / not found** | "FHWA (2009) Comprehensive truck size and weight study: costs of weigh stations." The study I could find is **U.S. DOT, FHWA (2000) Comprehensive Truck Size and Weight Study, Vol. II: Issues and Background, FHWA-PL-00-029** (https://rosap.ntl.bts.gov/view/dot/4747); enforcement costs are in its chapter 7. A 2009 date and the sub-title "costs of weigh stations" were not found. A later FHWA desk scan for the MAP-21 study (undated copy at ops.fhwa.dot.gov) compares fixed scale and WIM costs. Authors must say which document and which figure they cite; correct the year (2000 or the desk-scan year) and the title. |
| 11 | OK (not verifiable online) | Jacob B, OBrien EJ, Jehaes S, eds (2002) Weigh-in-Motion of Road Vehicles: Final Report of the COST 323 Action. Paris: LCPC. No DOI. Several papers cite this as "Jacob et al. 2002". I did not retrieve a catalogue record; mark as "check library record". |
| 12 | OK | Moses F (1979) Weigh-in-motion system using instrumented bridges. Transp Eng J ASCE 105(3):233–249. |
| 13 | OK | OBrien EJ, Quilligan MJ, Karoumi R (2006) Calculating an influence line from direct measurements. Proc ICE Bridge Eng 159(1):31–34. Manuscript page range "31–4" is a truncation of 31–34. |
| 14 | OK | OBrien EJ, Rowley CW, González A, Green MF (2009) Int J Heavy Veh Syst 16(3):310–327. |
| 15 | OK (year) | Žnidarič A, Kalin J, Kreslin M (2018) Struct Infrastruct Eng 14(4):412–424. Crossref online year 2017; volume/issue is 2018. Fine. |
| 16 | OK | Yu Y, Cai CS, Deng L (2016) Adv Struct Eng 19(9):1514–1530. |
| 17 | OK | Ojio T, Carey C, OBrien EJ, Doherty C, Taylor SE (2016) J Bridge Eng 21(7):04016032. My check printed only the first four authors; Taylor SE (fifth) was not confirmed by me. |
| 18 | OK | Law SS, Chan THT, Zeng QH (1997) J Sound Vib 201(1):1–22. |
| 19 | OK | Chan THT, Law SS, Yung TH, Yuan XR (1999) J Sound Vib 219(3):503–524. |
| 20 | OK | Law SS, Zhu XQ (2000) J Sound Vib 234(4):661–679. |
| 21 | OK | Zhu XQ, Law SS (2006) Mech Syst Signal Process 20(7):1759–1782. |
| 22 | OK | Hoang T, Duhamel D, Foret G, Yin H (2017) J Sound Vib 388:327–338. |
| 23 | OK | Deng L, Cai CS (2010) J Vib Control 16(14):2167–2194. |
| 24 | OK | Chen Z, Fang Y, Kong X, Deng L (2023) J Sound Vib 563:117866. |
| 25 | OK | Katori H (2018) World J Mech 8(5):192–199. |
| 26 | OK | Luo S, Jiang J, Zhang F, Mohamed MS (2023) Appl Sci 13(4):2537. |
| 27 | OK | Jiang J, Luo S, Mohamed MS, Liang Z (2020) Appl Sci 10(19):6767. Manuscript has "Jiang J, et al"; fine. |
| 28 | OK | Kapoor T, Wang H, Núñez A, Dollevoet R (2024) J Phys Conf Ser 2647:152003. |
| 29 | OK | Yang YB, Lin CW, Yau JD (2004) J Sound Vib 272(3–5):471–493. |
| 30 | OK | Feng D, Feng MQ (2018) Eng Struct 156:105–117. |
| 31 | OK | Nguyen DH, Nguyen QB, Bui-Tien T, De Roeck G, and possibly further authors (my check printed only the first four) (2020) Theor Appl Fract Mech 109:102728. Manuscript says "Nguyen DH, et al"; fine. |
| 32 | OK | Andersen P, Mukhopadhyay SK (1950) Determination of load distribution on a beam from measurements on its deflected form. University of Minnesota Bulletin, vol. 53 no. 1, 4 January 1950 (Minneapolis). Record at https://hdl.handle.net/11299/124278. Add the bulletin number. |
| 33 | mismatch (language) | Authors Nguyễn Quốc Bảo, Hoàng Tiến, Nguyễn Hùng Sơn; J Sci Technol Civ Eng (HUCE) 18(2V):61–71, 2024; DOI correct. **The Crossref title is Vietnamese: "Xác định tải trọng tác dụng lên kết cấu dầm giản đơn dựa trên số liệu đo độ võng".** The manuscript gives an English title; add "(in Vietnamese)" and, if the journal has an English title/abstract, use that exact title. Own work: self-citation should be marked. |
| 34 | OK (manual) | ABAQUS/Standard user's manual v6.9, Dassault Systèmes Simulia, 2009. Not checkable online. Replace "Smith M" by "Dassault Systèmes" if Elsevier style requires corporate author. |
| 35 | OK (not verified online) | Frýba L (1999) Vibration of Solids and Structures under Moving Loads, 3rd ed. Thomas Telford, London. No DOI. |
| 36 | OK (not verified online) | JCGM 100:2008, Evaluation of measurement data: Guide to the expression of uncertainty in measurement. BIPM, Sèvres. |
| 37 | OK | Sohn H (2007) Philos Trans R Soc A 365(1851):539–560. Crossref online date 2006 (Dec). Volume 365 is 2007; fine. |
| 38 | OK | Cross EJ, Koo KY, Brownjohn JMW, Worden K (2013) Mech Syst Signal Process 35(1–2):16–34. |
| 39 | OK (not verified online) | EN 1991-2:2003 Eurocode 1, Part 2: Traffic loads on bridges. CEN, Brussels. |
| 40 | OK (not verified online) | AASHTO LRFD Bridge Design Specifications, 10th ed. (2024). I did not retrieve the catalogue entry; confirm the year/edition. |

## Summary

- 31 DOIs resolved; no wrong DOIs.
- Mismatches: **[9]** (title not found, real FHWA report differs), **[10]** (title/year not found), **[33]** (title language).
- Not verifiable online (fine, but unconfirmed): 11, 34, 35, 36, 39, 40.
- Minor: [7] title quotation marks, [32] bulletin number, [13] page range.
- Qiu 2025: removed already from the JCSHM/ES/CSHM texts; remains only in the JMES draft and in a review report. Suspected fabricated.

## Missing citations the revision should add

Moses & Ghosn follow-ups, Ojio & Yamada 2002 (secondary), Cardini & DeWolf 2009, Chaudhary 2025, Döring 2023, Agüero-Barrantes 2023, Yang 2021, Zhou 2025: see `docs/novelty_matrix.md` (rows and DOIs there come from Crossref).
