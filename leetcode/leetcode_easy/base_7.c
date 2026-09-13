/**
 * Leetcode 504: Base 7
 *
 * Given an integer num, return a string of its base 7 representation.
 */

#include <stdbool.h>
#include <stdlib.h>

char *convertToBase7(int num) {
    bool is_negative = num < 0;
    long long n = num;
    if (is_negative)
        n = -n;

    if (n == 0) {
        char *result = malloc(2);
        result[0] = '0';
        result[1] = '\0';
        return result;
    }

    int exp = 0;
    long long val = 1;
    while (val * 7 <= n) {
        val *= 7;
        ++exp;
    }
    char *result = malloc((exp + 1) + (is_negative ? 1 : 0) + 1);
    int idx = 0;

    if (is_negative)
        result[idx++] = '-';

    while (exp >= 0) {
        int count = n / val;
        result[idx++] = count + '0';
        n %= val;

        val /= 7;
        --exp;
    }

    result[idx] = '\0';
    return result;
}
