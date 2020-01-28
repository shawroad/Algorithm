"""

@file   : 026-删除排序数组中的重复项.py

@author : xiaolu

@time   : 2020-01-15

"""
'''
给定数组 nums = [1,1,2], 
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
你不需要考虑数组中超出新长度后面的元素。
'''
class Solution:
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1

        nums = nums[:i+1]
        return nums


if __name__ == '__main__':
    nums = [1, 1, 2]
    sol = Solution()
    result = sol.removeDuplicates(nums)
    print("最终的结果:", result)
