# MagicSquare_XX — RED 단계 Todo

| 항목 | 내용 |
|------|------|
| **Phase** | RED (실패 테스트 먼저) |
| **근거** | [PRD.md](PRD.md), [.cursorrules](../.cursorrules), [reference.md](../.cursor/skills/magic-square-tdd/reference.md) |
| **상태** | 설계 확정 · `tests/`·`test_u_*`·`test_d_*` 본문 **미작성** |
| **작성일** | 2026-06-04 |

Dual-Track TDD RED 설계를 **바운더리(UI)** 와 **로직(entity/control)** Todo로 나눈 목록이다.  
체크는 `/tdd-red` 또는 테스트 스켈레톤 작성·pytest FAIL 확인 후 진행한다.

---

## 공통 Todo (RED 착수 전)

- [ ] `pip install -e ".[dev]"` 후 Harness pytest 동작 확인 (`0 collected` → 정상)
- [ ] `src/entity/constants.py` 등 **MagicConstant SSOT** 추가 (RED에서 `34`/`16` 리터럴 금지)
- [ ] E001~E007 boundary 오류 표 상세 확정 (Report/02 TBD 보강)
- [ ] conftest 픽스처 정의: **G1**, **G_complete**, **G_mom**, **grid_g1** (D-LOC row-major 예), **grid_bad_blanks** (빈칸 ≠2)

---

## Track A — Boundary (UI) RED Todo

| Layer | `boundary` |
| Track | **UI** |
| 파일 예 | `tests/boundary/test_u_*.py` |
| Mock | stdin/stdout/stderr·control spy **허용** |

### 입력 검증 (U-IN)

- [ ] **U-IN-01** — Given: `grid=None` → Then: `E003` `INVALID_NULL` → RED: `ModuleNotFoundError`
- [ ] **U-IN-02** — Given: `grid=3×4` (비정방) → Then: `E001` `INVALID_SIZE` → RED: `AssertionError`
- [ ] **U-IN-03** — Given: 빈칸 `0` 개수 ≠ 2 (예: 0개) → Then: `E002` `INVALID_BLANKS` → RED: `AssertionError`

### 출력 (U-OUT)

- [ ] **U-OUT-01** — Given: 유효 입력 **G1** → Then: `len(result)==6`, `[r1,c1,n1,r2,c2,n2]` **1-index** → RED: `pytest.fail()` (의도적 RED)

### 흐름 (U-FLOW)

- [ ] **U-FLOW-02** — Given: `grid=None` → Then: `control.execute()` **0회** 호출 (조기 종료) → RED: `pytest.fail()` (의도적 RED)

### Boundary RED 규칙 (매 항목 확인)

- [ ] entity/control에서 **E001~E005** raise·catch·매핑 없음
- [ ] `src/boundary` 미구현 시 **U-IN-01**은 import 단계 `ModuleNotFoundError`로 RED 완료 처리
- [ ] assert 완화·`skip`·`xfail`·테스트 삭제 없음

### Boundary pytest (예정)

```cmd
python -m pytest tests/boundary/test_u_*.py -v
```

---

## Track B — Logic (entity / control) RED Todo

| Layer | `entity`, `control` |
| Track | **Logic** |
| 파일 예 | `tests/entity/test_d_*.py`, `tests/control/test_d_*.py` |
| Mock | **Domain Mock 금지** |

### Entity — 10선 · 합 34 (D-01 ~ D-05)

- [ ] **D-01** — Given: **G1** → Then: 행 4개 각 `sum(row)==MAGIC_CONSTANT` → RED: `ModuleNotFoundError` / `ImportError` (PRD R-02)
- [ ] **D-02** — Given: **G1** → Then: 열 4개 각 `sum(col)==MAGIC_CONSTANT` → RED: 동일 (PRD R-03)
- [ ] **D-03** — Given: **G1** → Then: 주대각·부대각 `sum==MAGIC_CONSTANT` → RED: 동일 (PRD R-04)
- [ ] **D-04** — Given: **G_complete** (10선 OK) → Then: `verify_lines(grid) is True` → RED: `ModuleNotFoundError` 또는 `AssertionError` (PRD R-06, S-01)
- [ ] **D-05** — Given: **G_mom** (행·열 OK, 대각선 1개만 ≠34) → Then: `verify_lines(grid) is False` → RED: `AssertionError` (PRD T-04, SC-2, Mom Test 회귀)

### Entity — 빈칸 좌표 (D-LOC · FR-LOC-01)

**FR-LOC-01 (가칭 — PRD §3.1 미등재):** 4×4 격자에서 값 `0`인 빈칸 **정확히 2개**의 `(행, 열)`을 **row-major** 순으로 나열하고, 좌표는 **1-index** (1~4)로 반환한다.

| C2C | 내용 |
|-----|------|
| Rule 1 | 근거: PRD **R-01**, **R-05**, Input; Report/02·`.cursorrules` **1-index** 출력 계약 |
| Rule 2 | To-Do: PRD에 FR-LOC-01 문구 넣을지 결정 후 `test_d_loc_01.py` import RED 확정 |
| Rule 3 | Given/When/Then → 아래 D-LOC-01~03 |

| Test ID | 대상 함수 (가칭) | Given→Then | Invariant | Expected RED Failure |
|---------|------------------|------------|-----------|----------------------|
| D-LOC-01 | `blank_coords_row_major` | **grid_g1** → `[(2,1),(3,4)]` | `len==2`; 선형 인덱스 오름차순 | `ModuleNotFoundError` |
| D-LOC-02 | 동일 | **grid_g1** → `1≤r,c≤4` | 0-index 좌표 없음 | `ModuleNotFoundError` / `AssertionError` |
| D-LOC-03 | 동일 | **grid_bad_blanks** → 거부 | E001~E005 emit 금지 | `AssertionError` |

- [ ] **D-LOC-01** — `test_d_loc_01_blank_coords_row_major` — RED: `ModuleNotFoundError`
- [ ] **D-LOC-02** — `test_d_loc_02_coords_one_indexed` — RED: `AssertionError`
- [ ] **D-LOC-03** — `test_d_loc_03_rejects_wrong_blank_count` — RED: `AssertionError`
- [ ] 파일: `tests/entity/test_d_loc_01.py` (RED 묶음: D-LOC-01~03)
- [ ] PRD §3.1에 **FR-LOC-01** 공식 추가 (가칭 → 확정)

**grid_g1 예시 (1-index 빈칸 (2,1), (3,4)):**

```text
[ 1,  0,  3,  4]
[ 5,  6,  7,  8]
[ 9, 10, 11, 12]
[13, 14, 15,  0]
```

```cmd
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
```

### Entity — 격자 규칙 (D-06 ~ D-07)

- [ ] **D-06** — Given: 빈칸 `0`이 2개가 아닌 격자 → Then: 빈칸 규칙 위반 판정 실패 → RED: `AssertionError`
- [ ] **D-07** — Given: `1~16` 중복 또는 범위 밖 → Then: 도메인 거부 → RED: `AssertionError`

### Control · Solver (D-08 ~ D-09)

- [ ] **D-08** — Given: **G1** → control 10선 판정 파이프라인 → Then: entity 조합 결과 일관 → RED: `ImportError` (`control` 없음)
- [ ] **D-09** — Given: 부분 마방진 **G1** → Then: `solve_partial` → `int[6]`, 좌표 **1-index** → RED: `ModuleNotFoundError` (Report/02 출력 계약)

### Logic RED 규칙 (매 항목 확인)

- [ ] **MagicConstant SSOT** import만 사용 (`34`/`16` 리터럴 산재 금지)
- [ ] entity에서 **E001~E005** emit 금지 (입력 오류는 boundary Track)
- [ ] Domain Mock 없음 — 실제 격자·픽스처만
- [ ] RED 단계에서 **`src/` 수정 금지** (GREEN에서 최소 구현)

### Logic pytest (예정)

```cmd
python -m pytest tests/entity/test_d_*.py -v
python -m pytest tests/control/test_d_*.py -v
python -m pytest tests/entity/ -k "D-05" -v
```

---

## 트랙 비교 (참고)

| 구분 | Track | Layer | Test ID | Mock | RED 시 대표 실패 |
|------|-------|-------|---------|------|------------------|
| 바운더리 | UI (A) | `boundary` | `U-*` | I/O·control Mock 허용 | `E00x`, `pytest.fail()` |
| 로직 | Logic (B) | `entity`, `control` | `D-*` | Domain Mock 금지 | `ImportError`, `AssertionError` |

---

## GREEN 이후 Todo (참고 — RED 범위 밖)

- [ ] Track별 pytest **PASS** → 같은 Track 디렉터리 회귀
- [ ] `pytest tests/ -v --tb=short` 전체 Green
- [ ] REFACTOR: 동작 유지, ECB·Track 경계 유지

---

## 문서 동기화

- [x] README에 D-LOC 묶음 체크리스트 반영 — [README.md](../README.md#red-단계-체크리스트)
- [ ] PRD [PRD.md](PRD.md) §3.1에 **FR-LOC-01** 항목 추가 (현재 가칭만 RED-TODO에 존재)

---

## 관련 문서

- [PRD.md](PRD.md) — R-01~R-06, T-01~T-04, 성공 기준 SC-1~3
- [Report/02.MagicSquare_HarnessAndCursorRules_Report.md](../Report/02.MagicSquare_HarnessAndCursorRules_Report.md) — ECB Harness
- [.cursor/skills/magic-square-tdd/reference.md](../.cursor/skills/magic-square-tdd/reference.md) — `D-01`~`D-09` 요약
- 본 문서 §D-LOC — `D-LOC-01`~`03` · `/red-test-plan` 산출
