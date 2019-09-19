"""

@file  : 003-数组中重复的数字.py

@author: xiaolu

@time  : 2019-09-18

"""
'''
题目:
　　在一个长度为n的数组里的所有数字都在0~n-1的范围内.数组中某些数字是重复的,但不知到有几个数字重复了,
也不知道每个数字重复了几次.请找出数组中任意的一个重复的数字. 例如:如果输入长度为7的数组{2, 3, 1, 0, 
2, 5, 3}, 那么对应的输出是重复的数字2或者3
'''
'''
解题思路:
  　从第0个位置开始, 每个位置放其对应的数字
'''
def find_chongfu(data):
    '''
    找重复的某个值
    :param data:
    :return:
    '''
    if len(data) < 0:
        # 长度有问题
        return False

    for i in data:
        # 数据没有在0~len(data)的范围内
        if i < 0 or i > len(data):
            return False

    for i in range(len(data)):
        while data[i] != i:
            # 如果当前i位置的值(data[i])不等于i
            if data[i] == data[data[i]]:
                return data[i]

            temp = data[i]
            data[i] = data[temp]
            data[temp] = temp
            print(data)

    return False


if __name__ == '__main__':
    data = [1, 3, 2, 0, 5, 4, 7, 6, 7, 9, 8]
    result = find_chongfu(data)
    print("最终的结果:", result)

