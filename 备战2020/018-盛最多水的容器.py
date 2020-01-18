"""

@file   : 018-盛最多水的容器.py

@author : xiaolu

@time   : 2020-01-15

"""
'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
'''

class Solution:
    '''
    此方法超时
    '''
    def maxArea(self, height):
        result = []
        i = max(height)
        for i in range(1, i+1):
            m = 0
            n = len(height) - 1

            while m < len(height):
                if height[m] >= i:
                    break
                else:
                    m += 1
            while n >= 0:
                if height[n] >= i:
                    break
                else:
                    n -= 1

            res = (n - m) * i
            result.append(res)

        return max(result)


class Solution2:
    def maxArea(self, height):
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # sol = Solution()
    # result = sol.maxArea(height)
    # print(result)

    sol = Solution2()
    result = sol.maxArea(height)
    print(result)





