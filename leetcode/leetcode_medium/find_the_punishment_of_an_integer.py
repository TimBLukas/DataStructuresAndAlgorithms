"""
2698. Find the Punishment Number of an Integer

Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers i such that:
- 1 <= i <= n
- The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.
"""


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def is_valid_partition(s, target, index=0, total=0) -> bool:
            if index == len(s):
                return total == target

            for j in range(index, len(s)):
                num = int(s[index : j + 1])

                if is_valid_partition(s, target, j + 1, total + num):
                    return True
            return False

        punishment = 0
        for i in range(1, n + 1):
            value = i * i
            if is_valid_partition(str(value), i):
                punishment += value

        return punishment
