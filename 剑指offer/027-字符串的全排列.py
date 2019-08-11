"""

@file   : 027-字符串的全排列.py

@author : xiaolu

@time   : 2019-08-11

"""
'''
题目:
    输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc，
则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''
from copy import deepcopy


def isduplicate(li, n, t):
    """
    从li的位置n到位置t-1，有没有和li[t]相等的数字
    """
    while n < t:
        if li[n] == li[t]:
            return True
        n += 1
    return False


def swap(li, i, j):
    if i == j:
        return
    temp = li[j]
    li[j] = li[i]
    li[i] = temp


def permutation(li, size, n, result):
    '''
    n -> size的全排列
    :param li: 字符串数组
    :param size: 字符串长度
    :param n: 当前要占的位置
    :param result: 保留的结果
    :return:
    '''
    if n == size - 1:
        result.append(deepcopy(li))
        return
    for i in list(range(n, size)):
        if isduplicate(li, n, i):
            continue
        swap(li, i, n)
        permutation(li, size, n + 1, result)
        swap(li, i, n)


if __name__ == '__main__':
    # 输入的数据
    string = 'abc'
    li = list(string)
    size = len(li)
    n = 0
    result = []
    permutation(li, size, n, result)

    for i in result:
        print(i)
