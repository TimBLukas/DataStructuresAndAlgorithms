"""
Leetcode 654: Maximum Binary Tree

You are given an integer array nums with no duplicates.
A maximum binary tree can be built recursively from nums using the following algorithm:

1. Create a root node whose value is the maximum value in nums.
2. Recursively build the left subtree on the subarray prefix to the left of the maximum value.
3. Recursively build the right subtree on the subarray suffix to the right of the maximum value.

Return the maximum binary tree built from nums.
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        max, max_idx = 0, 0
        for i, n in enumerate(nums):
            if n > max:
                max = n
                max_idx = i

        return TreeNode(
            max,
            self.constructMaximumBinaryTree(nums[0:max_idx]),
            self.constructMaximumBinaryTree(nums[max_idx + 1 :]),
        )
