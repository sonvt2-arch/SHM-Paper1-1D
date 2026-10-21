# Tổng quan hiện trạng dự án SHM-Paper1-1D (cập nhật 21/10/2026)

## 1. Bài báo

- **Nhan đề:** "Blind spots and sensor placement for influence-area weigh-in-motion on continuous girders"
- **Tác giả:** Quoc-Bao Nguyen, Thai-Son Vu (tác giả liên hệ)
- **Tạp chí đích:** Advances in Structural Engineering (Sage).
  - Loại bài: Original Research Article; không thu phí, không Gold OA.
  - Trần độ dài: 12.000 từ quy đổi (số từ Word + 300 cho mỗi hình hoặc bảng).
- **Trạng thái: sẵn sàng nộp, CHƯA nộp.**
  - Ngày nộp ghi trong thư: 21 October 2026; nếu nộp muộn thì sửa ngày này.
  - Trước khi bấm nộp, thầy còn ba việc (mục 6).

### Nội dung chính

Phương pháp cân xe theo diện tích đường ảnh hưởng chia diện tích bản ghi cho một hằng số tích phân C. Trên dầm liên tục, C có thể bằng 0 vì đường ảnh hưởng đổi dấu.

Bài có ba đóng góp:
1. **Danh mục dạng đóng các điểm mù và gần mù** cho năm loại kênh đo.
   - Gauge biến dạng đo uốn tổng thể mù tại mọi điểm không của mômen dưới tải đều.
   - Trên hai nhịp bằng nhau, gauge biến dạng gần mù ở khoảng 0.19–0.32 nhịp tính từ gối giữa.
   - Gauge độ võng ở nhịp biên chỉ mù khi nhịp kề dài hơn.
   - Nhịp giữa của dầm ba nhịp gần bằng nhau (0.9647 ≤ β < 1.2247) cũng có điểm mù.
2. **Quy tắc đặt cảm biến** ở cực trị của đáp ứng dưới tải đều (Elfving, Pukelsheim).
   - Trên một ngày số liệu NOR-BWIM công khai, GLS dùng nhiễu khi không có xe cho sai số cao hơn trung bình các gauge 8.5 điểm phần trăm.
3. **Luật Möbius (phân thức tuyến tính) của C theo độ cứng trụ**, suy từ công thức Sherman–Morrison.
   - Áp cho cầu Mây 55 + 90 + 55 m, mô hình cơ sở.
   - Khi α tự do, hằng số nhịp biên N8 có tỷ số lớn nhất trên nhỏ nhất là 6.6, so với 1.5 ở N7 giữa nhịp chính.
   - Khi giới hạn độ cứng dầm 0.9–1.3 lần thiết kế, hai tỷ số này là 2.4 và 1.1.
   - Qua các biến thể mô hình: N8 từ 2.6 đến 16, N7 từ 1.3 đến 1.6.
   - Thiết bị đo nghiêng trụ đưa cận Cramér–Rao của SD(ln C8) từ 0.87 xuống 0.18.

Phần kiểm chứng:
- Thí nghiệm dầm hai nhịp kiểm đẳng thức diện tích ảnh hưởng.
- Số liệu công khai NOR-BWIM kiểm các giả thiết và mô hình nhiễu.
- Cầu Mây minh hoạ giới hạn của khả năng nhận dạng.

### Số đo của bản cuối

| Chỉ tiêu | Giá trị |
|---|---|
| Số từ Word | ≈ 8.650 |
| Hình | 7 |
| Bảng | 3 bảng đánh số + bảng ký hiệu |
| Số từ quy đổi | ≈ 11.990 (python-docx, cả bảng, +28, +300 × 11) |
| Thân bài (Tóm tắt đến Kết luận) | ≈ 6.400 từ; thầy chọn "viết đủ", bỏ mặc định III.19 |
| Tóm tắt | ≈ 190 từ (đếm thô cả ký hiệu toán), viết lại 21/10 theo ba kết quả First/Second/Third; có thể vượt mức ~150 biên tập viên nêu |
| Danh mục tài liệu | 57 bài (21/10 thêm 2 bài JSTCE-HUCE: Dang et al. 2023, Vu et al. 2023), Sage Harvard, tên tạp chí và sách in nghiêng; tự trích bài của thầy 0/2 |
| Supplementary | Mục S1–S11, Bảng S1–S19, Hình S1–S17 |
| Độ dễ đọc XII.14 | D = 5 (chỉ để báo cáo) |

## 2. Tệp nộp (`manuscript/ase/`)

| Tệp | Nguồn | Bản dựng |
|---|---|---|
| Bản thảo | `manuscript.md` | `word/Manuscript_ASE.docx` (+ PDF) |
| Supplementary | `supplementary_material.md` | `word/Supplementary_Material_ASE.docx` (+ PDF) |
| Thư gửi tạp chí | `cover_letter_ASE.md` | `word/Cover_Letter_ASE.docx` (+ PDF) |
| Hình 300 dpi | `figures/Fig1–Fig7_*.png` (+ PDF), `figures/supplementary/` | |
| Graphical abstract | `figures/GraphicalAbstract.png` | tuỳ chọn |
| Gói mã | `word/scripts.zip` | 220 mục; xem `code/supplementary/README.md` |
| Checklist nộp | `submission_checklist.md` (tiếng Việt, KHÔNG nộp) | |

**Dựng lại các tệp:** `bash manuscript/ase/word/build_docx.sh --pdf`
- Cần cài `libreoffice-math`, nếu không PDF mất công thức; script sẽ báo lỗi.
- `postprocess.py` sửa các ký tự công thức LibreOffice vẽ sai. Bản docx vốn đúng.
- Sau khi dựng, kiểm `pdftotext <pdf> - | grep -c '¿'`; kết quả phải bằng 0.

## 3. Mã và dữ liệu

- **Mã của bài:** `code/` (theory2, analysis, norbwim, v4, fieldplan, supplementary).
  - Log nằm trong `code/*/logs/` hoặc `results/`.
  - `code/supplementary/README.md` nối mỗi bảng và hình với script và log của nó.
- **Vẽ hình:** dùng `MATPLOTLIBRC` có `font.sans-serif: Inter`.
  - `schm_figures.py` mặc định ghi đè vào `manuscript/schm/figures`. Muốn vẽ ra chỗ khác thì import module, đặt `s.OUT` rồi gọi hàm.
- **scripts.zip** đã làm sạch:
  - không còn cầu Thái Bình, mã Drive, `[NEED VALUE]`, `wp7b_checks.py`;
  - nhãn trong mã đều tiếng Anh;
  - log của bài không đổi số.
- **Dữ liệu cầu Thái Bình và mã Drive vẫn còn trong repo**, ở các tệp ngoài scripts.zip: `data/bridges/lang-am/`, `data/bridges/cau-may/section_properties.csv`, `INVENTORY.md`. Không được đưa các tệp này vào gói nộp.
- **Số liệu cầu Mây đã làm sạch:** `manuscript/ase/data_release/`.

## 4. Lịch sử kiểm (biên bản trong `docs/editors_v4/`)

| Ngày | Bước kiểm | Kết quả | Biên bản |
|---|---|---|---|
| 19/10 | Hostile audit lần 1 | | `hostile_audit/` |
| 20/10 | Cổng 4 (4 biên tập viên + tổng biên tập mô phỏng) | Vòng 1: cả 4 "sửa rồi gửi". Vòng 2: cả 4 "gửi phản biện" | `gate4_ase/` |
| 20/10 | Hostile audit lần 2 (8 vai) | 9 lỗi chặn, đã sửa hết | `hostile_audit_v2/00_tong_hop.md` |
| 19–20/10 | Đọc mù XII.13 | Lượt 1–12; lượt cuối các mục bắt buộc đã sửa | `xii13_ase/` |
| 20/10 | Chấm độ dễ đọc XII.14 | D 4,5 → 5 | `xii14_ase/` |

Lỗi chặn nặng nhất của hostile audit lần 2: câu "a deflection gauge cannot be blind on equal spans" sai cho nhịp giữa của dầm ba nhịp. Đã sửa ở mục 2.2, Bảng 1, Kết luận 1 và S2.

Trạng thái chi tiết theo từng ngày: `docs/06_trang_thai_ASE.md`.

## 5. Quy ước làm việc (thầy đã định)

- Gọi tác giả là "thầy", tự xưng "em", trả lời bằng tiếng Việt. Khi cần thầy quyết, dùng câu hỏi bấm chọn, phương án khuyên dùng đặt đầu.
- Không làm thêm thí nghiệm; chỉ dùng dữ liệu đã có.
- Theo plugin viet-tu-nhien (Quy tắc v4.0):
  - không bịa số; chỗ thiếu để `[NEED VALUE]`;
  - sau mỗi lần sửa, đối chiếu số hai chiều bằng `kiem_khoa.py`;
  - tự trích bài đã đăng của thầy tối đa 2;
  - trước khi giao bản nộp phải chạy đọc mù XII.13.
- Chính tả lối Mỹ. Khai báo dùng AI đặt trong Acknowledgements theo Sage.
- Mọi thay đổi commit rồi push lên CẢ HAI nhánh: `claude/focused-bell-33lm0n` và `claude/loving-brown-3hgpml`.

## 6. Việc còn mở

1. **Thầy:**
   - mở `Manuscript_ASE.docx` bằng Microsoft Word thật, xem công thức, bảng, hình (mới xem bằng LibreOffice);
   - xem toàn văn Hong et al. (2016) và Wu et al. (2018), vì chỉ trích theo nghĩa rộng, Crossref không có tóm tắt;
   - lấy đường dẫn nộp từ trang ASE trên Sage (journals.sagepub.com/home/ase, mục Submit) rồi nộp.
2. **Mục nhẹ:** đã sửa hết ngày 21/10 (Bảng S1 thêm ký hiệu; chỉ số chữ đứng trong PDF; chữ chồng ở Hình 2b, S8; nhãn thừa và tiêu đề ô phải của graphical abstract; font Inter cho Hình 1, 2, S8, S16, S17; 'fiber' ở S12; S3 ghi rõ dải 2–160 m).
3. **Không có dữ liệu nên chưa sửa:** độ lặp của đồng hồ so ở thử tải cầu Mây; tải trọng và thứ tự từng quả nặng trong thí nghiệm.
4. **Nếu muốn nâng độ dễ đọc** (D = 5, mục tiêu 7): phải bỏ bớt số khỏi thân bài hoặc dựng thân bài ngắn theo III.19, khoảng 5.000–5.500 từ. Thầy đã chọn không làm cho lần nộp này.
5. **Sau khi nộp:** theo dõi phản hồi. Nếu bị trả, phương án dự phòng là JBE hoặc SIE; bảng so sánh ở `docs/editors_v4/journals/`.
