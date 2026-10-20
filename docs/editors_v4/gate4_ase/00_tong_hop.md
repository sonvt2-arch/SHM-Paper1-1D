# Cổng 4 trên bản ASE cuối (20/10/2026): 4 biên tập viên + 1 tổng biên tập mô phỏng (Opus, ngữ cảnh sạch)

| Vai | Phán quyết |
|---|---|
| Tổng biên tập ASE | Đúng phạm vi; mức mới đủ cho ASE; không có lý do loại ngay |
| BTV 1 kết cấu cầu | sửa rồi gửi |
| BTV 2 SHM, đo lường | sửa rồi gửi |
| BTV 3 BWIM | sửa rồi gửi |
| BTV 4 tổng quát | sửa rồi gửi |

So với v4.4 (3/4 trả bài trước phản biện), không ai loại; cả 4 đòi sửa trước khi gửi phản biện.

## Điểm chung (nặng)
1. Hệ số 6.6 (cả 4 BTV): đầu trên cần α ≈ 0.5; với tiên nghiệm α ∈ [0.9, 1.3] chỉ ~2.4 (ident_freq.log:51); ô C8 ở τ = 3, 4 % để trống (log có: 1.54, 3.39).
2. Độ dễ đọc (cả 4): tóm tắt ~184 từ (> 150); mục 2.2 Eq. (4)–(9) liền nhau; mục 5.2 đ4, 5.3 đ2–4, 4.2 đ1 dồn số; bảng ký hiệu chỉ ở S1.
3. Thiếu bảng vị trí dọc của xe thử tĩnh cầu Mây (BTV 1, 2, 3).
4. Lập τ: chia cho √6 dù 6 số đọc không phải lặp; nguồn của 1.75 % (BTV 1, 2, 3).
5. Khuyến nghị lấy Σ từ phần dư chưa có bằng chứng (23.4 % ngoài mẫu) (BTV 2, 3).
6. Tiêu chí mù biến dạng là của lý thuyết dầm; gauge bản mặt có thành phần cục bộ (ch11/ch8 = 3.9) (BTV 1, 2).
7. Ngưỡng 0.2 chưa có định nghĩa vận hành và độ nhạy (cả 4).

## Khác
Khoảng trống nên chỉ giả thiết bị vi phạm (SLM mặc định C ≠ 0), so cụ thể với Deng 2025; k, α là tham số hiệu dụng (bỏ cách đọc "loss of rigidity");
tiêu đề có thể thêm "weigh-in-motion"; nhan đề mục theo kết quả; chú thích Hình 2 (N8 ở 0.4L), 4 (trục thời gian, vết màu), 6c (N_ε), 7 ("static valley");
"antisymmetric pattern" (θ6 = −θ7); câu "each lane needs its own constant" (CI chạm 1); phương pháp bootstrap.

## Vòng 2 (20/10, sau bản sửa)

| Vai | Phán quyết |
|---|---|
| BTV 1 kết cấu cầu | gửi phản biện |
| BTV 2 SHM, đo lường | gửi phản biện |
| BTV 3 BWIM | gửi phản biện |
| BTV 4 tổng quát | gửi phản biện |

Không còn mục nặng. Đã sửa sau vòng 2:
- Ghép cặp cùng điều kiện ở Tóm tắt, mục 1, 5.2, Kết luận 3, thư: "6.6 against 1.5" (α tự do, τ = 5.3 %) và "2.4 against 1.1" (α giới hạn 0.9–1.3 lần thiết kế); bỏ chữ "plausible"; mục 5.2 nói rõ hai kịch bản, tiên nghiệm loại calibration B.
- Bảng S13 thêm cột C7 và C7 max/min (τ = 3 %: 1.1; 4 %: 1.4; 5.3 %: 1.5; tiên nghiệm: 1.1), lấy từ `ident_static.log` (thêm in C7, các số khác không đổi) và `ident_freq.log` dòng 51; mục 5.2 thêm câu độ tương phản giữ ở τ = 3, 4 %.
- Mục 5.2 đ3: chuyển suy dẫn 2.64 %/1.75 %/√6 sang S8 (đã có nguyên văn); đ4 nêu B_m 0.51 với 0.12.
- Câu cuối tóm tắt gắn "on this girder"; mục 6 "for a residual offset of 0.1 mm … on this 200 m unit", trỏ Bảng S17; mục 4.2 ghi CI 90 % 0.76–1.27 cạnh "27 %"; "necessary" sửa ở 4.3 và S10; chú thích Bảng 3 a; chú thích Hình 3, 6 về chuẩn hoá theo nhịp; câu tình huống dùng ở cuối mục 1 đ3; đóng góp (ii) thêm "the rule itself is not tested in the field"; chú thích Bảng 2 về độ phủ bootstrap; S7 câu 12 phép thử; tên dạng xoay trụ θ6 = −θ7 thống nhất ở S5, Bảng S1, Hình S7; "in brackets" -> "in parentheses".
- Giữ dưới trần 12.000 từ quy đổi: chuyển hai câu chi tiết sang S6, S7; rút vài câu trùng (mục 2.3, 4.1, 5.3, 6).
- Chưa làm (thiếu dữ liệu, không bịa số): độ lặp đồng hồ so (BT2 của BTV 2), tải từng quả nặng (BT26); BT22 của BTV 1 (chọn chỗ gauge biến dạng) giữ câu "Which governs depends on…".
