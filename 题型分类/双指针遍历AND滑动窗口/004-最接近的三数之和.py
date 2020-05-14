"""

@file  : 004-最接近的三数之和.py

@author: xiaolu

@time  : 2020-05-11

"""
'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        diff_value = float('inf')

        nums.sort()

        i = 0
        while i < n:
            L = i + 1
            R = n - 1
            while L < R:
                if abs(nums[i] + nums[L] + nums[R] - target) < diff_value:
                    diff_value = abs(nums[i] + nums[L] + nums[R] - target)
                    result = [nums[i], nums[L], nums[R]]

                if nums[i] + nums[L] + nums[R] - target < 0:
                    L += 1
                else:
                    R -= 1

            i += 1
        return sum(result)

if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    sol = Solution()
    result = sol.threeSumClosest(nums, target)
    print(result)



