"""

@file  : 006-克鲁斯卡尔算法实现最小生成树.py

@author: xiaolu

@time  : 2019-09-27

"""
from pylab import *

if __name__ == "__main__":
    INFINITY = 65535   # 代表无穷大
    vexs = [[0, 10, INFINITY, INFINITY, INFINITY, 11, INFINITY, INFINITY, INFINITY],
            [10, 0, 18, INFINITY, INFINITY, INFINITY, 16, INFINITY, 12],
            [INFINITY, 18, 0, 22, INFINITY, INFINITY, INFINITY, INFINITY, 8],
            [INFINITY, INFINITY, 22, 0, 20, INFINITY, INFINITY, 16, 21],
            [INFINITY, INFINITY, INFINITY, 20, 0, 26, INFINITY, 7, INFINITY],
            [11, INFINITY, INFINITY, INFINITY, 26, 0, 17, INFINITY, INFINITY],
            [INFINITY, 16, INFINITY, 24, INFINITY, 17, 0, 19, INFINITY],
            [INFINITY, INFINITY, INFINITY, 16, 7, INFINITY, 19, 0, INFINITY],
            [INFINITY, 12, 8, 21, INFINITY, INFINITY, INFINITY, INFINITY, 0]]

    lengthVex = len(vexs)   # 邻接矩阵大小
    beginEdge = []  # 有权边的起始点
    endEdge = []  # 有权边的终止点
    weight = []  # 权重值
    group = []  # 所有点节点

    # 生成边集数组
    for i in range(lengthVex):
        group.append([i])  # 节点编号从0 到 8
        for j in range(i + 1, lengthVex):
            if vexs[i][j] > 0 and vexs[i][j] < INFINITY:
                # 说明右边
                beginEdge.append(i)   # 每条边的起点
                endEdge.append(j)    # 每条边的终点
                weight.append(vexs[i][j])   # 每条边的权值

    # 边的条数
    lengthEdge = len(weight)

    sum = 0
    for i in range(lengthEdge):   # 遍历每一条边
        I = argsort(weight)[0]    # 按权重的大小排序　最终只落实在索引上
        for j in range(lengthVex):
            if beginEdge[I] in group[j]:
                m = j
            if endEdge[I] in group[j]:
                n = j

        if m != n:    # 判断当前这条边是否属于不同的连通分量，如果是，将其合并
            group[m] = group[m] + group[n]
            group[n] = []
            sum = sum + weight[I]
            print(weight[I], end=', ')
        del weight[I]     # 删除遍历过的边以及顶点
        del beginEdge[I]
        del endEdge[I]

    print("\n最小生成树的代价总和: ", sum)
