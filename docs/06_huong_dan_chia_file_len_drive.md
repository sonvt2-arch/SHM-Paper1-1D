# Hướng dẫn chia nhỏ file lớn để chuyển từ Drive lên GitHub

## Vì sao phải chia
Kết nối Google Drive của Claude chỉ tải được file nhỏ. Đã thử: 2,4 MB tải được; 6,6 MB và 9,8 MB làm ngắt kết nối. Vì vậy mỗi phần phải **≤ 2 MB**.

## Cách chia (Windows, dùng 7-Zip, miễn phí tại 7-zip.org)
1. Chuột phải vào file hoặc thư mục cần chuyển → **7-Zip → Add to archive…**
2. Trong hộp thoại:
   - **Archive format:** `zip`
   - **Compression level:** `Store` (nhanh nhất; file zip, rar, pdf vốn đã nén)
   - **Split to volumes, bytes:** gõ `2M`
3. Bấm OK. 7-Zip tạo các file `ten.zip.001`, `ten.zip.002`, …
4. Trên Drive, tạo thư mục **`Upload_GitHub`** trong `Paper1 - 1D`. Với mỗi file gốc, tạo một thư mục con (ví dụ `Upload_GitHub/SupplementaryMaterial_JCSHM/`) và kéo **tất cả** các phần `.zip.001, .002, …` vào đó. Đừng đổi tên các phần.
5. Báo Claude tên thư mục. Claude sẽ tải từng phần, ghép lại, kiểm tra, giải nén và đẩy lên GitHub.

Lưu ý:
- File `.rar` (ví dụ hồ sơ thiết kế Cầu Mây): máy chủ của Claude không có công cụ giải nén rar. Anh/chị giải nén rar trên máy trước, chỉ giữ phần cần, rồi chia theo các bước trên.
- Với PDF bản vẽ rất lớn (Thái Bình, 289 MB), không cần chuyển cả bộ. Chỉ in hoặc xuất ra PDF các trang cần (xem danh sách dưới). Nếu tệp xuất ra dưới 2 MB thì để thẳng lên Drive, không cần chia.

## Nên chuyển những gì (xếp theo ưu tiên)

| Ưu tiên | File | Vị trí trên Drive | Dùng để |
|---|---|---|---|
| 1 | `SupplementaryMaterial_JCSHM.zip` (9,8 MB) | `Paper1 - 1D/JSCHM/…` | Các script Monte Carlo, tải di động, kiểm ký hiệu, sai số cầu phương mà bài ghi là nộp kèm |
| 2 | Hình gốc thí nghiệm (Fig. 1, 2, 4, 5, 6, 10): thư mục `figs/` trong `files-JSCHM-SUBMIT.zip` (67 MB) | `Paper1 - 1D/JSCHM/` | Hình cho bản nộp SCHM. Nếu được, chỉ nén riêng thư mục hình |
| 3 | Thái Bình: 3–5 trang bản vẽ (mặt cắt dầm hộp giữa nhịp và đỉnh trụ, mặt cắt dọc, trụ T12–T13) | Thư mục "2021 - 05 - Kiểm định cầu Lạng Am" | Dựng lại mô hình, đưa vào bài làm cầu thứ hai |
| 4 | Cầu Mây: mô hình MIDAS (.mcb) trong file rar thiết kế 151 MB | Thư mục "Cầu Mây gửi Thái Sơn" | Nhận dạng độ cứng trụ, chốt chỉ số tại điểm N8 |
| Không cần | Ảnh hiện trường, các bản zip trùng (files-final*, ES_FINAL_BUNDLE…), bản vẽ dwg | – | – |

## Lưu trên GitHub
- File sau khi ghép ≤ 50 MB: lưu bình thường.
- File lớn hơn: lưu bằng Git LFS (có sẵn trên máy chủ). Nếu đẩy LFS không được, giữ dạng các phần đã chia, kèm checksum.
- Mỗi lần chuyển đều ghi nguồn (ID Drive), kích thước và SHA-256 vào `data/raw/MANIFEST.md`.
