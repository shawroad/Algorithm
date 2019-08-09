"""

@file   : 022-树的层序遍历.py

@author : xiaolu

@time   : 2019-08-07

"""
'''
题目:
    也就是从根节点开始, 一层一层的打印
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


def layers_visit(root):
    # 层序遍历
    queue = []
    queue.append(root)

    while len(queue) != 0:
        temp = queue.pop(0)
        print(temp.data, end=' ')
        if temp.lchild is not None:
            queue.append(temp.lchild)
        if temp.rchild is not None:
            queue.append(temp.rchild)


if __name__ == '__main__':
    # 将以下数据构造成二叉树
    array_data = [3, 2, 4, 9, 34, 53, 23, 43, 95]
    root = BiTree(array_data[0])
    root = build_tree(root, array_data)
    print("先序遍历:")
    show_prior(root)
    print("\n" + "*"*100)


    # 层次遍历
    print("层序遍历:")
    layers_visit(root)


