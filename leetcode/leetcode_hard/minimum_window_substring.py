"""
Leetcode 76: Minimum Window Substring
Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        open_chars = list(t)
        solution = None

        while right < len(s):
            if s[right] in open_chars:
                open_chars.remove(s[right])

            while len(open_chars) == 0:
                if solution is None or right - left + 1 < len(solution):
                    solution = s[left : right + 1]

                if s[left] in t:
                    window_count = s[left + 1 : right + 1].count(s[left])
                    required_count = t.count(s[left])

                    if window_count < required_count:
                        open_chars.append(s[left])

                left += 1
            right += 1

        return solution if solution else ""
