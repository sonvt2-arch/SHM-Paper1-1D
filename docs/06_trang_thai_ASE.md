# Trạng thái bản nộp Advances in Structural Engineering (ASE)

Cập nhật: 2026-10-19. Nhánh: `claude/focused-bell-33lm0n`.

## 1. Bài báo

- **Tên:** "Observability and sensor layout for influence-area load monitoring of continuous girder bridges".
- **Tác giả:** Quoc-Bao Nguyen, Thai-Son Vu (liên hệ, sonvt2@huce.edu.vn), cùng Faculty of Bridge and Road Engineering, HUCE. Hung-Son Nguyen đã được bỏ khỏi danh sách tác giả theo yêu cầu của thầy (19/10).
- **Tạp chí:** Advances in Structural Engineering (Sage). Loại bài Original Research Article. Nộp qua Sage Track, theo đường thuê bao, không mất phí. Phản biện ẩn danh một chiều.
- **Giới hạn của ASE:** tối đa 12.000 từ quy đổi (số từ Word cộng 300 cho mỗi hình và mỗi bảng); tóm tắt khoảng 150 từ; 4–8 từ khoá; kiểu trích dẫn Sage Harvard; mục "Statements and Declarations".
- **Hiện trạng (19/10, tối):** khoảng 7.900 từ theo cách đếm của Word, 7 hình, 4 bảng, tức khoảng 11.200 từ quy đổi. Tóm tắt khoảng 165 từ, 6 từ khoá, 46 tài liệu tham khảo. Chính tả lối Mỹ theo Quy tắc V.1. Ngày nộp ghi trong thư: 20 October 2026.

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

8. **Tối 19/10 (phiên tiếp theo):**
   - thầy chưa mở bằng Microsoft Word; em tự xử lý: gộp chỉ số chữ đứng (ví dụ "tot", "max") thành một khối OMML (`postprocess.py`); hình cao (Hình 4, 6) giới hạn cao 12 cm (`prep_md.py`), bản PDF từ 28 xuống 26 trang;
   - III.19: thầy chọn **"viết đủ"**, giữ độ dài hiện tại. Cổng đo chỉ để báo cáo: `kiem_de_doc.py` FAIL (5.985 từ tính từ Abstract tới hết Conclusions; 41,9 số/1.000 từ; 19 đoạn quá 4 số; 21 chỗ trỏ phụ lục); `kiem_bao_toan_so.py` so v4.4 với bài và Supplementary: phần thiếu chỉ là số trích dẫn kiểu [n], DOI của các bài đã bỏ và địa chỉ, không mất số liệu;
   - thêm 4 bài ASE: Hao et al. (2019), Zuo et al. (2019), Lin et al. (2023; online 2022), Wang et al. (2026; online 2025). Đã kiểm ba nguồn: Crossref, OpenAlex, Semantic Scholar, khớp tên bài, tạp chí, tập, trang, DOI. Semantic Scholar ghi tên Zuo là "Xiaoqiu", lệch với hai nguồn kia ("Xiao-Han"); giữ theo Crossref, là dữ liệu của nhà xuất bản. Năm ghi theo số tạp chí in. Mỗi bài một vế câu ở Introduction, viết theo tóm tắt; thư gửi tạp chí nhắc thêm bốn bài;
   - tóm tắt rút từ 184 xuống khoảng 165 từ; giữ đủ số liệu, giữ rào "vary too little in weight to test weight discrimination";
   - đọc mù XII.13 lượt 5–8 (`docs/editors_v4/xii13_ase/00_bao_cao.md`), sửa hết mục bắt buộc, trừ địa chỉ không dấu (đóng theo VII.6).
9. **Tối 19/10, theo yêu cầu của thầy:** "Cầu Mây" đổi thành "Mây Bridge" trong bài, Supplementary và thư; "at Cầu Mây" thành "at the Mây Bridge". Năm hình có chữ trong ảnh được vẽ lại bằng chính script (chỉ đổi nhãn, số liệu giữ nguyên; log Monte Carlo khớp): Hình 2 (`code/analysis/schm_figures.py`), Hình 3 và S2 (`code/theory2/gc_figures.py`), S5 và S6 (`code/theory2/multisensor_core.py`, `multisensor_figures.py`). Graphical abstract dựng lại. Phần chữ trong hình theo font Inter, cần `MATPLOTLIBRC` có `font.sans-serif: Inter`. Thay đổi nằm sau lượt đọc mù cuối; kiem_khoa đạt.
10. **Tối 19/10, hostile reviewer audit** (9 tác nhân; `docs/editors_v4/hostile_audit/00_tong_hop.md`): sửa mức khẳng định theo quyết định của thầy, thêm 4 tài liệu kinh điển (Elfving 1952, Udwadia 1994, Papadimitriou 2004, Katafygiotis & Beck 1998; danh mục 50 bài), sửa 3 mục danh mục theo Crossref, sửa 4 con số sai và nhiều lỗi nhỏ, vẽ lại 19 hình + graphical abstract, đánh số lại hình/bảng Supplementary, đóng gói lại scripts.zip sạch, CRediT thêm Investigation và Data curation cho Q.-B. Nguyen. Phát hiện PDF mất công thức do máy thiếu libreoffice-math; đã cài, build_docx.sh nay chặn lỗi này. Tóm tắt 184 từ; khoảng 8.300 từ Word, khoảng 11.600 từ quy đổi.

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

1. **Thầy kiểm bằng Microsoft Word thật** (V.5) trước khi bấm nộp. Em đã gộp chỉ số chữ đứng và giới hạn chiều cao hình, nhưng vẫn mới xem bằng LibreOffice; còn khoảng 1/3 trang trống trước Hình 4 và Hình 6.
2. **Nộp ngày 20/10/2026** trên Sage Track (xem `manuscript/ase/submission_checklist.md`).
3. Chưa chấm độ dễ đọc XII.14 (chỉ để báo cáo; thầy chọn "viết đủ").
4. **Sau khi nộp:** theo dõi phản hồi; nếu bị trả, phương án dự phòng là JBE hoặc SIE (xem bảng so sánh).
