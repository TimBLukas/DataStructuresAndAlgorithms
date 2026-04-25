# Leetcode 26: Remove Duplicates from sorted Array
#

"""
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each
unique element appears only once.
The relative order of the elements should be kept the same. The return the number of unique elements in `nums`

- Change the array `nums` such that the first k elements of nums contain the unique elements in the order they were present in nums initially
  The remaining elements as well as the size of nums are not important
- Return k
"""

from typing import List
import unittest


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l_pointer, r_pointer, k = 0, 1, 0

        if len(nums) < 2 or set(nums) == 1:
            return 1

        while nums[r_pointer] >= nums[l_pointer]:
            print(f"Left Pointer: {nums[l_pointer]}, Right Pointer: {nums[r_pointer]}")
            if nums[l_pointer] == nums[r_pointer]:
                temp = nums.pop(r_pointer)
                nums.append(temp)
                k += 1

            else:
                l_pointer += 1
                r_pointer += 1

        return k


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 1, 2]

        self.assertEqual(Solution().removeDuplicates(nums), 2)

    def test_2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

        self.assertEqual(Solution().removeDuplicates(nums), 5)

    def test_3(self):
        nums = [1, 1]

        self.assertEqual(Solution().removeDuplicates(nums), 1)

    # def test_4(self):
    #     nums = [1, 2, 2]

    #     self.assertEqual(Solution().removeDuplicates(nums), 2)


if __name__ == "__main__":
    unittest.main()
