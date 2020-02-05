"""

@file   : 034-搜索旋转排序数组.py

@author : xiaolu

@time   : 2020-02-03

"""
from typing import List


# 垃圾方法
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        if target > nums[i]:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        elif target < nums[i]:
            for i in range(len(nums)-1, -1, -1):
                if nums[i] == target:
                    return i
        else:
            return i


# 好方法: 借助二叉查找
class Solution1:
    def search(self, nums, target):
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        # 说明中间值在后半部分
                        right = pivot - 1
                    else:
                        left = pivot + 1

        def search(left, right):
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1

        n = len(nums)
        if n == 0:    # 数组的长度为0
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1

        # 找中间旋转那一块的索引
        rotate_index = find_rotate_index(0, n - 1)

        if nums[rotate_index] == target:
            return rotate_index

        if rotate_index == 0:
            return search(0, n-1)

        # 说明出在后半段
        if target < nums[0]:
            return search(rotate_index, n-1)

        return search(0, rotate_index)


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    # sol = Solution()
    # result = sol.search(nums, target)
    # print(result)

    sol = Solution1()
    result = sol.search(nums, target)
    print(result)




