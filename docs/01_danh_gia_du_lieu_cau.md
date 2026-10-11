# Đánh giá dữ liệu thử tải 5 cầu cho việc kiểm chứng bài báo

Ngày: 2026-10-11. Nguồn: thư mục Drive "1. Dữ liệu thử tải cầu". Chi tiết từng cầu ở `data/bridges/<cầu>/INVENTORY.md`.
Mọi số dưới đây lấy từ file đã đọc; chỗ chưa có ghi [NEED VALUE].

## 1. Tóm tắt theo cầu

| Cầu | Sơ đồ | Nhịp (m) | Số liệu đo có trong Drive | Bản ghi độ võng theo thời gian / theo vị trí xe | Mức hữu ích |
|---|---|---|---|---|---|
| Cầu Mây (ĐT389, Hải Dương, 2020) | **Dầm hộp BTCT DƯL liên tục 3 nhịp**, đúc hẫng, chiều cao 2,4–5,4 m | 55 + 90 + 55 | Độ võng tĩnh giữa N7, N8 (đoàn xe 4/6/10 xe ~25 t); ứng suất; tần số 3,0–3,6 Hz | Không (động chỉ có hình PDF) | **Trung bình**: cầu liên tục thật, có MIDAS, vị trí gần "mù" |
| Thái Bình (thư mục "Lạng Am", 2023) | **Dầm hộp liên tục 3 nhịp**, trụ T12, T13 liền dầm | 42 + 63 + 42 | Độ võng tĩnh 3 điểm/nhịp, 4/6/4 xe 29–32 t; đo/FE = 0,88–0,97; tần số 2,9–3,0 Hz | Không | **Thấp–Trung bình** |
| Gie Cục I (QL1, 2018) | Giản đơn, dầm I DƯL | 3 × 25,7 | Độ võng tĩnh; **bản ghi động 200 Hz, 15 s, N1–N3** | Có (từ máy SDA-830C), chưa rõ hiệu chuẩn | **Thấp–Trung bình** (chỉ kiểm tích phân trên dầm giản đơn) |
| Phương Độ (2018) | Giản đơn, dầm T BTCT | 2 × 18 | Độ võng tĩnh; **bản ghi động 200 Hz N1, N2**; gia tốc thô N2 | Có | **Trung bình cho kiểm tích phân**, thấp cho phần liên tục |
| Sông Sặt (Hải Dương, 2024) | Super-T giản đơn, liên tục nhiệt | 39,15 + 40 + 39,15 | Độ võng tĩnh N1; tần số | Không | **Thấp** |

## 2. Kết luận chính

1. **Không có bộ dữ liệu nào kiểm chứng trực tiếp được định lý bất biến trên cầu liên tục.** Hai cầu liên tục (Cầu Mây, Thái Bình) chỉ có số đọc tĩnh khi đoàn xe đỗ tại một vị trí. Không có lượt xe chạy chậm, không có chuỗi vị trí xe kiểu đường ảnh hưởng.
2. **Dùng được ngay (cấp 1, không cần thử nghiệm mới):**
   - *Bản đồ quan sát được áp cho cầu thật.* Tính sơ bộ với EI không đổi (`code/analysis/cm_multispan.py`):

     | Vị trí cảm biến | 192EI·C_m/L⁴ | Phần âm / phần dương |
     |---|---|---|
     | Mô hình thí nghiệm 2 × 2,5 m (đối chứng, khớp Eq. 11) | 1,000 | −0,429 |
     | Cầu Mây, giữa nhịp biên 55 m | **0,163** (< ngưỡng 0,2: gần mù) | −0,921 |
     | Cầu Mây, giữa nhịp chính 90 m | 0,755 | −0,301 |
     | Thái Bình, giữa nhịp biên 42 m | 0,481 | −0,764 |
     | Thái Bình, giữa nhịp chính 63 m | 0,705 | −0,368 |

     Cầu Mây có điểm đo thật ở giữa nhịp N8 (nhịp biên 55 m), đúng vùng gần mù. Đây là minh hoạ cầu thật cho tiêu chí quan sát được trước khi lắp cảm biến. **Phải tính lại với EI(x) thực** (dầm hộp thay đổi chiều cao 2,4–5,4 m) từ mô hình MIDAS hoặc bản vẽ, vì EI lớn ở trụ sẽ dịch kết quả.
   - *Hiệu chỉnh EI bằng số liệu tĩnh.* Đo/FE = 0,88–1,00 (Cầu Mây) và 0,88–0,97 (Thái Bình) cho phép ước lượng sai số của BPM khi dùng EI thiết kế. Đây là số liệu thật cho mục ngân sách sai số 4.1.
   - *Tính tuyến tính theo tải.* Cầu Mây có đoàn 4, 6, 10 xe: kiểm tra độ võng tỉ lệ với tổng tải (tiền đề của SLM) trên cầu liên tục thật.
   - *Bản ghi động Gie Cục I, Phương Độ.* Áp bộ ước lượng tích phân lên lượt xe thật (dầm giản đơn). Ba nhịp giống nhau của Gie Cục cho phép kiểm độ lặp. Bản ghi cũng cho thấy trôi đường nền thật (N1 Gie Cục trôi ~1,6 mm trong 15 s), tức là bằng chứng hiện trường cho kết luận "trôi zero là nguồn sai số chủ đạo" (mục 4.2). Cần biết trọng lượng xe, vận tốc và dầm được đo. Biên độ động (7,8–10,8 mm) lớn hơn độ võng tĩnh của 3 xe (3,6 mm), nên kênh độ võng có thể chưa hiệu chuẩn; chỉ dùng tương đối.
3. **Thiếu và cần xin bổ sung** (từ đơn vị kiểm định: HUCE, T&D Việt Nam, Tư vấn ĐHXD):
   - File thô SDA-830C (lượt xe động) của Cầu Mây, Thái Bình, Gie Cục, Phương Độ, Sông Sặt.
   - Mô hình MIDAS (.mcb) hoặc bảng đặc trưng mặt cắt EI(x) của Cầu Mây và Thái Bình.
   - Trọng lượng cân thực tế và tải trục từng xe; xe nào chạy lượt động, vận tốc, làn xe.
   - Số đọc võng ở nhịp không đặt tải (ví dụ võng giữa N8 khi đoàn xe ở N7). Nếu có, đây là bằng chứng đo trực tiếp phần đóng góp âm của nhịp kề.
4. **Bằng chứng quyết định vẫn là một đợt đo mới trên cầu liên tục** (xem kế hoạch, Gói WP5): xe chạy chậm, hai cấu hình trục khác nhau có cùng hoặc khác tổng tải, cảm biến ở 0,42L nhịp biên, giữa nhịp chính và ở vị trí gần mù.
