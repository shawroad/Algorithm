"""

@file   : 002-循环链表和双向链表.py

@author : xiaolu

@time   : 2019-06-24

"""
# 循环链表的节点定义
class RNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# 双向列表的节点定义
class BNode:
    def __init__(self, data, prior=None, next=None):
        self.data = data
        self.prior = prior
        self.next = next


def build_r_l(array):
    # 建立循环链表
    head = RNode(None, None)
    r = head
    for i in array:
        temp = RNode(i, None)
        r.next = temp
        r = temp
    r.next = head
    return head


def build_b_l(array):
    # 建立双向列表
    head = BNode(None, None, None)
    r = head
    for i in array:
        temp = BNode(i, None, None)
        r.next = temp
        temp.prior = r
        r = temp
    return head


if __name__ == '__main__':
    array = [3, 9, 23, 94, 23, 12, 75, 80, 24, 64]

    # 1.用上面的数据建立循环链表
    head1 = build_r_l(array)

    # 2.用上面的数据建立双向链表
    head2 = build_b_l(array)

    # 3.分别遍历两种链表
    # 3.1 遍历循环列表  让访问到第二次24的时候停止
    p = head1.next
    i = 0
    while p != None:
        print(p.data, end=' ')
        if p.data == 24:
            i += 1
            if i == 2:
                break
        p = p.next
    print("\n" + "*"*100)

    # 3.2 先找到双向的尾  然后从后往前访问
    p = head2.next
    while p.next != None:
        p = p.next
    q = p.prior
    while p.prior != None:
        print(p.data, end=' ')
        p = p.prior
