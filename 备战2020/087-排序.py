"""

@file   : 087-排序.py

@author : xiaolu

@time   : 2020-03-31

"""
from typing import List


# class Solution:
#     # 显示冒泡超时
#     def sortArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         for i in range(n-1, -1, -1):
#             sign = 1
#             for j in range(0, i):
#                 if nums[j] > nums[j+1]:
#                     sign = 0
#                     temp = nums[j]
#                     nums[j] = nums[j+1]
#                     nums[j+1] = temp
#             if sign == 1:
#                 break
#         return nums


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 快排
        i = 0
        j = len(nums) - 1
        self.quickSort(nums, i, j)
        return nums

    def quickSort(self, nums, low, high):
        i = low
        j = high
        if low < high:
            temp = nums[low]
            while i < j:
                while i < j and nums[j] > temp:
                    j -= 1
                if i < j:
                    nums[i] = nums[j]
                    i += 1

                while i < j and nums[i] < temp:
                    i += 1
                if i < j:
                    nums[j] = nums[i]
                    j -= 1
            nums[i] = temp
            self.quickSort(nums, low, i-1)
            self.quickSort(nums, i+1, high)


if __name__ == '__main__':
    nums = [2, 3, 12, 32, 0, 12, 312]
    sol = Solution()
    result = sol.sortArray(nums)
    print(result)
