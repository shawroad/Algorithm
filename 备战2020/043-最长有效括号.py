"""

@file   : 043-最长有效括号.py

@author : xiaolu

@time   : 2020-02-14

"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        if len(s) < 2:
            return 0
        dp = [0] * len(s)
        for i, c in enumerate(s):
            if c == ')':
                if stack and stack[-1][0] == "(":
                    _, index = stack.pop()
                    dp[i] = max(dp[i], dp[index - 1] + 2 + dp[i - 1])
            else:
                stack.append(('(', i))
        return max(dp)


if __name__ == '__main__':
    s = "(()"
    sol = Solution()
    result = sol.longestValidParentheses(s)
    print(result)
