"""

@file  : 003-一堆数中将负数和正数分离.py

@author: xiaolu

@time  : 2019-07-29

"""
def sep_neg_pos(data):
    # 分离正负数　以零作为基准
    data.insert(0, 0)
    i, j = 0, len(data) - 1
    temp = data[0]
    while i != j:
        while i < j and data[j] > temp:
            j -= 1
        if i < j:
            data[i] = data[j]
            i += 1
        while i < j and data[i] < temp:
            i += 1
        if i < j:
            data[j] = data[i]
            j -= 1
    return data


if __name__ == '__main__':
    # 将所有负数放在正数之前
    data = [29, 23, -2, 3, -12, 2, -3, -4, 23, -14, 30]
    print("原始序列:", data)
    result = sep_neg_pos(data)
    print("分离后的结果:", result)
