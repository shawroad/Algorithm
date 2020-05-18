"""

@file  : 009-长度最小的子数组.py

@author: xiaolu

@time  : 2020-05-18

"""
'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，
并返回其长度。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n*n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
'''
from typing import List


# solution 和　solution1都是超时算法　　暴力求解
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i = 0
        min_len = len(nums) + 1

        while i < len(nums):
            j = i
            S = 0
            while j < len(nums):
                S += nums[j]
                if S >= s:
                    min_len = min(min_len, j-i+1)
                    break
                j += 1
            i += 1
        return 0 if min_len == len(nums) + 1 else min_len


class Solution1:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_len = len(nums) + 1
        n = len(nums)
        for i in range(n):
            start = i
            sum_ = 0
            while start < n:
                sum_ += nums[start]
                start += 1
                if sum_ >= s:
                    min_len = min(min_len, start - i)
                    break
        return 0 if min_len == len(nums) + 1 else min_len


# 优化算法
class Solution2:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        left, sum = 0, 0
        for i in range(n):
            sum += nums[i]
            while sum >= s:
                ans = min(ans, i + 1 - left)
                sum -= nums[left]
                left += 1
        return 0 if ans == float('inf') else ans


if __name__ == '__main__':
    # s = 7
    # nums = [2, 3, 1, 2, 4, 3]

    # s = 11
    # nums = [1, 2, 3, 4, 5]

    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    sol = Solution2()
    result = sol.minSubArrayLen(s, nums)
    print(result)
