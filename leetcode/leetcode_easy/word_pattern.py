"""
Leetcode 290: Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

- Each letter in pattern maps to exactly one unique word in s.
- Each unique word in s maps to exactly one letter in pattern.
- No two letters map to the same word, and no two words map to the same letter.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letter_to_word = {}
        word_list = s.split(" ")

        for i, c in enumerate(pattern):
            if c not in letter_to_word.keys():
                letter_to_word[c] = word_list[i]
            
        compare_string = ""

        for letter in pattern:
            compare_string += word_list.get(letter) + " "

        if compare_string.trim() == s:
            return True
        
        return False


