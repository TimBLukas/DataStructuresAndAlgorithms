"""
Leetcode 1669: Merge In Between Linked Lists

Remove list1's nodes from the ath node to the bth node,
and put list2 in their place.
The blue edges and nodes in the following figure indicate the result:
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # find start and end of insertion
        cnt = 0
        node_a, node_b, curr = None, None, list1
        while cnt < a - 1:
            curr = curr.next
            cnt += 1
        node_a = curr
        while cnt < b:
            curr = curr.next
            cnt += 1
        node_b = curr.next

        # update pointers
        node_a.next = list2
        curr = list2
        while curr.next:
            curr = curr.next
        curr.next = node_b

        return list1






        