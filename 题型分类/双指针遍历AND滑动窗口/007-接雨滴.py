"""

@file  : 007-接雨滴.py

@author: xiaolu

@time  : 2020-05-12

"""
'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，
在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        i = 0
        j = len(height) - 1
        left_cur_max = 0
        right_cur_max = 0
        pre = 0

        area = 0
        while i < j:
            if left_cur_max <= right_cur_max:
                while i < j and height[i] <= left_cur_max:
                    i += 1

            if left_cur_max >= right_cur_max:
                while i < j and height[j] <= right_cur_max:
                    j -= 1

            area += (min(height[i], height[j]) - pre) * (j - i + 1)

            pre = min(height[i], height[j])

            left_cur_max = height[i]
            right_cur_max = height[j]

            # i += 1
            # j -= 1
        return area - sum(height)


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [0, 2, 0]
    sol = Solution()
    result = sol.trap(height)
    print(result)

