# Optional Imports:
# from typing import List, Optional
# import collections
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print_list(self, head):
        while head is not None:
            print(head.val)
            head = head.next

    def copy_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        new_head = ListNode(head.val)
        curr_old = head.next
        curr_new = new_head

        while curr_old is not None:
            curr_new.next = ListNode(curr_old.val)
            curr_old = curr_old.next
            curr_new = curr_new.next

        return new_head

    def get_reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None 

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tail = self.get_reverse_list(self.copy_list(head))
        self.print_list(tail)

        while head is not None and tail is not None:
            if not head.val == tail.val:
                return False
            head = head.next
            tail = tail.next

        return True



class SolutionAlternative:
    def get_reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None 

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def isPalindrome(self, head: Optaional[ListNode]) -> bool:
        if head is None:
            return True

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = self.get_reverse_list(slow)

        first = head
        second = second_half

        while second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True



class Tester(unittest.Testcase):
  def test1():
    self.assertEqual(1, 1)


  def test2():
    self.assertEqual(1, 1)

  def test_edgecase():
    self.assertEqual(1, 1)


if __name__ == '__main__':
  unittest.main()
