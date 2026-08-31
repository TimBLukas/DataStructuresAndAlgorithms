"""
2545: Sort the Students by Their Kth Score

You are also given an integer k.
Sort the students (i.e., the rows of the matrix)
by their scores in the kth (0-indexed) exam from the highest to the lowest.

Return the matrix after sorting it.
"""

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(reverse=True, key=lambda student: student[k])
        return score