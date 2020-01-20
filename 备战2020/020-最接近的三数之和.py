"""

@file   : 020-最接近的三数之和.py

@author : xiaolu

@time   : 2020-01-15

"""
'''
给定一个包括n个整数的数组nums和一个目标值target。找出nums中的三个整数，
使得它们的和与target最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''
class Solution:
    # 暴力解法
    def threeSumClosest(self, nums, target):
        min_val = 1000
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    chazhi = nums[i] + nums[j] + nums[k] - target
                    chazhi = abs(chazhi)
                    if chazhi < min_val:
                        min_val = chazhi
                        result = nums[i] + nums[j] + nums[k]

        return result


# 双指针法
class Solution2:
    def threeSumClosest(self, nums, target):
        min_value = 20000
        nums.sort()
        for i in range(len(nums)):

            m = i + 1
            n = len(nums) - 1
            while m < n:
                sum_ = nums[i] + nums[m] + nums[n]
                if abs(sum_ - target) < min_value:
                    min_value = abs(sum_ - target)
                    result = sum_

                if sum_ < target:
                    m += 1
                else:
                    n -= 1
        return result


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    sol = Solution()
    result = sol.threeSumClosest(nums, target)
    print("最终的结果:", result)

    sol2 = Solution2()
    res = sol2.threeSumClosest(nums, target)
    print("最终的结果:", res)


