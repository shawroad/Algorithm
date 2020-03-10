"""

@file   : 063-二叉树的直径.py

@author : xiaolu

@time   : 2020-03-10

"""
'''
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_path_len = 1

        def get_max(root):

            nonlocal max_path_len

            if root is None:
                return 0

            L = get_max(root.left)
            R = get_max(root.right)

            max_path_len = max(max_path_len, L + R + 1)   # 保存最大路径
            return max(L, R) + 1

        get_max(root)
        return max_path_len - 1
