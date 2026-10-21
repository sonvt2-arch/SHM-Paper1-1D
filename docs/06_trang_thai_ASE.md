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
11. **20/10, Cổng 4** (4 BTV + tổng biên tập mô phỏng; `docs/editors_v4/gate4_ase/00_tong_hop.md`): vòng 1 cả 4 "sửa rồi gửi"; sửa theo ý thầy (đổi nhan đề thành "Blind loci and sensor layout for influence-area bridge weigh-in-motion on continuous girders", nêu 6.6 và 2.4 song song, gói dễ đọc, bảng S3 ngưỡng, S16 vị trí trục, nguồn 1.75 %); vòng 2 cả 4 "gửi phản biện". Sau vòng 2: ghép cặp "6.6 against 1.5 / 2.4 against 1.1", Bảng S13 thêm C7, thu hẹp phạm vi câu cuối tóm tắt và mục 6. Khoảng 11.995 từ quy đổi (sát trần), tóm tắt khoảng 162 từ.
12. **20/10, hostile audit lần 2** (8 vai; `docs/editors_v4/hostile_audit_v2/00_tong_hop.md`): 9 lỗi chặn đã sửa (điểm mù độ võng ở nhịp giữa dầm ba nhịp gần bằng nhau, chú thích Hình 6 và 3, phạm vi tóm tắt và đóng góp (ii), hai lỗi làm tròn, PDF lỗi ký tự); theo ý thầy: 6.6 ghi "base model" kèm dải biến thể 2.6–16/1.3–1.6, thêm 5 tài liệu, Bảng 4 thành Bảng S19, gỡ cầu Thái Bình khỏi scripts.zip (log của bài không đổi số). Đọc mù lượt 11: 3 bắt buộc đã xử lý. Khoảng 11.996 từ quy đổi.
13. **20/10, chấm độ dễ đọc XII.14** (`docs/editors_v4/xii14_ase/`): D 4,5 -> 5 sau khi sửa có mục tiêu; đọc mù XII.13 lượt 12, 2 bắt buộc đã sửa. Thân bài khoảng 6.400 từ (III.19: 4.500–5.000); thầy chọn **giữ "viết đủ", nộp bản này** (khoảng 11.900 từ quy đổi, dưới trần 12.000 của ASE).

14. **21/10, theo yêu cầu của thầy:**
   - viết lại Tóm tắt (ba kết quả First/Second/Third, khoảng 190 từ), đoạn đóng góp ở Mở đầu (ba ý có tên: chỗ mù, chỗ đặt cảm biến, ảnh hưởng của độ cứng trụ; nói rõ mức đóng góp là bộ tiêu chí thiết kế, không phải thuật toán cân mới) và Kết luận (câu dẫn, năm ý có tên, câu chốt mức đóng góp; bỏ câu phụ về $N_M$ và $R$ ở ý 2). Bỏ khỏi Tóm tắt câu thí nghiệm trong phòng và câu thiết bị đo nghiêng trụ (vẫn có ở Mở đầu và Kết luận 3). Không thêm số mới (kiem_khoa đạt);
   - đổi nhan đề thành "Blind spots and sensor placement for influence-area weigh-in-motion on continuous girders" (bài, Supplementary, thư, graphical abstract, README);
   - sửa các mục nhẹ của hostile audit lần 2: Bảng S1 thêm ký hiệu; S3 ghi dải 2–160 m và định nghĩa entry shift; PDF in đứng chỉ số chữ (postprocess.py thêm m:nor); vẽ lại Hình 1, 2, S8, S12, S16, S17 bằng font Inter, dời chú giải ở Hình 2b và S8, "fiber" ở S12; graphical abstract bỏ nhãn "(a)/(b)", đổi tiêu đề ô phải theo câu ở mục 5.2. scripts.zip thay đúng các script đó (log không đổi);
   - ngày trong thư: 21 October 2026;
   - đọc mù XII.13 lượt 13–16 (`docs/editors_v4/xii13_ase/phieu_v13.md` đến `phieu_v16.md`); lượt 16 không còn mục bắt buộc; tên cầu Gie Cục I đổi thành Giẽ theo thầy;
   - khoảng 11.975 từ quy đổi.

15. **21/10, theo yêu cầu của thầy: thêm 2 bài JSTCE-HUCE.** Danh sách hiện có 0 bài của thầy (kiem_tu_trich 0/2); các bài đã đăng của thầy không bài nào về cầu hay cân xe, bài JSTCE của thầy (vu2026jstce) không liên quan nên không trích. Thầy chọn hai bài của tác giả khác (kiểm Crossref và OpenAlex, khớp tác giả, năm, tạp chí, tập, trang, DOI): Dang, Ho và Ha (2023), chẩn đoán suy giảm độ cứng dầm qua đường ảnh hưởng chuyển vị, 17(3V): 47–65 (Mở đầu, cạnh Zhou et al. 2026); Vu, Luong, Cu, Vu và Bui (2023), TLS đo độ võng cầu, 17(4): 14–25 (mục 6, kỹ thuật không tiếp xúc). Để giữ dưới trần, cắt khoảng 80 từ lặp ý ở mục 2.1, 2.2, 2.5, 3, 4, 5.2, 6 (không mất số liệu; kiem_khoa chỉ mất một câu trỏ "Section 5.1"). 57 tài liệu, khoảng 11.983 từ quy đổi. Đọc mù lượt 17–18; lượt 18 chỉ còn mục địa chỉ (đóng theo VII.6).

16. **21/10, theo yêu cầu của thầy: thư coi như bài độc lập.** Bỏ câu liệt kê các bài ASE mà bài trích và câu khai hai bài đang phản biện ở *Structures*. Đọc mù riêng thư (lượt 19): sửa "0.9–1.3 times design" thành "times the design value" ở thư và hai chỗ trùng trong bài (Tóm tắt, Kết luận 3); địa chỉ đóng theo VII.6. Bài khoảng 11.987 từ quy đổi.

17. **21/10, hostile audit lần 3 gọn** (dấu vết AI, Crossref, soát chữ; `docs/editors_v4/hostile_audit_v3/00_tong_hop.md`): sửa lỗi ngoặc trong PDF (bỏ m:sepChr rỗng), căn trái khối địa chỉ trong thư, câu "Such criteria" thiếu tiền ngữ, chữ viết tắt tên đệm và in nghiêng trong danh mục, bố cục bảng và hình, chữ d vi phân in đứng, app.xml, dấu vết quy trình trong scripts.zip; đọc mù lượt 20: "Acknowledgments", "Declaration of conflicting interests". Khoảng 11.988 từ quy đổi. Không nộp các tệp nội bộ (submission_checklist.md, figure_map.md, word/build/, tools/).

18. **21/10, Zenodo:** gói mã và dữ liệu (CC BY 4.0) ở `manuscript/ase/zenodo/`; thầy giữ chỗ DOI 10.5281/zenodo.23535533, đã điền vào Data availability của bài và thư (kiem_khoa chỉ thêm số DOI). Khoảng 11.993 từ quy đổi. Hướng dẫn nộp: `manuscript/ase/HUONG_DAN_NOP_ASE.md`. Zenodo đã Publish (https://zenodo.org/records/23535533; md5 trùng scripts.zip). Còn: thầy xem bản Word bằng Microsoft Word, rồi nộp.

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
