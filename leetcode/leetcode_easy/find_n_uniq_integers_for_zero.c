/**
* Leetcode 1304: Find N Uniqu Integers Sum up to Zero
*/

#include <stdlib.h>
#include <stdio.h>

int* sumZero(int n, int* returnSize) 
{
        int* return_arr = malloc(n * sizeof(int));
        int idx = 0;

        if ( n % 2 == 0 ) {
                int start = -1 * (n / 2);
                int end = n / 2;
        

                // skip 0
                while ( start <= end ) {
                        if ( start == 0)
                                start++;
                        else
                                return_arr[idx++] = start++;
                }

        } else {
                int start = -1 * (n / 2);
                int end = n / 2;

                // keep 0
                while ( start <= end ) {
                        return_arr[idx++] = start++;
                }
        }
        *returnSize = idx;
        return return_arr;
}

