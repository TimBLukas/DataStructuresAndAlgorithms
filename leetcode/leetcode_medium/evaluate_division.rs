// Optional imports
// use std::collections::HashMap;
// use std::collections::HashSet;

// You are given an array of variables pairs (equations) and an array of real Numbers values,
// where equations[i] = [A_i, B_i] and values[i] represents the equation A_i / B_i = values[i].
// Each A_i or B_i is a strings that represents a single variable
//
// You are also given some queries where queries[j] = [C_j, D_j] represents the jth query where you
// must find the answer for C_j / D_j = ?.
//
// Return the answers for all queries. if a single answer cannot be determined return  -1.0
//
// Note the input is always valid, you  may assume that evaluating the queries will not result in
// division by zero and that there is no contradiction
//
// Note the variables that do not occur in the list of equations are undefined, so the
// answer cannot be determined for them

pub struct Solution;

impl Solution {
    pub fn calc_equation(
        equations: Vec<Vec<String>>,
        values: Vec<f64>,
        queries: Vec<Vec<String>>,
    ) -> Vec<f64> {
        return vec![-1.0];
    }
}

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
