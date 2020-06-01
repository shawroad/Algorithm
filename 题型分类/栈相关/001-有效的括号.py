"""

@file  : 001-有效的括号.py

@author: xiaolu

@time  : 2020-05-27

"""
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
'''


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if s[0] == ')' or s[0] == ']' or s[0] == '}' or len(s) == 1:
            return False
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)

            if c == ')':
                if len(stack) >= 1 and stack[-1] == '(':
                    stack.pop(-1)
                else:
                    return False

            if c == ']':
                if len(stack) >= 1 and stack[-1] == '[':
                    stack.pop(-1)
                else:
                    return False

            if c == '}':
                if len(stack) >= 1 and stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    # s = '{[()]}'
    s = "[])"
    sol = Solution()
    result = sol.isValid(s)
    print(result)
