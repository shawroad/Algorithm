"""

@file   : 017-回文数.py

@author : xiaolu

@time   : 2020-01-15

"""
'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x = str(x)
            x_orign = x
            x_list = list(x)
            x_list.reverse()

            x_res = ''.join(x_list)

            if x_orign == x_res:
                return True
            else:
                return False


if __name__ == '__main__':
    # num = 121
    num = 10
    sol = Solution()
    result = sol.isPalindrome(num)
    print("最终的结果为:", result)
