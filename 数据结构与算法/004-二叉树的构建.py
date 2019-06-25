"""

@file   : 004-二叉树的构建.py

@author : xiaolu

@time   : 2019-06-25

"""
class BTNode:
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


def build_btree(array):
    queue = []
    step_node = BTNode(array[0], None, None)
    queue.append(step_node)
    i = 1
    while len(queue) != 0 and i < (len(array)-1):
        temp = queue.pop(0)
        # 构造左节点
        temp_l = BTNode(array[i], None, None)
        temp.lchild = temp_l
        i += 1

        temp_r = BTNode(array[i], None, None)
        temp.rchild = temp_r
        i += 1
        queue.append(temp_l)
        queue.append(temp_r)

    return step_node


def prior_visit(step_node):
    # 先序遍历
    if step_node != None:
        print(step_node.data, end=", ")
        prior_visit(step_node.lchild)
        prior_visit(step_node.rchild)


def mid_visit(step_node):
    # 中序遍历
    if step_node != None:
        mid_visit(step_node.lchild)
        print(step_node.data, end=", ")
        mid_visit(step_node.rchild)


def end_visit(step_node):
    # 中序遍历
    if step_node != None:
        end_visit(step_node.lchild)
        end_visit(step_node.rchild)
        print(step_node.data, end=", ")


if __name__ == "__main__":
    # 假设下面列表中的数据为层次遍历的结果
    array = [43, 23, 212, 46, 34, 90, 85, 2, 6, 323, 35]

    # 我们构建一棵树
    # 这里需要一个队列  我们就用队列的模拟 其中pop(0)代表出队， append()代表进队
    step_node = build_btree(array)

    # 我们先序遍历一下
    print("先序遍历的结果:", end='')
    prior_visit(step_node)
    print("\n" + "*"*100)

    print("中序遍历的结果:", end='')
    mid_visit(step_node)
    print("\n" + "*"*100)

    print("后序遍历的结果:", end='')
    end_visit(step_node)



