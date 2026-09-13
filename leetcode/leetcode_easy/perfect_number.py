"""
Leetcode 507: Perfect Number

A perfect number is a positive integer that is equal to the sum of its positive divisors,
excluding the number itself.
A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.
"""

import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = []
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0 and i != num:
                divisors.append(i)

                if i != num // i and num // i != num:
                    divisors.append(num // i)

        return sum(divisors) == num
