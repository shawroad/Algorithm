# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 8:38
# @Author  : xiaolu
# @FileName: 001-八皇后问题.py
# @Software: PyCharm


class Solution:
    def solveNQueers(self, n: int):
        st = [['.' for i in range(n)] for j in range(n)]
        res = []
        def dfs(x_d, y_d, cur):
            j = len(cur)
            if len(cur) == n:
                m = []
                for i in st:
                    m.append(''.join(i))
                res.append(m)
            for i in range(n):
                if i not in cur and i + j not in x_d and i - j not in y_d:
                    st[j][i] = 'Q'
                    dfs(x_d+[i+j], y_d+[i-j], cur+[i])
        dfs([], [], [])
        return res


if __name__ == '__main__':
    n = 4
    sol = Solution()
    result = sol.solveNQueers(n)
    print(result)

