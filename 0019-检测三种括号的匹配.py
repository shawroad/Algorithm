"""

@file   : 0019-检测三种括号的匹配.py

@author : xiaolu

@time   : 2019-07-01

"""
def is_fit(eq):
    stack = []
    for i in list(eq):
        if i not in ['{', '[', '(', ')', ']', '}']:
            pass
        else:
            print(stack)
            if i == '{':
                stack.append('{')
            elif i == '[':
                stack.append('[')
            elif i == '(':
                stack.append('(')
            elif i == ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop()   # 让栈中的最上面元素弹出来
            elif i == ']' and len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            elif i == '}' and len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            else:
                return False
    print(stack)

    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    # 下面是一个正常的式子，检测是否匹配正常
    eq = '12-{28/[(2+5)*12]}'
    # eq = '{[()][]()[]{{{[()]()}}[]}}}'
    # eq = '{[()]'
    sign = is_fit(eq)
    print("这个式子{}括号匹配是否:{}".format(eq, sign))

