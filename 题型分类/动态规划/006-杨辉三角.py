"""

@file  : 006-杨辉三角.py

@author: xiaolu

@time  : 2020-06-09

"""
'''
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        result = [[1], [1, 1]]
        for i in range(2, numRows):
            temp = [1] * (i+1)
            for j in range(1, len(temp)-1):
                temp[j] = result[i-1][j-1] + result[i-1][j]
            result.append(temp)
        return result


if __name__ == '__main__':
    numRows = 5
    sol = Solution()
    result = sol.generate(numRows)
    print(result)

