# Optional Imports:
# from typing import List, Optional
# import collections
import unittest


"""
Leetcode 22: Generate parenthesis

Given n pairs of parentheses, write a function to generate all combinations of well-formed
parentheses

Example:
Input n = 3
Output ["((()))", "(()())", "(())()", "()(())", "()()()"]

Example:
Input n = 2
Output ["()"], "(()())", "(())()", "()(())", "()()()"
"""

"""
Rules:
1. Always start with an opening parentheses
2. If an open parentheses is in the string, you can choose between an open and a close parentheses
3. The number of open parentheses + the number of closed parentheses can't be > n
4. There can not be more than n pairs
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate_options(s: str, num_open: int, num_close: int) -> List[str]:

            if len(s) == 2 * n:
                return [s]

            possibilities = []

            if num_open < n:
                possibilities.extend(generate_options(s + "(", num_open + 1, num_close))

            if num_close < num_open:
                possibilities.extend(generate_options(s + ")", num_open, num_close + 1))

            return possibilities

        return generate_options("", 0, 0)


if __name__ == "__main__":
    Solution().generateParenthesis(3)
