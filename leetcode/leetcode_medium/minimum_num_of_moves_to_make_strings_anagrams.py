"""
Leetcode 1347: Minimum Number of Steps to Make Two Strings Anagram
Return the minimum number of steps to make t an anagram of s.
An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
"""

from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2, diff = Counter(s), Counter(t), 0

        for ch, count in c1.items():
            if count > c2.get(ch, 0):
                diff += count - c2.get(ch, 0)
        
        return diff