/**
* Leetcode 1464: Maximum Product of Two Elements in an Array
*
* Given the array of integers nums, you will choose two different indices i and j of that array.
* Return the maximum value of (nums[i]-1)*(nums[j]-1).
*/

#include <stdio.h>
#include <stdlib.h>

int maxProduct(int* nums, int numsSize) 
{
        int val_1 = 0;
        int val_2 = 0;

        for ( int i = 0; i < numsSize; i++ )
        {
                if ( nums[i] > val_1 )
                {
                        if ( nums[i] > val_2 )
                        {
                                val_1 = val_2;
                                val_2 = nums[i];
                        }
                        else
                                val_1 = nums[i];
                }
        }

        return ( val_1 - 1 ) * ( val_2 - 1 );
}
