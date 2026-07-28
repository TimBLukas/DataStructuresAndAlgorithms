/**
* Leetcode 2161: Partition Array According to Given Pivot
*
* You are given a 0-indexed integer array nums and an integer pivot.
* Rearrange nums such that the following conditions are satisfied:
* Every element less than pivot appears before every element greater than pivot.
* Every element equal to pivot appears in between the elements less than and greater
* than pivot.
* The relative order of the elements less than pivot and the elements greater than
* pivot is maintained.
* More formally, consider every pi, pj where pi is the new position of the ith element
* and pj is the new position of the jth element.
* If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
* Return nums after the rearrangement.
*/

#include <stdlib.h>
#include <stdio.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* pivotArray(int* nums, int numsSize, int pivot, int* returnSize)
{
    int less_count = 0, equal_count = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < pivot) less_count++;
        else if (nums[i] == pivot) equal_count++;
    }

    int* result = malloc(numsSize * sizeof(int));
    int less_idx = 0;
    int equal_idx = less_count;
    int greater_idx = less_count + equal_count;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < pivot)
            result[less_idx++] = nums[i];
        else if (nums[i] == pivot)
            result[equal_idx++] = nums[i];
        else
            result[greater_idx++] = nums[i];
    }

    *returnSize = numsSize;
    return result;
}
