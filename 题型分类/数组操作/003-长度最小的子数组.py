# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 20:20
# @Author  : xiaolu
# @FileName: 003-长度最小的子数组.py
# @Software: PyCharm

'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

示例：
输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的连续子数组。
'''
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        return 0 if ans == n + 1 else ans


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    sol = Solution()
    result = sol.minSubArrayLen(s, nums)
    print(result)
