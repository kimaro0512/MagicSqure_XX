# Golden Master — 승인 기준선 (Baseline)

> **용도:** GREEN PASS 이후 회귀·REFACTOR·신규 Test ID 추가 시 “이전에 맞았던 출력”과 비교하는 기준선.  
> **규칙:** 기준선 변경은 **의도적** GREEN/REFACTOR 완료 후에만 — assert 완화·삭제로 맞추지 않는다.

---

## GREEN PASS 게이트 (Track B · D-LOC-01)

| 단계 | 명령 | 기대 |
|------|------|------|
| 1 | `python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v` | **1 passed** |
| 2 | `python -m pytest tests/entity/test_d_loc_01.py -v` | **1 passed** |
| 3 | `python -m pytest tests/entity/ -v` | **n passed**, 0 failed |
| 4 | `python -m pytest tests/ -v --tb=short` | **전체 Green**, 0 skip/xfail |

가상환경(권장):

```cmd
cd c:\DEV\MagicSqure_XX
.\.venv\Scripts\activate.bat
pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m pytest tests/ -v --tb=short
```

---

## Golden 파일 갱신 (UPDATE_GOLDEN)

```cmd
set UPDATE_GOLDEN=1
python -m pytest tests/entity/test_d_sol_01.py::test_d_sol_01_step_a_success -v
set UPDATE_GOLDEN=
python -m pytest tests/entity/test_d_sol_01.py::test_d_sol_01_step_a_success -v
```

PowerShell: `$env:UPDATE_GOLDEN='1'; python -m pytest ...`

**포맷 (고정):**

| 종류 | 한 줄 형식 | 예 |
|------|------------|-----|
| 성공 `int[6]` | `r1 c1 n1 r2 c2 n2` (공백 구분, 1-index) | `2 2 8 3 3 9` |
| 오류 | `E00x NAME` | `E002 INVALID_BLANKS` |

헬퍼: `tests/_approval.py` — `assert_matches_golden(actual, relative)`

---

## Baseline Registry

| Test ID | Layer | API | Fixture | Golden file | Approved line |
|---------|-------|-----|---------|-------------|---------------|
| **D-LOC-01** | entity | `find_blank_coords` | `grid_g1` | — (assert) | `[(2, 2), (3, 3)]` |
| **D-SOL-01** | entity | `solve_step_a` | `grid_g1` | `tests/golden/d_sol_01_g1_step_a.approved.txt` | `2 2 8 3 3 9` |

### D-LOC-01 · `grid_g1` (conftest)

```text
[ 1,  2,  3,  4]
[ 5,  0,  7,  8]
[ 9, 10,  0, 12]
[13, 14, 15, 16]
```

빈칸 1-index: **(2, 2)**, **(3, 3)** — `BLANK_CELL`(`0`) 위치와 일치.

---

## 검증 이력

| 일자 | Phase | Test ID | pytest | 결과 | Python | 비고 |
|------|-------|---------|--------|------|--------|------|
| 2026-06-04 | GREEN | D-LOC-01 | `tests/ -v --tb=short` | **1 passed** | 3.13.13 (.venv) | assert baseline |
| 2026-06-04 | GREEN | D-SOL-01 | `test_d_sol_01_step_a_success` | **matched** | 3.13.13 (.venv) | `d_sol_01_g1_step_a.approved.txt` |

---

## 다음 Golden Master 후보 (미등재)

| Test ID | 상태 |
|---------|------|
| D-SOL-02+ | RED 대기 |
| D-LOC-02 | RED 대기 |
| D-LOC-03 | RED 대기 |
| D-01~D-09 | RED 대기 |
| U-* | RED 대기 |

기준선 추가 시 본 표에 행을 추가하고, 동일 GREEN PASS 게이트(단일 → Track → `tests/`)를 통과한 뒤 등재한다.

---

## 관련 문서

- [Report/04.MagicSquare_GREEN_DLOC01_Report.md](../Report/04.MagicSquare_GREEN_DLOC01_Report.md) — GREEN · D-LOC-01
- [Report/05.MagicSquare_GoldenMaster_DSOL01_Report.md](../Report/05.MagicSquare_GoldenMaster_DSOL01_Report.md) — Golden Master · D-SOL-01
- [Report/03.MagicSquare_RED_DLOC01_Report.md](../Report/03.MagicSquare_RED_DLOC01_Report.md) — RED 선행 보고
- [docs/RED-TODO.md](RED-TODO.md) — Dual-Track Todo
