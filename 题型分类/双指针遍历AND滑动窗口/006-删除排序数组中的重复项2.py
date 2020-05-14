"""

@file  : 006-删除排序数组中的重复项2.py

@author: xiaolu

@time  : 2020-05-11

"""
'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定 nums = [1,1,1,2,2,3],
函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,1,2,3,3],
函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
你不需要考虑数组中超出新长度后面的元素。
'''
from typing import List


class Solution:
    # 直接在原始的列表上进行删除
    def removeDuplicates(self, nums: List[int]) -> int:
        i, count = 1, 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                count += 1
                if count > 2:
                    nums.pop(i)
                    i -= 1
            else:
                count = 1

            i += 1
        return len(nums)


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    sol = Solution()
    result = sol.removeDuplicates(nums)
    print(result)

