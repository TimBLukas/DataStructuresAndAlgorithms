# Optional Imports:
# from typing import List, Optional
# import collections
import unittest

from typing import List

"""
Given an array nums containing n distinct numbers in the range [0, n], return the only
number in the range that is missing from the array.

Examples: 
Input = [3,0,1] -> 2
Input = [0,1] -> 2
Input = [6,9,4,2,3,5,7,0,1] - >8
"""

class Solution: 
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        rng = set(range(0,n + 1))
        print(rng)

        for n in nums:
            print(n)
            rng.remove(n)

        return rng.pop()

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)

        for i in range(len(nums)):
            missing ^= i ^ nums[i]
        return missing


if __name__ == '__main__':
    print(Solution().missingNumber([3,0,1])

