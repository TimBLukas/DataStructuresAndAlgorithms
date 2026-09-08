"""
Leetcode 61: Rotate List

Given the head of a linked list, rotate the list to the right by k places.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # safeguard
        if not head or not head.next:
            return head

        # Get length
        curr, length = head, 0
        while curr:
            curr = curr.next
            length += 1

        # prevent iterating overflowing
        k = k % length if k != 0 else 0
        # don't iterate if there is no step to take
        if k == 0:
            return head

        # iterate to length - (k + 1)
        cnt, curr = 0, head
        while cnt != length - (k + 1):
            curr = curr.next
            cnt += 1

        # update end and store new head
        new_head, curr.next = curr.next, None

        # find end
        curr = new_head
        while curr and curr.next:
            curr = curr.next

        # attach new head to remaining list
        curr.next = head

        # return new_head
        return new_head
