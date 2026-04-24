# Optional Imports:
# from typing import List, Optional
# import collections
import unittest
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        curr = head 
        carry = 0
        while l1 or l2:
            tmp = 0
            if l1:
                tmp += l1.val
                l1 = l1.next

            if l2:
                tmp += l2.val
                l2 = l2.next

            if carry:
                tmp += carry

            pos = tmp % 10
            carry = math.floor(tmp / 10)
            

            if head is None:
                curr = ListNode(val=pos)
                head = curr
                is_first = not is_first

            else:
                curr.next = ListNode(val=pos)
                curr = curr.next

        if carry > 0:
            curr.next = ListNode(val=carry)

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
