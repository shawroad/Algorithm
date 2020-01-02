"""

@file   : 002-两数之和.py

@author : xiaolu

@time   : 2020-01-02

"""
'''
题目描述:
给定一个整数数组 nums 和一个目标值 target，请你在该
数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
'''
if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            k = nums[i] + nums[j]
            if k == target:
                print("两个数的下标分别为:{}, {}".format(i, j))
