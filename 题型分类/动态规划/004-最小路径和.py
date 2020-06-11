"""

@file  : 004-最小路径和.py

@author: xiaolu

@time  : 2020-06-09

"""
'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        row = len(grid)
        dp = [[0] * col for i in range(row)]

        # 处理首行
        dp[0][0] = grid[0][0]
        for i in range(1, col):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        # 处理首列
        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[row-1][col-1]


if __name__ == '__main__':
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]

    sol = Solution()
    result = sol.minPathSum(grid)
    print(result)




