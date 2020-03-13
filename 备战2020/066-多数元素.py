"""

@file   : 066-多数元素.py

@author : xiaolu

@time   : 2020-03-13

"""
'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [3,2,3]
输出: 3

示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2
'''
from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums) // 2
        nums = Counter(nums)
        nums = dict(nums)

        for d, n in nums.items():
            if n > l:
                return d


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    sol = Solution()
    result = sol.majorityElement(nums)
    print(result)
