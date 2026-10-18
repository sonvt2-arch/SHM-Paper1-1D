# Cập nhật 2026-10-18: câu trả lời mới trên Drive (từ bảng hỏi của bài MSSP)

## Nguồn
Thư mục Drive "1. Dữ liệu thử tải cầu" có 4 file mới (14–15/10/2026):

| File | ID | Kích thước | Đã đọc |
|---|---|---|---|
| Cau_hoi_lam_ro_so_lieu_thu_tai_5_cau.docx | 1hlOoX1K5cK-yhPpuGE8_ZqR7KjwJf-r5 | 646 KB | Có |
| Cau_hoi_mo_hinh_FEM_Midas_5_cau_1.docx | 1RyIah3OGig2fzWmnbzFSEcftW0ICZ_Mt | 155 KB | Có |
| Thông tin bổ sung.rar | 1cl2zvWYrLCHrFv96Z2h6-kCNCgxbNikv | 9,3 MB | **Không**: quá giới hạn tải (~2,4 MB) và máy chủ không giải nén được rar |
| 01 - Báo cáo kiểm định cầu Phương Độ.docx (bản chuẩn gửi lại) | 11zFhi96LrW8gYgDbeRQK-xwwPLI-yaKL | 131 KB | Chưa |

**Lưu ý:** hai bảng hỏi này là của **bài khác** (MSSP26-6346, phân bố ngang trên các nhịp dẫn giản đơn), không phải bảng hỏi của bài này (`docs/word/Cau_hoi_bo_sung_so_lieu.docx`, chưa có trả lời). Tuy vậy, một số câu trả lời dùng được cho bài này.

## Những câu trả lời dùng được cho bài này (đối chiếu mã câu hỏi của bảng hỏi Paper1)

| Mã Paper1 | Nội dung trả lời (trích, nguồn) | Hệ quả |
|---|---|---|
| B4 (phiếu cân Cầu Mây) | Đã gửi phiếu cân 10 xe; các nhịp liên tục dùng 10 xe; trung bình 25,06 t; trục 3,6 m và 1,35 m, vệt bánh 1,85 m, xe cách nhau 1,1 m (ngang) và 6 m (dọc). (Bảng hỏi số liệu M3, M4; bảng hỏi FEM M1) | Thay 25 t danh nghĩa bằng 25,06 t (+0,24%). Phiếu cân chi tiết có lẽ nằm trong file rar |
| B8, C6, D6 (quyền công bố) | "Được phép công bố do tác giả là người thực hiện thử tải." (bảng hỏi số liệu C12) | Điền mục Data Availability |
| B9 (xung đột lợi ích) | Cùng câu trên: tác giả là người thực hiện thử tải | Cần khai trong mục Conflicts of Interest / ghi rõ vai trò tác giả |
| B1 (mô hình MIDAS) | "Gửi file midas cho từng cầu" (C10); Midas Civil 2019, mô hình mạng dầm (C1). Với Thái Bình chỉ gửi mô hình 3 nhịp thử tải N2, N4, N24 (nhịp dẫn), không phải cầu chính liên tục | Phải mở file rar để biết có mô hình cầu chính Cầu Mây 55+90+55 không. Nếu chỉ có nhịp dẫn thì B1–B3 vẫn chưa được trả lời |
| B6 (thiết bị đo) | Đồng hồ Mitutoyo; thử ban ngày, trời nắng nóng; sai số đặt xe < 20 cm mỗi phương (C8, C9 FEM) | Bổ sung mô tả và ngân sách sai số |
| D3 (xe Gie Cục) | Không còn phiếu cân; 3 xe dùng cho cả hai khối và hai sơ đồ; ngày thử 11/12/2018; cầu chéo 70°, mô hình gối vuông góc (G5, G9, G12) | Không kiểm được tải tuyệt đối từ bản ghi động Gie Cục |
| C (Thái Bình) | Ngày thử 01/07/2023; số liệu gốc trùng báo cáo; không truy vết xe theo vị trí (L1, L4, L5) | Không giúp phần cầu chính liên tục |
| Mô đun đàn hồi | Mây E_dầm = 3,2777e7 kN/m² (super-T nhịp dẫn); Giẽ 3,3238e7; Phương Độ 3,077e7 (C2 FEM) | Chỉ áp cho nhịp dẫn/giản đơn; cầu chính Mây vẫn dùng Ec = 36 057 MPa của báo cáo |

## Việc cần làm
1. Tác giả giải nén `Thông tin bổ sung.rar` trên máy, rồi để các file lên Drive. File < 2 MB để nguyên; file lớn hơn chia phần 2 MB bằng 7-Zip (`docs/06_huong_dan_chia_file_len_drive.md`). Quan trọng nhất là phiếu cân 10 xe Cầu Mây và các file Midas (.mcb).
2. Kiểm xem có mô hình cầu chính Cầu Mây 55+90+55 m trong đó không. Nếu có, chạy lại WP3 để chốt chỉ số tại điểm N8.
3. Bảng hỏi riêng của Paper1 (B2 kích thước trụ, B3 số đọc ở nhịp không tải, B7 file thô lượt xe chạy, phần A về thí nghiệm) vẫn chưa có trả lời.
