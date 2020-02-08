"""

@file   : 037-合并区间.py

@author : xiaolu

@time   : 2020-02-07

"""
'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6]

'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # # 简单选择排序
        # for i, inter in enumerate(intervals):
        #     k = i
        #     min_val = inter[0]
        #     for j in range(i + 1, len(intervals)):
        #         if intervals[j][0] < min_val:
        #             min_val = intervals[j][0]
        #             k = j
        #     temp = intervals[i]
        #     intervals[i] = intervals[k]
        #     intervals[k] = temp

        # 或者把排序直接写成
        intervals.sort(key=lambda x: x[0])

        i = 0
        while i < (len(intervals) - 1):
            if intervals[i][1] >= intervals[i+1][0]:
                temp = [intervals[i][0], max(intervals[i+1][1], intervals[i][1])]
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i, temp)
            else:
                i += 1
        return intervals


class Solution1:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


if __name__ == '__main__':
    # nums = [[1, 3], [2, 6], [8, 10], [7, 18]]
    # nums = [[1,4],[2,3]]
    nums = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    sol = Solution()
    result = sol.merge(nums)
    print(result)

    sol1 = Solution1()
    result = sol1.merge(nums)
    print(result)




