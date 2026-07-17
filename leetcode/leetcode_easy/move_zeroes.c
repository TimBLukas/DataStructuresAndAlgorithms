/**
 * Leetcode 283: Move Zeroes
 * 
 * Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
 * Note that you must do this in-place without making a copy of the array.
 */


#include <stdlib.h>
#include <stdio.h>

void moveZeroes(int* nums, int numsSize) 
{
    int i, j;
    int added_zeroes = 0;
    for (i=0; i < numsSize; i++)
    {
        if ( i >= numsSize - added_zeroes )
            return;
        else if ( nums[i] == 0 )
        {
            for (j=i + 1; j < numsSize; j++)
            {
                nums[j - 1] = nums[j];
            }
            nums[numsSize - 1] = 0;
            added_zeroes++;
            i--;
        }
    }
}

void moveZeroesTwo(int* nums, int numsSize) 
{
    int insert = 0;
    for ( int i = 0; i < numsSize; i++)
    {
        if (nums[i] != 0)
        {
            nums[insert++] = nums[i];
        }
    }

    for ( ; insert < numsSize; insert++ )
    {
        nums[insert] = 0;
    }
}