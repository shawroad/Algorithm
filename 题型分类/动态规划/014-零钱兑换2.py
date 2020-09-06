# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 21:14
# @Author  : xiaolu
# @FileName: 014-零钱兑换2.py
# @Software: PyCharm
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    sol = Solution()
    res = sol.change(amount, coins)
    print(res)

