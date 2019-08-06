"""

@file   : 018-二叉树的镜像.py

@author : xiaolu

@time   : 2019-08-03

"""
'''
题目:  二叉树的镜像说白了就是所有节点的左右子树进行交换
'''
class BiTree:
    def __init__(self, data=0, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


def build_tree(root, data):
    # 使用层次遍历构造一个二叉树
    # 用queue模拟一个队列  append()入队 pop(0) 出队
    i = 0
    queue = []
    queue.append(root)
    while queue is not None:
        temp = queue.pop(0)

        i += 1
        if i == len(data):
            break
        left_node = BiTree(data[i])

        i += 1
        if i == len(data):
            break
        right_node = BiTree(data[i])

        temp.lchild = left_node
        temp.rchild = right_node
        queue.append(left_node)
        queue.append(right_node)
    return root


def show_prior(root):
    # 先序遍历的结果
    if root != None:
        print(root.data, end=' ')
        show_prior(root.lchild)
        show_prior(root.rchild)


def mirror(root):
    if root == None or (root.lchild == None and root.rchild == None):
        return None

    # 碰到一个节点就将其左右子树进行交换
    temp = root.lchild
    root.lchild = root.rchild
    root.rchild = temp

    if root.lchild:
        mirror(root.lchild)
    if root.rchild:
        mirror(root.rchild)


if __name__ == '__main__':
    # data1是属于树1上的数据 按层次遍历的结果
    data = [3, 7, 9, 5, 6, 10, 12]

    # 构建一棵二叉树
    root = BiTree(data[0])
    root = build_tree(root, data)
    # 看下构建的二叉树的先序遍历
    print("原始的二叉树先序遍历:")
    show_prior(root)

    print('\n'+"*"*100)
    # 一棵树的镜像
    mirror(root)
    print("原始二叉树的镜像先序遍历:")
    show_prior(root)


