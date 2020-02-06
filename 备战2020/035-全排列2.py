"""

@file   : 035-全排列2.py

@author : xiaolu

@time   : 2020-02-03

"""
'''
给定一个可包含重复数字的序列，返回所有不重复的全排列
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def permute(nums, tmp):
            if not nums:
                result.append(tmp)

            for i in range(len(nums)):
                permute(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        permute(nums, [])

        final_res = []
        for r in result:
            t = '%'.join([str(i) for i in r])
            final_res.append(t)
        final_res = list(set(final_res))
        # print(final_res)   # ['211', '112', '121']

        result = []
        for elem in final_res:
            temp = [int(i) for i in elem.split('%')]
            result.append(temp)

        return result


if __name__ == '__main__':
    nums = [1, 1, 2]
    sol = Solution()
    result = sol.permuteUnique(nums)
    print(result)

