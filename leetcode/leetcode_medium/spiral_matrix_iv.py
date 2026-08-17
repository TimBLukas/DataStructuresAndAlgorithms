"""
Leetcode 2326: Spiral Matrix IV

You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1] * n for _ in range(m)]

        left, right = 0, n - 1
        top, bottom = 0, m - 1

        curr = head

        while curr:
            for col in range(left, right + 1):
                if not curr:
                    break
                result[top][col] = curr.val
                curr = curr.next
            top += 1

            for row in range(top, bottom + 1):
                if not curr:
                    break
                result[row][right] = curr.val
                curr = curr.next
            right -= 1

            for col in range(right, left - 1, -1):
                if not curr:
                    break
                result[bottom][col] = curr.val
                curr = curr.next
            bottom -= 1

            for row in range(bottom, top - 1, -1):
                if not curr:
                    break
                result[row][left] = curr.val
                curr = curr.next
            left += 1

        return result
