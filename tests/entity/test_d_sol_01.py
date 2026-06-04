"""D-SOL-01 — step A success · int[6] golden (entity · Logic Track)."""

from entity.sol import solve_step_a

from tests._approval import assert_matches_golden

GOLDEN_D_SOL_01_G1_STEP_A = "d_sol_01_g1_step_a.approved.txt"


def test_d_sol_01_step_a_success(grid_g1: list[list[int]]) -> None:
    # D-SOL-01
    # Given: G1 (grid_g1)
    # When: solve_step_a(grid_g1)
    # Then: int[6] 1-index — golden: tests/golden/d_sol_01_g1_step_a.approved.txt
    actual = solve_step_a(grid_g1)
    assert_matches_golden(actual, GOLDEN_D_SOL_01_G1_STEP_A)
