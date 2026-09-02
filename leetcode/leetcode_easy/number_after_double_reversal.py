"""
Leetcode 2119: A Number After a Double Reversal

For example, reversing 2021 gives 1202.
Reversing 12300 gives 321 as the leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2.
Return true if reversed2 equals num. Otherwise return false.
"""

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num)
        return not (len(s) > 1 and s[-1] == "0")
