"""
Leetcode 1004: Max Consecutive Ones III

Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left, right, r_cnt = 0, 0, 0
        max_len = 0

        while right < len(nums):
            if r_cnt <= k:
                if nums[right] == 0:
                    r_cnt += 1
                right += 1
            while r_cnt > k:
                if nums[left] == 0:
                    r_cnt -= 1
                left += 1
            max_len = max_len(max_len, right - left)

        return max_len 