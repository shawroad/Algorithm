"""

@file  : 4-不限次数并且每次交易需收取手续费.py

@author: xiaolu

@time  : 2020-04-16

"""
'''
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
解释：相当于买入股票的价格升高了。
在第一个式子里减也是一样的，相当于卖出股票的价格减小了。
'''
from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee) -> int:
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -float('inf')
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i] - fee)
        return dp_i_0


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    fee = 1   # 手续费
    sol = Solution()
    result = sol.maxProfit(prices, fee)
    print(result)