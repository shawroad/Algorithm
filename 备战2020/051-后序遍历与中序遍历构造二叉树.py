"""

@file   : 051-后序遍历与中序遍历构造二叉树.py

@author : xiaolu

@time   : 2020-02-23

"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
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


# 先序遍历
def xianxubianli(root):
    if root:
        print(root.val)
        xianxubianli(root.left)
        xianxubianli(root.right)


if __name__ == '__main__':
    # 中序遍历
    inorder = [9, 3, 15, 20, 7]

    # 后序遍历
    postorder = [9, 15, 7, 20, 3]

    sol = Solution()
    root = sol.buildTree(inorder, postorder)

    xianxubianli(root)




