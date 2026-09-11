"""
Leetcode 213: House Robber II

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(nums):
            prev1, prev2 = 0, 0

            for money in nums:
                prev2, prev1 = prev1, max(prev1, prev2 + money)

            return prev1

        return (
            max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
            if len(nums) > 1
            else nums[0]
        )
