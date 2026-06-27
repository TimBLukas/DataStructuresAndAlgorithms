# Optional Imports:
# from typing import List, Optional
# import collections
import unittest
from typing import List


"""
Leetcode 860 Lemonade Change
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills).
You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you dont have any change first

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the
correct change, or false otherwise.
"""


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            if bill == 10:
                if change[5] > 0:
                    change[5] = change[5] - 1

                else:
                    return False

            if bill == 20:
                if change[5] > 0 and change[10] > 0:
                    change[5] = change[5] - 1
                    change[10] = change[10] - 1
                    print(f"covering {bill} with $5 and $10")

                elif change[5] > 2:
                    change[5] = change[5] - 3
                    print(f"covering {bill} with 3 * $5")
                else:
                    return False

            change[bill] = change[bill] + 1

        return True


if __name__ == "__main__":
    Solution().lemonadeChange([5, 5, 10, 10, 20])  # should output false
