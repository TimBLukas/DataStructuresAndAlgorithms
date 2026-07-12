"""
Leetcode 112 Path Sum

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up 
all the values along the path equals `targetSum`

Example:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: TreeNode, curr_sum: int):
            if node.left is None and node.right is None:
                return curr_sum + node.val == targetSum

            else:
                left, right = False, False
                if node.left is not None:
                    left = dfs(node.left, curr_sum + node.val)

                if node.right is not None:
                    right = dfs(node.right, curr_sum + node.val)

                if left or right:
                    return True
                return False


        return dfs(root, 0) if root is not None else False

        

