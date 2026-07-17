"""
Leetcode 383: Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            idx: int = magazine.find(c) 
            if idx == -1:
                return False

            magazine = magazine[0:idx - 1] + magazine[idx:]

        return True
