---
name: magic-square-tdd
description: MagicSquare_XX Dual-Track TDD·ECB 개발 시 Agent가 따를 절차. Use when implementing MagicSquare code, writing test_d_* or test_u_* tests, RED/GREEN/REFACTOR, entity/control/boundary layers, or MagicSquare ECB.
---

# MagicSquare Dual-Track TDD

MagicSquare_XX ECB + Dual-Track TDD 개발 절차. `.cursorrules`·Report/01·Report/02와 충돌 시 **문서 우선**.

추가 참조: [reference.md](reference.md) — Logic 테스트 ID (`D-*`) 목록.

---

## Skill을 켜는 조건

다음 **하나 이상**이면 본 Skill을 적용한다.

| 트리거 | 예시 |
|--------|------|
| MagicSquare 구현·테스트 | `verify_lines`, 빈칸 2개, 10선 합 34 |
| TDD 사이클 | RED / GREEN / REFACTOR, `test_d_*`, `test_u_*` |
| ECB 레이어 작업 | `src/entity`, `src/control`, `src/boundary` |
| Dual-Track | Logic Track vs UI Track, Mock 허용 여부 |
| 오류 코드 | E001~E007, boundary 포맷 |

**끄는 조건:** 문서만 편집, README·Report 작성, git commit/push만 요청(코드 변경 없음).

매 턴 **한국어**로 선언: `Phase` · `Layer` · `Track` · `Test ID`.

---

## Logic Track vs UI Track

| | Logic Track | UI Track |
|---|-------------|----------|
| **Layer** | entity, control | boundary |
| **tests/** | `entity/`, `control/` | `boundary/` |
| **파일명** | `test_d_*.py` | `test_u_*.py` |
| **테스트 ID** | `D-*` | `U-*` |
| **Mock** | Domain Mock **금지** | 입출력·stderr Mock **허용** |
| **검증 대상** | 도메인 규칙·유스케이스 | CLI·포맷·E001~E007 표면 |
| **상수** | MagicConstant SSOT import | boundary는 변환만, 상수 재정의 금지 |

---

## ECB · Mock · E001~E007

### ECB 의존

```
boundary → control → entity
```

| Layer | 허용 | 금지 |
|-------|------|------|
| **entity** | 순수 도메인 함수·타입 | `entity → *` import, I/O, E001~E005 |
| **control** | entity import, 유스케이스 조합 | boundary import, CLI, E001~E005 처리 |
| **boundary** | control import, I/O, E001~E007 | entity 직접 import (control 경유) |

### Mock

| Mock 종류 | Logic | UI |
|-----------|-------|-----|
| Domain 객체·함수 대체 | **금지** | — |
| `stdin` / `stdout` / `stderr` | — | **허용** |
| control·entity spy/stub | **금지** | boundary에서 control만 patch 가능(최소) |

### E001~E007

| 코드 | 담당 | entity/control |
|------|------|----------------|
| E001~E005 | boundary (검증·변환·포맷) | raise·catch·매핑 **금지** |
| E006~E007 | boundary 표면 | entity는 도메인 내부 규칙만 |

---

## RED (5~7단계)

1. **선언** — `Phase=RED`, Layer, Track, Test ID (`D-*` 또는 `U-*`).
2. **사양 확인** — Report/01·02, `.cursorrules`에서 입력·출력·오류 범위 확인.
3. **테스트 파일** — Logic: `tests/{entity|control}/test_d_<topic>.py` / UI: `tests/boundary/test_u_<topic>.py`.
4. **테스트 작성** — 함수 docstring 또는 주석에 `D-XX` / `U-XX` ID 명시.
5. **MagicConstant** — `34`/`16`/`4` 리터럴 금지; SSOT 없으면 RED 전 SSOT 모듈 추가(최소).
6. **실행** — 해당 파일 또는 `-k D-XX`만 실행 → **실패 확인**(ImportError·AssertionError).
7. **금지 확인** — skip·xfail·assert 완화·테스트 삭제 없음. 실패 원인을 완료 보고에 기록.

---

## GREEN (5~7단계)

1. **선언** — `Phase=GREEN`, Layer, Track, Test ID.
2. **최소 구현** — RED를 통과하는 **가장 작은** 코드만 해당 Layer에 추가.
3. **ECB 준수** — entity에 I/O·E001~E005 넣지 않음; boundary가 entity 직접 호출하지 않음.
4. **SSOT** — 새 상수는 MagicConstant 한 곳에만; 기존 리터럴 치환.
5. **실행** — 해당 테스트 파일 `-v` → **통과**.
6. **회귀** — 같은 Track 디렉터리 전체 pytest → 통과.
7. **금지 확인** — assert 완화·skip·xfail·테스트 삭제로 Green 달성하지 않았는지 확인.

---

## REFACTOR (5~7단계)

1. **선언** — `Phase=REFACTOR`, Layer, Track.
2. **전제** — GREEN 직후, 해당 Track 테스트 **전부 Green** 상태에서만 시작.
3. **범위** — 동작 변경 없이 이름·중복·구조만 정리; ECB·Track 경계 유지.
4. **실행 (Track)** — `tests/entity/` 또는 `tests/control/` 또는 `tests/boundary/` 전체 `-v`.
5. **실행 (전체)** — `pytest tests/ -v` → 전 Track Green.
6. **금지 확인** — 리팩터 중 테스트·assert 삭제·완화 없음.
7. **완료 보고** — 변경 요약·실행 명령·다음 RED 후보 Test ID.

---

## Test / Review Loop

| 시점 | 명령 | 기대 |
|------|------|------|
| RED 직후 | `pytest tests/<layer>/test_d_<file>.py -v` 또는 `-k "D-XX"` | **FAIL** |
| GREEN 직후 (단일) | 위와 동일 | **PASS** |
| GREEN 직후 (Track) | `pytest tests/entity/ -v` / `tests/control/ -v` / `tests/boundary/ -v` | **PASS** |
| REFACTOR 중·후 | `pytest tests/ -v` | **PASS** |
| UI Track RED/GREEN | `pytest tests/boundary/test_u_*.py -v` | FAIL → PASS |
| PR·세션 마감 Review | `pytest tests/ -v --tb=short` | **PASS**, 0 skip/xfail |
| Harness 점검 | `pip install -e ".[dev]"` 후 전체 pytest | dev env 정상 |

**Review Loop 규칙**

- RED: 실패가 **의도된 assertion/import** 인지 확인 (exit 0이면 RED 아님).
- GREEN: 단일 → Track → 전체 순으로 범위 확대.
- REFACTOR: 전체 Green 없이 커밋·완료 보고 금지.
- `exit code 5`(0 collected): 테스트 파일 미작성 — RED 미완료.

---

## 완료 보고 항목

작업 턴·세션 종료 시 아래를 **한국어**로 보고한다.

```
Phase: RED | GREEN | REFACTOR
Layer: entity | control | boundary
Track: Logic | UI
Test ID: D-XX | U-XX
파일: (변경된 src/tests 경로)
pytest: (실행한 명령)
결과: PASS n / FAIL n / RED 확인(실패 메시지 1줄)
ECB: 위반 없음 | (위반 시 수정 내역)
Mock: 사용 없음 | (UI Track Mock 목록)
E001~E007: entity/control 미접촉 확인
다음: (다음 Test ID 또는 Layer)
```

git commit/push는 **사용자 요청 시만**.

---

## 금지 (전 Phase 공통)

- assert 완화, `@pytest.mark.skip`, `xfail`, 실패 테스트 삭제
- Logic Track Domain Mock
- entity에서 E001~E005 처리
- `34`/`16` 리터럴 산재 (SSOT 위반)
- 요청 범위 밖 기능·파일 추가
