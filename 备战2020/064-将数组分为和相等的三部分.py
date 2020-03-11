"""

@file   : 064-将数组分为和相等的三部分.py

@author : xiaolu

@time   : 2020-03-11

"""
'''
给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

示例 1：
输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
'''
from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        # 计算总和
        s = sum(A)

        target = s // 3
        i = 0
        cur = 0
        while i < len(A):
            cur +=A[i]
            if cur == target:
                break
            i += 1
        if cur != target:
            return False

        cur = 0
        j = i + 1
        while j < len(A):
            cur += A[j]
            if cur == target:
                break
            j += 1
        if cur != target:
            return False

        if j == len(A)-1:
            return False

        return True


if __name__ == '__main__':
    # data = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
    data = [1, -1, 1, -1]
    sol = Solution()
    result = sol.canThreePartsEqualSum(data)
    print(result)

