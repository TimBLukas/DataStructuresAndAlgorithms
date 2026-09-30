"""
Leetcode 295: Find Median from Data Stream

The median is the middle value in an ordered integer list.
 If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
"""

class MedianFinder:

    def __init__(self):
        self.nums = []
        self.median = 0

    def addNum(self, num: int) -> None:
        self.nums.append(num) 
        self.nums.sort()
        
        self.median = (
            self.nums[len(self.nums) // 2]
            if len(self.nums) % 2 != 0 
            else (self.nums[len(self.nums) // 2 - 1] + self.nums[len(self.nums) // 2]) / 2 
        )

    def findMedian(self) -> float:
        return self.median
        

import heapq
        
class MedianFinder2:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.median = -1.0

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            heapq.heappush(self.min_heap, heapq.heappushpop_max(self.max_heap, num))
            self.median = self.min_heap[0]
        else:
            heapq.heappush_max(self.max_heap, heapq.heappushpop(self.min_heap, num))
            print(self.min_heap)
            self.median = (self.min_heap[0] + self.max_heap[0]) / 2

    def findMedian(self) -> float:
        return self.median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()