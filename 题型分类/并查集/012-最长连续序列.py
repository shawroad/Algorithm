# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 16:54
# @Author  : xiaolu
# @FileName: 012-最长连续序列.py
# @Software: PyCharm
'''
给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。

示例:
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
'''
import collections
from typing import List


class DSU:
    def __init__(self, nums):
        self.parent = {num: num for num in nums}   # 初始化  每个数的跟就是它本身
        self.cnt = collections.defaultdict(lambda: 1)   # 统计每个节点作为根  后面跟了几个节点

    def find(self, x):    # 找父节点
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        # x肯定在parent中，因为x本身就是nums中的数值, y就不一定了, 因为y是在x上自动加1得来的数
        if y not in self.parent:   # 如果y没在根集合中
            return 1

        # 寻找x, y的根节点，记为root1, root2
        root1, root2 = self.find(x), self.find(y)   # 找到他们的跟

        # 表示当前的数与之前已经出现的一些数字能构成连续序列
        if root1 == root2:    # 表示他们是同根
            return self.cnt[root1]

        # x，y是连续的 但是不同根 那就把它们合并起来
        self.parent[root2] = root1

        # 现在的树的元素个数就是这两棵树之和
        self.cnt[root1] += self.cnt[root2]
        return self.cnt[root1]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dsu = DSU(nums)
        res = 1
        for num in nums:
            res = max(res, dsu.union(num, num + 1))
        # 分析
        # 100的时候   parent: {100:100, 4:4, 200:200, 1:1, 3:3, 2:2}  cnt: {100: 1, 4: 1, 200: 1, 1: 1, 3: 1, 2: 1}
        # 4的时候     parent: {100:100, 4:4, 200:200, 1:1, 3:3, 2:2}  cnt: {100: 1, 4: 1, 200: 1, 1: 1, 3: 1, 2: 1}
        # 200的时候   parent: {100:100, 4:4, 200:200, 1:1, 3:3, 2:2}  cnt: {100: 1, 4: 1, 200: 1, 1: 1, 3: 1, 2: 1}
        # 1的时候     parent: {100:100, 4:4, 200:200, 1:1, 3:3, 2:1}  cnt: {100: 1, 4: 1, 200: 1, 1: 2, 3: 1, 2: 1}
        # 3的时候     parent: {100:100, 4:3, 200:200, 1:1, 3:3, 2:1}  cnt: {100: 1, 4: 1, 200: 1, 1: 2, 3: 2, 2: 1}
        # 2的时候     parent: {100:100, 4:3, 200:200, 1:1, 3:1, 2:1}  cnt: {100: 1, 4: 1, 200: 1, 1: 2, 3: 2, 2: 3}
        return res


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    sol = Solution()
    result = sol.longestConsecutive(nums)
    print(result)


