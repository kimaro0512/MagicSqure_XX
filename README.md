# MagicSquare_XX

4×4 **부분 마방진**을 다룰 때, 행·열·대각선 검증을 빠뜨려 “완료”로 착각하고 시간을 잃는 문제를 **Mom Test**로 정의하고, **10선(행 4 + 열 4 + 대각선 2) 합 34 판정**을 코드·테스트로 고정하는 프로젝트입니다.

| 항목 | 내용 |
|------|------|
| **도메인** | 4×4 격자, 1~16, 빈칸 `0`, 마법 합 **34**, 검증 **10선** |
| **페르소나** | 4×4 부분 마방진(빈칸 2개)을 손으로/코드로 다루는 학습자 |
| **현재 단계** | **GREEN** (D-LOC-01 PASS) · Golden Master baseline 등재 |
| **구현 상태** | `find_blank_coords` · `test_d_loc_01` **1 passed** · 나머지 `D-*`/`U-*` RED 대기 |

---

## 진짜 문제 (Mom Test)

> 4×4 부분 마방진을 풀 때 행·열·대각선 중 하나라도 검증에서 빼먹으면, 이미 맞췄다고 판단한 뒤 시간을 쓰게 되고, 틀림이 드러나면 그 시간이 전부 헛수고가 된다.

**증거 (인터뷰 인용)**

- "지난주 OO 과제에서"
- "빈칸 2개 넣고 행·열·대각선 합 맞췄는데"
- "대각선 하나를 빼먹어서 20분 날렸다"

---

## 이번에 하지 않는 것

| 표면 문제 (금지) | 이유 |
|------------------|------|
| 마방진 자동 생성·솔버 | 풀이가 아니라 **판정** 우선 |
| GUI / 웹 / 모바일 앱 | 검증 패턴을 테스트로 재현 |
| 프로젝트 전체 한 번에 완성 | 세션 3는 Rule · Command · (Skill) · Test Loop만 |

---

## 프로젝트 구조

```
MagicSquare_XX/
├── README.md                                          # 본 파일
├── docs/
│   ├── PRD.md                                         # 제품 요구사항 v0.1 (세션 3)
│   ├── RED-TODO.md                                    # RED 단계 Dual-Track Todo (상세)
│   └── GOLDEN-MASTER.md                               # GREEN PASS 기준선 · 회귀 레지스트리
├── src/entity|control|boundary/                       # ECB (패키지 골격)
├── tests/entity|control|boundary/                     # Dual-Track 테스트 트랙
├── Report/
│   ├── 01.REPORT.md                                   # Mom Test STEP 1 보고서
│   ├── 01.MagicSquare_ProblemDefinition_Report.md     # 문제 정의 보고서
│   ├── 02.MagicSquare_HarnessAndCursorRules_Report.md # Harness · .cursorrules
│   ├── 03.MagicSquare_RED_DLOC01_Report.md            # RED · D-LOC-01
│   ├── 04.MagicSquare_GREEN_DLOC01_Report.md          # GREEN · D-LOC-01 baseline
│   └── 05.MagicSquare_GoldenMaster_DSOL01_Report.md   # Golden Master · D-SOL-01
└── prompting/
    ├── 01.prompting.md                                # STEP 1 인터뷰 Transcript
    └── 01.MagicSquare_ProblemDefinition_Prompting.md  # 문제 정의·워크북 Transcript
```

---

## 문서 가이드

| 문서 | 용도 |
|------|------|
| [Report/01.REPORT.md](Report/01.REPORT.md) | Mom Test 인터뷰 원본 — 규칙, Q&A, 워크북 결과 |
| [Report/01.MagicSquare_ProblemDefinition_Report.md](Report/01.MagicSquare_ProblemDefinition_Report.md) | 문제 정의 — 페르소나, 진짜/표면 문제, 도메인, 채점(8/10) |
| [docs/PRD.md](docs/PRD.md) | PRD — R-G-I-O, Rule/Command/Skill/Test Loop, 성공 기준 |
| [docs/RED-TODO.md](docs/RED-TODO.md) | RED 단계 Dual-Track Todo — 바운더리·로직 설계·pytest |
| [docs/GOLDEN-MASTER.md](docs/GOLDEN-MASTER.md) | GREEN PASS 게이트 · 승인 출력 baseline (회귀) |
| [Report/04.MagicSquare_GREEN_DLOC01_Report.md](Report/04.MagicSquare_GREEN_DLOC01_Report.md) | GREEN · D-LOC-01 · Golden Master 1차 |
| [Report/05.MagicSquare_GoldenMaster_DSOL01_Report.md](Report/05.MagicSquare_GoldenMaster_DSOL01_Report.md) | Golden Master · D-SOL-01 · `_approval.py` |
| [prompting/01.prompting.md](prompting/01.prompting.md) | STEP 1 Cursor 대화 Export |
| [prompting/05.MagicSquare_GoldenMaster_DSOL01_Prompting.md](prompting/05.MagicSquare_GoldenMaster_DSOL01_Prompting.md) | GREEN·Golden Master 세션 Export |
| [prompting/01.MagicSquare_ProblemDefinition_Prompting.md](prompting/01.MagicSquare_ProblemDefinition_Prompting.md) | 문제 정의·워크북·PRD 작성 대화 Export |

---

## 세션 3 목표 (PRD 요약)

**주제:** 4×4 부분 마방진을 “다 맞췄다”고 판단하기 전에, **10선 합 34** 검증을 빠짐없이 돌릴 수 있는 **판정 규칙과 테스트 루프**만 만든다.

| | 내용 |
|---|------|
| **Role** | Verifier — 맞췄는지 판정 |
| **Goal** | 행 4 + 열 4 + 대각선 2 = 10선, 모두 합 34 |
| **Input** | 4×4 격자 (`0` = 빈칸, `1~16` = 채운 칸) |
| **Output** | `True` / `False` (+ 선택: 틀린 줄) |

### 성공 기준 (Mom Test 연결)

1. OO 과제형(빈칸 2개) 격자로 검증 실행 가능
2. 대각선 1개만 틀린 케이스 → 테스트 **실패**
3. pytest 1회(수 초)로 틀림 발견 — 수동 20분 헛수고 방지

---

## RED 단계 체크리스트

상세·pytest 명령: [docs/RED-TODO.md](docs/RED-TODO.md).  
체크는 테스트 작성 후 **pytest FAIL** 확인 시 진행 (`/tdd-red`).

### 공통 (RED 착수 전)

- [x] `pip install -e ".[dev]"` 후 pytest 확인 (`.venv` · **1 passed** @ D-LOC-01)
- [x] **MagicConstant SSOT** (`src/entity/constants.py`) — `34`/`16`/`4`/`0` 리터럴 금지
- [ ] E001~E007 boundary 오류 표 상세 확정
- [x] conftest 픽스처: **grid_g1** (D-LOC-01) · [ ] **G_complete**, **G_mom**, **grid_bad_blanks**

### Track A — Boundary (UI · `U-*`)

- [ ] **U-IN-01** — `grid=None` → `E003` `INVALID_NULL` → RED: `ModuleNotFoundError`
- [ ] **U-IN-02** — `grid=3×4` → `E001` `INVALID_SIZE` → RED: `AssertionError`
- [ ] **U-IN-03** — 빈칸 `0` ≠ 2개 → `E002` `INVALID_BLANKS` → RED: `AssertionError`
- [ ] **U-OUT-01** — 유효 **G1** → `len(result)==6`, 1-index → RED: `pytest.fail()`
- [ ] **U-FLOW-02** — `grid=None` → `execute()` 0회 → RED: `pytest.fail()`
- [ ] Boundary 규칙: entity E001~E005 미처리 · skip/xfail 금지

### Track B — Logic (entity/control · `D-*`)

- [ ] **D-01** — **G1** → 행 4개 합 = MagicConstant
- [ ] **D-02** — **G1** → 열 4개 합 = MagicConstant
- [ ] **D-03** — **G1** → 대각선 2개 합 = MagicConstant
- [ ] **D-04** — **G_complete** → `verify_lines` → `True`
- [ ] **D-05** — **G_mom** (대각선 1개만 틀림) → `verify_lines` → `False` *(Mom Test 회귀)*
- [ ] **D-06** — 빈칸 `0`이 2개가 아닌 격자 → 판정 실패
- [ ] **D-07** — `1~16` 중복·범위 밖 → 도메인 거부
- [ ] **D-08** — control 10선 판정 파이프라인
- [ ] **D-09** — `solve_partial` → `int[6]` 1-index
- [ ] Logic 규칙: Domain Mock 금지 · RED 중 `src/` 수정 금지 · SSOT import만

### Track B — 빈칸 좌표 (D-LOC · `FR-LOC-01` 가칭)

> **FR-LOC-01 (가칭):** 4×4 격자에서 `0`인 빈칸 **2개**의 `(행, 열)`을 **row-major** 순, **1-index** (1~4)로 반환.  
> PRD 본문에는 아직 없음 — [docs/RED-TODO.md](docs/RED-TODO.md) §D-LOC · R-01·R-05·Report/02 근거.

- [x] **D-LOC-01** — **grid_g1** → `find_blank_coords` → `[(2,2),(3,3)]` row-major · **GREEN PASS** ([Golden Master](docs/GOLDEN-MASTER.md))
- [ ] **D-LOC-02** — **grid_g1** → 모든 `r,c ∈ {1..4}` (0-index 없음) → RED: `AssertionError`
- [ ] **D-LOC-03** — **grid_bad_blanks** (빈칸 ≠2) → 도메인 거부 · E001~E005 **금지** → RED: `AssertionError`
- [x] `tests/entity/test_d_loc_01.py` GREEN · `pytest tests/entity/test_d_loc_01.py -v`
- [ ] PRD §3.1에 **FR-LOC-01** 문구 공식 반영 (선택)

---

## 개발 로드맵

| 단계 | 내용 | 상태 |
|------|------|------|
| STEP 1 | Mom Test 인터뷰 | ✅ |
| Problem Definition | 문제 정의 보고서 | ✅ |
| PRD v0.1 | 세션 3 요구사항 | ✅ |
| Harness · ECB | `src/`·`tests/` 골격 · Dual-Track | ✅ |
| RED | [체크리스트](#red-단계-체크리스트) · `test_d_*` / `test_u_*` | ⏳ (D-LOC-01만 GREEN) |
| Golden Master | [docs/GOLDEN-MASTER.md](docs/GOLDEN-MASTER.md) · D-LOC-01 baseline | ✅ |
| 세션 3 Green | `verify_lines` 등 구현 | ⏳ (D-LOC-01 ✅) |
| STEP 2 | 추궁 답변·추가 인터뷰 | ⏳ |

---

## 빠른 시작 (구현 후)

`src/`·`tests/`가 추가되면 아래처럼 실행합니다.

```cmd
cd c:\DEV\MagicSqure_XX
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install -e ".[dev]"
python -m pytest tests/ -v
python -m pytest tests/boundary/test_u_*.py -v
python -m pytest tests/entity/test_d_*.py -v
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
```

---

## 참고

- **Mom Test** — Rob Fitzpatrick, *The Mom Test*: 과거 행동·비용 중심 인터뷰, 솔루션 착각 방지
- **Magic Square** — 4×4에 1~16을 한 번씩 배치, 각 행·열·대각선의 합이 34
