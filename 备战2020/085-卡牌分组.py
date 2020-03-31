"""

@file   : 085-卡牌分组.py

@author : xiaolu

@time   : 2020-03-27

"""
'''
给定一副牌，每张牌上都写着一个整数。
此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。

示例 1：
输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]

示例 2：
输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。
'''
from typing import List
from fractions import gcd


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # 自己的理解  相当于统计所有数字的个数 所有的数字都能被最小的整除 即可  最小整数不能小于2
        temp_dict = dict()
        for d in deck:
            temp = temp_dict.get(d, 0)
            temp_dict[d] = temp + 1

        max_fre = max(temp_dict.values())

        for i in range(2, max_fre+1):
            count = 0
            for k, v in temp_dict.items():
                if v % i == 0:
                    count += 1
                if count == len(temp_dict):
                    return True

        return False


if __name__ == '__main__':
    deck = [1, 2, 3, 4, 4, 3, 2, 1]
    # deck = [1, 1, 1, 2, 2, 2, 3, 3]
    sol = Solution()
    result = sol.hasGroupsSizeX(deck)
    print(result)
