"""
Leetcode 861: Score After Flipping Matrix

A move consists of choosing any row or column and toggling
each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number,
and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).
"""

from typing import List
import math


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in grid:
            if row[0] == 0:
                # flip if first number is not 1
                for i in range(len(row)):
                    row[i] = 0 if row[i] == 1 else 1
        for col in range(len(grid[0])):
            one_cnt = 0
            for row in grid:
                if row[col] == 1:
                    one_cnt += 1
            if one_cnt < math.ceil(len(grid) / 2):
                for row in grid:
                    # flip if there are more 0 than ones
                    row[col] = 0 if row[col] == 1 else 1

        # calculate final score
        score, exp = 0, 0
        for row in grid:
            for i in row[::-1]:
                score += i * (2**exp)
                exp += 1
            exp = 0
        return score
