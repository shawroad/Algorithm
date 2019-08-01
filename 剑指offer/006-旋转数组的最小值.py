"""

@file   : 006-旋转数组的最小值.py

@author : xiaolu

@time   : 2019-07-31

"""
'''
题目: 
    把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个
非递减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的
一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

解析: https://cuijiahua.com/blog/2017/11/basis_6.html
'''
def find_min_value(rotation_array):
    if len(rotation_array) == 0:
        return 0
    left = 0
    right = len(rotation_array) - 1
    mid = 0
    while rotation_array[left] >= rotation_array[right]:
        if right - left == 1:
            mid = right
            break
        mid = left + (right - left) // 2
        if rotation_array[left] == rotation_array[mid] and rotation_array[mid] == rotation_array[right]:
            return minInorder(rotation_array, left, right)
        if rotation_array[mid] >= rotation_array[left]:
            left = mid
        else:
            right = mid
    return rotation_array[mid]


def minInorder(array, left, right):
    result = array[left]
    for i in range(left + 1, right + 1):
        if array[i] < result:
            result = array[i]
    return result


if __name__ == '__main__':
    # 思路: 找出分界处, 然后同时找
    rotation_array = [4, 5, 6, 7, 1, 2, 3, 4]  # 以上为一个旋转数组
    min_value = find_min_value(rotation_array)
    print("最小值:", min_value)

