"""
Leetcode 122: Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can sell and buy the stock multiple times on the same day,
ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought, profit = False, 0
        left, right = 0, 0

        while left < len(prices) and right < len(prices):
            if bought:
                if right + 1 >= len(prices) - 1 or prices[right + 1] < prices[right]:
                    bought = False
                    profit += prices[right] - prices[left]
                    left, right = right, right + 1
                else:
                    right += 1
            else:
                if prices[left] < prices[right]:
                    bought = True
                else:
                    left, right = right, right + 1

        return profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                maxProfit += prices[i] - prices[i - 1]
        return maxProfit
