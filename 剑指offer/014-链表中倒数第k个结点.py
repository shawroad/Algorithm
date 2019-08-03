"""

@file   : 014-链表中倒数第k个结点.py

@author : xiaolu

@time   : 2019-08-02

"""
'''
题目:
    输入一个链表，输出该链表中倒数第k个结点
解法: 定义p, q两个指针, 先让q走k步 然后再让p跟q一同往后走,等q走向终点的时候,p指的就是所谓的第k个节点
'''
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


def find_k_value(head, k):
    p = head.next
    q = head.next

    i = 0
    while i < k:
        q = q.next
        i += 1

    while q != None:
        p = p.next
        q = q.next
    return p.data


if __name__ == '__main__':
    data = [3, 1, 42, 23, 9, 12, 53, 25, 12, 94, 20]

    # 先构建列表
    head = build_list(data)

    # 遍历一下  看链表建立成功没
    print("遍历链表:", end=' ')
    r = head.next
    while r is not None:
        print(r.data, end=' ')
        r = r.next

    print('\n' + "*"*100)
    # 找倒数第k个节点
    k = 10
    result = find_k_value(head, k)
    print("倒数第k个节点:", result)






