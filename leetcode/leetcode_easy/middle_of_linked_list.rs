// Optional imports
// use std::collections::HashMap;
// use std::collections::HashSet;

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

pub struct Solution;

// Given the head of a singly linked list, return the middle node of the linked list.
// if there are two middle nodes, return the second middle node
//

impl Solution {
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut l = head;
        let mut r = head.next;
        while !r.is_none() {
            l = Box::into_inner(l.unwrap()?).next;
            r = Box::into_inner(r.unwrap()?).next.next;
        }

        return l;
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
