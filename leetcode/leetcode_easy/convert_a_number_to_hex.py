"""
Leetcode 405: Convert a Number to Hexadecimal

Given a 32-bit integer num, return a string representing its hexadecimal representation.
For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters,
and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.
"""

from string import ascii_lowercase


class Solution:
    def toHex(self, num: int) -> str:
        base, exp = 16, 0
        is_negative = False
        if num < 0:
            num = 2**32 + num

        val = 1
        while val * base <= num:
            val *= base
            exp += 1

        result = ""
        while exp >= 0:
            count = int(num // val)
            result += str(count) if count < 10 else ascii_lowercase[count - 10]
            num -= int(count * val)
            val //= base
            exp -= 1

        result = result.lstrip("0")

        return result if result else "0"
