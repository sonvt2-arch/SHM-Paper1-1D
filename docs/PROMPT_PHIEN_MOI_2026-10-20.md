# Prompt cho phiên làm việc mới (dán nguyên văn khối dưới)

```
Tiếp tục dự án SHM-Paper1-1D (repo sonvt2-arch/SHM-Paper1-1D, nhánh claude/focused-bell-33lm0n; mọi thay đổi commit rồi push lên CẢ HAI nhánh claude/focused-bell-33lm0n và claude/loving-brown-3hgpml).

Trước khi làm gì, đọc theo thứ tự:
1. docs/00_TONG_QUAN_HIEN_TRANG.md: tổng quan, tệp nộp, cách dựng, quy ước, việc còn mở.
2. docs/06_trang_thai_ASE.md: nhật ký trạng thái theo ngày.
3. manuscript/ase/submission_checklist.md.
4. Nếu cần: docs/editors_v4/hostile_audit_v2/00_tong_hop.md, docs/editors_v4/gate4_ase/00_tong_hop.md, docs/editors_v4/xii13_ase/, docs/editors_v4/xii14_ase/00_bao_cao.md.

Bối cảnh: bài "Blind loci and sensor layout for influence-area bridge weigh-in-motion on continuous girders" (Quoc-Bao Nguyen, Thai-Son Vu) đã sẵn sàng nộp Advances in Structural Engineering (Sage), chưa nộp. Bản cuối khoảng 11.900 từ quy đổi; thầy chọn giữ "viết đủ". Đã qua Cổng 4, hostile audit lần 2, đọc mù XII.13 lượt 12, kiem_khoa; độ dễ đọc XII.14 D = 5.

Quy ước bắt buộc:
- Gọi tôi là "thầy", xưng "em", trả lời tiếng Việt. Khi cần tôi quyết, hỏi bằng câu bấm chọn, phương án khuyên dùng đặt đầu.
- Không làm thêm thí nghiệm, chỉ dùng dữ liệu đã có. Không bịa số; chỗ thiếu để [NEED VALUE].
- Theo plugin viet-tu-nhien (Quy tắc v4.0). Sau mỗi lần sửa bản thảo: đối chiếu số hai chiều bằng kiem_khoa.py (thư mục scripts của plugin viet-tu-nhien), dựng lại bằng `bash manuscript/ase/word/build_docx.sh --pdf`, kiểm PDF không có '¿', giữ dưới 12.000 từ quy đổi (số từ docx đếm bằng python-docx gồm cả bảng, cộng khoảng 28, cộng 300 cho mỗi hình hoặc bảng). Trước khi giao bản nộp, chạy đọc mù XII.13 bằng tác nhân mới.
- Tự trích bài đã đăng của thầy tối đa 2. Chính tả lối Mỹ. Khai báo AI để trong Acknowledgements.
- Môi trường: cài libreoffice-math (nếu không PDF mất công thức), cùng matplotlib, scipy, sympy. Vẽ hình với MATPLOTLIBRC có font Inter.
- Không đưa dữ liệu cầu Thái Bình hay mã Drive vào gói nộp (scripts.zip đã sạch).

Việc tiếp theo (hỏi thầy trước khi làm): [ghi việc thầy muốn, ví dụ: sửa theo nhận xét của thầy sau khi đọc bản Word / chuẩn bị nộp / trả lời phản biện].
```
