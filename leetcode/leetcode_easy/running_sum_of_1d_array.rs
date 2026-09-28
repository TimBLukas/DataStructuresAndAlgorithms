
/// Leetcode 1480: Running Sum of 1d Array
/// 
/// Given an array num. We define a running sum of an array as runningSum[i] = sum(nums[0]..nums[i])
/// Return the running sum of nums.

impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut running_sum: i32 = 0;

        let result = nums.into_iter().map(|x| {
            running_sum += x;
            running_sum
        }).collect::<Vec<i32>>();
        result
    }
}