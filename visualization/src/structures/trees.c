#include "trees.h"

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 1000

/**
 * HELPER TYPESs
 */

typedef struct 
{
        BinaryTreeNode* node;
        int level;
} BinaryTreeSearchResult;

typedef struct {
        BinaryTreeNode* items[MAX_SIZE];
        int front;
        int rear;
} BinaryTreeNodeQueue;

// Queue functions
BinaryTreeNodeQueue* binary_tree_node_queue_initialize()
{
        BinaryTreeNodeQueue* q = malloc(sizeof(BinaryTreeNodeQueue));
        q->front = 0;
        q->rear = 0;

        return q;
}

bool binary_tree_node_queue_is_empty(BinaryTreeNodeQueue* q)
{
        return (q->front == q->rear);
}

bool binary_tree_node_queue_is_full(BinaryTreeNodeQueue* q)
{
        return (q->rear == MAX_SIZE);
}

void binary_tree_node_queue_enqueue(BinaryTreeNodeQueue* q, BinaryTreeNode* node)
{
        if (binary_tree_node_queue_is_full(q)) {
                return;
        }
        q->items[q->rear] = node;
        q->rear++;
}

BinaryTreeNode* binary_tree_node_queue_dequeue(BinaryTreeNodeQueue* q)
{
        if (binary_tree_node_queue_is_empty(q))
                return NULL;

        q->front++;
        return q->items[q->front-1];
}

BinaryTreeNode* binary_tree_node_queue_peek(BinaryTreeNodeQueue *q)
{
        if (binary_tree_node_queue_is_empty(q))
                return NULL;

        return q->items[q->front];
}

void binary_tree_node_queue_free(BinaryTreeNodeQueue *q)
{
        free(q);
}


/**
 *
* Tree Node Functions
*
*/

/**
* Binary Tree Node
*/
// Creation / Destruction
// ------------------------------
BinaryTreeNode* binarynode_create(int value)
{
        BinaryTreeNode* node = malloc(sizeof(BinaryTreeNode));
        if ( node == NULL )
                return NULL;

        node->value = value;
        node->left = NULL;
        node->right = NULL;

        return node;
}

void binarynode_destroy(BinaryTreeNode* node) 
{
        if ( node == NULL )
                return;

        binarynode_destroy(node->left);
        binarynode_destroy(node->right);

        free(node);
}


// Access
// ------------------------------
inline int binarynode_get_value(const BinaryTreeNode* node) 
{
        return node->value;
}

void binarynode_set_value(BinaryTreeNode* node, int value)
{
        node->value = value;
}


// Children
// ------------------------------
BinaryTreeNode* binarynode_get_left(const BinaryTreeNode* node)
{
        return node ? node->left : NULL;
}

BinaryTreeNode* binarynode_get_right(const BinaryTreeNode* node)
{
        return node ? node->right : NULL;
}

void binarynode_set_left(BinaryTreeNode* node, BinaryTreeNode* left)
{
        if ( node )
                node->left = left;
}

void binarynode_set_right(BinaryTreeNode* node,BinaryTreeNode* right)
{
        if ( node )
                node->right = right;
}


// Utility
// ------------------------------

static void binary_print_helper(const BinaryTreeNode *node, int depth)
{
    if (node == NULL)
        return;

    // Indentation
    for (int i = 0; i < depth; i++)
        printf("    ");

    printf("%d\n", node->value);

    binary_print_helper(node->left, depth + 1);
    binary_print_helper(node->right, depth + 1);
}

void binarynode_print(const BinaryTreeNode *node)
{
    binary_print_helper(node, 0);
}


/**
* Ternary Tree Node
*/
// Creation / Destruction
TernaryTreeNode* ternarynode_create(int value)
{
        TernaryTreeNode* node = malloc(sizeof(TernaryTreeNode));
        if ( node == NULL )
                return NULL;

        node->value = value;
        node->left = NULL;
        node->center = NULL;
        node->right = NULL;

        return node;
}

void ternarynode_destroy(TernaryTreeNode* node)
{
        if ( node == NULL )
                return;

        ternarynode_destroy(node->left);
        ternarynode_destroy(node->center);
        ternarynode_destroy(node->right);

        free(node);
}


// Access
int ternarynode_get_value(const TernaryTreeNode* node)
{
        return node->value;
}

void ternarynode_set_value(TernaryTreeNode* node, int value)
{
        if ( node )
                node->value = value;
}


// Children
TernaryTreeNode* ternarynode_get_left(const TernaryTreeNode* node)
{
        if ( node != NULL && node->left != NULL )
                return node->left;
        return NULL;
}

TernaryTreeNode* ternarynode_get_center(const TernaryTreeNode* node)
{
        if ( node != NULL && node->center != NULL )
                return node->center;
        return NULL;
}

TernaryTreeNode* ternarynode_get_right(const TernaryTreeNode* node)
{
        if ( node != NULL && node->right != NULL )
                return node->right;
        return NULL;
}


void ternarynode_set_left(TernaryTreeNode* node, TernaryTreeNode* child)
{
        if ( node )
                node->left = child;
}


void ternarynode_set_center(TernaryTreeNode* node, TernaryTreeNode* child)
{
        if ( node )
                node->center= child;
}

void ternarynode_set_right(TernaryTreeNode* node, TernaryTreeNode* child)
{
        if ( node )
                node->right = child;
}


static void ternary_print_helper(const TernaryTreeNode *node, int depth)
{
    if (node == NULL)
        return;

    for (int i = 0; i < depth; i++)
        printf("    ");

    printf("%d\n", node->value);

    ternary_print_helper(node->left, depth + 1);
    ternary_print_helper(node->center, depth + 1);
    ternary_print_helper(node->right, depth + 1);
}

void ternarynode_print(const TernaryTreeNode *node)
{
    ternary_print_helper(node, 0);
}

/**
* N-Ary Tree Node
*/
NaryTreeNode* narynode_create(int value)
{
        NaryTreeNode* node = malloc(sizeof(NaryTreeNode));
        if ( node == NULL )
                return NULL;

        node->value = value;
        node->child_count = 0;
        node->children = NULL;
        return node;
}

void narynode_destroy(NaryTreeNode* node)
{
        for ( int i = 0; i < node->child_count; i++ )
                narynode_destroy(node->children[i]);

        node->child_count = 0;
        free(node->children);
        free(node);
}

// Value
int narynode_get_value(const NaryTreeNode* node)
{
        return node->value;
}

void narynode_set_value(NaryTreeNode* node, int value)
{
        if ( node != NULL )
                node->value = value;
}


// Children
void narynode_add_child(NaryTreeNode* node, NaryTreeNode* child)
{
        if ( node == NULL )
                return;

        node->children = realloc( node->children, (node->child_count + 1) * sizeof(NaryTreeNode*));

        node->children[node->child_count] = child;
        node->child_count++;
}

void narynode_remove_child(NaryTreeNode* node, int index)
{
        if ( node == NULL || index >= node->child_count )
                return;

        narynode_destroy(node->children[index]);
        
        for ( int i = index; i < node->child_count - 1; i++ ) {
                node->children[i] = node->children[i+1];
        }

        node->child_count--;

        node->children = realloc(node->children, node->child_count * sizeof(NaryTreeNode*));
}

NaryTreeNode* narynode_get_child(const NaryTreeNode* node, int index)
{
        if ( node != NULL )
                return index < node->child_count ? node->children[index] : NULL;
        return NULL;
}

int narynode_child_count(const NaryTreeNode* node)
{
        return node == NULL ? 0 : node->child_count;
}

void nary_print_helper(const NaryTreeNode* node, int depth)
{
    if (node == NULL)
        return;

    for (int i = 0; i < depth; i++)
        printf("    ");

    printf("%d\n", node->value);

    for (int i = 0; i < node->child_count; i++)
        nary_print_helper(node->children[i], depth + 1);
}

void narynode_print(const NaryTreeNode* node)
{
        nary_print_helper(node, 0);
}


/**
 *
* Tree Functions
*
*/

/**
* Binary Tree 
*/
// Creation / Destruction
BinaryTree* binarytree_create(void)
{
        BinaryTree* tree = malloc(sizeof(BinaryTree));
        if ( tree == NULL )
                return NULL;

        tree->root = NULL;

        return tree;
}

void binarytree_destroy(BinaryTree* tree)
{
        if ( tree ) {
                binarynode_destroy(tree->root);
                free(tree);
        }
}


static BinaryTreeNode* binary_insert_helper (BinaryTreeNode* root, int value)
{
        if ( root == NULL )
                return binarynode_create(value);
        
        if ( value < root->value )
                root->left = binary_insert_helper(root->left, value);

        else
                root->right = binary_insert_helper(root->right, value);

        return root;

}

// Modification
void binarytree_insert(BinaryTree* tree, int value)
{
        tree->root = binary_insert_helper(tree->root, value);
}

static BinaryTreeNode* binarytree_min(BinaryTreeNode* node)
{
    while (node->left != NULL)
        node = node->left;

    return node;
}

static BinaryTreeNode* binarytree_remove_helper(BinaryTreeNode* root, int value)
{
    if (root == NULL)
        return NULL;

    if (value < root->value)
        root->left = binarytree_remove_helper(root->left, value);

    else if (value > root->value)
        root->right = binarytree_remove_helper(root->right, value);

    else {
        if (root->left == NULL && root->right == NULL) {
            free(root);
            return NULL;
        }

        if (root->left == NULL) {
            BinaryTreeNode* temp = root->right;
            free(root);
            return temp;
        }

        if (root->right == NULL) {
            BinaryTreeNode* temp = root->left;
            free(root);
            return temp;
        }

        BinaryTreeNode* successor = binarytree_min(root->right);

        root->value = successor->value;

        root->right = binarytree_remove_helper(root->right, successor->value);
    }

    return root;
}

void binarytree_remove(BinaryTree* tree, int value)
{
        if ( tree == NULL )
                return;
        tree->root = binarytree_remove_helper(tree->root, value);
}


// Search
static BinaryTreeSearchResult binarytree_find_helper(BinaryTreeNode* node, int value, int level)
{
    BinaryTreeSearchResult result;

    if (node == NULL) {
        result.node = NULL;
        result.level = -1;
        return result;
    }

    if (node->value == value) {
        result.node = node;
        result.level = level;
        return result;
    }

    if (value < node->value)
        return binarytree_find_helper(node->left, value, level + 1);

    return binarytree_find_helper(node->right, value, level + 1);
}

BinaryTreeNode* binarytree_find(BinaryTree* tree, int value)
{
    if (tree == NULL || tree->root == NULL)
        return NULL;

    return binarytree_find_helper(tree->root, value, 0).node;
}


// Traversal
void binarytree_preorder(BinaryTreeNode* root)
{
    if (root == NULL)
        return;

    printf("%d ", root->value);

    binarytree_preorder(root->left);
    binarytree_preorder(root->right);
}

void binarytree_inorder(BinaryTreeNode* root)
{
    if (root == NULL)
        return;

    binarytree_inorder(root->left);

    printf("%d ", root->value);

    binarytree_inorder(root->right);
}

void binarytree_postorder(BinaryTreeNode* root)
{
    if (root == NULL)
        return;

    binarytree_postorder(root->left);

    binarytree_postorder(root->right);

    printf("%d ", root->value);
}

void binarytree_levelorder(BinaryTreeNode* root)
{
        BinaryTreeNodeQueue* q = binary_tree_node_queue_initialize();

        binary_tree_node_queue_enqueue(q, root);

        while ( !binary_tree_node_queue_is_empty(q)) {
                BinaryTreeNode* node = binary_tree_node_queue_dequeue(q);
                printf("%d ", node->value);

                if ( node->left != NULL ) 
                        binary_tree_node_queue_enqueue(q, node->left);

                if ( root->right != NULL ) 
                        binary_tree_node_queue_enqueue(q, node->right);
        }

        binary_tree_node_queue_free(q);
}


// Information

int binarytree_height(BinaryTreeNode* root)
{
        if ( root == NULL )
                return 0;

        int left = binarytree_height(root->left);
        int right = binarytree_height(root->right);

        return (left > right ? left : right) + 1;
}

int binarytree_size(BinaryTreeNode* root)
{
        if ( root == NULL )
                return 0;

        return 1 + binarytree_size(root->left) + binarytree_size(root->right);
}


// Visualization helper
void binarytree_print(const BinaryTree* tree) 
{
        if ( tree == NULL )
                return;

        binarynode_print(tree->root);
}

/**
* Ternary Tree 
*/
TernaryTree* ternarytree_create(void);

void ternarytree_destroy(TernaryTree* tree);


void ternarytree_insert(TernaryTree* tree, int value);


TernaryTreeNode* ternarytree_find(TernaryTree* tree, int value);


void ternarytree_preorder(TernaryTreeNode* root);


void ternarytree_postorder(TernaryTreeNode* root);


int ternarytree_height(TernaryTreeNode* root);


int ternarytree_size(TernaryTreeNode* root);


void ternarytree_print(const TernaryTree* tree);

/**
* N-Ary Tree 
*/
NaryTree* narytree_create(void);

void narytree_destroy(NaryTree* tree);

void narytree_insert(NaryTree* tree, int value);

NaryTreeNode* narytree_find(NaryTree* tree, int value);

void narytree_preorder(NaryTreeNode* root);

void narytree_postorder(NaryTreeNode* root);

void narytree_levelorder(NaryTreeNode* root);

int narytree_height(NaryTreeNode* root);

int narytree_size(NaryTreeNode* root);

void narytree_print(const NaryTree* tree);

