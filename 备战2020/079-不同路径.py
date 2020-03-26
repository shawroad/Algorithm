"""

@file   : 079-不同路径.py

@author : xiaolu

@time   : 2020-03-24

"""
'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？


示例 1:
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_num = [[1 for i in range(m)] for j in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                path_num[i][j] = path_num[i-1][j] + path_num[i][j-1]
        return path_num[n-1][m-1]


if __name__ == '__main__':
    m = 3
    n = 2
    sol = Solution()
    result = sol.uniquePaths(m, n)
    print(result)

