"""

@file   : 045-外观数列.py

@author : xiaolu

@time   : 2020-02-15

"""
'''
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

输入: 4
输出: "1211"
解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。

'''


class Solution:
    def countAndSay(self, n:int) -> str:
        if n <= 1:
            return '1'

        pre = self.countAndSay(n - 1)

        res = ''
        count = 1
        for idx in range(len(pre)):
            if idx == 0:
                count = 1
            elif pre[idx] != pre[idx - 1]:
                tmp = str(count) + pre[idx - 1]
                res += tmp
                count = 1
            elif pre[idx] == pre[idx - 1]:
                count += 1

            if idx == len(pre) - 1:
                tmp = str(count) + pre[idx]
                res += tmp
        return res


class Solution1:
    def countAndSay(self, n: int) -> str:
        result = []
        origin = '1'
        result.append(origin)
        for i in range(n - 1):
            temp = result[-1]
            pre = list(temp)
            res = ''
            count = 1
            for idx in range(len(pre)):
                if idx == 0:
                    count = 1
                elif pre[idx] != pre[idx - 1]:
                    tmp = str(count) + pre[idx - 1]
                    res += tmp
                    count = 1
                elif pre[idx] == pre[idx - 1]:
                    count += 1

                if idx == len(pre) - 1:
                    tmp = str(count) + pre[idx]
                    res += tmp
            result.append(res)
        return result[n - 1]


if __name__ == '__main__':
    n = 4
    # sol = Solution()
    # result = sol.countAndSay(n)
    # print(result)
    #
    sol1 = Solution1()
    result = sol1.countAndSay(n)
    print(result)



