/**
* Leetcode 2824: Count Pairs whose sum is less than target
*
* Given a 0-indexed integer array nums of length n and an integer target,
* return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
*/

#include <stdlib.h>
#include <stdio.h>


int countPairs(int* nums, int numsSize, int target) {
  int pairs = 0, remainder_idx = 0;

  for ( int i = 0; i < numsSize; i++ ) {
    for ( int j = 0; j < i; j++) {
      pairs += nums[j] + nums[i] < target;
    }
  }
  return pairs;
}
