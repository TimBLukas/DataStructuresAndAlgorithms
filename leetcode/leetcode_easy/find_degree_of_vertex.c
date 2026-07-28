/**
 * Leetcode 3898: FInd the degree of each vertex
 */ 

#include <stdlib.h>
#include <stdio.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDegrees(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) 
{
        int* degrees = malloc(matrixSize * sizeof(int));
        int cnt = 0;

        for ( int i = 0; i < matrixSize; i++ ) {
                for ( int j = 0; j < matrixColSize[i]; j++ ) {
                        if ( matrix[i][j] == 1 )
                                ++cnt;
                }

                degrees[i] = cnt;
                cnt = 0;
        }

        *returnSize = matrixSize;
        return degrees;
}
