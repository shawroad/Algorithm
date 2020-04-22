"""

@file  : 2-不限制交易次数-无限次交易.py

@author: xiaolu

@time  : 2020-04-16

"""
'''
法宝:
因为k = +infinity 所以k  k-1 在我们眼里是一样的
我们发现数组中的 k 已经不会改变了，也就是说不需要记录 k 这个状态了：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -float('inf')
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    sol = Solution()
    result = sol.maxProfit(prices)
    print(result)

