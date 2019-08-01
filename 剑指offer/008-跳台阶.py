"""

@file   : 008-跳台阶.py

@author : xiaolu

@time   : 2019-07-31

"""
'''
题目:
    一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
解法类似fabnici数列  
解析: https://blog.csdn.net/shawroad88/article/details/88383878
'''

def dp_solver(n):
    # 迭代解法
    temp = [0] * n  # 建立一个长度为n的列表

    if n == 1:
        temp[0] = 1
        return temp
    elif n == 2:
        temp[0] = 1
        temp[1] = 2
        return temp
    else:
        temp[0] = 1
        temp[1] = 2
        for i in range(2, n):
            temp[i] = temp[i - 1] + temp[i - 2]  # 这里主要考虑到列表是从编号为0出开始存值
        return temp


def recursion(n):
    # 递归解法
    if n == 1:
        return 1
    if n == 2:
        return 2
    return recursion(n - 1) + recursion(n - 2)


if __name__ == '__main__':
    # 假设当前台阶我们设置为50层，问有多少种方法
    n = 10

    solve = dp_solver(n)
    print("爬各个层的方法:", solve)  # 打印爬各个层的方法
    print("当台阶数为:{}, 总共有{}种爬法!!!".format(n, solve[n - 1]))

    solve2 = recursion(n)
    print("当台阶数为:{}, 总共有{}种爬法!!!".format(n, solve2))
