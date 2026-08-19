"""
Leetcode 3289: The Two Sneaky Number of Digitville

In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1.
Each number was supposed to appear exactly once in the list, however,
two mischievous numbers sneaked in an additional time, making the list longer than usual.

As the town detective, your task is to find these two sneaky numbers.
Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.
"""

from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []

        for n in nums:
            if n in seen:
                result.append(n)
            else:
                seen.add(n)

        return result
