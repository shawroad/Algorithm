"""

@file   : 005-二叉排序树的构建.py

@author : xiaolu

@time   : 2019-06-25

"""
class BTNode:
    # 节点定义
    def __init__(self, data, lchild, rchild):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


def build_Tree(root, data):
    # 构建二叉树
    if root == None:
        root = BTNode(data, None, None)
        return

    elif data < root.data:     # 访问左子树
        if root.lchild == None:
            root.lchild = BTNode(data, None, None)
        build_Tree(root.lchild, data)

    elif data > root.data:     # 访问右子树
        if root.rchild == None:
            root.rchild = BTNode(data, None, None)
        build_Tree(root.rchild, data)

    else:    # 如果存在有值与原本树中的值相同，直接pass掉
        pass


def mid_visit(root):
    # 中序遍历
    if root != None:
        mid_visit(root.lchild)
        print(root.data, end=' ')
        mid_visit(root.rchild)


if __name__ == "__main__":
    # 定义一个根节点
    root = BTNode(51, None, None)
    # 接下来将下面的值插入排序树
    array = [32, 24, 12, 53, 656, 23, 53, 757, 75]
    for i in array:
        build_Tree(root, i)

    # 为了检查我们建立的树，我们采用中序，因为二叉排序树的中序遍历是有序的
    print("中序遍历二叉排序树的结果:")
    mid_visit(root)

