"""Blank-cell coordinates — row-major, 1-index (entity · Logic Track)."""

from entity.constants import BLANK_CELL, COORD_ONE_BASE, GRID_SIZE


def find_blank_coords(grid: list[list[int]]) -> list[tuple[int, int]]:
    """Return 1-index (row, col) for each BLANK_CELL in row-major order."""
    coords: list[tuple[int, int]] = []
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == BLANK_CELL:
                coords.append((row + COORD_ONE_BASE, col + COORD_ONE_BASE))
    return coords
