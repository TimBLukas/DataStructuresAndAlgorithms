"""
Leetcode 402: Remove k digits

Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.
"""


class Solution2:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        while k > 0:
            stack.pop()
            k -= 1

        result = "".join(stack).lstrip("0")

        return result if result else "0"
