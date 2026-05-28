# Optional Imports:
# from typing import List, Optional
# import collections
import unittest


"""
Leetcode 345 Reverse Vowels of a string

Given a string, reverse only the vowels of a string and return it

Example:
INput: "IceCreAm"
Output: "AceCreIm"

Example:
Input "leetcode"
Output "leotcede"
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")

        s = list(s)
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and s[l] not in vowels:
                l += 1

            while l < r and s[r] not in vowels:
                r -= 1

            s[l], s[r] = s[r], s[l]

            l += 1
            r -= 1

        return "".join(s)


if __name__ == "__main__":
    unittest.main()
