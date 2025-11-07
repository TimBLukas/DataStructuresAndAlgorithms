# Leetcode 543:

"""
Problem: 543 - Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val, left, right):
        if left:
            self.left = left
        else:
            self.left = None

        if right:
            self.right = right
        else:
            self.right = None

        if self.val:
            self.val = val
        else:
            self.val = 0


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left_depth, right_depth = 0, 0
        if root.left and root.right:
            left_depth = 1 + self.diameterOfBinaryTree(root.left)
            right_depth = 1 + self.diameterOfBinaryTree(root.right)
        elif root.left and not root.right:
            left_depth = 1 + self.diameterOfBinaryTree(root.left)
        elif root.right and not root.left:
            right_depth = 1 + self.diameterOfBinaryTree(root.right)
        else:
            return 0
        return max(left_depth, right_depth, left_depth+right_depth)

class SolutionTemplate:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)          
            right = dfs(root.right)

            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)

        dfs(root)
        return res[0]

    


class TestSolution(unittest.TestCase):
    def test_1(self):
        let root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5), TreeNode(3))
        self.assertEqual(Solution().diameterOfBinaryTree(root), 3)


if __name__ == "__main__":
    unittest.main()
