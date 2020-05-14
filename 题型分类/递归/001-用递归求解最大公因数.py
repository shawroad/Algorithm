"""

@file  : 001-用递归求解最大公因数.py

@author: xiaolu

@time  : 2020-05-11

"""

def f(a, b):
    if b == 0:
        print(a)
    else:
        f(b, a % b)


def jiecheng(n):
    if n == 1:
        return 1
    else:
        return jiecheng(n-1) * n

if __name__ == '__main__':
    # 求最大公因数
    num1 = 10
    num2 = 480
    f(num1, num2)

    # 求阶乘
    result = jiecheng(num1)
    print(result)




