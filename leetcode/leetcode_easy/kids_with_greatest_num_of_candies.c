/**
 * Leetcode 1431: Kids with the greatest Number of candies
 *
 * There are n kids with candies. You are given an integer array candies,
 * where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
 * Return a boolean array result of length n, where result[i] is true if,
 * after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
 * Note that multiple kids can have the greatest number of candies.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) 
{
        // find max
        int max = 0;

        for ( int i = 0; i < candiesSize; i++ )
                if ( candies[i] > max )
                        max = candies[i];

        // build result
        bool* can_be_greatest = (bool*)malloc(candiesSize * sizeof(bool));

        for ( int j = 0; j < candiesSize; j++ )
                if ( ( candies[j] + extraCandies ) >= max )
                        can_be_greatest[j] = true;
                else
                        can_be_greatest[j] = false;

        *returnSize = candiesSize;
        return can_be_greatest;
}
