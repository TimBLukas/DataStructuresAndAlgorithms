# Optional Imports:
# from typing import List, Optional
# import collections
import unittest
from typing import List
from collections import Counter

# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        frequency_map = Counter(nums)

        max_length = 0

        for number, count in frequency_map.items():
            if number + 1 in frequency_map:
                harmonious_length = count + frequency_map[number + 1]
                max_length = max(harmonious_length, max_length)

        return max_length


if __name__ == "__main__":
    res: int = Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7])
    print(res)
