#####################################
## Question 198 House Robber (medium)
#####################################

from typing import List
import unittest


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            max_not_adj: int = nums[0]
            max_adj: int = nums[1]
            max_global: int = max(max_not_adj, max_adj)

            for i in range(2, len(nums)):
                if max_not_adj + nums[i] < max_adj:
                    max_not_adj, max_adj = max_adj, max_adj
                else:
                    max_not_adj, max_adj = max_adj, max_not_adj + nums[i]

                max_global = max(max_not_adj, max_adj)

        return max_global


class Solution_Muster:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1, rob2 = rob2, temp

        return rob2


class SolutionTester(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3, 1]
        self.assertEqual(Solution().rob(nums), 4)

    def test_2(self):
        nums = [2, 7, 9, 3, 1]
        self.assertEqual(Solution().rob(nums), 12)


if __name__ == "__main__":
    unittest.main()
