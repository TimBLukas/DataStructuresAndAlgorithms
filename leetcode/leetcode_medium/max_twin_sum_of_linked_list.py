"""
Leetcode 2130: Maximum Twin Sum of a linked list


In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
"""

from typing import Optional
import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next

        left, right = 0, len(values) - 1
        mx = 0
        while left <= right:
            print(left, right, values[left], values[right])
            mx = max(mx, values[left] + values[right])
            left += 1
            right -= 1

        return mx


class Solution2:
    def reverse_llist(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        skipped = head

        while skipped and skipped.next:
            curr = curr.next
            skipped = skipped.next.next

        tail = self.reverse_llist(curr)

        mx = 0
        curr = head

        while tail:
            mx = max(mx, curr.val + tail.val)
            curr = curr.next
            tail = tail.next

        return mx
