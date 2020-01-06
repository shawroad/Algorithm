"""

@file   : 006-和为K的子数组.py

@author : xiaolu

@time   : 2020-01-05

"""
'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
'''

class Solution:
    def subarraySum(self, nums, k):
        if not nums:
            return 0
        sum_t = 0
        count = 0
        dic = {0: 1}
        for i in nums:
            sum_t += i
            if sum_t - k in dic:
                count += dic[sum_t - k]

            dic[sum_t] = dic.get(sum_t, 0) + 1
        return count


if __name__ == '__main__':
    '''
    setdefault(key, default=None) 
    参数
    key -- 查找的键值。
    default -- 键不存在时，设置的默认键值。
    '''
    nums = [1, 1, 1]
    k = 2
    sol = Solution()
    result = sol.subarraySum(nums, k)
    print("最终的结果:", result)


