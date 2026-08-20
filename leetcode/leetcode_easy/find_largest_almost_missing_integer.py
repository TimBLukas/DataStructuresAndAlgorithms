"""
Leetcdoe 3471: Find the largest almost missing integer

You are given an integer array nums and an integer k.

An integer x is almost missing from nums if x appears in exactly one subarray
of size k within nums.

Return the largest almost missing integer from nums.
If no such integer exists, return -1.

A subarray is a contiguous sequence of elements within an array.
"""

from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        max_element = -1
        if len(nums) > k:
            max_element = (
                max([nums[0], nums[-1]]) if len(set([nums[0], nums[-1]])) == 2 else -1
            )
            first_element_safe = True
            if nums[0] in nums[1:-1]:
                max_element = nums[-1]
                first_element_safe = False
            if nums[-1] in nums[1:-1]:
                max_element = nums[0] if first_element_safe else -1

            return max_element

        else:
            nums.sort(reverse=True)
            for i in range(len(nums) - 2):
                if nums[i] != nums[i + 1]:
                    return nums[i]

            return -1
