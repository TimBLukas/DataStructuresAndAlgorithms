"""
Leetcode 1614: Maximum Nesting Depth of the Parentheses

Given a valid parentheses string s, return the nesting depth of s.
The nesting depth is the maximum number of nested parentheses.
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        parenthese_stack = []
        max_depth = 0
        for c in s:
            if c == "(":
                parenthese_stack.append(c)
            elif c == ")":
                max_depth = max(max_depth, len(parenthese_stack))
                parenthese_stack.pop()
        return max_depth