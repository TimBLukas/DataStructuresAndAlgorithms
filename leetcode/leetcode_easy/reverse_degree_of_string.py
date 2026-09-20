"""
Leetcode 3498: Reverse Degree of a String
Given a string s, calculate its reverse degree.

The reverse degree is calculated as follows:
1. For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1)
with its position in the string (1-indexed).

2. Sum these products for all characters in the string.

Return the reverse degree of s.
"""

import string


class Solution:
    def reverseDegree(self, s: str) -> int:
        abc = string.ascii_lowercase
        reverse_degree = 0

        for i, c in enumerate(s):
            reverse_degree += (i + 1) * (26 - abc.find(c))

        return reverse_degree
