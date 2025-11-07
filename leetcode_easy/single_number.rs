// Optional imports
use std::collections::HashMap;
// use std::collections::HashSet;

pub struct Solution;

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut hash_map: HashMap<i32, Option<i32>> = HashMap::new();
        for n in nums {
            if hash_map.contains_key(&n) {
                hash_map.insert(n, Some(n));
            } else {
                hash_map.insert(n, None);
            }
        }
        for (k, v) in &hash_map {
            if *v == None {
                return *k;
            }
        }
        return -1;
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
