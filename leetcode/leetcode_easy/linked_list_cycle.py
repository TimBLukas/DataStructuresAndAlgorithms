# Optional Imports:
# from typing import List, Optional
# import collections
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen: set[ListNode] = set()
        curr = head

        while curr:
            if curr in seen:
                return True
            else:
                seen.add(curr)

            curr = curr.next

        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass



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
