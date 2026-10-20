> **Đã cũ.** Dùng `docs/PROMPT_PHIEN_MOI_2026-10-20.md` và `docs/00_TONG_QUAN_HIEN_TRANG.md` (20/10/2026).

# Prompt cho phiên làm việc tiếp theo

Chép nguyên khối dưới đây vào phiên mới.

---

Tiếp tục dự án bài báo SHM-Paper1-1D trên nhánh `claude/focused-bell-33lm0n`. Xưng "em", gọi tôi là "thầy". Khi cần tôi quyết, đưa các lựa chọn để tôi bấm (AskUserQuestion), phương án khuyến nghị đứng đầu.

**Đọc trước:**
- `docs/06_trang_thai_ASE.md`: trạng thái bản nộp ASE, lịch sử quyết định, việc còn chờ.
- `docs/05_trang_thai_va_viec_tiep_theo.md`: phần đầu.
- `manuscript/ase/submission_checklist.md`.

**Bối cảnh ngắn:**
- Bài "Observability and sensor layout for influence-area load monitoring of continuous girder bridges".
- Tác giả Quoc-Bao Nguyen và Thai-Son Vu (liên hệ). Không còn Hung-Son Nguyen.
- Nộp Advances in Structural Engineering (Sage). Nguồn bản thảo: `manuscript/ase/manuscript.md`, `supplementary_material.md`, `cover_letter_ASE.md`. Dựng Word/PDF bằng `bash manuscript/ase/word/build_docx.sh --pdf`.

**Ràng buộc thường trực:**
- Không làm thêm thí nghiệm; chỉ dùng dữ liệu đã có.
- Theo plugin viet-tu-nhien (Quy tắc viết chung v4.0):
  - không bịa số, chỗ thiếu để [NEED VALUE];
  - đối chiếu số liệu hai chiều bằng `kiem_khoa.py` sau mỗi lần sửa;
  - tự trích dẫn bài đã đăng của thầy tối đa 2;
  - đọc mù chuẩn mực XII.13 trước khi giao bản nộp.
- Trình bày Word theo V.1, V.1.1, V.2 (đã cài sẵn trong các script dựng).
- Khai báo AI: tiêu đề và vị trí theo nhà xuất bản (Sage: trong Acknowledgements), nội dung theo VII.1.
- Chính tả lối Mỹ.
- Mọi thay đổi commit và push lên nhánh trên.

**Việc tiếp theo (hỏi thầy theo thứ tự):**
1. Thầy đã mở bản Word bằng Microsoft Word chưa, và thấy lỗi gì về chỉ số, hình, khoảng trắng? Sửa theo phản hồi rồi dựng lại.
2. Quy tắc v4.0 III.19 (thân bài 4.500–5.000 từ, một mạch, nhiều nhất ba phát hiện): giữ bản ASE như hiện tại ("viết đủ"), hay rút tiếp? Nếu rút: chạy `kiem_de_doc.py`, `kiem_bao_toan_so.py` và chấm độ dễ đọc XII.14, rồi chạy lại đọc mù XII.13.
3. Có thêm các bài ASE gợi ý (Hao 2019, Zuo 2019, Lin 2022, Wang 2025) không? Nếu có: kiểm từng bài từ ba nguồn (VII.4) và giữ dưới trần 12.000 từ quy đổi.
4. Có rút tóm tắt (184 từ) về khoảng 150 từ không?
5. Ngày nộp: điền vào thư gửi tạp chí, dựng lại gói, gửi thầy các tệp nộp.
