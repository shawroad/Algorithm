"""

@file   : 056-将有序数组转换为二叉搜索树.py

@author : xiaolu

@time   : 2020-02-25

"""
'''
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
'''
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            p = (left + right) // 2

            # 中序遍历构造
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        return helper(0, len(nums) - 1)

    def xianxubianli(self, root):
        '''
        先序遍历
        :param root:
        :return:
        '''
        if root is not None:
            print(root.val)
            self.xianxubianli(root.left)
            self.xianxubianli(root.right)


if __name__ == '__main__':
    num = [-10, -3, 0, 5, 9]
    sol = Solution()
    root = sol.sortedArrayToBST(num)
    sol.xianxubianli(root)
