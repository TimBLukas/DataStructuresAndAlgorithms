#ifndef VIZGRAPH_H
#define VIZGRAPH_H

#include "graph.h"
#include "linked_list.h"
#include "trees.h"

typedef struct {
    float x;
    float y;
} Vec2;

typedef struct {
    int id;
    int value;
    Vec2 position;
    Vec2 velocity;
} VizNode;

typedef struct {
    VizNode *from;
    VizNode *to;
} VizEdge;

typedef struct {
    VizNode **nodes;
    VizEdge *edges;
} VizGraph;

VizNode *viznode_from_list_node(const ListNode *node, float x, float y,
                                float vel_x, float vel_y);

VizGraph *vizgraph_from_linked_list(const LinkedList *list, float width,
                                    float heigth);
VizGraph *vizgraph_from_binary_tree(const BinaryTree *tree, float width,
                                    float heigth);
VizGraph *vizgraph_from_ternary_tree(const TernaryTree *tree, float width,
                                     float heigth);
VizGraph *vizgraph_from_graph(const Graph *tree, float width, float height);

#endif
