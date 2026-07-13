/**
 * Leetcode 976: Largest Perimeter Triangle
 * Given an integer array `nums`, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any
 * triangle of a non-zero area, return `0`
 * 
 */

 // Formula: A triangle can be build if a + b > c, with c being the largest site

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int calcPerimeter(int side_a, int side_b, int side_c) 
{
        return side_a + side_b + side_c;
}

/**
 * Requirement: Side C = longest side
 */
bool isValidTriangle(int side_a, int side_b, int side_c)
{
        return (side_a + side_b) > side_c;
}

int compare ( const void* a, const void* b)
{
        return *( (int*) b) - *( (int*) a );
}

int largestPerimeter(int* nums, int numsSize) 
{
        qsort (nums, numsSize, sizeof(int), compare);

        for ( int i=2; i < numsSize; i++ )
        {
                if ( isValidTriangle( nums[i], nums[i-1], nums[i-2] ) )
                {
                        return calcPerimeter( nums[i], nums[i-1], nums[i-2] );
                }
        }
        return 0;
}