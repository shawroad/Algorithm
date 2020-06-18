"""

@file  : 009-统计全为1的正方形子矩阵.py

@author: xiaolu

@time  : 2020-06-10

"""
'''
给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。
 
示例 1：
输入：matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
输出：15
解释： 
边长为 1 的正方形有 10 个。
边长为 2 的正方形有 4 个。
边长为 3 的正方形有 1 个。
正方形的总数 = 10 + 4 + 1 = 15.

示例 2：
输入：matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
输出：7
解释：
边长为 1 的正方形有 6 个。 
边长为 2 的正方形有 1 个。
正方形的总数 = 6 + 1 = 7.
'''
from typing import List


# 看懂了
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp, nums = matrix, 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    if i >= 1 and j >= 1:
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    nums += dp[i][j]
        return nums


if __name__ == '__main__':
    matrix =[
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ]
    sol = Solution()
    result = sol.countSquares(matrix)
    print(result)
