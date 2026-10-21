# Hostile audit v3, part 2: citations and reference list

## Scope and method

Files audited (read-only): `manuscript/ase/manuscript.md` (body, figure captions, reference list), `manuscript/ase/supplementary_material.md`, `manuscript/ase/cover_letter_ASE.md`, and the built `manuscript/ase/word/Manuscript_ASE.pdf` (md and PDF both dated 21 Oct 2026 12:05). No file other than this report was edited. Working files are in the session scratchpad.

Method:
1. Two-way match by script. In-text citations were extracted by regular expression from the body and captions (44 "et al." citations plus all others), the Supplementary Material and the cover letter, and matched to the 57 list entries on first-author surname and year (with a/b suffix). Every list entry was then searched in the text. Parenthesis ordering was checked by eye on every multi-citation parenthesis.
2. Crossref. All 50 DOIs were fetched from `api.crossref.org/works/<url-encoded DOI>` (49 DOIs) or `api.datacite.org/dois/<DOI>` (the figshare dataset), 1 s apart. All 50 returned HTTP 200. Fields compared: author surnames, order and initials, title, container title, year (print vs online), volume, issue, pages or article number, DOI. For the 7 entries without a DOI, a Crossref `query.bibliographic` search was run and the Virginia Tech handle was fetched.
3. Usage. Crossref abstracts (19 entries) and OpenAlex abstracts (a further 6) were read against the sentence that cites each work. 18 entries have no abstract in either source (listed under check 3); these were judged by title only.
4. PDF. The PDF reference list (pdftotext) was compared with the md list after stripping markup, whitespace and hyphens; italics were checked with `pdftohtml -xml`. Every in-text citation string of the md body was also searched in the PDF text.
5. Style against Sage Harvard (Advances in Structural Engineering).

### Per-check summary

| Check | Result |
|---|---|
| 1a. Every in-text citation (body, captions, Supplementary, cover letter) has a list entry with the same year and spelling | Pass. No orphan citations. |
| 1b. Every list entry cited at least once (manuscript or Supplementary) | Pass. 57 of 57 cited. The Supplementary Material cites 6 entries (Deng 2025, Yan 2022, Moghadam 2023a, Frýba 1999, Sohn 2007, Cross 2013), all in the main body too. |
| 1c. a/b suffixes | Pass. Only Moghadam et al. 2023a and 2023b share author-year; both suffixed in text and list. Moghadam et al. (2022) needs no suffix (different year). The Supplementary uses "2023a" correctly. |
| 1d. Order inside parentheses (by year) | Pass. All 14 multi-citation parentheses checked, e.g. (Law et al., 1997; Chan et al., 1999; Law and Zhu, 2000), (Yang et al., 2021; Zhu et al., 2022; Agüero-Barrantes et al., 2023), (Sohn, 2007; Cross et al., 2013), (CEN, 2003; AASHTO, 2024), (Moghadam et al., 2022, 2023a, 2023b). |
| 1e. Cover letter | Pass. No paper is cited. The only reference-like item is the dataset DOI link in the data-availability paragraph, which is not an author-year citation. |
| 2. Crossref | 50 of 50 DOIs resolve; no wrong DOI, no wrong author order, no wrong volume, no wrong year convention. Two entries (Dang 2023, Vu 2023) match Crossref fully. Findings are minor (below). |
| 3. Usage | No clear mismatch or over-claim. A few sentences are slightly looser than the abstract or cannot be verified (minor). |
| 4. Style | Two should-fix items (initials of hyphenated given names; italics of stand-alone titles), several minor. |
| 5. Reference count | 57 entries: 50 with DOI (49 Crossref, 1 DataCite) and 7 without (AASHTO, Al-Qadi, CEN, Frýba, Jacob, Moghadam thesis, Ojio). |
| PDF | The reference list renders identical to the md after normalisation (only difference: the page number "29" glued to the last line by text extraction). All in-text citation strings of the md are found in the PDF. Journal and book titles are italic in the PDF. |

Blocking findings: none. Should fix: 2. Minor: 9.

## Findings

### Should fix

**S1. Initials of hyphenated given names are inconsistent (Zhu 2022, Yamaguchi 2009).**
- Entries: "Zhu J, Wang C, Qi T and Zhou Z (2022)" and "Yamaguchi E, Kawamura S, Matuso K, Matsuki Y and Naito Y (2009)".
- Crossref: Zhu **Jun-He**, Wang Chao, Qi **Tian-Yu**, Zhou **Zhuo-Sheng**; Yamaguchi Eiki, Kawamura **Shin-Ichi**, Matuso Kazushi, Matsuki Yuta, Naito Yasushi.
- The list elsewhere gives two initials for hyphenated names (Zhang WS, Yan WJ, Lin SW, Du YL, Yi TH, Yang DH, Zuo XH, He WY, Ren WX, Di SK, Jia ZJ, Hao TT, Yuen KV). The four names above break that rule.
- Minimal fix: "Zhu JH, Wang C, Qi TY and Zhou ZS (2022)"; "Kawamura SI" in Yamaguchi (2009). The in-text citations (et al.) do not change. The accepted "Matuso K" spelling stays.

**S2. Titles of stand-alone works are italic in some entries and plain in others.**
- Italic: AASHTO, Frýba, Ghali, Jacob, Pukelsheim.
- Plain: Al-Qadi (report FHWA-HRT-16-024), CEN (EN 1991-2:2003), Moghadam (2022) (PhD dissertation), Moghadam and Sarlo (2024) (dataset).
- Sage Harvard italicises the title of a report, thesis, standard and dataset the same way as a book.
- Minimal fix: italicise the title in these four entries, e.g. `*LTBP Program's Literature Review on Weigh-in-Motion Systems*`, `*EN 1991-2:2003, Eurocode 1: Actions on Structures – Part 2: Traffic Loads on Bridges*`, `*Integration of Traffic and Structural Health Monitoring Systems Using a Novel Nothing-On-Road (NOR) Bridge-Weigh-In-Motion (BWIM) System*`, `*Nothing-on-Road Bridge-Weigh-In-Motion (NOR-BWIM) Dataset*`. Optionally "PhD Thesis" instead of "PhD dissertation" (Sage wording). The Virginia Tech handle gives the title with "Using A Novel"; "Using a Novel" in the list is fine.

### Minor

**M1. Dang NTV, Ho DD and Ha MT (2023) (special attention). Matches Crossref.**
- Crossref (10.31814/stce.huce2023-17(3V)-04): authors in the order Đặng Ngọc Thúy **Vy**, Hồ Đức **Duy**, Hà Minh **Tuấn** (Crossref stores the personal name in the family field and the family name in the given field; order is identical to the list). Vietnamese convention gives Dang NTV, Ho DD, Ha MT, which is what the list has. Volume 17, issue 3V, pages 47–65, online 24 Aug 2023, no print date: all match. DOI matches (Crossref lower-cases "3v", which resolves the same).
- Title: Crossref has only the Vietnamese title ("Chẩn đoán sự suy giảm độ cứng trong kết cấu dầm thông qua dữ liệu đường ảnh hưởng của chuyển vị"). The bracketed English title uses "using" for "thông qua" (literally "through"). Acceptable. If the paper's own page prints an English title, use it verbatim; Crossref cannot confirm either.
- "(in Vietnamese)" and square brackets present, journal italic, "17(3V): 47–65" correct. No fix required.
- Usage: the Crossref abstract (Vietnamese) describes an FE study of a 2.2 m beam that diagnoses presence, location and degree of stiffness loss from displacement influence lines via RMSD and MAPD indices. The manuscript says influence lines "have been ... inverted ... for the presence and location of stiffness loss in a beam (Dang et al., 2023)". Correct in substance; "inverted" is slightly loose (it is a damage-index comparison on simulated data, with severity as well). Optional wording: "used for diagnosing the presence and location of stiffness loss in a beam".

**M2. Vu DC, Luong ND, Cu VH, Vu NQ and Bui NS (2023) (special attention). Matches Crossref.**
- Crossref (10.31814/stce.huce2023-17(4)-02): Chieu Vu Dinh, Dung Luong Ngoc, Hung Cu Viet, Quang Vu Ngoc, Son Bui Ngoc, i.e. Vu DC, Luong ND, Cu VH, Vu NQ, Bui NS, same order. Title identical. Volume 17, issue 4, pages 14–25, online 25 Dec 2023: all match. DOI matches.
- Crossref container: "Journal of Science and Technology in Civil Engineering (STCE) - HUCE"; list: "(HUCE)". Same journal, same short form as the other two HUCE entries; no fix needed. (Optional unification to "(STCE) – HUCE" for all three would follow Crossref.)
- Usage: the abstract is a TLS deflection measurement on a balanced-cantilever bridge in Hanoi, compared with dial indicators and a total station, concluding "acceptable accuracy". The manuscript cites it only as an example of terrestrial laser scanning of bridge deflection, which is correct.
- This is an English-language paper, so no "(in Vietnamese)" and no bracketed title are required, and none is given. Correct.

**M3. OBrien EJ, Rowley CW, González A and Green MF (2009).** Crossref gives `page: 310` and article number 27135 (OpenAlex: first and last page both 310). The list's end page 327 cannot be confirmed from Crossref or OpenAlex. Fix: confirm "310–327" on the Inderscience page; if not confirmed, give "16(3): 310" or the article number.

**M4. Print versus online years are consistent with the stated convention; recorded for the audit trail.** The list uses the print issue year in every case where it differs from the online year: Lin 2023 (online 2022-09), Wang 2026 (online 2025-07), Shi 2025 (online 2024-07), Sohn 2007 (online 2006-12), Yu 2018 (online 2017-11), Žnidarič 2018 (online 2017-12), Yamaguchi 2009 (online 2016), Agüero-Barrantes 2023 (OpenAlex shows 2022; Crossref print Feb 2023). Zhou 2026 (SCHM vol. 2026, issue 1, article 1361157; Crossref issued 2026-01, online Oct 2026) is consistent. Métodos y Materiales: Crossref issued dates are 2025-09 (digital deposit) for Lobo Aguilar 2018 and Agüero-Barrantes 2021, but volume 8 and volume 11 correspond to 2018 and 2021; the list years are right. No change.

**M5. Métodos y Materiales entries.** Crossref gives issue 8 for vol. 8 and issue 11 for vol. 11; the list omits the issue ("8: 11–22", "11: 43–53"). Acceptable if the journal is numbered by volume only; otherwise "8(8)" and "11(11)". Crossref's title field for Lobo Aguilar 2018 is corrupted ("A SimplifiePesaje ... serviciod Shear-Strain Based ..."); the list gives the correct English title "A simplified shear-strain based bridge weigh-in-motion method for in-service highway bridges", matching the English abstract. Known and accepted: "Lobo Aguilar" (2018) against "Lobo-Aguilar" in the ASCE record follows each original. Note that the 2021 Crossref record spells "Agüero Barrantes" without a hyphen, while the list (and the ASCE 2023 record) use "Agüero-Barrantes"; the list is consistent with itself.

**M6. Container-title wording differs slightly from Crossref in five records (accepted short forms).** "The Annals of Mathematical Statistics" (list omits "The", Elfving and Sherman); "Philosophical Transactions of the Royal Society A" (Crossref adds ": Mathematical, Physical and Engineering Sciences"); "Transportation Research Record" (Crossref adds ": Journal of the Transportation Research Board"); "Proceedings of the Institution of Civil Engineers: Bridge Engineering" (Crossref has a hyphen)). All are standard abbreviations; no fix unless the journal's copy-editor asks.

**M7. Surname rendering from Crossref.** The list writes "OBrien" (also in text) as Crossref does; the author's own spelling is O'Brien. Likewise "González" (Crossref "Gonzalez"). The list follows the more correct accented form for González. Optional: "O'Brien" in list and text, consistently.

**M8. Terminal period after DOI and after URLs.** Every entry ends with a full stop after "DOI: ..." and after the URLs. Sage's examples print the DOI without a final stop. It is consistent throughout, so low risk; check against the journal's template at proof stage.

**M9. Usage: sentences slightly looser than, or not verifiable against, the abstract.** No clear mismatch. Entries with no abstract in Crossref or OpenAlex (title only checked; Cardini 2009 has an OpenAlex abstract, consistent with its citation): Helmi 2014, Chaudhary 2025, Wu 2020, Zhang 2026, Zhou 2025, Wu 2018, Yan 2022, Fan 2015, Moghadam 2022, 2023b, Cross 2013, Moses 1979, Zhu and Law 2006, Katafygiotis and Beck 1998, Chan 1999, Law 1997, Law and Zhu 2000, Udwadia 1994, Papadimitriou 2004. Specific points:
- Helmi et al. (2014): "accurate to within 5 % on a seven-span slab-on-girder bridge for test trucks with well-estimated speeds". No abstract available; the figure and bridge type cannot be verified here. Check against the paper.
- Nguyen et al. (2024): "used the integral of mid-span deflection on a simply supported beam". The abstract (Vietnamese) says the load is determined by BPM and SLM from measured deflection on a simply supported beam, with FE and an experimental model; "integral" and "mid-span" are not in the abstract. Consistent with BPM/SLM as the manuscript defines them, but not confirmed. Check against the paper.
- Hong et al. (2016) and Wu et al. (2018): "Strain-history areas along continuous girders have served damage identification". Hong's abstract (strain time-history area ratio, simulation, lab test, field test of a real bridge) does not say continuous girders; Wu 2018 does (title). Optional: "Strain-history areas have served damage identification (Hong et al., 2016), including on continuous girders (Wu et al., 2018)".
- Moghadam et al. (2022, 2023a, 2023b): "deck strain on long-span box girders". The 2023a abstract gives a 144 m span concrete box girder; the other two are not confirmed as long-span (titles say concrete-box-girder bridges). Minor.
- Confirmed correct from abstracts: Hao 2019 (axle weights, model tests, simply supported and continuous beams), Zuo 2019 (load transverse distribution, multi-T-girders), Deng 2025 (absolute area of displacement influence line, continuous rigid-frame), Yang 2021 (strain integral coefficient), Zhu 2022 (strain response area), Agüero-Barrantes 2023 (area under the strain curve, Kriging), Shi 2025 (load-cell reactions, with a reaction-force and an area method), Lin 2023 (boundary spring stiffness of a suspension-bridge girder from influence lines), Wang 2026 (VMD deflection influence line), Zhou 2026 (stiffness inversion from deflection influence lines), Yamaguchi 2009 (two-span continuous bridge), OBrien 2006 (measured influence lines), OBrien 2009 (Tikhonov regularisation), Žnidarič 2018 (accuracy improvements), Yu 2018 (transverse position), Sohn 2007 (environmental and operational variability), Ventura 2024 (overloading frequency), Moghadam 2023a (mean absolute GVW error 4.6 %, cited in the Supplementary as 4.6 %).

### Items checked and found correct (no action)

- All 49 Crossref records: author surnames, order and initials (apart from S1), title wording (sentence case in the list against title case in Crossref, which is the Sage convention), volume, issue, pages or article number, DOI.
- DataCite record 10.7294/26880898.v1: creators Moghadam, Amin and Sarlo, Rodrigo; title "Nothing-on-Road Bridge-Weigh-In-Motion (NOR-BWIM) Dataset"; year 2024; publisher University Libraries, Virginia Tech. Matches the list.
- No-DOI entries: Moghadam (2022) thesis confirmed at http://hdl.handle.net/10919/111390 (Moghadam, Amin; Virginia Tech; 2022-07-27). Frýba (1999) 3rd ed., Thomas Telford is correct (Crossref only carries the 1972 Springer first edition 10.1007/978-94-011-9685-7). Ojio and Yamada (2002), Jacob et al. (2002), AASHTO (2024) and CEN (2003): no matching Crossref record (the Crossref hit for Ojio and Yamada is a different paper in the 2009 Wiley HVParis volume), so they cannot be checked this way. The Al-Qadi report URL returned "Access Denied" to the sandbox client and was not verified.
- Alphabetical order of the list (single author, then two authors, then multiple authors for the same first author; Moghadam entries 2022 thesis, 2024 with Sarlo, then the three-author papers) is correct; "Žnidarič" sits between Zhu and Zuo.
- "et al." in text is used for every work with three or more authors and "and" for two (Law and Zhu; Zhu and Law; Ojio and Yamada; Sherman and Morrison; Katafygiotis and Beck; Moghadam and Sarlo); each "et al." is followed by a year.
- Page ranges use en dashes throughout; "and" precedes the last author in every entry; "(in Vietnamese)" and the bracketed translated title are present on both Vietnamese-language papers (Dang 2023, Nguyen 2024), and are not used on the English-language Vu 2023.
- Journal and book titles are italic in md and PDF.

## Reference count

**57 references** (50 with DOI, 7 without).
