# Optional Imports:
# from typing import List, Optional
# import collections
import unittest


"""
Leetcode Nr 3:
Given a string `s`, find the length of the longest substring without duplicate characters

Example 1:
input s = "abcabcbb"
output = 3

Example 2:
input = "bbbbb"
output = 1

Example 3:
intput = "pwwkew"
output = 3
"""


class Solution:
    def lengthOfLongestSubstring2(self, s: str) -> int:
        pass

    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1
        longest = 1 if s else 0
        while left <= right and left <= len(s) and right <= len(s):
            longest = max(len(set(s[left:right])), longest)
            if len(set(s[left:right])) != len(s[left:right]):
                if left == right:
                    right += 1
                left += 1
                print(longest)

            else:
                right += 1

        return longest


if __name__ == "__main__":
    unittest.main()
