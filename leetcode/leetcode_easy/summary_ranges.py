# Optional Imports:
# from typing import List, Optional
# import collections
import unittest


# Leetcode 228
# You are given a sorted unique integer array nums
# A range [a, b] is the set of all integers from a to b (inclusive)
#
# Return the smallest sorted list of ranges that cover all the numbers in the
# array exactly. Thaat is each element of nums is vovered by exactly one of the ranges
# and there is no integer x such tat x is in one fo the ranges but not in nums
# each range should output as ("a->b") if a!= b, "a" if a==b
#
# Example
# Input: nums = [0,1,2,4,5,7], Output: ["0->2", "4->5", 7]
# Input: nums = [0,2,3,4,6,8,9], Output: ["0", "2->4", "6", "8->9"]

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l, r = 0, 1
        if len(nums) == 0:
            return []
        result = []
        while r < len(nums):
            print(l, r, result)
            if nums[r - 1] + 1 != nums[r]:
                if nums[l] == nums[r - 1]:
                    result.append(str(nums[l]))

                else:
                    result.append(f"{nums[l]}->{nums[r - 1]}")

                l = r
            r += 1

        if nums[l] == nums[-1]:
            result.append(str(nums[l]))
        else:
            result.append(f"{nums[l]}->{nums[-1]}")

        return result


if __name__ == "__main__":
    Solution().summaryRanges([0, 1, 2, 4, 5, 7])
