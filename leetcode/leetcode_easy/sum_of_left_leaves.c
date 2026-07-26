/**
 * Leetcode 404: Sum of Left Leaves
 *
 * Given the `root` of a binary tree, return the sum of all left leaves.
 * A leaf is a node with no children.
 * A left leaf is a leaf that is the left child of another node.
 */

#include <stdlib.h>
#include <stdio.h>


/**
 * Definition for a binary tree node.
 */
struct TreeNode 
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int dfs_left (struct TreeNode* node);
int dfs_right (struct TreeNode* node);

int dfs_left (struct TreeNode* node)
{
        if ( node->left == NULL && node->right == NULL)
                return node->val;

        int sum = 0;
        if ( node->left != NULL )
                sum += dfs_left( node->left );
        if ( node->right != NULL )
                sum += dfs_right(node->right);

        return sum;
}

int dfs_right (struct TreeNode* node)
{
        if ( node->left == NULL && node->right == NULL)
                return 0;

        int sum = 0;
        if ( node->left != NULL )
                sum += dfs_left( node->left );
        if ( node->right != NULL )
                sum += dfs_right(node->right);

        return sum;


}

int sumOfLeftLeaves(struct TreeNode* root) 
{
        int sum = 0;
        if ( root->left != NULL )    
        {
                sum += dfs_left(root->left);
        } 
        if ( root->right != NULL )    
        {
                sum += dfs_right(root->right);
        } 

        return sum;
}
