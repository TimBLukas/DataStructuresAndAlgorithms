"""
Leetcode 3541: Find most frequent vowel and consonant

You are given a string s consisting of lowercase English letters ('a' to 'z').

Your task is to:

Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
Find the consonant (all other letters excluding vowels) with the maximum frequency.
Return the sum of the two frequencies.

Note: If multiple vowels or consonants have the same maximum frequency,
you may choose any one of them.
If there are no vowels or no consonants in the string, consider their frequency as 0.

The frequency of a letter x is the number of times it occurs in the string.
"""

from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = set(["a", "e", "i", "o", "u"])
        vowel_freq, consonants_freq = {}, {}
        vowel_max, consonants_max = 0, 0

        for c in s:
            if c in vowel:
                vowel_freq[c] = vowel_freq.get(c, 0) + 1

            else:
                consonants_freq[c] = consonants_freq.get(c, 0) + 1

        return max(vowel_freq.values(), default=0) + max(
            consonants_freq.values(), default=0
        )
