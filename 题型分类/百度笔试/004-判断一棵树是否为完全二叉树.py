# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 15:19
# @Author  : xiaolu
# @FileName: 004-判断一棵树是否为完全二叉树.py
# @Software: PyCharm

# 判断一棵树是否为完全二叉树
# 左无、右有 ==> 返回 False
# 左无、右无 ==> 激活判断：之后所有节点都是叶节点
# 左有、右无 ==> 激活判断：之后所有节点都是叶节点        ==》      只要右无之后都必须是叶节点
# 左有、右有 ==> 不用处理


def isCBTree(head):
    if not head:
        return False
    que = []
    que.append(head)
    flag = False   # 是否激活判断
    while len(que) != 0:
        head = que.pop(0)
        if head.left:
            que.append(head.left)
        if head.right:
            que.append(head.right)

        if (not head.left) and head.right:
            # 左空, 右不空 不是完全二叉树
            return False

        if flag:
            # 若过程激活则判断节点是否为叶节点
            if head.left or head.right:
                return False

        if not (head.left and head.right):  # 左不空,右空   或者  左空,右空
            flag = True    # 激活判断在此之后的节点必须为叶节点
    return True