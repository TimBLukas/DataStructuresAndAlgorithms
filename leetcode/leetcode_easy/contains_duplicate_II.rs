// Optional imports
// use std::collections::HashMap;
// use std::collections::HashSet;

pub struct Solution;

impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        for i in &nums {
            for j in &nums[((*i + 1) as usize)..] {
                if ((i - j).abs() <= k) && (nums[*i as usize] == nums[*j as usize]) {
                    return true;
                }
            }
        }
        return false;
    }
}

// Tests in main um kein cargo projekt anlegen zu müssen
fn main() {
    println!("--- Testing ---");

    // Testfall 1
    {
        let nums = vec![2, 2, 1];
        let expected = 1;
        let result = Solution::single_number(nums.clone());

        assert_eq!(
            result, expected,
            "Fehler bei Testfall 1 (Eingabe: {:?})",
            nums
        );
        println!("Testfall 1: OK");
    }

    // Testfall 2
    {
        let nums = vec![4, 1, 2, 1, 2];
        let expected = 4;
        let result = Solution::single_number(nums.clone());

        assert_eq!(
            result, expected,
            "Fehler bei Testfall 2 (Eingabe: {:?})",
            nums
        );
        println!("Testfall 2: OK");
    }

    // Testfall für Randfälle
    {
        let nums = vec![1];
        let expected = 1;
        let result = Solution::single_number(nums.clone());

        assert_eq!(
            result, expected,
            "Fehler bei Randfall (Eingabe: {:?})",
            nums
        );
        println!("Randfall: OK");
    }

    println!("\n--- Alle Tests erfolgreich! ---");
}
