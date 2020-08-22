# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 15:18
# @Author  : xiaolu
# @FileName: 020-二叉树的序列化和反序列化.py
# @Software: PyCharm

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        # 序列化
        if root is None:
            return '[]'
        queue = []
        queue.append(root)
        res = []
        while len(queue) > 0:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('null')
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        # "[1,2,3,null,null,4,5]"
        # 反序列化
        if data == '[]':
            return
        vals, i = data[1: -1].split(','), 1   # 之所以从1开始到-1是为了把前后的括号去掉
        queue = []
        root = TreeNode(int(vals[0]))
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            if vals[i] != 'null':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != 'null':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

