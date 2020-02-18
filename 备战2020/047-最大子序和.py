"""

@file   : 047-最大子序和.py

@author : xiaolu

@time   : 2020-02-17

"""
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''
from typing import List


# 1. 分治法
class Solution:
    def cross_sum(self, nums, left, right, p):
        if left == right:
            return nums[left]

        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(p, left - 1, -1):
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)

        right_subsum = float('-inf')
        curr_sum = 0
        for i in range(p + 1, right + 1):
            curr_sum += nums[i]
            right_subsum = max(right_subsum, curr_sum)

        return left_subsum + right_subsum

    def helper(self, nums, left, right):
        if left == right:
            return nums[left]

        p = (left + right) // 2

        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)
        return max(left_sum, right_sum, cross_sum)

    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums) - 1)


# 2. 贪心算法
class Solution1:
    def maxSubArray(self, nums):
        n = len(nums)
        curr_sum = max_sum = nums[0]
        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # sol = Solution()
    # result = sol.maxSubArray(nums)
    # print(result)

    sol1 = Solution1()
    result = sol1.maxSubArray(nums)
    print(result)




