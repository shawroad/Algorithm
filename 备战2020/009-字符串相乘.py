"""

@file   : 009-字符串相乘.py

@author : xiaolu

@time   : 2020-01-07

"""
'''
给定两个以字符串形式表示的非负整数 num1 和 num2，
返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(''.join([str(i) for i in list(num1)])) * int(''.join([str(j) for j in list(num2)])))
