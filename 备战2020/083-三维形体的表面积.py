"""

@file   : 083-三维形体的表面积.py

@author : xiaolu

@time   : 2020-03-25

"""
'''
在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
请你返回最终形体的表面积。

示例 1：
输入：[[2]]
输出：10

示例 2：
输入：[[1,2],[3,4]]
输出：34
'''
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0
                        ans += max(grid[r][c] - nval, 0)
        return ans


if __name__ == '__main__':
    grid = [[1, 2], [3, 4]]
    sol = Solution()
    result = sol.surfaceArea(grid)
    print(result)

