# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 9:14
# @Author  : xiaolu
# @FileName: 002-判断平衡二叉树.py
# @Software: PyCharm
def get_hight(root):
    if root is None:
        return 0
    left_height = get_hight(root.left)
    right_height = get_hight(root.right)
    return max(left_height, right_height) + 1


def is_balance_tree(root):
    if root is None:
        return True
    return abs(get_hight(root.left) - get_hight(root.right)) <= 1 and is_balance_tree(root.left) and is_balance_tree(root.right)

