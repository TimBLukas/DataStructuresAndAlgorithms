"""
Leetcode 219: Contains Duplicate II

Given an integer array nums and an integer k,
 return true if there are two distinct indices i and j in the array 
such that nums[i] == nums[j] and abs(i - j) <= k. 
"""

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        val_idx_map = {} 
        for i, n in enumerate(nums):
            if n in val_idx_map.keys() and abs(i - val_idx_map.get(n, None)) <= k:
                return True
            
            val_idx_map[n] = i
            
        return False 
            

if __name__ == "__main__":
    print(Solution2().containsNearbyDuplicate([1,2,3,1], 3))
    print(Solution2().containsNearbyDuplicate([1,0,1,1], 1))
    print(Solution2().containsNearbyDuplicate([1,2,3,1], 3))
