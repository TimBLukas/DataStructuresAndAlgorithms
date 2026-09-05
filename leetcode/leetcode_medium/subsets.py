"""
78. Subsets
Given an integer array nums of unique elements,
return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order.
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def recursive(index: int, current: List[int]) -> None:
            if index == len(nums):
                result.append(current.copy())
                return
            recursive(index + 1, current)

            current.append(nums[index])
            recursive(index + 1, current)
            current.pop()

        recursive(0, [])
        return result
