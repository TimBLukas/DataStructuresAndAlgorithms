"""
2375. Construct Smallest Number From DI String

A 0-indexed string num of length n + 1 is created using the following conditions:

- num consists of the digits '1' to '9', where each digit is used at most once.
- If pattern[i] == 'I', then num[i] < num[i + 1].
- If pattern[i] == 'D', then num[i] > num[i + 1].

Return the lexicographically smallest possible string num that meets the conditions.
"""


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result, stack = [], []

        for i in range(len(pattern) + 1):
            stack.append(i + 1)

            if i == len(pattern) or pattern[i] == "I":
                while stack:
                    result.append(stack.pop())

        return "".join(map(str, result))
