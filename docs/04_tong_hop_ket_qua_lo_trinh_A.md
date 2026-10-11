# Tổng hợp kết quả WP1–WP4 và dàn ý bài mới (lộ trình A)

Ngày: 2026-10-11. Chi tiết: `docs/novelty_matrix.md`, `docs/reference_check.md`, `docs/wp2_three_span_theory.md`, `docs/wp3_continuous_bridges.md`, `docs/wp4_dynamic_records.md`.

## 1. Kết quả chính

### WP1. Tính mới và tạp chí
- Ý tưởng "tích phân phản ứng = tổng trọng lượng × diện tích đường ảnh hưởng" **đã có** cho biến dạng (Ojio & Yamada 2002; Yang 2021, 2023; Zhu 2022; Agüero-Barrantes 2023; Shi 2024). Định lý bất biến chỉ còn là nền móng, không phải đóng góp chính.
- Đóng góp còn đứng được: nghiệm kín cho dầm liên tục, vết mù C_m = 0, chỉ số quan sát được |C_m| với vị trí cảm biến tối ưu, và ngân sách sai số do trôi zero chi phối.
- Không tìm thấy bài "Integral Mean of Strain" (Measurement 2025). Chỉ trích dẫn khi có DOI.
- 31 DOI đều tồn tại. Cần sửa tài liệu [9], [10], [33]. Qiu 2025 đã được bỏ khỏi bản JCSHM, đúng.
- **Tạp chí: *Structures* (Elsevier).** Bài nghiên cứu khoảng 20 trang giãn dòng đôi, cần Highlights, CRediT và tuyên bố dữ liệu.

### WP2. Lý thuyết dầm liên tục 3 nhịp (kiểm bằng FE, sai lệch < 1e-8, 0 lỗi)
- Dầm đối xứng, β = L_giữa/L_biên, ρ = EI_giữa/EI_biên. Cảm biến ở nhịp biên cho cùng dạng Eq. (11a), với μ = 2(ρ + β³)/(2ρ + 3β).
- Vết mù có cùng điều kiện như dầm 2 nhịp: μ_crit = 2(1 + ξ − ξ²)/(1 + ξ).
- EI không đổi, cảm biến giữa nhịp biên: β_crit là nghiệm của 6β³ − 15β − 4 = 0, **β_crit = 1,700594** (dạng lượng giác chính xác). Ngưỡng gần mù 0,2 đạt tại β = 1,6214. Từ β = 2cos(π/9) = 1,8794 trở lên, không vị trí nào trên nhịp biên quan sát được.
- Cầu Mây có β = 90/55 = 1,636, tức đã qua ngưỡng gần mù.

### WP3. Hai cầu liên tục thật
- Cầu Mây: I = 5,482 m⁴ ở giữa nhịp và 59,612 m⁴ ở mặt trụ (báo cáo đánh giá của đơn vị thiết kế, tr. 5). Mô hình hiệu chỉnh độ cứng trụ khớp FE của báo cáo trong ±4%.
- Chỉ số tại điểm đo thật N8 (0,4L nhịp biên): **0,18** (dải 0,02 khi trụ là khớp, 0,45 khi trụ ngàm). Phần âm triệt tiêu 82% phần dương.
- **C_m tại điểm này thay đổi khoảng 14 lần giữa hai điều kiện trụ.** Đây là minh hoạ cầu thật cho lập luận "|C_m| là chỉ số điều kiện": ở điểm gần mù, C_m lấy từ mô hình thiết kế (BPM) không dùng được, chỉ SLM dùng được.
- Đo/FE: 0,92–0,94 (Cầu Mây) và 0,90–0,97 (Thái Bình). Cầu cứng hơn mô hình 4–11%, nên BPM dùng EI thiết kế sẽ đánh giá thấp tải khoảng chừng đó; SLM khử sai lệch này.
- Thái Bình chưa tin cậy được: mô hình 2D không tái tạo được FE của báo cáo (lệch −11/+22/−12%), thiếu chiều dày bản đáy và kích thước trụ.
- Không kiểm được tính tuyến tính theo số xe: không nhịp nào được xếp nhiều cỡ đoàn xe.
- Ngưỡng 0,2 cần định nghĩa lại cho dầm thay đổi tiết diện. Đề xuất bổ sung tỉ số triệt tiêu C_m/A⁺ (diện tích ròng chia diện tích dương), không phụ thuộc EI tham chiếu.

### WP4. Bản ghi động (Gie Cục I, Phương Độ, dầm giản đơn)
- **Không dùng để kiểm trọng lượng tuyệt đối được.** Chuỗi "đã xử lý" bị nhân hệ số khác nhau theo nhịp (Gie Cục 1,00 / 3,25 / 5,15; Phương Độ 0,67 / 1,34) và có chỉnh tay. Vận tốc suy từ bản ghi Gie Cục là 47–62 km/h, khác 30–40 km/h ghi trong báo cáo.
- Dùng được cho hai điểm của bài:
  1. **Trôi đường nền.** Trong cửa sổ một lượt xe (2–4 s), cách chọn đường nền làm tích phân lệch tới 6%. Trên cả bản ghi 15 s, lệch 7–60%, có bản ghi đổi dấu. Kết quả khớp công thức sai lệch ε0·T/∫y. Đây là bằng chứng thật cho khuyến nghị "chặn sát lượt xe và đặt lại zero trước và sau mỗi lượt".
  2. **Lọc tín hiệu.** Lọc thông cao phá huỷ tích phân (−44 đến −100%). Lọc thông thấp dưới 2 Hz giữ nguyên tích phân (tỉ số 0,9999–1,001). Phần động có tích phân ròng chỉ bằng 0,1–2% tích phân trị tuyệt đối của nó, phù hợp mục 4.6.

## 2. Dàn ý đề xuất cho bản *Structures* (mục tiêu 8–9 nghìn từ)

Tên tạm: *Load observability of continuous girder bridges from a single deflection channel: closed-form blind configurations, laboratory verification and application to in-service bridges*

1. **Introduction** (rút gọn). Đặt định lý trong dòng influence-area BWIM (Ojio & Yamada, Yang, Zhu, Agüero-Barrantes…). Câu hỏi mới: trên cầu liên tục, điểm đo nào quan sát được tổng tải.
2. **Theory.** 2.1 Bất biến và Maxwell–Betti (ngắn, nêu là kết quả đã biết dưới dạng tổng quát). 2.2 Dầm 2 nhịp: nghiệm kín, vết mù, ξ*. 2.3 **Dầm 3 nhịp: nghiệm kín mới, β_crit = 1,7006, vùng không quan sát được β ≥ 1,8794.** 2.4 Chỉ số quan sát được: |C_m| và tỉ số triệt tiêu C_m/A⁺; liên hệ với độ nhạy sai số.
3. **Laboratory verification** (giữ, rút gọn). Ghi rõ là kiểm chứng mô hình và thuật toán, không phải bằng chứng tỷ lệ công trình.
4. **Application to two in-service continuous box-girder bridges** (WP3). Bản đồ quan sát được tại điểm đo thật. Độ nhạy C_m theo điều kiện trụ (gấp 14 lần ở điểm gần mù). Đo/FE và hệ quả cho BPM so với SLM.
5. **Field deflection records: baseline drift and filtering** (WP4, ngắn, nói rõ giới hạn dữ liệu).
6. **Error budget and dynamic validity** (gộp mục 4 cũ, rút còn khoảng một nửa).
7. **Recommendations for sensor placement.** Quy trình từng bước: tính C_m, kiểm vết mù, chọn vị trí, chọn SLM khi gần mù.
8. **Conclusions.**

Phần bỏ hoặc chuyển sang phụ lục: chứng minh dài, bảng Monte Carlo chi tiết, mục "extensions", phần lặp giữa các mục.

## 3. Việc còn lại

| Việc | Ai | Trạng thái |
|---|---|---|
| Gửi thư xin số liệu (`docs/03_thu_xin_so_lieu.md`) | Tác giả | Chờ |
| Khi có MIDAS hoặc bản vẽ: tính lại Cầu Mây với điều kiện trụ thật; dựng lại Thái Bình | Bridge Modeller (Opus) | Chờ số liệu |
| Đọc toàn văn các bài mới gần nhất (Chaudhary 2025, Zhou 2025, Zhang 2026, Dan 2026) trước khi trích | Literature Scout (Sonnet) | Cần làm |
| Viết bản thảo theo dàn ý trên | Writer (Opus + viet-tu-nhien) | Chờ tác giả duyệt dàn ý |
| Phản biện đỏ ba vai, kiểm số và DOI | Red Team (Opus), Verifier (Haiku) | Sau bản thảo |
