"""
Leetcode 42: Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = 1
        sum = 0

        while left < len(height) and right < len(height):
            if height[left] > 0 and any(
                map(lambda x: x >= height[left], height[left + 1 :])
            ):
                while right < len(height) and height[left] > height[right]:
                    sum += height[left] - height[right]
                    right += 1
                left, right = right, right + 1

            else:
                left += 1
                right += 1
        return sum


class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) == 1:
            return 0

        # 1. Find the highest elevation
        highest = 0
        for i in range(len(height)):
            if height[i] > height[highest]:
                highest = i

        total = 0
        left, right = highest, highest
        tmp = highest

        while right < len(height):
            if any(x >= height[right] for x in height[right + 1 :]):
                right += 1
                continue
            total += sum(height[tmp] - height[i] for i in height[tmp:right])
            tmp = right
            right += 1

        tmp = highest

        while left >= 0:
            if any(x >= height[left] for x in height[:tmp:-1]):
                left -= 1
                continue
            total += sum(height[tmp] - height[i] for i in height[left:tmp])
            tmp = left
            left -= 1

        return total
