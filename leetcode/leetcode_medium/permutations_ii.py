"""
Leetcode 47: Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def recursive(start: List[int], remaining: List[int]) -> None:
            if len(remaining) == 1:
                permutation = start + remaining
                if permutation not in result:
                    result.append(permutation)
                return

            for num in remaining:
                stable, remainder = start.copy(), remaining.copy()
                stable.append(num)
                remainder.remove(num)

                permutations = recursive(stable, remainder)
                if permutations:
                    result.extend(permutations)

        recursive([], nums)
        return result


class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(path, used)

                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))
        return result
