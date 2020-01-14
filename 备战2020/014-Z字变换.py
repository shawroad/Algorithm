"""

@file   : 014-Z字变换.py

@author : xiaolu

@time   : 2020-01-13

"""
'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ['' for i in range(numRows)]
        if numRows < 2:
            return s

        i = 0
        sign = -1
        for n in s:
            result[i] += n
            if i == (numRows - 1) or i == 0:
                sign *= -1
            i += sign
        result = ''.join(result)
        return result


if __name__ == '__main__':
    s = 'LEETCODEISHIRING'
    numRows = 3
    sol = Solution()
    result = sol.convert(s, numRows)
    print("最终的结果为:", result)

