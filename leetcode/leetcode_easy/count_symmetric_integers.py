"""
Leetcode 2843: Count Symmetric Integers

An integer x consisting of 2 * n digits is symmetric 
if the sum of the first n digits of x is equal to the sum of the last n digits of x.
Numbers with an odd number of digits are never symmetric.

Return the number of symmetric integers in the range [low, high].
"""

class Solution:
    def is_symmetric(self, n: int) -> bool:
        s = str(n)
        half = len(s) // 2
        sum1 = sum(map(int, list(s[:half])))
        sum2 = sum(map(int, list(s[half:])))
        return sum1 == sum2

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0
        for i in range(low, high+1):
            if len(s) % 2 != 0:
                continue
            if self.is_symmetric(i):
                cnt += 1
        return cnt
                