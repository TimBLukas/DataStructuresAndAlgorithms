"""
Leetcode 2108: Find First Palindromic String in the Array

Given an array of strings words, return the first palindromic string in the array.
 If there is no such string, return an empty string "".
A string is palindromic if it reads the same forward and backward.
"""

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == "".join(reversed(list(word))):
                return word
        return ""


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
        return ""