"""

@file  : 010-哈夫曼编码

@author: xiaolu

@time  : 2019-10-16

"""


class Node:
    # 构造节点
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.left = None
        self.right = None


class HuffmanTree:
    # 哈弗曼树
    # 根据Huffman树的思想：以叶子节点为基础，反向建立Huffman树
    def __init__(self, char_weights):
        self.a = [Node(part[0], part[1]) for part in char_weights]  # 根据输入的字符及其频数生成叶子节点
        while len(self.a) != 1:
            self.a.sort(key=lambda node: node.value, reverse=True)  # 按照节点的值从小到大排 然后逆转
            c = Node(value=(self.a[-1].value + self.a[-2].value))  # 找出最小的两个 合并得到新节点
            c.left = self.a.pop(-1)
            c.right = self.a.pop(-1)
            self.a.append(c)   # 然后把新节点加入到集合中

        self.root = self.a[0]  # 最后加的和作为根节点
        # self.b用于保存每个叶子节点的Haffuman编码, range的值只需要不小于树的深度就行
        self.b = [i for i in range(10)]

    # 用递归的思想生成编码　用的是先序遍历的思想
    def pre(self, tree, length):
        node = tree
        if not node:
            return
        elif node.name:
            print(node.name + '的编码为:', end='')
            for i in range(length):
                print(self.b[i], end=', ')
            print('\n')
            return
        self.b[length] = 0
        self.pre(node.left, length + 1)
        self.b[length] = 1
        self.pre(node.right, length + 1)

    # 生成哈夫曼编码
    def get_code(self):
        self.pre(self.root, 0)


if __name__ == '__main__':
    # 待编码的字符以及频数
    char_weights = [('a', 5), ('b', 4), ('c', 10), ('d', 8), ('f', 15), ('g', 2)]

    tree = HuffmanTree(char_weights)  # 哈弗曼树构造好了
    tree.get_code()  # 得到编码
