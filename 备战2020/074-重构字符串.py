"""

@file   : 074-重构字符串.py

@author : xiaolu

@time   : 2020-03-20

"""
'''
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
若可行，输出任意可行的结果。若不可行，返回空字符串。

示例 1:
输入: S = "aab"
输出: "aba"

示例 2:
输入: S = "aaab"
输出: ""
'''
import collections

'''
将字符按字符数排序。
如果最多的字符占了半数以上，返回空，
如果总字符数是偶数，将排序后的字符分为前后两半，交叉得出结果
如果为奇数，将前后两半交叉，再加上最中间的字符。
'''
class Solution:
    def reorganizeString(self, S: str) -> str:
        s = sorted(S)
        count = collections.Counter(S)
        s.sort(key=count.get)
        n = len(s) // 2
        if s[n - 1] == s[-1]:
            return ''

        a, b = s[:n], s[n:]
        for i in range(len(b)):
            s[i * 2] = b[i]
        for i in range(len(a)):
            s[i * 2 + 1] = a[i]
        return ''.join(s)


if __name__ == '__main__':
    S = 'aab'
    sol = Solution()
    result = sol.reorganizeString(S)
    print(result)

