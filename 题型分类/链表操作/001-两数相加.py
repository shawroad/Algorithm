"""

@file  : 001-两数相加.py

@author: xiaolu

@time  : 2020-05-07

"""
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1.从链表上把这些数摘下来
        num1 = []
        r = l1
        while r is not None:
            num1.append(r.val)
            r = r.next

        num2 = []
        r = l2
        while r is not None:
            num2.append(r.val)
            r = r.next

        num1.reverse()
        num2.reverse()
        num1 = ''.join([str(i) for i in num1])
        num2 = ''.join([str(i) for i in num2])
        result = int(num1) + int(num2)
        result = list(str(result))
        result.reverse()
        result = [int(i) for i in result]
        l = ListNode(result[0])
        r = l
        for i in result[1:]:
            r.next = ListNode(i)
            r = r.next
        return l



