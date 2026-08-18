"""
Leetcode 2657: Find the Prefix Common Array of Two Arrays

You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i]
is equal to the count of numbers that are present at or before
the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers
from 1 to n exactly once.
"""

from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
        for i in range(len(A)):
            count = 0
            for n in A[: i + 1]:
                if n in B[: i + 1]:
                    count += 1

            result.append(count)

        return result


class Solution2:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        result = [0] * n
        seen = [0] * (n + 1)

        for i in range(n):
            seen[0] += seen[A[i]]
            seen[A[i]] = 1

            seen[0] += seen[B[i]]
            seen[B[i]] = 1

            result[i] = seen[0]

        return result
