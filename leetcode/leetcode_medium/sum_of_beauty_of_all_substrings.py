"""
Leetcode 1781: Sum of Beauty of All Substrings

The beauty of a string is the difference in frequencies between the most
frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.
"""


class Solution:
    def beautySum(self, s: str) -> int:
        n, ans = len(s), 0
        for i in range(n):
            beauty_score = {}
            for j in range(i, n):
                beauty_score[s[j]] = beauty_score.get(s[j], 0) + 1
                ans += max(beauty_score.values()) - min(beauty_score.values())
        return ans
