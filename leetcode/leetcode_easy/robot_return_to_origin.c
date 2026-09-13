/**
 * Leetcode 657: Robot Return to Origin
 *
 * There is a robot starting at the position (0, 0), the origin, on a 2D plane.
 * Given a sequence of its moves, judge if this robot ends up at (0, 0) after it
 * completes its moves.
 *
 * You are given a string moves that represents the move sequence of the robot
 * where moves[i] represents its ith move.
 * Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).
 *
 * Return true if the robot returns to the origin after it finishes all of its
 * moves, or false otherwise.
 *
 * Note: The way that the robot is "facing" is irrelevant.
 * 'R' will always make the robot move to the right once, 'L' will always make
 * it move left, etc. Also, assume that the magnitude of the robot's movement is
 * the same for each move.
 */

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool judgeCircle(char *moves) {
    int vert = 0;
    int hor = 0;

    if (strlen(moves) % 2 != 0)
        return false;

    for (int i = 0; moves[i] != '\0'; i++) {
        if (moves[i] == 'L')
            hor -= 1;
        else if (moves[i] == 'R')
            hor += 1;
        else if (moves[i] == 'D')
            vert -= 1;
        else if (moves[i] == 'U')
            vert += 1;
    }

    return vert == 0 && hor == 0 ? true : false;
}
