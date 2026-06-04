"""공통 pytest 픽스처 — 격자 데이터만 (도메인 함수 없음)."""

import pytest

from entity.constants import BLANK_CELL, GRID_SIZE


@pytest.fixture
def grid_g1() -> list[list[int]]:
    """G1: 4×4, 빈칸(BLANK_CELL) 2개, row-major (2,2) → (3,3) — 1-index."""
    _ = GRID_SIZE  # SSOT import (픽스처 크기 근거)
    return [
        [1, 2, 3, 4],
        [5, BLANK_CELL, 7, 8],
        [9, 10, BLANK_CELL, 12],
        [13, 14, 15, 16],
    ]
