# Tổng hợp 4 biên tập viên đọc bản v3 (2026-10-18), so với lần đọc bản SCHM v2

| Biên tập viên | Lần 1 (v2/SCHM) | Lần 2 (v3) |
|---|---|---|
| 1. Tổng biên tập | Gửi phản biện có điều kiện; phù hợp 7, chất lượng 6 | Gửi phản biện có điều kiện; **phù hợp 8**, chất lượng 6; dự kiến sửa lớn |
| 2. BWIM | **Trả lại trước phản biện**; tính mới 4, kỹ thuật 6 | **Sửa lớn**; **tính mới 5**, kỹ thuật 6 |
| 3. Cơ học | Sửa lớn; kỹ thuật 7 (lý thuyết 9, lab 7, cầu 5), rõ 7 | Sửa lớn; kỹ thuật 7 (lý thuyết 8, lab 6, hiện trường 5, **cầu 7**), rõ 7; "không cần thí nghiệm mới" |
| 4. Hiện trường | Sửa lớn; bằng chứng 4, tái lập 6 | Sửa lớn; **bằng chứng 5, tái lập 7** |

Không ai còn đề nghị trả lại trước phản biện. Tất cả xác nhận lý thuyết và các con số chính tái lập được từ log.

## Vấn đề chung ở v3
1. **Tính mới bị nói quá** (BT1, BT2, BT3): "định lý" tích phân và ước lượng GLS/tổng trọng số bằng 0 là kinh điển. Phần được công nhận là mới: danh mục vết mù (nhất là vành mù của strain gauge), chỉ số N_M và R, quy tắc đặt cảm biến, phân tích nhận dạng (luật Möbius). Phải đổi cách tuyên bố đóng góp.
2. **Báo cáo NOR-BWIM chọn lọc** (BT2, BT3, BT4):
   - Ngày 1 trọng lượng do tài xế khai, không cân; biến động chỉ ±4% nên đoán bằng trung bình đã cho ~2%. Ngày 2 (có cân) sai số 17,8%.
   - Ngày 1 chỉ dùng 4/12 kênh; 4 kênh khác không đạt bất biến (p ≤ 0,012), xe và vận tốc bị trộn lẫn.
   - "Không phụ thuộc vận tốc" là nói quá; 0,999 ± 0,140 không loại được chênh 25%.
3. **Bộ ước lượng miễn nhiễm chưa thử trên dữ liệu thật** (BT2, BT4): BT4 chạy lại thấy nhiễu khi không có xe ở 4 kênh ngày 2 tương quan rất cao (r = 0,83–0,96); GLS với hiệp phương sai đo được giảm sai số mỗi lượt từ ~25% xuống ~16%. → Làm được ngay, và là bằng chứng thật cho gói 1B.
4. **Lỗi kỹ thuật** (BT3): chuẩn hoá N_w (dầm giản đơn giữa nhịp = 2,5, không phải 1; ngưỡng 0,2 không tương đương N_M); dải N8 nên chuẩn hoá theo αEI (0,14–0,42; với α 0,9–1,3: 0,12–0,30); số không khớp (24,8 vs 23%; 2,7× vs 3,2×; 10⁻⁴ vs 5×10⁻⁶; "một nửa tích phân" thực ra 173%); quy tắc đặt strain gauge phải theo cực trị cM_q/EI.
5. **Cầu Mây** (BT4): không nêu mốc tham chiếu đồng hồ; "sai số chuẩn 1,9–2%" là phân tán ngang hệ thống chứ không phải lặp; kết luận phụ thuộc dung sai chọn; con số 21–25% trong tóm tắt dựa trên cách đọc tần số có điều kiện.
6. **Độ dài**: khoảng 13.200 từ tính cả phụ lục; nên ~9.000.
7. **Thiếu tài liệu**: Yan, Hao, Yuen & Papadimitriou, MSSP 2022 (doi 10.1016/j.ymssp.2022.109133) — ước lượng GVW từ tỉ số phản ứng hai tải, gần SLM, phải trích và phân biệt; Yu, Cai & Deng, SIE 2018 (NOR-BWIM với vị trí ngang); Lobo Aguilar & Christenson 2018 (shear-strain BWIM).
8. **Hành chính**: khai trùng lặp với 2 bài ở *Structures*; xung đột lợi ích; DOI dữ liệu Cầu Mây; Hình 1, 5; lỗi nhãn hình 3, 4, 8, 9; README gói bổ sung cũ.

## Việc làm được ngay (v4)
- Áp bộ ước lượng GLS/miễn nhiễm lên NOR-BWIM ngày 2 với hiệp phương sai nhiễu đo từ đoạn không xe (kiểm chéo, tránh trong mẫu); ước lượng ρ thực.
- Báo cáo đủ 12 kênh ngày 1, khoảng tin cậy 95%, kiểm định tương đương; đưa sai số ngày 2 vào tóm tắt; bỏ "không phụ thuộc vận tốc".
- Sửa chuẩn hoá, các số không khớp, dải N8 theo αEI, quy tắc strain cM_q/EI.
- Đổi tuyên bố đóng góp; trích Yan 2022 và các tài liệu trên (sau khi kiểm).
- Cắt còn ~9.000 từ; sửa nhãn hình; cập nhật README gói bổ sung; sửa nb_field.py ghi đè log.

## Cần tác giả
Khai trùng lặp; xung đột lợi ích; DOI dữ liệu; Hình 1, 5; (tuỳ chọn) thí nghiệm phòng lab.
