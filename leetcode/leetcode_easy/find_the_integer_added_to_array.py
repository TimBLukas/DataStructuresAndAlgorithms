"""
Leetcode 3131: Find the integer added to array I

You are given two arrays of equal length, nums1 and nums2.

Each element in nums1 has been increased (or decreased in the case of negative) by an integer,
represented by the variable x.

As a result, nums1 becomes equal to nums2.
Two arrays are considered equal when they contain the same integers with the same frequencies.

Return the integer x.
"""

from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        return nums2[0] - nums1[0]


class Solution2:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return (sum(nums2) - sum(nums1)) // len(nums1)
