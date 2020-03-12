"""

@file   : 065-字符串的最大公因子.py

@author : xiaolu

@time   : 2020-03-12

"""
'''
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。

返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

示例 1：
输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"

示例 2：
输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1), len(str2)), 0, -1):
            if (len(str1) % i) == 0 and (len(str2) % i) == 0:
                if str1[: i] * (len(str1) // i) == str1 and str1[: i] * (len(str2) // i) == str2:
                    return str1[: i]
        return ''


if __name__ == '__main__':
    str1 = "ABCABC"
    str2 = "ABC"
    sol = Solution()
    result = sol.gcdOfStrings(str1, str2)
    print(result)
