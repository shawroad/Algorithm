"""

@file   : 005-两数之和 II - 输入有序数组.py

@author : xiaolu

@time   : 2020-01-04

"""
'''
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
'''
class Solution:
    def twoSum(self, numbers, target):
        i, j = 0, len(numbers)-1
        while i < j:
            temp = numbers[i] + numbers[j]
            if temp == target:
                return i+1, j+1
            elif temp < target:
                i += 1
            else:
                j -= 1


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    result = sol.twoSum(numbers, target)
    print(result)
