# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 9:54
# @Author  : xiaolu
# @FileName: 005-最长公共子序列.py
# @Software: PyCharm

# 首先推出状态转移方程
# A, B
# i=0, j = 0    m[i][j] = 0
# i,j != 0 and Ai == Bj  m[i][j] = m[i-1][j-1] + 1
# i,j != 0 and Ai != Bj  m[i][j] = max(m[i-1][j], m[i][j-1])



