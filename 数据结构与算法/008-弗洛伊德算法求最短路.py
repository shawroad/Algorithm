"""

@file  : 008-弗洛伊德算法求最短路.py

@author: xiaolu

@time  : 2019-10-10

"""
stack = []
def find_path(path, i, j):
    # 假设这里想找到是a到g的最短路径　也就是0到6的最短路
    temp = path[i][j]
    stack.insert(0, temp)
    if temp == -1:
        return
    else:
        find_path(path, i, temp)
        find_path(path, temp, j)


if __name__ == '__main__':
    # a, b, c, d, e, f, g
    # 最后求出a->g的最短路
    inf = 10000
    matrix = [
        [  0, inf,   5,   2, inf, inf, inf],
        [ 11,   0,   4, inf, inf,   4, inf],
        [inf,   3,   0, inf,   2,   7, inf],
        [inf, inf, inf,   0,   6, inf, inf],
        [inf, inf, inf, inf,   0, inf,   2],
        [inf, inf, inf, inf, inf,   0,   3],
        [inf, inf, inf, inf, inf, inf,   0]
    ]
    # 此时matrix就是初始的邻接矩阵　我们再建立一个path矩阵
    path = [[-1 for i in range(len(matrix[0]))] for j in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if (matrix[j][i] + matrix[i][k]) < matrix[j][k]:
                    matrix[j][k] = matrix[j][i] + matrix[i][k]
                    path[j][k] = i
    begin = 0
    end = 4
    find_path(path, begin, end)

    stack.append(end)
    stack.insert(0, begin)
    print("最后的最短路径长度:", matrix[begin][end])
    print("路径:")
    for i in stack:
        if i != -1:
            print(i, end=' ')

