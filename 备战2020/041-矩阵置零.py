"""

@file   : 041-矩阵置零.py

@author : xiaolu

@time   : 2020-02-07

"""
'''
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

'''
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = set(), set()
        R = len(matrix)
        C = len(matrix[0])

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        for r in range(R):
            for c in range(C):
                if r in rows or c in cols:
                    matrix[r][c] = 0

        return matrix


if __name__ == '__main__':
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    sol = Solution()
    result = sol.setZeroes(matrix)
    print(result)



