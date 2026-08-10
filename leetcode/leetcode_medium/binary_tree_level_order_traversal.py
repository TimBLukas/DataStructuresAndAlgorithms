"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bfs(self, nodes: List[Optional[TreeNode]]) -> List[List[int]]:
        input = []
        curr_level = []

        for node in nodes:
            if node and node.left:
                input.append(node.left)
            if node and node.right:
                input.append(node.right)

            curr_level.append(node.val)

        if len(input) == 0:
            return [curr_level]

        result = self.bfs(input)
        result.insert(0, curr_level)
        return result

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        return self.bfs([root])
