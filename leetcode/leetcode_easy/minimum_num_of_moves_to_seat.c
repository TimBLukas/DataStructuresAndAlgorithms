/**
* Leetcode 2037: Minimum number of moves to seat everyone.
*
* There are n availabe seats and n students standing in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth student.
*
* You may perform the following move any number of times:
* Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
* 
* Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.
* 
* Note that there may be multiple seats or students in the same position at the beginning.
*/

#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#include <math.h>


int compare(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

int minMovesToSeat(int* seats, int seatsSize, int* students, int studentsSize)
{
    qsort(seats, seatsSize, sizeof(int), compare);
    qsort(students, studentsSize, sizeof(int), compare);

    int moves = 0;

    for (int i = 0; i < studentsSize; i++)
        moves += abs(seats[i] - students[i]);

    return moves;
}
