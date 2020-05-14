"""

@file  : 001-无重复字符的最长子串.py

@author: xiaolu

@time  : 2020-05-08

"""
'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''
'''
(abc)abcbb
a(bca)bcbb
ab(cab)cbb
abc(abc)bb
abca(bc)bb
abcab(cb)b
abcabc(b)b
abcabcb(b)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 定义一个集合 判断当前的字符之前有没有出现过
        occ = set()

        right = 0  # 右指针
        result = 0   # 这一种的right不进行返回
        for i in range(len(s)):
            # 右指针走 直到碰到相同的或走到最后
            while right < len(s) and s[right] not in occ:
                occ.add(s[right])
                right += 1

            result = max(result, right - i)
            occ.remove(s[i])
        return result


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         result = 0
#         temp = set()
#         for i in range(len(s)):
#             right = i   # right返回
#             while right < len(s) and s[right] not in temp:
#                 temp.add(s[right])
#                 right += 1
#
#             result = max(result, right - i)
#             temp = set()
#         return result


if __name__ == '__main__':
    s = 'bbbbb'
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    print(result)


