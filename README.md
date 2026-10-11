# SHM Paper 1 – 1D: Load observability of continuous bridge beams from a single deflection channel

Kho làm việc để làm lại bài báo về xác định tổng tải xe từ tích phân độ võng đo tại một điểm trên dầm liên tục.
Tác giả: Quoc-Bao Nguyen, Thai-Son Vu (liên hệ), Hung-Son Nguyen – Bộ môn Cầu – Đường, ĐH Xây dựng Hà Nội.

## Lịch sử nộp bài

| Tạp chí | Mã | Kết quả |
|---|---|---|
| Engineering Structures | ENGSTRUCT-D-26-08490 | Từ chối tại bàn: không phù hợp phạm vi |
| J. Civil Structural Health Monitoring | CSHM-D-26-00881 | Từ chối: phạm vi chỉ gồm công trình thật hoặc mô hình có tỷ lệ đủ suy ra công trình (`docs/decision_letter_JCSHM.md`) |
| **Structural Control and Health Monitoring** | – | **Đích hiện tại.** Gói nộp ở `manuscript/schm/` |

Trạng thái chi tiết và việc còn lại: **`docs/05_trang_thai_va_viec_tiep_theo.md`**.

## Cấu trúc kho

### `manuscript/`
| Thư mục | Nội dung |
|---|---|
| `text/` | Văn bản trích từ các bản đã nộp (ES, JCSHM, JMES), thư xin bài, các báo cáo phản biện và chẩn đoán nội bộ |
| `structures/` | v1: bản viết lại đầu tiên (khuôn Elsevier *Structures*), giữ để đối chiếu |
| `v2/` | v2: sau phản biện đỏ; trung tính về tạp chí; thư gửi SCHM và SIE |
| **`schm/`** | **Bản nộp SCHM**: `manuscript.md`, `cover_letter_SCHM.md`, `figures/`, `schm_requirements.md` (yêu cầu tạp chí), `submission_checklist.md`, `open_items.md` (việc tác giả cần làm), `traceability.md` (nguồn của từng con số), `figure_table_plan.md`, `response_to_red_team.md` |

### `docs/` (theo thứ tự đọc)
| File | Nội dung |
|---|---|
| `decision_letter_JCSHM.md`, `rejection_evidence.md` | Thư từ chối và chẩn đoán lý do |
| `01_danh_gia_du_lieu_cau.md` | Đánh giá dữ liệu thử tải 5 cầu |
| `02_ke_hoach_va_phan_vai.md` | Kế hoạch, gói công việc, phân vai tác nhân/model, các quyết định của tác giả (§5–7) |
| `03_thu_xin_so_lieu.md` | Thư xin số liệu thô gửi người lập báo cáo kiểm định |
| `04_tong_hop_ket_qua_lo_trinh_A.md` | Tổng hợp WP1–WP4 và dàn ý đã duyệt |
| `05_trang_thai_va_viec_tiep_theo.md` | Trạng thái hiện tại, việc còn lại |
| `novelty_matrix.md`, `reference_check.md` | WP1: tổng quan tính mới, kiểm tra DOI, chọn tạp chí |
| `wp2_three_span_theory.md` | WP2: nghiệm kín dầm liên tục 3 nhịp |
| `wp3_continuous_bridges.md` | WP3: Cầu Mây và Thái Bình |
| `wp4_dynamic_records.md` | WP4: bản ghi động Gie Cục I, Phương Độ |
| `wp8_red_team_report.md`, `wp8_verification_report.md` | WP8: phản biện đỏ 3 vai và kiểm tra số liệu/DOI |
| `drive_inventory_paper.md` | Danh mục file bài báo trên Google Drive (kèm ID) |

### `data/bridges/<cầu>/`
`INVENTORY.md` (danh mục file trên Drive kèm ID, phát hiện chính) và các bảng CSV trích từ báo cáo kiểm định:
`cau-may` (liên tục 55+90+55 m), `lang-am` (cầu Thái Bình, liên tục 42+63+42 m), `gie-cuc-1`, `phuong-do`, `song-sat` (giản đơn).

### `code/analysis/`
| Script | Việc | Log |
|---|---|---|
| `cm_multispan.py` | C_m cho dầm liên tục nhiều nhịp, EI thay đổi (phần tử không lăng trụ chính xác) | `logs/cm_multispan.log` |
| `cm_3span_theory.py`, `verify_3span.py` | Nghiệm kín 3 nhịp (SymPy) và kiểm bằng FE (sai lệch < 1e-8) | `logs/cm_3span_theory.log`, `logs/verify_3span.log` |
| `wp3_sections.py`, `wp3_fe.py`, `wp3_run.py` | Tiết diện, mô hình và hiệu chỉnh Cầu Mây, Thái Bình | `logs/wp3_run.log`, `results/` |
| `wp4_dynamic_records.py` | Xử lý bản ghi động (tách sự kiện, đường nền, lọc) | `logs/wp4.log` |
| `wp7b_peps.py` | Tải tương đương của độ lệch zero, ngân sách sai số | `logs/wp7b_peps.log` |
| `wp7b_checks.py` | Đếm từ, kiểm [NEED VALUE], tham chiếu chéo | – |
| `schm_figures.py` | Vẽ hình cho bản SCHM | `manuscript/schm/figures/schm_figures_values.txt` |

Chạy: `python3 code/analysis/<script>.py` (cần numpy, scipy, sympy, matplotlib).

### `figures/`
Hình làm việc từ WP2–WP4. Hình bản nộp ở `manuscript/schm/figures/`.

## Quy tắc
- Mọi con số trong bài phải truy được tới một file trong `data/`, một log trong `code/analysis/logs/` hoặc bản thảo gốc (`traceability.md`).
- Không tự điền số. Thiếu thì ghi `[NEED VALUE]`.
- Dữ liệu gốc lớn (zip, rar, dwg, MIDAS, ảnh) vẫn ở Google Drive; ID ghi trong các `INVENTORY.md` và `docs/drive_inventory_paper.md`.
