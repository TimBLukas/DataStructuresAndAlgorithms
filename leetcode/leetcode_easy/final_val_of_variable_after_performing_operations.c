/**
 * Leetcode 2011: Final Value of Variable after Performing Operations
 *
 * There is a programming language with only four operations and one variable X:
 *
 * ++X and X++ increments the value of the variable X by 1.
 * --X and X-- decrements the value of the variable X by 1.
 * Initially, the value of X is 0.
 *
 * Given an array of strings operations containing a list of operations, return
 * the final value of X after performing all the operations.
 */

#include <stdlib.h>
#include <string.h>

int finalValueAfterOperations(char **operations, int operationsSize) {
    int finalValue = 0;

    for (int i = 0; i < operationsSize; i++) {
        if (operations[i][1] == '+') {
            finalValue++;
        } else if (operations[i][1] == '-') {
            finalValue--;
        }
    }

    return finalValue;
}
