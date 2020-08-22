# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 15:50
# @Author  : xiaolu
# @FileName: 021-二叉树的所有路径.py
# @Software: PyCharm
'''
给定一个二叉树，返回所有从根节点到叶子节点的路径。
说明: 叶子节点是指没有子节点的节点。
示例:

输入:
   1
 /   \
2     3
 \
  5
输出: ["1->2->5", "1->3"]
解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
'''
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        def constrict_paths(root, path):
            if root is not None:
                path.append(str(root.val))
                if root.left is None and root.right is None:   # 当前节点是叶子节点
                    paths.append(path)   # 当前节点是叶子 将路径加入其中
                else:
                    path += '->'   # 当前节点不是叶子节点
                    constrict_paths(root.left, path)
                    constrict_paths(root.right, path)

        paths = []
        constrict_paths(root, '')
        return paths
