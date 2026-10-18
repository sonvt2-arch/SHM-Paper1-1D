# Trạng thái và việc tiếp theo

Cập nhật: 2026-10-12. Trạng thái: **chờ câu trả lời của người lập báo cáo** (bảng câu hỏi `docs/word/Cau_hoi_bo_sung_so_lieu.docx`). Mô tả đầy đủ: `00_MO_TA_CHI_TIET_DU_AN.md`.

Cập nhật trước: 2026-10-11. Nhánh: `claude/focused-bell-33lm0n`.

## Cập nhật 2026-10-18
- Đưa câu trả lời mới (từ bảng hỏi bài MSSP, `08_cap_nhat_...md`) vào bản SCHM: xe Cầu Mây 25,06 t (dải sai số nhịp biên 35–93%), Data Availability, Conflicts of Interest (còn [NEED VALUE] tên tác giả), thiết bị Mitutoyo, sai số đặt xe < 20 cm (≤ 0,6% ở N8).
- Xuất Word: `manuscript/schm/word/Manuscript_SCHM.docx`, `Cover_Letter_SCHM.docx` (dựng lại bằng `build_docx.sh --pdf`).
- Gói script bổ sung `code/supplementary/` (`run_all.sh`, `REPRODUCTION_REPORT.md`). 10 nhận định cũ không tái lập được đã được sửa cho khớp script; ghi tại `manuscript/schm/changelog_reproduction.md`. Khi có `SupplementaryMaterial_JCSHM.zip` gốc thì đối chiếu lại.
- Còn chờ tác giả: giải nén `Thông tin bổ sung.rar` (phiếu cân, Midas); chia phần `SupplementaryMaterial_JCSHM.zip`; tên tác giả tham gia thử tải; hình thí nghiệm; bảng hỏi riêng của Paper1 (B2, B3, B7, phần A).

## 1. Đã làm

| Gói | Kết quả | Tác nhân (model) |
|---|---|---|
| Kiểm kê dữ liệu | 5 cầu và tài liệu bài báo trên Drive → `data/bridges/`, `manuscript/text/` | 6 agent (Sonnet) |
| WP1 | Ma trận tính mới, kiểm 31 DOI, chọn tạp chí | Literature Scout (Sonnet) |
| WP2 | Nghiệm kín 3 nhịp: β_crit = 1,700594; dải gần mù 1,621399–1,775; kiểm FE < 1e-8 | Structural Theorist (Opus) |
| WP3 | Cầu Mây: hai cách hiệu chỉnh cùng khớp số đo → N8 = 0,181 / 0,476, N7 = 0,209 / 0,234. Thái Bình chưa dùng được (mô hình lệch tới 22%) | Bridge Modeller (Opus) |
| WP4 | Bản ghi động Gie Cục, Phương Độ: không kiểm được tải tuyệt đối; dùng được cho trôi nền và lọc | Signal Analyst (Sonnet) |
| WP7 | Bản v1 (Structures) → v2 (sau phản biện) → bản SCHM | Writer/Reviser (Opus + viet-tu-nhien) |
| WP8 | Phản biện đỏ 3 vai (32 vấn đề) và kiểm số/DOI; đã xử lý trong v2 | Red Team (Opus), Verifier (Haiku) |

Quyết định của tác giả: lộ trình A (chỉ dữ liệu có sẵn), không làm thêm thí nghiệm, tạp chí đích SCHM (tác giả xác nhận không mất phí). Chi tiết ở `02_ke_hoach_va_phan_vai.md` §5–7.

## 2. Việc tác giả cần làm trước khi nộp (`manuscript/schm/open_items.md`)

1. Gửi file hình thí nghiệm: Fig. 1, 2, 4, 5, 6, 10 (đang nằm trong file docx trên Drive).
2. Điền: cấp chính xác quả cân; quyền công bố số liệu Cầu Mây; lời cảm ơn; phiếu cân xe Cầu Mây.
3. Mục Funding: đơn vị công tác, ai trả phí (hoặc miễn phí).
4. Xác nhận bài không trùng giàn thử hoặc số liệu với hai bài đang nộp ở *Structures*.
5. Quyết định có khai đơn vị tư vấn HUCE (thử tải Cầu Mây) ở mục xung đột lợi ích không.
6. Kiểm phí xuất bản ở bước khai báo khi nộp (DOAJ ghi tối đa 2.370 USD, có chính sách miễn giảm).
7. Gửi thư xin số liệu `03_thu_xin_so_lieu.md` cho người lập báo cáo kiểm định.

## 3. Vấn đề còn mở

- **Script tài liệu bổ sung còn thiếu.** Bài ghi là nộp kèm các script Monte Carlo, tải di động, kiểm ký hiệu 2 nhịp và bảng sai số cầu phương, nhưng repo chưa có. Bản gốc nằm trong các file zip ở thư mục Drive "Python" (ID trong `drive_inventory_paper.md`). Hai cách: (a) tác giả tải bản giải nén lên; (b) viết lại từ phương trình trong bài rồi chạy đối chiếu.
- **Cầu Mây, điểm N8:** chỉ số quan sát được không nhận dạng được từ hai số đọc tĩnh (0,18–0,48). Khi có mô hình MIDAS hoặc kích thước trụ, chạy lại `wp3_run.py` để chốt.
- **Thái Bình:** cần 3–5 trang bản vẽ (mặt cắt dầm hộp giữa nhịp và đỉnh trụ, mặt cắt dọc, trụ T12–T13) để dựng lại mô hình. Nếu khớp FE của báo cáo trong khoảng ±5%, đưa vào bài làm cầu thứ hai (β = 1,5, dưới ngưỡng, đối chứng với Cầu Mây β = 1,636).
- **Độ dài:** phần chính 9.221 từ. SCHM không giới hạn; có thể rút thêm nếu muốn.

## 4. Dự phòng
Nếu SCHM từ chối: Structure and Infrastructure Engineering. Cần đổi khung bài sang lập kế hoạch quan trắc và quản lý cầu (xem `wp8_red_team_report.md` §1b); thư gửi SIE có ở `manuscript/v2/cover_letter_SIE.md`.
