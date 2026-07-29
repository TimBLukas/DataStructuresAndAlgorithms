/**
* Leetcode 2942: Find Words Containing Character
*
* You are given a 0-indexed array of strings words and a character x.
* Return an array of indices representing the words that contain the character x.
*
* Note that the returned array may be in any order.
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int* findWordsContaining(char** words, int wordsSize, char x, int* returnSize) 
{
        int* has_char = (int*) malloc(wordsSize * sizeof(int));
        int has_char_idx = 0;
        for ( int i = 0; i < wordsSize; i++) {
                if (strchr(words[i], x) != NULL) {
                        has_char[has_char_idx++] = i;
                }
        }

        *returnSize = has_char_idx;
        return has_char;
}
