# MagicSquare_XX

4×4 **부분 마방진**을 다룰 때, 행·열·대각선 검증을 빠뜨려 “완료”로 착각하고 시간을 잃는 문제를 **Mom Test**로 정의하고, **10선(행 4 + 열 4 + 대각선 2) 합 34 판정**을 코드·테스트로 고정하는 프로젝트입니다.

| 항목 | 내용 |
|------|------|
| **도메인** | 4×4 격자, 1~16, 빈칸 `0`, 마법 합 **34**, 검증 **10선** |
| **페르소나** | 4×4 부분 마방진(빈칸 2개)을 손으로/코드로 다루는 학습자 |
| **현재 단계** | STEP 1 Mom Test 완료 → 문제 정의·PRD 초안 → **세션 3 구현 예정** |
| **구현 상태** | 문서 단계 (`src/`, `tests/` 미생성) |

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
│   └── PRD.md                                         # 제품 요구사항 v0.1 (세션 3)
├── Report/
│   ├── 01.REPORT.md                                   # Mom Test STEP 1 보고서
│   └── 01.MagicSquare_ProblemDefinition_Report.md     # 문제 정의 보고서
└── prompting/
    ├── 01.prompting.md                                # STEP 1 인터뷰 Transcript
    └── 01.MagicSquare_ProblemDefinition_Prompting.md  # 문제 정의·워크북 Transcript
```

**세션 3 구현 예정 (미생성)**

```
src/                    # verify_lines 등 판정 로직
tests/                  # 10선 · 합 34 · 대각선 회귀 테스트
```

---

## 문서 가이드

| 문서 | 용도 |
|------|------|
| [Report/01.REPORT.md](Report/01.REPORT.md) | Mom Test 인터뷰 원본 — 규칙, Q&A, 워크북 결과 |
| [Report/01.MagicSquare_ProblemDefinition_Report.md](Report/01.MagicSquare_ProblemDefinition_Report.md) | 문제 정의 — 페르소나, 진짜/표면 문제, 도메인, 채점(8/10) |
| [docs/PRD.md](docs/PRD.md) | PRD — R-G-I-O, Rule/Command/Skill/Test Loop, 성공 기준 |
| [prompting/01.prompting.md](prompting/01.prompting.md) | STEP 1 Cursor 대화 Export |
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

## 개발 로드맵

| 단계 | 내용 | 상태 |
|------|------|------|
| STEP 1 | Mom Test 인터뷰 | ✅ |
| Problem Definition | 문제 정의 보고서 | ✅ |
| PRD v0.1 | 세션 3 요구사항 | ✅ |
| 세션 3 Red | 행/열/대각선 테스트 작성 | ⏳ |
| 세션 3 Green | `verify_lines` 등 구현 | ⏳ |
| STEP 2 | 추궁 답변·추가 인터뷰 | ⏳ |

---

## 빠른 시작 (구현 후)

`src/`·`tests/`가 추가되면 아래처럼 실행합니다.

```cmd
cd c:\DEV\MagicSqure_XX
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install pytest
python -m pytest tests/ -v
```

---

## 참고

- **Mom Test** — Rob Fitzpatrick, *The Mom Test*: 과거 행동·비용 중심 인터뷰, 솔루션 착각 방지
- **Magic Square** — 4×4에 1~16을 한 번씩 배치, 각 행·열·대각선의 합이 34
