"""

@file  : 003-螺旋矩阵.py

@author: xiaolu

@time  : 2020-05-21

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

示例 2:
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        result = []
        left, right = 0, len(matrix[0])-1
        upper, buttom = 0, len(matrix)-1
        while left <= right and upper <= buttom:

            if left <= right and upper <= buttom:
                for i in range(left, right+1):
                    result.append(matrix[upper][i])
                upper += 1

            if left <= right and upper <= buttom:
                for i in range(upper, buttom+1):
                    result.append(matrix[i][right])
                right -= 1

            if left <= right and upper <= buttom:

                for i in range(right, left-1, -1):
                    result.append(matrix[buttom][i])
                buttom -= 1

            if left <= right and upper <= buttom:

                for i in range(buttom, upper-1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result


if __name__ == '__main__':
    data = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
            ]
    # data = [[1, 2, 3],
    #         [4, 5, 6],
    #         [7, 8, 9]]
    sol = Solution()
    result = sol.spiralOrder(data)
    print(result)

