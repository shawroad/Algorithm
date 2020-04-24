"""

@file  : 6-不限次数.py

@author: xiaolu

@time  : 2020-04-16

"""
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n // 2 < k:
            return self.maxProfit_any_k(prices)

        dp = [[[0] * 2] * (k + 1)] * n
        for i in range(n):
            for j in range(k, 0, -1):
                if i - 1 == -1:
                    dp[i][1][1] = -prices[0]
                    dp[i][0][0] = 0

                    break

                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[n - 1][k][0]

    def maxProfit_any_k(self, prices: List[int]) -> int:
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -float('inf')
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0


if __name__ == '__main__':
    # prices = [1, 2, 3, 0, 2]
    # k = 2

    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    k = 2
    sol = Solution()
    result = sol.maxProfit(k, prices)
    print(result)