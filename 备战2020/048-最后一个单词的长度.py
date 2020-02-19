"""

@file   : 048-最后一个单词的长度.py

@author : xiaolu

@time   : 2020-02-17

"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])


if __name__ == '__main__':
    s = 'Hello World'
    sol = Solution()
    result = sol.lengthOfLastWord(s)
    print(result)

