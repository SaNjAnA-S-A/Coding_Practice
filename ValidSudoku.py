# https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150

""" Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules."""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        flag = 0
        for i, row in enumerate(board):
            if flag == 0:
                for j, x in enumerate(row):
                    if x != '.':
                        if len(res) == len(set(res)):
                            res.append((i,x))
                            res.append((x,j))
                            res.append((i // 3, j // 3, x))
                        else:
                            flag = 1
                            break
            else:
                break
        return len(res) == len(set(res))
