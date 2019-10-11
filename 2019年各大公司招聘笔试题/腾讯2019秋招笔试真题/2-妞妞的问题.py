"""

@file  : 2-妞妞的问题.py

@author: xiaolu

@time  : 2019-10-09

"""
"""
题目:
   有一个黑白相间的棋盘,　我们这里举个例子　5x5 (1, 1) 除为白 我们用0表示　黑色用1表示
然后给出两组坐标,一组坐标围城的长方形将其全部涂白,另一组将其全部涂黑,最后统计黑白的个数
"""
def build_table():
    # 这里举个例子 用10x10的表格　
    table = [[0 for i in range(10)] for j in range(10)]
    # 构造棋盘　
    for i in range(10):
        for j in range(10):
            if i % 2 == 0:
                if j % 2 == 0:
                    table[i][j] = 0
                else:
                    table[i][j] = 1
            else:
                if j % 2 == 0:
                    table[i][j] = 1
                else:
                    table[i][j] = 0
    return table


if __name__ == '__main__':
    # 1. 第一步: 构造棋盘
    table = build_table()
    print("一:构造的棋盘(0:白, 1:黑):")
    for _ in table:
        print(_)

    # 2. 第二步: 对应的两组坐标 这里我们之间给出
    anchor1_group = [(1, 3), (2, 6)]

    anchor2_group = [(2, 5), (6, 9)]

    # 3. 第三步: 根据第第一组坐标　将表格中对应为值涂白　也就是置成0
    for i in range(anchor1_group[0][0], anchor1_group[1][0]+1):
        for j in range(anchor1_group[0][1], anchor1_group[1][1]+1):
            table[i][j] = 0
    print("二:将坐标{}和坐标{}围成的长方形涂白以后的结果".format(anchor1_group[0], anchor1_group[1]))
    for _ in table:
        print(_)

    # 4. 第三步: 根据第二组坐标 将表格中对应的值涂黑 也就是置成1
    for i in range(anchor2_group[0][0], anchor2_group[1][0] + 1):
        for j in range(anchor2_group[0][1], anchor2_group[1][1] + 1):
            table[i][j] = 1
    print("二:将坐标{}和坐标{}围成的长方形涂白以后的结果".format(anchor2_group[0], anchor2_group[1]))
    for _ in table:
        print(_)

    # 5. 第四步: 统计此时此刻棋盘中黑色和白色的旗子各有多少个
    white_num = 0
    black_num = 0
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 0:
                white_num += 1
            else:
                black_num += 1
    print("此时此刻,黑色旗子有{}个,白色旗子有{}个".format(black_num, white_num))







