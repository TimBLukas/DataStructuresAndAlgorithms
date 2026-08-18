"""
Leetcode 3945: Digit Frequency Score

You are given an integer n.

The score of n is defined as the sum of d * freq(d) over all distinct digits d,
where freq(d) denotes the number of times the digit d appears in n.

Return an integer denoting the score of n.
"""

from collections import Counter


class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s = str(n)
        cntr = Counter(s)
        score = 0

        for digit in cntr:
            score += cntr[digit] * int(digit)

        return score
