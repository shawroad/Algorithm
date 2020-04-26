"""

@file  : 091-跳跃游戏.py

@author: xiaolu

@time  : 2020-04-17

"""
'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

示例 2:
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
'''
from typing import List


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         now_pos = 0   # 统计走到的位置
#         next_s = nums[0]
#         while True:
#             now_pos = now_pos + next_s
#             if now_pos == len(nums) - 1:
#                 return True
#
#             if now_pos >= len(nums):
#                 return True
#
#             next_s = nums[now_pos]
#             if now_pos == now_pos + next_s:
#                 return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0  # 初始化当前能到达最远的位置
        for i, jump in enumerate(nums):  # i为当前位置，jump是当前位置的跳数
            if max_i >= i and i + jump > max_i:  # 如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i + jump  # 更新最远能到达位置

        return max_i >= i


if __name__ == '__main__':
    # nums = [2, 3, 1, 1, 4]
    # nums = [3, 2, 1, 0, 4]
    # nums = [1, 2, 3]
    nums = [2, 5, 0, 0]
    sol = Solution()
    result = sol.canJump(nums)
    print(result)
