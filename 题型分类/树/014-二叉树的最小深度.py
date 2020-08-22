# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 14:15
# @Author  : xiaolu
# @FileName: 014-二叉树的最小深度.py
# @Software: PyCharm


class Solution:
    def minDepth(self, root) -> int:
        if root is None:
            return 0

        children = [root.left, root.right]
        if root.left is None and root.right is None:
            return 1

        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1
