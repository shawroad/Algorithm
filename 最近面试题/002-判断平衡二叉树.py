# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 9:14
# @Author  : xiaolu
# @FileName: 002-判断平衡二叉树.py
# @Software: PyCharm
def get_height(root):
    if root is None:
        return 0
    l_height = get_height(root.left)
    r_height = get_height(root.right)
    return max(l_height, r_height) + 1


def is_balance_tree(root):
    if root is None:
        return True

    return abs(get_height(root.left) - get_height(root.right)) <= 1 and \
           is_balance_tree(root.left) and is_balance_tree(root.right)
