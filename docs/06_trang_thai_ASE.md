# Trạng thái bản nộp Advances in Structural Engineering (ASE)

Cập nhật: 2026-10-19. Nhánh: `claude/focused-bell-33lm0n`.

## 1. Bài báo

- **Tên:** "Observability and sensor layout for influence-area load monitoring of continuous girder bridges".
- **Tác giả:** Quoc-Bao Nguyen, Thai-Son Vu (liên hệ, sonvt2@huce.edu.vn), cùng Faculty of Bridge and Road Engineering, HUCE. Hung-Son Nguyen đã được bỏ khỏi danh sách tác giả theo yêu cầu của thầy (19/10).
- **Tạp chí:** Advances in Structural Engineering (Sage). Loại bài Original Research Article. Nộp qua Sage Track, theo đường thuê bao, không mất phí. Phản biện ẩn danh một chiều.
- **Giới hạn của ASE:** tối đa 12.000 từ quy đổi (số từ Word cộng 300 cho mỗi hình và mỗi bảng); tóm tắt khoảng 150 từ; 4–8 từ khoá; kiểu trích dẫn Sage Harvard; mục "Statements and Declarations".
- **Hiện trạng:** khoảng 7.700 từ theo cách đếm của Word, 7 hình, 4 bảng, tức khoảng 11.000 từ quy đổi. Tóm tắt 184 từ, 6 từ khoá, 42 tài liệu tham khảo. Chính tả lối Mỹ theo Quy tắc V.1.

## 2. Lịch sử quyết định

1. Bài bị trả không qua phản biện ở Engineering Structures và JCSHM. Bản v4.4 chuẩn bị cho SCHM nằm ở `manuscript/v4/`.
2. Bốn biên tập viên mô phỏng đọc v4.4; ba người trả bài trước phản biện (`docs/editors_v4/editors/00_TONG_HOP_V4.md`). Lý do chung là không có thí nghiệm nào kiểm chứng quỹ tích mù. Thầy giữ nguyên quyết định không làm thêm thí nghiệm.
3. So sánh 5 tạp chí bằng tổng biên tập mô phỏng (`docs/editors_v4/journals/`):

   | Tạp chí | Gửi phản biện sau khi đổi khung | Được nhận tổng thể |
   |---|---|---|
   | JBE | ~55 % | ~30 % |
   | ASE | ~60 % | ~25–30 % |
   | SIE | ~60 % | ~27 % |
   | SHM (SAGE) | ~55 % | ~28 % |
   | Measurement | ~45–50 % | ~20 % |

   Thầy chọn ASE.
4. Trước khi đổi khung, các lỗi biên tập viên chỉ ra ở v4.4 đã được sửa:
   - sai số chuẩn của trung bình (SEM) so với độ lệch chuẩn (SD);
   - RMS bị ghi là MAE;
   - điều kiện tần số của giới hạn Cramér–Rao;
   - hệ số giữa hai cách ước lượng tốc độ (1,139);
   - ghi chú về kiểm định bội;
   - công thức mômen đầu nhịp chính;
   - nhãn β trong Bảng A.1;
   - nhãn Hình 7;
   - lệnh chạy lại toàn bộ phân tích `run_all.sh --v4`.
5. Đổi khung bài thành "khả quan sát và bố trí cảm biến", gồm ba đóng góp:
   - danh mục quỹ tích mù dạng giải tích;
   - quy tắc đặt cảm biến, kèm bài học hiện trường về ma trận hiệp phương sai lúc không có xe;
   - luật Möbius và tính khả nhận dạng ở Cầu Mây.

   Bài rút từ khoảng 14.300 xuống khoảng 7.900 từ; phần cắt chuyển sang Supplementary (mục S1–S11, Bảng S1–S16, Hình S1–S17). Trích dẫn chuyển sang Sage Harvard bằng `manuscript/ase/tools/harvard.py`. Bảng đối chiếu số hình và bảng cũ với mới: `manuscript/ase/figure_map.md`.
6. **Kiểm tra đã chạy:**
   - đối chiếu số liệu bằng `kiem_khoa.py`: không có con số mới;
   - kiểm lỗi sau cắt (`docs/editors_v4/journals/kiem_sau_cat_ase.json`), đã sửa hết;
   - tự trích dẫn 1/2;
   - chạy lại toàn bộ mã trên bản sao: khớp log;
   - đọc mù chuẩn mực XII.13 bốn lượt (`docs/editors_v4/xii13_ase/00_bao_cao.md`), sửa hết mục bắt buộc trừ hai mục đóng theo nguồn (tên "Lobo-Aguilar" giữ như bản gốc từng bài, địa chỉ không dấu theo VII.6); mục cân nhắc thầy cho sửa hết. Theo quyết định của thầy, các chỗ sửa sau lượt 4 không chạy thêm lượt đọc.
7. **Ngày 19/10 (sau khi thầy xem bản Word):**
   - bỏ tác giả Hung-Son Nguyen; câu về bài Nguyen et al. (2024) đổi thành "One of the present authors, with co-workers";
   - khai báo AI: tiêu đề và vị trí theo Sage (nằm trong Acknowledgements), nội dung giữ nguyên theo Quy tắc VII.1;
   - trình bày Word theo V.1, V.1.1, V.2 (mục 3);
   - đổi sang lối Mỹ, giữ nguyên tên bài trong danh mục tài liệu;
   - sửa nhãn trong ảnh Hình 3 ("normalized") và Hình 7 ("misfit ratio", "gray", 300 dpi);
   - thêm graphical abstract.

## 3. Cách dựng tệp Word

```bash
bash manuscript/ase/word/build_docx.sh --pdf
```

| Tệp | Vai trò |
|---|---|
| `word/prep_md.py` | Khối tiêu đề căn giữa; đặt mỗi hình ngay sau đoạn đầu tiên nhắc tới nó; chú thích một dòng căn giữa, nhiều dòng căn đều |
| `word/prep_supp.py` | Làm như trên cho Supplementary |
| `word/make_reference.py` | Times New Roman; lề 2,5 cm; văn bản căn đều; tiêu đề căn trái; kiểm soát dòng lẻ; số trang ở chân trang |
| `word/eqnum.lua` | Phương trình trong bảng ba cột không viền; số phương trình sát lề phải |
| `word/postprocess.py` | Bảng căn giữa, chỉ kẻ ba đường ngang; cột số căn phải; lặp hàng tiêu đề; danh mục tài liệu căn trái, thụt treo; đánh số dòng |

Hình nằm ở `manuscript/ase/figures/` (Fig1–Fig7, `supplementary/FigS1–S17`, `GraphicalAbstract.png`). Graphical abstract dựng bằng `code/v4/graphical_abstract.py`.

## 4. Gói nộp (`manuscript/ase/`)

- `word/Manuscript_ASE.docx` và `.pdf`
- `word/Supplementary_Material_ASE.docx` và `.pdf`
- `word/Cover_Letter_ASE.docx`
- `figures/` (300 dpi) và `figures/GraphicalAbstract.png`
- `word/scripts.zip` (mã và log; `ASE_numbering.md` đổi số hình và bảng v4 sang số của bản ASE)
- `submission_checklist.md`

## 5. Còn chờ

1. **Thầy kiểm bằng Microsoft Word thật** (V.5). Em mới xem bản xuất PDF bằng LibreOffice. Cần kiểm chỉ số đứng (ví dụ $P_\mathrm{tot}$ phải hiện "tot" chữ đứng), vị trí hình và khoảng trắng.
2. **Khoảng trắng gần hình:** vài trang còn khoảng nửa trang trống ngay trước hình lớn, vì hình không vừa phần còn lại của trang.
3. **Ngày nộp:** điền ở dòng đầu `cover_letter_ASE.md`, rồi dựng lại gói.
4. **Tóm tắt dài 184 từ**, trong khi ASE ghi "khoảng 150 từ". Có thể rút thêm nếu thầy muốn.
5. **Bài ASE nên trích thêm:** Hao 2019, Zuo 2019, Lin 2022, Wang 2025. Chưa thêm; cần thầy đồng ý và phải kiểm từng bài từ ba nguồn (VII.4).
6. **Quy tắc v4.0 (19/10)** thêm III.19: thân bài mặc định 4.500–5.000 từ, kể một mạch, nhiều nhất ba phát hiện. Bản ASE hiện khoảng 7.700 từ, được dựng trước khi quy tắc này ra. Cần thầy quyết: giữ nguyên ("viết đủ" cho bài này), hay rút tiếp. Cũng chưa chạy `kiem_de_doc.py`, `kiem_bao_toan_so.py` và chấm độ dễ đọc XII.14.
7. **Sau khi nộp:** theo dõi phản hồi; nếu bị trả, phương án dự phòng là JBE hoặc SIE (xem bảng so sánh).
