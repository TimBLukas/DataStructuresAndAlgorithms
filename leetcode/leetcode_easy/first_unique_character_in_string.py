"""
Leetcode 387: First Unique character in a string

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

from dataclasses import dataclass

@dataclass
class IdxToBool:
    idx: int
    isDuplicate: bool

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Map char - isDuplicate
        char_map = {}
        
        for i, c in enumerate(s):
            if c in char_map.keys():
                char_map[c].isDuplicate = True 
            else:
                char_map[c] = IdxToBool(i, False)
            
        for key in char_map.keys():
            if not char_map[key]:
                return char_map[key].idx

        return -1