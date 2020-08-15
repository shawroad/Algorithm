# -*- coding: utf-8 -*-
# @Time    : 2020/8/15 13:21
# @Author  : xiaolu
# @FileName: 009-统计封闭岛屿的数目.py
# @Software: PyCharm
def closedIsland(grid):
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        nonlocal flag
        if grid[i][j] == 0:
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                flag = False
            grid[i][j] = 1

        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                dfs(x, y)

    res = 0
    for i in range(m):
        for j in range(n):
            flag = True
            if grid[i][j] == 0:
                dfs(i, j)
                if flag:
                    res += 1

    return res


if __name__ == '__main__':
    # 岛屿是0  海水是1
    grid = [[1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]]


    result = closedIsland(grid)
    print(result)

