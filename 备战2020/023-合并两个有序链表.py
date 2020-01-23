"""

@file   : 023-合并两个有序链表.py

@author : xiaolu

@time   : 2020-01-15

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        r = head

        p1 = l1
        p2 = l2

        while p1 != None and p2 != None:
            if p1.val < p2.val:
                r.next = p1
                p1 = p1.next
                r = r.next
            else:
                r.next = p2
                p2 = p2.next
                r = r.next

        if p1 != None:
            r.next = p1
        if p2 != None:
            r.next = p2

        return head.next

