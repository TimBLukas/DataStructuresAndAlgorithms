"""
Leetcode 424: Longest Repeating Character Replacement

You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left, max_freq, maximum_sequence = 0, 0, 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_freq = max(max_freq, counts[s[right]])

            # make window smaller as long as it is invalid
            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
            maximum_sequence = max(maximum_sequence, right - left + 1)

        return maximum_sequence
