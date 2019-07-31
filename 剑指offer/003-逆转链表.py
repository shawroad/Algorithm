"""

@file   : 003-逆转链表.py

@author : xiaolu

@time   : 2019-07-30

"""
'''
题目:
   输入一个链表，返回一个反序的链表
'''
import copy

class LNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next


def build_Lnode(head, array_data):
    # 建立链表
    r = head
    for d in array_data:
        p = LNode(d, None)
        r.next = p
        r = r.next
    return head


def reverse_Lnode(head):
    # 逆转
    p = head.next
    head.next = None
    while p != None:
        q = copy.deepcopy(p)
        q.next = head.next
        head.next = q
        p = p.next
    return head


def show_Lnode(head):
    # 打印建立好的链表
    p = head.next
    while p != None:
        print(p.data, end=' ')
        p = p.next


if __name__ == '__main__':
    # 这里使用带头节点
    array_data = [3, 4, 5, 6, 7, 8]
    head = LNode(None, None)
    head = build_Lnode(head, array_data)

    # 链表建立好了 我们show一下
    show_Lnode(head)
    print('\n' + "*"*100)

    # 接下来队列表进行逆转
    head = reverse_Lnode(head)
    show_Lnode(head)

