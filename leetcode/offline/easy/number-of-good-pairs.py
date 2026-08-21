# https://leetcode.com/problems/number-of-good-pairs/
#
# Title: 1512. Number of Good Pairs
# Difficulty: Easy
#
# Given an array of integers `nums`, return the number of good pairs.
#
# A pair `(i, j)` is called good if `nums[i] == nums[j]` and `i` < `j`.
#
# Example 1:
#
#     Input: nums = [1,2,3,1,1,3]
#     Output: 4
#     Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
#
# Example 2:
#
#     Input: nums = [1,1,1,1]
#     Output: 6
#     Explanation: Each pair in the array are good.
#
# Example 3:
#
#     Input: nums = [1,2,3]
#     Output: 0
#
# Constraints:
#
# 1. `1 <= nums.length <= 100`
#
# 2. `1 <= nums[i] <= 100`


from __future__ import annotations

from typing import List

import unittest


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pass  # TODO: implement


class TestNumberOfGoodPairs(unittest.TestCase):
    def test_example_1(self) -> None:
        self.assertEqual(Solution().numIdenticalPairs(nums=[1,2,3,1,1,3]), 4)

    def test_example_2(self) -> None:
        self.assertEqual(Solution().numIdenticalPairs(nums=[1,1,1,1]), 6)

    def test_example_3(self) -> None:
        self.assertEqual(Solution().numIdenticalPairs(nums=[1,2,3]), 0)

    def test_edgecase(self) -> None:
        pass  # TODO add your own edge cases.


if __name__ == "__main__":
    unittest.main()
