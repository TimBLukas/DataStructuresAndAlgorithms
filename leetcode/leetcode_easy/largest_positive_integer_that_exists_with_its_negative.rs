/// Leetcode 2441: Largest Positive Integer That Exists With Its Negative
/// Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
/// 
/// Return the positive integer k. If there is no such integer, return -1.

impl Solution {
    pub fn find_max_k(nums: Vec<i32>) -> i32 {
        let mut sorted_nums = nums.clone();
        sorted_nums.sort();
        let mut left: usize = 0;
        let mut right: usize = nums.len() - 1;

        while left <= right {
            println!("{} - {}", sorted_nums[left], sorted_nums[right]);
            if sorted_nums[left] == (-1 * sorted_nums[right]) {
                return sorted_nums[right];
            } else if sorted_nums[left] < (-1 * sorted_nums[right]) {
                left += 1;
            } else if sorted_nums[left] > (-1 * sorted_nums[right]) {
                right -= 1;
            }
        }
        -1
    }
}
