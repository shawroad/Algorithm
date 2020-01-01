"""

@file   : 001-机器人路径问题(两种).py

@author : xiaolu

@time   : 2020-01-01

"""
count = 0


def find_num_point(r, c, rows, cols, k, matrix):
    global count
    # 1. 看给出的坐标坐标是否越界
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return

    # 2. 将坐标分解进行加法
    num_list = list(str(r)) + list(str(c))
    num_sum = 0
    for n in num_list:
        temp = int(n)
        num_sum += temp

    # 3. 将不符合的点置为-1 表示不能访问
    if num_sum > k:
        matrix[r][c] = -1
        return

    if matrix[r][c] == 1:
        return

    # 如果没有越界  标记为1
    matrix[r][c] = 1

    count += 1
    # 分别向四个方向走
    find_num_point(r + 1, c, rows, cols, k, matrix)
    find_num_point(r, c + 1, rows, cols, k, matrix)
    find_num_point(r - 1, c, rows, cols, k, matrix)
    find_num_point(r, c - 1, rows, cols, k, matrix)


if __name__ == "__main__":
    # 问题1: 告诉你一些行列坐标拆解之和大于K的点不能走  问你能走多少点  上下左右都可以走
    print("问题一")
    c = 10
    r = 10
    k = 5
    matrix = [[0 for j in range(c)] for i in range(r)]
    find_num_point(0, 0, c, r, k, matrix)
    print("{}x{}的格子, k值为:{}, 最终能走的格子数:{}".format(c, r, k, count))

    # 问题2: 一个四方矩阵  问你从左上角到右下角有多少条路径 只能往右和往下走
    print("问题二")
    n, m = 2, 3
    data = [[1 for i in range(n)] for j in range(m)]
    # print(data)

    for i in range(1, m):
        for j in range(1, n):
            data[i][j] = data[i-1][j] + data[i][j-1]
    print("总共的路径:", data[m-1][n-1])
