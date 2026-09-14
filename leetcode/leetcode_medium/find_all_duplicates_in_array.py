"""
Leetcode 442: Find All Duplicates in an Array

Given an integer array nums of length n where all the integers of nums
are in the range [1, n] and each integer appears at most twice,
return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space,
excluding the space needed to store the output
"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for n in nums:
            idx = abs(n) - 1

            if nums[idx] < 0:
                result.append(abs(n))
            else:
                nums[idx] *= -1

        return result
