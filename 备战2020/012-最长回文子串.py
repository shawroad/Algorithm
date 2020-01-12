"""

@file   : 012-最长回文子串.py

@author : xiaolu

@time   : 2020-01-11

"""
class Solution:
    # 中心扩散法Spread From Center
    def spread(self, s, left, right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        # 动态规划法-中心扩散法Spread From Center
        if s == s[::-1]:
            return s
        res = s[:1]
        for i in range(len(s)):
            palindrome_odd = self.spread(s, i, i)
            palindrome_even = self.spread(s, i, i + 1)
            # 当前找到的最长回文子串
            res = max(palindrome_odd, palindrome_even, res, key=len)
        return res


if __name__ == '__main__':
    s = "ab"
    sol = Solution()
    result = sol.longestPalindrome(s)
    print(result)

