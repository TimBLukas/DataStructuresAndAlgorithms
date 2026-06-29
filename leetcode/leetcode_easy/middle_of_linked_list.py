# Optional Imports:
# from typing import List, Optional
# import collections
import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        right = left.next
        while right and right.next:
            left = left.next
            right = right.next.next

        if right:
            return left.next

        return left


# Testcases
class Tester(unittest.Testcase):
    def test1():
        self.assertEqual(1, 1)

    def test2():
        self.assertEqual(1, 1)

    def test_edgecase():
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
