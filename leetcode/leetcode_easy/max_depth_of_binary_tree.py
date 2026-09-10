"""
Leetcode 104: Maximum Depth of Binary   Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recursive(node: Optional[TreeNode], depth) -> int:
            if not node.left and not node.right:
                return depth

            left, right = depth, depth
            if node.left:
                left = recursive(node.left, depth + 1)
            if node.right:
                right = recursive(node.right, depth + 1)
            return max(left, right)

        return recursive(root, 1) if root else 0
