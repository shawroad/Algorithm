"""

@file   : 032-n皇后问题.py

@author : xiaolu

@time   : 2020-02-02

"""


class Solution:
    def solveNQueens(self, n):
        res = []
        if n == 0:
            return res

        nums = [i for i in range(n)]  # [0, 1, 2, 3, 4, 5, 6, 7]
        col = [False for _ in range(n)]   # 列状态
        master = [False for _ in range(2 * n - 1)]  # 主对角线状态
        slave = [False for _ in range(2 * n - 1)]   # 负对角线状态
        stack = []

        self.__backtracking(nums, 0, n, col, master, slave, stack, res)
        return res

    def __backtracking(self, nums, row, n, col, master, slave, stack, res):
        if row == n:
            # 如果走到最终的结果 就将其转为我们的表格 输出
            board = self.__convert2board(stack, n)
            res.append(board)
            return

        for i in range(n):
            if not col[i] and not master[row + i] and not slave[row - i + n - 1]:
                # 选择当前进入 需要改变周围的状态
                stack.append(nums[i])
                col[i] = True
                master[row + i] = True   # 当前调整好后 主对角线不能放 所以将其置为True
                slave[row - i + n - 1] = True    # 当前调整好, 负对角线不能放 所以将其置为True

                # 深入下去
                self.__backtracking(nums, row + 1, n, col, master, slave, stack, res)

                # 如果深入不下去 我们回溯
                slave[row - i + n - 1] = False
                master[row + i] = False
                col[i] = False
                stack.pop()

    def __convert2board(self, stack, n):
        return ["." * stack[i] + "Q" + "." * (n - stack[i] - 1) for i in range(n)]


if __name__ == '__main__':
    n = 8
    solution = Solution()
    res = solution.solveNQueens(n)
    print(res)
