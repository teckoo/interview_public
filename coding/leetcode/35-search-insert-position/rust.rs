/*
Runtime: 0 ms, faster than 100.00% of Rust online submissions for Search Insert Position.
Memory Usage: 2.6 MB, less than 100.00% of Rust online submissions for Search Insert Position.
 *
*/
use std::cmp::Ordering;

impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let (mut low, mut high) = (0i32, nums.len() as i32 - 1);

        while low <= high {
            let mid = low + (high - low) / 2;

            match nums[mid as usize].cmp(&target) {
                Ordering::Equal => { return mid; }
                Ordering::Greater => { high = mid - 1; }
                Ordering::Less => { low = mid + 1; }
            }
        }

        low
    }
}
