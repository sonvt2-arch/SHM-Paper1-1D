# Mô tả chi tiết dự án và hướng dẫn làm tiếp

Cập nhật: 2026-10-12. Kho: `sonvt2-arch/shm-paper1-1d`, nhánh `claude/focused-bell-33lm0n`.
**Đọc file này đầu tiên khi quay lại.** Nó tóm tắt toàn bộ những gì đã làm, các quyết định, kết quả bằng số, vị trí từng file, và việc cần làm khi có câu trả lời của người lập báo cáo.

---

## 1. Bối cảnh

**Bài báo:** xác định tổng tải xe từ tích phân độ võng đo tại **một điểm** trong suốt lượt xe qua cầu. Tác giả: Quoc-Bao Nguyen, Thai-Son Vu (liên hệ), Hung-Son Nguyen, Bộ môn Cầu – Đường, ĐH Xây dựng Hà Nội.

**Ý tưởng cốt lõi:** với dầm đàn hồi tuyến tính, ∫y dx = P_tổng · C_m. Hằng số C_m là diện tích đường ảnh hưởng độ võng tại điểm đo, và bằng độ võng tại điểm đo khi tải phân bố đều đơn vị trên toàn cầu (Maxwell–Betti). C_m không phụ thuộc số trục hay khoảng cách trục. Hai cách tính tải:
- **BPM:** C_m tính từ EI và nhịp.
- **SLM:** lấy tỉ số với lượt xe chuẩn đã biết trọng lượng.

Trên dầm liên tục, đường ảnh hưởng âm ở nhịp kề, nên có cấu hình "mù" (C_m = 0).

**Lịch sử nộp:**

| Tạp chí | Mã | Kết quả |
|---|---|---|
| Engineering Structures | ENGSTRUCT-D-26-08490 | Từ chối tại bàn: không phù hợp phạm vi |
| JCSHM | CSHM-D-26-00881 | Từ chối: phạm vi chỉ gồm công trình thật hoặc mô hình có tỷ lệ đủ suy ra công trình. Thí nghiệm ống thép 25 mm, nhịp 2 × 2,5 m bị coi là không đủ |

---

## 2. Các quyết định của tác giả (theo thứ tự)

1. Lộ trình A: **chỉ dùng dữ liệu có sẵn**, không đo hiện trường mới.
2. **Không làm thêm thí nghiệm** phòng lab.
3. Dàn ý bài mới đã duyệt (`docs/04_tong_hop_ket_qua_lo_trinh_A.md` §2).
4. **Không nộp *Structures*** vì đang có 2 bài khác ở đó.
5. **Tạp chí đích: Structural Control and Health Monitoring (SCHM, Wiley).** Tác giả xác nhận không mất phí; kiểm lại ở bước khai phí khi nộp. Dự phòng: Structure and Infrastructure Engineering (SIE).
6. Thái Bình chưa đưa vào phân tích chính, chờ bản vẽ.
7. Sẽ hỏi người lập báo cáo theo bảng câu hỏi Word (`docs/word/Cau_hoi_bo_sung_so_lieu.docx`).

---

## 3. Kết quả chính (bằng số, đã kiểm)

### 3.1. Dữ liệu 5 cầu (`docs/01_danh_gia_du_lieu_cau.md`, `data/bridges/*/INVENTORY.md`)

| Cầu | Sơ đồ | Có gì | Dùng được cho |
|---|---|---|---|
| Cầu Mây | Liên tục 55+90+55 m, dầm hộp | Số đọc võng tĩnh; I = 5,482 / 59,612 m⁴ (giữa nhịp / mặt trụ) | Áp dụng tiêu chí quan sát được (mục 4 bài) |
| Thái Bình (thư mục "Lạng Am") | Liên tục 42+63+42 m | Số đọc võng tĩnh | Chưa dùng: mô hình lệch tới 22% |
| Gie Cục I | Giản đơn 3 × 25,7 m | Bản ghi động 200 Hz | Minh hoạ trôi nền và lọc (mục 5 bài) |
| Phương Độ | Giản đơn 2 × 18 m | Bản ghi động 200 Hz | Như trên |
| Sông Sặt | Giản đơn | Tĩnh | Không dùng |

### 3.2. Lý thuyết mới cho dầm 3 nhịp (WP2; `docs/wp2_three_span_theory.md`; kiểm bằng FE, sai lệch < 1e-8, 0 lỗi)

- Ký hiệu: β = L_giữa / L_biên, ρ = EI_giữa / EI_biên. Cảm biến ở nhịp biên cho cùng dạng công thức như dầm 2 nhịp, với μ = 2(ρ + β³)/(2ρ + 3β).
- EI không đổi, cảm biến giữa nhịp biên: **β_crit = 1,700594** (nghiệm 6β³ − 15β − 4 = 0, dạng lượng giác chính xác).
- Dải gần mù |N| < 0,2: β = 1,621399–1,775021. Với dầm 2 nhịp: ρ_L = 1,385–1,525.
- β = 2cos(π/9) = 1,8794 là điểm kết thúc vết mù trên nhịp biên. Vượt qua đó C_m âm nhưng **vẫn quan sát được** (|C_m| mới là đại lượng quyết định).

### 3.3. Cầu Mây (WP3; `docs/wp3_continuous_bridges.md`; `code/analysis/logs/wp3_run.log`)

Hai cách hiệu chỉnh đều khớp số đo; hai số đọc tĩnh không tách được độ cứng dầm và độ cứng trụ:

| Cách | EI_hd / EI_tk | Sai lệch so với số đo | N8 (0,4L nhịp biên) | N7 (giữa nhịp chính) |
|---|---|---|---|---|
| A: độ cứng trụ khớp FE của báo cáo | 1,088 | −4,6 / +5,0 % | 0,181 (triệt tiêu 82%) | 0,209 |
| B: khớp trực tiếp hai số đo | 0,716 | ±2,9 % | 0,476 (triệt tiêu 44%) | 0,234 |

Hệ quả viết trong bài: điểm đo nhịp biên bị điều kiện hoá kém theo độ cứng trụ. C_m phải lấy từ mô hình nhận dạng tại chỗ hoặc dùng SLM, không lấy từ mô hình thiết kế.

**Tải tương đương của độ lệch zero** (`code/analysis/logs/wp7b_peps.log`): với xe 25 t và ε0 = 0,05 mm, sai số tải là 93% (A) hoặc 36% (B) ở nhịp biên, và 11% (A) hoặc 10% (B) ở nhịp chính.

### 3.4. Bản ghi động (WP4; `docs/wp4_dynamic_records.md`)

- Không kiểm được tải tuyệt đối: hệ số xử lý khác nhau theo nhịp, có chỉnh tay, vận tốc Gie Cục không khớp báo cáo.
- Trôi nền: chọn đường nền khác nhau làm tích phân lệch tới 6% trong một lượt xe, và 7–60% trên bản ghi 15 s.
- Lọc thông cao phá huỷ tích phân; lọc thông thấp dưới 2 Hz giữ nguyên tích phân (tỉ số 0,9999–1,001).

### 3.5. Tính mới (WP1; `docs/novelty_matrix.md`)

Ý tưởng "tích phân phản ứng × diện tích ảnh hưởng" đã có cho biến dạng (Ojio & Yamada 2002 và các bài 2021–2024). Đóng góp còn đứng được: nghiệm kín cho dầm liên tục, vết mù, chỉ số quan sát được và vị trí tối ưu, ngân sách sai số do trôi zero chi phối. Không tìm thấy bài "Integral Mean of Strain" 2025, nên không trích.

### 3.6. So sánh bản SCHM với bản đã nộp JCSHM

| Mặt | Thay đổi |
|---|---|
| Phạm vi, tỷ lệ | Thêm áp dụng trên cầu liên tục thật (mạnh hơn rõ) |
| Lý thuyết | Thêm nghiệm kín 3 nhịp (mạnh hơn) |
| Định vị | Ghi công Ojio–Yamada, nêu rõ phần mới (mạnh hơn nhiều) |
| Độ chặt chẽ | Sửa lỗi số thập phân, bỏ các tuyên bố quá mức, ngân sách sai số thống nhất, 491 con số truy được nguồn, 47 tài liệu đã kiểm DOI |
| Độ dài | Khoảng 16.000 từ → 9.221 từ |
| **Còn yếu** | **Chưa kiểm chứng cân tải bằng tích phân trên cầu liên tục** (không có bản ghi lượt xe chạy); thí nghiệm không kiểm trực tiếp tính bất biến |

Ước lượng chủ quan của hội đồng phản biện mô phỏng: khả năng qua vòng đọc bàn ở SCHM khoảng 35% với bản cũ, khoảng 60% với bản hiện tại.

---

## 4. Bản đồ file

| Cần gì | Mở file |
|---|---|
| Bản nộp SCHM | `manuscript/schm/manuscript.md`, `cover_letter_SCHM.md`, `figures/` |
| Yêu cầu tạp chí, danh mục kiểm tra trước khi nộp | `manuscript/schm/schm_requirements.md`, `submission_checklist.md` |
| Việc tác giả phải điền | `manuscript/schm/open_items.md` (8 chỗ [NEED VALUE]) |
| Nguồn của từng con số | `manuscript/schm/traceability.md` |
| Phản hồi 32 vấn đề phản biện đỏ | `manuscript/schm/response_to_red_team.md`, `docs/wp8_red_team_report.md` |
| Bảng câu hỏi gửi người lập báo cáo | `docs/word/Cau_hoi_bo_sung_so_lieu.docx` (script tạo: `docs/word/make_questions.js`) |
| Thư xin số liệu (bản ngắn) | `docs/03_thu_xin_so_lieu.md` |
| Cách chia file lớn để chuyển qua Drive | `docs/06_huong_dan_chia_file_len_drive.md` |
| Các bản trước | `manuscript/structures/` (v1), `manuscript/v2/`, `manuscript/text/` (bản đã nộp và các báo cáo phản biện cũ) |
| Mã gốc của tác giả | `code/original/files-v2/` (bản sớm) |
| Script phân tích | `code/analysis/` (xem README) |

---

## 5. Khi có câu trả lời: việc cần làm theo từng câu hỏi

Mã câu hỏi theo file Word.

| Câu trả lời | Việc phải làm | File, script liên quan |
|---|---|---|
| **A1** số đọc 3 lần lặp | Tính độ không đảm bảo loại A; sửa mục 3 và Bảng 10 | `code/analysis/wp7b_peps.py` (Part D), `manuscript/schm/manuscript.md` |
| **A2** cấp chính xác quả cân | Điền [NEED VALUE] mục 7.2; cập nhật ngân sách sai số | như trên |
| **A3** thứ tự tải 3 trục | Xác nhận; nếu khác giả thiết hiện tại thì chạy lại bảng tải | `wp7b_peps.py` (Part C) |
| **A4** file hình gốc | Đặt vào `manuscript/schm/figures/` (Fig. 1, 2, 4, 5, 6, 10) | `figure_table_plan.md` |
| **A5** trùng với bài ở Structures | Nếu trùng: trích dẫn hoặc nêu trong thư gửi biên tập | `cover_letter_SCHM.md` |
| **A9** script bổ sung | Ghép các phần (theo hướng dẫn 06), đưa vào `code/original/`; chạy lại, đối chiếu số | – |
| **B1–B3** MIDAS, kích thước trụ, số đọc ở nhịp không tải | Hiệu chỉnh lại độ cứng trụ; chốt N8 (A hay B, hay giá trị mới); viết lại mục 4 | `code/analysis/wp3_*.py`, `logs/wp3_run.log` |
| **B4** phiếu cân | Thay 25 t danh nghĩa; tính lại Bảng 6, 8 | `wp7b_peps.py`, `wp3_run.py` |
| **B7 / C5** file thô lượt xe chạy | **Quan trọng nhất:** kiểm cân tải bằng tích phân trên cầu liên tục. Dùng quy trình WP4 (tách sự kiện, đường nền, lọc), rồi so ∫y với P·C_m | `code/analysis/wp4_dynamic_records.py` |
| **B8, C6, D6** quyền công bố | Điền mục Data Availability, Acknowledgments | `manuscript.md` |
| **B9** xung đột lợi ích | Điền mục Conflicts of Interest | `manuscript.md` |
| **C1–C3** bản vẽ, số đọc Thái Bình | Dựng lại mô hình; nếu khớp FE của báo cáo trong ±5% thì thêm Thái Bình làm cầu thứ hai (β = 1,5, dưới ngưỡng; đối chứng với Cầu Mây β = 1,636) | `wp3_sections.py`, `wp3_run.py` |
| **D1–D4** kênh võng Gie Cục, Phương Độ | Nếu xác nhận hiệu chuẩn và có trọng lượng, vận tốc xe: thử kiểm tải tuyệt đối trên dầm giản đơn | `wp4_dynamic_records.py` |

**Sau mỗi lượt cập nhật:**
1. Chạy lại script liên quan; log lưu vào `code/analysis/logs/`.
2. Cập nhật `traceability.md`.
3. Chạy `python3 code/analysis/wp7b_checks.py manuscript/schm` để đếm từ và kiểm [NEED VALUE].
4. Nếu đổi kết luận chính, chạy lại phản biện đỏ (Opus) và kiểm số/DOI (Haiku) trước khi nộp.

---

## 6. Phân vai tác nhân đã dùng (để chạy lại)

| Vai | Model | Dùng cho |
|---|---|---|
| Điều phối | Opus | Chia việc, kiểm lại kết quả quan trọng trong log trước khi chấp nhận |
| Kiểm kê dữ liệu, tìm tài liệu, xử lý tín hiệu | Sonnet | Đọc Drive, tổng quan, xử lý bản ghi |
| Lý thuyết, mô hình cầu, viết và sửa bài, phản biện đỏ | Opus (viết bài dùng skill `viet-tu-nhien`) | WP2, WP3, WP7, WP8 |
| Kiểm số, tham chiếu chéo, DOI | Haiku | WP8 |

Quy tắc chung: không tự điền số; thiếu thì ghi [NEED VALUE]; mọi con số phải truy được tới file trong repo; câu khai báo dùng AI giữ nguyên văn của tác giả.

---

## 7. Giới hạn kỹ thuật cần nhớ

- Kết nối Google Drive chỉ tải được file khoảng ≤ 2,4 MB (6,6 MB đã lỗi). File lớn phải chia phần 2 MB bằng 7-Zip (`docs/06_huong_dan_chia_file_len_drive.md`).
- Máy chủ không giải nén được rar. Có sẵn Git LFS nhưng chưa thử đẩy lên GitHub.
- Các trang Wiley/Elsevier hay trả lỗi 403. Thông tin tạp chí lấy qua nguồn trung gian, nên kiểm lại trên trang chính thức khi nộp.
