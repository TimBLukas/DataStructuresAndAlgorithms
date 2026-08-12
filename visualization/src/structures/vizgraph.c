#include "vizgraph.h"

#include <stdlib.h>

#include "graph.h"
#include "linked_list.h"
#include "trees.h"

int CURR_ID = 1;

// typedef struct {
//     float x;
//     float y;
// } Vec2;
//
// typedef struct {
//     int value;
//     Vec2 position;
//     Vec2 velocity;
// } VizNode;
//
// typedef struct {
//     VizNode *from;
//     VizNode *to;
// } VizEdge;
//
// typedef struct {
//     VizNode *head;
//     VizEdge *edges;
// } VizGraph;

VizNode *viznode_from_list_node(const ListNode *node, float x, float y,
                                float vel_x, float vel_y) {

    VizNode *viz_node = malloc(sizeof(VizNode));
    if (node == NULL)
        return NULL;

    viz_node->id = CURR_ID++;
    viz_node->position = (Vec2){x, y};
    viz_node->velocity = (Vec2){vel_x, vel_y};
    viz_node->value = node->value;

    return viz_node;
}

VizGraph *vizgraph_from_linked_list(const LinkedList *list, float width,
                                    float height) {
    VizNode *prev = NULL;
    VizNode *curr = NULL;
    VizGraph *graph = malloc(sizeof(VizGraph));
    ListNode *node = list->head;

    if (curr == NULL || prev == NULL || node == NULL || graph == NULL)
        return NULL;

    int curr_x_pos = 80;
    int y = height / 2;
    int x_pos_increment = ((width - curr_x_pos) / list->size);

    size_t node_idx = 0, edge_idx = 0;
    graph->nodes = malloc(list->size * sizeof(VizNode *));
    graph->edges = malloc((list->size - 1) * sizeof(VizEdge *));

    if (graph->nodes == NULL || graph->edges == NULL)
        return NULL;

    while (node != NULL) {
        // calculate position
        curr = viznode_from_list_node(node, curr_x_pos, y, 0, 0);
        curr_x_pos += x_pos_increment;

        graph->nodes[node_idx] = curr;

        if (node_idx != 0)
            graph->edges[node_idx++] = (VizEdge){prev, curr};

        prev = curr;
        node = node->next;
    }

    return graph;
}

VizGraph *vizgraph_from_binary_tree(const BinaryTree *tree, float width,
                                    float heigth);
VizGraph *vizgraph_from_ternary_tree(const TernaryTree *tree, float width,
                                     float heigth);
VizGraph *vizgraph_from_graph(const Graph *tree, float width, float height);
