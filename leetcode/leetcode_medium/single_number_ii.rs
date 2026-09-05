/// 137. Single Number II
///
/// Given an integer array nums where every element appears three times except for one,
/// which appears exactly once.
///
/// Find the single element and return it.
///
/// You must implement a solution with a linear runtime complexity and use only constant extra space.

use std::collection::HashMap;

struct Solution;

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut seen: HashMap<i32, i32> = HashMap::new();
        for n in nums {
            *seen.entry(n).or_insert(0) += 1;
        } 

        for (number, times_seen) in &seen {
            if *times_seen < 3 {
                return *number;
            }
        }
        -1
    }
}
