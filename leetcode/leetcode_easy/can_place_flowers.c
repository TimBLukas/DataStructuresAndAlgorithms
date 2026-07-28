/**
 * Leetcode 605: Can place flowers
 * 
 * You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
 * Given an integer array `flowerbed` containing 0's and 1's, where 0 means empty and 1 means not empty and an integer n, return true
 * if n flowers can be planted without violating the no-adjecent flower rule and false otherwise.
 */

#include <stdio.h>
#include <stdbool.h>

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n)
{
        bool can_plant = true;
        int plant_spots = 0;

        for ( int i=0; i < flowerbedSize; i++ ) {
                if ( flowerbed[i] == 1 ) {
                        can_plant = false;
                } else {
                        if ( can_plant && ( i + 1 == flowerbedSize || flowerbed[i+1] == 0 ) ) {
                                ++plant_spots;
                                can_plant = false;
                        }
                        else
                        {
                                can_plant = !can_plant;
                        }
                }
        }
        return plant_spots >= n;
}
