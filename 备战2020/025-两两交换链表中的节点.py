"""

@file   : 025-两两交换链表中的节点.py

@author : xiaolu

@time   : 2020-01-15

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 顶点数少于两个
        if not head or not head.next:
            return head

        end = ListNode(0)    # end初始化为头结点
        res = head.next    # 返回结果首节点
        pre, cur = head, head.next    # 当前要交换的前节点，后节点

        while cur:
            tmp = cur.next
            end.next = cur
            cur.next = pre
            end = pre
            if not tmp:    # 节点数为偶数的结束条件
                end.next = None
                break
            pre = tmp
            cur = tmp.next
        if not cur:    # 节点数为奇数的处理
            end.next = pre
        return res
