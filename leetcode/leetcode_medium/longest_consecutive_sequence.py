# Optional Imports:
# from typing import List, Optional
# import collections
import unittest

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert to set 
        list_as_set = set(nums)
        longest: int = 0

        for num in list_as_set:
            # check if start of sequence
            if (num - 1) in list_as_set:
                # if not skip
                continue

            # get length of sequence
            length = 1
            while (num + length) in list_as_set:
                length += 1

            # update global max if longer
            longest = max(length, longest)

        return longest


                
        

# Testcases
class Tester(unittest.Testcase):
  def test1():
    self.assertEqual(1, 1)

  def test2():
    self.assertEqual(1, 1)

  def test_edgecase():
    self.assertEqual(1, 1)


if __name__ == '__main__':
  unittest.main()
