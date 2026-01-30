########################################################
## Leetcode Problem 167 Two Sum II Input Array is Sorted
########################################################

from typing import List, Dict
import unittest


# O(n^2)
class Solution_Test:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

        return []


# O(n)
class Solution_self:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        val_to_idx: Dict[int, int] = {}
        for i, n in enumerate(numbers):
            diff: int = target - n
            if diff in val_to_idx:
                return [val_to_idx[diff], i + 1]
            val_to_idx[n] = i + 1

        return []


# O(n) - Less Memory
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer, right_pointer = 0, len(numbers) - 1
        while left_pointer < right_pointer:
            if numbers[left_pointer] + numbers[right_pointer] > target:
                right_pointer -= 1
            elif numbers[left_pointer] + numbers[right_pointer] < target:
                left_pointer += 1
            else:
                return [left_pointer + 1, right_pointer + 1]

        return []


class SolutionTester(unittest.TestCase):
    def test_1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        self.assertEqual(Solution().twoSum(numbers, target), [1, 2])

    def test_2(self):
        numbers = [2, 3, 4]
        target = 6
        self.assertEqual(Solution().twoSum(numbers, target), [1, 3])

    def test_3(self):
        numbers = [-1, 0]
        target = -1
        self.assertEqual(Solution().twoSum(numbers, target), [1, 2])


if __name__ == "__main__":
    unittest.main()
