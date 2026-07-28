/**
* Leetcode 3110: Score of a String
*
* You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
*
* Return the score of s.
*/

#include <stdlib.h>
#include <string.h>


int scoreOfString(char* s) 
{
        int score = 0;

        for ( int i = 0; (i + 1) < strlen(s); i++) {
                score += abs(s[i] - s[i + 1]);
        }

        return score;
}

