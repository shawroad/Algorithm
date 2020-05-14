"""

@file  : 005-合并k个排序链表.py

@author: xiaolu

@time  : 2020-05-08

"""
'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def mergeKLists(self, lists: List[ListNode]):
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


# 下面方法借助两个排序链表
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         head = ListNode(0)
#         r = head

#         p1 = l1
#         p2 = l2

#         while p1 != None and p2 != None:
#             if p1.val < p2.val:
#                 r.next = p1
#                 p1 = p1.next
#                 r = r.next
#             else:
#                 r.next = p2
#                 p2 = p2.next
#                 r = r.next

#         if p1 != None:
#             r.next = p1
#         if p2 != None:
#             r.next = p2

#         return head.next

#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         if len(lists) == 0:
#             return None
#         if len(lists) == 1:
#             return lists[0]

#         if len(lists) == 2:
#             return self.mergeTwoLists(lists[0], lists[1])

#         if len(lists) >= 3:
#             temp = self.mergeTwoLists(lists[0], lists[1])
#             for i in lists[2:]:
#                 temp = self.mergeTwoLists(temp, i)

#         return temp