"""

@file   : 030-串联所有单词的子串.py

@author : xiaolu

@time   : 2020-01-16

"""
'''
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1：
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]

解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
'''
import itertools

# class Solution:
#     def findSubstring(self, s: str, words):
#         if s == '' or len(words) == 0:
#             return []
#
#         n = len(words)
#         index_pailie = list(itertools.permutations(range(n)))
#         pailie = []
#         for p in index_pailie:
#             string = ''
#             for i in p:
#                 string += words[i]
#             pailie.append(string)
#
#         result = []
#         for i in pailie:
#             num = s.count(i)
#
#             k = 0
#             start = 0
#             while k < num:
#                 r = s.find(i, start, len(s))
#                 k += 1
#                 if r != -1:
#                     result.append(r)
#                 start = r + 1
#         result = list(set(result))
#         return result


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter
        if not s or not words:
            return []

        words_len = len(words[0])           # 一个单词的长度
        words_num = len(words)              # words中单词的个数
        words_cnt = Counter(words)          # {'foo': 1, 'bar': 1}
        s_len = len(s)                      # 字符串s的长度
        res = []                            # 存储起始位置

        W = words_len * words_num           # 此处窗口大小为 2*3
        left = 0
        while (left + W) <= s_len:
            tmp = []
            i = left
            for j in range(words_num):       # 将窗口内的字符串添加到tmp中
                tmp.append(s[i:i + words_len])
                i = i + words_len
            tmp = Counter(tmp)
            if tmp == words_cnt:
                res.append(left)
                left = left + 1
            else:
                left = left + 1
        return res


if __name__ == '__main__':
    # s = "barfoothefoobarman"
    # words = ["foo", "bar"]

    # s = "foobarfoobar"
    # words = ["foo", "bar"]

    s = "aaa"
    words = ["a", "a"]
    sol = Solution()
    result = sol.findSubstring(s, words)
    print("最终的结果是:", result)

