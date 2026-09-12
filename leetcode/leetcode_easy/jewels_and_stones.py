"""
Leetcode 771: Jewels and Stones

You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have.
Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([stone for stone in stones if stone in jewels])


class Solution2:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels = set(jewels)

        for stone in stones:
            if stone in jewels:
                count += 1

        return count
