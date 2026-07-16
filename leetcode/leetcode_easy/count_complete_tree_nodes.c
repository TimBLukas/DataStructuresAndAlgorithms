/**
 * Leetcode 222: Count Complete Tree Nodes
 * 
 * Given the root of a complete binary tree, return the number of the nodes in the tree.
 * According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible.
 *  It can have between 1 and 2h nodes inclusive at the last level h.
 * Design an algorithm that runs in less than O(n) time complexity.
 */

#include <stdio.h>
#include <stdlib.h>

/* Definition of Tree Node */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int dfs(struct TreeNode* node)
{
    if (node->left == NULL && node->right == NULL) 
    {
        return 1;
    }
    else
    {
        int val = 0;
        if (node->left != NULL)
            val += dfs(node->left);

        if (node->right != NULL)
            val += dfs(node->right);

        return val + 1;
    }
}

int countNodes(struct TreeNode* root) 
{
    if (root == NULL) 
        return 0;
    return dfs(root);
}