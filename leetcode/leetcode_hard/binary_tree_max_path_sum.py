"""
Leetcode 124: Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
 A node can only appear in the sequence at most once.
   Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from dataclasses import dataclass

@dataclass
class RecResult:
    max_subtree: int
    max_path: int

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        def recursive(child: TreeNode | None) -> RecResult:
            if child is None:
                return None

            if child.left is None and child.right is None:
                return RecResult(child.val, child.val)
            
            left_result = recursive(child.left)
            right_result = recursive(child.right)
            if left_result and right_result:
                max_subtree = max(
                    left_result.max_subtree,
                    right_result.max_subtree,
                    (max(0, left_result.max_path) + max(0, right_result.max_path) + child.val),
                    child.val
                )
                max_path = max(left_result.max_path + child.val, child.val, right_result.max_path + child.val)

            elif left_result:
                max_subtree = max(
                    left_result.max_subtree,
                    (max(0, left_result.max_path) + child.val),
                    child.val
                )
                max_path = max(left_result.max_path + child.val, child.val)

            elif right_result:
                max_subtree = max(
                    right_result.max_subtree,
                    (max(0, right_result.max_path) + child.val),
                    child.val
                )
                max_path = max(right_result.max_path + child.val, child.val)

            return RecResult(max_subtree, max_path)
        
        result = recursive(root)
        return max(result.max_path, result.max_subtree)