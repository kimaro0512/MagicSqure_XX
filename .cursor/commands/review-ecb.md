# Review ECB — 계약·아키텍처 리뷰

MagicSquare_XX **ECB·Dual-Track 계약**만 검토한다. **코드 수정 금지** — 파일 읽기·분석·표 보고만.

근거: `.cursorrules` · Report/01 · Report/02 · `.cursor/skills/magic-square-tdd/SKILL.md`

사용자가 `/review-ecb` 뒤에 `@` 파일·경로·커밋 범위를 적으면 그 범위만 리뷰한다. 미지정 시 `src/`·`tests/` 전체.

**한국어**로 응답한다.

---

## 필수 선언

응답 **첫 줄**:

```
Review: ECB | Scope: src/entity, tests/entity | Code change: none
```

---

## 절차

1. **범위 확정** — 리뷰 대상 파일 목록 명시.
2. **읽기 전용** — `src/entity`, `src/control`, `src/boundary`, `tests/**` import·호출·상수·Mock 패턴 스캔.
3. **5항목 체크** — 아래 체크리스트 각각 ✅ / ⚠️ / ❌ 판정.
4. **위반 표** — ❌·⚠️만 `## 위반` 표에 기록 (파일:줄, 규칙, 설명).
5. **요약** — 위반 건수, 통과 여부, 수정 제안은 **텍스트만** (diff·패치 금지).

---

## 체크리스트 (5항목)

### 1. Import 방향 (ECB)

| Layer | 허용 import | 위반 |
|-------|-------------|------|
| entity | 표준 lib, 동일 package 내부 | `control`, `boundary`, 상위 package |
| control | `entity` | `boundary`, entity 우회 I/O |
| boundary | `control` | `entity` 직접 import |

`boundary → control → entity` 역방향 import ❌.

### 2. entity · E001~E005

entity/control에서 **금지**:

- `E001`~`E005` 문자열·코드·예외 raise/catch/매핑
- 입력 포맷 검증·CLI 변환·I/O

E001~E007 **표면 처리는 boundary만**.

### 3. 출력 계약 · `int[6]` 1-index

성공 출력: `[r1, c1, n1, r2, c2, n2]`

| 항목 | 계약 |
|------|------|
| 길이 | 6 |
| 좌표 | `r*`, `c*`는 **1-index** (1~4) |
| 값 | `n*`는 `1~16` |
| 0-index 혼용 | ❌ (배열 인덱스와 출력 좌표 혼동) |

### 4. MagicConstant SSOT

| 허용 | 위반 |
|------|------|
| SSOT 모듈에서 `34`/`16`/`4` import | `src/**`·`tests/**`에 마방진 상수 **리터럴 산재** |
| 테스트 fixture 주석의 설명용 숫자 | assert·비즈니스 로직에 bare `34`, `16`, `4` |

SSOT 파일 경로를 보고에 명시 (없으면 ⚠️).

### 5. Logic Track · Domain Mock

| 경로 | Mock |
|------|------|
| `tests/entity/`, `tests/control/` (`test_d_*`) | entity/control **Domain Mock 금지** (`patch`, stub, fake domain) |
| `tests/boundary/` (`test_u_*`) | stdin/stdout/stderr Mock **허용** |

`unittest.mock.patch` on `entity.*` / `control.*` in Logic tests → ❌.

---

## 보고 형식

### 체크 요약

| # | 항목 | 판정 | 비고 |
|---|------|------|------|
| 1 | Import 방향 | ✅ / ⚠️ / ❌ | |
| 2 | entity E001~E005 | ✅ / ⚠️ / ❌ | |
| 3 | int[6] 1-index | ✅ / ⚠️ / ❌ | |
| 4 | MagicConstant SSOT | ✅ / ⚠️ / ❌ | |
| 5 | Logic Domain Mock | ✅ / ⚠️ / ❌ | |

### 위반 (해당 시만)

| ID | 파일:줄 | 규칙 | 설명 |
|----|---------|------|------|
| V-01 | `src/entity/foo.py:12` | Import 방향 | `from boundary import ...` |
| V-02 | `tests/entity/test_d_x.py:8` | Domain Mock | `@patch("entity.bar")` |

위반 없으면: **「ECB·계약 위반 없음」** 한 줄.

### 최종

```
Review result: PASS | FAIL (n violations)
Code change: none
```

---

## 금지

| 금지 | |
|------|--|
| **코드·테스트 수정** | 리뷰만 |
| **리팩터·GREEN 제안을 코드로 적용** | 텍스트 권고만 |
| **스타일·성능·일반 품질 리뷰** | ECB·계약 5항목 외 논의 금지 |
| **git commit / push** | 사용자 요청 시만 |
