/**
* Leetcode 2315:  Count Asterisks
*
* You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words,
* the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.
*
* Return the number of '*' in s, excluding the '*' between each pair of '|'.
*
* Note that each '|' will belong to exactly one pair.
*
*/

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>


int countAsterisks(char* s) 
{
        bool should_consider = true;
        int asterisks_cnt = 0;

        for ( int i = 0; i < strlen(s); i++ ) {
                if ( s[i] == '|' )
                        should_consider = !should_consider;

                if ( should_consider && s[i] == '*' )
                        ++asterisks_cnt;
        }
        return asterisks_cnt;
}
