"""
Leetcode 100: Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None or q == None:
            return p == q
        elif p.val == q.val:
            left_identical, right_identical = False, False
            if p.left and q.left:
                left_identical = self.isSameTree(p.left, q.left)
            elif not p.left and not q.left:
                left_identical = True
            else:
                left_identical = False

            if p.right and q.right:
                right_identical = self.isSameTree(p.right, q.right)
            elif not p.right and not q.right:
                right_identical = True
            else:
                right_identical = False

            if right_identical and left_identical:
                return True
            else:
                return False

        return False
