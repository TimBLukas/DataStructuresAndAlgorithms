# Optional Imports:
# from typing import List, Optional
# import collections
import unittest

from typing import List


# The majority Element is the element that appears more than [n / 2] times.
# you may assume that the majority element always exists in the array
#
# Examples:
# INput: nums = [3,2,3] -> Output: 3
# Input: nums = [2,2,1,1,1,2,2] -> Output 2
#
# The input is generated such that a majority element will exist in the array


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            count += 1 if candidate == num else -1

        return candidate


if __name__ == "__main__":
    unittest.main()
