/**
 *
 * Leetcode 2392: Build a Matrix With Conditions
 *
 * You are given a positive integer k. You are also given:
 *
 * - a 2D integer array rowConditions of size n where rowConditions[i] =
 * [abovei, belowi], and
 * - a 2D integer array colConditions of size m where colConditions[i] = [lefti,
 * righti].
 *
 * The two arrays contain integers from 1 to k.
 *
 * You have to build a k x k matrix that contains each of the numbers from 1 to
 * k exactly once. The remaining cells should have the value 0.
 *
 * The matrix should also satisfy the following conditions:
 * - The number abovei should appear in a row that is strictly above the row at
 * which the number belowi appears for all i from 0 to n - 1.
 * - The number lefti should appear in a column that is strictly left of the
 * column at which the number righti appears for all i from 0 to m - 1.
 *
 * Return any matrix that satisfies the conditions. If no answer exists, return
 * an empty matrix.
 */

#include <stdlib.h>

/**
 * Topological sort of the graph defined by conditions.
 *
 * conditions[i] = [from, to]
 *
 * Returns an array containing 1..k in topological order,
 * or NULL if the graph contains a cycle.
 */
int *topologicalSort(int **conditions, int conditionsSize, int k) {
    int *indegree = calloc(k + 1, sizeof(int));
    int **graph = malloc((k + 1) * sizeof(int *));

    for (int i = 0; i <= k; i++)
        graph[i] = calloc(k + 1, sizeof(int));

    for (int i = 0; i < conditionsSize; i++) {
        int from = conditions[i][0];
        int to = conditions[i][1];

        if (!graph[from][to]) {
            graph[from][to] = 1;
            indegree[to]++;
        }
    }

    int *queue = malloc(k * sizeof(int));
    int front = 0, back = 0;

    for (int i = 1; i <= k; i++) {
        if (indegree[i] == 0)
            queue[back++] = i;
    }

    int *order = malloc(k * sizeof(int));
    int count = 0;

    while (front < back) {
        int node = queue[front++];
        order[count++] = node;

        for (int next = 1; next <= k; next++) {
            if (graph[node][next]) {
                indegree[next]--;

                if (indegree[next] == 0)
                    queue[back++] = next;
            }
        }
    }

    if (count != k) {
        free(order);
        order = NULL;
    }

    for (int i = 0; i <= k; i++)
        free(graph[i]);

    free(graph);
    free(indegree);
    free(queue);

    return order;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 */
int **buildMatrix(int k, int **rowConditions, int rowConditionsSize,
                  int *rowConditionsColSize, int **colConditions,
                  int colConditionsSize, int *colConditionsColSize,
                  int *returnSize, int **returnColumnSizes) {

    int *rowOrder = topologicalSort(rowConditions, rowConditionsSize, k);
    int *colOrder = topologicalSort(colConditions, colConditionsSize, k);

    if (rowOrder == NULL || colOrder == NULL) {
        if (rowOrder)
            free(rowOrder);
        if (colOrder)
            free(colOrder);

        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    int **result = malloc(k * sizeof(int *));
    *returnColumnSizes = malloc(k * sizeof(int));

    for (int i = 0; i < k; i++) {
        result[i] = calloc(k, sizeof(int));
        (*returnColumnSizes)[i] = k;
    }

    /*
     * rowPos[x] = row in which number x should be placed
     * colPos[x] = column in which number x should be placed
     */
    int *rowPos = malloc((k + 1) * sizeof(int));
    int *colPos = malloc((k + 1) * sizeof(int));

    for (int i = 0; i < k; i++) {
        rowPos[rowOrder[i]] = i;
        colPos[colOrder[i]] = i;
    }

    // Place every number exactly once
    for (int number = 1; number <= k; number++) {
        result[rowPos[number]][colPos[number]] = number;
    }

    free(rowOrder);
    free(colOrder);
    free(rowPos);
    free(colPos);

    *returnSize = k;
    return result;
}
