"""
Leetcode 819: Most Common Word

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned.
It is guaranteed there is at least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Note that words can not contain punctuation symbols.
"""

from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.strip()

        chars_to_remove = set(['"', "!", "?", "'", ",", ";", "."])
        paragraph = "".join(
            c if c not in chars_to_remove else " " for c in paragraph
        ).lower()

        words = [word for word in paragraph.split() if word not in banned]

        counter = Counter(words)
        return counter.most_common(1)[0][0]
