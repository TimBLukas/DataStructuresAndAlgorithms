"""
Leetcode 3567: Minimum Absolute Difference in Sliding Submatrix

You are given an m x n integer matrix grid and an integer k.

For every contiguous k x k submatrix of grid,
compute the minimum absolute difference between any two distinct values within that submatrix.

Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is the minimum absolute difference
in the submatrix whose top-left corner is (i, j) in grid.

Note: If all elements in the submatrix have the same value, the answer will be 0.

A submatrix (x1, y1, x2, y2) is a matrix that is formed by choosing all cells matrix[x][y]
where x1 <= x <= x2 and y1 <= y <= y2.
"""

from typing import List
import math


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def calc_min_diff(matrix: List[List[int]]) -> int:
            values = [v for row in matrix for v in row]
            values.sort()
            min_diff = math.inf
            for i in range(len(values) - 1):
                if values[i + 1] != values[i]:
                    min_diff = min(min_diff, values[i + 1] - values[i])
            return min_diff if min_diff != math.inf else 0

        result = []
        col_idx = 0
        row_idx = 0
        while row_idx + k <= len(grid):
            row = []
            while col_idx + k <= len(grid[0]):
                sub_matrix = [
                    r[col_idx : col_idx + k] for r in grid[row_idx : row_idx + k]
                ]
                row.append(calc_min_diff(sub_matrix))
                col_idx += 1
            col_idx = 0
            result.append(row)
            row_idx += 1

        return result
