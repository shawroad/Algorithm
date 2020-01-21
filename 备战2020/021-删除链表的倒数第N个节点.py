"""

@file   : 021-删除链表的倒数第N个节点.py

@author : xiaolu

@time   : 2020-01-15

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        # 这一部分是为了克服删除第一个节点
        t = head
        length = 0
        while t != None:
            length += 1
            t = t.next
        if length == n:
            head = head.next
            return head

        i = 0
        p = head
        pre = head
        q = head
        while i < n:
            q = q.next
            i += 1
        while q != None:
            q = q.next
            pre = p
            p = p.next

        pre.next = p.next

        return head
