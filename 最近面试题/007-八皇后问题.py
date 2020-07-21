# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 11:09
# @Author  : xiaolu
# @FileName: 007-八皇后问题.py
# @Software: PyCharm

def main(n):
    result = []

    def back(board, row):
        if row == len(board):
            result.append([''.join(b) for b in board])
            return

        for col in range(0, len(board)):
            if not isValid(board, row, col):
                continue   # 表示当前选择不合法
            board[row][col] = 'Q'
            back(board, row+1)
            board[row][col] = '.'

    board = [['.' for j in range(n)] for i in range(n)]
    back(board, 0)
    return result


def isValid(board, row, col):
    n = len(board)

    # 检查列是否有皇后互相冲突
    for i in range(n):
        if board[i][col] == 'Q':
            return False

    # 检查右上方是否有冲突
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    # 检测右上方是否有冲突
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    return True


if __name__ == '__main__':
    n = 4
    result = main(n)
    print(result)
