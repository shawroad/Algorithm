"""

@file  : 002-打家劫舍2.py

@author: xiaolu

@time  : 2020-04-27

"""

'''
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，
这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间
相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:
输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2:
输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
'''
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1 or len(nums) == 2:
            return max(nums)

        # 不外乎就是第一家到底偷不偷
        # 第一家偷 第二家和最后一家必不能偷　
        result = [0 for i in range(len(nums))]
        result[0], result[1] = nums[0], nums[0]
        for i in range(2, len(nums) - 1):
            result[i] = max(nums[i] + result[i-2], result[i-1])
        result[len(nums)-1] = result[len(nums) - 2]

        # 第一家不能偷　
        result2 = [0 for i in range(len(nums))]
        result2[0] = 0
        result2[1] = nums[1]
        for i in range(2, len(nums)):
            result2[i] = max(nums[i] + result2[i-2], result2[i-1])

        data = result + result2
        return max(data)


if __name__ == '__main__':
    # nums = [1, 2, 3, 1]
    nums = [2, 3, 2]
    sol = Solution()
    result = sol.rob(nums)
    print(result)
