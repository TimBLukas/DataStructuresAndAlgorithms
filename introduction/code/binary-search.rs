fn binary_search(arr: &Vec<i32>, target: i32) -> Option<usize> {
    let mut low = 0;
    let mut high = arr.len();

    while low <= high {
        let mid = (low + high) / 2;
        let guess = arr[mid];

        if guess == target {
            return Some(mid);
        } else if guess < target {
            low = mid + 1;
        } else if guess > target {
            high = mid - 1;
        }
    }
    None
}

fn main() {
    println!("Testing binary search !!");
    let test_values_1 = vec![1, 2, 5, 12, 15, 16, 21, 25, 29, 31, 32];
    let test_target_1 = 5;

    println!(
        "Running binary search with test values {:?} and target {}",
        test_values_1, test_target_1
    );
    if let Some(val) = binary_search(&test_values_1, test_target_1) {
        println!("Result of binary search: {val}");
    } else {
        println!("The Result of binary search was None");
    }

    let test_values_2 = vec![1, 100, 200, 230, 241, 340, 455, 511, 623, 823];
    let test_target_2 = 1;

    println!(
        "Running binary search with test values {:?} and target {}",
        test_values_2, test_target_2
    );
    if let Some(val_2) = binary_search(&test_values_2, test_target_2) {
        println!("Result of binary search: {val_2}");
    } else {
        println!("The Result of binary search was None");
    }
}
