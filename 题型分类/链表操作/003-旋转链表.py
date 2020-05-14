"""

@file  : 003-旋转链表.py

@author: xiaolu

@time  : 2020-05-08

"""
'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL

解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL

解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
'''
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        length = 0
        r = head
        while r is not None:
            r = r.next
            length += 1

        # 本身链表就不存在
        if length == 0:
            return None

        k = k % length

        # 偏移0位 那就是原地不动
        if k == 0:
            return head

        # 找出倒数k个节点　然后摘下来　接到最前面
        farward = head
        for i in range(k):
            farward = farward.next
        pre = head
        while farward.next is not None:
            farward = farward.next
            pre = pre.next

        h = pre.next
        pre.next = None

        r_z = h
        while r_z.next is not None:
            r_z = r_z.next

        r_z.next = head
        return h
