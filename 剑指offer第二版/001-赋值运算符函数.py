"""

@file  : 001-赋值运算符函数.py

@author: xiaolu

@time  : 2019-09-18

"""
# 1. python中的赋值运算只是简单的引用  指定的是同一片内存
a = 1
b = a
print(type(a))
print(type(b))
print(id(a))
print(id(b))
# 输出:
# <class 'int'>
# <class 'int'>
# 94540623440384
# 94540623440384

# 2. 同理
aa = [[2, 3], [4, 5], [6, 7]]
bb = aa
print(type(aa))
print(type(bb))
print(id(aa))
print(id(bb))
# 输出
# <class 'list'>
# <class 'list'>
# 139810098009672
# 139810098009672
