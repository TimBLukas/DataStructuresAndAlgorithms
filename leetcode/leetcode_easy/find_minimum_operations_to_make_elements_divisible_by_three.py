"""
Leetcode 3190: Find Minimum Operations to Make All Elements Divisible by Three

You are given an integer array nums.
In one operation, you can add or subtract 1 from any element of nums.

Return the minimum number of operations to make all elements of nums divisible by 3.
"""

from typing import List

import math


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = 0
        for n in nums:
            counter += min(n % 3, 3 - (n % 3))
            print(counter)
        return counter
