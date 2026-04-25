# Optional Imports:
# from typing import List, Optional
# import collections
import unittest


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        tracker: dict = {}
        for i, num in enumerate(numbers):
            remainder = target - num

            # check if partner exists
            if num in tracker:
                return [tracker.get(num) + 1, i + 1]
            else:
                tracker[remainder] = i

        return []


class SolutionAlternative:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum > target:
                r -= 1

            elif curSum < target:
                l += 1

            else:
                return [l + 1, r + 1]

        return
    

# Testcases
class Tester(unittest.TestCase):
  def test1():
    self.assertEqual(Solution().twosum([2,7,11,15]), [1,2])

  def test2():
    self.assertEqual(Solution().twosum([2,3,4]), [1,3])



if __name__ == '__main__':
  unittest.main()
