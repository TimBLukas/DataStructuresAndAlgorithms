/**
 * Leetcode 496: Next Greater Element I
 *
 * The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
 * You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
 * For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2.
 * If there is no next greater element, then the answer for this query is -1.
 * Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
 */

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

typedef struct
{
        int key;
        int value;
} Pair;

int findValue( Pair* map, int size, int key )
{
        for ( int i = 0; i < size; i++ ) {
                if ( map[i].key == key )
                        return map[i].value;
        }
        return -1;
}

int* nextGreaterElement(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) 
{
        *returnSize = nums1Size;

        int* ans = malloc(nums1Size * sizeof(int));

        Pair* map = malloc(nums2Size * sizeof(Pair));
        int mapSize = 0;

        int* stack = malloc(nums2Size * sizeof(int));
        int top = -1;

        for ( int i = nums2Size - 1; i >= 0; i-- ) {
                while (top >= 0 && stack[top] <= nums2[i])
                        top--;

                map[mapSize].key = nums2[i];
                map[mapSize].value  =( top >= 0 ) ? stack[top] : -1;

                mapSize++;

                stack[++top] = nums2[i];
        }

        for ( int i = 0; i < nums1Size; i++ )
                ans[i] = findValue(map, mapSize, nums1[i]);

        free(map);
        free(stack);

        return ans;

}
