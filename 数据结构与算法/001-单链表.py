"""

@file   : 001-单链表.py

@author : xiaolu

@time   : 2019-06-24

"""
# 定义节点
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


def build_lianbiao1(array):
    # 1.先给列表设个头
    head = Node(None, None)
    rear = head   # 在设个尾 因为打算用尾插法
    # 2.每次访问一个数据，构造一个节点，然后进行尾插
    for i in array:
        temp = Node(i, None)
        rear.next = temp
        rear = temp
    return head


def build_lianbiao2(array):
    # 1. 建立头节点
    head = Node(None, Node)
    # 第一个节点需要特殊考虑一下
    head.next = Node(array[0], None)

    # 2. 进行头插法
    for i in array[1:]:
        temp = Node(i, None)
        temp.next = head.next
        head.next = temp
    return head


if __name__ == "__main__":
    # 下面是一个列表  我们用底下列表中的数字构建一个链表
    array = [3, 9, 23, 94, 23, 12, 75, 80, 24, 64]

    # 1.尾插发建立链表
    head1 = build_lianbiao1(array)
    # 接下来 我们遍历一个上面建立的链表
    p = head1.next
    while p != None:
        print(p.data, end=' ')
        p = p.next
    print("\n" + "*"*100)

    # 2.头插法建立链表
    head2 = build_lianbiao2(array)
    p = head2.next
    while p != None:
        print(p.data, end=' ')
        p = p.next
    print("\n" + "*"*100)

    # 3.尾插法建立的列表  在94后面插入5
    temp = Node(5, None)   # 构造好5这个节点
    p = head1.next
    while p != None:
        if p.data == 94:
            temp.next = p.next
            p.next = temp
        p = p.next
    # 重新遍历一下head1链表
    p = head1.next
    while p != None:
        print(p.data, end=' ')
        p = p.next
    print("\n" + "*"*100)


