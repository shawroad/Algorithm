"""

@file  : 002-删除链表的倒数第N个节点.py

@author: xiaolu

@time  : 2020-05-08

"""
'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 如果删除的是第一个节点　需要特殊处理
        length = 0
        r = head
        while r is not None:
            r = r.next
            length += 1
        if n == length:
            return head.next

        # 其余情况
        farward = head
        for i in range(n):
            farward = farward.next
        pre = head
        while farward.next is not None:
            farward = farward.next
            pre = pre.next

        pre.next = pre.next.next
        return head
