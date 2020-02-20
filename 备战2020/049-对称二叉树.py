"""

@file   : 049-对称二叉树.py

@author : xiaolu

@time   : 2020-02-19

"""


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True

        # 用队列保存节点
        queue = [root, root]
        while queue:
            # 从队列中取出两个节点，在比较这两个节点
            left = queue.pop()
            right = queue.pop()

            # 如果两个节点都为空就继续循环，两者有一个为空就返回False
            if left == None and right == None:
                continue

            if left == None or right == None:
                return False

            if left.val != right.val:
                return False

            # 将左节点的左孩子， 右节点的右孩子放入队列
            queue.append(left.left)
            queue.append(right.right)

            # 将左节点的右孩子，有节点的左孩子放入队列
            queue.append(left.right)
            queue.append(right.left)
        return True


if __name__ == '__main__':
    tree = TreeNode(0)
    left_c = TreeNode(1)
    right_c = TreeNode(1)
    tree.left = left_c
    tree.right = right_c
    sol = Solution()
    is_bi_tree = sol.isSymmetric(tree)
    print(is_bi_tree)




