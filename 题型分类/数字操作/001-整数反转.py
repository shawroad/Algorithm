"""

@file  : 002-整数反转.py

@author: xiaolu

@time  : 2020-05-20

"""
'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

 示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21
'''
class Solution:
    def reverse(self, x: int) -> int:

        sign = 1
        if x < 0:
            sign = -1
        s = str(x).replace('-', '')
        s = list(s)
        s.reverse()
        s = ''.join(s)
        s = s.lstrip('0')
        if len(s) == 0:
            return 0
        else:
            res = int(s) * sign
            return 0 if res < -1 * 2 ** 31 or res > 2**31-1 else res


if __name__ == '__main__':
    x = 123
    sol = Solution()
    result = sol.reverse(x)
    print(result)
