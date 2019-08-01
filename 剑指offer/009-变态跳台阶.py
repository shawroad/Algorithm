"""

@file   : 009-变态跳台阶.py

@author : xiaolu

@time   : 2019-07-31

"""
'''
题目:
    一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。  
解析: https://cuijiahua.com/blog/2017/11/basis_9.html

可以延续上一题的思路，逆向思维来考虑这个问题。要想跳到第n级台阶，
就可以从第n-1级、第n-2级、***、第1级 跳到第n级，再加上直接从地面到第n级的一种情况。

'''
# 迭代解法
def method_num(n):
    result = [1, 2]  # 第一阶: 1种   第二阶: 2种
    i = 2   # 从第三阶开始求  这里下标是从0开始的
    while i < n:
        total = 0
        for j in range(0, i):
            total += result[j]
        total += 1   # 这里加的是一步调到指定位置
        result.append(total)
        i += 1
    return result


# # 递归解法
# def digui_method_num(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#
#     sum_ = 0
#     for i in range(n-1):
#         sum_ += digui_method_num(i)
#
#     return sum_


if __name__ == "__main__":
    n = 3
    result = method_num(n)
    print("迭代的解法 跳到10层总共的跳法:", result)

    # digui_num = digui_method_num(n)
    # print("递归的解法 跳到10层总共的跳法:", digui_num)


