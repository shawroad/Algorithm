"""

@file   : 003-链栈和链队的实现.py

@author : xiaolu

@time   : 2019-06-25

"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def push_stack(head, data):
    # 说明一下：链栈的进栈使用的是头插法，出栈使用的是头删法
    # 1.data数据想进栈 第一步是构造节点
    temp = Node(data, None)
    temp.next = head.next
    head.next = temp
    return head


def pop_stack(head):
    # 出栈
    data = head.next.data
    head = head.next
    return head, data


def input_seq(head, data):
    # 说明一下：链队是尾插法+头删法
    # 进队
    temp = Node(data, None)
    if head.next == None:
        head.next = temp
    else:
        r = head.next
        while r.next != None:
            r = r.next
        r.next = temp

    return head


def output_seq(head):
    # 出队
    data = head.next.data
    head = head.next
    return head, data


if __name__ == '__main__':
    # 建立好链栈和链队，讲一下元素插入到其中
    array = [3, 9, 23, 94, 23, 12, 75, 80, 24, 64]
    head_stack = Node(None, None)     # 这个是链栈的头节点

    # 将array中的元素入栈
    for i in array:
        head = push_stack(head_stack, i)

    # 将下来看一下链表
    p = head_stack.next
    while p != None:
        print(p.data, end=' ')
        p = p.next
    print('\n')

    # 出栈  相当于从头删除
    head_stack, data1 = pop_stack(head_stack)
    print("第一个出栈的元素:", data1)
    head_stack, data2 = pop_stack(head_stack)
    print("第二个出栈的元素:", data2)
    print("*"*100)

    # 接下来创建队列 尾插法+头删法
    # 进队
    head_seq = Node(None, None)   # 链队的头
    for i in array:
        head_seq = input_seq(head_seq, i)
    # 将下来看一下链表
    p = head_seq.next
    while p != None:
        print(p.data, end=' ')
        p = p.next
    print('\n')
    # 出队
    head_seq, data1 = output_seq(head_seq)
    print("第一个出队的元素:", data1)
    head_seq, data2 = output_seq(head_seq)
    print("第二个出队的元素:", data2)

