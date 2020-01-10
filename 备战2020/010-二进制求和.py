"""

@file   : 010-二进制求和.py

@author : xiaolu

@time   : 2020-01-07

"""
'''
给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。

输入: a = "1010", b = "1011"
输出: "10101"
'''
class Solution:
    def addBinary(self, a, b):
        if len(a) > len(b):
            end = '0' * (len(a) - len(b))
            end += b
            b = end

        else:
            end = '0' * (len(b) - len(a))
            end += a
            a = end

        a = '0' + a
        b = '0' + b

        i = len(a) - 1
        a = list(a)
        b = list(b)
        print(a)
        print(b)

        c = []
        jin = None
        while i >= 0:
            if jin != None:
                temp = int(a[i]) + int(b[i]) + jin
            else:
                temp = int(a[i]) + int(b[i])

            if temp < 2:
                c.insert(0, temp)
                jin = None
            else:
                jin = 1
                c.insert(0, temp % 2)

            i -= 1

        if c[0] == 0:
            result = ''.join([str(i) for i in c[1:]])
        else:
            result = ''.join([str(i) for i in c])

        return result


if __name__ == '__main__':
    # a = '1010'
    # b = '10110'
    # a = "1010"
    # b = "1011"
    a = "1111"
    b = "1111"
    sol = Solution()
    result = sol.addBinary(a, b)
    print(result)

