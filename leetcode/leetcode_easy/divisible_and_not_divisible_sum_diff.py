"""
Leetcode 2894. Divisible and Non-divisible Sums Difference

You are given positive integers n and m.

Define two integers as follows:

num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
Return the integer num1 - num2.
"""

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        div, non_div = 0, 0
        for i in range(1, n):
            if i % m == 0:
                div += i
            else:
                non_div += i

        return non_div - div
