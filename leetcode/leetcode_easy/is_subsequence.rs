// Optional imports
// use std::collections::HashMap;
// use std::collections::HashSet;

// Leetcode 392
// given two strings s and t retrun true if s is a subsequence of t or false otherwise.
//
// A subsequence of a string is a new string that is formed from the original string by deleting
// some /can boe none) of the characters without disturbing the relative positions of the remaining
// characters (i.e. "ace" is a subsequence of "abcde" while "aec" is not)

pub struct Solution;

impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let global: int = 0;
        while global < s.len() {
            for x in s.chars() {
                if s.chars().nth(global).unwrap() == x { 
                    global++;
                }

            }
            return false;
        }
        return true;
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
