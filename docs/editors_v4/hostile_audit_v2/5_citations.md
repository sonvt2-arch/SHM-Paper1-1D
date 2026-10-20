# 5_citations: citation / reference audit

Scope: manuscript.md (body, captions, reference list), supplementary_material.md, cover_letter_ASE.md, built Manuscript_ASE.pdf.
Method: every in-text citation matched to the list and back; all 43 DOIs in the list fetched from Crossref (42 returned 200, plus DataCite for the dataset); metadata compared field by field; usage checked against Crossref/OpenAlex abstracts where available.

## 1. Two-way match (cited vs listed)
- 52 reference entries. Every one is cited at least once in manuscript.md or the Supplementary Material (AASHTO, CEN, Frýba, Sohn, Cross, Katafygiotis and Beck, Udwadia, Papadimitriou and Moghadam 2022 are cited in Sections 2.5, 4.1, 6 and the Supplement).
- Every in-text citation (body, captions, supplement, cover letter) has a list entry. Year and spelling agree, including OBrien, Žnidarič, Agüero-Barrantes, Lobo Aguilar and Frýba. The a/b suffixes for Moghadam et al. 2023a/b are used consistently. "Moghadam (2022)" (thesis) and "Moghadam et al. (2022)" are distinguishable.
- No orphan, missing or mis-dated citation: nothing to report in the blocking class for citation-to-list matching.

## 2. Crossref metadata (authors and order, title, journal, year, volume, issue, pages/article number, DOI)
No mismatches in authors or order, title wording, journal, volume, issue or pages for any of the 42 Crossref-resolved DOIs. Per-entry notes (none is an error):
- Agüero-Barrantes 2021 and Lobo Aguilar 2018 (Métodos y Materiales): Crossref "issued" year is 2025 (deposit date), with issue 11 and issue 8. Volume 11 (2021) and volume 8 (2018) are the true publication years, so the list is right. The list omits the issue number. Crossref's primary title for Lobo Aguilar 2018 is the Spanish "Pesaje simplificado de vehículos en movimiento basado en mediciones de deformaciones unitarias cortantes para puentes en servicio". The list gives the English title (the English abstract is on the same record). Fine.
- Lin 2023, Wang 2026, Yu 2018, Žnidarič 2018, Shi 2025, Sohn 2007: Crossref online-first year (2022, 2025, 2017, 2017, 2024, 2006) differs from the list's issue year (2023, 2026, 2018, 2018, 2025, 2007). The issue year is correct under Sage Harvard. No change needed.
- O'Brien 2009: Crossref gives only the first page (310). The list's 310–327 is the known range.
- Nguyen 2024: Crossref has a Vietnamese title and Vietnamese author diacritics. The list's bracketed translation and "(in Vietnamese)" follow Sage practice. Issue "2V" and pages 61–71 match.
- Moghadam and Sarlo 2024 dataset: DOI 10.7294/26880898.v1 is not in Crossref. It resolves in DataCite (title, authors Moghadam A and Sarlo R, publisher University Libraries Virginia Tech, year 2024: all match).
- Ghali et al. 2017: Crossref confirms the DOI, authors and title ("Structural Analysis"). No edition is given in Crossref or the list; see 3a.

## 3. Findings

### blocking
None found.

### should-fix
a. Reference list formatting is not Sage Harvard. In the built PDF (Manuscript_ASE.pdf, References; the markdown has no emphasis markers) journal names, book titles and proceedings titles are not italicised. Sage Harvard italicises the journal, book and conference-proceedings title, for example "Journal of Bridge Engineering 28(2): 04022138". Fix: italicise those elements in all entries, or confirm that ASE accepts plain text at submission.
b. Ghali et al. (2017) has no edition. The DOI 10.1201/9781315273006 is the 7th edition. Sage style gives the edition after the title for books (as done for AASHTO, 10th ed., and Frýba, 3rd ed.). Fix: "Structural Analysis: A Unified Classical and Matrix Approach. 7th ed. Boca Raton: CRC Press." Please confirm the edition against the book.

### minor
c. The Sage in-text rule is "Author (year)" or "(Author, year)". Both are used correctly. The mixed narrative form "Deng et al. (2025)", "Yu et al. (2016)", "Nguyen et al. (2024)", "Ojio and Yamada (2002)", "Moses (1979)" and "Katafygiotis and Beck (1998)" is fine. No action.
d. Ojio and Yamada (2002), Jacob et al. (2002), Al-Qadi et al. (2016), Moghadam (2022 thesis), CEN (2003) and AASHTO (2024) have no DOI and could not be checked against Crossref. The rosap and VT handle URLs were not reachable from the audit environment (HTTP 403 and 404 on automated fetch), so they are unverified. Fix: confirm manually before submission that https://rosap.ntl.bts.gov/view/dot/35735 and hdl.handle.net/10919/111390 resolve and that the ICWIM3 pages are 209–218.
e. Métodos y Materiales entries have no issue number although Crossref lists 11 and 8. Optional.
f. Self-citation: Nguyen et al. (2024) has the first author of this paper (Quoc-Bao Nguyen) as first author. It is cited once, descriptively and accurately, and is flagged only because a reviewer may notice it.

## 4. Citation-content check (where abstracts were verifiable)
All verified usages are accurate:
- Hao 2019: abstract confirms axle-weight identification with model experiments on simply supported and continuous beams. OK.
- Zuo 2019: multi-T-girder weight identification with the load transverse distribution effect. OK.
- Deng 2025: abstract confirms use of the area of the absolute field value. OK.
- Yang 2021 (strain integral coefficient), Zhu 2022 (strain response area), Agüero-Barrantes 2023 (area and centroid with Kriging) and Agüero-Barrantes 2021 (number and location of sensors, single-span) support "strain areas and integrals / sparse sensing". OK.
- Lobo Aguilar 2018 (shear-strain BWIM), Shi 2025 (load cells at supports), Cardini 2009 (long-term SLM-type system), Žnidarič 2018 (accuracy improvements), Yu 2018 (transverse position), OBrien 2006 (measured influence lines), Yu 2016 (review), Lin 2023 (rotational spring stiffness from influence lines), Wang 2026 (deflection influence-line identification) and Zhou Y 2026 (stiffness inversion from deflection influence lines, continuous beams) all match what the text says they do.
- Moghadam 2023a: reports mean absolute GVW error 4.6 % on the 144 m span concrete box girder. This matches the Supplement ("4.6 %") and the five-span geometry 86.5 + 3 × 144 + 86.5 = 605 m.
- Ventura 2024: concerns the frequency of traffic overloading, linked to bridge failure probability. It is used only for "risk-informed asset management". Acceptable.
- Not verifiable from open abstracts (publisher abstracts elided): Fan 2015 (collapse linked to heavy vehicles), Helmi 2014 ("accurate to within 5 % on a seven-span slab-on-girder bridge for test trucks with well-estimated speeds"), Chaudhary 2025 (distributed fibre-optic strain, continuous bridges), Wu 2020, Zhou C 2025, Zhang 2026, Yan 2022, Moghadam 2022 and 2023b. The Helmi "5 %" and "seven-span" details are the most specific and the highest risk; the authors should re-check them against the full text. No contradiction was found.
- The cover letter (Yu 2016; Hao 2019; Zuo 2019; Lin 2023; Wang 2026 as "published in this journal") is correct: all five are in Advances in Structural Engineering per Crossref.

## Counts
blocking: 0 | should-fix: 2 | minor: 4 (items c is a no-action note and is not counted; d, e, f counted plus the unverifiable-abstract caveat in section 4)
