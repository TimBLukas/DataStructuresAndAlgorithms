"""
Leetcode 3760: Maximum Substrings With Distinct Start

You are given a string s consisting of lowercase English letters.

Return an integer denoting the maximum number of substrings you can split s
into such that each substring starts with a distinct character
(i.e., no two substrings start with the same character).
"""


class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))
