"""

@file   : 055-验证回文字符串.py

@author : xiaolu

@time   : 2020-02-25

"""
'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例:
输入: "A man, a plan, a canal: Panama"
输出: true
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = list(s)

        modify_str = []
        for s in s_list:
            if s.isalpha():
                s = s.lower()
                modify_str.append(s)

            if 48 <= ord(s) < 58:
                modify_str.append(s)

        i, j = 0, len(modify_str) - 1
        while i < j:
            if modify_str[i] == modify_str[j]:
                i += 1
                j -= 1

            else:
                return False
        return True


if __name__ == '__main__':
    string = "a man, a plan, a canal: panama"
    sol = Solution()
    sign = sol.isPalindrome(string)
    print("是否是回文字符串:", sign)

