"""

@file   : 036-跳跃游戏II.py

@author : xiaolu

@time   : 2020-02-03

"""
'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
'''
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        end = 0
        max_bound = 0
        for i in range(len(nums)-1):
            max_bound = max(max_bound, nums[i]+i)
            if i == end:
                step += 1
                end = max_bound
        return step


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    sol = Solution()
    result = sol.jump(nums)
    print(result)

