"""

@file   : 054-杨辉三角.py

@author : xiaolu

@time   : 2020-02-25

"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows == 0:
            return res

        res.append([1])
        if numRows == 1:
            return res

        for i in range(1, numRows):
            tmp = []
            for j in range(i+1):
                if 1 <= j < i:
                    tmp.append(res[i-1][j-1] + res[i-1][j])
                else:
                    tmp.append(1)
            res.append(tmp)
        return res


if __name__ == '__main__':
    numRows = 4
    sol = Solution()
    result = sol.generate(numRows)
    print('结果:', result)

