"""
Given the head of a linked list head, in which each node contains an integer value.
Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.
Return the linked list after insertion.
The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
"""

from typing import Optional, List

import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev = head
        curr = head

        while curr.next:
            curr = curr.next
            new_node = ListNode(math.gcd(prev.val, curr.val), curr)
            prev.next = new_node
            prev = curr

        return head
