# Hostile audit lần 3, gọn (21/10/2026) — tổng hợp và cách xử lý

Ba vai, mỗi vai một tác nhân mới: 1 dấu vết AI (Sonnet), 2 trích dẫn và Crossref (Sonnet), 3 soát chữ (Opus). Biên bản: `1_ai_artifacts.md`, `2_citations.md`, `3_proofreading.md`.

## Lỗi chặn và cách sửa
- **Ngoặc trong PDF** (vai 1 và 3): LibreOffice vẽ "]" và "|" co giãn thành ")" (Eq. (2), (9), (13), $B_m$, $\bar M_\mathrm{main}$, $|N_w|$, Supplementary S2, S3, S8, S10). Nguyên nhân: thẻ `m:sepChr` rỗng do pandoc ghi. `postprocess.py` bỏ thẻ này; Word hiển thị như cũ. Đã kiểm bằng mắt.
- **Thư: khối địa chỉ bị dàn đều** (vai 3): `postprocess.py` căn trái đoạn có ngắt dòng tay.
- **"Such criteria" không có tiền ngữ** ở Mở đầu (vai 3): sửa thành "Criteria that locate these zeros are needed ... This paper supplies them."
- **Thư mục gói nộp có tệp nội bộ** (vai 1): không sửa; chỉ nộp các tệp trong word/ (docx, pdf), figures/ và scripts.zip; KHÔNG nộp submission_checklist.md, figure_map.md, word/build/, tools/.

## Nên sửa đã làm
- Trích dẫn: Zhu JH, Wang C, Qi TY, Zhou ZS; Kawamura SI (theo Crossref); in nghiêng tên 4 tài liệu không phải bài báo (Al-Qadi, CEN, luận án Moghadam, bộ dữ liệu NOR-BWIM).
- Bố cục PDF: tiêu đề bảng ký hiệu giữ cùng bảng; chú thích hình và bảng không tách trang; bảng ngắn (S13, S15, S18) và chú thích của bảng nằm cùng trang.
- Chữ "d" vi phân in đứng trong PDF (m:nor cho mọi chữ sty p).
- Mục 6: tách câu Vu et al. (2023) khỏi câu "therefore".
- Bảng S1: $\nu = 1.5\bar M_\mathrm{main}$ (pinned piers), gọi là deflection coefficient (đã kiểm đại số).
- S4: câu trỏ vòng về mục 5.3 sửa thành "under the noise model above".
- S6: tỉ số 1.010 ghi rõ cả hai tích phân theo quy tắc hình thang.
- Eq. (S2) dùng phân số đứng; Bảng 1 viết $\zeta_0 = (1-\sqrt{1-\mu/\beta^2})/2$.
- S11: bỏ câu khẳng định "every equation ... checked independently"; giữ "closed forms are checked against FE evaluations (logs in the archive)".
- Thư: "derived data behind the figures and tables" (không còn "every", vì dữ liệu thô S16–S17 không kèm); ký tên "on behalf of both authors".
- docx: app.xml cũ của pandoc (Word 12.0, 83 từ, 1 trang) thay bằng phần rỗng.
- scripts.zip: bỏ đường dẫn tuyệt đối trong fieldplan_compute.log; làm sạch chú thích mã còn dấu vết quy trình (beam_theory.py, ident_static.py, wp3_sections.py, graphical_abstract.py, README).
- "(main-text Table 2)"; "standard deviation (SD)" ở lần dùng đầu trong S7; dấu cách không ngắt trong "55 + 90 + 55 m".

## Chưa làm (nhẹ, để thầy quyết nếu muốn)
- "Five channel types" trong khi Bảng 1 có 6 dòng (hai loại phản lực tính là một).
- Hình 7b không được trích trong thân bài; Hình 5b trích trước 5a.
- Số 0.87 → 0.18, 167 µrad, 10.6 % trỏ về S8/S4 nhưng chỉ có trong log (README đã nối với ident_fisher.log).
- 12.4 s ở S10 tính lại khoảng 12.3 s (không đổi số khi chưa có nguồn).
- Lối viết "X, not Y" lặp; câu dẫn "The paper gives three main results"; vài chi tiết hình (Hình 4 gạch nối trong chú giải, S15 hai nhãn "A", S13 thiếu đơn vị trục, S17 số lẻ không đều, Hình 6 hai nhãn sát nhau).
- Tên tạp chí HUCE viết gọn; số tập Métodos y Materiales; trang cuối OBrien 2009.
