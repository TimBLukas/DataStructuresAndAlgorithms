"""
Leetcode 3683: Earliest Time to finish one task

You are given a 2D integer array tasks where tasks[i] = [si, ti].
Each [si, ti] in tasks represents a task with start time si that takes ti units of time to finish.
Return the earliest time at which at least one task is finished.
"""

from typing import List
import sys


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        earliest_time: int = sys.maxsize
        for task in tasks:
            earliest_time = min(earliest_time, (task[0] + task[1]))

        return earliest_time


class Solution2:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(s + t for s, t in tasks)
