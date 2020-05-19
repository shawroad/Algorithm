"""

@file  : 001-Z字形变换.py

@author: xiaolu

@time  : 2020-05-18

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

示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

示例 2:
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:
L     D     R
E   O E   I I
E C   I H   N
T     S     G
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = [[] for i in range(numRows)]
        sign = True  # True标志向下移动, False标志向上移动
        col = 0
        for i in s:
            if sign:
                result[col].append(i)
                if col+1 == len(result):
                    col -= 1
                    sign = False
                else:
                    col += 1
            else:
                result[col].append(i)
                if col-1 == -1:
                    col += 1
                    sign = True
                else:
                    col -= 1
        return ''.join([''.join(r) for r in result])


if __name__ == "__main__":
    s = "LEETCODEISHIRING"
    numRows = 4
    sol = Solution()
    result = sol.convert(s, numRows)
    print(result)


