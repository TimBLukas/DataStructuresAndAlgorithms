"""
Leetcode 593: Valid Square

Given the coordinates of four points in 2D space p1, p2, p3 and p4,
return true if the four points construct a square.

The coordinate of a point pi is represented as [xi, yi].
The input is not given in any order.

A valid square has four equal sides with positive length and four equal angles (90-degree angles
"""

from typing import List


class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        points = [p1, p2, p3, p4]

        def distance(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        distances = []

        for i in range(4):
            for j in range(i + 1, 4):
                distances.append(distance(points[i], points[j]))

        distances.sort()

        return (
            distances[0] > 0
            and distances[0] == distances[1] == distances[2] == distances[3]
            and distances[4] == distances[5]
        )
