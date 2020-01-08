"""

@file   : 008-两数相加.py

@author : xiaolu

@time   : 2020-01-07

"""
'''
给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字0之外，这两个数都不会以 0 开头。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        p1 = l1
        p2 = l2
        data1_list = []
        data2_list = []
        while p1 != None:
            data1_list.append(p1.val)
            p1 = p1.next

        while p2 != None:
            data2_list.append(p2.val)
            p2 = p2.next

        data1_list.reverse()
        data2_list.reverse()
        data1 = ''.join([str(i) for i in data1_list])
        data2 = ''.join([str(i) for i in data2_list])
        data1 = int(data1)
        data2 = int(data2)

        result = data1 + data2

        result = str(result)
        result = list(result)
        result.reverse()

        q = ListNode(result[0])
        r = q
        for d in result[1:]:
            temp = ListNode(d)
            r.next = temp
            r = r.next
        return q
