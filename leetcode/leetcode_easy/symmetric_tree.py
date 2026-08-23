# Optional Imports:
from typing import List, Optional

# import collections

"""
Leetcode 101: Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def _sub(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None or right is None:
                return left == right

            elif left.val == right.val:
                if left.right == right.left and left.left == right.right:
                    return _sub(left.left, right.right) and _sub(left.right and right.left)
                else:
                    return False
            else:
                return False

        if (not root) or (root.left and not root.right) or (root.right and not root.left):
            return False
        else:
            if root.left == root.right:
                return _sub(root.left, root.right)
                


if __name__ == "__main__":
    unittest.main()
