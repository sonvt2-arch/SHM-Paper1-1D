> **Đã cũ.** Dùng `docs/PROMPT_PHIEN_MOI_2026-10-20.md` và `docs/00_TONG_QUAN_HIEN_TRANG.md` (20/10/2026).

# Prompt để mở phiên làm việc mới

Dán một trong các prompt dưới đây vào phiên Claude Code mới, mở trên kho `sonvt2-arch/shm-paper1-1d`.

## Mẫu 1: Làm tiếp khi đã có câu trả lời của người lập báo cáo

```
Tiếp tục dự án bài báo SHM Paper1-1D trong kho sonvt2-arch/shm-paper1-1d, nhánh claude/focused-bell-33lm0n (checkout nhánh này, làm và đẩy lên đúng nhánh này).

Bước 1: Đọc theo thứ tự
- docs/00_MO_TA_CHI_TIET_DU_AN.md (bối cảnh, quyết định, kết quả, bản đồ file, việc cần làm theo từng mã câu hỏi)
- docs/05_trang_thai_va_viec_tiep_theo.md
- manuscript/schm/open_items.md
Tóm tắt lại cho tôi trong 10 dòng trước khi làm gì.

Bước 2: Câu trả lời của người lập báo cáo
[DÁN CÂU TRẢ LỜI, hoặc ghi: "file trả lời ở Google Drive, thư mục ..." / "file Word đính kèm"]
Số liệu thô (nếu có) ở Drive: Paper1 - 1D/Upload_GitHub/[TÊN THƯ MỤC] (các phần .zip.001, .002… mỗi phần ≤ 2 MB; ghép lại theo docs/06_huong_dan_chia_file_len_drive.md).

Bước 3: Xử lý theo bảng mục 5 của 00_MO_TA_CHI_TIET_DU_AN.md
- Mỗi câu trả lời: chạy lại script liên quan, lưu log vào code/analysis/logs/, cập nhật manuscript/schm/manuscript.md và traceability.md.
- Ưu tiên: B7/C5 (file thô lượt xe chạy, để kiểm cân tải bằng tích phân trên cầu liên tục) > B1–B3 (chốt chỉ số N8 Cầu Mây) > C1–C3 (thêm cầu Thái Bình) > các mục điền [NEED VALUE].
- Kết luận chính thay đổi thì chạy lại phản biện đỏ 3 vai (Opus) và kiểm số/DOI (Haiku).

Quy tắc: không tự điền số, thiếu thì ghi [NEED VALUE]; mọi con số phải truy được tới file trong repo; giữ nguyên văn câu khai báo dùng AI; dùng skill viet-tu-nhien khi sửa văn bài báo; phân vai agent theo mục 6 của 00_MO_TA_CHI_TIET_DU_AN.md. Commit và push sau mỗi bước; không tạo pull request.

Tạp chí đích: Structural Control and Health Monitoring (Wiley). Dự phòng: Structure and Infrastructure Engineering.
```

## Mẫu 2: Hoàn thiện để nộp ngay, không chờ số liệu thô

```
Tiếp tục dự án SHM Paper1-1D trong kho sonvt2-arch/shm-paper1-1d, nhánh claude/focused-bell-33lm0n. Đọc docs/00_MO_TA_CHI_TIET_DU_AN.md và manuscript/schm/open_items.md trước.

Tôi muốn nộp SCHM với số liệu hiện có. Đây là các thông tin còn thiếu:
- Cấp chính xác quả cân: [ ]
- Quyền công bố số liệu Cầu Mây / Gie Cục / Phương Độ: [ ]
- Lời cảm ơn: [ ]
- Funding (đơn vị, ai trả phí): [ ]
- Trùng giàn thử/số liệu với 2 bài ở Structures: [có/không, tên bài]
- Xung đột lợi ích (Công ty TNHH Tư vấn ĐHXD): [ ]
- Ngày nộp, ORCID: [ ]
- File hình thí nghiệm (Fig. 1, 2, 4, 5, 6, 10): [vị trí trên Drive]
- Script bổ sung (SupplementaryMaterial_JCSHM.zip đã chia phần): [vị trí trên Drive]

Hãy: điền vào bản thảo; đưa hình và script vào repo; chạy wp7b_checks.py; kiểm lại toàn bộ bằng một agent Haiku (số liệu, tham chiếu chéo, DOI); xuất bản thảo và thư gửi biên tập ra file Word theo định dạng SCHM; cập nhật submission_checklist.md. Commit và push lên đúng nhánh; không tạo pull request.
```

## Mẫu 3: Phiên ngắn, chỉ hỏi trạng thái

```
Đọc docs/00_MO_TA_CHI_TIET_DU_AN.md trong kho sonvt2-arch/shm-paper1-1d (nhánh claude/focused-bell-33lm0n) và cho tôi biết: bài đang ở bước nào, còn thiếu gì để nộp SCHM, và việc nào nên làm trước.
```
