# https://leetcode.com/problems/reverse-string-prefix/
#
# Title: 3794. Reverse String Prefix
# Difficulty: Easy
#
# You are given a string `s` and an integer `k`.
#
# Reverse the first `k` characters of `s` and return the resulting string.
#
# Example 1:
#
# Input: s = "abcd", k = 2
#
# Output: "bacd"
#
# Explanation:​​​​​​​
#
# The first `k = 2` characters `"ab"` are reversed to `"ba"`. The final
# resulting string is `"bacd"`.
#
# Example 2:
#
# Input: s = "xyz", k = 3
#
# Output: "zyx"
#
# Explanation:
#
# The first `k = 3` characters `"xyz"` are reversed to `"zyx"`. The final
# resulting string is `"zyx"`.
#
# Example 3:
#
# Input: s = "hey", k = 1
#
# Output: "hey"
#
# Explanation:
#
# The first `k = 1` character `"h"` remains unchanged on reversal. The final
# resulting string is `"hey"`.
#
# Constraints:
#
# 1. `1 <= s.length <= 100`
#
# 2. `s` consists of lowercase English letters.
#
# 3. `1 <= k <= s.length`


from __future__ import annotations


import unittest


class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        pass  # TODO: implement


class TestReverseStringPrefix(unittest.TestCase):
    def test_example_1(self) -> None:
        self.assertEqual(Solution().reversePrefix(s="abcd", k=2), "bacd")

    def test_example_2(self) -> None:
        self.assertEqual(Solution().reversePrefix(s="xyz", k=3), "zyx")

    def test_example_3(self) -> None:
        self.assertEqual(Solution().reversePrefix(s="hey", k=1), "hey")

    def test_edgecase(self) -> None:
        pass  # TODO add your own edge cases.


if __name__ == "__main__":
    unittest.main()
