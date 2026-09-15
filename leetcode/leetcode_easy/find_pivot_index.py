"""
Leetcode 724: Find pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly
to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array,
then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.

Return the leftmost pivot index.
If no such index exists, return -1.
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if sum(nums[:i]) == sum(nums[i + 1 :]):
                return i

        return -1


class Solution2:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left, sum_right = 0, sum(nums[1:])
        if sum_left == sum_right:
            return 0

        for i in range(1, len(nums)):
            sum_left += nums[i - 1]
            sum_right -= nums[i]
            print(i, sum_left, sum_right)

            if sum_left == sum_right:
                return i

        return -1
