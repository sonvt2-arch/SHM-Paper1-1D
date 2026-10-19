# Tổng hợp 4 biên tập viên mô phỏng đọc bản v4.4 (19/10/2026)

| Biên tập viên | v3 (18/10) | v4.4 |
|---|---|---|
| 1. Tổng biên tập SCHM | Gửi phản biện có điều kiện; phù hợp 8, chất lượng 6 | **Trả lại trước phản biện**; phù hợp 7, mới 4, kỹ thuật 7, bằng chứng 3, rõ/độ dài 4, khả năng qua phản biện 3 |
| 2. BWIM | Sửa lớn; mới 5, kỹ thuật 6 | **Trả lại trước phản biện**; mới 3, kỹ thuật 6, trung thực 6, thực tiễn 4 |
| 3. Cơ học | Sửa lớn; kỹ thuật 7; "không cần thí nghiệm mới" | **Trả lại trước phản biện**; kỹ thuật 6 (lý thuyết 7, lab 4, hiện trường 4, cầu 5), rõ 6; **cần thí nghiệm mới** |
| 4. Hiện trường, tái lập | Sửa lớn; bằng chứng 5, tái lập 7 | Gửi phản biện, dự kiến sửa lớn; bằng chứng 3, thống kê 6, ngân sách sai số 4, **tái lập 8**, dữ liệu 6 |

Vì sao nặng hơn v3: bản v4 trình bày trung thực (mean-weight thắng mọi bộ ước lượng, GLS kém hơn trung bình, bất biến chỉ trong 10–27 %), nên điểm yếu bằng chứng lộ rõ; bản v3 còn che bằng kết quả GLS lạc quan.

## Điểm chung cả 4 người
1. **Không thí nghiệm nào kiểm điều bài tuyên bố là mới** (vết mù, dải gần mù, N_M, R, quy tắc đặt cảm biến, luật Möbius). Lab hai nhịp bằng nhau, tĩnh; cấu hình mù 2500 + 3644 mm chưa làm; NOR-BWIM không có gauge gần điểm mù, không có kênh võng; Cầu Mây chỉ có hai số đọc tĩnh, thử tải di động mới là dự báo.
2. **Tính mới mỏng**: các tiêu chí suy ra một bước từ kết quả kinh điển (điểm uốn của mô men tải đều, đỉnh của hàm lồi, Sherman–Morrison/reanalysis). Phần được công nhận: danh mục vết mù (nhất là strain), R, luật Möbius áp cho trụ liền khối.
3. **Hệ số 6,6 ở Cầu Mây yếu**: phụ thuộc dung sai τ; dải chấp nhận gồm α ≈ 0,5 (mất 49 % độ cứng) mà chính bài coi là phi lý; với prior α 0,9–1,3 dải chỉ còn khoảng 2,5 lần; vị trí xe dọc cầu chưa lập bảng nên không tái lập được.
4. **Bài dài** (~14.000 từ cả phụ lục); nên 8–9 nghìn.

## Lỗi cụ thể phải sửa dù chọn hướng nào (không cần số liệu mới)
- §5.2: "1,9–2,0 %" là **sai số chuẩn của trung bình (SEM)**, không phải độ lệch chuẩn (SD thật 4,7 % và 5,0 %); lượt sửa đọc mù vòng 2 đã đổi nhầm "spread" thành "standard deviation". Phải sửa lại và xem lại cách dựng τ.
- Supplementary: "10,4 % / 28,4 %" là **RMS**, không phải MAE (MAE 8,5 % / 23,4 %).
- §5.3: cận Cramér–Rao 0,24 giả định tần số thứ nhất đo được, nhưng tần số thứ nhất **chưa đo**; không được gọi là "identified".
- Tốc độ: log `norbwim/logs/field.log` cho thấy tốc độ khớp toàn bản ghi lớn hơn tốc độ tại gauge trung vị 1,139 lần (SD 0,124); bài chưa báo; tốc độ làn B tính khác cách → tỉ số làn 0,79 bị lẫn.
- Bảng A.1: dòng "β = 1,636" thực tính tại β = 90/55 (đúng ra ξ* = 0,2996, N_w = 0,3323 và 0,1641).
- Phụ lục B: thiếu mô men đầu nhịp giữa khi trụ có lò xo; (μ/β², μ/β²) chỉ đúng khi trụ khớp.
- Gói script: Bảng 6, 7 và số mô hình dầm ở §4.2 lấy từ `code/v3`, `code/fieldplan` không có trong zip; `run_all.sh` không chạy phân tích v4; README trỏ `docs/` và đánh số cũ.
- Hình 7: nhãn "immune"; Hình 7c ghi "12 gauges" nhưng chỉ vẽ 2.
- Thư: còn "[date of submission]"; "offset-immune"; nên mở bằng đóng góp, không mở bằng điểm yếu; xác nhận tên biên tập viên hiện tại.
- Thống kê: 12 phép thử tương đương không hiệu chỉnh bội; bootstrap percentile với n = 7–8 hẹp; gauge "tốt nhất" chọn sau.

## Lối ra các biên tập viên gợi ý
- (a) Thí nghiệm cấu hình mù và gần mù trên dầm hiện có (2500 + 3644 mm và λ ≈ 1,40–1,50), tải di động hoặc từng bước, thêm một strain gauge trong dải gần mù và một cặp võng; hoặc thử tải di động Cầu Mây đã thiết kế.
- (b) Không có thí nghiệm: đổi khung thành bài lý thuyết kèm kiểm tra khả thi; bỏ "laboratory verification" và phần hiện trường khỏi tiêu đề; cắt mục 4 thành case study ngắn; hạ tuyên bố đóng góp.
