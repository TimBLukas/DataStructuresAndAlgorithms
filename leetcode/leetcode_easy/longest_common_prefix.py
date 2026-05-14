# Optional Imports:
# from typing import List, Optional
# import collections
import unittest

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = strs[0]

        for s in strs[1:]:
            length = min(len(longest_prefix), len(s))

            for i in range(length):
                if s[i] != longest_prefix[i]:
                    longest_prefix = longest_prefix[:i]
                    break
            else:
                longest_prefix = longest_prefix[:length]

        return longest_prefix


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
