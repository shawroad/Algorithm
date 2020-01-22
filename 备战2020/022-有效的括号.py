"""

@file   : 022-有效的括号.py

@author : xiaolu

@time   : 2020-01-15

"""
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

示例:
输入: "()[]{}"
输出: true
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == '{' or c == '[':
                stack.append(c)
            if c == ")":
                if len(stack) == 0:
                    return False
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            if c == "}":
                if len(stack) == 0:
                    return False

                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False

            if c == ']':
                if len(stack) == 0:
                    return False

                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "()[]{}"
    s = '[{}]{()}{}['
    sol = Solution()
    result = sol.isValid(s)
    print("括号匹配的结果:", result)
