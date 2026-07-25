/**
* Leetcode 744: Find Smallest Letter greater than target
*
* You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
* There are at least two different characters in letters.
* Return the smallest character in letters that is lexicographically greater than target.
* If such a character does not exist, return the first character in letters.
*/


#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>
#include <stdio.h>

char nextGreatestLetter(char* letters, int lettersSize, char target) 
{
        char return_char = '~';

        for ( int i = 0; i < lettersSize; i++ )
        {
                if ( (letters[i] - target > 0)
                        && (( letters[i] - target ) < ( return_char - target )))
                        return_char = letters[i];
        }
    
        if ( return_char == '~')
                return_char = letters[0];

        return return_char;
}
