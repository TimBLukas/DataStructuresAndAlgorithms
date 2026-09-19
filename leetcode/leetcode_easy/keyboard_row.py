"""
Leetcode 500: Keyboard Row

Given an array of strings words,
return the words that can be typed using letters of the alphabet
on only one row of American keyboard like the image below.
Note that the strings are case-insensitive,
both lowercased and uppercased of the same letter are treated as if they are at the same row.

In the American keyboard:
- the first row consists of the characters "qwertyuiop",
- the second row consists of the characters "asdfghjkl", and
- the third row consists of the characters "zxcvbnm".
"""


class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        first_row = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
        second_row = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
        third_row = ["z", "x", "c", "v", "b", "n", "m"]

        valid_words = []

        for word in words:
            if all(w.lower() in first_row for w in word):
                valid_words.append(word)

            elif all(w.lower() in second_row for w in word):
                valid_words.append(word)

            elif all(w.lower() in third_row for w in word):
                valid_words.append(word)

        return valid_words
