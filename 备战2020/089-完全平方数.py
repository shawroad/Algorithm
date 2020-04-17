"""

@file  : 089-完全平方数.py

@author: xiaolu

@time  : 2020-04-15

"""
'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:
输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.

示例 2:
输入: n = 13
输出: 2
解释: 13 = 4 + 9.
'''

'''
思路: 动态规划　　欲求n 借用n之前某个数的平方和结果
'''
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n + 1)    # 0->n 所有数都由几个平方数组成
        for i in range(1, n+1):
            dp[i] = i   # dp[1] = 1相当于就是1是有平方数1组成的
            j = 1
            while (i - j * j) >= 0:
                dp[i] = min(dp[i], dp[i - j * j] + 1)  # i之前的平方数个数+1就是i由几个平方数组成
                j += 1
        return dp[-1]


if __name__ == '__main__':
    n = 13
    sol = Solution()
    result = sol.numSquares(n)


