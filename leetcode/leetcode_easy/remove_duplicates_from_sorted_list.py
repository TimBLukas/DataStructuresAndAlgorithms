# Optional Imports:
# from typing import List, Optional
# import collections
import unittest

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr is not None and curr.next is not None:
            next = curr.next
            if curr.val == next.val:
                curr.next = next.next
                continue

            curr = curr.next

        return head


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
