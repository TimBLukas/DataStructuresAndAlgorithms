"""
Leetcode 1605: Find Valid Matrix given row and column Sums

You are given two arrays rowSum and colSum of non-negative integers where rowSum[i]
is the sum of the elements in the ith row and colSum[j]
is the sum of the elements of the jth column of a 2D matrix.
In other words, you do not know the elements of the matrix,
but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length
that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements.
It's guaranteed that at least one matrix that fulfills the requirements exists.
"""

from typing import List
import math


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        result = [[0] * len(colSum) for _ in range(len(rowSum))]

        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                value = min(rowSum[i], colSum[j])

                result[i][j] = value

                rowSum[i] -= value
                colSum[j] -= value

        return result
