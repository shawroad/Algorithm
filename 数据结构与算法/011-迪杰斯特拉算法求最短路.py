"""

@file  : 011-迪杰斯特拉算法求最短路.py

@author: xiaolu

@time  : 2019-10-12

"""


def print_path(path, start, end):
    # 打印路径
    road = [end]
    temp = path[end]
    while temp != -1:
        road.append(temp)
        temp = path[temp]
    # road.append(start)
    road.reverse()
    print(road)


if __name__ == '__main__':
    # 定义一个邻接矩阵
    inf = 1000
    matrix = [
        [  0, inf,   5,   2, inf, inf, inf],
        [ 11,   0,   4, inf, inf,   4, inf],
        [inf,   3,   0, inf,   2,   7, inf],
        [inf, inf, inf,   0,   6, inf, inf],
        [inf, inf, inf, inf,   0, inf,   2],
        [inf, inf, inf, inf, inf,   0,   3],
        [inf, inf, inf, inf, inf, inf,   0]
    ]

    dist = [0 for i in range(len(matrix))]  # 最短距离
    path = [0 for i in range(len(matrix))]  # 前驱
    vset = [0 for i in range(len(matrix))]  # 标记有没有被访问

    # 初始点从0开始
    # 初始化
    for i in range(len(matrix)):
        if matrix[0][i] < inf:
            dist[i] = matrix[0][i]
            path[i] = 0
        else:
            dist[i] = inf
            path[i] = -1
    # print(dist)
    # print(path)

    # 起始点是从0开始
    origin = 0
    vset[0] = 1
    path[0] = -1
    u = 0
    for i in range(len(matrix)):  # 控制次数
        min_v = inf
        for j in range(len(matrix)):
            if (vset[j] == 0) and (dist[j] < min_v):
                u = j
                min_v = dist[j]

        vset[u] = 1

        for j in range(len(matrix)):
            if (vset[j] == 0) and (matrix[u][j] < dist[j]):
                dist[j] = matrix[u][j]
                path[j] = u

    print("*"*100)
    print(dist)
    print(path)

    start = 0
    end = 5

    print_path(path, start, end)
