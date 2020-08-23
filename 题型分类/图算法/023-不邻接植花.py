# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 11:46
# @Author  : xiaolu
# @FileName: 023-不邻接植花.py
# @Software: PyCharm
'''
有 N 个花园，按从 1 到 N 标记。在每个花园中，你打算种下四种花之一。
paths[i] = [x, y] 描述了花园 x 到花园 y 的双向路径。
另外，没有花园有 3 条以上的路径可以进入或者离开。
你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。
以数组形式返回选择的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。
花的种类用  1, 2, 3, 4 表示。保证存在答案。

'''

class Solution(object):
    def gardenNoAdj(self, N, paths):
        if len(paths) == 0:
            return [1] * N   # 如果paths等于0  相当于节点直接没有连接  那直接都种上第一种花

        r = [0] * N  # 默认都还没种
        G = [[] for i in range(N)]   # 建立邻接矩阵
        for x, y in paths:
            G[x-1].append(y-1)
            G[y-1].append(x-1)
        for i in range(N):
            r[i] = ({1, 2, 3, 4} - {r[j] for j in G[i]}).pop()  # 相当于遍历与i直接相邻节点的花 然后让所有花减去,就是你可以选取的了，弹一个就ok了
        return r


if __name__ == '__main__':
    N = 4
    paths = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3]]
    sol = Solution()
    res = sol.gardenNoAdj(N, paths)
    print(res)
