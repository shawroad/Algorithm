"""

@file   : 0024-虐心排序算法.py

@author : xiaolu

@time   : 2019-08-19

"""
'''
题目: 第一步: 找出最小值和最大值 然后将其放在data[0] 和data[n-1] 处
      第二步: 找出次小值和次大值 然后将其放在data[1] 和data[n-2] 处
      第三步: 找出次次小值和次次大值 然后将其放在data[2] 和 data[n-3]依次类推 直到最后
'''
def greive_sort(data):
    '''
    对data中的数据进行排序
    :param data: 传进来的数据
    :return: 返回排好的数据
    '''

    L = len(data)
    i = 0
    while i < (L-i):
        min_, max_ = i, i
        for j in range(i+1, L-i):
            if data[j] < data[min_]:
                min_ = j
            if data[j] > data[max_]:
                max_ = j

        if min_ != i:
            temp = data[min_]
            data[min_] = data[i]
            data[i] = temp

        if max_ != L-i-1:
            # 之所以要判断 是因为试过上面进行最小值移动的时候,如果我们的最大值在i位置 岂不是就把我们的最大值移动到min_位置处了
            if max_ == i:
                temp = data[L-i-1]
                data[L-i-1] = data[min_]
                data[min_] = temp
            else:
                temp = data[L-i-1]
                data[L-i-1] = data[max_]
                data[max_] = temp
        i += 1
    return data


if __name__ == '__main__':
    data = [3, 12, 42, 4, 129, 32, 12, 53, 23, 123, 32, 45, 1, 6]
    sort_data = greive_sort(data)
    print(sort_data)

