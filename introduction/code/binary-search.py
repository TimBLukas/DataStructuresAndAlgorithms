from typing import List


def binary_search(arr: List, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        elif guess > target:
            high = mid - 1

    return None


if __name__ == "__main__":
    print("Testing binary search")
    test1_values: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    test1_target = 10

    print(f"Testing with {test1_values} and Target = {test1_target}")
    output_test_1 = binary_search(test1_values, test1_target)
    print(f"The output of the binary search: {output_test_1}")

    test2_values: List[str] = [
        "Alex",
        "Chloe",
        "James",
        "Kevin",
        "Lukas",
        "Otto",
        "Ruben",
        "Tim",
        "Wilfred",
    ]
    test2_target = "Chloe"

    print(f"Testing with {test2_values} and Target = {test2_target}")
    output_test_2 = binary_search(test2_values, test2_target)
    print(f"The output of the binary search: {output_test_2}")
