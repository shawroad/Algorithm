"""

@file  : 003-三数之和.py

@author: xiaolu

@time  : 2020-05-09

"""
'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        result = []
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                return result
            if i > 0:
                while i < len(nums)-2 and nums[i-1] == nums[i]:
                    i += 1

            low = i + 1
            height = len(nums) - 1
            while low < height:
                if nums[i] + nums[low] + nums[height] == 0:
                    result.append([nums[i], nums[low], nums[height]])
                    while low < height and nums[low+1] == nums[low]:
                        low += 1

                    while low < height and nums[height-1] == nums[height]:
                        height -= 1
                    low += 1
                    height -= 1

                elif nums[i] + nums[low] + nums[height] < 0:
                    low += 1

                else:
                    height -= 1

            i += 1
        return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]

    # [-4, -1, -1, 0, 1, 2]
    sol = Solution()
    result = sol.threeSum(nums)
    print(result)


