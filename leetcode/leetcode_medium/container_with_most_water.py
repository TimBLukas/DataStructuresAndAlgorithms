"""
Leetcode 11: Container with most water

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        def calc_area(start, end):
            print(start, end)
            w = end - start
            h = min(height[start], height[end])
            return w * h

        left, right = 0, len(height) - 1
        maxArea = calc_area(left, right)

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            maxArea = max(maxArea, calc_area(left, right))

        return maxArea
