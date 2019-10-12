"""

@file  : 009-二叉排序树.py

@author: xiaolu

@time  : 2019-10-10

"""
class BtNode:
    # 节点定义
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


def digui_xian(root):
    # 递归先序
    if root is not None:
        print(root.data, end=' ')
        digui_xian(root.lchild)
        digui_xian(root.rchild)


def digui_zhong(root):
    # 递归中序
    if root is not None:
        digui_zhong(root.lchild)
        print(root.data, end=' ')
        digui_zhong(root.rchild)


def insert_node(root, data):
    while True:
        if data < root.data:
            if root.lchild is None:
                root.lchild = BtNode(data)
                break
            else:
                root = root.lchild
        if data > root.data:
            if root.rchild is None:
                root.rchild = BtNode(data)
                break
            else:
                root = root.rchild


if __name__ == '__main__':
    data_list = [6, 2, 8, 23, 4, 12, 1, 5]

    root = BtNode(data_list[0])
    for d in data_list[1:]:
        insert_node(root, d)

    # 先序遍历
    digui_xian(root)

    print("\n")
    # 中序遍历 二叉排序树的中序遍历是从小到大的
    digui_zhong(root)


