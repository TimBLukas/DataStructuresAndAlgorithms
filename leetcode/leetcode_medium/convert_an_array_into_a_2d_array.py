"""
Leetcode 2610: Convert an Array into a 2d aray with conditions

You are given an integer array nums.
You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.
"""


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        result = [[]]
        added = False

        for n in nums:
            for i in range(len(result)):
                if n in set(result[i]):
                    continue
                result[i].append(n)
                added = True
                break
            if not added:
                result.append([n])
            added = False

        return result
