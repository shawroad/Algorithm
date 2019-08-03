"""

@file   : 013-调整数组顺序使奇数位于偶数前面.py

@author : xiaolu

@time   : 2019-08-02

"""
'''
题目:
    给定一个数组，其中元素包含偶数和奇数。 我们的目的是将奇数放在偶数之前
'''
def solve_fun(data):
    i, j = 0, len(data) - 1

    while i < j:
        while i < j and data[j] % 2 == 0:  # 从后往前 碰到奇数 j往前移一步
            j -= 1
        while i < j and data[i] % 2 != 0:  # 从前往后 碰到偶数 i往前移一步
            i += 1
        # 此时的 i, j 分别指向的是偶数和奇数  所以我们交换位置
        temp = data[j]
        data[j] = data[i]
        data[i] = temp
        i += 1
        j -= 1
    return data


if __name__ == '__main__':
    data = [4, 23, 12, 424, 23, 94, 3, 41, 49]
    result = solve_fun(data)
    print(result)



