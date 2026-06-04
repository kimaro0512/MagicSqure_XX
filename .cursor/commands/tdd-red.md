# TDD RED — 실패 테스트 먼저

MagicSquare_XX Dual-Track TDD **RED 단계만** 수행한다.  
`.cursorrules`·Report/01·Report/02·`.cursor/skills/magic-square-tdd/reference.md`를 따른다. **한국어**로 응답한다.

사용자가 채팅에서 `/tdd-red` 뒤에 적은 텍스트(예: `D-01 entity`, `U-01 boundary`)를 Test ID·Layer 힌트로 사용한다.

---

## 필수 선언

응답 **첫 줄**은 반드시 아래 형식이다.

```
Phase: red | Layer: entity | Track: Logic | Test ID: D-01
```

| 필드 | 값 |
|------|-----|
| Phase | `red` (소문자) |
| Layer | `entity` \| `control` \| `boundary` |
| Track | Logic Track → `entity`/`control` · UI Track → `boundary` |
| Test ID | `D-*` (Logic) 또는 `U-*` (UI) |

Layer·Track 불일치 시 RED 시작 전에 사용자에게 확인한다.

---

## 절차

1. **ID 확인** — `reference.md` 또는 사용자 입력에서 Test ID·Layer·Track 확정. 미정이면 RED 중단 후 질문.
2. **사양 확인** — Report/01·02, `.cursorrules`에서 해당 ID의 입력·출력·오류 범위만 확인 (구현 설계 금지).
3. **파일 경로** — Logic: `tests/entity/test_d_*.py` 또는 `tests/control/test_d_*.py` · UI: `tests/boundary/test_u_*.py`.
4. **AAA 테스트 작성** — Arrange / Act / Assert. 함수 docstring 또는 `# D-XX` 주석에 Test ID 명시.
5. **상수** — `34`/`16`/`4` 리터럴 금지. SSOT 모듈이 없으면 import 실패(ImportError)로 RED를 유도한다 — **`src/`는 수정하지 않는다.**
6. **pytest 실행** — 해당 파일 또는 `-k "D-XX"`만 실행 → **FAIL** 확인.
7. **RED 검증** — exit code 0이면 RED 미완료. AssertionError·ImportError·ModuleNotFoundError 등 **의도된 실패**여야 한다.

---

## pytest 예시 (bash)

```bash
# Logic — entity, 단일 파일
pytest tests/entity/test_d_row_sum.py -v

# Logic — Test ID로 필터
pytest tests/entity/ -k "D-01" -v

# Logic — control
pytest tests/control/test_d_verify_pipeline.py -v

# UI — boundary
pytest tests/boundary/test_u_cli_format.py -v
pytest tests/boundary/ -k "U-01" -v
```

**기대:** `FAILED` 또는 `ERROR` (ImportError 포함). `passed`만 있으면 RED 아님.

---

## 보고

RED 완료 시 아래 항목을 보고한다.

| 항목 | 내용 |
|------|------|
| Test ID | `D-XX` 또는 `U-XX` |
| FAIL 요약 | pytest 실패 메시지 1~3줄 (assertion / import 등) |
| 변경 파일 | **`tests/` 하위만** — 경로 목록 |
| pytest 명령 | 실행한 명령 그대로 |
| 다음 | GREEN 대기 — `src/` 구현은 별도 요청 |

git commit/push는 사용자 요청 시만.

---

## 금지

| 금지 | 이유 |
|------|------|
| **`src/` 수정** | RED는 테스트만 — GREEN에서 구현 |
| **Logic Track Domain Mock** | entity/control 함수·객체 대체 금지 |
| **assert 완화·삭제** | Green을 테스트가 아닌 assert로 달성 |
| **`@pytest.mark.skip` / `xfail`** | RED 우회 |
| **GREEN·REFACTOR 작업** | 본 Command 범위 밖 |
| **요청 밖 Layer·ID** | 선언한 Test ID·Layer만 |

UI Track(boundary)에서만 `stdin`/`stdout`/`stderr` Mock 허용.
