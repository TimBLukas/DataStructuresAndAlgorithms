/**
* Leetcode 258: Add Digits
*
* Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
*/


#include <math.h>
#include <stdlib.h>


int addDigits(int num) 
{
        int numDigits = floor(log10(abs(num))) + 1;
        int curr_num;

        while (numDigits > 1)
        {
                curr_num = num;
                num = 0;
                while (curr_num)
                {
                        num += curr_num % 10;
                        curr_num /= 10;
                }

                numDigits = floor(log10(abs(num))) + 1;
        }

        return num;
    
}
