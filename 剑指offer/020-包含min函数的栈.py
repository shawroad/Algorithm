"""

@file   : 020-包含min函数的栈.py

@author : xiaolu

@time   : 2019-08-07

"""
'''
题目描述:
    定义栈的数据结构, 请在该类型中实现一个能够得到栈的最小元素的min函数. 在该栈中，
调用min， push及 pop 的时间复杂度都是O(1)
'''
def push_stack(stack, temp_stack, d):
    '''
    入栈
    :param stack: 真正的栈
    :param temp_stack: 辅助栈  存当前栈中的最小值
    :param d: 需要进栈的元素
    :return: None
    '''
    if len(stack) == 0:
        stack.append(d)
        temp_stack.append(d)
    else:
        if d < temp_stack[-1]:
            temp_stack.append(d)
            stack.append(d)
        else:
            stack.append(d)
            temp_stack.append(temp_stack[-1])


def get_min_value(stack, temp_stack):
    '''
    获取最小值 但是并不从栈中拿出来
    :param stack: 真正的栈
    :param temp_stack: 辅助栈
    :return: 返回此时栈中的最小值
    '''
    if len(stack) != 0:
        min_value = temp_stack[-1]
        return min_value
    else:
        return -1   # 代表没有最小


def pop_stack(stack, temp_stack):
    '''
    出栈
    :param stack: 真正的栈
    :param temp_stack: 辅助栈
    :return: 返回出栈元素
    '''
    # 将元素弹出  这个时候也看看一下辅助栈的最小值有没有边
    if len(stack) == 0:
        return
    else:
        value = stack.pop(-1)
        _ = temp_stack.pop(-1)
        return value


if __name__ == '__main__':
    # stack为原始栈    temp_stack 为辅助栈
    stack = []
    temp_stack = []

    # 依次将data中的数据入栈
    data = [5, 6, 2, 4, 8, 1, 3]

    # 1. 将元素依次压入栈
    for d in data:
        push_stack(stack, temp_stack, d)
    print(stack)
    print(temp_stack)

    # 2. 获取当前栈中元素的最小值
    min_value = get_min_value(stack, temp_stack)
    print("当前栈中最小值为:", min_value)

    # 3. 出栈  出两次栈 然后再看当前栈的最小值
    top_value = pop_stack(stack, temp_stack)
    min_value = get_min_value(stack, temp_stack)
    top_value_ = pop_stack(stack, temp_stack)
    min_value_ = get_min_value(stack, temp_stack)
    print("第一次出栈:", top_value)
    print("此时最小值:", min_value)
    print("第二次出栈:", top_value_)
    print("此时最小值:", min_value_)
