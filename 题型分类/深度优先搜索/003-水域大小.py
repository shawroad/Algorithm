# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 19:24
# @Author  : xiaolu
# @FileName: 017-水域大小.py
# @Software: PyCharm
'''
你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。
由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。

示例：

输入：
[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
输出： [1,2,4]
'''
from typing import List

class Solution:
    def pondSizes(self, land):
        if not land:
            return 0

        m, n = len(land), len(land[0])

        def dfs(i, j):
            nonlocal cnt
            if land[i][j] == 0:
                # 当前是海的话
                cnt += 1
                land[i][j] = 1
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n  and land[x][y] == 0:
                    dfs(x, y)
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    cnt = 0
                    dfs(i, j)
                    res.append(cnt)

        return sorted(res)


if __name__ == '__main__':
    land = [[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0,1]]
    sol = Solution()
    result = sol.pondSizes(land)
    print(result)
