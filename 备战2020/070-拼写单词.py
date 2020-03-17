"""

@file   : 070-拼写单词.py

@author : xiaolu

@time   : 2020-03-17

"""
'''
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
注意：每次拼写时，chars 中的每个字母都只能用一次。
返回词汇表 words 中你掌握的所有单词的 长度之和。

示例 1：
输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释： 
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。

'''
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # 1. 先将chars构建成一个字典 标记处每个字符的个数
        result = []
        for word in words:
            char_dict = {}
            for i in chars:
                t = char_dict.get(i, 0)
                char_dict[i] = t + 1

            if self.fit(word, char_dict):
                result.append(word)
        result = ''.join(result)
        return len(result)

    def fit(self, word, char_dict):
        for i in word:
            t = char_dict.get(i, 0)
            if t == 0:
                return False
            else:
                char_dict[i] = t - 1
        return True


if __name__ == '__main__':
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    sol = Solution()
    result = sol.countCharacters(words, chars)
    print(result)

