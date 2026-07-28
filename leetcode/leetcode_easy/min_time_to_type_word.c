/**
 * Leetcode 1974: Minimum time to type word using special typewriter
 * 
 * There is a special typewriter with lowercase English letters `a` to `z` arranged in a circle with a pointer. A character can only
 * be typed if the pointer is pointing to that character.
 * The pointer is initially pointing to the character `a`
 * 
 * Each second you can perform one of the following operations:
 * - Move the pointer one character clockwise or counterclockwise, type the character the pointer is currently on.
 * 
 * Given a string word, return the minimum number of seconds to type out the charactesr in `word`
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int minTimeToType(char* word) 
{
        int time = 0;
        int curr_pos = (int)'a';
        int upper = (int)'z';
        int lower = (int)'a';
        int target;

        for ( int i = 0; i < strlen(word); i++ ) {
                target = (int)word[i];
                if ( target < curr_pos ) {
                        if ( ((upper - curr_pos) + (target - lower)) < curr_pos - target ) {
                                time += ((upper - curr_pos) + (target - lower)) + 1;

                        }
                        else {
                                time += curr_pos - target;
                        }

                }
                else if ( target > curr_pos ) {
                        if ( ((curr_pos - lower) + (upper - target)) < target - curr_pos) {
                                time += ((curr_pos - lower) + (upper - target)) + 1;

                        } else {
                                time += target - curr_pos;
                        }
                }

                time++;
                curr_pos = target;
        }
        return time;
}
