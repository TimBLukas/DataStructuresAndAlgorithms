/**
* Leetcode 709: To Lower Case
*
* Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
*/

#include <string.h>
#include <stdlib.h>


char* toLowerCase(char* s) 
{
        for ( int i = 0; i < strlen(s); i++ ) {
                if ( s[i] >= 'A' && s[i] <= 'Z' ) {
                        s[i] = 'a' + (s[i] - 'A');
                }
        }

        return s;
}
