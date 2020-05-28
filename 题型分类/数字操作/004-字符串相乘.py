"""

@file  : 004-字符串相乘.py

@author: xiaolu

@time  : 2020-05-20

"""
'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))



if __name__ == '__main__':
    num1 = "123"
    num2 = "456"

    sol = Solution()
    result = sol.multiply(num1, num2)
    print(result)




