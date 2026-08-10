#include "graph.h"

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

// struct GraphEdge
// {
//     GraphNode* destination;
//     GraphEdge* next;
// };

// --------------------------------------------------
// Node
// --------------------------------------------------

// struct GraphNode
// {
//     int value;
//
//     GraphEdge* edges;
//
//     GraphNode* next;
// };

// --------------------------------------------------
// Graph
// --------------------------------------------------

// struct Graph
// {
//     GraphNode* head;
//     int node_count;
// };

// ==================================================
// Node Functions
// ==================================================

GraphNode *graphnode_create(int value) {
    GraphNode *node = malloc(sizeof(GraphNode));

    if (node == NULL)
        return NULL;

    node->value = value;
    node->edges = NULL;
    node->next = NULL;

    return node;
}

void graphnode_destroy(GraphNode *node) {
    if (node == NULL)
        return;

    GraphEdge *edge = node->edges;

    while (edge != NULL) {
        GraphEdge *next = edge->next;
        free(edge);
        edge = next;
    }

    free(node);
}

int graphnode_get_value(const GraphNode *node) { return node->value; }

void graphnode_set_value(GraphNode *node, int value) { node->value = value; }

void graphnode_print(const GraphNode *node) {
    if (node == NULL)
        return;

    printf("%d: ", node->value);

    GraphEdge *edge = node->edges;

    while (edge != NULL) {
        printf("%d", edge->destination->value);

        if (edge->next != NULL)
            printf(" -> ");

        edge = edge->next;
    }

    printf("\n");
}
// ==================================================
// Edge Functions
// ==================================================

bool graphnode_has_edge(const GraphNode *from, const GraphNode *to) {
    if (from == NULL || to == NULL)
        return false;

    GraphEdge *edge = from->edges;

    while (edge != NULL) {
        if (edge->destination == to)
            return true;

        edge = edge->next;
    }

    return false;
}

void graphnode_add_edge(GraphNode *from, GraphNode *to) {
    if (from == NULL || to == NULL)
        return;

    // Do not allow duplicate edges
    if (graphnode_has_edge(from, to))
        return;

    GraphEdge *edge = malloc(sizeof(GraphEdge));
    if (edge == NULL)
        return;

    edge->destination = to;
    edge->next = from->edges;

    from->edges = edge;
}

void graphnode_remove_edge(GraphNode *from, GraphNode *to) {
    if (from == NULL || to == NULL)
        return;

    GraphEdge *edge = from->edges;
    GraphEdge *prev = NULL;

    while (edge != NULL) {
        if (edge->destination == to) {
            if (prev != NULL)
                prev->next = edge->next;
            else
                from->edges = edge->next;
            free(edge);
            return;
        }

        prev = edge;
        edge = edge->next;
    }
}

// ==================================================
// Graph Functions
// ==================================================

Graph *graph_create(void) {
    Graph *graph = malloc(sizeof(Graph));
    if (graph == NULL)
        return NULL;

    graph->head = NULL;
    graph->node_count = 0;

    return graph;
}

void graph_destroy(Graph *graph) {
    graphnode_destroy(graph->head);
    graph->node_count = 0;
    free(graph);
}

GraphNode *graph_add_node(Graph *graph, int value) {
    if (graph == NULL)
        return NULL;

    GraphNode *new_node = graphnode_create(value);

    if (new_node == NULL)
        return NULL;

    new_node->next = graph->head;
    graph->head = new_node;

    graph->node_count++;

    return new_node;
}

void graph_remove_node(Graph *graph, int value) {
    if (graph == NULL)
        return;

    GraphNode *target = graph_find(graph, value);

    if (target == NULL)
        return;

    // remove edges pointing to target
    GraphNode *curr = graph->head;

    while (curr != NULL) {
        graphnode_remove_edge(curr, target);
        curr = curr->next;
    }

    // Remove target from node list
    GraphNode *node = graph->head;
    GraphNode *prev = NULL;

    while (node != NULL) {
        if (node == target) {
            if (prev != NULL)
                prev->next = node->next;
            else
                graph->head = node->next;

            graph->node_count--;
            graphnode_destroy(node);
        }

        prev = node;
        node = node->next;
    }
}

GraphNode *graph_find(const Graph *graph, int value) {
    if (graph == NULL)
        return NULL;

    GraphNode *curr = graph->head;

    while (curr != NULL) {
        if (curr->value == value)
            return curr;

        curr = curr->next;
    }

    return NULL;
}

void graph_add_edge(Graph *graph, int from, int to) {
    if (graph == NULL)
        return;

    GraphNode *from_node = graph_find(graph, from);
    GraphNode *to_node = graph_find(graph, to);

    if (from_node == NULL || to_node == NULL)
        return;

    graphnode_add_edge(from_node, to_node);
}

void graph_remove_edge(Graph *graph, int from, int to) {
    if (graph == NULL)
        return;

    GraphNode *from_node = graph_find(graph, from);
    GraphNode *to_node = graph_find(graph, to);

    if (from_node == NULL || to_node == NULL)
        return;

    graphnode_remove_edge(from_node, to_node);
}

void graph_print(const Graph *graph);

int graph_size(const Graph *graph) {
    if (graph == NULL)
        return 0;

    return graph->node_count;
}

void graph_clear(Graph *graph) {
    if (graph == NULL)
        return;

    GraphNode *curr = graph->head;

    while (curr != NULL) {
        GraphNode *next = curr->next;
        graphnode_destroy(curr);
        curr = next;
    }

    graph->head = NULL;
    graph->node_count = 0;
}

// Traversals
void dfs_rec(const Graph *graph, GraphNode **visited, int *visited_count,
             GraphNode *node, int *res, int *idx) {
    visited[(*visited_count)++] = node;

    res[(*idx)++] = node->value;

    GraphEdge *edge = node->edges;

    while (edge != NULL) {
        GraphNode *destination = edge->destination;

        int already_visited = 0;

        for (int i = 0; i < *visited_count; i++) {
            if (visited[i] == destination) {
                already_visited = 1;
                break;
            }
        }

        if (!already_visited) {
            dfs_rec(graph, visited, visited_count, destination, res, idx);
        }

        edge = edge->next;
    }
}

void graph_dfs(const Graph *graph, int start) {
    GraphNode **visited = malloc(graph->node_count * sizeof(GraphNode *));

    int *res = malloc(graph->node_count * sizeof(int));

    if (visited == NULL || res == NULL) {
        free(visited);
        free(res);
        return;
    }

    int visited_count = 0;
    int idx = 0;

    GraphNode *start_node = graph->head;

    while (start_node != NULL) {
        if (start_node->value == start)
            break;

        start_node = start_node->next;
    }

    if (start_node == NULL) {
        free(visited);
        free(res);
        return;
    }

    dfs_rec(graph, visited, &visited_count, start_node, res, &idx);

    for (int i = 0; i < idx; i++)
        printf("%d ", res[i]);

    printf("\n");

    free(visited);
    free(res);
}

void graph_bfs(const Graph *graph, int start) { /* TODO */ }
