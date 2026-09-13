"""
347. Top K Frequent Elements
Given an integer array nums and an integer k,
return the k most frequent elements.

You may return the answer in any order.
"""

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [el[0] for el in Counter(nums).most_common(k)]
