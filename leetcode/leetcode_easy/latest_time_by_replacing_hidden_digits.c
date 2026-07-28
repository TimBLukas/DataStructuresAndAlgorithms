/**
 * Leetcode 1736: Latest Time by Replacing hidden digits
 * 
 * You are given a string `time` in the form of `hh:mm`, where some of the digits in the string are hidden (represented by `?`)
 * The valid times are those inclusively between `00:00` and `23:59`.
 * Return the latest valid time you can get from `time` by replacing the hidden digits.
 */

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

char* maximumTime(char* time) 
{
    char* result = (char*)malloc(6 * sizeof(char));

    for (int i = 0; i < 5; i++)
        result[i] = time[i];

    result[5] = '\0';

    if ( result[0] == '?' ) {
        if (result[1] == '?' || result[1] <= '3')
            result[0] = '2';
        else
            result[0] = '1';
    }

    if ( result[1] == '?' ) {
        if (result[0] == '2')
            result[1] = '3';
        else
            result[1] = '9';
    }

    if ( result[3] == '?' )
        result[3] = '5';

    if ( result[4] == '?' )
        result[4] = '9';

    return result;
}
