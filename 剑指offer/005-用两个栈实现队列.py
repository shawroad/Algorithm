"""

@file   : 005-用两个栈实现队列.py

@author : xiaolu

@time   : 2019-07-30

"""
def en_queue(stack1, stack2, data):
    # 进队  直接让其进入的栈1
    for d in data:
        stack1.append(d)
    return stack1, stack2


def de_queue(stack1, stack2):
    # 出队  从栈1中出来 然后让其进入栈2 最后再输出
    print("出队序列:")
    while len(stack1) != 0:
        stack2.append(stack1.pop(-1))

    # 接着从stack2中出来
    while len(stack2) != 0:
        print(stack2.pop(-1), end=' ')


if __name__ == '__main__':
    stack1 = []   # 进栈 list.append()  出栈 list.pop(0)
    stack2 = []

    # 进队
    data = [1, 2, 3, 4, 5, 6, 7, 8]   # 将这些元素进队
    stack1, stack2 = en_queue(stack1, stack2, data)

    # 出队
    de_queue(stack1, stack2)

