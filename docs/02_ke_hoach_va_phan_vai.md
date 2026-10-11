# Kế hoạch làm lại bài Paper1-1D và phân vai tác nhân

## 0. Chẩn đoán

| Lần nộp | Kết quả | Lý do |
|---|---|---|
| Engineering Structures | Từ chối tại bàn biên tập | Chưa có thư trong repo [NEED VALUE]; nhiều khả năng cùng lý do dưới đây |
| JCSHM, CSHM-D-26-00881 | Từ chối | Tổng biên tập: phạm vi tạp chí là SHM công trình thật, hoặc mô hình thí nghiệm có tỷ lệ đủ để suy ra công trình (`docs/decision_letter_JCSHM.md`) |

Lý thuyết không bị chê. Vấn đề là **bằng chứng thực nghiệm chỉ có ống thép 25 × 25 × 2 mm, nhịp 2 × 2,5 m, tải treo tĩnh**. Ngoài ra còn rủi ro trùng ý tưởng với nhánh BWIM dùng "diện tích đường ảnh hưởng" và chỉ số *Integral Mean of Strain* (Measurement, 2025) mà phản biện nội bộ đã nêu. Bài phải trích dẫn và phân biệt rõ.

Hồ sơ chẩn đoán trên Drive (`docs/rejection_evidence.md`) còn nêu thêm các điểm yếu phải sửa ở mọi lộ trình:
- **Tính mới:** định lý bất biến có thể bị coi là hệ quả sơ cấp của tích chập Moses (1979) và của khái niệm diện tích đường ảnh hưởng. Đóng góp phải đặt vào phần mà cầu giản đơn không có: vết mù, chỉ số quan sát được, vị trí tối ưu dạng nghiệm kín, áp dụng cho cầu liên tục thật.
- **Thí nghiệm:** tải treo tĩnh nên bất biến chưa được kiểm trực tiếp (cùng tổng tải, đổi khoảng cách trục).
- **Độ dài:** khoảng 16–17 nghìn từ, cần rút về 8–9 nghìn.
- **Tài liệu tham khảo:** nghi một tài liệu không có thật (Qiu 2025). Phải kiểm từng DOI.
- **Nhịp nộp bài:** 9 lần nộp trong 9 ngày; nên dừng nộp cho tới khi có bằng chứng mới.
- Thư xin bài gửi ES tự nhận "no field data are reported".

**Mục tiêu bản mới:** giữ khung lý thuyết (định lý bất biến, Maxwell–Betti, nghiệm kín, cấu hình mù, chỉ số quan sát được). Bổ sung ba lớp bằng chứng: (i) dữ liệu kiểm định có sẵn của cầu thật; (ii) mở rộng lý thuyết sang cầu liên tục 3 nhịp, dạng phổ biến nhất ở Việt Nam; (iii) một đợt đo hiện trường hoặc mô hình lớn có tỷ lệ đủ để suy ra công trình.

## 1. Hai lộ trình

| | Lộ trình A: chỉ dùng dữ liệu có sẵn | Lộ trình B: A + đợt đo mới (khuyến nghị) |
|---|---|---|
| Bằng chứng | Bản đồ quan sát được trên Cầu Mây và Thái Bình (EI thực); hiệu chỉnh EI từ thử tải tĩnh; tích phân trên bản ghi động thật (Gie Cục, Phương Độ) | Thêm lượt xe chạy chậm trên 1 cầu liên tục 2–3 nhịp, 2 xe cân trước, cảm biến tại vị trí tối ưu và vị trí gần mù |
| Tạp chí phù hợp | *Structures* (Elsevier), *Measurement*, *Applied Sciences / Sensors* | *JCSHM* (nộp mới), *Structural Control and Health Monitoring*, *J. Bridge Engineering (ASCE)*, *Engineering Structures* |
| Thời gian | 4–6 tuần | 3–5 tháng (phụ thuộc cấp phép đo) |
| Rủi ro | Vẫn có thể bị chê thiếu kiểm chứng trực tiếp trên cầu liên tục | Chi phí, phối hợp đơn vị quản lý cầu |

Khuyến nghị: làm A ngay (đó cũng là phần chuẩn bị của B), đồng thời xin phép đo cho B. Chỉ nộp lại JCSHM khi có B.

## 2. Gói công việc (WP)

| WP | Nội dung | Đầu ra | Phụ thuộc |
|---|---|---|---|
| WP0 | Lưu trữ: thu thập file thô, MIDAS, bản vẽ; xin số liệu thiếu (danh sách ở `docs/01_danh_gia_du_lieu_cau.md` §3) | `data/raw/…`, thư xin số liệu | — |
| WP1 | Tổng quan và kiểm tra tính mới: influence-area BWIM, IMS 2025, nhận dạng tổng tải bằng diện tích; bảng so sánh | `docs/novelty_matrix.md`, danh mục tham khảo cập nhật | — |
| WP2 | Mở rộng lý thuyết: nghiệm kín C_m cho dầm liên tục 3 nhịp đối xứng (tỉ số nhịp biên/nhịp chính); vết mù; vị trí tối ưu; có EI(x) | Mục 2.3 mới, `code/analysis/cm_multispan.py` mở rộng, kiểm tra ký hiệu bằng SymPy | — |
| WP3 | Cầu Mây và Thái Bình: C_m với EI(x) thực, bản đồ quan sát được; hiệu chỉnh EI từ thử tải tĩnh; kiểm tra tuyến tính 4/6/10 xe | Mục "Field case studies", 2–3 hình, 2 bảng | WP0, WP2 |
| WP4 | Bản ghi động Gie Cục, Phương Độ: tách sự kiện, khử trôi nền, đổi thời gian sang quãng đường, tích phân, so với P·C_m; độ lặp giữa các nhịp; trôi nền thật cho mục 4.2 | Notebook, hình, bảng sai số | WP0 (trọng lượng xe, vận tốc) |
| WP5 | Thiết kế và thực hiện đợt đo mới (lộ trình B): chọn cầu liên tục 2–3 nhịp; LVDT hoặc camera hoặc laser; 2 xe cấu hình trục khác nhau, cân trước; ≥ 5 lượt chạy chậm mỗi xe; dừng tĩnh mỗi L/10; một kênh tại vị trí gần mù | Đề cương đo, dữ liệu, phân tích | WP2, WP3 |
| WP6 | (Tuỳ chọn) Thí nghiệm bổ sung trên mô hình hiện có: thay đổi khoảng cách trục với tổng tải cố định; dời gối để có nhịp 2500/3644 mm (thí nghiệm mù) | Bảng thí nghiệm mới | — |
| WP7 | Viết lại bài: cấu trúc mới, tóm tắt, mở đầu nhấn vào giám sát công trình thật; thư gửi biên tập | Bản thảo mới `manuscript/` | WP1–WP5 |
| WP8 | Phản biện đỏ: mô phỏng biên tập viên đọc bàn và 3 phản biện; kiểm tra số liệu, DOI, định dạng | Báo cáo phản biện, danh sách sửa | WP7 |

## 3. Phân vai tác nhân và model

| Vai | Model | Việc chính | Công cụ |
|---|---|---|---|
| **Điều phối (Orchestrator)** | Opus 5.5 (phiên này) | Chia việc, nghiệm thu từng WP, quyết định lộ trình, ghép bản thảo | Agent, GitHub |
| **Lưu trữ dữ liệu (Data Archivist)** | Sonnet 5.5 | WP0: kiểm kê Drive, trích bảng số, ghi nguồn từng con số; soạn thư xin số liệu | Google Drive |
| **Tìm kiếm tài liệu (Literature Scout)** | Sonnet 5.5 | WP1: tìm và đọc tài liệu, lập ma trận tính mới, xác minh DOI | Elicit, alphaXiv, Firecrawl |
| **Cơ học kết cấu (Structural Theorist)** | Opus 5.5 | WP2: dẫn nghiệm kín 3 nhịp, chứng minh, kiểm bằng SymPy và FE | Python, SymPy |
| **Mô hình hoá cầu (Bridge Modeller)** | Opus 5.5 | WP3: EI(x) từ MIDAS hoặc bản vẽ, C_m thực, so với thử tải | Python, OpenSeesPy |
| **Xử lý tín hiệu (Signal Analyst)** | Sonnet 5.5 | WP4: khử trôi, tách sự kiện, tích phân, Monte Carlo sai số | Python, SciPy |
| **Thiết kế đợt đo (Field-test Designer)** | Opus 5.5 | WP5, WP6: đề cương đo, bố trí cảm biến theo C_m, kịch bản xe | Python |
| **Viết bài (Writer)** | Opus 5.5 + skill `viet-tu-nhien` | WP7: viết lại tiếng Anh học thuật; chỉ dùng số đã nghiệm thu, chỗ thiếu ghi [NEED VALUE] | Skill viet-tu-nhien |
| **Hội đồng phản biện (Red Team)** | Opus 5.5 × 3 vai (biên tập viên đọc bàn, chuyên gia BWIM, chuyên gia đo hiện trường) | WP8: chấm như vòng đọc bàn của tạp chí đích | — |
| **Kiểm tra (Verifier)** | Haiku 5.5 | Đối chiếu mọi số trong bài với log và script, kiểm DOI, định dạng tạp chí, đánh số hình/bảng | Python, Grep |

Quy tắc chung:
- Mỗi con số trong bài phải truy được tới một file trong `data/` hoặc một log trong `code/`.
- Tác nhân không tự điền số. Thiếu thì ghi [NEED VALUE] và đưa vào danh sách hỏi tác giả.
- Khai báo dùng AI giữ đúng câu tác giả đã dùng.

## 4. Tiến độ và mốc nghiệm thu

| Tuần | Việc | Mốc |
|---|---|---|
| 1 | WP0, WP1, WP2 song song | Có ma trận tính mới; nghiệm kín 3 nhịp kiểm bằng FE tới 1e-9 |
| 2–3 | WP3, WP4 | Bản đồ quan sát được cho Cầu Mây và Thái Bình với EI(x) thực; bảng tích phân trên bản ghi động |
| 3 | Quyết định lộ trình | Nếu có số liệu thô hoặc được phép đo: sang B. Nếu không: viết A |
| 4–6 | WP7, WP8 (lộ trình A) | Bản thảo A đạt ≥ 8/10 ở vòng đọc bàn mô phỏng |
| 6–18 | WP5 (lộ trình B), cập nhật WP7, WP8 | Bản thảo B nộp tạp chí SHM |

## 5. Quyết định của tác giả (2026-10-11)

1. **Engineering Structures (ENGSTRUCT-D-26-08490):** từ chối tại bàn, chỉ nêu không phù hợp phạm vi tạp chí.
2. **Số liệu thô, mô hình MIDAS:** tác giả sẽ hỏi người lập báo cáo kiểm định. Thư xin số liệu: `docs/03_thu_xin_so_lieu.md`.
3. **Đo bổ sung trên cầu liên tục:** không có. Bỏ WP5. WP6 (thí nghiệm bổ sung trên mô hình hiện có) để tuỳ chọn.
4. **Lộ trình: A**, chỉ dùng dữ liệu có sẵn, 4–6 tuần, đích *Structures* hoặc *Measurement*.

### Hệ quả cho lộ trình A
- Bài không được tự nhận là "kiểm chứng hiện trường" trên cầu liên tục. Phần cầu thật được viết là **ứng dụng tiêu chí quan sát được và kiểm tra nhất quán trên dữ liệu kiểm định có sẵn**.
- Chọn tạp chí sau WP1:
  - *Structures*: phạm vi kết cấu rộng, chấp nhận lý thuyết + thí nghiệm + nghiên cứu điển hình. Đây là lựa chọn mặc định.
  - *Measurement*: hợp nếu bài xoay trục sang quan sát được, ngân sách sai số và bố trí cảm biến. Nhưng bài IMS 2025 cũng đăng ở đây, nên phải phân biệt thật rõ.
- Gói chạy ngay: WP1 (tài liệu, tính mới, kiểm DOI), WP2 (nghiệm kín 3 nhịp), WP3 (Cầu Mây, Thái Bình với EI(x) lấy từ thuyết minh thiết kế nếu đọc được), WP4 (bản ghi động Gie Cục, Phương Độ). Phần nào thiếu metadata thì ghi rõ giả thiết và chờ số liệu tác giả xin về.

## 6. Quyết định bổ sung (2026-10-11, sau WP1–WP4)
- Không làm thêm thí nghiệm. Bỏ WP6.
- Dàn ý trong `docs/04_tong_hop_ket_qua_lo_trinh_A.md` §2 đã được duyệt. Bắt đầu WP7 (viết bản thảo cho *Structures*), sau đó WP8 (phản biện đỏ và kiểm tra).
- Thái Bình không đưa vào phân tích chính vì mô hình chưa khớp; chỉ nêu ở phần hạn chế và hướng tiếp theo.
