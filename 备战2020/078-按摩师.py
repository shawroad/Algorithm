"""

@file   : 078-按摩师.py

@author : xiaolu

@time   : 2020-03-24

"""
'''
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。
在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，
替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。
注意：本题相对原题稍作改动

示例 1：
输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。

示例 2：
输入： [2,7,9,3,1]
输出： 12
解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。

示例 3：
输入： [2,1,4,5,3,1,1,3]
输出： 12
解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。
'''
from typing import List


class Solution:
    '''
    采用动态规划的方法
    '''
    def massage(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        d0, d1 = 0, nums[0]  # 代表第0的不预约和第0个预测的时长
        for i in nums[1:]:
            select_0 = max(d0, d1)   # 当前步不预约 那就看前一步的最大的结果
            select_1 = i + d0    # 当前步预约  那就是当前步结果加前一步不预约的结果
            d0 = select_0
            d1 = select_1

        return max(d0, d1)


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    sol = Solution()
    result = sol.massage(nums)
    print(result)


