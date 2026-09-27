"""
Leetcode 23: Merge k sorted lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        head = None
        curr = None

        while any(lists):
            smallest, smallest_idx = None, None
            for i, l in enumerate(lists):
                if l and (not smallest or l.val < smallest):
                    smallest = l.val
                    smallest_idx = i
            if not head:
                head = ListNode(lists[smallest_idx].val, None)
                curr = head
            elif curr:
                curr.next = ListNode(lists[smallest_idx].val, None)
                curr = curr.next
            else:
                curr = ListNode(lists[smallest_idx].val, None)

            lists[smallest_idx] = lists[smallest_idx].next

        return head


class Solution2:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if len(lists) == 0:
            return None

        res = []
        for l in lists:
            node = l
            while node:
                res.append(node.val)
                node = node.next
        print(res)
        res.sort()
        print(res)
        if len(res) == 0:
            return None

        head = None
        curr = head
        for node_val in res:
            if not curr:
                curr = ListNode(node_val, None)
                head = curr
                continue
            curr.next = ListNode(node_val, None)
            curr = curr.next

        return head
