"""
Leetcode 3146: Permutation Difference between Two Strings

You are given two strings s and t such that every character occurs at most
once in s and t is a permutation of s.

The permutation difference between s and t is defined as the sum of the
absolute difference between the index of the occurrence of each character in
s and the index of the occurrence of the same character in t.

Return the permutation difference between s and t.
"""


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        char_to_idx = {}
        permutations = 0

        for i, c in enumerate(s):
            char_to_idx[c] = i

        for j, c in enumerate(t):
            permutations += abs(char_to_idx[c] - j)

        return permutations
