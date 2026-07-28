#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/**
 * Definition for a binary tree node.
 */

struct TreeNode 
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

 /**
  * Leetcode 257: Binary Tree Paths
  * 
  * Given the root of a binary tree, return all root-to-leaf paths in any order.
  * A leaf is a node with no children.
  */

void dfs(struct TreeNode* node, char* path, char** result, int* returnSize)
{
    if ( node == NULL )
        return;

    char currentPath[1024];

    if ( strlen(path) == 0 )
        snprintf(currentPath, sizeof(currentPath), "%d", node->val);
    else
        snprintf(currentPath, sizeof(currentPath), "%s->%d", path, node->val);

    if ( node->left == NULL && node->right == NULL ) {
        result[*returnSize] = malloc(strlen(currentPath) + 1);
        strcpy(result[*returnSize], currentPath);
        (*returnSize)++;
        return;
    }

    dfs(node->left, currentPath, result, returnSize);
    dfs(node->right, currentPath, result, returnSize);
}


char** binaryTreePaths(struct TreeNode* root, int* returnSize)
{
    *returnSize = 0;

    if (root == NULL)
        return NULL;

    char** result = malloc(sizeof(char*) * 100);

    char emptyPath[1] = "";
    dfs(root, emptyPath, result, returnSize);

    return result;
}
