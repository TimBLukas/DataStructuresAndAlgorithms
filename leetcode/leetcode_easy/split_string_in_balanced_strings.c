/**
* Leetcode 1221: Split a String in Balanced Strings
*
* Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
* Given a balanced string s, split it into some number of substrings such that:
* - Each substring is balanced.
* Return the maximum number of balanced strings you can obtain.
*/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int balancedStringSplit( char* s ) 
{
        int num_substrings = 0;
        int l_count = 0, r_count = 0;

        for ( int i = 0; i < strlen(s); i++ )
        {
                if ( s[i] == 'R' )
                        r_count++;

                else if ( s[i] == 'L' )
                        l_count++;

                if ( l_count == r_count )
                {
                        num_substrings++;
                        l_count = 0;
                        r_count = 0;
                }
        }
        return num_substrings;
}
