"""

@file  : 003-划分字母区间.py

@author: xiaolu

@time  : 2020-05-18

"""
'''
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，
同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。

示例 1:
输入: S = "ababcbacadefegdehijhklij"
输出: [9,7,8]

解释:
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

注意:
S的长度在[1, 500]之间。
S只包含小写字母'a'到'z'。
'''

'''
思路：
   看见开头一个字母, 就要看这个字母最后出现在哪, 然后这个开头和结尾之间的那些其他字母是不是都落在这个区间里, 
   如果不是, 则扩充区间, 如果是, 那就最好了. 另一个点用什么方法确定? 对于这道题,一个关键点是利用字典key的
   唯一性来记载一个字母最大的index是几. 然后遍历字符串并跟它比较,用max函数取出边界大还是当前遍历的这个字母
   的最大index大. 如果当前遍历字母的最大index大,那就说明超过了边界,那就要更新边界．
'''
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        max_index = {item: idx for idx, item in enumerate(S)}  # 这里保存的是每个字母在字符串中最靠后的位置是哪
        start, end = 0, 0  # 起始边界， 结束边界
        ans = []

        for idx, i in enumerate(S):
            end = max(end, max_index[i])  # 这里就是用边界和当前遍历到的那个字母的最大index去比较,看看谁大

            if idx == end:
                # 遍历的位置和边界重合
                ans.append(end - start + 1)
                start = idx + 1
        return ans


if __name__ == '__main__':
    S = "ababcbacadefegdehijhklij"
    sol = Solution()
    result = sol.partitionLabels(S)
    print(result)
