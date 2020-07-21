# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 10:36
# @Author  : xiaolu
# @FileName: 006-全排列.py
# @Software: PyCharm
def main(nums):
    result = []

    def back(nums, track):
        if len(track) == len(nums):
            result.append(track[:])
            return
        for i in range(len(nums)):
            if nums[i] in track:
                continue
            track.append(nums[i])
            back(nums, track)
            track.pop()
    back(nums, [])
    return result


if __name__ == '__main__':
    nums = ['a', 'b', 'c']
    result = main(nums)
    print(result)


