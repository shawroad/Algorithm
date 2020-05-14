"""

@file  : 006-反转链表.py

@author: xiaolu

@time  : 2020-05-11

"""
'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        qian = head
        forward = head.next
        qian.next = None

        while forward:
            hou = forward
            forward = forward.next
            hou.next = qian
            qian = hou
        return qian


