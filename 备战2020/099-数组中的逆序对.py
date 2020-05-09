"""

@file  : 099-数组中的逆序对.py

@author: xiaolu

@time  : 2020-04-24

"""
'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。

示例 1:
输入: [7,5,6,4]
输出: 5
'''
from typing import List


# # 1. 最简单的方式(超时)
# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         count = 0
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] > nums[j]:
#                     count += 1
#         return count


# 2. 借助归并排序
class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        self.cnt = 0

        def merge(nums, start, mid, end):
            i, j, temp = start, mid + 1, []
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    self.cnt += mid - i + 1
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1

            for i in range(len(temp)):
                nums[start + i] = temp[i]

        def mergeSort(nums, start, end):
            if start >= end:
                return
            mid = (start + end) >> 1  # 相当于除2 有小数的话 直接舍掉 然后+1
            mergeSort(nums, start, mid)
            mergeSort(nums, mid+1, end)
            merge(nums, start, mid, end)

        mergeSort(nums, 0, len(nums) - 1)
        return self.cnt


if __name__ == '__main__':
    data = [7, 5, 6, 4]
    sol = Solution()
    result = sol.reversePairs(data)
    print(result)
