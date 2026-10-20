# Kiểm tái lập scripts.zip (20/10/2026)

Cách làm: giải nén scripts.zip vào thư mục trống; nối data/public (NOR-BWIM, tải từ figshare 26880898) và data/bridges từ repo;
chạy `bash code/supplementary/run_all.sh --with-analysis --all` (khoảng 45 phút CPU); so mọi log, CSV, npz với bản đóng gói.

Kết quả:
- Mọi log và tệp kết quả trùng từng byte, trừ: đường dẫn tuyệt đối (thư mục chạy), thời gian chạy, nhãn "Cầu Mây" -> "Mây Bridge" ở
  multisensor_mc.log và multisensor_placement.log (log đóng gói tạo trước khi đổi tên), khoảng trắng của một nhãn ở s03, một dòng trống cuối
  ở ba log analysis. Không có khác biệt nào về số (script so số từng dòng: 0 khác biệt).
- ident_freq_curves.npz lệch tối đa 9e-11 Hz (sai số làm tròn của bộ giải).
- Lỗi: code/v4/figS1_lab_il.py (Hình S8) đọc manuscript/v4/supplementary_material.md, không có trong gói. Đã sửa: đọc
  code/v4/lab_single_load_influence_line.csv (21 điểm của Bảng S4); hình mới trùng từng pixel với Hình S8 đã nộp.
- Theo quyết định của thầy, gói kèm data/bridges/cau-may (3 CSV đã làm sạch: bỏ biển số xe, ID Drive, tên tệp nguồn, [NEED VALUE];
  nguồn lưu ở manuscript/ase/data_release/). Chạy lại ident_freq.py chỉ với dữ liệu trong gói: log trùng từng byte.
- Không kèm: bản ghi thô NOR-BWIM (công khai, theo DOI) và bản ghi động Gie Cục I, Phương Độ (Hình S16–S17); README ghi rõ.
