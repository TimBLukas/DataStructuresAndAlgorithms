/**
 * Leetcode 2160. Minimum Sum of Four Digit Number After Splitting Digits
 *
 * You are given a positive integer num consisting of exactly four digits. Split
 * num into two new integers new1 and new2 by using the digits found in num.
 * Leading zeros are allowed in new1 and new2, and all the digits found in num
 * must be used. For example, given num = 2932, you have the following digits:
 * two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22,
 * 93], [23, 92], [223, 9] and [2, 329]. Return the minimum possible sum of new1
 * and new2.
 */

#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) { return (*(int *)a - *(int *)b); }

int minimumSum(int num) {
    int digits[4];

    for (int i = 0; i < 4; i++) {
        digits[i] = num % 10;
        num /= 10;
    }

    qsort(digits, 4, sizeof(int), compare);

    return (digits[0] + digits[1]) * 10 + digits[2] + digits[3];
}

// Example usage:
int main() {
    printf("%d\n", minimumSum(2932)); // Output: 52 (29 + 23 or 23 + 29)
    printf("%d\n", minimumSum(4009)); // Output: 13 (04 + 09)
    return 0;
}
