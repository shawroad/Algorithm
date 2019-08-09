"""

@file   : 023-二叉树的后序遍历.py

@author : xiaolu

@time   : 2019-08-07

"""
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


def digui_hou(root):
    # 递归的后序遍历算法
    if root != None:
        digui_hou(root.lchild)
        digui_hou(root.rchild)
        print(root.data, end=' ')


def feidigui_hou(root):
    # 非递归的后序遍历算法
    temp_result = []
    stack = []  # 进栈append(), 出栈pop()
    stack.append(root)

    while len(stack) != 0:
        temp = stack.pop(-1)

        temp_result.append(temp.data)

        if temp.lchild != None:
            stack.append(temp.lchild)

        if temp.rchild != None:
            stack.append(temp.rchild)

    result = reversed(temp_result)
    # 因为reversed完后的结果的迭代器 所以需要逐个取
    for r in result:
        print(r, end=' ')


if __name__ == '__main__':
    # 将以下数据构造成二叉树
    array_data = [3, 2, 4, 9, 34, 53, 23, 43, 95]
    root = BiTree(array_data[0])
    root = build_tree(root, array_data)

    # 1. 先整一个递归的后序遍历算法
    print("递归的后序遍历:")
    digui_hou(root)

    print('\n' + "*"*100)

    # 2. 非递归的后续遍历算法
    print("非递归的后序遍历:")
    feidigui_hou(root)

