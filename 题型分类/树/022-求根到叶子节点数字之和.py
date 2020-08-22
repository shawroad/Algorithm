# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 16:37
# @Author  : xiaolu
# @FileName: 022-求根到叶子节点数字之和.py
# @Software: PyCharm
'''
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
例如，从根到叶子节点路径 1->2->3 代表数字 123。
计算从根到叶子节点生成的所有数字之和。
说明: 叶子节点是指没有子节点的节点。

示例 1:
输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, s_n):
            if root is not None:
                s_n += str(root.val)
                if root.left is None and root.right is None:
                    t = int(s_n) if len(s_n) > 0 else 0
                    result.append(t)
                else:
                    dfs(root.left, s_n)
                    dfs(root.right, s_n)

        result = []
        dfs(root, '')
        return sum(result)









