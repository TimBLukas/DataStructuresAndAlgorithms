"""
Leetcode 242: Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)
        for letter in t:
            c[letter] -= 1

            if c[letter] < 0:
                return False

        if c.most_common(1)[0][1] > 0:
            return False

        return True


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
