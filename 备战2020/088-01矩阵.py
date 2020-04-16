"""

@file  : 088-01矩阵.py

@author: xiaolu

@time  : 2020-04-15

"""
'''
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。

示例 1: 
输入:
0 0 0
0 1 0
0 0 0
输出:
0 0 0
0 1 0
0 0 0

示例 2: 
输入:
0 0 0
0 1 0
1 1 1
输出:
0 0 0
0 1 0
1 2 1

注意:
给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。
'''
from typing import List
import collections

# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#
#         m, n = len(matrix), len(matrix[0])
#         # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
#         dist = [[10**9] * n for _ in range(m)]
#
#         # 如果 (i, j) 的元素为 0，那么距离为 0
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     dist[i][j] = 0
#
#         # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序
#         for i in range(m):
#             for j in range(n):
#                 if i - 1 >= 0:
#                     dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
#                 if j - 1 >= 0:
#                     dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
#
#         # 只有 水平向左移动 和 竖直向下移动，注意动态规划的计算顺序
#         for i in range(m - 1, -1, -1):
#             for j in range(n):
#                 if i + 1 < m:
#                     dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
#                 if j - 1 >= 0:
#                     dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
#         # 只有 水平向右移动 和 竖直向上移动，注意动态规划的计算顺序
#         for i in range(m):
#             for j in range(n - 1, -1, -1):
#                 if i - 1 >= 0:
#                     dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
#                 if j + 1 < n:
#                     dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
#         # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
#         for i in range(m - 1, -1, -1):
#             for j in range(n - 1, -1, -1):
#                 if i + 1 < m:
#                     dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
#                 if j + 1 < n:
#                     dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
#         return dist

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]

        # 将所有零加入队列
        q = collections.deque(zeroes_pos)
        # 这里面是所有零的坐标
        seen = set(zeroes_pos)

        # 广度搜索
        while q:
            i, j = q.popleft()  # 出队 从左边弹出一个元素　　# 广度遍历先从所有的零开始

            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                # 当前零周围的元素
                # (ni, nj) not in seen 主要就是不考虑零元素
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1   # 广度　因为把零所在的坐标全部添加到列表中了　所以这里都是1
                    q.append((ni, nj))
                    seen.add((ni, nj))
        return dist


if __name__ == '__main__':
    matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    sol = Solution()
    result = sol.updateMatrix(matrix)
    print(result)




