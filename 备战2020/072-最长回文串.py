"""

@file   : 072-最长回文串.py

@author : xiaolu

@time   : 2020-03-19

"""
'''
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
注意:
假设字符串的长度不会超过 1010。

示例 1:
输入:
"abccccdd"
输出:
7
解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        # 相当于统计两两相等的字母有多少组
        s_list = list(s)
        pair = 0

        while len(s_list) != 0:
            v = s_list.pop(0)
            for w in s_list:
                if w == v:
                    s_list.remove(w)
                    pair += 1
                    break
        if 2 * pair == len(s):
            return 2 * pair
        else:
            return 2 * pair + 1


if __name__ == '__main__':
    # s = 'abccccdd'
    s = 'bb'
    sol = Solution()
    result = sol.longestPalindrome(s)
    print(result)

