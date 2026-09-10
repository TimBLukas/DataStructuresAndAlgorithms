/**
 * Leetcode 171: Excel Sheet Column Number
 *
 * Given a string columnTitle that represents the column title as appears in an
 * Excel sheet, return its corresponding column number.
 *
 * For example:
 *
 * A -> 1
 * B -> 2
 * C -> 3
 * ...
 * Z -> 26
 * AA -> 27
 * AB -> 28
 * ...
 *
 */

#include <math.h>
#include <stdlib.h>
#include <string.h>

int titleToNumber(char *columnTitle) {
    int sum = 0;
    for (int i = 0; columnTitle[i] != '\0'; i++) {
        sum = sum * 26 + (columnTitle[i] - 'A' + 1);
    }

    return sum;
}
