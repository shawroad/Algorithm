"""

@file  : 1-限制交易次数-只能交易一次.py

@author: xiaolu

@time  : 2020-04-16

"""
'''
法宝:
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], -prices[i])
'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2] * n
        for i in range(n):
            if i - 1 == -1:
                dp[i][0] = 0   # 第一天　数组第二维度是0 表示目前手里没有股票
                dp[i][1] = -prices[i]  # 第一天　数组第二维度是1　表示目前手里有股票　那肯定要自掏腰包
                continue

            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])  # 一种是上一步就没有股票　然后干等到第二天, 一种是上一次有　但第二天卖了
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[n-1][0]


# 纯粹是为了省空间
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -float('inf')
        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    sol = Solution()
    sol2 = Solution2()
    result = sol.maxProfit(prices)
    result2 = sol2.maxProfit(prices)
    print(result)
    print(result2)

