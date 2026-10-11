const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  AlignmentType, HeadingLevel, PageOrientation, ShadingType, BorderStyle, Footer, PageNumber } = require('docx');

const FONT = 'Times New Roman';
const W = [700, 5250, 4050, 1000, 3600];
const TW = W.reduce((a, b) => a + b, 0);
const border = { style: BorderStyle.SINGLE, size: 4, color: '808080' };
const borders = { top: border, bottom: border, left: border, right: border };

function p(text, opts = {}) {
  return new Paragraph({ spacing: { after: opts.after ?? 120 }, alignment: opts.align,
    children: [new TextRun({ text, font: FONT, size: opts.size ?? 24, bold: opts.bold, italics: opts.italics })] });
}
function cell(text, w, opts = {}) {
  return new TableCell({ width: { size: w, type: WidthType.DXA }, borders,
    shading: opts.fill ? { type: ShadingType.CLEAR, color: 'auto', fill: opts.fill } : undefined,
    margins: { top: 60, bottom: 60, left: 90, right: 90 },
    children: String(text).split('\n').map(t => new Paragraph({ alignment: opts.align,
      children: [new TextRun({ text: t, font: FONT, size: 21, bold: opts.bold })] })) });
}
function table(rows) {
  const head = new TableRow({ tableHeader: true, children:
    ['STT', 'Câu hỏi / tài liệu cần cung cấp', 'Dùng để làm gì trong bài báo', 'Ưu tiên', 'Trả lời / tên file gửi kèm']
      .map((h, i) => cell(h, W[i], { bold: true, fill: 'D9E2F3', align: AlignmentType.CENTER })) });
  const body = rows.map(([id, q, why, pr]) => new TableRow({ cantSplit: true, children: [
    cell(id, W[0], { align: AlignmentType.CENTER }), cell(q, W[1]), cell(why, W[2]),
    cell(pr, W[3], { align: AlignmentType.CENTER, fill: pr === 'Cao' ? 'FCE4D6' : undefined }), cell('', W[4])] }));
  return new Table({ width: { size: TW, type: WidthType.DXA }, columnWidths: W, rows: [head, ...body] });
}
function h1(t) { return new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 240, after: 120 },
  children: [new TextRun({ text: t, font: FONT, size: 28, bold: true })] }); }

const A = [
 ['A1', 'Số đọc thô của cả 3 lần chất tải – dỡ tải tại từng vị trí (cả 3 cấu hình: 1 tải, 2 tải, 3 tải), kể cả số đọc zero trước và sau mỗi lần.', 'Tính độ không đảm bảo loại A thay vì chỉ chặn trên bằng độ phân giải; kiểm trôi zero trong phòng thí nghiệm.', 'Cao'],
 ['A2', 'Cấp chính xác hoặc giấy hiệu chuẩn của các quả cân thép và của cân dùng để cân; khối lượng móc treo (tải chuẩn 4,143 kg đã gồm móc).', 'Mục 7.2 và bảng ngân sách sai số đang để trống [NEED VALUE].', 'Cao'],
 ['A3', 'Xác nhận thứ tự tải trong cấu hình 3 tải: tải 2550 g đi đầu, rồi khoảng cách 250 mm hay 500 mm trước? (bản cũ có hai cách đọc khác nhau).', 'Tính lại đường độ võng lý thuyết của cấu hình 3 tải; một cách đọc cho sai số 0,03 mm, cách kia 0,55 mm.', 'Cao'],
 ['A4', 'File hình gốc (≥ 300 dpi hoặc vector) của: sơ đồ dầm và bố trí đo, ảnh giàn thử, đường ảnh hưởng đo, hình minh hoạ bất biến, đường hiệu chuẩn, sơ đồ quy trình.', 'Hình 1, 2, 4, 5, 6, 10 của bản nộp SCHM (repo chưa có).', 'Cao'],
 ['A5', 'Giàn thử và số liệu này có được dùng trong hai bài đang nộp ở Structures không? Nếu có, ghi tên bài.', 'SCHM kiểm trùng lặp bằng iThenticate; nếu dùng chung phải nêu trong thư gửi biên tập.', 'Cao'],
 ['A6', 'Kích thước đo thực tế của ống (bề rộng, chiều dày thành tại nhiều điểm); E đo hay lấy theo mác thép?', 'Ước lượng sai số EI cho phương pháp BPM.', 'Trung bình'],
 ['A7', 'Chiều dài dầm 5400 mm so với 2 × 2500 mm: hai đầu thừa bao nhiêu? Gối giữa có kẹp chống nhổ không? Có thấy gối C bị nhấc lên khi tải ở nhịp AB không?', 'Mô tả điều kiện biên; phản biện đã hỏi về phần thừa và hiện tượng nhổ gối.', 'Trung bình'],
 ['A8', 'LVDT: model, ngày hiệu chuẩn, sai số tuyến tính; cấu hình data logger TDS-303; nhiệt độ phòng lúc thí nghiệm.', 'Hoàn thiện mô tả thiết bị và ngân sách sai số.', 'Thấp'],
 ['A9', 'Bản giải nén các script trong thư mục Drive "Python" (bản dùng cho JCSHM: Monte Carlo, tải di động, kiểm ký hiệu, sai số cầu phương) hoặc file SupplementaryMaterial_JCSHM.zip chia nhỏ ≤ 2 MB.', 'Bài ghi là nộp kèm các script này làm tài liệu bổ sung.', 'Cao'],
];
const B = [
 ['B1', 'Mô hình MIDAS (.mcb) của cầu chính 55 + 90 + 55 m. Nếu không có: bảng đặc trưng mặt cắt dầm hộp theo chiều dài (A, I, trục trung hoà).', 'Kiểm lại mô hình dầm thay đổi tiết diện đang tự dựng.', 'Cao'],
 ['B2', 'Kích thước hai trụ chính ở hai đầu nhịp N7 (tiết diện thân, chiều cao từ đỉnh móng), kiểu liên kết trụ – dầm (liền khối hay gối), loại móng.', 'Độ cứng trụ quyết định chỉ số quan sát được ở nhịp biên: hiện dao động 0,18–0,48 vì chưa biết độ cứng trụ.', 'Cao'],
 ['B3', 'Số đọc độ võng tại TẤT CẢ các điểm đo trong MỖI sơ đồ xếp tải, đặc biệt võng giữa nhịp N8 khi đoàn xe ở N7 và ngược lại.', 'Đo trực tiếp phần đóng góp âm của nhịp kề; tách độ cứng dầm và độ cứng trụ.', 'Cao'],
 ['B4', 'Phiếu cân từng xe thử (tổng trọng lượng và tải trục).', 'Hiện dùng tải danh nghĩa 25 t; có phiếu cân thì tính lại các bảng 6 và 8.', 'Cao'],
 ['B5', 'Toạ độ thực tế của từng trục xe trong mỗi sơ đồ tĩnh (hiện lấy theo đề cương).', 'Tính độ võng dự báo tại điểm đo.', 'Trung bình'],
 ['B6', 'Thiết bị đo võng nhịp chính (thuỷ bình, toàn đạc hay đầu đo), độ chính xác; thời gian giữ tải; độ võng dư sau dỡ tải; nhiệt độ lúc đo.', 'Đánh giá độ tin cậy của số đo và độ tuyến tính.', 'Trung bình'],
 ['B7', 'File thô máy SDA-830C các lượt xe chạy (độ võng hoặc gia tốc theo thời gian), tần số lấy mẫu, vị trí đầu đo, xe chạy, vận tốc, làn.', 'Kiểm trực tiếp phương pháp tích phân trên cầu liên tục: bằng chứng mạnh nhất còn thiếu của bài.', 'Cao'],
 ['B8', 'Có được phép công bố số liệu thử tải trong bài báo không? Ghi đúng tên chủ đầu tư hay ẩn danh? Cảm ơn những ai?', 'Mục Data Availability và Acknowledgments.', 'Cao'],
 ['B9', 'Đơn vị thực hiện thử tải là Công ty TNHH Tư vấn Đại học Xây dựng. Có tác giả nào làm việc, tư vấn hoặc có lợi ích tại đơn vị này không?', 'Mục Conflicts of Interest.', 'Cao'],
];
const C = [
 ['C1', '3–5 trang bản vẽ xuất PDF (< 2 MB): mặt cắt ngang dầm hộp tại giữa nhịp và tại đỉnh trụ; mặt cắt dọc (quy luật thay đổi chiều cao); bản vẽ trụ T12, T13.', 'Dựng lại mô hình; hiện thiếu chiều dày bản đáy và kích thước trụ nên mô hình lệch tới 22%.', 'Cao'],
 ['C2', 'Mô hình MIDAS hoặc giá trị I, A dầm hộp tại giữa nhịp và đỉnh trụ.', 'Như C1.', 'Cao'],
 ['C3', 'Số đọc võng tại tất cả điểm đo trong mỗi sơ đồ (kể cả nhịp không đặt tải).', 'Đối chứng với Cầu Mây: Thái Bình có β = 1,5, dưới ngưỡng gần mù, còn Cầu Mây β = 1,636.', 'Cao'],
 ['C4', 'Xe nào thuộc sơ đồ nào; phiếu cân và tải trục 10 xe; toạ độ trục xe từng sơ đồ.', 'Tính độ võng dự báo.', 'Trung bình'],
 ['C5', 'File thô SDA-830C lượt xe chạy 30–40 km/h, kèm vị trí đầu đo, vận tốc, làn.', 'Như B7.', 'Trung bình'],
 ['C6', 'Quyền công bố số liệu.', 'Data Availability.', 'Cao'],
];
const D = [
 ['D1', 'Kênh "Vong" trong file "Vong dong" là độ võng đo trực tiếp (mm) hay tích phân từ gia tốc? Đã hiệu chuẩn chưa?', 'Biên độ động (7,8–10,8 mm) lớn hơn võng tĩnh dưới 3 xe (3,6 mm): nghi chưa hiệu chuẩn.', 'Cao'],
 ['D2', 'Vì sao chuỗi đã xử lý được nhân hệ số khác nhau theo nhịp (Gie Cục: 1,00 / 3,25 / 5,15; Phương Độ: 0,67 / 1,34)? Phương Độ N1 có chỉnh tay (nhân 0,678 và bậc −1,56 mm tại 7,19 s) – lý do?', 'Không giải thích được thì không so sánh được giữa các nhịp.', 'Cao'],
 ['D3', 'Xe chạy lượt động: loại xe, tổng trọng lượng, tải trục, vận tốc thực, làn; đầu đo đặt dưới dầm nào. (Vận tốc suy từ bản ghi Gie Cục là 47–62 km/h, báo cáo ghi 30–40 km/h.)', 'Kiểm tải tuyệt đối từ tích phân độ võng trên cầu thật.', 'Cao'],
 ['D4', 'File gia tốc thô của Phương Độ N1 (N1.XLS) và đơn vị của file DAT0034 (N2).', 'Kiểm thuỳ dương +2,8 mm ở N1 là thật hay do xử lý.', 'Trung bình'],
 ['D5', 'Mô hình MIDAS hoặc đặc trưng tiết diện liên hợp đã dùng; hệ số phân bố ngang.', 'Tính C_m cho dầm được đo.', 'Thấp'],
 ['D6', 'Quyền công bố số liệu hai cầu.', 'Data Availability.', 'Trung bình'],
];
const E = [
 ['E1', 'Phiếu cân và tải trục của cả 12 xe (báo cáo mới ghi 6 xe).', 'Chỉ cần nếu dùng cầu này trong bài sau.', 'Thấp'],
 ['E2', 'File thô SDA-830C các lượt xe chạy; mô hình MIDAS (MotDN.mcb).', 'Như trên.', 'Thấp'],
];

const children = [
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 },
    children: [new TextRun({ text: 'DANH MỤC CÂU HỎI BỔ SUNG SỐ LIỆU', font: FONT, size: 32, bold: true })] }),
  p('Thí nghiệm phòng lab và số liệu thử tải các cầu – phục vụ bài báo "Load observability of continuous girder bridges from a single deflection channel"', { align: AlignmentType.CENTER, italics: true }),
  p('Người gửi: [NEED VALUE]          Ngày gửi: [NEED VALUE]          Đề nghị trả lời trước: [NEED VALUE]', { align: AlignmentType.CENTER }),
  p('Cách trả lời: ghi trực tiếp vào cột cuối, hoặc ghi tên file gửi kèm. File lớn hơn 2 MB xin nén và chia phần bằng 7-Zip (định dạng zip, mức nén Store, Split to volumes = 2M) rồi để trên Google Drive. Mục ưu tiên "Cao" là cần để nộp bài; "Trung bình" làm bài mạnh hơn; "Thấp" để dùng sau. Nếu không có số liệu, xin ghi "không có" để nhóm tác giả không chờ.'),
  h1('Phần A. Thí nghiệm phòng lab (dầm thép hai nhịp 2 × 2500 mm)'),
  p('Người trả lời: người trực tiếp làm thí nghiệm.', { italics: true }), table(A),
  h1('Phần B. Cầu Mây (ĐT389, Hải Dương) – dầm hộp liên tục 55 + 90 + 55 m, thử tải 6/2020'),
  p('Người trả lời: đơn vị lập báo cáo thử tải.', { italics: true }), table(B),
  h1('Phần C. Cầu Thái Bình (thư mục "Lạng Am") – dầm hộp liên tục 42 + 63 + 42 m, thử tải 4/2023'),
  table(C),
  h1('Phần D. Cầu Gie Cục I (2018) và cầu Phương Độ (2018) – dầm giản đơn, bản ghi động'),
  table(D),
  h1('Phần E. Cầu qua sông Sặt (2024) – không bắt buộc'),
  table(E),
  p(''),
  p('Xin cảm ơn anh/chị. Số liệu chỉ dùng cho mục đích nghiên cứu, ghi rõ nguồn; bản thảo sẽ được gửi để anh/chị xem trước khi nộp.', { italics: true }),
];

const doc = new Document({
  styles: { default: { document: { run: { font: FONT, size: 24 } } } },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838, orientation: PageOrientation.LANDSCAPE },
      margin: { top: 1000, bottom: 1000, left: 1100, right: 1100 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ font: FONT, size: 18, children: ['Trang ', PageNumber.CURRENT, ' / ', PageNumber.TOTAL_PAGES] })] })] }) },
    children }],
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(process.argv[2], b); console.log('ok'); });
