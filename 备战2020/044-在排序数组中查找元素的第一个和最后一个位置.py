"""

@file   : 044-在排序数组中查找元素的第一个和最后一个位置.py

@author : xiaolu

@time   : 2020-02-15

"""
'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
'''
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)

        if len(result) >= 1:
            return [result[0], result[-1]]
        else:
            return [-1, -1]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    sol = Solution()
    result = sol.searchRange(nums, target)
    print(result)




