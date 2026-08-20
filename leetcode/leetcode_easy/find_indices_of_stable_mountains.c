/**
 * Leetcode 3285: Find Indices of Stable Mountains
 *
 * There are n mountains in a row, and each mountain has a height.
 * You are given an integer array height where height[i] represents the height
 * of mountain i, and an integer threshold.
 *
 * A mountain is called stable if the
 * mountain just before it (if it exists) has a height strictly greater than
 * threshold. Note that mountain 0 is not stable.
 *
 * Return an array containing the indices of all stable mountains in any order.
 *
 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include <stdio.h>
#include <stdlib.h>

int *stableMountains(int *height, int heightSize, int threshold,
                     int *returnSize) {

    int *result = malloc(heightSize * sizeof(int));
    int idx = 0;

    for (int i = 1; i < heightSize; i++) {
        if (height[i - 1] > threshold) {
            result[idx++] = i;
        }
    }

    *returnSize = idx;
    return result;
}
