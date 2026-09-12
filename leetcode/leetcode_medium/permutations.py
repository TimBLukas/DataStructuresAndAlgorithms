"""
Leetcode 46: Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive(start: List[int], remaining: List[int]) -> List[List[int]]:
            result = []
            if len(remaining) == 1:
                result.append(start + remaining)
                return result

            for num in remaining:
                stable = start.copy()
                stable.append(num)
                remainder = remaining.copy()
                remainder.remove(num)
                permutations = recursive(stable, remainder)
                if permutations:
                    result.extend(permutations)
            return result

        return recursive([], nums)
