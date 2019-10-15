"""

@file  : 1-万万没想到之抓捕孔连顺.py

@author: xiaolu

@time  : 2019-10-09

"""
"""
题目描述:
    给定埋伏点的个数N, 埋伏点之间的最大距离, 我们只有三个队,有多少中埋伏的方案
解法:
    找出所有组合　然后筛选出符合条件的组合
"""
def fangan_num(anchor_pos, N, D):
    total_method = []
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                temp = [anchor_pos[i], anchor_pos[j], anchor_pos[k]]
                total_method.append(temp)

    # print(total_method)
    result = []
    for m in total_method:
        if (m[2] - m[0]) <= D:
            result.append(m)
    print("最终的方案:", result)


if __name__ == '__main__':
    N = 5   # 五个埋伏点
    D = 19   # 两个埋伏点之间最长距离不能超过19
    anchor_pos = [1, 10, 20, 30, 50]

    # self-method
    fangan_num(anchor_pos, N, D)
