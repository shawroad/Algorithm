"""

@file  : 3-不限次数并每次卖出后要等一天才能交易.py

@author: xiaolu

@time  : 2020-04-16

"""

'''
每次 sell 之后要等一天才能继续交易。只要把这个特点融入上一题的状态转移方程即可：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
解释：第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -float('inf')
        dp_pre_0 = 0   # 表示dp[i-2][0]
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp
        return dp_i_0


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    sol = Solution()
    result = sol.maxProfit(prices)
    print(result)