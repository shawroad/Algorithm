"""

@file  : 004-翻转二叉树.py

@author: xiaolu

@time  : 2020-06-10

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)

        root.left = right
        root.right = left
        return root

