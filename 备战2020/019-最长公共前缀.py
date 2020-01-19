"""

@file   : 019-最长公共前缀.py

@author : xiaolu

@time   : 2020-01-15

"""
'''
输入: ["flower","flow","flight"]
输出: "fl"
'''
class Solution:
    def longestCommonPrefix(self, strs):
        result = []

        if len(strs) == 1:
            return strs[0]
        if len(strs) == 0:
            return ''

        # 找出最大的串
        min_len = 1000
        min_str = ''
        for i in strs:
            if len(i) < min_len:
                min_len = len(i)
                min_str = i

        strs.remove(min_str)
        for i, c in enumerate(list(min_str)):
            sign = True
            for s in strs:
                s = list(s)
                if s[i] == c:
                    pass
                else:
                    sign = False

            if sign == True:
                result.append(c)
            else:
                break

        result = ''.join(result)
        return result

if __name__ == '__main__':
    # strs = ["flower", "flow", "flight"]
    strs = ["aa", "a"]
    sol = Solution()
    result = sol.longestCommonPrefix(strs)
    print(result)


