# https://leetcode.com/problems/removing-stars-from-a-string/
#
# Title: 2390. Removing Stars From a String
# Difficulty: Medium
#
# You are given a string `s`, which contains stars `*`.
#
# In one operation, you can:
#
# 1. Choose a star in `s`.
#
# 2. Remove the closest non-star character to its left, as well as remove the
#    star itself.
#
# Return the string after all stars have been removed.
#
# Note:
#
# 1. The input will be generated such that the operation is always possible.
#
# 2. It can be shown that the resulting string will always be unique.
#
# Example 1:
#
#     Input: s = "leet**cod*e"
#     Output: "lecoe"
#     Explanation: Performing the removals from left to right:
#     - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
#     - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
#     - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
#     There are no more stars, so we return "lecoe".
#
# Example 2:
#
#     Input: s = "erase*****"
#     Output: ""
#     Explanation: The entire string is removed, so we return an empty string.
#
# Constraints:
#
# 1. `1 <= s.length <= 10^5`
#
# 2. `s` consists of lowercase English letters and stars `*`.
#
# 3. The operation above can be performed on `s`.


from __future__ import annotations


import unittest


class Solution:
    def removeStars(self, s: str) -> str:
        pass  # TODO: implement


class TestRemovingStarsFromAString(unittest.TestCase):
    def test_example_1(self) -> None:
        self.assertEqual(Solution().removeStars(s="leet**cod*e"), "lecoe")

    def test_example_2(self) -> None:
        self.assertEqual(Solution().removeStars(s="erase*****"), "")

    def test_edgecase(self) -> None:
        pass  # TODO add your own edge cases.


if __name__ == "__main__":
    unittest.main()
