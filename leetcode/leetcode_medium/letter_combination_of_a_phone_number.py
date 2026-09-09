"""
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
"""

from typing import List

import string


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letters = {}
        idx = 0
        for i in range(2, 10):
            num_to_letters[i] = (
                string.ascii_letters[idx : idx + 3]
                if i != 7 and i != 9
                else string.ascii_letters[idx : idx + 4]
            )
            idx += 3 if i != 7 and i != 9 else 4

        result = [""]
        for digit in digits:
            new_result = []

            for combination in result:
                for letter in num_to_letters[int(digit)]:
                    new_result.append(combination + letter)

            result = new_result

        return result
