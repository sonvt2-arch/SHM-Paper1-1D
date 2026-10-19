# Hostile reviewer audit, 19/10/2026 — tổng hợp và cách xử lý

Phân vai: đọc mù liền mạch (Opus); 1 phương trình (Opus); 2 con số (Opus); 3 bảng và hình (Opus); 4 tính mới (Opus);
5 trích dẫn/DOI qua Crossref (Sonnet); 6 tóm tắt–kết quả–kết luận (Opus); 7 dấu vết AI (Sonnet); 8 soát chữ (Opus).
Sau đó: vẽ lại hình (Opus), đóng gói lại scripts.zip (Sonnet), đọc mù cuối (Opus).

## Lỗi chặn
- PDF mất toàn bộ công thức: do LibreOffice của máy thiếu gói libreoffice-math (bản docx không lỗi). Đã cài gói;
  build_docx.sh nay báo lỗi nếu PDF không có ký hiệu toán.

## Đã sửa theo quyết định của thầy
- Mức khẳng định (thầy chọn "sửa hết, 6.6 kèm điều kiện"): closed form chỉ cho dầm lăng trụ, tiêu chí điểm 0 của M_q cho dầm có vút;
  luật Möbius cho dầm đối xứng có trụ bằng nhau; quy tắc đặt cảm biến cần nhiễu không phụ thuộc vị trí; kết quả GLS một ngày;
  4 gauge ngày 1 lệch 22–26 %; strain/deflection chỉ so ở giữa nhịp, đảo chiều gần điểm 0; 6.6 ở mức dung sai hai độ lệch chuẩn,
  cận trên cần α ≈ 0.5; "bound within a factor of 1.5" cho nhịp chính; câu khoảng trống nghiên cứu thu hẹp; định nghĩa "observes".
- Trích thêm 4 bài (đã kiểm Crossref, OpenAlex, Semantic Scholar): Elfving 1952; Udwadia 1994; Papadimitriou 2004; Katafygiotis & Beck 1998.
- Vẽ lại 19 hình + graphical abstract: bỏ tiêu đề ghi chú, mã nội bộ, chữ bị cắt, nhãn chồng; log không đổi.
- Đánh số lại hình/bảng Supplementary theo thứ tự trích lần đầu (Fig. S9↔S11; Table S7↔S8, S10↔S12).
- CRediT: thêm Investigation, Data curation cho Q.-B. Nguyen.

## Đã sửa (chắc chắn, không cần quyết)
- Danh mục: Fan 2015 (+Wu Y), Yang 2021 (+Zhang Y), Zhu 2022 (Zhou Z), Zhou 2026 (số 1), Lobo Aguilar 2021, thứ tự Zhu J/Zhu XQ và Agüero.
- Yu et al. 2016 trích như bài tổng quan; thư: "Yu et al. (2016)".
- Số: 15.43 mm; CV làn B; tốc độ 1.4 % trung bình (tối đa 4.6 %); "một phần tư đến một phần ba" (một phần năm tại mặt trụ);
  chú thích Bảng 3/S14 (biến thể chiều dài vút 40–45 m); "base model" cho 14.0/0.59; 2.64 % là SE gộp; 90 % CI 0.76–1.27;
  0.9 % là tỉ số phương sai, 10.6 % là bộ ước lượng zero-sum; ghi chú Bảng S9 (12.8); 5 × 10⁻⁵ ở ρ = 0.9; hệ số 4 (độ võng)/2 (biến dạng);
  12.4 s gồm chiều dài trục xe; β = 90/55.
- Ký hiệu: \hat P cho ước lượng; R định nghĩa cho C > 0; μ ở Bảng S1; T5–T8; r² đúng chỗ; 0.4$L$; $n$, $p$, $\chi^2$.
- Chữ: "this threshold"; câu tỉ số st36; "12" thay "twelve"; OIML viết đầy đủ; 0.65–1.00; Equation/Figure ở đầu câu;
  chú thích Hình 5 (chỉ dải ±10 %); câu hạn chế mục 6; bỏ câu "Every equation ... checked" ở Data availability.
- scripts.zip: bỏ ASE_numbering.md, REPRODUCTION_REPORT.md, logs/files-v2; xoá đường dẫn tuyệt đối; README theo số cuối; cờ --all.

## Giữ nguyên (lý do)
- "Acknowledgements": tên mục theo hướng dẫn của Sage.
- Địa chỉ không dấu: dạng quy định ở VII.6.
- N_w dùng trước định nghĩa ở mục 2.2: đã có câu trỏ (thầy quyết ở lượt trước).
- Ghali et al. 2017: số lần xuất bản chưa xác minh được (Crossref ghi "6th edition" cho bản CRC 2017), để như cũ.
- In nghiêng tên tạp chí, "Fig." trong chữ: để Sage biên tập.
- Tóm tắt 183 từ (dài hơn mục tiêu 150 vì thêm điều kiện phạm vi theo quyết định của thầy).
- Thứ tự trích bảng S ở bài chính (S10, S11, S13 trước S12) khác Supplementary; Supplementary đã theo thứ tự.

## Đọc mù liền mạch cuối (Opus, sau mọi sửa)
5 bắt buộc: sửa 2 (ký hiệu k ở Hình S4 đổi thành "2/3 sensors", vẽ lại; n bỏ khỏi chú thích Bảng 2, S7 và Hình 7);
đóng 3 theo nguồn (Lobo-Aguilar 2023 đúng như Crossref; địa chỉ không dấu theo VII.6; số thập phân Bảng S10 giữ như phiếu cân).
6 cân nhắc: thầy cho sửa 4 nhóm ("design pier stiffness" thay "calibration A" khi α refit = 1.07; "influence-area identity" ở tóm tắt;
tách câu dài ở 5.3; nối kết quả GLS với quy tắc ở (ii) và viết gọn mục 2, 3 của thư). Các chỗ sửa này nằm sau lượt đọc cuối; kiem_khoa đạt.
Ghi chú: điểm A′ ở Hình S15 (α = 1.088, best static α tại k thiết kế) khác α* = 1.07 ở mục 5.3 (refit ở Hình 7b); không gắn hai chỗ với nhau.
