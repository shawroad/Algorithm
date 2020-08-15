# -*- coding: utf-8 -*-
# @Time    : 2020/8/15 16:33
# @Author  : xiaolu
# @FileName: 019-被围绕的区域.py
# @Software: PyCharm
'''
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
示例:
X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X
'''

def solve(board):
    if len(board) == 0:
        return

    row = len(board)
    col = len(board[0])

    def bfs(i, j):
        queue = []
        queue.insert(0, (i, j))
        while queue:
            i, j = queue.pop()
            if 0 <= i < row and 0 <= j < col and board[i][j] == 'O':
                board[i][j] = "B"
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    queue.insert(0, (i + dx, j + dy))
    for j in range(col):
        if board[0][j] == 'O':
            bfs(0, j)
        if board[row-1][j] == 'O':
            bfs(row-1, j)
    for i in range(row):
        if board[i][0] == 'O':
            bfs(i, 0)
        if board[i][col - 1] == 'O':
            bfs(i, col - 1)

    for i in range(row):
        for j in range(col):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            if board[i][j] == 'B':
                board[i][j] = 'O'


if __name__ == '__main__':
    # board = [["X", "X", "X", "X"],
    #          ["X", "O", "O", "X"],
    #          ["X", "X", "O", "X"],
    #          ["X", "O", "X", "X"]]
    board = [['O', 'O'],
             ['O', 'O']]

    solve(board)
    print(board)
