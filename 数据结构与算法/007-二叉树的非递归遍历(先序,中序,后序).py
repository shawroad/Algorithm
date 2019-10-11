"""

@file  : 007-二叉树的非递归遍历(先序,中序,后序).py

@author: xiaolu

@time  : 2019-10-10

"""
class BtNode:
    # 节点定义
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


def build_tree(data_list):
    # 建立二叉树
    root = BtNode(data_list[0])
    queue = []  # 队列
    queue.append(root)
    i = 0
    while queue is not None:
        temp = queue.pop(0)
        i += 1
        if i <= (len(data_list) - 1):
            lnode = BtNode(data_list[i])
            temp.lchild = lnode
            queue.append(lnode)
        else:
            break

        i += 1
        if i <= (len(data_list) - 1):
            rnode = BtNode(data_list[i])
            temp.rchild = rnode
            queue.append(rnode)
        else:
            break
    return root


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


def digui_hou(root):
    # 递归后序
    if root is not None:
        digui_hou(root.lchild)
        digui_hou(root.rchild)
        print(root.data, end=' ')


def fei_digui_xian(root):
    # 非递归的先序遍历
    stack = []
    stack.append(root)
    while len(stack) != 0:
        temp = stack.pop(-1)
        print(temp.data, end=' ')
        if temp.rchild is not None:
            stack.append(temp.rchild)
        if temp.lchild is not None:
            stack.append(temp.lchild)


def fei_digui_zhong(root):
    p = root
    stack = []
    while (p is not None) or (len(stack) != 0):
        while p is not None:
            stack.append(p)
            p = p.lchild

        if len(stack) != 0:
            p = stack.pop(-1)
            print(p.data, end=' ')
            p = p.rchild


def fei_digui_hou(root):
    # 非递归的后序遍历
    stack1 = []
    stack2 = []
    stack1.append(root)
    while len(stack1) != 0:
        temp = stack1.pop(-1)
        stack2.append(temp.data)
        if temp.lchild is not None:
            stack1.append(temp.lchild)
        if temp.rchild is not None:
            stack1.append(temp.rchild)
    while len(stack2) != 0:
        print(stack2.pop(-1), end=' ')


if __name__ == '__main__':
    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = build_tree(data_list)

    print("递归先序", end=':')
    digui_xian(root)
    print('\n')

    print("递归中序", end=':')
    digui_zhong(root)
    print('\n')

    print("递归后序", end=':')
    digui_hou(root)
    print('\n')

    print("非递归先序", end=':')
    fei_digui_xian(root)
    print('\n')

    print("非递归中序", end=':')
    fei_digui_zhong(root)
    print('\n')

    print("非递归后序", end=':')
    fei_digui_hou(root)
    print('\n')
