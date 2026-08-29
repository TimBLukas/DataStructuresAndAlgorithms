/**
 * Leetcode 3884: First Matching Character From Both Ends
 * 
 * Return the smallest index i such that s[i] == s[n - i - 1].
 * If no such index exists, return -1.
 */

#include <string.h>
#include <stdio.h>

int firstMatchingIndex(char* s) {
    int front = 0;
    int back = strlen(s) - 1;

    while ( front <= back ) {
        if ( s[front] == s[back] )
            return front;
        front++;
        back--;
    }

    return -1;
}