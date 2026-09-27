"""
Leetcode 55: Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if 0 not in nums or len(nums) == 1:
            return True

        idx = 0
        while idx < len(nums) - 1:
            if nums[idx] == 0:
                skipped = False
                for i in range(1, idx + 1):
                    if nums[idx - i] > i or (idx - i) + nums[idx - i] >= len(nums) - 1:
                        idx += 1
                        skipped = True
                        break
                if not skipped:
                    return False
            else:
                idx += 1
        return True
