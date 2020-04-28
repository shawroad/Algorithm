"""

@file  : 092-岛屿数量.py

@author: xiaolu

@time  : 2020-04-20

"""
'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1:
输入:
11110
11010
11000
00000
输出: 1

示例 2:
输入:
11000
11000
00100
00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
'''
from typing import List


# 深度优先遍历解法
class Solution:
    def dfs(self, grid, x, y):
        grid[x][y] = '0'
        row = len(grid) - 1
        col = len(grid[0]) - 1
        for i, j in (x-1, y), (x, y-1), (x+1, y), (x, y+1):
            if 0 <= i <= row and 0 <= j <= col and grid[i][j] == '1':
                self.dfs(grid, i, j)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        num_island = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_island += 1
                    self.dfs(grid, i, j)
        return num_island


if __name__ == '__main__':
    # grid = [['1', '1', '1', '1', '0'],
    #         ['1', '1', '0', '1', '0'],
    #         ['1', '1', '0', '0', '0'],
    #         ['0', '0', '0', '0', '0']]

    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']]
    sol = Solution()
    result = sol.numIslands(grid)
    print(result)

