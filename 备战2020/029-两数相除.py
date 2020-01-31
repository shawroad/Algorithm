"""

@file   : 029-两数相除.py

@author : xiaolu

@time   : 2020-01-16

"""
'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:
输入: dividend = 10, divisor = 3
输出: 3

示例 2:
输入: dividend = 7, divisor = -3
输出: -2
'''

# 解法一   这种方法会超时
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if divisor < 0:
            sign *= -1
            divisor *= -1
        if dividend < 0:
            sign *= -1
            dividend *= -1

        if dividend < divisor:
            return 0

        i = 1
        temp = dividend - divisor
        while temp > divisor:
            temp = temp - divisor
            i += 1

        i *= sign
        return i


# 解法二
class Solution2:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = False
        if dividend > 0 and divisor > 0:
            pass

        elif dividend > 0 and divisor < 0:
            divisor = -divisor
            flag = True
        elif dividend < 0 and divisor > 0:
            dividend = -dividend
            flag = True
        else:
            dividend = -dividend
            divisor = -divisor

        if dividend == 0 or dividend < divisor:
            return 0

        if dividend == divisor:
            if flag:
                return -1
            else:
                return 1

        i = 1
        temp = divisor
        # divisor 首先加一倍的它,接着加两倍的它... 快速逼近dividend
        while divisor < dividend:
            last_divisor = divisor
            divisor += divisor
            last_i = i
            i += i

        divisor -= last_divisor
        i -= last_i

        # 不够多少倍的差值  然后在进行运算
        i += self.divide(dividend - divisor, temp)

        if flag:
            return -2147483647 if -i >= 2147483648 else -i
        else:
            return 2147483647 if i >= 2147483648 else i


if __name__ == '__main__':
    # dividend = -10
    # divisor = 3

    # dividend = -1
    # divisor = -1

    # 下面这种情况 严重超时
    dividend = 2147483647
    divisor = 2

    sol = Solution2()
    result = sol.divide(dividend, divisor)
    print("最终的结果为:", result)
