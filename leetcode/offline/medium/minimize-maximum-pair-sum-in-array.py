# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
#
# Title: 1877. Minimize Maximum Pair Sum in Array
# Difficulty: Medium
#
# The pair sum of a pair `(a,b)` is equal to `a + b`. The maximum pair sum is
# the largest pair sum in a list of pairs.
#
# 1. For example, if we have pairs `(1,5)`, `(2,3)`, and `(4,4)`, the maximum
#    pair sum would be `max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8`.
#
# Given an array `nums` of even length `n`, pair up the elements of `nums`
# into `n / 2` pairs such that:
#
# 1. Each element of `nums` is in exactly one pair, and
#
# 2. The maximum pair sum is minimized.
#
# Return the minimized maximum pair sum after optimally pairing up the
# elements.
#
# Example 1:
#
#
#     Input: nums = [3,5,2,3]
#     Output: 7
#     Explanation: The elements can be paired up into pairs (3,3) and (5,2).
#     The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
#
# Example 2:
#
#
#     Input: nums = [3,5,4,2,4,6]
#     Output: 8
#     Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
#     The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.
#
# Constraints:
#
# 1. `n == nums.length`
#
# 2. `2 <= n <= 10^5`
#
# 3. `n` is even.
#
# 4. `1 <= nums[i] <= 10^5`


from __future__ import annotations

from typing import List

import unittest


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        pass  # TODO: implement


class TestMinimizeMaximumPairSumInArray(unittest.TestCase):
    def test_example_1(self) -> None:
        self.assertEqual(Solution().minPairSum(nums=[3,5,2,3]), 7)

    def test_example_2(self) -> None:
        self.assertEqual(Solution().minPairSum(nums=[3,5,4,2,4,6]), 8)

    def test_edgecase(self) -> None:
        pass  # TODO add your own edge cases.


if __name__ == "__main__":
    unittest.main()
