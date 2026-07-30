/**
* Leetcode 2000: Reverse Prefix of Word
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>


char* reversePrefix(char* word, char ch) 
{
        int char_idx = 0;
        for ( int i = 0; i < strlen(word); i++ )
        {
                if ( word[i] == ch ) {
                        char_idx = i;
                        break;
                }
        }

        int j = 0;
        while ( j < char_idx ) {
                char prev = word[char_idx];
                word[char_idx--] = word[j];
                word[j++] = prev;
        }
        return word;
}
