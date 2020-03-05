"""

@file   : 060-逆波兰表达式求值.py

@author : xiaolu

@time   : 2020-03-05

"""
'''
根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
示例 1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9
示例 2：

输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6
'''
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        while len(tokens) != 0:
            temp = tokens.pop(0)
            if temp != '+' and temp != '-' and temp != '/' and temp != '*':
                stack.append(temp)

            else:
                if temp == '+':
                    b = int(stack.pop())
                    a = int(stack.pop())
                    t = a + b
                    stack.append(t)

                elif temp == '-':
                    b = int(stack.pop())
                    a = int(stack.pop())
                    t = a - b
                    stack.append(t)

                elif temp == '*':
                    b = int(stack.pop())
                    a = int(stack.pop())
                    t = a * b
                    stack.append(t)

                else:
                    b = int(stack.pop())
                    a = int(stack.pop())
                    t = a / b
                    stack.append(t)
        return int(stack[0])


if __name__ == '__main__':
    # tokens = ["2", "1", "+", "3", "*"]
    tokens = ["4", "13", "5", "/", "+"]
    sol = Solution()
    result = sol.evalRPN(tokens)
    print(result)
