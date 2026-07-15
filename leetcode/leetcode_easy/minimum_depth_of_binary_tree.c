
/**
 * Leetcode 111 Minimum Depth of binary tree
 *
 * Given a binary tree, find its minimum depth
 * the minimum depth is the number of nodes along the shortest path from the
 * root node to the nearest leaf node.
 */

/**
 * Definition for a binary tree node.
 */

#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
        int val;
        struct TreeNode *left;
        struct TreeNode *right;
};

int dfs(struct TreeNode *node, int curr_depth) {
        if (node->left == NULL && node->right == NULL) {
                return curr_depth;
        } else {
                int left, right;

                if (node->left != NULL)
                        left = dfs(node->left, curr_depth + 1);

                if (node->right != NULL)
                        right = dfs(node->right, curr_depth + 1);

                if (left != NULL) {
                        if (right != NULL) {
                                if (left < right)
                                        return left;
                                return right;
                        }
                        return left;
                }
                return right;
        }
}

int minDepth(struct TreeNode *root) {
        if (root == NULL) 
                return 0;
        
        return dfs(root, 1);
}
