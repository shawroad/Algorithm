"""

@file   : 011-无重复字符的最长子串.py

@author : xiaolu

@time   : 2020-01-10

"""
'''
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len


if __name__ == '__main__':
    # s = "abcabcbb"
    s = 'au'
    # s = "jbpnbwwd"
    # s = "pwwkew"
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    print("最终的结果为:", result)


