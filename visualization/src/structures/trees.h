#ifndef TREES_H 
#define TREES_H 

// Node Definitions
// ------------------------------
typedef struct BinaryTreeNode
{
        int value;
        struct BinaryTreeNode* left;
        struct BinaryTreeNode* right;
} BinaryTreeNode;

typedef struct TernaryTreeNode
{
        int value;
        struct TernaryTreeNode* left;
        struct TernaryTreeNode* center;
        struct TernaryTreeNode* right;
} TernaryTreeNode;


typedef struct NaryTreeNode
{
        int value;
        struct NaryTreeNode** children;
        int child_count;
} NaryTreeNode;


// Tree Definitions
// ------------------------------
typedef struct
{
        BinaryTreeNode* root;
} BinaryTree;


typedef struct
{
        TernaryTreeNode* root;
} TernaryTree;


typedef struct
{
        NaryTreeNode* root;
} NaryTree;



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
BinaryTreeNode* binarynode_create(int value);

void binarynode_destroy(BinaryTreeNode* node);


// Access
// ------------------------------
int binarynode_get_value(const BinaryTreeNode* node);

void binarynode_set_value(BinaryTreeNode* node, int value);


// Children
// ------------------------------
BinaryTreeNode* binarynode_get_left(const BinaryTreeNode* node);

BinaryTreeNode* binarynode_get_right(const BinaryTreeNode* node);

void binarynode_set_left(BinaryTreeNode* node, BinaryTreeNode* left);

void binarynode_set_right(BinaryTreeNode* node,BinaryTreeNode* right);

// Utility
// ------------------------------
void binarynode_print(const BinaryTreeNode* node);

/**
* Ternary Tree Node
*/
// Creation / Destruction
TernaryTreeNode* ternarynode_create(int value);

void ternarynode_destroy(TernaryTreeNode* node);


// Access
int ternarynode_get_value(const TernaryTreeNode* node);

void ternarynode_set_value(TernaryTreeNode* node, int value);


// Children

TernaryTreeNode* ternarynode_get_left(const TernaryTreeNode* node);

TernaryTreeNode* ternarynode_get_center(const TernaryTreeNode* node);

TernaryTreeNode* ternarynode_get_right(const TernaryTreeNode* node);



void ternarynode_set_left(TernaryTreeNode* node, TernaryTreeNode* child);


void ternarynode_set_center(TernaryTreeNode* node, TernaryTreeNode* child);


void ternarynode_set_right(TernaryTreeNode* node, TernaryTreeNode* child);


void ternarynode_print(const TernaryTreeNode* node);

/**
* N-Ary Tree Node
*/
NaryTreeNode* narynode_create(int value);

void narynode_destroy(NaryTreeNode* node);

// Value
int narynode_get_value(const NaryTreeNode* node);

void narynode_set_value(NaryTreeNode* node, int value);


// Children
void narynode_add_child(NaryTreeNode* node, NaryTreeNode* child);

void narynode_remove_child(NaryTreeNode* node, int index);

NaryTreeNode* narynode_get_child(const NaryTreeNode* node, int index);

int narynode_child_count(const NaryTreeNode* node);

void narynode_print(const NaryTreeNode* node);


/**
 *
* Tree Functions
*
*/

/**
* Binary Tree 
*/
// Creation / Destruction
BinaryTree* binarytree_create(void);

void binarytree_destroy(BinaryTree* tree);


// Modification
void binarytree_insert(BinaryTree* tree, int value);

void binarytree_remove(BinaryTree* tree, int value);

// Search
BinaryTreeNode* binarytree_find(BinaryTree* tree, int value);

// Traversal
void binarytree_preorder(BinaryTreeNode* root);

void binarytree_inorder(BinaryTreeNode* root);

void binarytree_postorder(BinaryTreeNode* root);

void binarytree_levelorder(BinaryTreeNode* root);


// Information
int binarytree_height(BinaryTreeNode* root);

int binarytree_size(BinaryTreeNode* root);


// Visualization helper
void binarytree_print(const BinaryTree* tree);

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

#endif
