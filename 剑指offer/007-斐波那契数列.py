"""

@file   : 007-斐波那契数列.py

@author : xiaolu

@time   : 2019-07-31

"""
'''
题目:
   大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。（n<=39）
                  0         n = 0
    f(x) =        1         n = 1
           f(n-1) + f(n-2)  n > 1
'''
# 迭代解法
def fabnaci(n):
    a, b = 1, 1
    i = 3
    c = 0  # 保存最后的结果
    while i <= n:
        c = a + b
        a = b
        b = c
        i += 1

    return c


# 递归求解
def digui_fab(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return digui_fab(n - 1) + digui_fab(n - 2)


if __name__ == '__main__':
    n = 36
    result = fabnaci(n)
    print("迭代的求解结果:", result)

    # 前36个
    digui_result = digui_fab(n)
    print("递归的求解结果:", digui_result)
