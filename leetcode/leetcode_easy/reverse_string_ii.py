"""
Leetcode 541: Reverse String II

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them.
If there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and leave the other as original.
"""

import math


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        count = 0
        result = ""
        curr = ""

        for c in s:
            if count < k:
                curr = c + curr
                count += 1

            else:
                curr += c
                count += 1

            if count % (2 * k) == 0:
                count = 0
                result += curr
                curr = ""

        return result + curr


class Solution2:
    def reverseStr(self, s: str, k: int) -> str:
        splits = math.floor(len(s) / k)
        result = ""

        for i in range(0, splits):
            sub = s[i * k : (i + 1) * k]
            print(sub)
            if i % 2 != 0:
                result = result + sub

            else:
                result = result + sub[::-1]

        return (
            result + s[splits * k :]
            if splits % 2 != 0
            else result + s[splits * k : :][::-1]
        )
