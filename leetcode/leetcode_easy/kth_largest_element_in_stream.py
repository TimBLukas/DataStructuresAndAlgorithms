# Optional Imports:
# from typing import List, Optional
# import collections
import unittest

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with k largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) # O(n)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]
        


# Problem:
# - Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
