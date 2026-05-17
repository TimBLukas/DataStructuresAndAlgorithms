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
        def check_pos_in_word(board: List[List[str]], word: str, curr_idx: int, x: int, y: int) -> bool:
                return True if board[y, x] == word[curr_idx] else False

        def exist(self, board: List[List[str]], word: str) -> bool:
                pass