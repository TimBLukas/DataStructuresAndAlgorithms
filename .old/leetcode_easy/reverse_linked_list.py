# Leetcode xx:

"""
Problem: 206 - Reverse Linked List
Given the head of a linked list, reverse the list, and return the reversed list.

"""

import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            prev_node = head
        else:
            return head

        if head.next is not None:
            new_head = head.next
            prev_node.next = None
        else:
            return head

        while new_head.next:
            temp = new_head.next

            new_head.next = prev_node
            prev_node = new_head
            new_head = temp

        new_head.next = prev_node
        return new_head


class SampleSolution:
    # T = O(n) M = O(1)
    def reverseListIterativ(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def reverseListRecursiv(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive: T = O(n), M = O(n)
        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseListRecursiv(head.next)
            head.next.next = head
        head.next = None

        return new_head


# Test do not work because diffrent objects not being equal
class TestSolution(unittest.TestCase):
    def test_1(self):
        # [1,2,3,4,5] -> Expected Result: [5,4,3,2,1]
        input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected_result = ListNode(
            5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))
        )
        self.assertEqual(expected_result, Solution().reverseList(head=input))

    def test_2(self):
        # [1,2] -> Expected Result: [2,1]
        input = ListNode(1, ListNode(2))
        expected_result = ListNode(2, ListNode(1))
        self.assertEqual(expected_result, Solution().reverseList(head=input))

    def test_with_empty_list(self):
        # [] -> Expected Result []
        expected_result = ListNode()
        self.assertEqual(expected_result, Solution().reverseList(None))


if __name__ == "__main__":
    unittest.main()
