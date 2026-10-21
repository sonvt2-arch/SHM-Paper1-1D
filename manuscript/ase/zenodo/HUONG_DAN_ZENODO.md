# Hướng dẫn tải gói mã và dữ liệu lên Zenodo (KHÔNG nộp tệp này cho tạp chí)

Tệp tải lên: `BlindSpots_InfluenceAreaWIM_code_data_v1.0.zip` (khoảng 14 MB, 221 mục; cùng nội dung với `word/scripts.zip` của gói nộp ASE).
SHA-256: `62ca77e083043dc2e5f10d5ce5f703a5e09db6099f251e8e9266428917327abb`

## Các bước

1. Đăng nhập https://zenodo.org (có thể dùng ORCID hoặc GitHub), bấm **New upload**.
2. Kéo thả tệp zip ở trên vào ô **Files**.
3. Ở mục **Digital Object Identifier**, chọn "No" (chưa có DOI) rồi bấm **Get a DOI now!** (Reserve DOI). Zenodo hiện DOI dạng `10.5281/zenodo.NNNNNNN`. Gửi em DOI này; em điền vào bài và thư, dựng lại tệp Word.
4. Điền các ô theo bảng dưới, bấm **Save draft**.
5. Sau khi em dựng lại bài có DOI, thầy bấm **Publish** trên Zenodo, rồi mới nộp ASE (để link DOI hoạt động khi biên tập viên bấm vào). Sau khi Publish, tệp không sửa được, chỉ tạo được phiên bản mới.

Link của bản lưu sẽ là `https://doi.org/10.5281/zenodo.NNNNNNN` (và `https://zenodo.org/records/NNNNNNN`).

## Nội dung các ô (dán nguyên văn)

| Ô | Nội dung |
|---|---|
| Resource type | Dataset |
| Title | Code and data for: Blind spots and sensor placement for influence-area weigh-in-motion on continuous girders |
| Publication date | ngày bấm Publish |
| Creators | 1. Nguyen, Quoc-Bao; Affiliation: Hanoi University of Civil Engineering; ORCID: 0000-0003-4406-2476. 2. Vu, Thai-Son; Affiliation: Hanoi University of Civil Engineering; ORCID: 0009-0005-2491-6018; role: contact person |
| Description | xem khối dưới |
| Licenses | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| Keywords | bridge weigh-in-motion; influence line; continuous girder; sensor placement; observability; identifiability; structural health monitoring |
| Version | 1.0 |
| Language | English |
| Related works | "Is derived from": `10.7294/26880898.v1` (DOI; NOR-BWIM dataset, figshare). "Is supplement to": để trống lúc này; khi bài được nhận, thêm DOI của bài (Advances in Structural Engineering) |
| Funding | để trống (bài không có tài trợ riêng) |
| Access | Public (Open) |

### Description

```
Scripts, console logs and derived data behind the article "Blind spots and sensor placement for influence-area weigh-in-motion on continuous girders" (Quoc-Bao Nguyen and Thai-Son Vu) and its Supplementary Material.

Contents:
- closed forms of the blind loci of five channel types on prismatic two- and three-span girders, with their finite element verification;
- the multi-channel placement study and Monte Carlo simulation;
- the identifiability analysis of the in-service three-span box girder (Mây Bridge), with the processed acceptance-test data;
- the processing of the public NOR-BWIM field records;
- the laboratory evaluation of the influence-area identity.

README.md maps every figure and table of the article and the Supplementary Material to a script and a log file; run_all.sh --all reruns the analyses. The raw NOR-BWIM records are not redistributed; they are available under CC0 at https://doi.org/10.7294/26880898.v1. Python 3 with numpy, scipy, sympy, pandas and matplotlib (requirements.txt).
```

## Sau khi có DOI

Em sửa hai chỗ đang để `[NEED VALUE]`:
- bài, mục Data availability: "... and archived on Zenodo (https://doi.org/[NEED VALUE]) ...";
- thư gửi tạp chí, đoạn Data availability.
Sau đó dựng lại, kiểm số, rồi thầy Publish Zenodo và nộp ASE.


**21/10:** DOI đã giữ chỗ: 10.5281/zenodo.23535533 (https://doi.org/10.5281/zenodo.23535533). Đã điền vào bài và thư. Còn bước Publish.
