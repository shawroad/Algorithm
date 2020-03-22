"""

@file   : 075-旋转数组.py

@author : xiaolu

@time   : 2020-03-20

"""
'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
'''
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k > 0:
            rotation_num = nums[-k:]
            rotation_num.reverse()

            for n in rotation_num:
                nums.insert(0, n)

            i = 0
            while i < k:
                i += 1
                nums.pop()


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    # nums = [1]
    # k = 0
    sol = Solution()
    sol.rotate(nums, k)
    print(nums)
