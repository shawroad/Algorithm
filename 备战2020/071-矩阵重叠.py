"""

@file   : 071-矩阵重叠.py

@author : xiaolu

@time   : 2020-03-18

"""
'''
矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
给出两个矩形，判断它们是否重叠并返回结果。

示例 1：
输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
输出：true

示例 2：
输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
输出：false

说明：
两个矩形 rec1 和 rec2 都以含有四个整数的列表的形式给出。
矩形中的所有坐标都处于 -10^9 和 10^9 之间。

'''
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # 不重叠 不外乎rec1在rec2的上下左右方向
        # return not(
        #         rec1[3] <= rec2[1] or   # rec1在rec2的左边
        #         rec1[0] <= rec2[2] or   # rec1在rec2的上边
        #         rec1[1] >= rec2[3] or   # rec1在rec2的右边
        #         rec1[2] >= rec2[0]    # rec1在rec2的下边
        # )

        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])  # top


if __name__ == '__main__':
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    sol = Solution()
    result = sol.isRectangleOverlap(rec1, rec2)
    print(result)
