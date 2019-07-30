"""

@file   : 001-二维数组中的查找.py

@author : xiaolu

@time   : 2019-07-30

"""
'''
题目:
   在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

解析地址: https://cuijiahua.com/blog/2017/11/basis_1.html
'''
def find_data(data, finded_data):
    i, j = 0, len(data[0])-1
    while i < len(data)-1 and j > 0:
        if finded_data == data[i][j]:
            return i, j
        elif finded_data < data[i][j]:
            j -= 1
        else:
            i += 1
    return -1, -1


if __name__ == '__main__':
    data = [[1, 3, 4, 5, 7, 12],
            [2, 5, 6, 9, 8, 13],
            [4, 7, 9, 10, 11, 14],
            [5, 9, 10, 13, 15, 19]
            ]

    finded_data = 7
    result = find_data(data, finded_data)
    print("7所对应的下标:", result)

