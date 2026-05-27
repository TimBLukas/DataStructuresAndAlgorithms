# Optional Imports:
# from typing import List, Optional
# import collections
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def _sub(node: TreeNode):
            if node.left is not None:
                pass


if __name__ == "__main__":
    unittest.main()
