"""

@file  : 004-复制带随机指针的链表.py

@author: xiaolu

@time  : 2020-05-08

"""
'''
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
要求返回这个链表的 深拷贝。 
我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
 

示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

示例 2：
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

示例 3：
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]

示例 4：
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
 

提示：
-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。
'''
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# 思路:
# 遍历链表两次：
# 第一遍：把每个新生成的结点放在对应的旧结点后面， 形如: 1->1'->2->2'->3->3'->4->4'->null。 相当于在原始的链表中的每个节点后加一个新节点
# 第二遍：修改每个新结点的 next 指针和 random 指针。

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # 第一遍遍历，把每个新生成的结点放在对应的旧结点后面
        p = head
        while p:
            new_node = Node(p.val)
            new_node.next = p.next
            p.next = new_node

            p = new_node.next  # 下一个旧结点

        # 第二遍修改每个新结点的 next 和 random
        p = head
        while p:
            # 相当于把原始节点删除了
            next_origin = p.next.next  # 下一个旧结点备份一下
            p.next.next = next_origin.next if next_origin else None  # 修改新结点的 next　

            p.next.random = p.random.next if p.random else None  # 修改新结点的 random

            p = next_origin  # 下一个旧结点

        return head.next
