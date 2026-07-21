"""
Leetcode 796: Rotate String
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
- For example, if s = "abcde", then it will be "bcdea" after one shift.
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i, c in enumerate(s):
            if c == goal[0]:
                comp = (
                    s[i : i + len(goal)]
                    if i + len(goal) < len(s)
                    else s[i:] + s[: len(goal) - (len(s) - i)]
                )
                if comp == goal:
                    return True
        return False
