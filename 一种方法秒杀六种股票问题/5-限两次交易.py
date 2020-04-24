"""

@file  : 5-限两次交易.py

@author: xiaolu

@time  : 2020-04-16

"""
'''
原始的动态转移方程，没有可化简的地方
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_k = 2
        dp = [[[0] * 2] * (max_k + 1)] * n

        for i in range(n):
            for k in range(max_k, 0, -1):
                if i - 1 == -1:
                    for k in range(3):  # base case i=0
                        dp[0][k][0] = 0
                        dp[0][k][1] = -prices[0]

                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

        return dp[n-1][max_k][0]


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    sol = Solution()
    result = sol.maxProfit(prices)
    print(result)