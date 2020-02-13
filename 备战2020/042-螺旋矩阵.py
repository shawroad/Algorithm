"""

@file   : 042-螺旋矩阵.py

@author : xiaolu

@time   : 2020-02-13

"""
'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
'''
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix

        # 左 到 右
        i = 0
        j = len(matrix[0])
        # 上 到 下
        m = 0
        n = len(matrix)
        result = []
        while i < j and m < n:
            if i < j and m < n:
                for k in range(i, j):
                    result.append(matrix[m][k])
                m += 1

            if i < j and m < n:
                for k in range(m, n):
                    result.append(matrix[k][j-1])
                j -= 1

            if i < j and m < n:
                for k in range(j-1, i-1, -1):
                    result.append(matrix[n-1][k])
                n -= 1

            if i < j and m < n:
                for k in range(n-1, m-1, -1):
                    result.append(matrix[k][i])
                i += 1
        return result


if __name__ == '__main__':
    # matrix = [[1, 2, 3],
    #           [4, 5, 6],
    #           [7, 8, 9]]
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
    sol = Solution()
    result = sol.spiralOrder(matrix)
    print(result)


