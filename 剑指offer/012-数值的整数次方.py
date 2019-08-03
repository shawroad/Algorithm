"""

@file   : 012-数值的整数次方.py

@author : xiaolu

@time   : 2019-08-02

"""
'''
题目:
    给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
思路: https://cuijiahua.com/blog/2017/11/basis_12.html
'''
def resolve(base, exponent):
    '''
    求base的exponent次方
    :param base: 底数
    :param exponent: 次方数
    :return: 返回计算的结果
    '''
    if base == 0:
        return 0   # 0的任何次方都等于零

    result = 1
    if exponent % 2 == 0:
        for i in range(exponent // 2):
            result *= base
        return result * result

    if exponent % 2 != 0:
        for i in range(exponent // 2):
            result *= base
        return result * result * base


if __name__ == '__main__':
    base = float(input("输入一个float型的数据:"))
    exponent = int(input("输入一个int性的数据:"))
    result = resolve(base, exponent)
    print("{}的{}次方是{}".format(base, exponent, result))


