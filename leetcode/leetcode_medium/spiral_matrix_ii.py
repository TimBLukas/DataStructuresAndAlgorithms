"""
Leetcode 59: Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
"""

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(1, n + 1)] for j in range(n)]

        top, bottom, left, right = 0, n - 1, 0, n - 1
        row, col, cnt = 0, 0, 1

        while (bottom - top >= 0) and (right - left >= 0):
            while col < right:
                result[row][col] = cnt
                cnt += 1
                col += 1
            top += 1

            while row < bottom:
                result[row][col] = cnt
                cnt += 1
                row += 1
            right -= 1

            while col > left:
                result[row][col] = cnt
                cnt += 1
                col -= 1
            bottom -= 1

            while row > top:
                result[row][col] = cnt
                cnt += 1
                row -= 1
            left += 1
        if top == left and right == bottom:
            result[row][col] = cnt

        return result
