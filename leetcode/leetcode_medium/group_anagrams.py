"""
Leetcode 49: Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        word_grouper = {}
        for w in strs:
            s = "".join(sorted(w))
            val = word_grouper.get(s, [])
            val.append(w)
            word_grouper[s] = val

        return [v for v in word_grouper.values()]
