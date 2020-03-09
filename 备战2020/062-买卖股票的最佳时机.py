"""

@file   : 062-买卖股票的最佳时机.py

@author : xiaolu

@time   : 2020-03-09

"""
'''
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
'''
from typing import List


# 暴力破解
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if (prices[j] - prices[i]) > max_profit:
                    max_profit = prices[j] - prices[i]
        return max_profit


# 一次遍历法
class Solution1:
    def maxProfix(self, prices):
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif (p - min_price) > max_profit:
                max_profit = p - min_price
        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    result = sol.maxProfit(prices)
    print(result)

    sol = Solution1()
    result = sol.maxProfix(prices)
    print(result)






