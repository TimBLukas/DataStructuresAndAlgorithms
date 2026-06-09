// Optional imports
// use std::collections::HashMap;
// use std::collections::HashSet;

pub struct Solution;

// Given an unsorted array of integers nums, return the length of the longest continuous increasing
// subsequence (i.e. subarray). The subsequence must be strictly increasing.
//
// A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is
// [nums[l], nums[l + 1], ..., nums[r-1], nums[r]] and for each l <= i <= r, nums[i] < nums[i + 1]
//
// Examples:
// Input: nums[1,3,5,7] -> Output: 3 The longest sequence is 1,3,5
// INput: nums[2,2,2,2,2] -> Output: 1 The longest continuous increasing subsequence is [2] with
// length 1

use std::cmp;
impl Solution {
    pub fn find_length_of_lcis(nums: Vec<i32>) -> i32 {
        let mut prev: Option<i32> = None;
        let mut max: i32 = 0;
        let mut curr_max: i32 = 0;
        for n in nums {
            if prev.is_none() {
                curr_max += 1;
            } else if prev.unwrap() < n {
                curr_max += 1;
            } else if prev.unwrap() >= n {
                max = cmp::max(curr_max, max);
                curr_max = 1;
                prev = Some(n);
            }

            prev = Some(n);
        }

        return cmp::max(curr_max, max);
    }
}
