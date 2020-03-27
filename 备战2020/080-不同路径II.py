"""

@file   : 080-不同路径II.py

@author : xiaolu

@time   : 2020-03-24

"""
'''
个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。
说明：m 和 n 的值均不超过 100。
示例 1:
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
'''
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        width = len(obstacleGrid[0])
        height = len(obstacleGrid)
        path_num = [[0 for i in range(width)] for j in range(height)]

        # 初始化第一行
        for i in range(width):
            if obstacleGrid[0][i] != 1:
                path_num[0][i] = 1
            else:
                break

        # 初始化第一列
        for j in range(height):
            if obstacleGrid[j][0] != 1:
                path_num[j][0] = 1
            else:
                break

        for i in range(1, height):
            for j in range(1, width):
                if obstacleGrid[i][j] == 1:
                    path_num[i][j] = 0
                else:
                    path_num[i][j] = path_num[i-1][j] + path_num[i][j-1]
        return path_num[height-1][width-1]


if __name__ == '__main__':
    # obstacleGrid = [[0, 0, 0],
    #                 [0, 1, 0],
    #                 [0, 0, 0]]
    obstacleGrid = [[0, 0], [1, 1], [0, 0]]
    sol = Solution()
    result = sol.uniquePathsWithObstacles(obstacleGrid)
    print(result)
