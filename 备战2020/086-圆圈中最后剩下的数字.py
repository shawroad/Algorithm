"""

@file   : 086-圆圈中最后剩下的数字.py

@author : xiaolu

@time   : 2020-03-30

"""
'''
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。
求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则
删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

示例 1：
输入: n = 5, m = 3
输出: 3


示例 2：
输入: n = 10, m = 17
输出: 2
'''
import sys

# 设置递归深度
# sys.setrecursionlimit(100000)
#
#
# class Solution:
#     def lastRemaining(self, n: int, m: int) -> int:
#         return self.f(n, m)
#
#     def f(self, n, m):
#         if n == 0:
#             return 0
#         x = self.f(n-1, m)
#         return (m + x) % n


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f


if __name__ == '__main__':
    n = 5
    m = 3
    sol = Solution()
    result = sol.lastRemaining(n, m)
    print(result)


