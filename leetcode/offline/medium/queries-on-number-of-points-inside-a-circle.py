# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
#
# Title: 1828. Queries on Number of Points Inside a Circle
# Difficulty: Medium
#
# You are given an array `points` where `points[i] = [x_i, y_i]` is the
# coordinates of the `i^th` point on a 2D plane. Multiple points can have the
# same coordinates.
#
# You are also given an array `queries` where `queries[j] = [x_j, y_j, r_j]`
# describes a circle centered at `(x_j, y_j)` with a radius of `r_j`.
#
# For each query `queries[j]`, compute the number of points inside the `j^th`
# circle. Points on the border of the circle are considered inside.
#
# Return an array `answer`, where `answer[j]` is the answer to the `j^th`
# query.
#
# Example 1:
#
#     Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
#     Output: [3,2,2]
#     Explanation: The points and circles are shown above.
#     queries[0] is the green circle, queries[1] is the red circle, and queries[2] is the blue circle.
#
# Example 2:
#
#     Input: points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
#     Output: [2,3,2,4]
#     Explanation: The points and circles are shown above.
#     queries[0] is green, queries[1] is red, queries[2] is blue, and queries[3] is purple.
#
# Constraints:
#
# 1. `1 <= points.length <= 500`
#
# 2. `points[i].length == 2`
#
# 3. `0 <= x_​​​​​​i, y_​​​​​​i <= 500`
#
# 4. `1 <= queries.length <= 500`
#
# 5. `queries[j].length == 3`
#
# 6. `0 <= x_j, y_j <= 500`
#
# 7. `1 <= r_j <= 500`
#
# 8. All coordinates are integers.
#
# Follow up: Could you find the answer for each query in better complexity
# than `O(n)`?


from __future__ import annotations

from typing import List

import unittest


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        pass  # TODO: implement


class TestQueriesOnNumberOfPointsInsideACircle(unittest.TestCase):
    def test_example_1(self) -> None:
        self.assertEqual(Solution().countPoints(points=[[1,3],[3,3],[5,3],[2,2]], queries=[[2,3,1],[4,3,1],[1,1,2]]), [3,2,2])

    def test_example_2(self) -> None:
        self.assertEqual(Solution().countPoints(points=[[1,1],[2,2],[3,3],[4,4],[5,5]], queries=[[1,2,2],[2,2,2],[4,3,2],[4,3,3]]), [2,3,2,4])

    def test_edgecase(self) -> None:
        pass  # TODO add your own edge cases.


if __name__ == "__main__":
    unittest.main()
