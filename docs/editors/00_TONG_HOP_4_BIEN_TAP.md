# Tổng hợp đánh giá của 4 biên tập viên (mô phỏng, độc lập) – bản SCHM ngày 2026-10-18

| Biên tập viên | Quyết định | Điểm |
|---|---|---|
| 1. Tổng biên tập SCHM | Gửi phản biện **có điều kiện** | Phù hợp 7, chất lượng 6 |
| 2. Phó BT – BWIM | **Trả lại trước phản biện**; nộp lại thì dự kiến sửa lớn | Tính mới 4, kỹ thuật 6 |
| 3. Phó BT – cơ học kết cấu | Sửa lớn | Kỹ thuật 7 (lý thuyết 9, thí nghiệm 7, phần cầu 5), rõ ràng 7 |
| 4. Phó BT – đo hiện trường | Sửa lớn | Bằng chứng 4, tái lập 6 |

Không ai từ chối hẳn. Cả 4 đều xác nhận lý thuyết đúng (biên tập viên 3 dẫn lại Eqs. 4–10, β_crit, 2cos(π/9), O_m).

## Vấn đề cả 4 cùng nêu
1. **Chưa có thử nghiệm tải di động nào trên kết cấu liên tục.** Thí nghiệm là tải tĩnh trên dầm hai nhịp bằng nhau; Cầu Mây chỉ có số đọc xe đỗ; mục 5 là cầu giản đơn. Ba người đề nghị làm hai thí nghiệm trên giàn sẵn có: cùng tổng tải đổi khoảng cách trục, và thí nghiệm mù 2500 + 3644 mm.
2. **Hồ sơ chưa đủ để xử lý:** thiếu hình 1, 2, 4, 5, 6, 10; chưa khai trùng lặp với 2 bài ở *Structures*; còn [NEED VALUE] (xung đột lợi ích, quỹ, DOI dữ liệu).

## Vấn đề kỹ thuật quan trọng (đã kiểm một phần)
3. **Phần Cầu Mây trình bày sai về hiệu chỉnh** (BT3, BT1, BT4):
   - "Cách A" trong bảng là EI thiết kế + k_FE, không khớp số đo (N7 lệch 11%). Biến thể khớp (α = 1,088) cho chỉ số khoảng 0,16, không phải 0,181.
   - Không cặp (α, k) nào khớp đúng cả hai số đọc: hai tham số chỉ vào dưới dạng k/α và một hệ số tỉ lệ. Tỉ số đo/mô hình N8/N7 nhỏ nhất là 1,058 tại cách B. Vậy B là gần nhất (dư khoảng 6%), không phải "khớp".
   - α = 0,716 (E thấp hơn thiết kế 28% trên dầm DƯL mới) là phi vật lý, nhất là khi cầu đo cứng hơn thiết kế.
   - Sửa: thay hai điểm bằng **dải chấp nhận được của chỉ số nhịp biên theo k/α**; sửa thứ tự cận N7 ở Bảng 5; nói rõ giả thiết vùng cứng trên trụ, quy luật chiều cao n = 2,943.
4. **Độ lệch zero giả định quá lạc quan** (BT4, BT2, BT1): 0,02–0,05 mm cho nhịp 90 m vượt sông, trong khi bản ghi của chính bài cho 0,17–0,23 mm. Với 0,2 mm, sai số tải khoảng 370% (N8) và 45% (N7). Con số 35–93% trong tóm tắt là kịch bản, không phải kết quả. Sửa: mở rộng Bảng 8 tới 0,1–0,5 mm, ghi giá trị ε0 cạnh mọi con số chính.
5. **Bảng 10 gọi là theo GUM nhưng không phải** (BT4, BT1): khoảng giá trị bị nhập như độ không đảm bảo chuẩn; bỏ qua tương quan offset trong SLM; loại A chỉ chặn trên; không có độ không đảm bảo mở rộng; bước 1,010 → 1,017 chưa đưa vào.
6. **Tính mới** (BT2, BT1): đẳng thức tích phân là Ojio–Yamada cộng tương hỗ; tỉ số mù chính xác chỉ đúng cho dầm lăng trụ, Bảng 5 cho thấy không chuyển sang dầm vút. Sửa: đặt đóng góp vào **quy trình** (C_m, tỉ số triệt tiêu, tải tương đương offset, độ nhạy theo độ cứng trụ), thêm khảo sát vết mù theo tỉ lệ vút, nói rõ BWIM theo đường ảnh hưởng không bị mù tại các điểm này.
7. **Hiệu ứng hiện trường bị bỏ qua** (BT2): vị trí ngang (chênh tới 2,05 mm), xe đi một mình trên cả 200 m khoảng 12 s, nhiều xe cùng lúc.
8. **Mục 5 (bản ghi Gie Cục, Phương Độ) yếu** (BT1, BT2, BT4): hệ số kênh chưa rõ, thuỳ −2,8 mm ở Phương Độ N1, răng cưa lượng tử. Hai người đề nghị bỏ hoặc chuyển sang tài liệu bổ sung.
9. **Độ dài và độ chính xác thừa** (BT1): khoảng 15,5 nghìn từ tính cả phụ lục; số in 6–11 chữ số; O_m, Monte Carlo, cầu phương, phụ lục D làm loãng mạch chính.
10. **Thí nghiệm:** thứ tự tải 3 trục chọn sau bằng cách khớp; tỉ số đo/lý thuyết tăng theo tải; ghi công Ojio–Yamada qua nguồn thứ cấp.
11. **Gói tái lập:** `REPRODUCTION_REPORT.md` chưa cập nhật theo bản thảo mới; gói phụ thuộc thư mục ngoài; thiếu số đọc thô 3 chu kỳ.

Tài liệu nên thêm (BT2 đã kiểm trên web; cần kiểm lại trước khi trích): Agüero-Barrantes et al. 2021, doi 10.15517/mym.v11i0.46400; Wu et al. 2020, doi 10.1007/s11709-020-0653-0.

## Phân loại việc sửa
**Làm được ngay (không cần tác giả):** mục 3 (quét dải k/α, viết lại phần Cầu Mây), 4 (mở rộng Bảng 8, sửa tóm tắt), 5 (làm lại Bảng 10 hoặc đổi tên thành "ngân sách độ nhạy chỉ báo"), 6 (đổi khung đóng góp, khảo sát vết mù theo tỉ lệ vút), 7 (thêm vị trí ngang, nhiều xe vào phần hạn chế và ngân sách), 8 (chuyển mục 5 sang tài liệu bổ sung), 9 (cắt còn khoảng 10 nghìn từ, làm tròn số), 11 (cập nhật gói tái lập), thêm 2 tài liệu sau khi kiểm.

**Cần tác giả:** hình thí nghiệm; khai trùng lặp; xung đột lợi ích và quỹ; số đọc thô 3 chu kỳ (A1); xác nhận thứ tự tải 3 trục (A3); kích thước trụ hoặc tần số đo của Cầu Mây (để chọn dải k); **quyết định có làm 2 thí nghiệm trên giàn không** (cả 4 biên tập viên đều xem đây là điểm yếu lớn nhất).
