/**
* Leetcode 412: Fizz Buzz
*
* Given an integer n, return a string array answer (1-indexed) where:
*
* answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
* answer[i] == "Fizz" if i is divisible by 3.
* answer[i] == "Buzz" if i is divisible by 5.
* answer[i] == i (as a string) if none of the above conditions are true.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

char** fizzBuzz(int n, int* returnSize) 
{
    *returnSize = n;

    char** return_val = (char**)malloc(n * sizeof(char*));
    if ( return_val == NULL ) {
        return NULL; 
    }

    for ( int i = 0; i < n; i++ ) {
        int num = i + 1;

        return_val[i] = (char*)malloc(12 * sizeof(char));
        if ( return_val[i] == NULL ) {
            for ( int j = 0; j < i; j++ ) {
                free(return_val[j]);
            }

            free(return_val);
            return NULL;
        }

        if ( num % 15 == 0 ) {
            strcpy(return_val[i], "FizzBuzz");

        } else if ( num % 3 == 0 ) {
            strcpy(return_val[i], "Fizz");

        } else if ( num % 5 == 0 ) {
            strcpy(return_val[i], "Buzz");
        } else {
            sprintf(return_val[i], "%d", num);
        }
    }

    return return_val;
}
