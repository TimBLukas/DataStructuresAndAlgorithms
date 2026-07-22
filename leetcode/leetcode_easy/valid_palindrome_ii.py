"""
Leetcode 680: Valid Palindrome II

Given a string s, return true if the s can be palindrome after
deleting at most one character from it.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        deleted = False
        left, right = 0, len(s) - 1

        while left < right:
            print(left, s[left], right, s[right], deleted)
            if s[left] == s[right]:
                left += 1
                right -= 1

            elif not deleted:
                if s[left + 1] == s[right]:
                    left += 1
                elif s[right - 1] == s[left]:
                    right -= 1
                deleted = True

            else:
                return False

        return True
