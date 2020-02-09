"""

@file   : 038-跳跃游戏.py

@author : xiaolu

@time   : 2020-02-07

"""
'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
'''
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= last-i:
                last = i
        if last == 0:
            return True
        return False


class Solution1:
    def canJump(self, nums):
        max_i = 0       # 初始化当前能到达最远的位置
        for i, jump in enumerate(nums):   # i为当前位置，jump是当前位置的跳数
            if max_i >= i and i+jump > max_i:  # 如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i+jump   # 更新最远能到达位置
        return max_i >= i


if __name__ == '__main__':
    # nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1, 0, 4]
    sol = Solution()
    result = sol.canJump(nums)
    print(result)

    sol = Solution1()
    result = sol.canJump(nums)
    print(result)





