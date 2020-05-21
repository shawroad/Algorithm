"""

@file  : 002-快乐数.py

@author: xiaolu

@time  : 2020-05-18

"""
'''
编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，
也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 True ；不是，则返回 False 。

示例：
输入：19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''
# 暴力　有些耗时
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = []
        while n != 1:
            if n in visited:
                return False
            n = sum([int(i)*int(i) for i in list(str(n))])
        return True

# 推荐第二种快慢指针方法
class Solution2:
    def isHappy(self, n):
        def get_next(n):
            return sum([int(i)*int(i) for i in list(str(n))])

        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1


if __name__ == '__main__':
    n = 19
    sol = Solution2()
    result = sol.isHappy(n)
    print(result)

