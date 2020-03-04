"""

@file   : 059-分割回文串.py

@author : xiaolu

@time   : 2020-03-04

"""
'''

给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

思路:
在已有的字符串基础上增加一个字母，除了在每个结果后面加上新字母外，增加的
字母还有可能与前结果的最后一个回文，或者最后两个回文组成新回文，没有其他情况。
'''
class Solution:
    # 回溯法
    def partition(self, s):
        split_result = []   # 保存最终的结果

        if len(s) == 0:
            return split_result

        def back(start=0, res=[]):
            if start >= len(s):
                split_result.append(res)
                return

            for end in range(start + 1, len(s) + 1):
                split_s = s[start: end]

                # 判断是回文
                if split_s == s[start: end][::-1]:
                    back(end, res + [split_s])
        back()
        return split_result


if __name__ == '__main__':
    s = 'aab'
    sol = Solution()
    result = sol.partition(s)
    print(result)

