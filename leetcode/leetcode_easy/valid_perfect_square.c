/**
 * Leetcode 367: Valid Perfect Square
 * 
 * Given a positive integer num, return `true` is a perfect square or `false` otherwise
 * 
 * A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
 * Do not use built-in library functions
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#include <stdbool.h>

bool isPerfectSquare(int num)
{
    if ( num < 0 )
        return false;

    long long left = 0;
    long long right = num;

    while ( left <= right ) {
        long long mid = left + (right - left) / 2;
        long long square = mid * mid;

        if (square == num)
            return true;
        else if (square < num)
            left = mid + 1;
        else
            right = mid - 1;
    }

    return false;
}
