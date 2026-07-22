/**
 * Leetcode 101: Symmetric Tree
 * Given the root of a binary tree, check whether it is a mirror of itself 
 * (i.e., symmetric around its center).
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/**
 * Definition for a binary tree node.
 */
struct TreeNode 
{
        int val;
        struct TreeNode *left;
        struct TreeNode *right;
};

bool dfs ( struct TreeNode* left, struct TreeNode* right )
{
        if (left == NULL && right == NULL)
                return true;

        else if ((left == NULL && right != NULL) || (left != NULL && right == NULL))
              return false;

        else if (left->val == right->val)
        {
                return dfs(left->left, right->right) && dfs( left->right, right->left);
        }
        else
        {
                return false;
        }

}


bool isSymmetric(struct TreeNode* root) 
{
        if (root == NULL)
                return true;

        else if (root->left == NULL && root->right != NULL || root->left != NULL && root->right == NULL)
                return false;

        else
                return dfs ( root->left, root->right);
    
}
