"""

@file   : 007-两数之和 IV - 输入 BST.py

@author : xiaolu

@time   : 2020-01-07

"""
'''
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root, k):
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        num = inorder(root)
        num.sort()
        n = len(num)

        i, j = 0, n - 1
        while i < j:
            if num[i] + num[j] > k:
                j -= 1
            elif num[i] + num[j] < k:
                i += 1
            else:
                return True
        return False
