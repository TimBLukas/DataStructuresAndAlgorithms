/**
 * Leetcode 3427: Sum of Variable Length Subarrays
 *
 * You are given an integer array nums of size n. For each index i where 0 <= i
 * < n, define a subarray nums[start ... i] where start = max(0, i - nums[i]).
 * Return the total sum of all elements from the subarray defined for each index
 * in the array.
 */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int subarraySum(int *nums, int numsSize) {
    int sum = 0, idx = 0;

    while (idx < numsSize) {
        int start = 0 > (idx - nums[idx]) ? 0 : (idx - nums[idx]);
        printf("%d - %d\n", start, idx);

        while (start <= idx)
            sum += nums[start++];

        idx++;
    }

    return sum;
}
