"""

@file   : 016-字符串转换整数.py

@author : xiaolu

@time   : 2020-01-14

"""
'''
示例:
输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。

示例:
输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
     
示例:
输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
     因此返回 INT_MIN (−231) 。
'''
class Solution:
    def myAtoi(self, str: str) -> int:
        i = 0
        sign = 1
        result = []

        count_1 = 0   # 统计加
        count_2 = 0   # 统计减
        have_num = False

        while i < len(str):
            if str[i] == '-' and count_1 == 0 and count_2 == 0 and have_num == False:
                sign = -1
                i += 1
                count_1 += 1
            elif str[i] == '+' and count_1 == 0 and count_2 == 0 and have_num == False:
                i += 1
                count_2 += 1

            elif '0' <= str[i] <= '9':
                result.append(str[i])
                i += 1
                have_num = True
            elif str[i] == ' ' and have_num == False and count_1 == 0 and count_2 == 0:
                i += 1
            else:
                break

        if len(result) == 0:
            return 0
        result = int(''.join(result))
        result *= sign

        if result < -2147483648:
            return -2147483648
        if result > 2147483647:
            return 2147483647
        return result


if __name__ == '__main__':
    sol = Solution()
    # num = '  -4193 with words'
    # num = "-91283472332"
    # num = 'fanaodk423'
    num = "-+1"
    result = sol.myAtoi(num)
    print(result)
