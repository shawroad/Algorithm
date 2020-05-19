"""

@file  : 002-最长公共前缀.py

@author: xiaolu

@time  : 2020-05-18

"""
'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        if len(strs) == 1:
            return strs[0]
        if len(strs) == 0:
            return ''

        # 找出最短的串
        min_len = float('inf')
        min_str = ''
        for i in strs:
            if len(i) < min_len:
                min_len = len(i)
                min_str = i

        strs.remove(min_str)

        for i, c in enumerate(list(min_str)):
            sign = True
            for s in strs:
                if s[i] == c:
                    pass
                else:
                    sign = False

            if sign == True:
                result.append(c)
            else:
                break

        result = ''.join(result)
        return result


if __name__ == '__main__':
    # s = ["flower", "flow", "flight"]
    # s = ["dog", "racecar", "car"]
    s = [""]
    sol = Solution()
    result = sol.longestCommonPrefix(s)
    print(result)


