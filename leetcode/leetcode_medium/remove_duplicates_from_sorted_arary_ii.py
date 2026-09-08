"""
Leetcode 80: Remove Duplciates from Sorted Array II

Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        el, sc, cnt, i, added = None, 0, 0, 0, 0

        while i < len(nums) - added:
            if el == nums[i]:
                sc += 1
                if sc > 2:
                    added += 1
                    nums.pop(i)
                    nums.append(el)
                else:
                    i += 1
            else:
                cnt += sc if sc <= 2 else 2
                el = nums[i]
                sc = 1
                i += 1
        cnt += sc if sc <= 2 else 2

        return cnt


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        read, write, length = 1, 1, len(nums)
        same_count, ref, n = 1, nums[0], 0

        while read < len(nums):
            n = nums[read]
            if n == ref:
                same_count += 1
                if same_count > 2:
                    read += 1
                    continue
            else:
                same_count = 1
                ref = n
            nums[write] = n
            read += 1
            write += 1

        return length - (read - write)
