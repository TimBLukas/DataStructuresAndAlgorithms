"""
Leetcode 704: Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            center = (left + right) // 2
            if target < nums[center]:
                right = center - 1
            elif target > nums[center]:
                left = center + 1
            else:
                return center
        return -1
