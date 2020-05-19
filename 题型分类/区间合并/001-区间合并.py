"""

@file  : 001-区间合并.py

@author: xiaolu

@time  : 2020-05-18

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
        if len(intervals) <= 1:
            return intervals
        result = []
        intervals.sort(key=lambda x: x[0])

        cur_left = intervals[0][0]
        cur_right = intervals[0][1]
        for s in intervals[1:]:
            if s[0] <= cur_right:
                cur_right = max(s[1], cur_right)
            else:
                result.append([cur_left, cur_right])
                cur_left = s[0]
                cur_right = s[1]
        result.append([cur_left, cur_right])
        return result


if __name__ == '__main__':
    intervals = [[8, 10], [1, 3], [2, 6], [15, 18]]
    sol = Solution()
    result = sol.merge(intervals)
    print(result)
