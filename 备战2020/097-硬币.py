"""

@file  : 097-硬币.py

@author: xiaolu

@time  : 2020-04-23

"""
'''
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)

示例1:
输入: n = 5
输出：2
解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1

示例2:
输入: n = 10
输出：4
解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1

说明：
注意:
你可以假设：
0 <= n (总金额) <= 1000000
'''
# class Solution:
#     def waysToChange(self, n: int) -> int:
#         result = 0
#         # 25, 10, 5, 1
#         for i in range(0, n // 25 + 1):
#             temp1 = n - i * 25
#             for j in range(0, temp1 // 10 + 1):
#                 result += (temp1 - j * 10) // 5 + 1
#         return result


class Solution:
    def waysToChange(self, n: int) -> int:
        mod = 10 ** 9 + 7

        ans = 0
        for i in range(n // 25 + 1):
            res = n - i * 25
            a, b = res // 10, res % 10 // 5
            ans += (a + 1) * (a + b + 1)
        return ans % mod


if __name__ == '__main__':
    n = 5
    sol = Solution()
    result = sol.waysToChange(n)
    print(result)
