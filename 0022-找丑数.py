"""

@file  : 0022-找丑数.py

@author: xiaolu

@time  : 2019-07-27

"""
# 丑数判断方法: uglynum=2*2……*2*3*3*……*3*5*5……*5组成


def isUglyNumber(n):
    while n % 2 == 0:
        n /= 2
    while n % 3 == 0:
        n /= 3
    while n % 5 == 0:
        n /= 5
    return n == 1


if __name__ == '__main__':
    result = []
    num = int(input("找哪个数以内的丑数:"))
    i = 1
    while i <= num:
        if isUglyNumber(i):
            result.append(i)
        i += 1
    print("{}以内的丑数为:\n".format(num))
    print(result)
