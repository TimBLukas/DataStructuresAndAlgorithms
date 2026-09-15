"""
Leetcode 769: Max Chunks to make sorted

You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk.
After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.
"""

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        max_val = arr[0]
        for i, n in enumerate(arr):
            max_val = max(max_val, n)

            if max_val == i:
                chunks += 1

        return chunks
