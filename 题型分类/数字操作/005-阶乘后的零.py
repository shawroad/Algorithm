"""

@file  : 005-阶乘后的零.py

@author: xiaolu

@time  : 2020-05-20

"""
'''
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
'''
# 方法一: 超时
# class Solution:
#     def trailingZeroes(self, n: int) -> int:
#         res = 1
#         for i in range(1, n + 1):
#             res *= i
#         count = 0
#         res = str(res)
#
#         for i in range(len(res)-1, -1, -1):
#             if res[i] == '0':
#                 count += 1
#             else:
#                 break
#         return count


class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        while n > 0:
            n //= 5
            zero_count += n
        return zero_count


if __name__ == '__main__':
    n = 5
    sol = Solution()
    result = sol.trailingZeroes(n)
    print(result)
