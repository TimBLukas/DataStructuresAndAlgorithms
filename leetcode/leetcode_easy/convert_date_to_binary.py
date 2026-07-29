"""
Leetcode 3280: Convert date to binary

You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.
date can be written in its binary representation obtained by converting year, month, and day
to their binary representations without any leading zeroes and writing them down in year-month-day format.
Return the binary representation of date.
"""

from typing import List


class Solution:
    def to_binary(self, vals: List[str]) -> List[str]:
        result = []
        for val in vals:
            val = int(val)
            base = 1
            binary = ""

            while base * 2 <= val:
                base *= 2

            while base >= 1:
                print(val, base)
                if val >= base:
                    val -= base
                    binary += "1"
                else:
                    binary += "0"

                base = base / 2

            result.append(binary)

        return result

    def convertDateToBinary(self, date: str) -> str:

        return "-".join(self.to_binary(date.split("-")))
