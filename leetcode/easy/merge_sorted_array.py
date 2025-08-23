from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n1 = 0
        n2 = 0
        while n2 < n:
            if nums1[n1:] == [0 for i in range(len(nums1) - n1)]:
                nums1[n1:] = nums2[n2:]
            if nums1[n1] < nums2[n2] and n1 <= m:
                n1 += 1
            else:
                nums1.insert(n1, nums2[n2])
                nums1.pop()
                n2 += 1
        print(nums1)

Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)
Solution().merge([1,4,6,7,0,0,0], 4, [2,5,6], 3)
Solution().merge([1,2,3], 3, [], 0)
Solution().merge([0], 0, [1], 1)
