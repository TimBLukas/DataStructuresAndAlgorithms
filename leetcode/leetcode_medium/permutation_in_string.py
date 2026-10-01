"""
Leetcode 567: Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
"""

from typing import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        comp = Counter(s1)
        for i in range(len(s2)):
            print(Counter(s2[i : i + len(s1)]), comp)
            if Counter(s2[i : i + len(s1)]) == comp:
                return True

        return False
