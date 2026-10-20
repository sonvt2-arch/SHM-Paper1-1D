# Hostile reviewer audit lần 2 (20/10/2026, bản sau Cổng 4) — tổng hợp và cách xử lý

Phân vai: 1 phương trình, 2 con số, 3 bảng/hình, 4 tính mới, 6 tóm tắt–kết luận, 8 soát chữ (Opus); 5 trích dẫn/Crossref, 7 dấu vết AI (Sonnet).
Tổng: 9 chặn, 40 nên sửa, 64 nhẹ. Quyết định của thầy: giữ 6.6 kèm "base model" và dải biến thể; thêm 5 tài liệu; chuyển Bảng 4 sang Bảng S19; gỡ cầu Thái Bình khỏi scripts.zip.

## Lỗi chặn và cách sửa
- PDF có ký tự lỗi "¿" (A⁺, ξ*, |·|) và gạch trên M̄ thành dấu sắc: postprocess.py chuyển chỉ số chỉ có toán tử và thanh đứng thành chữ thường, gạch trên U+203E -> U+00AF. Docx vốn đúng.
- Mục 2.2: "deflection gauge cannot be blind on equal spans" sai cho nhịp giữa dầm ba nhịp: đã kiểm tay (ν = 1 + ζ − ζ², ba nhịp bằng nhau ν = 1.2, ζ = 0.276, |N_w| ≤ 0.10); sửa câu, Bảng 1, Kết luận 1, S2. "longer or stiffer" -> "longer (λ > 1, β² > 3/2)".
- Chú thích Hình 6 "(c) L is the main span" sai (gc_figures.py chuẩn hoá theo nhịp chứa điểm) -> sửa; Hình 3: bước nhảy của N_V là phản lực gối.
- Câu cuối tóm tắt: "a model-based side-span constant needs identified pier stiffness"; đóng góp (ii) thêm "on one day".
- Làm tròn: Bảng S13 1.9 -> 1.8, Bảng S13/S17 5.0 -> 4.9 (×10⁻⁴).

## Nên sửa đã làm
6.6 ghi "base model", mục 5.2 thêm dải biến thể 2.6–16 (N8) và 1.3–1.6 (N7) từ ident_static.log; 5 tài liệu mới (Crossref): Hong 2016, Wu 2018, Sherman–Morrison 1950, Pukelsheim 2006, Yamaguchi 2009 (ASE); viết nhẹ câu khoảng trống, câu Zhou 2025, "referred to below as the Möbius law"; danh mục in nghiêng theo Sage Harvard, Ghali 6th ed. (theo Crossref);
Bảng 3, S15 dòng trụ khớp/ngàm dùng mô hình cơ sở L_v = 44 m kèm R (gc_results.log; khớp 14.0 và 0.59 ở S8); Bảng S9 điền tương quan ngày 1 (0.42, 0.30; v4.log);
bỏ "S14" ở 5.1; "within 1 %"; 24.8 % "for a 220 m record"; cận Cramér–Rao trỏ S8 thay Hình 7b; 543 -> 542; biên 12–27 % (TOST 11.8/26.7 %); chú thích Hình 4 (cùng gauge chưa lọc, lọc 0.5 Hz, vạch vào/ra); Bảng S2 và Hình 2a: ξ* là cực đại dương, nhánh âm lớn hơn từ β = 1.639 (đã tính);
θ6, θ7 gắn với nhãn trụ mục 5; S4 nói rõ δ0 là độ lệch chuẩn của offset ngẫu nhiên; Data availability nói đúng phần có và không có; thư: điều kiện của câu tiltmeter, "3 numbered tables and a table of symbols", "Sincerely"; đánh số (S1), (S2) trong Supplementary; khoảng trắng không ngắt giữa số và đơn vị.
Số từ quy đổi khoảng 11.991 (7 hình + 3 bảng + bảng ký hiệu).

## Chưa làm
Bảng S1 thiếu một số ký hiệu (A⁻, C̄, ν, ξ0, μ_crit ...); chỉ số "tot, ref" in nghiêng trong PDF LibreOffice; vài mục nhẹ về hình (chữ chồng ở Hình 2b, S8, nhãn "(a)" thừa ở graphical abstract, font không đồng nhất); M3 S3 "factor 1.5–6.6" thiếu trường hợp 8.1.
