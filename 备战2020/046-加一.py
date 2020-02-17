"""

@file   : 046-加一.py

@author : xiaolu

@time   : 2020-02-16

"""

'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

'''
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = ''.join([str(i) for i in digits])
        digits = int(digits) + 1

        result = [int(i) for i in list(str(digits))]
        return result


if __name__ == '__main__':
    digits = [1, 2, 3]
    sol = Solution()
    result = sol.plusOne(digits)
    print(result)
