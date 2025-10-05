# Leetcode 70: Climbing Stairs

"""
Problem: You are climbing a staircase. It takes n steps to reach the top
Each time you can either climb one or two steps. In how many distinct ways can you climb to the top.

 Constraints:
    - 1 <= n <= 45
"""

import unittest


class Solution:
    def __init__(self) -> None:
        self.cache = []

    def climbStairs(self, n: int) -> int:
        for _ in reversed(range(n)):
            if len(self.cache) == 0:
                self.cache.insert(0, 1)

            elif len(self.cache) == 1:
                self.cache.insert(0, 2)

            else:
                val = self.cache[0] + self.cache[1]
                self.cache.insert(0, val)

        return self.cache[0]


class TestSolution(unittest.TestCase):
    def test_1(self):
        # Test with 2 steps
        self.assertEqual(2, Solution().climbStairs(2))

    def test_2(self):
        # Test with 3 Steps
        self.assertEqual(3, Solution().climbStairs(3))

    def test_3(self):
        # Test with 4 Steps
        self.assertEqual(5, Solution().climbStairs(4))

    def test_4(self):
        # Test with 5 Steps
        self.assertEqual(7, Solution().climbStairs(5))

    def test_5(self):
        # Test with 6 Steps
        self.assertEqual(13, Solution().climbStairs(6))

    def test_6(self):
        # Test with max Amount of Stairs
        self.assertEqual(123, Solution().climbStairs(45))


if __name__ == "__main__":
    unittest.main()
