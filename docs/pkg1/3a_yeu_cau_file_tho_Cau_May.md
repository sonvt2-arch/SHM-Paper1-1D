# Đề nghị bổ sung tài liệu Cầu Mây (cầu chính 55 + 90 + 55 m)

Kính gửi tác giả báo cáo kiểm định Cầu Mây (Công ty TNHH Tư vấn Đại học Xây dựng, 2020),

Cảm ơn anh/chị đã gửi phiếu cân 10 xe và các mô hình MIDAS của cầu dẫn. Để hoàn thiện phần cầu liên tục của bài báo và chuẩn bị đợt đo xe chạy chậm (đề cương: `docs/pkg1/3_de_cuong_thu_nghiem_hien_truong.md`), chúng tôi đề nghị anh/chị gửi thêm ba nhóm tài liệu dưới đây. Tất cả đều là tài liệu của **cầu chính** (nhịp N6, N7, N8; trụ T5–T8).

## 1. File thô SDA-830C của lượt xe chạy trên cầu chính (ưu tiên cao nhất)
- File gốc do máy xuất ra (định dạng của máy, hoặc .txt/.csv), chưa qua xử lý. Gồm các lượt xe khoảng 25 t chạy 30–40 km/h, đo tại giữa nhịp **N6, N7, N8** và trên trụ **T5–T8**, đủ 3 phương.
- Kèm theo: tần số lấy mẫu; kênh nào là gia tốc, kênh nào là chuyển vị; hệ số chuyển đổi và đơn vị; biển số và phiếu cân của xe chạy; chiều chạy, làn chạy, tốc độ (nếu có); nhật ký giờ đo.
- Mục đích: kiểm tích phân độ võng khi xe qua cầu liên tục (Eq. 2 của bài) và tách các tần số riêng 1–4. Theo mô hình, f₁ cỡ 1,4–1,6 Hz; con số 3,4–3,6 Hz trong báo cáo có thể là mode cao hơn.

## 2. Bản vẽ trụ và móng T5–T8
- Bản vẽ kết cấu thân trụ T6, T7 (liền khối với dầm) và T5, T8 (gối chậu): kích thước tiết diện thân trụ, chiều cao trụ, bệ cọc, số cọc và chiều dài cọc. Thêm số liệu địa chất tại trụ, nếu có.
- Bản vẽ bố trí chung cầu chính, có cao độ đáy dầm và mực nước.
- Mục đích: xác định độ cứng xoay của trụ k. Đây là đại lượng mà hai số đọc võng tĩnh năm 2020 không tách được khỏi EI của dầm, và nó quyết định khả năng quan sát của võng kế nhịp biên N8.

## 3. Mô hình MIDAS Civil của cầu chính
- File .mcb (hoặc .mct) của **cầu chính 55 + 90 + 55 m**, dùng cho tính toán thử tải năm 2020 (đã có kết quả N8 = 5,93 mm và N7 = 16,70 mm). Đề nghị gửi bản có tiết diện thay đổi, liên kết trụ–dầm và lò xo móng.
- Nếu tiện, gửi thêm phương án tải sơ đồ III và IV (tọa độ xe).
- Mục đích: thay giả thiết về quy luật chiều cao dầm (parabol, L_v = 44 m) bằng tiết diện thật, và chốt vị trí đặt cảm biến trước đợt đo.

Các file trên 2 MB xin chia phần theo hướng dẫn `docs/06_huong_dan_chia_file_len_drive.md`, rồi để vào thư mục Drive "Cầu Mây gửi Thái Sơn". Nếu có tài liệu nào không còn lưu, xin anh/chị cho biết để chúng tôi ghi rõ trong bài.

Trân trọng cảm ơn.
