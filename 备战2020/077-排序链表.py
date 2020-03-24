"""

@file   : 077-排序链表.py

@author : xiaolu

@time   : 2020-03-23

"""
'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
输入: 4->2->1->3
输出: 1->2->3->4
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 垃圾方法
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        data = []
        r = head
        while r != None:
            data.append(r.val)
            r = r.next
        data.sort()
        head = ListNode(data[0])
        r = head
        for d in data[1:]:
            temp = ListNode(d)
            r.next = temp
            r = r.next
        return head


# 归并
class Solution1:
    def sortList(self, head):
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        # 找出了中间位置
        mid, slow.next = slow.next, None   # 保存并切断

        # 递归去切断
        left, right = self.sortList(head), self.sortList(mid)

        # 合并
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next

        h.next = left if left else right

        return res.next


if __name__ == '__main__':
    # 构造链表
    data = [4, 2, 1, 3]
    head = ListNode(data[0])
    r = head
    for d in data[1:]:
        temp = ListNode(d)
        r.next = temp
        r = r.next

    sol = Solution1()
    result = sol.sortList(head)
    r = result

    while r != None:
        print(r.val)
        r = r.next







