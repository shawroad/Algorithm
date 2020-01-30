"""

@file   : 028-括号生成.py

@author : xiaolu

@time   : 2020-01-16

"""
'''
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution(object):
    def generateParenthesis(self, n):

        def generate(A = []):
            '''
            生成2 ** (2n) 个     # 如果n对 则需填2n个坑, 然后根据排列组合 得出所有的情况
            :param A:
            :return:
            '''
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:  # bar 等于负数 说明右括号超了
                    return False
            return bal == 0

        ans = []
        generate()
        return ans


if __name__ == '__main__':
    n = 3
    sol = Solution()
    result = sol.generateParenthesis(n)
    print("最终的结果为:", result)

