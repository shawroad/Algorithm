"""

@file   : 052-二叉树的最大最小深度.py

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 后续遍历构造二叉树
        def helper(in_left, in_right):
            # 没有元素构造节点
            if in_left > in_right:
                return None

            # 取最后一个元素构造节点
            val = postorder.pop()
            root = TreeNode(val)

            # 然后在中序遍历中分割
            index = idx_map[val]

            # 建立右子树
            root.right = helper(index + 1, in_right)

            # 建立左子树
            root.left = helper(in_left, index - 1)
            return root

        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)

    def maxDepth(self, root):
        '''
        最大深度
        :param root: 根节点
        :return:
        '''
        if root is None:
            return 0

        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

    def minDepth(self, root):
        '''
        最小深度
        :param root:
        :return:
        '''
        if not root:
            return 0

        children = [root.left, root.right]

        # 代表没有任何孩子
        if not any(children):
            return 1

        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1


if __name__ == '__main__':
    # 首先构造二叉树
    # 中序遍历
    inorder = [9, 3, 15, 20, 7]
    # 后序遍历
    postorder = [9, 15, 7, 20, 3]

    sol = Solution()
    root = sol.buildTree(inorder, postorder)
    depth = sol.maxDepth(root)
    print('二叉树的最大深度为:', depth)

    depth = sol.maxDepth(root)
    print('二叉树的最小深度为:', depth)


