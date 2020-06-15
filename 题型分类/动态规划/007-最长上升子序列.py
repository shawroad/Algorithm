"""

@file  : 007-最长上升子序列.py

@author: xiaolu

@time  : 2020-06-09

"""
'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
'''
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            temp = []
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    temp.append(dp[j])
            if len(temp) > 0:
                dp[i] = max(temp) + 1

        return max(dp)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    sol = Solution()
    result = sol.lengthOfLIS(nums)
    print(result)


