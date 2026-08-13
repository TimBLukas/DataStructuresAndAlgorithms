/**
* Leetcode 1689: Partitioning Into Minimum Number of Deci-Binary Numbers
*
* A decimal number is called deci-binary if each of its digits is either 0 or 1
without any leading zeros.
* For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
* Given a string n that represents a positive decimal integer, return the
* minimum number of positive deci-binary numbers needed so that they sum up to
n.
*/

#include <stdlin.h>
#include <string.h>

int minPartitions(char *n) {
    int partitions = 0, length = strlen(n);

    for (int i = 0; i < length; i++)
        partitions = partitions < (n[i] - '0') ? (n[i] - '0') : partitions;
    return partitions;
}
