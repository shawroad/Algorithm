"""

@file  : 090-合并区间.py

@author: xiaolu

@time  : 2020-04-16

"""
'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 0:
            return []
        # # 先对区间的第一维度进行排序  冒泡
        # for i in range(len(intervals)-1, -1, -1):
        #     for j in range(len(intervals)-1):
        #         if intervals[j][0] > intervals[j+1][0]:
        #             temp = intervals[j]
        #             intervals[j] = intervals[j+1]
        #             intervals[j+1] = temp

        intervals.sort(key=lambda x: x[0])

        # 区间已经排序
        start = intervals[0][0]
        end = intervals[0][1]
        result = []
        for idx in range(1, len(intervals)):

            curStart, curEnd = intervals[idx]

            # 如果有重叠 则需要更新end
            if curStart <= end:
                end = max(end, curEnd)
            else:
                # 如果没有重叠 则添加  并更新过起点和终点
                result.append([start, end])
                start = curStart
                end = curEnd

        result.append([start, end])
        return result


if __name__ == '__main__':
    intervals = [[8, 10], [1, 3], [15, 18], [2, 6]]
    sol = Solution()
    result = sol.merge(intervals)
    print(result)
