"""

@file  : 002-对称二叉树.py

@author: xiaolu

@time  : 2020-06-10

"""
'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def check(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return node1.val == node2.val and self.check(node1.left, node2.right) and self.check(node1.right, node2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root, root)

