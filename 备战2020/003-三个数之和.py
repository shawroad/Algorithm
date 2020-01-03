"""

@file   : 003-三个数之和.py

@author : xiaolu

@time   : 2020-01-02

"""
'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存
在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
'''
class Solution:
    def threeSum(self, nums):
        n = len(nums)

        result = []
        if not nums or n<3:
            return []

        # 对给定列表排序
        nums.sort()

        for i in range(n):
            if nums[i] > 0:
                return result
            if i > 0 and nums[i] == nums[i - 1]:
                continue   # 出现重复值

            L = i + 1
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    result.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L = L + 1   # 消除重复解
                    while L < R and nums[R] == nums[R - 1]:
                        R = R - 1   # 消除重复解

                    L, R = L + 1, R - 1

                elif nums[i] + nums[L] + nums[R] > 0:
                    R = R - 1

                else:
                    L = L + 1
        return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    result = sol.threeSum(nums)
    print(result)


