"""

@file   : 0018-八皇后问题.py

@author : xiaolu

@time   : 2019-06-29

"""
total = 0  # 统计解法
c = [0] * 8


def is_ok(row):
    for j in range(0, row):
        # 是否水平在一天线上或者两个斜方向(左到右向下方向, 左到右向上方向)
        if c[row] == c[j] or row - c[row] == j-c[j] or row + c[row] == j + c[j]:
            return False
    return True


def queen(row):
    global total
    if row == n:    # row如果等于8 说明0-7行放好了，正式我们要的结果
        total += 1
        print("解法:", c)
    else:
        for col in range(0, n):
            c[row] = col
            # 每列放一次，要检查此时行是否满足
            if is_ok(row):
                queen(row+1)


if __name__ == '__main__':
    n = 8  # 棋盘8*8
    queen(0)  # 开始放第一行
    print("总共有{}中解法".format(total))
