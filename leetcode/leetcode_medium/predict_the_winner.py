"""
Leetcode 486: Predict the Winner

You are given an integer array nums.

Two players are playing a game with this array: Player 1 and Player 2.

Player 1 and Player 2 take turns, with Player 1 starting first. Both players start the game with a score of 0.

At each turn, the current player takes the number at either end of the array (i.e., nums[0] or nums[nums.length - 1]),
removing it from the array and adding it to their own score. The game ends when there are no more elements in the array.

Return true if Player 1's final score is greater than or equal to Player 2's final score, and false otherwise.

Note that a tie counts as a win for Player 1. You may assume that both players play optimally.
"""


class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        optimal_pics = []
        while len(nums) > 0:
            optimal_pics.append(nums.pop(0) if nums[0] >= nums[-1] else nums.pop(-1))
        print(optimal_pics)
        print(sum(optimal_pics[::2]), sum(optimal_pics[1::2]))
        return sum(optimal_pics[::2]) >= sum(optimal_pics[1::2])
