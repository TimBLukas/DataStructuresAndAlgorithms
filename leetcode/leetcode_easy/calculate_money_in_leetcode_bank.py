"""
1716. Calculate Money in Leetcode Bank

He starts by putting in $1 on Monday, the first day.
Every day from Tuesday to Sunday, he will put in $1 more than the day before.
On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
"""

class Solution:
    def totalMoney(self, n: int) -> int:
        base, curr, final, day = 1, 1, 0, 0
        while day < n:
            final += curr
            curr += 1
            if day % 7 == 6:
                base += 1
                curr = base
            day += 1
        return final