# Leetcode 79. Word Search
# https://leetcode.com/problems/word-search/

"""
Problem Description: Given an m * n Grid of characters board and a string word, return True if the word exists in the grid
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter may not be used mroe than once

```python
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

```python
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```
"""


from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(x, y, idx):
            if idx == len(word):
                return True

            if x < 0 or x >= rows or y < 0 or y >= cols:
                return False

            if board[x][y] != word[idx]:
                return False

            temp = board[x][y]
            board[x][y] = "#"  # markieren

            found = (
                dfs(x + 1, y, idx + 1) or
                dfs(x - 1, y, idx + 1) or
                dfs(x, y + 1, idx + 1) or
                dfs(x, y - 1, idx + 1)
            )

            board[x][y] = temp  # backtracking
            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False