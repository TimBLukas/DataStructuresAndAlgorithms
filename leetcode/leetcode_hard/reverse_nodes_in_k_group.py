"""
Leetcode 25: Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time,
and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
if the number of nodes is not a multiple of k then left-out nodes,
in the end, should remain as it is.

You may not alter the values in the list's nodes,
only nodes themselves may be changed.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        cnt = 0
        curr = head
        start = None 

        while curr:
            cnt += 1
            if cnt == k:
                nxt = curr.next
                group_start = start.next if start else head

                tmp = group_start 
                prev = nxt
                while tmp is not nxt:
                    tmp_nxt = tmp.next
                    tmp.next = prev
                    prev = tmp
                    tmp = tmp_nxt

                if start is None:
                    head = prev 
                else:
                    start.next = prev 

                start = group_start
                curr = nxt
                cnt = 0

            else:
                curr = curr.next

        return head


