"""

@file   : 069-字符串压缩.py

@author : xiaolu

@time   : 2020-03-16

"""
'''
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

示例1:
 输入："aabcccccaaa"
 输出："a2b1c5a3"
 
示例2:
 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。

'''
class Solution:
    def compressString(self, S: str) -> str:
        if len(S) == 0:
            return ''
        result = ''
        count = 0
        origin = S[0]
        for s in S:
            if s == origin:
                count += 1
            else:
                result += origin + str(count)
                origin = s
                count = 1
        result += origin + str(count)
        if len(result) < len(S):
            return result
        else:
            return S


if __name__ == '__main__':
    # s = 'aaaabbbb'
    s = "abbccd"
    sol = Solution()
    result = sol.compressString(s)
    print(result)
