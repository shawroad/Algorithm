"""

@file  : 002-最大子序和.py

@author: xiaolu

@time  : 2020-06-09

"""
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            else:
                dp[i] = max(nums[i], dp[i-1] + nums[i])
        return max(dp)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    result = sol.maxSubArray(nums)
    print(result)


