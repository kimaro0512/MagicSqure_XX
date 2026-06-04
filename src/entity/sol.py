"""Partial magic-square fill — int[6] output (entity · Logic Track)."""

from __future__ import annotations

from entity.constants import COORD_ONE_BASE, GRID_SIZE, MAGIC_CONSTANT
from entity.loc import find_blank_coords


def solve_step_a(grid: list[list[int]]) -> list[int]:
    """Step A: per blank, value so its column sums to MAGIC_CONSTANT (partial grid)."""
    coords = find_blank_coords(grid)
    out: list[int] = []
    for row_1, col_1 in coords:
        col_vals = [grid[row][col_1 - COORD_ONE_BASE] for row in range(GRID_SIZE)]
        value = MAGIC_CONSTANT - sum(col_vals)
        out.extend([row_1, col_1, value])
    return out
