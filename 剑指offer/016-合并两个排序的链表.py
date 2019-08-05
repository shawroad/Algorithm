"""

@file   : 016-合并两个排序的链表.py

@author : xiaolu

@time   : 2019-08-02

"""
class LNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def build_list(data):
    head = LNode(None, None)  # 定义的头结点
    r = head
    for i in data:
        temp_node = LNode(i, None)
        r.next = temp_node
        r = r.next
    return head


def merge_list(head1, head2):
    p = head1.next
    q = head2.next
    head = head1
    r = head
    while p != None and q != None:
        if p.data < q.data:
            r.next = p
            p = p.next
            r = r.next
        else:
            r.next = q
            q = q.next
            r = r.next
    r.next = None
    if p != None:
        r.next = p
    if q != None:
        r.next = q
    return head


if __name__ == '__main__':
    data1 = [2, 3, 5, 8, 10, 12, 23]
    data2 = [5, 23, 34, 45, 55]

    head1 = build_list(data1)
    head2 = build_list(data2)

    head = merge_list(head1, head2)

    print("遍历链表:", end=' ')
    r = head.next
    while r is not None:
        print(r.data, end=' ')
        r = r.next
