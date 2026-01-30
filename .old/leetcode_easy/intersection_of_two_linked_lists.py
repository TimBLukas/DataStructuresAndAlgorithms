# Optional Imports:
from typing import List, Optional

# import collections
import unittest


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        while headA.next:
            headA = headA.next
            if headA == headB:
                return headA

            if headB.next:
                headB = headB.next
                if headA == headB:
                    return headB


# Testcases
class Tester(unittest.Testcase):
    def test1(self):
        self.assertEqual(1, 1)

    def test2(self):
        self.assertEqual(1, 1)

    def test_edgecase(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
