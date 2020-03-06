"""

@file   : 061-相同的树.py

@author : xiaolu

@time   : 2020-03-06

"""
'''
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例:
输入:       1         1
          / \       /  \
         2   3     2    3
        [1,2,3],   [1,2,3]

输出: true

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if not q or not p:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

