"""

@file   : 076-链表的中间节点.py

@author : xiaolu

@time   : 2020-03-23

"""
'''
给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # 策略 设置两个指针 一个人走一步 一个人每次走两步
        lay, forward = head, head
        while forward.next != None:
            forward = forward.next
            forward = forward.next
            lay = lay.next
            if forward == None:
                break
        return lay


if __name__ == '__main__':
    # 构造链表
    data = [1, 2, 3, 4, 5, 6]
    head = ListNode(None)
    r = head
    for d in data:
        temp = ListNode(d)
        r.next = temp
        r = r.next
    sol = Solution()
    result = sol.middleNode(head)
    print(result)



