"""

@file   : 015-整数翻转.py

@author : xiaolu

@time   : 2020-01-13

"""


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = x * sign
        else:
            sign = 1
            x = x * sign

        num_list = list(str(x))
        num_list.reverse()
        result = ''.join(num_list)
        result = sign * int(result)
        return result if -2147483648 < result < 2147483647 else 0


if __name__ == '__main__':
    x = -321
    sol = Solution()
    result = sol.reverse(x)
    print("最终的结果:", result)
