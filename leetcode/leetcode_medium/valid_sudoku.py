"""
Leetcode 36: Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 1. Check rows
        for row in board:
            tmp = [n for n in row if n != "."] 
            if not len(tmp) == len(set(tmp)):
                return False

        # 2. Check cols
        for i in range(len(board)):
            tmp = [row[i] for row in board if row[i] != "."]
            if not len(tmp) == len(set(tmp)):
                return False

        # 3. Check boxes
        for i in range(3):
            for j in range(3):
                box = [r[i*3:(i*3)+3] for r in board[j*3:(j*3)+3]]
                seen = []
                for r in box:
                    for number in r:
                        if number != "." and number in seen:
                            return False
                        elif number != ".":
                            seen.append(number)

        return True 


