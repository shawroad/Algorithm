"""

@file   : 082-整数转罗马数字.py

@author : xiaolu

@time   : 2020-03-24

"""
'''
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。
       12 写做 XII ，即为 X + II 。 
       27 写做  XXVII, 即为 XX + V + II 。
'''
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         num2roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
#         str_num = str(num)
#         num_list = list(str_num)
#         num_list.reverse()
#         result = ''
#         for i, n in enumerate(num_list):
#             n = int(n)
#             if i == 0 and n < 5:
#                 result += num2roman.get(1) * n
#             elif i == 0 and n > 5:
#                 result += (n - 5) * num2roman.get(1)
#                 result += int((n / 5)) * num2roman.get(5)
#
#             if i == 1 and n < 5:
#                 result += n * num2roman.get(10)
#             elif i == 1 and n > 5:
#                 result += (n - 5) * num2roman.get(10)
#                 result += int((n / 5)) * num2roman.get(50)
#
#             if i == 2 and n < 5:
#                 result += n * num2roman.get(100)
#             elif i == 2 and n > 5:
#                 result += (n - 5) * num2roman.get(100)
#                 result += int((n / 5)) * num2roman.get(500)
#
#             if i >= 3:
#                 result += n * num2roman.get(1000)
#
#         return result


class Solution:
    def intToRoman(self, num: int) -> str:
        c = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
             ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
             ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
             ["", "M", "MM", "MMM"]]
        result = ''
        result += c[3][num // 1000]
        result += c[2][num // 100 % 10]
        result += c[1][num // 10 % 10]
        result += c[0][num % 10]

        return result


if __name__ == '__main__':
    # num = 2
    num = 12
    sol = Solution()
    result = sol.intToRoman(num)
    print(result)
