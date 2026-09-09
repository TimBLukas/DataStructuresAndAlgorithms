"""
Leetcode 6: ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
"""

from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        conversion: List[List[str]] = [[] for _ in range(numRows)]
        if numRows == 1:
            return s

        row, decreasing = 0, True
        for c in s:
            conversion[row].append(c)

            if row == numRows - 1 or row == 0:
                decreasing = not decreasing

            row = row - 1 if decreasing else row + 1

        return "".join(map("".join, conversion))
