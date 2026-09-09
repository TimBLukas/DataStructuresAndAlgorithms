"""
Leetcode 231: Power of Two

Given an integer n, return true if it is a power of two.
Otherwise, return false.

An integer n is a power of two,
if there exists an integer x such that n == 2x.
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        exp = 0
        while 2**exp <= n:
            if 2**exp == n:
                return True
            exp += 1

        return False
