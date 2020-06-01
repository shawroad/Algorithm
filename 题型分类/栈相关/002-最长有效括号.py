"""

@file  : 002-最长有效括号.py

@author: xiaolu

@time  : 2020-05-27

"""
'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"

示例 2:
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        if len(s) < 2:
            return 0
        dp = [0] * len(s)
        for i, c in enumerate(s):
            if c == ')':
                if stack and stack[-1][0] == "(":
                    _, index = stack.pop()
                    dp[i] = max(dp[i], dp[index - 1] + 2 + dp[i - 1])
            else:
                stack.append(('(', i))
        return max(dp)


if __name__ == '__main__':
    s = ')()())'
    sol = Solution()
    result = sol.longestValidParentheses(s)
    print(result)
