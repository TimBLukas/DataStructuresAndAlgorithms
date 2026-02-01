# Given an array of integers `nums` sorted in non decreasing order, find the starting and ending position of a given `target` value.
# If `target` is not found, return [-1, -1]
#
# Example:
# Input: nums = [5,7,7,8,8,10], target = 8
# Ouput: [3,4]

from typing import List
import unittest


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Search Position
        low = 0
        high = len(nums) - 1
        target_idx_low = -1
        target_idx_high = -1

        while low <= high:
            medium = (low + high) // 2
            guess = nums[medium]

            if guess == target:
                target_idx_low = medium
                target_idx_high = medium
                break

            elif guess < target:
                low = medium + 1

            elif guess > target:
                high = medium - 1

        if target_idx_low == -1 or target_idx_high == -1:
            return [target_idx_low, target_idx_high]

        # Detect Range
        for i in range(target_idx_low, -1, -1):
            if nums[i] != target:
                break
            else:
                target_idx_low = i

        for i in range(target_idx_high, len(nums)):
            if nums[i] != target:
                break
            else:
                target_idx_high = i

        return [target_idx_low, target_idx_high]


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        self.assertEqual([3, 4], Solution().searchRange(nums, target))

    def test_2(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        self.assertEqual([-1, -1], Solution().searchRange(nums, target))

    def test_3(self):
        nums = []
        target = 0
        self.assertEqual([-1, -1], Solution().searchRange(nums, target))

    def test_4(self):
        nums = [2, 2]
        target = 2
        self.assertEqual([0, 1], Solution().searchRange(nums, target))


if __name__ == "__main__":
    unittest.main()
