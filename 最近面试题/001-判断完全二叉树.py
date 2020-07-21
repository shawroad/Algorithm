# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 9:14
# @Author  : xiaolu
# @FileName: 001-判断完全二叉树.py
# @Software: PyCharm

def is_full_tree(root):
    queue = []
    queue.append(root)
    sign = False
    while len(queue) > 0:
        temp = queue.pop(0)
        if temp.left is not None:
            queue.append(temp.left)

        if temp.right is not None:
            queue.append(temp.right)

        if temp.left is None and temp.right is not None:  # 左空右不空 立马就是False
            return False

        if sign:
            if temp.left is not None or temp.right is not None:
                return False

        if temp.left is None or temp.right is None:
            sign = True
    return True
