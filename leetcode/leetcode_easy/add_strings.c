/**
 * Leetcode 415: Add Strings
 *
* Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
* You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
* You must also not convert the inputs to integers directly.
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#include <stdlib.h>
#include <string.h>

char *addStrings(char *num1, char *num2)
{
    int len1 = strlen(num1);
    int len2 = strlen(num2);

    int maxLen = (len1 > len2 ? len1 : len2) + 2;
    char *result = malloc(maxLen);

    if (result == NULL)
        return NULL;

    int i = len1 - 1;
    int j = len2 - 1;
    int k = maxLen - 1;

    result[k] = '\0';
    k--;

    int carry = 0;

    while (i >= 0 || j >= 0 || carry)
    {
        int sum = carry;

        if (i >= 0)
            sum += num1[i--] - '0';

        if (j >= 0)
            sum += num2[j--] - '0';

        result[k--] = (sum % 10) + '0';
        carry = sum / 10;
    }

    memmove(result, result + k + 1, maxLen - k - 1);

    return result;
}
