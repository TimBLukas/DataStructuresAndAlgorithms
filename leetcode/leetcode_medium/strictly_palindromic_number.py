"""
Leetcode 2396: Strictly Palindromic Number

Given an integer n, return true if n is strictly palindromic and false otherwise.
A string is palindromic if it reads the same forward and backward.
"""


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def base_is_palindromic(n: int, b: int) -> bool:
            if n == 0:
                digits = [0]
            else:
                digits = []
                while n:
                    digits.append(int(n % b))
                    n = n // b

            s = "".join(map(str, digits))
            if s == s[::-1]:
                return True
            return False

        for i in range(2, n - 1):
            if not base_is_palindromic(n, i):
                return False

        return True
