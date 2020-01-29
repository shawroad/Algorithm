"""

@file   : 027-移除元素.py

@author : xiaolu

@time   : 2020-01-16

"""
'''
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

'''

class Solution:
    def removeElement(self, nums, val):
        count = 0
        for n in nums:
            if n == val:
                count += 1

        i = 0
        while i < count:
            nums.remove(val)
            i += 1
        return len(nums)


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    sol = Solution()
    result = sol.removeElement(nums, val)
    print("最终的结果为:", result)



