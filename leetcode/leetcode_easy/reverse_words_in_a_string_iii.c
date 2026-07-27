/**
* Leetcode 557: Reverse Words in a string iii
*
* Given a string s, reverse the order of characters in each word within
* a sentence while still preserving whitespace and initial word order.
*/

#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <threads.h>

char* reverseWords(char* s) 
{
        char* result = (char *) malloc ((strlen(s) + 1) * sizeof(char));
        int length = (int)strlen(s);
        int end = 0, curr_pos = 0;
        for ( int i = 0; i <= length; i++ )
        {
                if ( s[i] == ' ' || s[i]  == '\0' )
                {
                        curr_pos = i - 1;
                        int out = end;
                        while ( curr_pos >= end )
                        {
                                result[out++] = s[curr_pos--];
                        }
                        result[i] = s[i];
                        end = i + 1;
                }
        }

        result[length] = '\0';
        return result;
}
