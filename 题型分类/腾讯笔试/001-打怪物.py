"""

@file  : 001-打怪物.py

@author: xiaolu

@time  : 2020-05-15

"""
'''
有一个人需要去打怪物，每打一个怪物需要耗费xi的血量，但是会获得yi的金币，
然后开局可以使用金币去购买血量，一个金币可以购买q点血量，用不完的血量所有怪物结束之后不会保留，
每一个怪物都可以选择打或者不打，问最后结束时，可以获得最大的收益是多少。

输入描述
第一行输入n q，分别表示总共有n个怪物，和一个金币可以购买q点血量
接下来的n行，分别是xi yi分别是打一个怪物的消耗和金币收益

输入
3 2
1 1
1 10
3 1

输出
10
'''
# 只要收益大于花费, 我们就打
from math import ceil

# n个怪物, q点血量
n, q = [int(i) for i in input().split(' ')]

res = 0
b = 0
for i in range(n):
    cost, gain = [int(i) for i in input().split(' ')]
    if gain * q > cost:
        res += gain   # 统计的金币收益
        b += cost    # 消耗的血量

print(res - ceil(b/q))

