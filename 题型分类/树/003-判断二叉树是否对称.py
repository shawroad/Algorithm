# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 9:15
# @Author  : xiaolu
# @FileName: 003-判断二叉树是否对称.py
# @Software: PyCharm


def is_duichen(l_root, r_root):
    if l_root is None and r_root is None:
        return True
    if l_root is None or r_root is None:
        return False

    return l_root.val == r_root.val and is_duichen(l_root.left, r_root.right) and is_duichen(l_root.right, r_root.left)


def main(root):
    if root is None:
        return True
    return is_duichen(root, root)
