"""

@file   : 053-平衡二叉树.py

@author : xiaolu

@time   : 2020-02-25

"""
from typing import List


class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(in_left=0, in_right=len(inorder)):
            # nonlocal关键字解释: nonlocal只能在封装函数中使用，在外部函数先进行声明，在内部函数进行nonlocal声明
            # 这样在buildTree()函数中的pre_idx与helper()中的pre_idx是同一个变量。
            nonlocal pre_idx

            if in_left == in_right:
                return None

            # 构造根节点
            root_val = preorder[pre_idx]  # 先序遍历的第一个值
            root = TreeNode(root_val)

            # 用根节点分中序遍历序列 然后分其左右
            index = idx_map[root_val]

            # 递归
            pre_idx += 1

            # 建立左子树
            root.left = helper(in_left, index)

            # 建立右子树
            root.right = helper(index + 1, in_right)
            return root

        # 从先序遍历开始
        pre_idx = 0

        # 建立值和id的映射  这里针对的是中序遍历
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper()

    def height(self, root: TreeNode) -> int:
        # 求树的最大高度
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        # 判断是否平衡
        if not root:
            return True

        # 左右子树和本身平衡 就认为本树平衡
        return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == '__main__':
    # 前序遍历
    preorder = [3, 9, 20, 15, 7]

    # 中序遍历
    inorder = [9, 3, 15, 20, 7]

    sol = Solution()
    root = sol.buildTree(preorder, inorder)
    sign = sol.isBalanced(root)
    print('平衡与否:', sign)
