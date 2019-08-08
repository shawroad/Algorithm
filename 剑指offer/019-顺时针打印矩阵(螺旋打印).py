"""

@file   : 019-顺时针打印矩阵(螺旋打印).py

@author : xiaolu

@time   : 2019-08-03

"""
'''
题目:
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字
    
'''
def shunshizhen_output(matrix):
    length = len(matrix[0])
    width = len(matrix)
    i = 0
    j = length
    m = width
    n = 0

    count = 0   # 统计元素是否读完 若读完则跳出
    while True:
        for x in range(n, j):
            print(matrix[i][x], end=' ')
            count += 1
        i += 1

        for x in range(i, m):
            print(matrix[x][j-1], end=' ')
            count += 1
        j -= 1

        for x in range(j-1, n-1, -1):
            print(matrix[m-1][x], end=' ')
            count += 1
        m -= 1

        for x in range(m-1, i-1, -1):
            print(matrix[x][n], end=' ')
            count += 1
        n += 1

        if count == length * width:
            break


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    shunshizhen_output(matrix)

