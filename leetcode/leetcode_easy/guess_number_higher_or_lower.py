# Optional Imports:
# from typing import List, Optional
# import collections
#
import unittest


# Leetcode 374
# Guess number higher or lower
# Game:
# I pick a number from `1` to `n`. You have to guess which number i picked (the picked number stays the same throughout the game)
# Every time you guess wrong i will tell whether the number i picked is higher or lower than your guess

# Use the pre-defined int guess(int num), which returns three possible results:
#   -1: your guess is higher than the number
#   1: your guess is lower than the number
#   0: you guess is the number
#
# return the number that was picked


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:

    def guessNumber(self, n: int) -> int:
        l,r = 1, n

        while True:
            attempt = (l + r) // 2
            response = guess(attempt)

            if response == -1:
                r = attempt - 1
            elif response == 1:
                l = attempt +  1
            else:
                return attempt

        

        




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
