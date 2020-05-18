"""

@file  : 008-买卖股票的最佳时机.py

@author: xiaolu

@time  : 2020-05-14

"""
'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。
 

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
     
示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''
from typing import List


# 暴力搜索
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_value = 0
#         for i in range(0, len(prices)):
#             for j in range(i, len(prices)):
#                 if prices[j] - prices[i] > max_value:
#                     max_value = prices[j] - prices[i]
#         return max_value if max_value > 0 else 0


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > max_profit:
                max_profit = p - min_price
        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    result = sol.maxProfit(prices)
    print(result)

