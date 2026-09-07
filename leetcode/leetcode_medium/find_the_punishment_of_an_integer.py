"""
2698. Find the Punishment Number of an Integer

Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers i such that:
- 1 <= i <= n
- The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.
"""


class Solution:
    def punishmentNumber(self, n: int) -> int:
        punishment = 0
        for i in range(n):
            val = i * i
            if sum([int(c) for c in str(val)]) == i:
                punishment += val

        return punishment
