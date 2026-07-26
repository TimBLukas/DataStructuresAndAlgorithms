"""
Leetcode 1207: Unique number of occurences

Given an array of integers arr,
return true if the number of occurrences of each value in the array is unique or false otherwise.
"""

from typing import List, Dict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency_map: Dict[int, int] = {}

        for i in arr:
            if i in frequency_map.keys():
                frequency_map[i] += 1
            else:
                frequency_map[i] = 1

        seen = set()
        for _, value in frequency_map.items():
            if value not in seen:
                seen.add(value)

            else:
                return False

        return True
