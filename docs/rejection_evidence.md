# Rejection evidence for Paper 1 (1D, deflection-integral load observability)

Sources are Google Drive files listed in `drive_inventory_paper.md`; local text copies are in `/home/user/SHM-Paper1-1D/manuscript/text/`.

## 1. Editor decision text: none found

No decision letter, editor email or rejection notice for Engineering Structures (ENGSTRUCT-D-26-08490) or for JCSHM (CSHM-D-26-00881) exists in the Drive folders searched, nor anywhere else in the Drive full-text searches ('desk reject', 'Editor', 'CSHM-D-26-00881', 'ENGSTRUCT', 'ENGSTRUCT-D-26-08490', 'regret', title searches). The files named after those manuscript numbers are Editorial Manager "Manuscript Draft" PDFs generated at submission, not decisions. The only statement that the paper was rejected on Drive comes from the authors' own diagnosis, quoted next.

The diagnosis file states the same limit itself:

> "Không tìm thấy thư quyết định gốc nào trong hộp thư vuthaison@gmail.com: địa chỉ đăng ký trong Editorial Manager là sonvt2@huce.edu.vn." (BaoCao_ChanDoan_Reject_StructuralPaper.docx, section 2)

> "Với Engineering Structures: không có bất kỳ mô tả lý do nào trên Drive. Việc lấy lại thư này từ hộp thư HUCE là việc điều tra ưu tiên số một." (same file, section 2)

> "GIỚI HẠN BẰNG CHỨNG. Không tìm thấy thư quyết định gốc của bất kỳ tạp chí nào ... Lý do từ chối của Engineering Structures hoàn toàn chưa xác định." (same file, closing note)

Action needed from the user: pull the ES (ENGSTRUCT-D-26-08490) and JCSHM (CSHM-D-26-00881) decision emails from sonvt2@huce.edu.vn. Nothing below should be read as the editors' reasons.

### Timeline facts (secondary source: BaoCao_ChanDoan_Reject_StructuralPaper.docx, dated 27.08.2026)

- 16.08 Engineering Structures, ENGSTRUCT-D-26-08490, Paper 1 (1D): "Từ chối trong <= 6 ngày".
- 22.08 J. Civil SHM (Springer), CSHM-S-26-01166, Paper 1 (second submission): "Đang xét" at that date. The later number CSHM-D-26-00881 (PDF created 01.09.2026) is the JCSHM manuscript the user says was desk-rejected; the Drive has no document on that outcome.
- The same file says the group saw four rejections across the series (JSV about 20 h and IJMS about 7 h are desk rejects of Paper 3, not Paper 1). Its only verbatim rejection quotes are for IJMS (Paper 3), taken from README_START_HERE.docx and IJMS_to_SHM_Detailed_Revision_Plan, which are not about Paper 1.

### Statements in the diagnosis that apply to Paper 1 (author-written, not editor-written)

> "Ba tạp chí cơ học tổng quát (JSV, IJMS, và nhiều khả năng cả Engineering Structures) đều đọc công trình như kỹ thuật cầu, trong khi bản thảo được viết như cơ học lý thuyết. Đây là scope mismatch, không phải phán quyết về chất lượng khoa học."

> "Cover letter đã tự nói ra: “and no field data are reported” (ES) ... Với AE của Engineering Structures, một bài BWIM không dữ liệu cầu thật là desk-reject tự động — không cần mở file PDF."

These are the authors' inference, not a quotation from the journal.

## 2. Main criticisms, Phan_bien_8_tac_nhan_JCSHM.md (Vietnamese, pre-submission critique of JCSHM_Submission.docx by 8 simulated reviewers)

This file is NOT a rejection. It is an internal critique written before the JCSHM submission. Overall verdict: "nộp được sau một vòng sửa ngắn trên bàn giấy", weighted score 7,5/10 (technical correctness 8,5; measurement quality and statistics 6,5; novelty 6,0; importance 7,0; conclusions vs evidence 7,5; reproducibility 9,0; presentation 7,5; submission procedure 8,0). Its mathematics checks passed; the criticisms are:

- A4-1 (chặn nộp), tính mới: quan hệ tích phân đáp ứng = tổng tải x diện tích đường ảnh hưởng đã có trong cộng đồng BWIM ("influence area"); gần nhất là chỉ số Integral Mean of Strain (Measurement, 2025). Danh mục 40 tài liệu không có mục nào thuộc họ này, bỏ trống từ Andersen-Mukhopadhyay 1950 [32] tới bài trước của nhóm [33]. Đề xuất đặt lại tính mới vào bốn kết quả của dầm siêu tĩnh: quỹ tích mù dạng đóng, dạng đóng cho dầm hai nhịp bất kỳ (tham số mu), chỉ số |C_m| trước lắp đặt, và "giá của tính bất biến" O_m <= 1.
- A1-1: kênh đo là chuyển vị tuyệt đối, khó đo nhất trên cầu đang khai thác (không có mốc cố định, LVDT cần giá tựa đất, thị giác/radar trôi nền). Giả định eps0 = 0,02 đến 0,05 mm ở Bảng 11 là lạc quan.
- A1-2: căng thẳng nội tại giữa "không cần cấu hình trục" và nhu cầu biết tốc độ (đoàn nhiều trục phải khớp bình phương tối thiểu với khoảng cách trục làm tham số).
- A1-3: nhiều xe cùng lúc, chỉ nói "loại bỏ", thiếu ước lượng tỷ lệ lượt xe còn lại; A1-4: biến thiên EI theo nhiệt độ làm C_m đổi, SLM chỉ khử phần chung.
- A2-2 (khuyến nghị giá trị cao nhất): định lý không giới hạn ở chuyển vị, mở rộng sang biến dạng, góc xoay, phản lực. A2-3: chữ "observability" dùng rộng hơn nghĩa; nên gọi "total-load observability".
- A5: tính bất biến, luận điểm trung tâm, chưa được kiểm trực tiếp (ba cấu hình thay đổi cả tổng tải lẫn khoảng cách trục); R^2 = 0,99998 trên ba điểm không có giá trị chứng minh; toàn bộ thí nghiệm là tĩnh dù chữ "crossing" dùng khắp Mục 3; kết luận nói quá "one-, two- and three-axle groups" (lượt đơn là lượt chuẩn).
- A3: thành phần loại A bị "chặn" trong khi dữ liệu ba chu kỳ đo đã có; lỗi thập phân Mục 4.1 (0,1260/0,1989 phải là 1,2596/1,9893 mm^-1); cột Bias Bảng 7 không mang thông tin; tải chuẩn nhẹ hơn tải đo; thiếu cấp chính xác quả cân; dải sai số hiện trường 3-11% và 6-19% quá rộng.
- A6: một lỗi thập phân, một câu lặp nguyên văn (Mục 3.1), phát biểu Hệ quả thiếu công thức, câu "three quarters" sai, thứ tự trích bảng, Bảng 12 ghi 0,001 so với 0 ở Bảng 1 và 8.
- A8: thân bài khoảng 16.000 từ (JCSHM điển hình khoảng một nửa), đánh số phương trình không tuần tự (11, 11a, 11b, 11c, 15, 15a), câu cuối bài.

Follow-up file BaoCao_PhanBien_6TacNhan_Forensic_JCSHM.docx (22.08.2026) records how a pre-submission forensic audit of the same manuscript was applied: abstract cut from 269 to 244 words, the 27 equations (previously images) converted to native Word OMML, "dưới 1 %" corrected to "xấp xỉ 1 % tại tám chu kỳ", the abstract changed to say only the two- and three-load groups were identified, "Declarations" renamed "Statements and Declarations"; "không có thay đổi khoa học". Open items it lists include DOI checks, two ORCIDs and the suggested reviewers.

## 3. Main criticisms, BaoCao_PhanBien.docx (Vietnamese, "Phản biện 6 tác nhân")

This file reviews the earlier JMES-format manuscript "Indirect identification of service loads on two-span continuous beams based on mid-span deflection measurements" (file 01. Research Paper - 03.docx), before the ES/JCSHM versions. It is also not an editor decision. Verdict: "bản thảo hiện tại ở mức Q3-Q4 (đúng tầm JMES ...)"; the theory core is sound but "phải sửa 17 lỗi và bổ sung 6 phân tích mới". Criticisms:

- Mô tả sai gối trung gian B ("fixed support preventing both vertical displacement and rotation"), trong khi mô hình là dầm liên tục gối đơn; điều kiện biên viết sai vị trí (s = l/2 thay vì s = l) và thiếu điều kiện thật sự cần.
- Con số "60-70%" sai (đúng là khoảng 72%).
- Lỗi công thức: Eq. (15)/(16) nhánh ba dùng 192EI thay vì 64EI; Eq. (20) 1/128 thay vì 1/192; Eq. (13) viết tổng chữ nhật chứ không phải hình thang; Eq. (10)-(11) mâu thuẫn Eq. (17) về miền tích phân [0, 2l + a_max].
- Sáu giá trị lực sai hệ số 1000 (ví dụ 67,730.0 N thay vì 67.73 N).
- Khẳng định "tích phân giải tích và số trùng khớp giá trị chính xác" sai: sai lệch cầu phương -0.50% (hình thang, dx = 250 mm); BPM mang sai lệch hệ thống này, SLM triệt tiêu; đề xuất Simpson.
- Bảng 3 (Monte Carlo) không nhất quán nội tại (BPM và SLM trùng nhau tới hai chữ số dù độ chệch khác nhau); kết luận "SLM giảm độ nhạy nhiễu" sai về xác suất: SLM triệt tiêu sai số common-mode nhưng khuếch đại nhiễu ngẫu nhiên độc lập theo sqrt(2).
- Thiếu: trôi điểm không (dP/P = eps*L_tot/I_y, 0,4-1,0% chỉ từ độ phân giải LVDT, 4-10% trên cầu thật), tốc độ xe, mô hình nhiễu phi vật lý, độ lặp lại (độ lệch chuẩn ba lần đo), thí nghiệm cùng tổng tải khác khoảng cách trục.
- Tài liệu: tham chiếu [10] (Qiu 2025) nghi bịa (trùng số bài và DOI với [9] Gajda 2025); [20] và [2,3] trích sai chỗ; [18], [23], [3] thiếu thông tin; thiếu hẳn dòng BWIM (Moses 1979, Znidaric, OBrien), chỉ 27 tài liệu (Q1 chuẩn 45-70).
- Độ mới: tính bất biến "chỉ là diện tích dưới đường ảnh hưởng" (phản biện R1, "đòn nặng nhất"); đề xuất phát biểu thành định lý tổng quát cho mọi dầm tuyến tính và mọi điểm đo.
- Hình thức: đánh số công thức hỏng, Fig. 3 và Fig. 4 không đạt chuẩn, abstract 340 từ, mở đầu 1,400 từ, mục 4 được hứa nhưng không có, thiếu CRediT/Data availability/Nomenclature.
- Tạp chí: JMES (ESCI, JIF khoảng 0.4) không phải Q1/Q2. Bảng độ phù hợp: Structures và Measurement (5 sao), JCSHM (4 sao), Engineering Structures (3 sao: "cần dữ liệu hiện trường hoặc phân tích động"), MSSP (1 sao).

Related files (not editor text): Q1_Improvement_Recommendations_Service_Load_Identification.pdf (score about 8.1/10, asks for rigorous proof, B-support correction, parametric study, dynamic analysis, field validation) and Huong_nghien_cuu_tiep_theo_Deflection_Integral_Load_Observability.pdf (follow-up topics: VBI and road roughness first, then real-bridge field validation; notes it was written from the review of ENGSTRUCT-D-26-08490).

## 4. Engineering Structures version vs JCSHM version

Compared: `ENGSTRUCT-D-26-08490.txt` and `Manuscript_EngStruct_Submission.txt` (ES, 17,058 words in the manuscript docx text) against `CSHM-D-26-00881.txt` and `JCSHM_Submission_docx_v_drive.txt` (JCSHM, 16,738 words). The two share the same section structure (2.1-2.7, 3.1-3.4, 4.1-4.7, 5.1-5.5), the same equations, tables, experiment and numbers. Paragraph-level comparison: 140 of 313 ES paragraphs and 133 of 306 JCSHM paragraphs are not identical, mostly equation placeholders, figure captions and small rewording. Differences found:

| item | Engineering Structures (16 Aug 2026) | JCSHM (22 Aug 2026) |
|---|---|---|
| title | "Load observability from the deflection integral of continuous beams: invariance theorem, closed-form blind configurations, dynamic validity and experimental validation" | "Load observability of continuous bridge beams from a single deflection sensor: invariance, blind configurations and laboratory validation" |
| article type | Research Paper | Original Paper |
| abstract opening | "Identifying the gross weight of vehicles crossing a bridge normally requires a dedicated weigh-in-motion installation, or an ill-posed inverse problem solved from a dense sensor array." | "Before a bridge monitoring system can weigh traffic, a prior question must be answered: ... is the total load observable at all?" |
| abstract on experiment | "identify one-, two- and three-axle groups to within 1.19 % and 0.70 %" | "verify the influence line and identify unknown two- and three-load groups within 1.19 % ... and 0.70 % ... relative to direct weighing" (single load is the reference run, per the forensic audit) |
| abstract on dynamics | "bounds the dynamic error below 1 % once the crossing time exceeds eight fundamental periods" | "approximately 1 % at a crossing time of eight fundamental periods and below 1 % for larger ratios" |
| abstract ending | "an error budget shows that zero-offset drift, and not random noise, dominates" | "zero-offset drift and speed estimation as the principal field sensitivities ... a total-load estimator and a pre-deployment observability criterion for sensor placement" |
| keywords | Deflection integral; Load identification; Continuous beam; Bridge weigh-in-motion; Load observability; Measurement uncertainty | Structural health monitoring; Bridge weigh-in-motion; Load observability; Deflection integral; Sensor placement; Measurement uncertainty |
| abstract length | 258 words (counted) | 244 words (limit 250) |
| Highlights | 5 bullets present | none |
| Methods text | contains "Computational implementation ... in Python for the analysis and in Node.js for document assembly, with the assistance of a generative AI tool" (flagged in the diagnosis as an unnecessary self-disclosure) | sentence about Node.js absent; AI use declared in "Statements and Declarations" |
| back matter | Elsevier style: "Declaration of competing interest", "Declaration of Generative AI ...", Data availability | Springer style: "Statements and Declarations", Code availability |
| equations | LaTeX-rendered images | 27 native Word (OMML) equations |
| cover letter | Elsevier frame: "conclusions ... in a form a designer can act on"; limitations include "the dynamic study models a constant force ..., the unequal-span results are analytical and numerically verified but not yet tested experimentally, and no field data are reported" | SHM frame: "Before a monitoring system can weigh traffic ... is the load observable at all?"; limitations: laboratory scale, 1-D, field entries are scenarios, the blind configuration is not yet tested experimentally; claims fit because of "laboratory verification rather than ... numerical work alone"; says the manuscript "is not under consideration by any other journal" |
| scope of validation | identical in both: one 2 x 2500 mm steel tube beam (25 x 25 x 2.03 mm), static weights moved at 250 mm steps, 3 load configurations, LVDT 0.005 mm, FE (Abaqus), Monte Carlo, constant-force moving-load FE; no VBI, no field data, blind configuration not tested experimentally | same |

The diagnosis file measured 81.1 % verbatim 8-gram overlap between the ES and the earlier JCSHM (CSHM-S-26-01166) versions ("Cùng một bài, đổi tiêu đề, viết lại abstract"), and the Editorial Manager text of the first JCSHM submission (CSHM-S-26-01166.txt) is identical to CSHM-D-26-00881.txt apart from the manuscript number (word-level similarity 0.99997).

## 5. Reference [33] (earlier simply-supported paper)

From the JCSHM reference list (JCSHM_Submission_docx_v_drive.txt, ref 33): Nguyen QB, Hoang T, Nguyen HS (2024) "Determination of the load applied on a simple supported beam based on measured deflection data". J Sci Technol Civ Eng (HUCE) 18:61-71. https://doi.org/10.31814/stce.huce2024-18(2V)-05. The paper itself is not on Drive. The manuscript says of it: "That study demonstrated the idea on a statically determinate beam, where the influence line is of one sign and no configuration is blind ... None of these results is present in [33], and the two studies share no structure, no specimen configuration and no data."
