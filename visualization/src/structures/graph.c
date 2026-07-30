#include "graph.h"

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>

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

GraphNode* graphnode_create(int value);

void graphnode_destroy(GraphNode* node);

int graphnode_get_value(const GraphNode* node);

void graphnode_set_value(GraphNode* node, int value);

void graphnode_print(const GraphNode* node);


// ==================================================
// Edge Functions
// ==================================================

void graphnode_add_edge(GraphNode* from, GraphNode* to);

void graphnode_remove_edge(GraphNode* from, GraphNode* to);

bool graphnode_has_edge(const GraphNode* from,
                        const GraphNode* to);


// ==================================================
// Graph Functions
// ==================================================

Graph* graph_create(void);

void graph_destroy(Graph* graph);

GraphNode* graph_add_node(Graph* graph, int value);

void graph_remove_node(Graph* graph, int value);

GraphNode* graph_find(const Graph* graph, int value);

void graph_add_edge(Graph* graph, int from, int to);

void graph_remove_edge(Graph* graph, int from, int to);

void graph_print(const Graph* graph);

int graph_size(const Graph* graph);

void graph_clear(Graph* graph);


// Traversals

void graph_dfs(const Graph* graph, int start);

void graph_bfs(const Graph* graph, int start);

