# D-* Logic 테스트 ID (예정)

| ID | Layer | 요약 |
|----|-------|------|
| D-01 | entity | 행 4개 각각 합 = MagicConstant |
| D-02 | entity | 열 4개 각각 합 = MagicConstant |
| D-03 | entity | 대각선 2개 각각 합 = MagicConstant |
| D-04 | entity | 10선 전부 만족 → True |
| D-05 | entity | 행·열 OK, 대각선 1개만 불일치 → False (Mom Test 회귀) |
| D-06 | entity | 빈칸 `0` 정확히 2개 검증 |
| D-07 | entity | `1~16` 중복·범위 밖 거부 |
| D-08 | control | entity 조합 유스케이스 — 10선 판정 파이프라인 |
| D-09 | control | 부분 마방진 입력 → `[r1,c1,n1,r2,c2,n2]` 조합 (Logic, Mock 금지) |

파일명 예: `tests/entity/test_d_row_sum.py` (함수·주석에 `D-01` 명시).
